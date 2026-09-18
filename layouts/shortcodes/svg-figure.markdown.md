{{- /* The SVG lives under assets/ and is inlined into the HTML output, so it has
       no published URL to link to here. Render the figure as its caption plus
       the text alternative, which is what a reader of the markdown needs. */ -}}
{{- $n := .Get "n" -}}
{{- $alt := .Get "alt" -}}

*{{ with $n }}Figure {{ . }}. {{ end }}{{ trim .Inner "\n " }}*{{ with $alt }} (Diagram: {{ . }}){{ end }}
