---
title: "IDP Pattern: One ESC environment per lifecycle stage"
linktitle: "One ESC environment per lifecycle stage"
menu:
  idp:
    parent: idp-patterns
    weight: 30
aliases:
  - /docs/idp/guides/best-practices/patterns/one-esc-environment-per-lifecycle-stage/
meta_desc: Use one Pulumi ESC environment per lifecycle stage to manage configuration across development, staging, and production environments
h1: "IDP Pattern: One ESC environment per lifecycle stage"
description: <p>Use one Pulumi ESC environment per lifecycle stage to manage configuration across development, staging, and production environments.</p>
---

## Description

This pattern involves creating dedicated Pulumi ESC (Environments, Secrets, and Configuration) environments for each lifecycle stage of your application deployment pipeline, such as development, staging, and production. Each stage has its own environment with stage-specific configuration and secrets.

## When to use this pattern

- **Always-on services**: When running SaaS applications, social media sites, or online stores with one primary instance
- **Reliability focus**: When uptime and reliability are critical business requirements
- **Careful rollouts**: When you need to test configuration changes through stages before production
- **Single-instance applications**: When you have one main production deployment rather than multiple customer instances

## When NOT to use this pattern

- **Multi-tenant applications**: When you deploy separate instances for different customers
- **Rapid iteration**: When you need to deploy frequently without formal staging processes
- **Cost-sensitive projects**: When maintaining multiple environments is too expensive

## How to use this pattern

This pattern works well with Pulumi ESC's composition to share common configuration while allowing stage-specific overrides.

### Example

Consider a SaaS application deployed across three stages:

```yaml
# environments/development.yaml
values:
  stage: "development"
  app:
    replicas: 1
    logLevel: "debug"
    database:
      host: "dev-db.example.com"
      ssl: false
  secrets:
    apiKey: "dev-api-key"
```

```yaml
# environments/staging.yaml
values:
  stage: "staging"
  app:
    replicas: 2
    logLevel: "info"
    database:
      host: "staging-db.example.com"
      ssl: true
  secrets:
    apiKey: "staging-api-key"
```

```yaml
# environments/production.yaml
values:
  stage: "production"
  app:
    replicas: 5
    logLevel: "warn"
    database:
      host: "prod-db.example.com"
      ssl: true
  secrets:
    apiKey: "prod-api-key"
```

Your Pulumi program can compose with shared base configuration:

```yaml
# pulumi.yaml for production deployment
name: web-app
runtime: nodejs

environment:
  - base-config
  - production
```

This allows consistent base configuration while enabling stage-specific customization.

## Related patterns

- [IDP Pattern: One ESC environment per service](/docs/idp/guides/best-practices/patterns/one-esc-environment-per-service) - Can be combined for service-stage matrices
- [IDP Pattern: One ESC environment per team](/docs/idp/guides/best-practices/patterns/one-esc-environment-per-team) - Can be combined for team-stage matrices
- [IDP Pattern: Composable environments](/docs/idp/guides/best-practices/patterns/composable-environments) - For sharing base configuration across stages
