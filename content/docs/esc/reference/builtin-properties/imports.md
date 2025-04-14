---
title: imports
title_tag: imports
h1: imports
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-builtin-properties
    identifier: esc-ref-builtin-imports
    weight: 3
---

The `imports` built-in property provides access to imported environments. This allows the selective use of values from imported environments, including those that are imported without participating in the merge stack.

## Properties

| Property | Type | Description                                                       |
|----------|------|-------------------------------------------------------------------|
| import   | any  | The imported environment to access

## Example

```yaml
imports:
  - app/dev: { merge: false }
values:
  other: Hello, ${imports["app/dev"].name}!
```

### Evaluated result

```json
{
  "greeting": "Hello, My App!"
}
```
