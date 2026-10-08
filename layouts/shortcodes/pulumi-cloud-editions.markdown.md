{{- /* Plain-text rendition of pulumi-cloud-editions.html; see that file. */ -}}
{{- $feature := .Get 0 -}}
{{- $px := partialCached "pricing/data.html" "pricing-data" "pricing-data" -}}
{{- $names := partial "pricing/feature-editions.html" (dict "feature" $feature "where" .Page.File.Path) -}}
{{- if eq (len $names) (len $px.editions) -}}
  All editions
{{- else -}}
  {{- delimit $names ", " -}}
{{- end -}}
