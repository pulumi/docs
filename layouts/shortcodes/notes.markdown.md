{{- $type := default "info" (.Get "type") -}}
{{- $label := "Note" -}}
{{- if eq $type "warning" }}{{ $label = "Warning" }}{{ end -}}
{{- if eq $type "tip" }}{{ $label = "Tip" }}{{ end -}}
{{- $inner := .Inner | strings.TrimSpace -}}
{{- $inner = replaceRE `</?p>` "" $inner -}}
{{- $inner = replaceRE `<a href="([^"]*)"[^>]*>([^<]*)</a>` "[$2]($1)" $inner -}}
{{- $inner = replaceRE `<code>([^<]*)</code>` "`$1`" $inner -}}
{{- $inner = replaceRE `<strong>([^<]*)</strong>` "**$1**" $inner -}}
{{- $inner = replaceRE `<em>([^<]*)</em>` "*$1*" $inner -}}
{{- $inner = $inner | htmlUnescape -}}

> **{{ $label }}:** {{ $inner }}
