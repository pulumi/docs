---
title: Interpolations and References
title_tag: Interpolations and References
h1: Interpolations and References
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/reference/esc-syntax/interpolations-and-references/
  - /docs/esc/reference/interpolations-and-references/
  - /docs/esc/environments/syntax/interpolations-and-references/
  - /docs/esc/environments/syntax/builtin-properties/
  - /docs/reference/esc-syntax/builtin-properties/
  - /docs/esc/reference/builtin-properties/
  - /docs/esc/environments/syntax/builtin-properties/context/
  - /docs/reference/esc-syntax/builtin-properties/context/
  - /docs/esc/reference/builtin-properties/context/
  - /docs/esc/environments/syntax/builtin-properties/environments/
  - /docs/reference/esc-syntax/builtin-properties/environments/
  - /docs/esc/reference/builtin-properties/environments/
  - /docs/esc/environments/syntax/builtin-properties/imports/
  - /docs/reference/esc-syntax/builtin-properties/imports/
  - /docs/esc/reference/builtin-properties/imports/
menu:
  esc:
    parent: esc-concepts
    identifier: esc-syntax-interpolations-and-references
    weight: 6
---

Interpolations and references are additional syntactical constructs that ESC layers on top of YAML to allow users to reuse properties to construct new values.

References take the form `${property-path}`. References may appear alone or embedded within strings. The former case is referred to as a _bare reference_; the latter is an _interpolation_.

## Property paths

Property paths--[used throughout the Pulumi ecosystem](/docs/reference/property-paths/)--are JavaScript-inspired expressions that refer to properties within JSON-like values.

The syntax supports both dot notation and bracket notation.
For keys that contain special characters (i.e. `[`, `]`, `"`, or `.`) or begin with a digit,
bracket notation is required.

## Binding references

In the context of ESC, references either refer to properties in the evaluated environment in which they are contained or to [built-in properties](#built-in-properties).

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

Interpolations evaluate to the [string representation](/docs/esc/concepts/builtin-functions/fn-to-string/) of the referenced value.

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

## Built-in properties

In addition to referencing properties defined within an environment, references can access several built-in properties: information about the user evaluating an environment (`context`), other environments in the organization (`environments`), and imported environments (`imports`).

### context

The `context` built-in property provides information about the user evaluating an ESC environment. It exposes the login of the requesting user at `context.pulumi.user.login` and the login of their organization at `context.pulumi.organization.login`.

```yaml
values:
  greeting: Hello, ${context.pulumi.organization.login}/${context.pulumi.user.login}!
```

### environments

The `environments` built-in property provides access to other environments within the same organization. This allows the selective use of values from other environments without explicitly importing them. Reference a value as `${environments.<project>.<environment>.<property-path>}`.

```yaml
values:
  other: Hello, ${environments.app.dev.name}!
```

### imports

The `imports` built-in property provides access to imported environments, including those that are imported without participating in the merge stack (`merge: false`). For details on importing environments, see [Imports](/docs/esc/concepts/imports/).

```yaml
imports:
  - app/dev: { merge: false }
values:
  other: Hello, ${imports["app/dev"].name}!
```
