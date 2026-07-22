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
generated card (a page-level `meta_image` always wins).

## Path-Based Image Mapping (override only)

When you do need a custom docs image, use these legacy paths:

- `iac/clouds/aws` → `/images/docs/meta-images/docs-clouds-aws-meta-image.png`
- `iac/clouds/azure` → `/images/docs/meta-images/docs-clouds-azure-meta-image.png`
- `iac/clouds/gcp` → `/images/docs/meta-images/docs-clouds-google-cloud-meta-image.png`
- `iac/clouds/kubernetes` → `/images/docs/meta-images/docs-clouds-kubernetes-meta-image.png`
- **All others** → `/images/docs/meta-images/docs-meta.png`
