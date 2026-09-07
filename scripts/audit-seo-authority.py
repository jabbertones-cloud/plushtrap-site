#!/usr/bin/env python3
"""SEO/commerce authority guard for PlushTrap."""
from pathlib import Path
import json
import re
ROOT = Path(__file__).resolve().parents[1]
errors = []
raw_shopify = ROOT / 'data' / 'shopify-products-raw.json'
if raw_shopify.exists():
    for rel in ('docs/CURRENT-COMMERCE-AUTHORITY-2026-09.md', 'docs/CURRENT-CATALOG-AUTHORITY-2026-09.md'):
        text = (ROOT / rel).read_text()
        if 'historical' not in text.lower() or 'shopify' not in text.lower(): errors.append(f'{rel}: missing Shopify historical-only boundary')
for rel in ('llms.txt', 'docs/SEARCH-ANSWER-COMMERCE-CONTRACT.md', 'docs/SEO-AEO-BENCHMARK-2026-09.md'):
    text = (ROOT / rel).read_text()
    if 'Shopify' in text and not any(term in text for term in ('historical', 'not a current SEO authority', 'does not use Shopify')): errors.append(f'{rel}: Shopify reference lacks historical/non-authority boundary')
robots = (ROOT / 'robots.txt').read_text()
for crawler in ('Googlebot', 'Bingbot', 'OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot'):
    if f'User-agent: {crawler}' not in robots: errors.append(f'robots missing retrieval crawler {crawler}')
for crawler in ('GPTBot', 'Google-Extended', 'CCBot', 'ClaudeBot'):
    if not re.search(rf'User-agent: {re.escape(crawler)}\nDisallow: /', robots): errors.append(f'robots missing explicit training boundary for {crawler}')
catalog_path, sitemap_path = ROOT / 'public-current-catalog.json', ROOT / 'sitemap.xml'
if not catalog_path.exists(): errors.append('verified live catalog seed missing')
if not sitemap_path.exists(): errors.append('sitemap.xml missing')
if catalog_path.exists() and sitemap_path.exists():
    catalog = json.loads(catalog_path.read_text()); sitemap = sitemap_path.read_text(); locs = re.findall(r'<loc>([^<]+)</loc>', sitemap)
    if len(locs) != len(set(locs)): errors.append('sitemap contains duplicate URLs')
    if not all(url.startswith('https://plushtrap.com/') for url in locs): errors.append('sitemap contains non-canonical host')
    direct_urls = {p.get('url') for p in catalog.get('products', []) if p.get('url') and p.get('verification') == 'direct_pdp'}
    product_urls = {u for u in locs if '/shop/' in u}
    if not product_urls.issubset(direct_urls): errors.append('sitemap publishes a product without direct PDP verification')
    if 'https://plushtrap.com/shop/bbbm' not in product_urls: errors.append('verified BBBM canonical product URL missing from sitemap')
    for product in catalog.get('products', []):
        if product.get('verification') == 'live_related_product_link' and 'availability' in product:
            errors.append(f"related-link-only product must not assert availability: {product.get('sku')}")
    if catalog.get('authority') != 'verified-live-storefront-seed': errors.append('catalog seed authority marker invalid')
if 'Sitemap: https://plushtrap.com/sitemap.xml' not in robots: errors.append('robots must advertise the verified current sitemap')
for forbidden in ('data/products.json', 'myshopify.com'):
    if forbidden in robots: errors.append(f'robots leaks historical commerce authority: {forbidden}')

# Wholesale terms are executable commercial facts, not SEO copy. The current
# repository contains no verified wholesale authority record, so do not let
# durable discovery artifacts start projecting MOQ, margin, credit, lead-time,
# response-time, territory, or warehouse promises until such a source exists.
wholesale_authority = ROOT / 'data' / 'wholesale-authority.json'
commercial_patterns = [
    (re.compile(r'\$\s*\d+(?:\.\d+)?\s*(?:k\+?\s*)?MOQ', re.I), 'MOQ'),
    (re.compile(r'\b\d{1,3}(?:\s*[–-]\s*\d{1,3})?%\s*(?:margin|keystone)', re.I), 'margin'),
    (re.compile(r'\bNet\s*(?:15|30|45|60|90)\b', re.I), 'credit terms'),
    (re.compile(r'\b\d+\s*[–-]\s*\d+\s*days?\b|\b\d+\s*[–-]\s*\d+\s*weeks?\b', re.I), 'lead time'),
    (re.compile(r'\b(?:under|within|<)\s*48\s*h(?:ours?)?\b', re.I), 'response time'),
    (re.compile(r'\bships? from (?:a |the )?US warehouse\b', re.I), 'warehouse origin'),
]
if not wholesale_authority.exists():
    for rel in ('index.html', 'llms.txt', 'sitemap.xml', 'public-current-catalog.json'):
        p = ROOT / rel
        if not p.exists(): continue
        text = p.read_text()
        for pattern, label in commercial_patterns:
            if pattern.search(text): errors.append(f'{rel}: unverified wholesale {label} leaked into durable discovery surface')
else:
    authority = json.loads(wholesale_authority.read_text())
    if authority.get('status') != 'verified': errors.append('wholesale authority exists but is not verified')
    if not authority.get('verified_at') or not authority.get('source'): errors.append('verified wholesale authority requires verified_at and source provenance')

if errors: raise SystemExit('SEO authority audit failed:\n- ' + '\n- '.join(errors))
print('SEO authority audit passed')
