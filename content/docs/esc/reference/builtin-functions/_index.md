---
title: Built-in Functions
title_tag: Built-in Functions
h1: Built-in Functions
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-reference
    identifier: esc-ref-builtin-functions
    weight: 3
---

ESC provides a number of built-in functions to help perform common value manipulations and to help access information stored outside of ESC.

All function invocations take the form of an object with a single key that names the function to invoke. The value of the key is the argument passed to the function. It is an error to attempt to invoke an unknown function, or for an object literal with multiple entries to contain a key with the prefix `fn::`.

## Functions

- [`fn::fromJSON`](/docs/esc/reference/builtin-functions/fn-from-json)
- [`fn::fromBase64`](/docs/esc/reference/builtin-functions/fn-from-base64)
- [`fn::join`](/docs/esc/reference/builtin-functions/fn-join)
- [`fn::open`](/docs/esc/reference/builtin-functions/fn-open)
- [`fn::rotate`](/docs/esc/reference/builtin-functions/fn-rotate)
- [`fn::secret`](/docs/esc/reference/builtin-functions/fn-secret)
- [`fn::toBase64`](/docs/esc/reference/builtin-functions/fn-to-base64)
- [`fn::toJSON`](/docs/esc/reference/builtin-functions/fn-to-json)
- [`fn::toString`](/docs/esc/reference/builtin-functions/fn-to-string)
