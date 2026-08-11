{{- /* Markdown-output variant of pulumi-languages.html. Keep the two in step. */ -}}
{{- $set := default (.Get "set") (.Get 0) -}}
{{- $set = default "all" $set -}}
{{- $links := eq (.Get "links") "true" -}}
{{- if eq $set "general-purpose" -}}
Python, TypeScript, JavaScript, Go, .NET, and Java
{{- else if $links -}}
Python, TypeScript, JavaScript, Go, .NET, Java, [YAML](/docs/iac/languages-sdks/yaml/), and [HCL](/docs/iac/languages-sdks/hcl/)
{{- else -}}
Python, TypeScript, JavaScript, Go, .NET, Java, YAML, and HCL
{{- end -}}
