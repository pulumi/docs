---
# /gads/ is a container for paid-search landing pages, not a destination of its
# own. Without this file Hugo auto-generated a section list page for it, which
# rendered through _default/list.html (badly), was crawlable, and shipped in the
# sitemap. See https://github.com/pulumi/docs/issues/20268.
#
# redirect_to sends it to the homepage: head.html emits a zero-delay meta
# refresh, which scripts/translate-redirects.js turns into a real S3 301 keyed
# to gads/index.html alone. The landing pages under /gads/* are separate files
# and are unaffected.
#
# block_external_search_index adds a noindex tag and drops the page from the
# sitemap and the on-site search index, so it stays out of search results even
# before the 301 is applied.
title: Google Ads landing pages
block_external_search_index: true
redirect_to: /
---
