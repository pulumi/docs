---
title: {{ .Title }}
{{ with or .Params.meta_desc .Description }}description: {{ replaceRE `\s+` " " (replaceRE `<[^>]+>` "" (trim . " \n")) }}
{{ end }}url: {{ .RelPermalink }}
---
{{ partial "markdown/sections.md" . }}
