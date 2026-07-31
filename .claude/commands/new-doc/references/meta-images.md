---
user-invocable: false
---

# Meta Image Selection

`meta_image` is **optional**. Leave it blank/omit it and the build generates an
on-brand social-media card for the page automatically — see
`scripts/generate-meta-images.mjs` and `layouts/partials/meta-image-url.html`.
Generated cards cover `docs`, `tutorials`, `case-studies`, `what-is`, `migrate`,
`partner`, and `topics`. Prefer the generated card for new pages.

Only set `meta_image` when you need a **custom** image that overrides the
generated card (a page-level `meta_image` always wins). For a docs page, that is
almost never — omit it.

**Never point `meta_image` at a generic section placeholder** (e.g. an old
"Pulumi Docs" card). Doing so suppresses the generated, page-specific card and
gives every page the same social image. If a page genuinely needs a custom
image, it must be artwork made for that page.
