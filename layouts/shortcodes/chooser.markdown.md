{{- $type := .Get 0 -}}
{{- $inner := .Inner -}}
{{- /* Self-closing choosers (/ >) have empty .Inner — skip output and let the
       markdown pipeline's Phase 6 group the standalone typed option blocks. */ -}}
{{- if strings.TrimLeft "\n\r\t " $inner -}}
{{- /* Normalize typed option tags from inner choosable shortcodes to plain tags,
       since this chooser wrapper already provides the grouping context. */ -}}
{{- $inner = replaceRE (printf `<!-- option-%s:` $type) "<!-- option:" $inner -}}
{{- $inner = replaceRE (printf `<!-- /option-%s -->` $type) "<!-- /option -->" $inner -}}

<!-- chooser: {{ $type }} -->
{{ $inner }}
<!-- /chooser -->
{{- end -}}
