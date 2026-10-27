{{ range index .Page.Params.integration_groups (.Get 0) }}
- [{{ .name }}]({{ .link }})
{{ end }}
