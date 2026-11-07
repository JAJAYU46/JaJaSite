"""Check the built portfolio using only Python's standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
BASE = '/JaJaSite/'

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.elements = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))

assert DIST.is_dir(), 'Run pnpm run build first.'
errors = []
pages = list(DIST.rglob('*.html'))
checked = 0
for path in pages:
    if path.relative_to(DIST).parts[0] == 'admin':
        continue  # Retained template CMS is not a portfolio publishing route.
    page = Page(path.read_text(encoding='utf-8'))
    for tag, attrs in page.elements:
        for key in ('href', 'src'):
            value = attrs.get(key, '')
            url = urlsplit(value)
            if not value or url.scheme or url.netloc or value.startswith('#'):
                continue
            if not url.path.startswith(BASE):
                errors.append(f'{path.relative_to(DIST)}: missing base: {value}')
                continue
            target = DIST / unquote(url.path[len(BASE):])
            if not (target.is_file() or (target / 'index.html').is_file()):
                errors.append(f'{path.relative_to(DIST)}: missing target: {value}')
            checked += 1
        if tag == 'img' and ('alt' not in attrs or (not attrs['alt'] and attrs.get('aria-hidden') != 'true')):
            errors.append(f'{path}: image without alt text')

home = Page((DIST / 'index.html').read_text(encoding='utf-8'))
featured = [a for t,a in home.elements if 'featured-project-link' in a.get('class','').split()]
assert len(featured) == 3, f'Expected three featured projects, got {len(featured)}'
assert not any('industrial-standards' in a['href'] or 'mini-camera-drone' in a['href'] for a in featured)
index = Page((DIST / 'projects/index.html').read_text(encoding='utf-8'))
cards = [a for t,a in index.elements if t == 'article' and 'post-card' in a.get('class','').split()]
assert len(cards) >= 17, f'Expected at least 17 project cards, got {len(cards)}'
for slug in ['autonomous-tomato-harvesting', 'autonomous-navigation-object-search']:
    text = (DIST / slug / 'index.html').read_text(encoding='utf-8')
    page = Page(text)
    iframe = next(a for t,a in page.elements if t == 'iframe')
    assert text.index('<iframe') < text.index('<h1'), f'{slug}: video must precede title'
    assert iframe.get('loading') == 'lazy'
    assert iframe['src'].startswith('https://www.youtube-nocookie.com/embed/')
    assert 'autoplay' not in iframe['src']
assert not (DIST / 'welcome/index.html').exists(), 'Template drafts must not be published'
fast = (DIST / 'fast-livo2-slam-global-relocalization/index.html').read_text(encoding='utf-8')
assert '<iframe' not in fast, 'Do not invent a FAST-LIVO2 video URL'
assert 'fast-livo2-concept.svg' in fast, 'Keep the conceptual diagram available'
for slug in ['fast-livo2-slam-global-relocalization', 'autonomous-tomato-harvesting']:
    page = Page((DIST / slug / 'index.html').read_text(encoding='utf-8'))
    assert any(t == 'nav' and a.get('aria-label') == 'Breadcrumb' for t, a in page.elements)
    assert any(t == 'a' and a.get('rel') in ['prev','next'] for t, a in page.elements)
assert not errors, '\n'.join(errors)
print(f'PASS: {len(pages)-1} portfolio HTML pages, {len(cards)} project cards, {checked} internal links/assets, 3 featured cards, and both video heroes.')
