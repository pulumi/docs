{{- $type := .Get 0 -}}
{{- $options := .Get 1 -}}
{{- if eq $options "nodejs" -}}
    {{- $options = "javascript,typescript" -}}
{{- end -}}

<!-- chooser: {{ $type }} -->
{{ .Inner }}
<!-- /chooser -->
