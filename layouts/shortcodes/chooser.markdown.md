{{- $type := .Get 0 -}}
{{- $options := .Get 1 -}}
{{- if eq $options "nodejs" -}}
    {{- $options = "javascript,typescript" -}}
{{- end -}}
{{- $inner := .Inner -}}
{{- /* Normalize typed option tags from inner choosable shortcodes to plain tags,
       since this chooser wrapper already provides the grouping context. */ -}}
{{- $inner = replaceRE (printf `<!-- option-%s:` $type) "<!-- option:" $inner -}}
{{- $inner = replaceRE (printf `<!-- /option-%s -->` $type) "<!-- /option -->" $inner -}}

<!-- chooser: {{ $type }} -->
{{ $inner }}
<!-- /chooser -->
