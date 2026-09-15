{{- $rows := .Inner | transform.Unmarshal -}}
{{ range $rows }}
- {{ .body }}
{{- end }}
