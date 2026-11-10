{{- $title := .Get "title" -}}
{{- $product := .Get "product" -}}

**{{ $title }}.** {{ trim .Inner "\n " }}{{ with $product }} *({{ . }}.)*{{ end }}
