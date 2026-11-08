"""Anonymous access audit. Preserves original URLs; never saves remote images."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/sources/JaJaSite_project_source_data.json'

def check(item):
    try:
        request = Request(item['url'], headers={'User-Agent': 'Mozilla/5.0 (compatible; JaJaSiteContentAudit/1.0)'})
        with urlopen(request, timeout=20) as response:
            sample = response.read(32768)
            content_type = response.headers.get('Content-Type', '')
            item.update(status=response.status, contentType=content_type, finalUrl=response.url)
            if item['kind'] == 'image':
                image_signature = sample.startswith((b'\xff\xd8\xff', b'\x89PNG', b'GIF8', b'RIFF'))
                item['result'] = 'anonymous-image-response' if content_type.startswith('image/') and image_signature else 'not-an-image-response'
            else:
                html = sample.decode('utf-8', 'replace')
                title = re.search(r'<title[^>]*>(.*?)</title>', html, re.S | re.I)
                item['pageTitle'] = re.sub(r'\s+', ' ', title.group(1)).strip()[:200] if title else ''
                item['result'] = 'login-required' if 'accounts.google.com' in response.url else 'http-response-only-not-content-verification'
    except HTTPError as error:
        item.update(status=error.code, result='http-error', error=str(error))
    except Exception as error:
        item.update(result='unverified-network-error', error=str(error))
    return item

def main():
    source = json.loads(SOURCE.read_text(encoding='utf-8-sig'))
    items = {}
    for project in source['projects']:
        for kind, key in [('image', 'imageUrls'), ('document', 'documentUrls'), ('video', 'youtubeUrls')]:
            for url in project[key]:
                if url in items:
                    items[url]['projects'].append(project['title'])
                else:
                    items[url] = {'url': url, 'kind': kind, 'projects': [project['title']]}
    old_site = 'https://jajayu46.github.io/JaJaWebsite/JaJaWeb'
    items[old_site] = {'url': old_site, 'kind': 'website', 'projects': ["JaJa's Original Website"]}
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(check, items.values()))
    report = {
        'checkedAt': datetime.now(timezone.utc).isoformat(),
        'method': 'Anonymous HTTP GET without cookies or credentials; up to 32 KB read per URL. No images saved. HTTP success alone does not verify document content, browser image rendering, or video playback.',
        'resources': results,
    }
    (ROOT / 'docs/PROJECT_MEDIA_AUDIT.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    counts = {}
    for entry in results:
        counts[entry['result']] = counts.get(entry['result'], 0) + 1
        print(f"{entry['kind']}: {entry['result']} ({entry.get('status', 'no HTTP response')}) — {entry['projects'][0]}")
    print(json.dumps(counts))

if __name__ == '__main__':
    main()
