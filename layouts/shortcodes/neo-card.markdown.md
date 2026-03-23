{{- $title := .Get "title" -}}
{{- $prompt := .Get "prompt" | default $title -}}
{{- $href := printf "https://app.pulumi.com/neo?prompt=%s" ($prompt | urlquery) -}}
[{{ $title }}]({{ $href }})
