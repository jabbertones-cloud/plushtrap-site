# PlushTrap Current Catalog Authority — 2026-09

PlushTrap's current commerce authority is Stripe/site runtime, not historical Shopify exports and not the filenames under `assets/products/`.

The repository contains many useful product-image filenames with strong buyer-language clues, including examples such as:

- Black Brim 1-Hole Balaclava
- Black Bunski 3-Hole Balaclava / bunny-ear ski mask
- Blue Bunski 3-Hole Balaclava / bunny-ear ski mask
- Camo Bunski Balaclava / bunny-ear ski mask
- Distressed Black Bunski Balaclava / 1-hole ski mask
- DIY Black 5-Hole Balaclava / customizable ski mask
- fleece bunny beanies

These filenames are evidence that the product concepts/assets exist in the repo. They are **not** evidence of current price, inventory, Stripe status, canonical URL, color availability, restock policy or current collection membership.

## Search ownership

Once current Stripe/runtime authority is extracted, canonical PDPs should own exact configuration queries:

- 1-hole balaclava / 1-hole ski mask
- 3-hole bunny-ear balaclava / bunny-ear ski mask
- 5-hole balaclava / customizable ski mask
- black bunny-ear ski mask
- blue bunny-ear ski mask
- camo bunny-ear ski mask

The collection/home surface can own broader `kawaii streetwear`, `streetwear balaclava`, `kawaii ski mask`, and browse intent. Do not generate a landing page for every adjective/color combination.

## Current blockers

- `index.html` still advertises `Lovers Lane Drop / Live Now`, `Limited runs. No restocks.`, and named Lovers Lane bundles in metadata without a current Stripe/runtime reconciliation.
- No `data/products.json` exists on the active branch, which is preferable to reviving a stale Shopify-derived authority file.
- `robots.txt` correctly omits a sitemap until canonical current product URLs can be generated from verified authority.

## Required extraction contract

A future canonical catalog projection must require, per product:

1. stable current product identity
2. current Stripe/runtime sellability
3. current canonical public URL
4. current price source
5. current availability source
6. exact configuration/title
7. current image URL

Only after those fields reconcile should the product enter sitemap, Product JSON-LD, Merchant/OpenAI feed projections or answer-engine product facts.
