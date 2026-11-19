{{- $title := .Get "title" -}}
{{- $href := .Get "href" -}}
- [{{ $title }}]({{ $href }}): {{ .Inner | strings.TrimSpace }}
