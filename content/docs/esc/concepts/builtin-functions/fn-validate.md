---
title: fn::validate
title_tag: fn::validate
h1: fn::validate
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/esc/environments/syntax/builtin-functions/fn-conform/
  - /docs/esc/environments/syntax/builtin-functions/fn-validate/
menu:
  esc:
    parent: esc-syntax-builtin-functions
    identifier: esc-syntax-fn-validate
    weight: 13
---

The `fn::validate` built-in function validates a value against a JSON Schema. If the value does not conform to the schema, a validation error is raised and the environment cannot be saved until the issues are resolved.

## Declaration

```yaml
fn::validate:
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

## Validation errors

When a value does not conform to its schema, `fn::validate` raises an error that prevents the environment from being saved. This ensures configuration issues are caught before the environment is used.

### Example: type mismatch

```yaml
values:
  type-error:
    fn::validate:
      schema: { type: string }
      value: 42
```

This raises an error: `expected string, got number`. The environment cannot be saved until the value conforms to the schema.

### Example: missing required field

```yaml
values:
  missing-required:
    fn::validate:
      schema:
        type: object
        properties:
          name: { type: string }
        required: [name]
      value:
        other: "value"
```

This raises an error indicating that the required field `name` is missing. The environment cannot be saved until the required field is provided.
