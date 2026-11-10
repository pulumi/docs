{{- $cards := .Inner | transform.Unmarshal -}}
{{ range $cards }}
- **{{ .number }}** — {{ .label }}
{{- end }}
