"""One-time migration check, invoked only for the migration commit in CI."""
import hashlib, json, re, sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

class Article(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.text, self.images, self.links, self.code = [], [], [], []
        self.current_code = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'div' and a.get('id') == 'article-view':
            self.depth = 1
            return
        if not self.depth: return
        if tag == 'div': self.depth += 1
        if tag == 'img': self.images.append(a.get('src'))
        if tag == 'a' and 'href' in a: self.links.append(a['href'])
        if tag == 'pre': self.current_code = []
    def handle_endtag(self, tag):
        if not self.depth: return
        if tag == 'pre' and self.current_code is not None:
            self.code.append(''.join(self.current_code).rstrip('\n'))
            self.current_code = None
        if tag == 'div': self.depth -= 1
    def handle_data(self, data):
        if self.depth:
            self.text.append(data)
            if self.current_code is not None: self.current_code.append(data)

def digest(s): return hashlib.sha256(s.encode()).hexdigest()
root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site')
failed = []
items = json.loads(Path('tools/migration-baseline.json').read_text(encoding='utf-8'))
for item in items:
    file = root / unquote(item['url']).strip('/') / 'index.html'
    if not file.is_file():
        failed.append((item['file'], 'missing page')); continue
    p = Article(); p.feed(file.read_text(encoding='utf-8'))
    actual = {'text': digest(re.sub(r'[\s\u200b\ufeff]', '', ''.join(p.text))), 'images': p.images, 'links': p.links, 'code': [digest(c) for c in p.code]}
    for key in actual:
        if actual[key] != item[key]: failed.append((item['file'], key))
if failed:
    for file, key in failed: print(f'Migration mismatch: {file}: {key}')
    sys.exit(1)
print(f'All {len(items)} posts preserve their text, code, images and links.')
