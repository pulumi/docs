{{- /* Plain-Markdown rendering of the audit log event catalog, for the .md
       output format. See audit-log-events.html for how the data is produced. */ -}}
{{- $categories := site.Data.audit_log_event_categories -}}
{{- $events := (site.Data.audit_log_events).eventTypes -}}
{{ range $categories }}{{ $category := . }}{{ $matching := where $events "category" $category.id }}{{ if $matching }}
## {{ $category.name }}

{{ $category.description }}

| Event | Event ID | Description |
|---|---|---|
{{ range sort $matching "displayName" -}}
{{- $notes := slice -}}
{{- if .requiresOrgAdmin }}{{ $notes = $notes | append "Requires organization admin." }}{{ end -}}
{{- if .requiresStackAdmin }}{{ $notes = $notes | append "Requires stack admin." }}{{ end -}}
{{- if .authenticationFailure }}{{ $notes = $notes | append "Recorded as an authentication failure." }}{{ end -}}
{{- $description := replace (chomp .description) "|" "\\|" -}}
{{- with $notes }}{{ $description = printf "%s _%s_" $description (delimit . " ") }}{{ end -}}
| {{ replace .displayName "|" "\\|" }} | `{{ .event }}` | {{ $description }} |
{{ end }}{{ end }}{{ end }}
