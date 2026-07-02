# Company logos for event cards

The events card places **Pulumi + optional partner/company logos** in a horizontal
lockup at the bottom of the text column, joined by a muted **`+`** (Pulumi `+`
Microsoft `+` …). Pass logo **paths** in the render config
(`logos: ["pulumi", "<path>"]`); `"pulumi"` is the one special name (it maps to
the bundled brand mark — never recolor or restyle it).

## Three hard rules

1. **Wordmark, not glyph.** Default to the lockup that includes the **company
   name** (e.g. the Microsoft squares + "Microsoft"; the Pinecone mark +
   "Pinecone"). A bare icon next to "Pulumi" reads as unfinished. Only use a
   glyph if no wordmark exists or the glyph *is* the brand.
2. **Horizontal, not stacked.** The renderer scales every logo to a fixed row
   *height*, so a vertical/stacked lockup (mark above the name) renders its text
   tiny. Prefer the horizontal variant (mark beside the name, or the wordmark
   alone) — aim for an aspect ratio **≳ 3:1** and reject stacked/near-square
   lockups (aspect ≲ 2). Many brands ship both; take the horizontal one.
3. **SVG or transparent PNG only.** The card is near-white (`#f5f5ff`); a logo
   with a baked-in white/opaque background shows as an ugly box. A PNG that
   `file` reports as `RGB` (no alpha) is opaque — reject it. Confirm transparency
   in the render before caching.

## Resolution ladder

For each requested company logo, stop at the first hit that satisfies both rules:

1. **Cached** — `assets/logos/<name>.{svg,png}` (this dir; inventory below).
2. **Repo** — `static/logos/**` (the site's own brand assets — often clean SVG
   wordmarks).
3. **Web** — `WebSearch` `"<company> logo wordmark SVG transparent"` →
   `WebFetch`/`curl` the official SVG. Good sources: the company's brand/press
   page, Wikimedia Commons (`*_logo.svg`), reputable vector libraries.
   simple-icons (`https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/<slug>.svg`)
   is **glyph-only + monochrome** — last resort; recolor the `<path>` with
   `fill="#<brandcolor>"`.
4. **Ask** the user for a transparent SVG/PNG wordmark. Prefer asking over
   shipping a mark-only or white-background logo.

**Cache** any clean fetched logo to `assets/logos/<name>.{svg,png}` and add a row
below. The renderer scales every logo to a common height preserving aspect ratio,
so source dimensions don't matter. Keep the lockup short: Pulumi + 1–2 partners
reads best.

## Cached inventory (`assets/logos/`)

| name | file | wordmark? | notes |
|------|------|-----------|-------|
| pulumi | `pulumi.svg` | ✅ | bundled brand mark; reference via the `"pulumi"` config name |
| microsoft | `microsoft.svg` | ✅ | squares + "Microsoft" (Wikimedia, transparent) |
| google-cloud | `google-cloud.svg` | ✅ | hexagon + "Google Cloud" (Wikimedia, transparent) |
| pinecone | `pinecone.png` | ✅ | mark + "Pinecone" (transparent RGBA) |
| github-wordmark | `github-wordmark.svg` | ✅ | Invertocat + "GitHub" (Wikimedia `GitHub_logo_2013.svg`, transparent, aspect ~3.5:1) |
| github | `github.svg` | ⚠️ | glyph only — swap for a wordmark when used |
| gitlab | `gitlab.svg` | ⚠️ | glyph only |
| aws | `aws.svg` | ⚠️ | glyph only |
| google | `google.svg` | ⚠️ | glyph only |
| azure | `azure-icon.svg` | ⚠️ | glyph only |
| kubernetes | `kubernetes.svg` | ⚠️ | glyph only |
| docker | `docker.svg` | ⚠️ | glyph only |
| datadog | `datadog.svg` | ⚠️ | glyph only |
| databricks | `databricks.svg` | ⚠️ | glyph only |

The ⚠️ glyph-only seeds are starting points — prefer fetching the wordmark
version (per the two hard rules above) and updating the row when you do.

Add fetched logos here as you cache them.
