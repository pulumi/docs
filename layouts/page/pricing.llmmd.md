# {{ .Title }}

{{ with .Params.meta_desc }}
{{ . }}
{{ end }}

## Pricing Plans

{{ range .Params.tiers.trialed.items }}
### {{ .title }}
{{ .subtitle }}

**Pulumi IaC:** {{ .iac_price }}{{ if .iac_unit }} {{ .iac_unit }}{{ end }}{{ if .iac_note }} ({{ .iac_note }}){{ end }}
{{ if .esc_price }}**Pulumi ESC:** {{ .esc_price }}{{ if .esc_unit }} {{ .esc_unit }}{{ end }}{{ if .esc_note }} ({{ .esc_note }}){{ end }}{{ end }}
{{ if .insights_price }}**Pulumi Insights:** {{ .insights_price }}{{ if .insights_unit }} {{ .insights_unit }}{{ end }}{{ if .insights_note }} ({{ .insights_note }}){{ end }}{{ end }}

{{ .items }}

{{ end }}

## Feature Comparison

{{ range .Params.comparison_table.sections }}
### {{ .header }}

{{ range .tables }}
#### {{ .header }}
{{ with .subheader }}{{ . }}{{ end }}

| Feature | Free | Team | Enterprise | Business Critical |
|---------|------|------|------------|-------------------|
{{ range .rows }}| {{ .title }} | {{ range $index, $item := .items }}{{ if eq $item.content "_check" }}✓{{ else if eq $item.content "_blank" }}—{{ else }}{{ $item.content | markdownify | plainify }}{{ end }}{{ if ne $index 3 }} | {{ end }}{{ end }} |
{{ end }}

{{ end }}
{{ end }}

## Customer Success Stories

{{ range .Params.customers }}
- {{ .stat | markdownify | plainify }}
{{ end }}

## Frequently Asked Questions

{{ range .Params.faq }}
### {{ .category }}

{{ range .items }}
**{{ .question }}**

{{ .answer }}

{{ end }}
{{ end }}