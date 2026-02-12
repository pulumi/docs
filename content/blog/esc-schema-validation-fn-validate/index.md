---
title: "Schema Validation Comes to Pulumi ESC with fn::validate"
date: 2026-02-12T11:00:00-03:00
draft: false
meta_desc: "Validate configuration values against JSON Schema with fn::validate in Pulumi ESC."
meta_image: meta.png
authors:
    - pablo-terradillos
    - claire-gaestel
tags:
    - esc
    - features
schema_type: auto
social:
    twitter:
    linkedin:
aliases:
    - /blog/esc-schema-validation-fn-conform/
---

Pulumi ESC environments can now validate configuration values against JSON Schema with the new `fn::validate` built-in function. Invalid configurations are caught immediately when you save, preventing misconfigurations from reaching your deployments.
<!--more-->

Configuration errors are often discovered too late during deployment or, worse, in production. With `fn::validate`, you define validation rules directly in your environment, and ESC enforces them at save time. If a value doesn't match its schema, the environment cannot be saved until the issue is resolved.

## How it works

The `fn::validate` function takes a JSON Schema and a value. If the value conforms to the schema, it passes through unchanged. If not, ESC raises a validation error.

```yaml
values:
  port:
    fn::validate:
      schema: { type: number, minimum: 1, maximum: 65535 }
      value: 8080
```

This validates that `port` is a number between 1 and 65535. The evaluated result is simply `8080`.

## Validating objects with required fields

For complex configurations, you can enforce structure and required fields:

```yaml
values:
  database:
    fn::validate:
      schema:
        type: object
        properties:
          host: { type: string }
          port: { type: number }
          name: { type: string }
        required: [host, port, name]
      value:
        host: "db.example.com"
        port: 5432
        name: "myapp"
```

If any required field is missing or has the wrong type, the environment cannot be saved.

## Reusing schemas across environments

Define schemas once and reference them across multiple environments. Using the [`environments` built-in property](/docs/esc/environments/syntax/builtin-properties/environments/) keeps the schema out of your environment's output:

**Schema environment (my-project/schemas)**

```yaml
values:
  database-schema:
    type: object
    properties:
      host: { type: string }
      port: { type: number }
    required: [host, port]
```

**Environment using the schema**

```yaml
values:
  database:
    fn::validate:
      schema: ${environments.my-project.schemas.database-schema}
      value:
        host: "prod-db.example.com"
        port: 5432
```

This pattern ensures consistent validation rules across teams and projects.

## What happens when validation fails

When a value doesn't conform to its schema, ESC returns a clear error message:

```yaml
values:
  port:
    fn::validate:
      schema: { type: string }
      value: 8080
```

This raises: `expected string, got number`. The environment cannot be saved until you fix the value or update the schema.

## When to use schema validation

Enable `fn::validate` for:

- Values with specific type requirements (numbers, strings, arrays)
- Objects that must have certain fields present
- Numbers that must fall within a valid range
- Configurations shared across multiple environments
- Any value where catching errors early prevents downstream issues

## Getting started

The `fn::validate` function is available now in all Pulumi ESC environments. Add schema validation to your existing environments or use it when creating new ones.

For more information, see the [fn::validate documentation](/docs/esc/environments/syntax/builtin-functions/fn-validate/).
