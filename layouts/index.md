---
title: {{ .Title }}
{{ with .Params.meta_desc }}description: {{ replaceRE `\s+` " " (trim . " \n") }}
{{ end }}url: {{ .RelPermalink }}
---
{{ with .Params.meta_desc }}> {{ replaceRE `\s+` " " (trim . " \n") }}
{{ end }}
Pulumi documentation lives at [/docs/](/docs/); every docs page (and this page) supports `Accept: text/markdown` content negotiation and the `.md` URL suffix. A curated index for agents is at [/llms.txt](/llms.txt), and a machine-readable docs sitemap at [/docs/llm-sitemap.json](/docs/llm-sitemap.json).
{{ partial "markdown/sections.md" . }}
