---
title: Releases
meta_desc: A running log of major platform updates from the Pulumi team.

# Opt this section into JSON and RSS feeds (built in config/_default/config.yml).
# JSON -> /releases/index.json (layouts/releases/list.json)
# RSS  -> /releases/rss.xml    (layouts/releases/rss.xml)
outputs:
  - HTML
  - JSON
  - RSS

# Everything on /releases/ is auto-discovered from this section's pages — no
# manifest to maintain. Two page kinds, distinguished by type:
#   - releases:  full release detail pages at content/releases/<slug>.md,
#                rendered as large cards on the list page.
#   - changelog: individual items at content/releases/changelog/<slug>.md
#                (see that directory's _index.md), rendered as linked rows that
#                open in a modal on the list page.
# The list page, JSON feed, and RSS feed all range over .RegularPagesRecursive,
# newest-first; the list page groups them by month.
---
