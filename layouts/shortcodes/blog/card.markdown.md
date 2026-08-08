{{- with .Get 0 }}{{- with site.GetPage . }}
**[{{ .Title }}](https://www.pulumi.com{{ .RelPermalink }})**
{{ with .Params.meta_desc }}
{{ . }}
{{ end }}
{{ end }}{{ end -}}
