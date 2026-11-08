"""Source preservation and generated-route checks for this content migration."""
from collections import Counter
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
source = json.loads((ROOT/'docs/sources/JaJaSite_project_source_data.json').read_text(encoding='utf-8-sig'))
inventory = json.loads((ROOT/'docs/PROJECT_IMPORT_INVENTORY.json').read_text(encoding='utf-8'))
mapping = {entry['sourceSlug']: entry for entry in inventory}
def read_post(path):
    _, front, body = path.read_text(encoding='utf-8-sig').split('---', 2)
    data = {}
    for line in front.strip().splitlines():
        key, value = line.split(':', 1)
        data[key] = json.loads(value.strip())
    return data, body

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.elements=[]; self.feed(text)
    def handle_starttag(self, tag, attrs): self.elements.append((tag, dict(attrs)))

published = []
for path in (ROOT/'src/content/posts').glob('*.md'):
    if 'projectCategory:' in path.read_text(encoding='utf-8'):
        data, body = read_post(path)
        if not data.get('draft'): published.append((path.stem, data))
assert len(published) == 17
assert len({slug for slug, data in published}) == 17
assert Counter(data['projectCategory'] for slug,data in published) == {'robotics':6,'software':6,'embedded':5}
featured = sorted([(slug,data) for slug,data in published if data.get('featured')], key=lambda p:p[1]['featuredOrder'])
assert [slug for slug,data in featured] == ['fast-livo2-slam-global-relocalization','autonomous-tomato-harvesting','autonomous-navigation-object-search']
images = set(); videos = set(); documents = set(); hero_count = 0
for item in source['projects']:
    entry = mapping[item['slug']]
    path = ROOT/'src/content/posts'/f"{entry['existingSlug']}.md"
    data, body = read_post(path)
    output = ROOT/'dist'/entry['existingSlug']/'index.html'
    assert output.is_file(), f'Missing route {entry["existingSlug"]}'
    text = output.read_text(encoding='utf-8')
    if item['slug'] == 'fast-livo2':
        assert sha256(path.read_bytes()).hexdigest() == entry['previousBodySha256'], 'FAST-LIVO2 must stay byte-for-byte intact'
        continue
    assert data['cover'] == item['coverImageUrl'], item['slug']
    all_data = json.dumps(data, ensure_ascii=False)
    for url in item['imageUrls'] + item['resourceUrls'] + item['youtubeUrls'] + item['documentUrls']:
        assert url in all_data or url in body, f'Lost source URL: {item["slug"]}: {url}'
    images.update(item['imageUrls']); videos.update(item['youtubeUrls']); documents.update(item['documentUrls'])
    page = Page(text)
    if data.get('youtubeUrl'):
        hero_count += 1
        if item['youtubeUrls']:
            assert data['youtubeUrl'] == item['youtubeUrls'][0]
        assert text.index('<iframe') < text.index('<h1'), f'{item["slug"]}: video precedes title'
    else:
        assert 'post-full-image' in text, f'{item["slug"]}: show cover when no video exists'
    for tag, attrs in page.elements:
        if tag == 'a' and attrs.get('href') in [r['url'] for r in data['resources']]:
            assert attrs.get('target') == '_blank'
            assert 'noopener' in attrs.get('rel','') and 'noreferrer' in attrs.get('rel','')
drone = dict(published)['mini-camera-drone']
assert len(drone['gallery']) == 4 and not drone['featured']
assert not dict(published)['industrial-standards-ai-agent']['featured']
assert hero_count == 6
assert len(images) == 20 and len(videos) == 7 and len(documents) == 8
agent = dict(published)['industrial-standards-ai-agent']
assert agent['youtubeUrl'] == 'https://youtu.be/UfZgKLt_768?si=UbmXFmzrK2Mg4VCF'
assert any(r['url'] == 'https://youtu.be/ALsJD0Rnkuc?si=W2TTRqhqdLSPz6jS' for r in agent['resources'])
print(f'PASS: 17 unique routes; category counts 6/6/5; 3 featured in order; 20 original image URLs; 7 source video URLs + 2 report-discovered videos / 6 heroes; 8 original document URLs; unchanged FAST-LIVO2; drone consolidated.')
