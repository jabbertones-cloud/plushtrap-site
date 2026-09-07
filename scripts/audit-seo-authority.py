#!/usr/bin/env python3
"""SEO/commerce authority guard for PlushTrap."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
errors = []

legacy = ROOT / 'data' / 'products.json'
if legacy.exists():
    data = json.loads(legacy.read_text())
    if data.get('seo_authority') is not False or data.get('commerce_authority') is not False:
        errors.append('data/products.json must be explicitly non-authoritative')
    if data.get('historical_only') is not True:
        errors.append('legacy product dump must be historical_only')

raw_shopify = ROOT / 'data' / 'shopify-products-raw.json'
if raw_shopify.exists():
    for rel in ('docs/CURRENT-COMMERCE-AUTHORITY-2026-09.md', 'docs/CURRENT-CATALOG-AUTHORITY-2026-09.md'):
        text = (ROOT / rel).read_text()
        if 'historical' not in text.lower() or 'shopify' not in text.lower():
            errors.append(f'{rel}: missing Shopify historical-only boundary')

for rel in ('llms.txt', 'docs/SEARCH-ANSWER-COMMERCE-CONTRACT.md', 'docs/SEO-AEO-BENCHMARK-2026-09.md'):
    text = (ROOT / rel).read_text()
    if 'Shopify' in text and not any(term in text for term in ('historical', 'not a current SEO authority', 'does not use Shopify')):
        errors.append(f'{rel}: Shopify reference lacks historical/non-authority boundary')

robots = (ROOT / 'robots.txt').read_text()
for crawler in ('Googlebot', 'Bingbot', 'OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot'):
    if f'User-agent: {crawler}' not in robots:
        errors.append(f'robots missing retrieval crawler {crawler}')
for crawler in ('GPTBot', 'Google-Extended', 'CCBot', 'ClaudeBot'):
    block = re.search(rf'User-agent: {re.escape(crawler)}\nDisallow: /', robots)
    if not block:
        errors.append(f'robots missing explicit training boundary for {crawler}')

catalog_path = ROOT / 'public-current-catalog.json'
sitemap_path = ROOT / 'sitemap.xml'
if not catalog_path.exists():
    errors.append('verified live catalog seed missing')
if not sitemap_path.exists():
    errors.append('sitemap.xml missing')

if catalog_path.exists() and sitemap_path.exists():
    catalog = json.loads(catalog_path.read_text())
    sitemap = sitemap_path.read_text()
    locs = re.findall(r'<loc>([^<]+)</loc>', sitemap)
    if len(locs) != len(set(locs)):
        errors.append('sitemap contains duplicate URLs')
    if not all(url.startswith('https://plushtrap.com/') for url in locs):
        errors.append('sitemap contains non-canonical host')
    verified_urls = {p.get('url') for p in catalog.get('products', []) if p.get('url')}
    product_urls = {u for u in locs if '/shop/' in u}
    if not product_urls.issubset(verified_urls):
        errors.append('sitemap contains product URL not proven by verified live catalog')
    if 'https://plushtrap.com/shop/bbbm' not in product_urls:
        errors.append('verified BBBM canonical product URL missing from sitemap')
    if catalog.get('authority') != 'verified-live-storefront-seed':
        errors.append('catalog seed authority marker invalid')

if 'Sitemap: https://plushtrap.com/sitemap.xml' not in robots:
    errors.append('robots must advertise the verified current sitemap')
for forbidden in ('data/products.json', 'myshopify.com'):
    if forbidden in robots:
        errors.append(f'robots leaks historical commerce authority: {forbidden}')

if errors:
    raise SystemExit('SEO authority audit failed:\n- ' + '\n- '.join(errors))
print('SEO authority audit passed')
