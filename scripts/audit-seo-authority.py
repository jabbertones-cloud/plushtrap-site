#!/usr/bin/env python3
"""SEO/commerce authority guard for PlushTrap."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
errors = []

# The generated Shopify manifest was previously mistaken for current commerce
# truth. It must stay deleted unless it is explicitly historical-only.
legacy = ROOT / 'data' / 'products.json'
if legacy.exists():
    data = json.loads(legacy.read_text())
    if data.get('seo_authority') is not False or data.get('commerce_authority') is not False:
        errors.append('data/products.json must be explicitly non-authoritative')
    if data.get('historical_only') is not True:
        errors.append('legacy product dump must be historical_only')

# Raw Shopify source may remain for migration/media provenance, but discovery
# code must never project it as live price, stock, canonical URL or sitemap.
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

# Do not advertise a sitemap until it is generated from current Stripe-backed
# storefront authority. A dangling or Shopify-derived sitemap is worse than none.
if 'Sitemap:' in robots:
    errors.append('robots must not advertise a sitemap before current catalog authority exists')

for forbidden in ('data/products.json', 'myshopify.com'):
    if forbidden in robots:
        errors.append(f'robots leaks historical commerce authority: {forbidden}')

if errors:
    raise SystemExit('SEO authority audit failed:\n- ' + '\n- '.join(errors))
print('SEO authority audit passed')
