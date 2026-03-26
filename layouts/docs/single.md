---
title: {{ .Title }}
{{ with .Description }}description: {{ . }}
{{ end }}url: {{ .RelPermalink }}
---
{{- $content := .RenderShortcodes -}}
{{- $content = partial "docs/markdown-pipeline.md" $content -}}

{{ $content }}
