---
title: Integrations
title_tag: Pulumi ESC integrations and providers
meta_desc: Explore Pulumi ESC integrations and providers that help you securely manage cloud resources, configurations, and secrets.
h1: Pulumi ESC integrations
menu:
    pulumiesc:
        weight: 8
        identifier: esc-integrations
aliases:
    - /docs/esc/providers/
---

Pulumi ESC's support for dynamic configuration providers allows ESC to integrate with secrets stored in any other provider. Organizations often use AWS OIDC, AWS Secrets Manager, Vault, Azure OIDC, Azure KeyVault, GCP OIDC, and GCP Secrets Manager plus many more sources of truth for their secrets and configuration. Pulumi ESC supports them all, providing a single interface to your configuration and secrets, no matter where their source of truth is. Pulumi ESC works with these tools to provide improved management of secrets and configuration.

ESC also integrates with tools like Direnv, Terraform, and Docker to help manage environment variables, interact with existing infrastructure, and support containerized workflows.

## Dynamic login providers

- [AWS login provider](/docs/esc/integrations/dynamic-login-credentials/aws-login)
- [Azure login provider](/docs/esc/integrations/dynamic-login-credentials/azure-login)
- [GCP login provider](/docs/esc/integrations/dynamic-login-credentials/gcp-login)
- [Vault login provider](/docs/esc/integrations/dynamic-login-credentials/vault-login)

## Dynamic secrets providers

- [AWS Secrets Manager](/docs/esc/integrations/dynamic-secrets/aws-secrets)
- [Azure KeyVault](/docs/esc/integrations/dynamic-secrets/azure-secrets)
- [GCP Secrets Manager](/docs/esc/integrations/dynamic-secrets/gcp-secrets)
- [Vault Secrets Management](/docs/esc/integrations/dynamic-secrets/vault-secrets)
- [1Password](/docs/esc/integrations/dynamic-secrets/1password-secrets/)

## Kubernetes

- [Kubernetes](/docs/esc/integrations/kubernetes)

## Developer tools

- [Direnv](/docs/esc/integrations/dev-tools/direnv)
- [Docker](/docs/esc/integrations/dev-tools/docker)

## Infrastructure tools

- [Pulumi IaC](/docs/esc/integrations/infrastructure/pulumi-iac)
- [Terraform](/docs/esc/integrations/infrastructure/terraform)
- [Cloudflare](/docs/esc/integrations/infrastructure/cloudflare)
