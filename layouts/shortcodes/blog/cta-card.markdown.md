{{- $title := .Get "title" | default "Program the Cloud" -}}
{{- $label := .Get "label" | default site.Params.cta.primary.label -}}
{{- $href := .Get "href" | default site.Params.cta.primary.href -}}
{{- $text := "Create, deploy, and manage cloud infrastructure using your favorite language." -}}
{{- with trim .Inner " \n\t\r" }}{{ $text = . }}{{ end -}}
**{{ $title }}**

{{ $text }}

[{{ $label }}]({{ $href }})
