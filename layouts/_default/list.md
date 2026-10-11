---
title: {{ .Title }}
{{ with or .Params.meta_desc .Description }}description: {{ replaceRE `\s+` " " (replaceRE `<[^>]+>` "" (trim . " \n")) }}
{{ end }}url: {{ .RelPermalink }}
---
{{- $content := .RenderShortcodes -}}
{{- $content = partial "docs/markdown-pipeline.md" $content -}}

{{ $content }}
{{- partial "markdown/sections.md" . }}
{{ range .Pages }}
- [{{ .Title }}]({{ .RelPermalink }}){{ with .Params.meta_desc }} — {{ replaceRE `\s+` " " (replaceRE `<[^>]+>` "" (trim . " \n")) }}{{ end }}
{{- end }}
