# {{ .Title }}

{{ with .Params.meta_desc }}
> {{ . }}
{{ end }}

{{ range .Params.sections }}
## {{ .heading }}

{{ with .description_md }}
{{ . | markdownify }}
{{ end }}

{{- if .cards }}
{{ range .cards }}
{{- if or .heading .label }}
### {{ or .heading .label }}
{{- end }}

{{ with .description }}
{{ . }}
{{ end }}

{{ with .link }}
[Read more]({{ . | relURL }}index.md)
{{ end }}

{{ end }}
{{ end }}

{{- end }}

{{- if .Content }}
{{ .Content }}
{{- end }}
