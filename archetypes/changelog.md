---
# Changelog entry for the Pulumi releases log.
#
# Create one with:
#
#   hugo new --kind changelog content/releases/changelog/YYYY-MM-DD-your-slug.md
#
# The filename MUST be date-prefixed as YYYY-MM-DD-<slug> (e.g.
# 2026-07-11-universal-search.md). `make lint` enforces this format and checks
# that the date prefix matches the `date:` value below. The title and date are
# derived from the filename, so keep the date prefix accurate.

# A short, descriptive headline for the entry. Derived from the slug — edit it
# to read well (the slug-to-title conversion is only a starting point).
title: "{{ $slug := replaceRE `^[0-9]{4}-[0-9]{2}-[0-9]{2}-` `` .Name }}{{ replace $slug `-` ` ` | title }}"

# The publish date, used for display and for grouping entries by month on
# /releases/. Pulled from the filename's date prefix; keep the two in sync.
date: {{ substr .Name 0 10 }}

# A one- or two-sentence summary for search results and social previews.
# Required — the build fails the linter without it. Max length 160 characters.
meta_desc:

# Optional tier badge shown beside the date (e.g. "public preview", "ga").
# Remove this line if you don't need a badge.
# tier: public preview
---

Describe what shipped in a short paragraph or two. Lead with what the reader can now do, then link out to the announcement post and/or the docs for details.

Images and videos live in the shared `images/` and `videos/` folders next to this file. Name them with a date prefix too — `YYYY-MM-DD-<slug>.<ext>`, using this entry's date (e.g. `2026-07-11-your-image.png`) — and reference them by absolute path, e.g. `/releases/changelog/images/2026-07-11-your-image.png`. `make lint` enforces the asset naming.
