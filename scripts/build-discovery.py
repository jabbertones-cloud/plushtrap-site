#!/usr/bin/env python3
"""Generate search/answer discovery artifacts from the Shopify-derived product manifest.

This deliberately treats data/products.json as a projection of Shopify, not an
independent catalog authority. Re-run data/build-manifest.py first whenever the
Shopify export changes.
"""
from __future__ import annotations
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "products.json"
SITE = "https://plushtrap.com"

manifest = json.loads(DATA.read_text())
products = manifest.get("products", [])
active = [p for p in products if p.get("url") and p.get("title")]

# Sitemap uses canonical product URLs already supplied by the Shopify-derived manifest.
urls = [SITE + "/"] + sorted({p["url"] for p in active})
for url in urls:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.netloc != "plushtrap.com":
        raise SystemExit(f"non-canonical sitemap URL: {url}")

xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url in urls:
    xml.extend(["  <url>", f"    <loc>{url}</loc>", "  </url>"])
xml.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(xml) + "\n")

facts = {
    "schema_version": "1.0",
    "publisher": "PlushTrap",
    "canonical": SITE + "/",
    "source": manifest.get("source"),
    "source_generated_at": manifest.get("generated_at"),
    "product_count": len(active),
    "authority_note": "Current product pages and upstream Shopify catalog govern commercial facts. This file is a generated retrieval projection.",
    "products": [
        {
            "id": str(p.get("id")),
            "title": p.get("title"),
            "url": p.get("url"),
            "price_min": p.get("price_min"),
            "price_max": p.get("price_max"),
            "currency": p.get("currency"),
            "in_stock": p.get("in_stock"),
            "image": (SITE + "/" + p["image"].lstrip("/")) if p.get("image") else None,
            "tags": p.get("tags", []),
        }
        for p in active
    ],
}
(ROOT / "facts.json").write_text(json.dumps(facts, indent=2, ensure_ascii=False) + "\n")

print(f"generated sitemap.xml and facts.json for {len(active)} products")
