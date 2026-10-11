{{- $text := "This is an **experimental feature**. Experimental features are opt-in (enabled with a flag, command, or environment variable), may change or be removed at any time, and are not necessarily supported. See What does \"experimental\" mean? (/docs/support/faq/infrastructure/#what-does-experimental-mean) for details." -}}
{{- $inner := trim (printf "%s" .Inner) " \t\n\r" -}}

> **Warning:** {{ $text }}{{ with $inner }} {{ . }}{{ end }}
