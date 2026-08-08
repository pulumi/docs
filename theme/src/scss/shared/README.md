# Shared style system

These are the site's **reusable, cross-bundle style primitives** — a small design
system built on Tailwind v4 `@apply`/`@extend`. They're consumed by both SCSS
bundles (`main.scss` = docs/app, `_marketing.scss` = marketing) and by cross-file
`@extend` consumers throughout the theme.

**Reuse these before rolling your own.** Don't reinvent a button, card, badge, or
heading — compose the classes below in markup, or `@extend`/`@apply` them in SCSS.

| File | Exposes | Compose as |
|------|---------|-----------|
| `_button.scss` | `.btn` base + variants (`primary`, `outline`, `secondary`, `ghost`, `ghost-primary`, `ghost-nav`, `destructive`, `link`), sizes (`xs/sm/lg/xl`, `icon*`), `.btn-split`, `.btn-group` | `class="btn btn-primary"` — see the file's header for the full API |
| `_card.scss` | `.card`, `.card-hover`, `.card-highlight` (tinted panel) | `class="card"` / `@extend .card;` |
| `_forms.scss` | `.form-input`, `.form-textarea`, `.form-select`, `.form-checkbox`, `.form-radio`, `.form-range`, `.form-label`/`.form-help`/`.form-error`, sizes (`sm/lg/xl`); plus `@mixin`s (`form-control-base`, `form-check-base`, …) | `class="form-input form-input-lg"`, or `@include form-control-base;`. Heights mirror the `.btn` scale |
| `_badge.scss` | `.badge` base + variants (`default`, `brand`, `secondary`, `outline`, `success`, `warning`, `destructive`, `info`, `dark`, `ghost`, `preview`, `required`), sizes (`sm/lg`) | `class="badge badge-success"`, `layouts/partials/badge.html`, or `@extend .badge; @extend .badge-<variant>;` |
| `_utilities.scss` | `@utility` type scale: `heading-xl`/`heading-1`…`heading-6`, `body-sm`…`body-2xl`, `font-overline`, `font-overline-sm` | `class="heading-2"` / `@apply heading-2;` |
| `_base.scss` | `@layer base` element defaults (border-color reset, custom-element `display:block`, `h1`–`h6`/`p`) — foundation, not a class you apply | imported inside `@layer base` |

## Authoring styles — order of preference

Applies everywhere, not just here:

1. **Inline Tailwind utility classes** — including arbitrary values
   (`bg-[#abc123]`, `w-[42ch]`). The default for one-off styling.
2. **SCSS with Tailwind `@apply` / `@extend`** — only when inline classes can't
   stay DRY (the same cluster repeated across many elements/templates). Prefer
   `@extend`ing a shared primitive above over re-`@apply`ing its utilities.
3. **Raw CSS / SCSS** — last resort, for what Tailwind can't express.

## Import notes

- `_utilities.scss` uses `@utility`, so it must be imported at the **top level**
  of each bundle (not inside `@layer base { … }`).
- `_base.scss` must be imported inside `@layer base`.
- `_button.scss`, `_card.scss`, `_badge.scss` are imported inside
  `@layer components`.
- `_forms.scss` must be imported **first** inside `@layer components` — it
  exposes Sass `@mixin`s that later partials (`_hubspot`, `_blog`, `_footer`)
  `@include`, and `@mixin` (unlike `@extend`) is order-dependent.
- Sass `@extend` resolves globally after the full stylesheet is parsed, so
  cross-file consumers (`_tiles`, `_neo-card`, `_templates`, `_algolia`,
  `_chooser`, `_hubspot`, …) don't depend on these files' import order.
