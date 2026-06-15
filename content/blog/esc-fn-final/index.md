---
title: "Lock Down Values in Pulumi ESC with fn::final"
date: 2026-03-17T11:00:00-07:00
draft: false
meta_desc: "Mark configuration values as final in Pulumi ESC to prevent child environments from overriding them with fn::final."
meta_image: meta.png
feature_image: feature.png
authors:
    - pablo-terradillos
    - sean-yeh
tags:
    - esc
    - features
categories:
    - product-launches
    - security-governance
schema_type: auto
---

[Pulumi ESC (Environments, Secrets, and Configuration)](/docs/esc/) allows you to compose environments by importing configuration and secrets from other environments, but this also means a child environment can silently override a value set by a parent. When that value is a security policy or a compliance setting, an accidental override can cause real problems. With the new [fn::final](/docs/esc/environments/syntax/builtin-functions/fn-final/) built-in function, you can mark values as final, preventing child environments from overriding them. If a child environment tries to override a final value, ESC raises a warning and preserves the original value.

<!--more-->

## How it works

Let's say you have a parent environment that sets the AWS region for all deployments. You can use `fn::final` to ensure no child environment can change it:

```yaml
# project/parent-env
values:
  aws-region:
    fn::final: us-east-1
```

If a child environment tries to override the final value, ESC raises a `cannot override final value` warning.

```yaml
# project/child-env
imports:
  - project/parent-env
values:
  aws-region: eu-west-1 # raises a warning
```

This evaluates to:

```json
{
  "aws-region": "us-east-1"
}
```

In this scenario, the ESC environment is still valid, but the final value remains unchanged.

## When to use fn::final

Use `fn::final` for:

- Security-sensitive values that shouldn't be changed
- Compliance or policy settings enforced by a platform team
- Shared base environments where certain values must remain consistent

## Getting started

The `fn::final` function is available now in all Pulumi ESC environments. For more information, check out the [fn::final documentation](/docs/esc/environments/syntax/builtin-functions/fn-final/)!
