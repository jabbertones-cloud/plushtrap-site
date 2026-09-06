# Search, Answer, and Commerce Publication Contract

Verified: 2026-09-05

## Principle

Search eligibility, answer-engine retrieval, merchant-feed eligibility, and agentic checkout are separate capabilities. Passing one never proves another.

## Canonical authority order

1. Current visible canonical product page and canonical catalog authority.
2. Matching Product/Offer structured data.
3. Merchant/feed projections generated from the same authority.
4. Machine facts and question registries generated from that authority.
5. `llms.txt` and other ancillary discovery files.

No lower layer may silently override a higher layer.

## Google

Google AI Overviews and AI Mode use normal Search foundations. Do not invent AI-only schema or treat `llms.txt` as a ranking requirement. Keep pages crawlable, indexable, internally linked, useful, and ensure structured data matches visible content. For ecommerce, combine Product structured data with Merchant Center product data and maximize truthful attribute completeness.

## Microsoft/Bing

Keep Bingbot crawlable and maintain a valid sitemap. Use IndexNow for changed canonical URLs when the production host/key are verified. Measure AI citations/cited URLs/grounding-query data when available rather than treating successful submission as proof of Copilot visibility.

## OpenAI

Keep OAI-SearchBot and user-requested ChatGPT retrieval crawlable. Merchant feeds are a separate commerce integration and must be generated from canonical product authority using the current OpenAI feed contract. Do not equate GPTBot training permission with ChatGPT Search eligibility.

## Perplexity

Keep PerplexityBot crawlable for public canonical content while private/cart/checkout/API surfaces remain excluded.

## Agentic commerce

Do not publish a Google UCP profile or claim native agentic checkout until merchant eligibility/onboarding, advertised capabilities, endpoints, and conformance are real. Readiness code must remain distinguishable from live capability.

## Release gates

A release should fail when visible product facts, structured data, feeds, sitemap URLs, or ancillary machine files disagree on stable identity or commercial facts. Product feeds should carry rich truthful attributes and product Q&A where supported, not merely title/price/image.
