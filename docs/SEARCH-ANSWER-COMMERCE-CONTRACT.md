# Search, Answer, and Commerce Publication Contract

Verified: 2026-09-05

## Principle
Search eligibility, answer-engine retrieval, merchant-feed eligibility, and agentic checkout are separate capabilities. Passing one never proves another.

## PlushTrap authority boundary
PlushTrap does not use Shopify for current commerce. Stripe is the money-moving commerce authority. The current site/product registry owns descriptive product identity/content; Stripe-backed product/price identifiers own current checkout economics. Historical Shopify exports and identifiers are migration/reference evidence only and are forbidden as inputs to current SEO/AEO commerce projections.

## Canonical publication order
1. Current site/product registry for canonical identity/content plus Stripe-backed current product/price authority.
2. Visible canonical product surface.
3. Matching Product/Offer structured data.
4. Merchant/feed projections generated only after authority reconciliation.
5. Machine facts and question registries from the same reconciled authority.
6. `llms.txt` and ancillary discovery files.

No lower layer may silently override a higher layer. A historical catalog dump can never become current authority merely because it is structured.

## Platform rules
- Google: normal Search foundations remain primary. Keep visible content and structured data aligned; combine Product structured data with Merchant Center data and truthful attribute completeness.
- Microsoft/Bing: keep Bingbot crawlable, maintain a valid sitemap, use IndexNow only with verified production host/key handling, and measure actual AI citations, cited URLs, grounding queries, intents, topics, and citation share when available.
- OpenAI: keep OAI-SearchBot and ChatGPT-User crawlable. Merchant feeds are separate and must be generated from reconciled current authority. GPTBot training permission is independent.
- Perplexity: keep PerplexityBot crawlable for public canonical content while private/cart/checkout/API surfaces remain excluded.
- Agentic commerce: do not publish a UCP profile or claim native checkout until eligibility/onboarding, endpoints, advertised capabilities, and conformance are real.

## Release gates
Publication must fail when visible product facts, Stripe-backed price authority, structured data, feeds, sitemap URLs, or ancillary machine files disagree on stable identity or commercial facts. Product feeds should carry rich truthful attributes and product Q&A where supported, not merely title/price/image.
