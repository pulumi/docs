---
title: "IDP Pattern: Composable environments"
linktitle: "Composable environments"
menu:
  idp:
    parent: idp-patterns
    weight: 40
meta_desc: Use composable Pulumi ESC environments to share configuration across services, teams, and lifecycle stages
h1: "IDP Pattern: Composable environments"
description: <p>Use composable Pulumi ESC environments to share configuration across services, teams, and lifecycle stages.</p>
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

Consider AWS credentials and region configuration composed for different deployment stages:

```yaml
# aws-creds ESC environment
values:
  creds:
    fn::open::aws-login:
      oidc:
        roleArn: arn:aws:iam::123456789012:role/pulumi-environments-oidc
        sessionName: pulumi-environments-session
        duration: 1h
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.creds.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.creds.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.creds.sessionToken}
```

```yaml
# aws-production ESC environment
imports:
  - aws-creds
values:
  aws:
    region: us-east-1
  pulumiConfig:
    aws:region: ${aws.region}
```

```yaml
# aws-staging ESC environment
imports:
  - aws-creds
values:
  aws:
    region: us-west-2
  pulumiConfig:
    aws:region: ${aws.region}
```

This allows developers to use either `aws-production` or `aws-staging` environments and automatically inherit the proper authentication while getting stage-specific regional configuration.

## Related patterns

- [IDP Pattern: One ESC environment per service](/docs/idp/well-architected/patterns/one-esc-environment-per-service) - Benefits from shared base configuration
- [IDP Pattern: One ESC environment per team](/docs/idp/well-architected/patterns/one-esc-environment-per-team) - Can import from organizational environments
- [IDP Pattern: One ESC environment per lifecycle stage](/docs/idp/well-architected/patterns/one-esc-environment-per-lifecycle-stage) - Can share base configuration across stages
