---
title: Migrate
meta_desc: Section holder for the Pulumi migration marketing pages; not rendered as a list page.

# The migration hub that used to live at /migrate/ is retired (pulumi/docs#20247);
# /migrate/ now 301s to /docs/iac/guides/migration/ (see
# scripts/redirects/general-broken-links-redirects.txt). This directory is kept
# only as a home for the two vanity marketing pages that override their URLs:
# terraform.md (/terraform) and cloudformation.md (/cloudformation). Those still
# render — `build` applies to this page alone and is not inherited by children.
build:
  render: never
  list: never
---
