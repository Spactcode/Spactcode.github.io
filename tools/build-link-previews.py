"""Collect standalone link metadata during publication; failure leaves a usable link."""
import concurrent.futures, ipaddress, json, socket, sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.urls=set(); self.p=None; self.blocked=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag in ('figure','pre','blockquote','li','table'): self.blocked+=1
        if tag=='p' and not self.blocked: self.p={'text':'','links':[], 'other':False}
        elif self.p is not None:
            if tag=='a': self.p['links'].append(a.get('href',''))
            else: self.p['other']=True
        if tag=='figure' and a.get('data-ke-type')=='opengraph': self.urls.add(a.get('data-og-url',''))
    def handle_data(self, text):
        if self.p is not None: self.p['text']+=text
    def handle_endtag(self, tag):
        if tag=='p' and self.p is not None:
            p=self.p; self.p=None
            if not p['other']:
                if len(p['links'])==1: self.urls.add(p['links'][0])
                elif not p['links'] and p['text'].strip().startswith(('https://','http://')) and not any(c.isspace() for c in p['text'].strip()): self.urls.add(p['text'].strip())
        if tag in ('figure','pre','blockquote','li','table'): self.blocked=max(0,self.blocked-1)

class Meta(HTMLParser):
    def __init__(self): super().__init__(); self.data={}; self.title=False; self.text=''
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='title': self.title=True
        if tag=='meta':
            key=a.get('property',a.get('name','')).lower(); value=a.get('content','').strip()
            if value: self.data.setdefault(key,value)
    def handle_endtag(self, tag):
        if tag=='title': self.title=False
    def handle_data(self, value):
        if self.title: self.text+=value

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs): return None

def public(url):
    u=urlsplit(url)
    if u.scheme not in ('http','https') or not u.hostname or u.username or u.password: return False
    return all(ipaddress.ip_address(a[4][0]).is_global for a in socket.getaddrinfo(u.hostname,u.port or (443 if u.scheme=='https' else 80)))

def preview(url):
    try:
        current=url; opener=build_opener(NoRedirect())
        for _ in range(5):
            if not public(current): return url,{}
            try: response=opener.open(Request(current,headers={'User-Agent':'Mozilla/5.0 (compatible; LaonBlogPreview/1.0)'}),timeout=6)
            except Exception as e:
                if getattr(e,'code',None) in (301,302,303,307,308): current=urljoin(current,e.headers['Location']); continue
                raise
            with response:
                if 'html' not in response.headers.get('Content-Type',''): return url,{}
                html=response.read(512000).decode(response.headers.get_content_charset() or 'utf-8',errors='replace')
            meta=Meta(); meta.feed(html); d=meta.data
            result={'title':(d.get('og:title') or meta.text).strip()[:300], 'description':(d.get('og:description') or d.get('description',''))[:600]}
            image=d.get('og:image') or d.get('twitter:image')
            if image:
                image=urljoin(current,image)
                if public(image): result['image']=image
            return url,{k:v for k,v in result.items() if v}
    except Exception: pass
    return url,{}

root=Path(sys.argv[1] if len(sys.argv)>1 else '_site'); urls=set()
for page in (root/'entry').rglob('index.html'):
    parser=Links(); parser.feed(page.read_text(encoding='utf-8')); urls.update(parser.urls)
urls=sorted(u for u in urls if u.startswith(('https://','http://')) and urlsplit(u).hostname not in ('laoncode.github.io','spactcode.github.io'))
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool: data=dict(pool.map(preview,urls))
(root/'assets'/'link-previews.json').write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
print(f'Link previews: {sum(bool(v) for v in data.values())}/{len(urls)}; others use compact fallback links.')
