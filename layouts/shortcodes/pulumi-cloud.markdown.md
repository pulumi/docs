{{- $edition := .Get 0 -}}
{{- $out := slice -}}
{{- if or $edition (not .Inner) }}{{ $out = $out | append (partial "cloud-availability-body.html" (dict "edition" $edition "where" $.Page.File.Path)) }}{{ end -}}
{{- /* Trim both ends: `.Inner` keeps the newline after the opening tag, and a
       leading newline would become an empty `> ` line below. */ -}}
{{- with .Inner }}{{ $out = $out | append (trim . "\n") }}{{ end -}}

{{ replaceRE `(?m)^` "> " (delimit $out "\n\n") | safeHTML }}

