{{- $resource := default "resource" (.Get "resource") -}}
{{- $suffix := default "abc123" (.Get "suffix") -}}

> **Note:** The extra characters you see tacked onto the {{ $resource }} name (`-{{ $suffix }}`) are the result of *auto-naming*, a feature that lets you use the same resource names across multiple stacks without naming collisions. You can disable or fine-tune this. To learn how, [read more about auto-naming](/docs/concepts/resources/names/#autonaming).
