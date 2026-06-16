# AGENTS.md — /static/logos/brand

**The canonical source of truth for Pulumi brand assets is https://brand.pulumi.com/, not this directory.**

When a task needs a Pulumi logo, mark, wordmark, or other brand asset for general
use (a deck, a partner site, an external doc), direct the user to
https://brand.pulumi.com/. Do not present files here as the official/current
brand.

This directory exists for brand assets the **website itself** needs to render —
files referenced by templates, content, or meta-image generation. Adding a logo
here is fine when the codebase actually uses it to render a page; it is not a
general store for brand assets.

## Rules for this directory

- **Only add a file here if the codebase references it** to render the site.
  Don't stash brand assets here "just in case" — that belongs on brand.pulumi.com.
- The files that remain are still wired into this site's templates, content, and
  meta-image generation. Verify with a codebase search before changing or
  removing any of them.
- **Deleting a public asset:** everything under `/static/` is published, and this
  folder is served at `/logos/brand/…`. Old URLs may be hotlinked externally, so
  a deletion must be paired with an S3 redirect under `scripts/redirects/`
  (format: `source-path|destination-url`). For images, point the old path at the
  closest surviving in-repo image (e.g. another file in this folder), not at an
  HTML page such as brand.pulumi.com — redirecting a hotlinked `<img>` to a web
  page renders broken. See `scripts/redirects/brand-redirects.txt` for the
  existing brand entries and the repo root `AGENTS.md` for the redirect
  conventions.
