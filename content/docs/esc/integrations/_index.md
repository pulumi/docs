---
title: Integrations
title_tag: Pulumi ESC integrations and providers
meta_desc: Explore Pulumi ESC integrations and providers that help you securely manage cloud resources, configurations, and secrets.
h1: Pulumi ESC integrations
menu:
  esc:
    parent: esc-home
    identifier: esc-integrations
    weight: 6
aliases:
    - /docs/esc/providers/
    - /docs/pulumi-cloud/esc/providers/ 
---

Pulumi ESC's support for dynamic configuration providers allows ESC to integrate with secrets stored in any other provider. Organizations often use AWS OIDC, AWS Secrets Manager, Vault, Azure OIDC, Azure KeyVault, GCP OIDC, and GCP Secrets Manager plus many more sources of truth for their secrets and configuration. Pulumi ESC supports them all, providing a single interface to your configuration and secrets, no matter where their source of truth is. Pulumi ESC works with these tools to provide improved management of secrets and configuration.

ESC also integrates with tools like Direnv, Terraform, and Docker to help manage environment variables, interact with existing infrastructure, and support containerized workflows.

## Dynamic login providers

- [AWS login provider](/docs/esc/integrations/dynamic-login-credentials/aws-login)
- [Azure login provider](/docs/esc/integrations/dynamic-login-credentials/azure-login)
- [Doppler login provider](/docs/esc/integrations/dynamic-login-credentials/doppler-login)
- [GCP login provider](/docs/esc/integrations/dynamic-login-credentials/gcp-login)
- [Infisical login provider](/docs/esc/integrations/dynamic-login-credentials/infisical-login)
- [Vault login provider](/docs/esc/integrations/dynamic-login-credentials/vault-login)

## Dynamic secrets providers

- [AWS Secrets Manager](/docs/esc/integrations/dynamic-secrets/aws-secrets)
- [Azure KeyVault](/docs/esc/integrations/dynamic-secrets/azure-secrets)
- [Doppler Secrets](/docs/esc/integrations/dynamic-secrets/doppler-secrets)
- [GCP Secrets Manager](/docs/esc/integrations/dynamic-secrets/gcp-secrets)
- [Infisical Secrets](/docs/esc/integrations/dynamic-secrets/infisical-secrets)
- [Vault Secrets Management](/docs/esc/integrations/dynamic-secrets/vault-secrets)
- [1Password](/docs/esc/integrations/dynamic-secrets/1password-secrets/)

## Secret rotation providers

- [AWS IAM user](/docs/esc/integrations/rotated-secrets/aws-iam)
- [MySQL](/docs/esc/integrations/rotated-secrets/mysql)
- [Postgres](/docs/esc/integrations/rotated-secrets/postgres)
- [AWS Lambda Connector](docs/esc/environments/rotation/#rotation-connectors)

## Kubernetes

- [Kubernetes](/docs/esc/integrations/kubernetes/kubernetes)
- [External Secrets Operator (ESO)](/docs/esc/integrations/kubernetes/external-secrets-operator)

## Developer tools

- [Direnv](/docs/esc/integrations/dev-tools/direnv)
- [Docker](/docs/esc/integrations/dev-tools/docker)
- [GitHub](/docs/esc/integrations/dev-tools/github)

## Infrastructure tools

- [Pulumi IaC](/docs/esc/integrations/infrastructure/pulumi-iac)
- [Terraform](/docs/esc/integrations/infrastructure/terraform)
- [Cloudflare](/docs/esc/integrations/infrastructure/cloudflare)
