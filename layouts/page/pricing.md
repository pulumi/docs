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
{{- /* Cost estimation: the same numbers the /pricing/#calculator sliders compute
       with, from `calculator:` in data/pulumi_pricing.yaml. The HTML page hands an
       agent a slider it can't move, so state the per-unit rates and the model
       outright. Rates are monthly; the comparison table above carries the hourly
       form of each one. */}}
{{- with site.Data.pulumi_pricing.calculator }}
{{- $c := . }}

## Cost estimation

An estimate at list prices, excluding taxes, committed-use discounts, and volume pricing. All usage draws from one shared pool of Pulumi Credits, where 1 credit costs $1 USD.
{{ range $e := $px.editions }}
{{- with index $c.editions $e.id }}

**{{ $e.name }}** — ${{ .base_usd }}/month base, which includes {{ .included_credits }} credits and covers up to {{ lang.FormatNumberCustom 0 .included_resources }} IaC resources.

| Unit | Rate |
|---|---|
| IaC resource, per month | ${{ partial "pricing/rate.html" .iac_resource_month }} |
| ESC secret, per month | ${{ partial "pricing/rate.html" .esc_secret_month }} |
| Discovered resource, per month | ${{ partial "pricing/rate.html" .insights_resource_month }} |
| Workflow minute | ${{ partial "pricing/rate.html" $c.meters.workflow_minute }} |
| 1M Neo tokens | ${{ partial "pricing/rate.html" $c.meters.neo_tokens_per_million }} |
{{- end }}
{{- end }}

The rates above are per whole month. IaC resources and discovered resources are really billed by the hour, so infrastructure that exists for only part of the month costs proportionally less; ESC secrets are billed for the full month either way. The base price covers the included resource count, and usage beyond the included credits is billed on demand. Past about {{ lang.FormatNumberCustom 0 $c.contact_sales_resources }} IaC resources, volume pricing usually applies, so figures computed from the rates above are an upper bound rather than a quote — [contact sales](/contact/?form=sales) for what it would actually cost at that size. An interactive estimator is at /pricing/#calculator.
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
