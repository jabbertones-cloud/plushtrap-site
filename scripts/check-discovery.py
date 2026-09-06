#!/usr/bin/env python3
"""Fail on common false-positive search/discovery states."""
from __future__ import annotations
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "data/products.json").read_text())
facts = json.loads((ROOT / "facts.json").read_text()) if (ROOT / "facts.json").exists() else None
sitemap = (ROOT / "sitemap.xml").read_text() if (ROOT / "sitemap.xml").exists() else ""
robots = (ROOT / "robots.txt").read_text()
llms = (ROOT / "llms.txt").read_text()
errors = []

if not facts:
    errors.append("facts.json missing: run scripts/build-discovery.py")
else:
    source_products = [p for p in manifest.get("products", []) if p.get("url") and p.get("title")]
    if facts.get("product_count") != len(source_products):
        errors.append("facts product_count drift")
    fact_urls = {p.get("url") for p in facts.get("products", [])}
    source_urls = {p.get("url") for p in source_products}
    if fact_urls != source_urls:
        errors.append("facts product URL set drift")
    for p in facts.get("products", []):
        if p.get("currency") != "USD":
            errors.append(f"unexpected currency for {p.get('id')}")
        if not isinstance(p.get("in_stock"), bool):
            errors.append(f"availability is not boolean for {p.get('id')}")

locs = re.findall(r"<loc>([^<]+)</loc>", sitemap)
if len(locs) != len(set(locs)):
    errors.append("duplicate sitemap URLs")
for url in locs:
    u = urlparse(url)
    if u.scheme != "https" or u.netloc != "plushtrap.com" or u.query or u.fragment:
        errors.append(f"non-canonical sitemap URL: {url}")

for agent in ("Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot"):
    if f"User-agent: {agent}" not in robots:
        errors.append(f"retrieval crawler missing: {agent}")
for agent in ("GPTBot", "Google-Extended", "CCBot", "ClaudeBot"):
    block = re.search(rf"User-agent: {re.escape(agent)}\n([^\n]*\n)*?Disallow: /", robots)
    if not block:
        errors.append(f"training crawler not explicitly separated: {agent}")
if "not an independent source of commercial truth" not in llms:
    errors.append("llms authority boundary missing")

if errors:
    raise SystemExit("discovery contract failed:\n- " + "\n- ".join(errors))
print("discovery contract passed")
