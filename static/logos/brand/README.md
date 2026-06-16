# Pulumi brand assets

**The source of truth for Pulumi logos, colors, and brand guidelines is [brand.pulumi.com](https://brand.pulumi.com/).**

Go there for the current, approved brand assets. Do not treat this directory as the canonical brand source.

## What belongs here

This directory holds brand assets that the website itself needs to render —
files referenced by templates, content, or meta-image generation (e.g.
`logo.svg`, `og-default.png`, `twitter-summary.png`, the `avatar-*` and
`logo-on-*` variants). If the codebase needs a logo to render a page, it's
reasonable to add it here.

This is **not** a general store for brand assets, and it is **not** the canonical
source of truth — that's [brand.pulumi.com](https://brand.pulumi.com/).

## Guidelines

- **Need a Pulumi logo for general use** (a deck, a partner site, an external
  doc)? Get it from [brand.pulumi.com](https://brand.pulumi.com/) — don't copy
  files out of this directory.
- **Adding a file here?** Only do so if the codebase actually references it to
  render the site. Don't stash brand assets here "just in case."
- **Removing a file?** Anything under `/static/` is served publicly (this folder
  maps to `/logos/brand/…`) and may be hotlinked from outside the repo. Before
  deleting, search the codebase for references and add an S3 redirect under
  `scripts/redirects/`. Point image URLs at the closest surviving in-repo image
  (e.g. another file in this folder) — **not** at an HTML page like
  brand.pulumi.com, since a hotlinked `<img>` redirected to a web page just
  renders broken. Existing brand redirects live in
  `scripts/redirects/brand-redirects.txt`; see the repo root `AGENTS.md` for the
  redirect conventions.
