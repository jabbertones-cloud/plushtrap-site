# PlushTrap Current Commerce Authority Gate — 2026-09

Public SEO/AEO product facts come from the current PlushTrap storefront/product registry reconciled with Stripe-backed commerce identifiers. Historical Shopify exports are migration references only and may not supply current price, inventory, canonical URL, sitemap membership, Product/Offer JSON-LD or merchant-feed facts.

## Publishable product contract

A product can enter a discovery/commerce projection only when its canonical public URL, current name, stable identifier, sellable state, current price/currency, literal configuration attributes, current image and Stripe-backed checkout mapping are verified.

Amazon identity is separate. Duplicate or unresolved ASIN/SKU mappings are not canonical site identity.

## Search-intent ownership

Exact configuration language belongs on canonical PDPs. Broader category/editorial surfaces may own streetwear balaclava, fashion balaclava, cute/kawaii balaclava, balaclava outfit and styling intent, but must link to current canonical products and must not become color/query clones.

## Release gate

A conservative sitemap is now permitted because `public-current-catalog.json` supplies a verified seed. Every product URL in the sitemap must be present in that seed and pass `scripts/audit-seo-authority.py`. Expanding the sitemap requires expanding verified authority first. A historical product dump passing a schema check is never publication proof.

Adopt the ODR CNTRL completion rule: code path + executable audit + live/deployed proof when available + failure-mode checks + status documentation. Until all applicable layers are proven, report the surface as not fully complete.
