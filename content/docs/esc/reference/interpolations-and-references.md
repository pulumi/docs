---
title: Interpolations and References
title_tag: Interpolations and References
h1: Interpolations and References
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-reference
    identifier: esc-ref-interpolations-and-references
    weight: 2
---

Interpolations and references are additional syntactical constructs that ESC layers on top of YAML to allow users to reuse properties to construct new values.

References take the form `${property-path}`. References may appear alone or embedded within strings. The former case is referred to as a _bare reference_; the latter is an _interpolation_.

## Property paths

Property paths--[used throughout the Pulumi ecosystem](/docs/iac/concepts/miscellaneous/property-paths)--are JavaScript-inspired expressions that refer to properties within JSON-like values.

The syntax supports both dot notation and bracket notation.
For keys that contain special characters (i.e. `[`, `]`, `"`, or `.`) or begin with a digit,
bracket notation is required.

## Binding references

In the context of ESC, references either refer to properties in the evaluated environment in which they are contained or to [built-in properties](/docs/esc/reference/builtin-properties).

Interpolations and references are _early-bound_: each reference is evaluated within the context of the environment in which it is contained. This allows the author of an environment definition to reliably predict the form of the value referred to by a reference.

Early binding contrasts with late binding, which would evaluate references within the context of the top-level environment and its entire import stack. [ESC does not currently support late-bound references](https://github.com/pulumi/esc/issues/127).

## Bare references

Bare references evaluate to a copy of the referenced value.

### Example

```yaml
values:
  user:
    name: Real Name
    login: user-login
  user-copy: ${user}
```

#### Evaluated result

```json
{
  "user": {
    "name": "Real Name",
    "login": "user-login"
  },
  "user-copy": {
    "name": "Real Name",
    "login": "user-login"
  }
}
```

## Interpolations

Interpolations evaluate to the [string representation](/docs/esc/reference/builtin-functions/fn-to-string) of the referenced value.

### Example

```yaml
values:
  user:
    name: Real Name
    login: user-login
  greeting: Hello, ${user.name}!
```

#### Evaluated result

```json
{
  "user": {
    "name": "Real Name",
    "login": "user-login"
  },
  "greeting": "Hello, Real Name!"
}
```
