---
title: "IDP Pattern: One ESC environment per service"
linktitle: "One ESC environment per service"
menu:
  idp:
    parent: idp-patterns
    weight: 10
aliases:
  - /docs/idp/best-practices/patterns/one-esc-environment-per-service/
meta_desc: Use one Pulumi ESC environment per service to maintain clear boundaries and improve security isolation in your Pulumi IDP implementation
h1: "IDP Pattern: One ESC environment per service"
description: <p>Use one Pulumi ESC environment per service to maintain clear boundaries and improve security isolation in your Pulumi IDP implementation.</p>
---

## Description

This pattern involves creating a dedicated Pulumi ESC (Environments, Secrets, and Configuration) environment for each service in your infrastructure. Each service gets its own isolated environment containing service-specific configuration, secrets, and variables.

## When to use this pattern

- **Service isolation**: When you need strong boundaries between different services
- **Security requirements**: When services have different security or compliance requirements
- **Independent deployment**: When services are developed and deployed by different teams
- **Granular access control**: When you need fine-grained permissions per service
- **Service-specific configuration**: When each service has unique configuration needs

## When NOT to use this pattern

- **Shared configuration**: When services share significant amounts of configuration
- **Small, tightly coupled services**: When services are part of a cohesive application unit
- **Development environments**: When you need simplified setup for local development
- **Limited team capacity**: When managing many environments exceeds team capacity
- **Frequent cross-service updates**: When configuration changes often affect multiple services

## How to use this pattern

This pattern works well with Pulumi ESC's ability to compose multiple environments. You can create separate environments for each service while still allowing your Pulumi programs to consume configuration from multiple services when needed.

### Example

Consider a web application that needs a database, cache, and authentication service:

```yaml
# environments/database-service.yaml
values:
  database:
    host: "db.example.com"
    port: 5432
    name: "myapp"
  secrets:
    connectionString: "postgresql://user:pass@db.example.com:5432/myapp"
```

```yaml
# environments/cache-service.yaml
values:
  cache:
    host: "redis.example.com"
    port: 6379
    ttl: 3600
```

```yaml
# environments/auth-service.yaml
values:
  auth:
    provider: "oauth2"
    clientId: "app-client-id"
  secrets:
    clientSecret: "oauth-client-secret"
```

Your Pulumi program can then compose these environments:

```yaml
# pulumi.yaml
name: web-app
runtime: nodejs

environment:
  - database-service
  - cache-service  
  - auth-service
```

This allows each service team to manage their own configuration independently while enabling your application to consume from multiple services as needed.

## Related patterns

- [IDP Pattern: One ESC environment per team](/docs/idp/guides/best-practices/patterns/one-esc-environment-per-team) - Alternative organizational approach
- [IDP Pattern: One ESC environment per lifecycle stage](/docs/idp/guides/best-practices/patterns/one-esc-environment-per-lifecycle-stage) - Complementary staging approach
- [IDP Pattern: Composable environments](/docs/idp/guides/best-practices/patterns/composable-environments) - For sharing common configuration across services
