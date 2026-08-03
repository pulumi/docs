---
title: {{ .Title }}
{{ with .Params.meta_desc }}description: {{ replaceRE `\s+` " " (trim . " \n") }}
{{ end }}url: {{ .RelPermalink }}
---
{{ with .Params.meta_desc }}{{ replaceRE `\s+` " " (trim . " \n") }}
{{ end }}
{{- /* Editions: the tiers frontmatter that pricing.html renders as cards. */}}
{{ range .Params.tiers.trialed.items }}
{{- $item := . }}
## {{ .title }}
{{ with .subtitle }}
{{ . }}
{{ end }}
**{{ .price }}{{ with .price_label }} {{ . }}{{ end }}**{{ with .unit }} — {{ . }}{{ end }}{{ with .note }} ({{ . }}){{ end }}
{{ with $item.features }}
{{ with $item.features_intro }}{{ . }}{{ end }}
{{- range . }}
- {{ . }}
{{- end }}
{{ end }}
{{- end }}
{{- /* Edition comparison: mirror the comparison_table frontmatter as markdown
       tables, one per product area, with the tier names as columns. */}}
{{- $tierNames := slice }}
{{- range .Params.tiers.trialed.items }}{{ $tierNames = $tierNames | append .title }}{{ end }}
{{- with .Params.comparison_table }}
## Edition comparison
{{ range .sections }}
{{- range .tables }}

### {{ .header }}

| | {{ delimit $tierNames " | " }} |
|---|{{ range $tierNames }}---|{{ end }}
{{- range .rows }}
| {{ replace .title "|" "\\|" }} |
{{- range .items }} {{ with .content }}
{{- /* _check/_blank are sentinels the HTML table renders as icons. */ -}}
{{- if eq . "_check" }}✓{{ else if eq . "_blank" }}—{{ else }}{{ replace (replace . "\n" " ") "|" "\\|" }}{{ end }}{{ end }}{{ with .subtext }} ({{ replace . "|" "\\|" }}){{ end }} |{{ end }}
{{- end }}
{{- end }}
{{- end }}
{{- end }}
{{- /* FAQ: high-value for agents; answers are markdown in frontmatter. */}}
{{- with .Params.faq }}

## Frequently asked questions
{{ range . }}
### {{ .category }}
{{ range .items }}
**{{ .question }}**

{{ trim .answer " \n" }}
{{ end }}
{{- end }}
{{- end }}
