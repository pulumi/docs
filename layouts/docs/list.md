---
title: {{ .Title }}
{{ with .Description }}description: {{ replaceRE `<[^>]+>` "" . }}
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
{{- else if .Params.cloud_overview -}}
{{- with .Params.h1 }}
# {{ . }}
{{ end -}}
{{- with .Params.description }}
{{ . }}
{{ end -}}
{{- with .Params.get_started_guide }}
[Get started]({{ .link }})
{{ end -}}

## Providers

{{ with .Params.providers.description }}{{ . }}

{{ end -}}
{{- range .Params.providers.provider_list -}}
### {{ .display_name }}
{{ range .content_links -}}
- [{{ .display_name }}](/registry/packages/{{ .url }})
{{ end }}
{{ end -}}

## Templates

{{- range .Params.templates }}
- [{{ .display_name }}](/templates/{{ .url }})
{{- end }}

## Components

{{- range .Params.components }}
- [{{ .display_name }}](/registry/packages/{{ .url }})
{{- end }}
{{ with .Params.guides }}

## Guides

{{ with .description }}{{ . }}

{{ end -}}
{{- range .guides_list -}}
- [{{ .display_name }}]({{ .url }})
{{ end -}}
{{- end -}}
{{- with .Params.policy }}

## Policy

[Policies](/docs/insights/{{ .url }}) — {{ .description }}
{{ end -}}
{{- range .Params.convert -}}

## {{ .heading }}

{{ with .description }}{{ . }}

{{ end -}}
{{- if .url -}}
[{{ .heading }}]({{ .url }})
{{ end -}}
{{- range .tools -}}
- [{{ .display_name }}]({{ .url }})
{{ end -}}
{{- end -}}
{{- with .Params.kubernetes_cluster_management }}

## {{ .heading }}

{{ with .description }}{{ . }}

{{ end -}}
{{- range .links -}}
- [{{ .display_name }}]({{ .url }})
{{ end -}}
{{- end -}}
{{- with .Params.kubernetes_operator }}

## {{ .heading }}

{{ with .description_1 }}{{ . }}

{{ end -}}
{{- with .description_2 }}{{ . }}

{{ end -}}
{{- range .links -}}
- [{{ .display_name }}]({{ .url }})
{{ end -}}
{{- end -}}
{{- end -}}
