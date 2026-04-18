#!/usr/bin/env python3
"""Build clean product manifest + download feature images from Shopify dump."""
import json, os, re, urllib.request, urllib.parse, pathlib, datetime

ROOT = pathlib.Path('/Users/scottmanthey/claw-repos/plushtrap-site')
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
downloaded = 0
skipped = 0
failed = 0

for p in products:
    if p.get('status') != 'active':
        continue
    images = p.get('images', [])
    if not images:
        continue

    variants = p.get('variants', [])
    prices = [float(v.get('price', '0') or 0) for v in variants]
    price_min = min(prices) if prices else 0
    price_max = max(prices) if prices else 0
    in_stock = any(
        (v.get('inventory_quantity') or 0) > 0 or v.get('inventory_policy') == 'continue'
        for v in variants
    )

    slug = slugify(p['title'])
    title = p['title'].split(' \u2013 ')[0].split(' - ')[0].strip()
    tagline = ''
    if ' \u2013 ' in p['title']:
        tagline = p['title'].split(' \u2013 ', 1)[1].strip()
    elif ' - ' in p['title']:
        tagline = p['title'].split(' - ', 1)[1].strip()

    feat = images[0]
    parsed = urllib.parse.urlparse(feat['src'])
    ext = os.path.splitext(parsed.path)[1] or '.jpg'
    local_feat = f'assets/products/{slug}{ext}'
    dest = ROOT / local_feat

    if not dest.exists():
        try:
            req = urllib.request.Request(
                feat['src'], headers={'User-Agent': 'plushtrap-fetch/1.0'}
            )
            with urllib.request.urlopen(req, timeout=30) as r, open(dest, 'wb') as w:
                w.write(r.read())
            downloaded += 1
            print(f'  + {slug}{ext}  ({len(images)} total imgs)')
        except Exception as e:
            print(f'  ! failed {slug}: {e}')
            failed += 1
            continue
    else:
        skipped += 1

    manifest.append({
        'id': p['id'],
        'title': title,
        'tagline': tagline,
        'handle': p['handle'],
        'url': f"https://plushtrap.com/products/{p['handle']}",
        'vendor': p.get('vendor', ''),
        'product_type': p.get('product_type', ''),
        'tags': [t.strip() for t in (p.get('tags', '') or '').split(',') if t.strip()],
        'price_min': price_min,
        'price_max': price_max,
        'currency': 'USD',
        'in_stock': in_stock,
        'image': local_feat,
        'image_alt': feat.get('alt') or title,
        'image_w': feat.get('width'),
        'image_h': feat.get('height'),
        'all_images': [img['src'] for img in images],
        'total_images': len(images),
        'created_at': p.get('created_at'),
        'published_at': p.get('published_at'),
    })

manifest.sort(key=lambda x: x.get('published_at') or '', reverse=True)

out_json = ROOT / 'data' / 'products.json'
with out_json.open('w') as f:
    json.dump({
        'generated_at': datetime.datetime.utcnow().isoformat() + 'Z',
        'source': 'pluhtrap.myshopify.com',
        'total_active': len(manifest),
        'products': manifest,
    }, f, indent=2, ensure_ascii=False)

print('---')
print(f'active products  : {len(manifest)}')
print(f'images downloaded: {downloaded}')
print(f'images cached    : {skipped}')
print(f'images failed    : {failed}')
print(f'manifest         : {out_json}')
