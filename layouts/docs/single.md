---
title: {{ .Title }}
{{ with .Description }}description: {{ replaceRE `<[^>]+>` "" . }}
{{ end }}url: {{ .RelPermalink }}
---
{{- $content := .RenderShortcodes -}}
{{- $content = partial "docs/markdown-pipeline.md" $content -}}

{{ $content }}
