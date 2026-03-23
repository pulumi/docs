{{- $values := .Get 1 -}}
{{- if eq $values "nodejs" -}}
    {{- $values = "javascript,typescript" -}}
{{- end -}}
{{- $label := index (split $values ",") 0 -}}

<!-- option: {{ $label }} -->
{{ .Inner }}
<!-- /option -->
