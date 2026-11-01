(() => {
  'use strict';
  const body = document.querySelector('#article-view');
  if (!body) return;
  const http = value => { try { const u = new URL(value, location.href); return /^https?:$/.test(u.protocol) ? u.href : ''; } catch { return ''; } };
  const items = [];
  function render(node, url, data = {}) {
    const a = document.createElement('a');
    a.href = url; a.className = 'link-preview';
    const text = document.createElement('span'); text.className = 'link-preview-text';
    const title = document.createElement('strong'); title.textContent = data.title || new URL(url).hostname;
    const host = document.createElement('span'); host.className = 'link-preview-host'; host.textContent = new URL(url).hostname;
    text.append(title);
    if (data.description?.trim()) { const desc = document.createElement('span'); desc.className = 'link-preview-description'; desc.textContent = data.description; text.append(desc); }
    text.append(host); a.append(text);
    const image = http(data.image || '');
    if (data.image && image) {
      const img = document.createElement('img'); img.alt = ''; img.loading = 'lazy'; img.src = image;
      img.addEventListener('error', () => { img.remove(); a.classList.remove('has-image'); });
      a.classList.add('has-image'); a.prepend(img);
    }
    node.replaceWith(a); return a;
  }
  body.querySelectorAll('figure[data-ke-type="opengraph"]').forEach(figure => {
    const url = http(figure.querySelector('a')?.getAttribute('href'));
    if (!url) return;
    const data = {title: figure.dataset.ogTitle, description: figure.dataset.ogDescription, image: figure.dataset.ogImage};
    const previous = figure.previousElementSibling;
    // Tistory often stores the same URL immediately before its preview.
    if (previous?.tagName === 'P' && previous.children.length === 1 && previous.firstElementChild.tagName === 'A' && previous.textContent.trim() === previous.firstElementChild.textContent.trim() && http(previous.firstElementChild.getAttribute('href')) === url) previous.remove();
    items.push({node:render(figure,url,data),url,data});
  });
  body.querySelectorAll('p').forEach(p => {
    if (p.closest('figure,pre,blockquote,li,table,.no-preview')) return;
    const a = p.firstElementChild;
    const raw = p.textContent.trim();
    let url, title;
    if (p.children.length === 1 && a.tagName === 'A' && raw === a.textContent.trim() && !a.querySelector('img') && !a.classList.contains('no-preview')) { url=http(a.getAttribute('href')); title=raw; }
    else if (!p.children.length && /^https?:\/\/\S+$/.test(raw)) { url=http(raw); }
    if (!url || new URL(url).origin === location.origin) return;
    const data = {title: title && !/^https?:\/\//.test(title) ? title : new URL(url).hostname};
    items.push({node:render(p,url,data),url,data});
  });
  if (items.length) fetch('/assets/link-previews.json').then(r=>r.ok?r.json():{}).then(index=>{
    items.forEach(item=>{const info=index[item.url];if(info)item.node=render(item.node,item.url,{...item.data,...info});});
  }).catch(()=>{});
})();
