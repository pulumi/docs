---
title: {{ .Title }}
{{ with .Description }}description: {{ . }}
{{ end }}url: {{ .RelPermalink }}
---
{{- $content := .RenderShortcodes -}}
{{- $content = partial "docs/markdown-pipeline.md" $content -}}

{{ $content }}
{{- if .Params.docs_home -}}
{{- with .Params.h1 }}
# {{ . }}
{{ end -}}
{{- with .Params.description }}
{{ replaceRE `<[^>]+>` "" (replaceRE `<a[^>]*href="([^"]*)"[^>]*>([^<]*)</a>` "[$2]($1)" .) }}
{{ end -}}
{{- with .Params.link_buttons -}}
{{- with .primary }}
[{{ .label }}]({{ .link }})
{{ end -}}
{{- end -}}
{{- range .Params.sections }}
{{- if .heading }}

## {{ .heading }}
{{ end -}}
{{- with .description }}
{{ replaceRE `<[^>]+>` "" (replaceRE `<a[^>]*href="([^"]*)"[^>]*>([^<]*)</a>` "[$2]($1)" .) }}
{{ end -}}
{{- range .cards }}
- [{{ with .heading }}{{ . }}{{ else }}{{ .label }}{{ end }}]({{ .link }}){{ with .description }} — {{ . }}{{ end }}
{{- end }}
{{ end -}}
{{- end -}}
