# PlushTrap Current Catalog Authority — 2026-09

PlushTrap's current commerce authority is Stripe/site runtime. Historical Shopify exports and asset filenames are migration/reference evidence only.

## Verified publication seed

The branch now contains `public-current-catalog.json`, a deliberately small verified-live-storefront seed. It records only products whose current storefront identity, canonical URL, price/availability snapshot and buyer-language configuration were directly verified. The seed is not permission to infer other live catalog handles.

## Search ownership

Canonical PDPs own exact configuration intent: 1-hole balaclava / ski mask, 3-hole bunny-ear balaclava, 5-hole / customizable balaclava, and verified color/configuration terms. The shop/home surface owns broader kawaii streetwear, streetwear balaclava, kawaii ski mask and browse intent. Do not create doorway pages for adjective/color combinations.

## Sitemap status

A conservative sitemap now exists and `robots.txt` may advertise it. Sitemap membership is evidence-gated: homepage, shop, wholesale and verified canonical product URLs only. `scripts/audit-seo-authority.py` must reject any product sitemap URL absent from the verified current catalog seed.

This replaces the earlier blocker that said no sitemap should exist. The correct rule is: **a sitemap is allowed, but only from verified current authority.**

## Remaining extraction contract

Before another product enters sitemap, Product JSON-LD, Merchant Center/OpenAI feed projections or answer-engine product facts, verify stable current identity, Stripe/runtime sellability, exact canonical URL, current price/currency, current availability, literal configuration attributes, and current image URL.

Amazon identifiers remain separate channel identity. Duplicate/unresolved ASIN or SKU mappings must never become canonical site identity.

## ODR CNTRL comparison adopted

ODR CNTRL's useful pattern is an authority pipeline: independent query jobs, visible direct answers, claim boundaries, route-level schema, internal cluster links, changed-URL IndexNow submission, and a harsh completion bar that refuses to call source checks production proof. PlushTrap should copy that operating model while keeping fashion/product facts specific to its verified catalog.
