---
title: Built-in Functions
title_tag: Built-in Functions
h1: Built-in Functions
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/reference/esc-syntax/builtin-functions/
  - /docs/esc/reference/builtin-functions/
  - /docs/esc/environments/syntax/builtin-functions/
menu:
  esc:
    parent: esc-concepts
    identifier: esc-syntax-builtin-functions
    weight: 7
---

ESC provides a number of built-in functions to help perform common value manipulations and to help access information stored outside of ESC.

All function invocations take the form of an object with a single key that names the function to invoke. The value of the key is the argument passed to the function. It is an error to attempt to invoke an unknown function, or for an object literal with multiple entries to contain a key with the prefix `fn::`.

## Functions

- [`fn::secret`](/docs/esc/concepts/builtin-functions/fn-secret/)
- [`fn::concat`](/docs/esc/concepts/builtin-functions/fn-concat/)
- [`fn::final`](/docs/esc/concepts/builtin-functions/fn-final/)
- [`fn::fromBase64`](/docs/esc/concepts/builtin-functions/fn-from-base64/)
- [`fn::fromJSON`](/docs/esc/concepts/builtin-functions/fn-from-json/)
- [`fn::join`](/docs/esc/concepts/builtin-functions/fn-join/)
- [`fn::open`](/docs/esc/concepts/builtin-functions/fn-open/)
- [`fn::rotate`](/docs/esc/concepts/builtin-functions/fn-rotate/)
- [`fn::split`](/docs/esc/concepts/builtin-functions/fn-split/)
- [`fn::toBase64`](/docs/esc/concepts/builtin-functions/fn-to-base64/)
- [`fn::toJSON`](/docs/esc/concepts/builtin-functions/fn-to-json/)
- [`fn::toString`](/docs/esc/concepts/builtin-functions/fn-to-string/)
- [`fn::validate`](/docs/esc/concepts/builtin-functions/fn-validate/)
