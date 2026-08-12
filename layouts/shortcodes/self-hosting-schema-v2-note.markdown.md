{{- $inner := trim (printf "%s" .Inner) " \t\n\r" -}}

> **Warning:** **Upgrading an existing installation?** The current installers enable the V2 engine events database schema (`PULUMI_ENGINE_EVENTS_SCHEMA_V2`). Moving an existing installation onto it requires a database migration that Pulumi performs with you. [Contact Pulumi support](/support/) before pointing an existing install at a current installer version or changing `PULUMI_ENGINE_EVENTS_SCHEMA_V2` or `PULUMI_ENGINE_EVENTS_LEGACY_WRITE`. Fresh installations are unaffected.{{ with $inner }} {{ . }}{{ end }}
