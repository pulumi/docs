---
title: fn::template
title_tag: fn::template
h1: fn::template
meta_desc: The fn::template built-in function defines a template expression with deferred evaluation for use with fn::eval.
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-template
    weight: 11
---

The `fn::template` built-in function defines a template expression whose interpolations are not resolved immediately. Instead, the template is evaluated later when a consumer environment references it with [`fn::eval`](/docs/esc/environments/syntax/builtin-functions/fn-eval/). This enables late binding — defining reusable expressions in one environment and evaluating them with different values in another.

## Declaration

```yaml
fn::template: expression
```

### Parameters

| Property     | Type   | Description                                                                                       |
|--------------|--------|---------------------------------------------------------------------------------------------------|
| `expression` | any    | An expression containing interpolations (e.g., `Hello ${name}!`). The interpolations are not resolved in the defining environment — they are deferred until evaluation with `fn::eval`. |

### Returns

A template value that can be referenced by other environments. The template is not evaluated in the defining environment. It produces a result only when consumed via `fn::eval`.

## Example

### Defining a reusable template

#### Template environment (example/defn)

```yaml
values:
  hello:
    fn::template: Hello ${name}!
```

This defines a template that references `${name}`. The value of `name` is determined by the environment that evaluates the template.

#### Consumer environment (example/a)

```yaml
values:
  name: "foo"
  example:
    fn::eval: ${environments.example.defn.hello}
```

#### Evaluated result

```json
{
  "example": "Hello foo!",
  "name": "foo"
}
```

The template resolves `${name}` to `"foo"` because that is the value of `name` in the consumer environment.

### Using templates for standardized configuration

Templates are useful for enforcing consistent patterns across environments. For example, you can define a naming convention template and have all environments evaluate it with their own values:

#### Template environment (org/templates)

```yaml
values:
  resource-name:
    fn::template: ${project}-${environment}-${region}
```

#### Consumer environment (org/prod-us)

```yaml
values:
  project: "myapp"
  environment: "prod"
  region: "us-east-1"
  name:
    fn::eval: ${environments.org.templates.resource-name}
```

#### Evaluated result

```json
{
  "project": "myapp",
  "environment": "prod",
  "region": "us-east-1",
  "name": "myapp-prod-us-east-1"
}
```

## Related functions

- [`fn::eval`](/docs/esc/environments/syntax/builtin-functions/fn-eval/) — evaluates a template expression in the context of the current environment.
