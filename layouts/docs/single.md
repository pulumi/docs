---
title: {{ .Title }}
{{ with .Description }}description: {{ replaceRE `<[^>]+>` "" . }}
{{ end }}url: {{ .RelPermalink }}
---
{{- $content := .RenderShortcodes -}}
{{- $content = partial "docs/markdown-pipeline.md" $content -}}
{{ with .Params.pulumi_cloud }}
> {{ partial "cloud-availability-body.html" (dict "edition" . "where" $.RelPermalink) }}
{{ end }}

{{ $content }}
