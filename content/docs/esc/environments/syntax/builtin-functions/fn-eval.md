---
title: fn::eval
title_tag: fn::eval
h1: fn::eval
meta_desc: The fn::eval built-in function evaluates a template expression in the context of the current environment.
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-eval
    weight: 2
---

The `fn::eval` built-in function evaluates a [template expression](/docs/esc/environments/syntax/builtin-functions/fn-template/) in the context of the current environment. Together with `fn::template`, it enables late binding — the ability to define reusable expressions in one environment and evaluate them with different values in another.

## Declaration

```yaml
fn::eval: template-reference
```

### Parameters

| Property             | Type | Description                                                                                              |
|----------------------|------|----------------------------------------------------------------------------------------------------------|
| `template-reference` | any  | A reference to a value defined with `fn::template`. Typically an interpolation like `${environments.org.defn.my-template}`. |

### Returns

The result of evaluating the referenced template in the context of the calling environment. The template's interpolations are resolved using the values available in the environment where `fn::eval` is called, not where the template is defined.

## Example

### Reusable greeting template

This example shows how to define a template in one environment and evaluate it in multiple environments with different values.

#### Template environment (example/defn)

```yaml
values:
  hello:
    fn::template: Hello ${name}!
```

The `fn::template` expression defines a template that references `${name}`. The interpolation is not resolved in this environment — it is deferred until a consumer evaluates it with `fn::eval`.

#### Consumer environment A (example/a)

```yaml
values:
  name: "foo"
  example:
    fn::eval: ${environments.example.defn.hello}
```

#### Consumer environment B (example/b)

```yaml
values:
  name: "bar"
  example:
    fn::eval: ${environments.example.defn.hello}
```

#### Parent environment

```yaml
values:
  a: ${environments.example.a}
  b: ${environments.example.b}
```

#### Evaluated result

```json
{
  "a": {
    "example": "Hello foo!",
    "name": "foo"
  },
  "b": {
    "example": "Hello bar!",
    "name": "bar"
  }
}
```

Environment A resolves the template with `name: "foo"`, producing `"Hello foo!"`. Environment B resolves the same template with `name: "bar"`, producing `"Hello bar!"`.

## Related functions

- [`fn::template`](/docs/esc/environments/syntax/builtin-functions/fn-template/) — defines a template expression for deferred evaluation.
