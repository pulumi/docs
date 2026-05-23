{{- $labels := dict
  "both" "Custom and component"
  "component" "Component only"
  "custom" "Custom only"
  "provider" "Provider only" -}}
| Resource option | Description | Applies to |
|---|---|---|
{{ range $name, $d := site.Data.resource_options -}}
| [{{ $name }}](/docs/iac/concepts/resources/options/{{ lower $name }}/) | {{ chomp $d.description }} | {{ index $labels $d.applies_to }} |
{{ end -}}
