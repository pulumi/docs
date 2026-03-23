{{- $type := default "info" (.Get "type") -}}
{{- $label := "Note" -}}
{{- if eq $type "warning" }}{{ $label = "Warning" }}{{ end -}}
{{- if eq $type "tip" }}{{ $label = "Tip" }}{{ end -}}

> **{{ $label }}:** {{ .Inner | strings.TrimSpace }}
