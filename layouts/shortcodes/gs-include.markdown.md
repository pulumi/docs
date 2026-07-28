{{- /*
    Markdown-output twin of gs-include.html (same fragment resolution). A
    fragment with no nested shortcodes is emitted as raw markdown, preserving
    full fidelity (lists, links, emphasis) — the same convention as
    cleanup.markdown.md. A fragment that does contain shortcodes must go
    through RenderString so those nested calls resolve to their .markdown.md
    variants; the docs markdown pipeline then converts the rendered HTML back
    to markdown.
*/ -}}
{{- $name := .Get 0 -}}
{{- if not $name -}}
    {{- errorf "gs-include: a fragment name is required (in %s)" .Page.File.Path -}}
{{- end -}}
{{- $cloud := partial "get-started/cloud-slug.html" .Page -}}
{{- $cloudPath := printf "fragments/get-started/%s/%s.md" $name $cloud -}}
{{- $sharedPath := printf "fragments/get-started/%s.md" $name -}}
{{- $path := $sharedPath -}}
{{- if fileExists $cloudPath -}}
    {{- $path = $cloudPath -}}
{{- end -}}
{{- if not (fileExists $path) -}}
    {{- errorf "gs-include: fragment %q not found (looked for %s, then %s; called from %s)" $name $cloudPath $sharedPath .Page.File.Path -}}
{{- end -}}
{{- $raw := readFile $path -}}
{{- if or (in $raw "{{<") (in $raw "{{%") -}}
{{ .Page.RenderString (dict "display" "block") $raw }}
{{- else -}}
{{ $raw }}
{{- end -}}
