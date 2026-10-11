{{- $key := .Get 0 -}}
{{- $data := index site.Data.resource_options $key -}}
{{- $body := partial "resource-option-scope-body.html" (dict "name" $key "data" $data) -}}

> {{ $body }}
