---
title: values
title_tag: values
h1: values
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-ref-top-level-properties
    identifier: esc-ref-values
    weight: 2
---

The `values` top-level property defines the environment's values--i.e. the properties and values that the environment will produce when evaluated.

The value of this property must be a mapping from static strings (property names) to ESC values.

ESC values include standard YAML values, [symbols and interpolations](/docs/esc/reference/value-references), and [function calls](/docs/esc/reference/builtin-functions).

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
