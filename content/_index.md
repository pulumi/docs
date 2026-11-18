---
title: Infrastructure as code for humans and agents – Pulumi
meta_desc: Pulumi is an open-source infrastructure as code platform that helps humans and agents build and manage cloud infrastructure with real programming languages.

# The homepage itself now ships from pulumi/marketing-web (see AGENTS.md).
# This node stays only because Hugo still builds /index.json (the search
# index), /llms.txt, and /sitemap-index.xml from the home page; it no longer
# emits HTML or markdown. sitemap_exclude (not the standard sitemap.disable --
# layouts/_default/sitemap.xml checks this flat param instead, see
# content/registry.md) keeps it out of this site's own sitemap.xml: without
# HTML in outputs.home, .RelPermalink here resolves to this page's first
# remaining output format ("/index.json") instead of "/", so leaving it in
# would list the search index itself as a sitemap URL.
sitemap_exclude: true
---
