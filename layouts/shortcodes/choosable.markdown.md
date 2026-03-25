{{- $values := .Get 1 -}}
{{- if eq $values "nodejs" -}}
    {{- $values = "javascript,typescript" -}}
{{- end -}}
{{- $label := index (split $values ",") 0 -}}
{{- $inner := .Inner -}}
{{- /* Convert Chroma syntax-highlighted HTML back to fenced code blocks */ -}}
{{- $inner = replaceRE `<div class="highlight"><pre[^>]*><code class="language-([^"]*)"[^>]*>` "```$1\n" $inner -}}
{{- $inner = replaceRE `</code></pre></div>` "\n```\n\n" $inner -}}
{{- /* Strip remaining span tags from Chroma highlighting */ -}}
{{- $inner = replaceRE `</?span[^>]*>` "" $inner -}}
{{- /* Strip <p> tags */ -}}
{{- $inner = replaceRE `</?p>` "" $inner -}}
{{- /* Decode HTML entities */ -}}
{{- $inner = $inner | htmlUnescape -}}

<!-- option: {{ $label }} -->
{{ $inner }}
<!-- /option -->
