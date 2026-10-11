---
title: "IDP Pattern: Composable environments"
linktitle: "Composable environments"
menu:
  idp:
    parent: idp-patterns
    weight: 40
aliases:
  - /docs/idp/best-practices/patterns/composable-environments/
meta_desc: Use composable Pulumi ESC environments to share configuration across services, teams, and lifecycle stages
h1: "IDP Pattern: Composable environments"
description: Use composable Pulumi ESC environments to share configuration across services, teams, and lifecycle stages.
---

## Description

This pattern involves creating multiple Pulumi ESC (Environments, Secrets, and Configuration) environments that can be composed together, allowing you to share common configuration while maintaining specific customizations. Environments can import from other environments, creating a hierarchical structure.

## When to use this pattern

- **Shared configuration**: When multiple services or teams need access to common settings
- **DRY principle**: When you want to avoid duplicating configuration across environments
- **Organizational hierarchy**: When you need to reflect organizational structure in configuration
- **Flexible composition**: When different applications need different combinations of shared configuration

## When NOT to use this pattern

- **Simple applications**: When you have minimal configuration that doesn't benefit from composition
- **Strict isolation**: When teams or services require completely separate configuration
- **Complex debugging**: When composition creates too many layers to troubleshoot effectively

## How to use this pattern

Pulumi ESC's composition feature allows you to create a hierarchy of environments where child environments can import and override values from parent environments.

### Example

Consider monitoring configuration composed for different deployment stages:

```yaml
# monitoring-base ESC environment
values:
  monitoring:
    datadog:
      apiKey:
        fn::secret: dd-api-key
      appKey:
        fn::secret: dd-app-key
    alerting:
      slackChannel: "#alerts"
      pagerDutyService: "platform-team"
  environmentVariables:
    DD_API_KEY: ${monitoring.datadog.apiKey}
    DD_APP_KEY: ${monitoring.datadog.appKey}
```

```yaml
# monitoring-production ESC environment
imports:
  - monitoring-base
values:
  monitoring:
    environment: "production"
    alerting:
      errorThreshold: 0.01  # 1% error rate triggers alert
      responseTimeThreshold: 500  # 500ms response time threshold
      slackChannel: "#production-alerts"
  pulumiConfig:
    monitoring:environment: ${monitoring.environment}
    monitoring:errorThreshold: ${monitoring.alerting.errorThreshold}
```

```yaml
# monitoring-staging ESC environment
imports:
  - monitoring-base
values:
  monitoring:
    environment: "staging"
    alerting:
      errorThreshold: 0.05  # 5% error rate triggers alert
      responseTimeThreshold: 1000  # 1s response time threshold
      slackChannel: "#staging-alerts"
  pulumiConfig:
    monitoring:environment: ${monitoring.environment}
    monitoring:errorThreshold: ${monitoring.alerting.errorThreshold}
```

This allows developers to use either `monitoring-production` or `monitoring-staging` environments and automatically inherit the base monitoring configuration while getting stage-specific alert thresholds and notification channels.

## Related patterns

- [IDP Pattern: One ESC environment per service](/docs/idp/guides/best-practices/patterns/one-esc-environment-per-service) - Benefits from shared base configuration
- [IDP Pattern: One ESC environment per team](/docs/idp/guides/best-practices/patterns/one-esc-environment-per-team) - Can import from organizational environments
- [IDP Pattern: One ESC environment per lifecycle stage](/docs/idp/guides/best-practices/patterns/one-esc-environment-per-lifecycle-stage) - Can share base configuration across stages
