---
title: {{ .Title }}
{{ with .Description }}description: {{ replaceRE `<[^>]+>` "" . }}
{{ end }}url: {{ .RelPermalink }}
---
{{- $content := .RenderShortcodes -}}
{{- $content = partial "docs/markdown-pipeline.md" $content -}}
{{ with .Params.pulumi_cloud_feature }}
> {{ partial "cloud-availability-body.html" (dict "feature" . "where" $.RelPermalink) }}
{{ end }}

{{ $content }}
