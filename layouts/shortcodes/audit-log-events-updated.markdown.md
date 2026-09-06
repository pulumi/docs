{{- with (site.Data.audit_log_events_updated).updated -}}
Event list last updated on {{ . }}, synced automatically from the Pulumi Cloud API.
{{- end -}}
