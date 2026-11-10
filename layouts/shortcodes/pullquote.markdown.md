{{- $attribution := .Get "attribution" -}}
{{- $variant := .Get "variant" -}}
{{- $inner := trim .Inner "\n " -}}
{{- if eq $variant "statement" }}
**{{ $inner }}**
{{- else }}
> {{ $inner }}{{ with $attribution }}
>
> — {{ . }}{{ end }}
{{- end }}
