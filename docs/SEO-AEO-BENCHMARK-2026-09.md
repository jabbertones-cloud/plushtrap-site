# PlushTrap SEO/AEO Benchmark — September 2026

This branch is for public search and answer-engine discovery. PlushTrap uses Stripe for checkout; historical Shopify data is not a current SEO authority.

## Google

- AI Overviews and AI Mode use ordinary Search foundations. Prioritize crawl/index eligibility, canonical URLs, unique useful visible text, internal linking, image context, and structured data that agrees with the page.
- `llms.txt` is optional ancillary infrastructure, not a Google ranking mechanism.
- Product structured data and Merchant Center data should complement each other.
- For apparel, maximize truthful variant/attribute completeness: product type, color, material, size/configuration, bundle quantity, images, stable identifiers, price, and availability where known.
- Merchant Center's newer conversational-shopping fields such as detailed product attributes and product Q&A should be generated only from supported visible product facts.

## Microsoft/Bing

- Bingbot must be able to crawl canonical public pages.
- Add IndexNow only for materially changed canonical URLs and only after production key/host behavior is verified.
- Measure Copilot/Bing AI visibility through AI Performance (citations, cited pages, grounding queries, intents/topics/citation share where available), not through ordinary ranking impressions alone.

## OpenAI / Perplexity

- OAI-SearchBot, ChatGPT-User, and PerplexityBot should reach public canonical product/content pages.
- GPTBot training permission is independent.
- Optional `llms.txt` should route systems toward canonical content rather than duplicate it.

## PlushTrap content target

Build high-information-gain product/category content around actual products and buyer questions rather than programmatic keyword clones. Important apparel intents include what the item is, construction/material, color/variant, fit/sizing, configuration or pack quantity, use/style context, care where known, and how variants differ.
