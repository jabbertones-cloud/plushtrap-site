#!/usr/bin/env python3
"""SEO authority guard for PlushTrap."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
errors = []
legacy = ROOT / 'data' / 'products.json'
if legacy.exists():
    data = json.loads(legacy.read_text())
    if data.get('seo_authority') is not False or data.get('commerce_authority') is not False:
        errors.append('data/products.json must be explicitly non-authoritative')
    if data.get('historical_only') is not True:
        errors.append('legacy product dump must be historical_only')

for rel in ('llms.txt', 'docs/SEARCH-ANSWER-COMMERCE-CONTRACT.md', 'docs/SEO-AEO-BENCHMARK-2026-09.md'):
    text = (ROOT / rel).read_text()
    if 'Shopify' in text and not any(term in text for term in ('historical', 'not a current SEO authority', 'does not use Shopify')):
        errors.append(f'{rel}: Shopify reference lacks historical/non-authority boundary')

robots = (ROOT / 'robots.txt').read_text()
for crawler in ('Googlebot', 'Bingbot', 'OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot'):
    if f'User-agent: {crawler}' not in robots:
        errors.append(f'robots missing retrieval crawler {crawler}')

if errors:
    raise SystemExit('SEO authority audit failed:\n- ' + '\n- '.join(errors))
print('SEO authority audit passed')
