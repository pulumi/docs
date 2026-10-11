{{- $src := .Get "src" -}}
{{- $title := default "Video" (.Get "title") -}}
[{{ $title }}]({{ $src }})
