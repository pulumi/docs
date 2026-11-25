{{- $text := "This is an **experimental feature**. Experimental features are opt-in (enabled with a flag, command, or environment variable), may change or be removed at any time, and are not necessarily supported. See Experimental features (/docs/support/experimental-features/) for details." -}}
{{- $inner := trim (printf "%s" .Inner) " \t\n\r" -}}

> **Warning:** {{ $text }}{{ with $inner }} {{ . }}{{ end }}
