---
name: event-meta-image
description: "Generate on-brand social cards for a Pulumi event/workshop in five sizes (1200x628 OG, 1200x675, 628x628, 1080x1080, 540x960) using the shared Satori events renderer. Enriches the build-time default with people not in frontmatter (external co-presenters + their photos) and company/partner logos (Pulumi + e.g. Microsoft). Runs event-bound (writes into a content/events/<slug>/ bundle + sets meta_image / meta_image_square) or standalone (just emit the five PNGs to a folder). Use when the user types /event-meta-image or asks to create, generate, regenerate, or enrich an event's meta image, social card, OpenGraph image, or speaker/workshop card."
---

# `/event-meta-image` — Generate event / workshop social cards

You generate the branded event card (the Figma "Workshop / event images" component) in **five sizes** via the shared Node/Satori renderer — the *same* renderer the build uses for the automatic default, so output is identical to what ships, just enriched with inputs that aren't in frontmatter (external co-presenters, their photos, partner logos).

**Skill directory**: `.claude/commands/event-meta-image/` — paths below are relative to the **repo root** unless noted.
**Renderer CLI**: `scripts/meta-images/render-event.mjs` (shared with the build). One JSON config → one PNG per size.

> **You do not need a custom card for most events.** Every event already gets an on-brand landscape + square card automatically at build time from its frontmatter (`scripts/generate-meta-images.mjs`). Use this skill only to (a) enrich a card with people/logos not in frontmatter, (b) override the auto default, or (c) grab the extra social sizes (square-large, portrait, tall) for manual use.

---

## [Step 0/6] Pick the mode

- **Event-bound** — there is a target `content/events/<slug>/` page. Triggered when `$ARGUMENTS` names an event path/slug, when `git status` shows a changed event, or when the user points at one. Writes the PNGs **into the page bundle** and updates frontmatter.
- **Standalone** — the user just wants images ("generate event images for …", no event attached). Collect inputs directly (Steps 3–5), skip frontmatter, and write the PNGs to an output dir (default `.context/event-images/<slug>/`, or a path the user gives). **No** frontmatter or bundle writes.

Everything below applies to both modes **except** the bundle/frontmatter writes in Step 6 (event-bound only).

## [Step 1/6] Locate the event (event-bound)

1. If `$ARGUMENTS` contains an event path or slug, use `content/events/<slug>/index.md`.
2. Otherwise run `git status` / `git diff --name-only` for changed `content/events/*/index.md`.
3. Multiple candidates → ask with `AskUserQuestion`. None → ask for the slug/path (or switch to standalone if the user only wants loose images).

Read the full `index.md` (frontmatter + body).

## [Step 2/6] Seed from frontmatter

Pull from frontmatter:

- **title** (required — the card's main title; the renderer fits it to the box).
- **event_type** → the default **overline** (uppercased automatically).
- **presenters**: `presenters: [{ name, role, photo }]` — the in-frontmatter speakers. Each `photo` (e.g. `/images/people/<x>.jpg` or `/images/team/<x>.jpg`) resolves under `static/`.

The build default already uses exactly these. If the user only wants the default look in all five sizes (no new people/logos), you can skip straight to Step 6 with `overline`, `title`, the presenters' `photo` paths as `speakers`, the `"With …"` line as `additionalText`, and `["pulumi"]` as `logos`.

## [Step 3/6] Add people not in frontmatter (external co-presenters)

Ask (with `AskUserQuestion`) whether to add anyone beyond the `presenters:` list — e.g. a partner-company co-host. For each added person collect **name** + **role/company**, then resolve a **color photo** via this ladder (stop at the first hit):

1. An existing `presenters[].photo` (already have it).
2. `static/images/team/<kebab-name>.{jpg,jpeg,png}`.
3. `static/images/people/<kebab-name>.{jpg,jpeg,png}`.
4. **Web**: `WebSearch` for a headshot / company bio photo, then `WebFetch` the image. LinkedIn images are usually auth-gated — expect this to fail and fall through.
5. **Ask** the user for a photo URL or local file path.

Save any fetched/provided external photo to a real file (e.g. `.context/event-images/<slug>/<kebab-name>.jpg`) and pass that **path** in the config — the renderer resolves local files and `data:` URIs, not remote URLs. Photos render **color + circular on a violet ring** (the renderer can't reproduce the Figma duotone; the ring keeps them on-brand). Up to **5** speakers display (the renderer shrinks the circles so they fit, stacking vertically on landscape and in a row on square/portrait); the byline lists every name. Beyond 5 is rare — pick the 5 to show in Step 5.

## [Step 4/6] Company / partner logos

Pulumi is **always** included (`"pulumi"` → the bundled brand mark — never re-color or restyle it). The renderer lays the logos out in a row joined by a muted **`+`** (Pulumi `+` Microsoft `+` …), so each entry should read as a company on its own.

Ask whether to add partner/company logos (e.g. Microsoft, GitHub, Google Cloud, NVIDIA). Three hard rules when sourcing each one:

- **Default to the WORDMARK** — the lockup that includes the **company name** (e.g. the Microsoft squares *plus* "Microsoft"), not the bare glyph. A mark-only icon next to "Pulumi" reads as unfinished. Only fall back to a glyph if no wordmark exists or the glyph IS the brand (rare).
- **Prefer the HORIZONTAL variant.** The renderer scales every logo to a fixed row *height*, so a vertical/**stacked** lockup (mark stacked above the name) renders its text tiny and unbalanced next to Pulumi. Choose the horizontal lockup (mark beside the name, or the wordmark alone). Rule of thumb: check the SVG `viewBox` / PNG dimensions and prefer an **aspect ratio ≳ 3:1**; reject stacked or roughly-square lockups (aspect ≲ 2) even when they're technically a wordmark, and keep looking (a company's brand/press page usually offers both a "horizontal" and a "stacked" variant — take the horizontal one).
- **Must be an SVG or a TRANSPARENT PNG.** The card background is near-white (`#f5f5ff`), so a logo with a baked-in **white/opaque background shows as an ugly box — never use one.** Verify transparency before caching (a PNG reported by `file` as `RGB` with no alpha is opaque; `RGBA` or a colormap with `tRNS` may be transparent — check the render).

Resolve each via this ladder, stopping at the first hit that satisfies both rules:

1. `.claude/commands/event-meta-image/assets/logos/<name>.svg` (cached — see `references/logos.md`).
2. `static/logos/**` (the site's own brand assets — often clean SVG wordmarks).
3. **Web** — `WebSearch` `"<company> logo wordmark SVG transparent"`, then `WebFetch`/`curl` the official SVG. Good sources: the company's own brand/press page, Wikimedia Commons (`*_logo.svg`), and reputable vector libraries. simple-icons (`https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/<slug>.svg`) is **glyph-only and monochrome** — use it only as a last resort, and recolor the `<path>` with `fill="#<brandcolor>"`.
4. **Ask the user** for a transparent SVG/PNG wordmark. Prefer asking over shipping a mark-only or white-background logo.

**Cache** any clean fetched logo to `.claude/commands/event-meta-image/assets/logos/<name>.{svg,png}` and add a row to `references/logos.md`. Pass logo **paths** (absolute, or relative to the config file) in the config; `"pulumi"` is the one special name.

## [Step 5/6] Options

Confirm with `AskUserQuestion` (skip anything `$ARGUMENTS` already answered):

- **overline** — default `event_type` (e.g. `WORKSHOP`, `WEBINAR`, `PANEL`). Allow an override.
- **secondary title** — hidden by default; offer to set a small line above the title.
- **show "Register" button?** — default **no**.
- **which people / logos to include and their order** — when there are more than 5 people, pick the 5 to show; order logos Pulumi-first.

## [Step 6/6] Render the five sizes

Write **one** config JSON (e.g. `.context/event-images/<slug>/config.json`), then loop the renderer over the five sizes.

**Config schema** (all optional except `title`):

```json
{
  "overline": "WORKSHOP",
  "title": "Advanced CI/CD for AWS using Pulumi and GitHub Actions",
  "secondaryTitle": "",
  "additionalText": "With Jane Doe - Staff Engineer, Acme and John Roe",
  "showButton": false,
  "buttonText": "Register",
  "speakers": ["/images/people/jane.jpg", ".context/event-images/<slug>/john-roe.jpg"],
  "logos": ["pulumi", ".claude/commands/event-meta-image/assets/logos/microsoft.svg"]
}
```

- `additionalText` is the literal "With …" line. Compose it yourself: one presenter → `With {name} - {role}`; many → names only, Oxford comma (`With A, B, and C`). (Omit to let the CLI derive it from a `presenters: [{name, role}]` array instead.)
- `speakers` / `logos` resolve as: `data:` URI → path relative to the config file → repo path (`/images/…`, `static/`, `assets/fingerprinted/`, `static/logos/**`) → absolute path. Unresolved entries are skipped with a warning.

**Render loop** — same config, five sizes:

| size | event-bound filename | wired to |
|------|----------------------|----------|
| `1200x628` | `meta.png` | `meta_image` (primary OG + twitter:image) |
| `628x628`  | `meta-square.png` | `meta_image_square` (second og:image) |
| `1200x675` | `meta-landscape-tall.png` | — (manual social) |
| `1080x1080`| `meta-square-large.png` | — (manual social) |
| `540x960`  | `meta-portrait.png` | — (manual social) |

```bash
CFG=.context/event-images/<slug>/config.json
DEST=content/events/<slug>          # event-bound; standalone → .context/event-images/<slug>
node scripts/meta-images/render-event.mjs --config "$CFG" --size 1200x628  --out "$DEST/meta.png"
node scripts/meta-images/render-event.mjs --config "$CFG" --size 628x628   --out "$DEST/meta-square.png"
node scripts/meta-images/render-event.mjs --config "$CFG" --size 1200x675  --out "$DEST/meta-landscape-tall.png"
node scripts/meta-images/render-event.mjs --config "$CFG" --size 1080x1080 --out "$DEST/meta-square-large.png"
node scripts/meta-images/render-event.mjs --config "$CFG" --size 540x960   --out "$DEST/meta-portrait.png"
```

### Event-bound writes (only)

After rendering into `content/events/<slug>/`, set frontmatter:

```yaml
meta_image: /events/<slug>/meta.png
meta_image_square: /events/<slug>/meta-square.png
```

(Optionally set `overline:` if you customized it.) The three extra sizes are **not** wired to meta tags — they're for manual social use. Setting `meta_image` makes the build skip the auto card for this page (the override wins; see `layouts/partials/meta-image-url.html`).

### Standalone writes (only)

Write all five PNGs to the chosen output dir and report their paths. No frontmatter, no bundle.

## Wrap-up

Report: mode; the event (event-bound); overline + title used; people shown (and where each photo came from); logos placed; the five output paths; and for event-bound, the frontmatter that was set. **Always remind the user to preview the PNGs** (and, event-bound, the live page) before committing. Preview the landscape and square first — those are the ones that ship as og:image.

## Error handling

- `render-event.mjs` prints `warning: could not resolve …` for any photo/logo it couldn't find — fix the path or re-resolve via the ladder.
- "Offset is outside the bounds of the DataView" or a decode error → the image is corrupt/truncated; re-fetch it. (Mislabeled extensions like a PNG named `.jpg` are handled automatically — the renderer sniffs the real type.)
- No `title` → ask the user. Long titles auto-shrink to fit; you don't need to trim them.
- Don't generate or AI-synthesize brand imagery or the Pulumi mascot; use the bundled logo and approved assets only.

## References

- `references/logos.md` — cached company-logo inventory + the resolution ladder.
- Renderer internals / layout: `scripts/meta-images/events.mjs`. Shared CLI: `scripts/meta-images/render-event.mjs`.
