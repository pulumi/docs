---
title: {{ .Title }}
url: {{ .Permalink }}
---

# {{ .Title }}

{{ .RawContent }}

{{- if .Pages }}

## Pages in this section

{{- range .Pages }}
- [{{ .Title }}]({{ .RelPermalink }})
{{- end }}
{{- end }}

