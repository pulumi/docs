---
title: Changelog
meta_desc: The full Pulumi releases changelog, with each entry's complete announcement.

# Each changelog item is its own page in this directory: title, date, and an
# optional tier badge in front matter, with the full announcement as the
# markdown body. Items render at /releases/changelog/<slug>/ and are listed
# (grouped by month, alongside full releases) on /releases/.
#
# This section page renders at /releases/changelog/ as the *expanded* view of
# the releases feed (layouts/changelog/list.html), the counterpart to the
# compact /releases/ list. `type: changelog` routes it (and every item) to the
# changelog layouts; HTML-only output keeps the JSON/RSS feeds on /releases/.
type: changelog
outputs:
  - HTML
cascade:
  type: changelog
---
