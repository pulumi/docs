---
title: "IDP Pattern: One ESC environment per team"
linktitle: "One ESC environment per team"
menu:
  idp:
    parent: idp-patterns
    weight: 20
aliases:
  - /docs/idp/guides/best-practices/patterns/one-esc-environment-per-team/
meta_desc: Use one Pulumi ESC environment per team to align configuration management with organizational structure in your Pulumi IDP implementation
h1: "IDP Pattern: One ESC environment per team"
description: <p>Use one Pulumi ESC environment per team to align configuration management with organizational structure in your Pulumi IDP implementation.</p>
---

## Description

This pattern involves creating a dedicated Pulumi ESC (Environments, Secrets, and Configuration) environment for each team in your organization. Each team manages their own environment containing team-specific configuration, secrets, and variables across all their services.

## When to use this pattern

- **Team autonomy**: When teams need full control over their configuration and secrets
- **Organizational alignment**: When infrastructure boundaries should match team boundaries
- **Shared team resources**: When teams share configuration across multiple services
- **Simplified access control**: When you want team-based permissions rather than service-based
- **Cross-service coordination**: When teams need to coordinate configuration across their services

## When NOT to use this pattern

- **Service isolation requirements**: When different services within a team need strict isolation
- **Compliance boundaries**: When services have different compliance or security requirements
- **Multi-team services**: When services span multiple teams
- **Fine-grained permissions**: When you need service-level access control
- **Large team sizes**: When teams are too large to effectively manage shared configuration

## How to use this pattern

This pattern leverages Pulumi ESC's composition capabilities to allow teams to manage their own configuration while still enabling cross-team collaboration when needed.

### Example

Consider two teams: backend and frontend, each managing multiple services:

```yaml
# environments/backend-team.yaml
values:
  team: "backend"
  services:
    api:
      port: 8080
      replicas: 3
    worker:
      concurrency: 10
      timeout: 30
  shared:
    database:
      host: "backend-db.example.com"
  secrets:
    dbPassword: "backend-db-secret"
```

```yaml
# environments/frontend-team.yaml
values:
  team: "frontend"
  services:
    web:
      port: 3000
      replicas: 2
    cdn:
      provider: "cloudflare"
  shared:
    apiEndpoint: "https://api.example.com"
```

Teams can compose with shared organizational environments:

```yaml
# pulumi.yaml for backend team's API service
name: backend-api
runtime: nodejs

environment:
  - org-shared
  - backend-team
```

This allows teams to maintain autonomy while accessing shared organizational resources.

## Related patterns

- [IDP Pattern: One ESC environment per service](/docs/idp/guides/best-practices/patterns/one-esc-environment-per-service) - Alternative service-focused approach
- [IDP Pattern: One ESC environment per lifecycle stage](/docs/idp/guides/best-practices/patterns/one-esc-environment-per-lifecycle-stage) - Complementary staging approach
- [IDP Pattern: Composable environments](/docs/idp/guides/best-practices/patterns/composable-environments) - For sharing configuration across teams
