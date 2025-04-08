---
title: environments
title_tag: environments
h1: environments
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-builtin-properties
    identifier: esc-ref-builtin-environments
    weight: 2
---

The `environments` built-in property provides access to other environments within the same organization. This allows the selective use of values from other environments without explicitly importing those environments.

## Properties

| Property | Type                           | Description                                                       |
|----------|--------------------------------|-------------------------------------------------------------------|
| project  | [ESCProject](#pulumicontext)   | The project that contains the environment to access

### ESCProject

| Property       | Type   | Description                                                       |
|----------------|--------|-------------------------------------------------------------------|
| environment    | any    | The environment to access

## Example

```yaml
values:
  other: Hello, ${environments.app.dev.name}!
```

### Evaluated result

```json
{
  "greeting": "Hello, My App!"
}
```
