---
title: Built-in Functions
title_tag: Built-in Functions
h1: Built-in Functions
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  reference:
    parent: reference-esc-syntax
    identifier: esc-ref-builtin-functions
    weight: 3
---

ESC provides a number of built-in functions to help perform common value manipulations and to help access information stored outside of ESC.

All function invocations take the form of an object with a single key that names the function to invoke. The value of the key is the argument passed to the function. It is an error to attempt to invoke an unknown function, or for an object literal with multiple entries to contain a key with the prefix `fn::`.

## Functions

- [`fn::fromJSON`](/docs/reference/esc-syntax/builtin-functions/fn-from-json)
- [`fn::fromBase64`](/docs/reference/esc-syntax/builtin-functions/fn-from-base64)
- [`fn::join`](/docs/reference/esc-syntax/builtin-functions/fn-join)
- [`fn::concat`](/docs/reference/esc-syntax/builtin-functions/fn-concat)
- [`fn::open`](/docs/reference/esc-syntax/builtin-functions/fn-open)
- [`fn::rotate`](/docs/reference/esc-syntax/builtin-functions/fn-rotate)
- [`fn::secret`](/docs/reference/esc-syntax/builtin-functions/fn-secret)
- [`fn::toBase64`](/docs/reference/esc-syntax/builtin-functions/fn-to-base64)
- [`fn::toJSON`](/docs/reference/esc-syntax/builtin-functions/fn-to-json)
- [`fn::toString`](/docs/reference/esc-syntax/builtin-functions/fn-to-string)

## Examples

### Valid function invocation

```yaml
valid:
  fn::join: [ " ", [ "hello", "world" ] ]
```

### Too many keys

```yaml
tooManyKeys:
  fn::join: [ " ", [ "hello", "world" ] ]
  fn::toString: { "hello": "world" }
```

### Unknown function

```yaml
unknownFunction:
  fn::undefined: {}
```
