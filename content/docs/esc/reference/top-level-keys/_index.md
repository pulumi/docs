---
title: Top-Level Keys
title_tag: Top-Level Keys
h1: Top-Level Keys
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-reference
    identifier: esc-ref-top-level-keys
    weight: 1
---

ESC defines two top-level keys that are available to environment authors: `imports` and `values`.

- __`imports`__: This top-level key is a list of other environments that this environment imports. Imported environments are evaluated and merged to form the basis for the current environment, which is then evaluated and merged with the imported values. For more information, see the [`imports` reference](/docs/esc/reference/top-level-keys/imports).
- __`values`__: This top-level key defines the contents of the environment--i.e. the values that this environment will produce when evaluated. For more information, see the [`values` reference](/docs/esc/reference/top-level-keys/values).
