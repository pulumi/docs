{{- $idp := .Get "idp" | default "your Identity Provider" -}}
Pulumi supports only one Pulumi organization per SCIM application. If your team manages multiple Pulumi organizations, you must configure separate SCIM applications for each organization in {{ $idp }}.
