---
title: {{ .Title }}
{{ with .Params.meta_desc }}description: {{ replaceRE `\s+` " " (trim . " \n") }}
{{ end }}url: {{ .RelPermalink }}
---
{{ with .Params.meta_desc }}{{ replaceRE `\s+` " " (trim . " \n") }}
{{ end }}
{{- /* Editions and the comparison matrix both come from data/pulumi_pricing.yaml,
       the same file pricing.html renders as cards and rows. */}}
{{- $px := partialCached "pricing/data.html" . "pricing-data" }}
{{- range $px.editions }}
{{- $card := .card | default dict }}
## {{ .name }}
{{ with $card.subtitle }}
{{ . }}
{{ end }}
**{{ $card.price }}{{ with $card.price_label }} {{ . }}{{ end }}**{{ with $card.unit }} — {{ . }}{{ end }}{{ with $card.note }} ({{ . }}){{ end }}
{{ with $card.features }}
{{ with $card.features_intro }}{{ . }}{{ end }}
{{- range . }}
- {{ . }}
{{- end }}
{{ end }}
{{- end }}
{{- /* Edition comparison: one markdown table per category, with the edition names
       as columns. The old frontmatter used `_check`/`_blank` sentinels for the
       icon cells; the data file says the same thing with a bool, which
       pricing/value.html normalizes into a "check" or "blank" kind. Hidden
       features have no row on /pricing/, so they get none here either. */}}
{{- $editionNames := slice }}
{{- range $px.editions }}{{ $editionNames = $editionNames | append .name }}{{ end }}

## Edition comparison
{{ range $px.groups }}
{{- range .categories }}

### {{ .name }}

| | {{ delimit $editionNames " | " }} |
|---|{{ range $editionNames }}---|{{ end }}
{{- range .features }}
{{- if not .hidden }}
{{- $feature := . }}
| {{ replace .name "|" "\\|" }} |
{{- range $px.editions }}
{{- $cell := partial "pricing/value.html" (index $feature.cells .id) }}
{{- if eq $cell.kind "check" }} ✓
{{- else if eq $cell.kind "text" }} {{ replace (replace $cell.content "\n" " ") "|" "\\|" }}
{{- else }} —
{{- end }}
{{- with $cell.subtext }} ({{ replace (replace . "\n" " ") "|" "\\|" }}){{ end }} |
{{- end }}
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
