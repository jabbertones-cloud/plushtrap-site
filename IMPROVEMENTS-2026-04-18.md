# Plushtrap (static brand site) — Design Improvement Report

**Source audit:** `SITE-AUDIT-2026-04-18-v4.md` §1. Current weighted score **7.64** against Awwwards (Design 40 / Usability 30 / Creativity 20 / Content 10). Tier: **SOTD** (barely clears the 7.5 floor).

**Target:** 7.95 weighted — comfortable SOTD that survives a weak-day jury rotation.

**Benchmark set:** Baggu × Miffy, Online Ceramics, Aimé Leon Dore, YUNUENY, Sandy Liang.

## Constraints (do not change)

- Fraunces variable axes (`opsz`, `SOFT`, `WONK`) + Archivo Black + Space Mono — this is the signature type contract, already jury-legible.
- `--ink / --bone / --lemon / --bubble / --plum` palette — the duality is the brand.
- Static HTML + Cloudflare Pages host — do not port to a framework until the commerce surface (§2) inherits this identity.
- "Limited runs. No restocks." scarcity posture — part of the drop-culture DNA.

## Prioritized actions

### 1. Custom-cursor accessibility fallback — SHIPPED 2026-04-18

Done in this pass. Added `@media (scripting: none)` + `.no-js` class pattern to `index.html` so the custom cursor disables cleanly for: touch devices (already covered), reduced-motion users (already covered), JS-disabled desktop users (newly covered), and any assistive tech that strips JS. Removes the v4 Usability deduction cited for `cursor: none` without fallback.

**Verify on re-audit:** Disable JS in devtools → `body { cursor: auto }` active, `.cursor-dot` not rendered, buttons show `cursor: pointer`. Expected Usability 6.8 → 7.4.

### 2. Campaign page per named bundle — Baggu × Miffy pattern

Each Lovers Lane bundle ("Bonnie & Clyde," "Cuffed & Cozy," "Red Flag," "Kawaii Crush") gets a dedicated `/drops/lovers-lane/bonnie-and-clyde/` page structured as:

- Campaign headline (Fraunces 7xl, `WONK=1`, `SOFT=100`)
- 3–5 editorial spreads (square + portrait mix, cream-on-lemon backgrounds)
- 1 story paragraph (Space Mono eyebrow → Fraunces body, 60ch max)
- Looks-in-this-drop grid (cross-link to siblings)
- Shop the look: anchor buttons to the §2 commerce routes

Template file: `campaign.html` — single HTML template, content driven by a flat JSON of `{ bundle, headline, story, spreads[] }`. One author can ship a campaign page in 20 minutes with photos in hand.

**Mechanism of lift:** Content dimension is currently 7.2 (strong drop narrative but no campaign depth). Shipping 4 campaign pages moves Content to ~8.4 by the Awwwards Content-10 rubric (storytelling completeness).
**Delta:** +0.12 weighted.
**Competitor anchor:** Baggu × Miffy ships a full campaign page per collab (see `baggu.com/pages/miffy`) — same pattern.

### 3. Shoppable countdown block on hero — Aimé Leon Dore / Kith pattern

A single row above the fold: `NEXT DROP · [named campaign] · [countdown DD:HH:MM:SS] · Set Reminder`. Static HTML can do this with a `data-drop-at="2026-MM-DDTHH:MM:SSZ"` attribute + a 20-line `setInterval` updater. Until the next drop is scheduled, show the most-recent drop's "sold out" state in the same slot — the slot must never go empty.

**Mechanism:** Creativity 20 is currently 8.0. Scarcity-as-UI is the award-earning move in drop-culture category; an editorial countdown pushes to 8.6+.
**Delta:** +0.12 weighted.
**Competitor anchor:** Aimé Leon Dore's drop pages have a timestamp + sold-out persistence; Kith's drops show the countdown on every page, not just the drop page.

### 4. Drop-story long-form piece per season — Sandy Liang / Online Ceramics editorial

One long-form scroll per season that reads as a zine: hero image full-bleed → 3–5 editorial cards with pull-quotes in Fraunces → small-caps credit footer. One season per year is enough. The page exists to be linked from Instagram bios, not to be found by search.

**Mechanism:** Content 10 dimension gets another +1 from editorial depth.
**Delta:** +0.05 weighted.
**Competitor anchor:** Sandy Liang's `sandyliang.info` is essentially one long editorial page — that tone.

## Out of scope

- Adding a full CMS. The JSON-driven campaign template is explicitly the cheapest path — do not graft Sanity or Contentful onto a static site for 4 pages a year.
- Removing the custom cursor. It's a signature — the fix above keeps it everywhere it works and disables it everywhere it doesn't.
- Porting the static site into Next.js. The §2 commerce app is the framework surface; this static site should stay a hand-coded marketing page.
- Font changes. Fraunces variable is a jury-legible choice; changing it now resets the Design score.

## Re-audit verification

A re-audit passes on this site when:

1. Keyboard-only nav shows a visible focus ring on every interactive element (Tab through the page → focus ring always visible).
2. `html` has `class="no-js"` at parse time and the class is stripped by the first inline script.
3. Each named bundle in the active drop has a campaign page with ≥3 editorial images and ≥1 story paragraph.
4. Hero has a visible next-drop slot — countdown active OR most-recent-drop "sold out" persistent state.
5. Lighthouse accessibility score ≥98 on the home page with JS disabled.

Expected post-implementation weighted score: **7.95** (Design 8.3 / Usability 7.5 / Creativity 8.6 / Content 8.0).
