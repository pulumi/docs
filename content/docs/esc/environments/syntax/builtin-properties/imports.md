---
title: imports
title_tag: imports
h1: imports
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/reference/esc-syntax/builtin-properties/imports/
  - /docs/esc/reference/builtin-properties/imports/
menu:
  esc:
    parent: esc-syntax-builtin-properties
    identifier: esc-syntax-builtin-imports
    weight: 3
---

The `imports` built-in property provides access to imported environments. This allows the selective use of values from imported environments, including those that are imported without participating in the merge stack (i.e. imported with [`merge: false`](/docs/esc/environments/syntax/top-level-keys/imports/#available-options)).

## Properties

| Property | Type | Description                                                       |
|----------|------|-------------------------------------------------------------------|
| import   | any  | The imported environment to access

## Example

In the following example, the `app/dev` environment is imported with `merge: false`, so its values are not merged into the current environment. Instead, they are accessed explicitly via the `imports` built-in:

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
