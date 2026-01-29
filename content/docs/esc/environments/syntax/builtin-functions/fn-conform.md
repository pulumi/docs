---
title: fn::conform
title_tag: fn::conform
h1: fn::conform
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-conform
    weight: 2
---

The `fn::conform` built-in function validates a value against a JSON Schema. If the value does not conform to the schema, a validation error is raised and the environment cannot be saved until the issues are resolved.

## Declaration

```yaml
fn::conform:
  schema: json-schema
  value: value-to-validate
```

### Parameters

| Property | Type   | Description                                          |
|----------|--------|------------------------------------------------------|
| `schema` | object | A JSON Schema definition to validate the value against.
| `value`  | any    | The value to validate.

### Returns

If validation passes, the original `value` is returned. If validation fails, an error is raised and the environment cannot be saved.

## Example

### Basic type validation

#### Definition

```yaml
values:
  valid-string:
    fn::conform:
      schema: { type: string }
      value: "hello"
```

#### Evaluated result

```json
{
  "valid-string": "hello"
}
```

### Number constraints

#### Definition

```yaml
values:
  validated-number:
    fn::conform:
      schema: { type: number, minimum: 0 }
      value: 42
```

#### Evaluated result

```json
{
  "validated-number": 42
}
```

### Object with required fields

#### Definition

```yaml
values:
  user:
    fn::conform:
      schema:
        type: object
        properties:
          name: { type: string }
          email: { type: string }
        required: [name, email]
      value:
        name: "Alice"
        email: "alice@example.com"
```

#### Evaluated result

```json
{
  "user": {
    "name": "Alice",
    "email": "alice@example.com"
  }
}
```

### Dynamic schema from reference

You can define schemas as values and reference them dynamically:

#### Definition

```yaml
values:
  my-schema:
    type: string
    minLength: 1
  validated:
    fn::conform:
      schema: ${my-schema}
      value: "hello"
```

#### Evaluated result

```json
{
  "my-schema": {
    "type": "string",
    "minLength": 1
  },
  "validated": "hello"
}
```

### Array validation

#### Definition

```yaml
values:
  tags:
    fn::conform:
      schema:
        type: array
        items: { type: string }
      value: ["production", "us-east-1"]
```

#### Evaluated result

```json
{
  "tags": ["production", "us-east-1"]
}
```

### Reusing schemas from other environments

You can define schemas in a separate environment and reference them for reuse across multiple environments. This allows you to centralize schema definitions and ensure consistent validation.

Using the [`environments` built-in property](/docs/esc/environments/syntax/builtin-properties/environments/) to reference the schema is the recommended approach because it doesn't merge the schema into your environment's output.

#### Schema environment (myproj/schemas)

```yaml
values:
  user-schema:
    type: object
    properties:
      name: { type: string }
      email: { type: string }
    required: [name, email]
```

#### Environment using the schema reference

```yaml
values:
  user:
    fn::conform:
      schema: ${environments.myproj.schemas.user-schema}
      value:
        name: "Alice"
        email: "alice@example.com"
```

#### Evaluated result

```json
{
  "user": {
    "name": "Alice",
    "email": "alice@example.com"
  }
}
```

This pattern is useful for enforcing consistent validation rules across teams and projects.

## Validation errors

When a value does not conform to its schema, `fn::conform` raises an error that prevents the environment from being saved. This ensures configuration issues are caught before the environment is used.

### Example: type mismatch

```yaml
values:
  type-error:
    fn::conform:
      schema: { type: string }
      value: 42
```

This raises an error: `expected string, got number`. The environment cannot be saved until the value conforms to the schema.

### Example: missing required field

```yaml
values:
  missing-required:
    fn::conform:
      schema:
        type: object
        properties:
          name: { type: string }
        required: [name]
      value:
        other: "value"
```

This raises an error indicating that the required field `name` is missing. The environment cannot be saved until the required field is provided.
