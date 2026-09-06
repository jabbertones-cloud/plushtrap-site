#!/usr/bin/env python3
"""LEGACY IMPORT UTILITY ONLY.

PlushTrap current commerce is Stripe-only. This script reads a historical Shopify
export solely to preserve/migrate old media and catalog references. Its output is
NOT current SEO/AEO authority and MUST NOT drive sitemap, structured data,
Merchant Center feeds, llms files, facts, availability, or current pricing.

Current search/discovery publication must use the live PlushTrap site/product
registry reconciled with Stripe-backed current product/price identifiers.
"""
import json, os, re, urllib.request, urllib.parse, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / 'data' / 'shopify-products-raw.json'
OUT_DIR = ROOT / 'assets' / 'products'
OUT_DIR.mkdir(parents=True, exist_ok=True)


def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return re.sub(r'-+', '-', s).strip('-')[:60]


with SRC.open() as f:
    data = json.load(f)

products = data['products']
manifest = []
downloaded = skipped = failed = 0
for p in products:
    if p.get('status') != 'active' or not p.get('images'):
        continue
    images = p['images']
    slug = slugify(p['title'])
    title = p['title'].split(' – ')[0].split(' - ')[0].strip()
    feat = images[0]
    parsed = urllib.parse.urlparse(feat['src'])
    ext = os.path.splitext(parsed.path)[1] or '.jpg'
    local_feat = f'assets/products/{slug}{ext}'
    dest = ROOT / local_feat
    if not dest.exists():
        try:
            req = urllib.request.Request(feat['src'], headers={'User-Agent': 'plushtrap-legacy-import/1.0'})
            with urllib.request.urlopen(req, timeout=30) as r, open(dest, 'wb') as w:
                w.write(r.read())
            downloaded += 1
        except Exception as e:
            print(f'! failed legacy media {slug}: {e}')
            failed += 1
            continue
    else:
        skipped += 1
    manifest.append({
        'legacy_id': p['id'], 'title': title, 'legacy_handle': p.get('handle'),
        'image': local_feat, 'all_images': [img['src'] for img in images],
        'historical_only': True,
    })

out_json = ROOT / 'data' / 'products.json'
with out_json.open('w') as f:
    json.dump({
        'generated_at': datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00', 'Z'),
        'source': 'historical Shopify export; NOT CURRENT AUTHORITY',
        'seo_authority': False,
        'commerce_authority': False,
        'historical_only': True,
        'products': manifest,
    }, f, indent=2, ensure_ascii=False)
print(f'legacy references: {len(manifest)}; downloaded={downloaded}; cached={skipped}; failed={failed}')
