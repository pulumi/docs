---
title: values
title_tag: values
h1: values
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-top-level-keys
    identifier: esc-ref-values
    weight: 2
---

The `values` top-level key defines the environment's values--i.e. the properties and values that the environment will produce when evaluated.

The value of this key must be a mapping from string literals (property names) to ESC values.

ESC values include standard YAML values, [interpolations and references](/docs/esc/reference/interpolations-and-references), and [function calls](/docs/esc/reference/builtin-functions).

Here is an example definition that uses the `values` section:

```yaml
values:
  bool-value: true
  number-value: 3.14
  string-value: hello!
  list-value:
    - entry 1
    - entry 2
  mapping-value:
    bool: ${bool-value}
    number: ${number-value}
    string: ${string-value}
```

When evaluated, this environment will produce the following result:

```json
{
  "bool-value": true,
  "number-value": 3.14,
  "string-value": "hello!",
  "list-value": [
    "entry 1",
    "entry 2"
  ],
  "mapping-value": {
    "bool": true,
    "number": 3.14,
    "string": "hello!"
  }
}
```
