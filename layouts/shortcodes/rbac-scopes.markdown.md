{{- /* Plain-Markdown rendering of the RBAC scope reference, for the .md output
       format. See rbac-scopes.html. */ -}}
{{- $id := .Get 0 -}}
{{- $entity := partial "rbac/entity.html" $id -}}
{{- range $entity.sections }}
## {{ .name }}

{{ partial "rbac/scope-table.html" (dict "entity" $id "section" .) }}
{{- end -}}
