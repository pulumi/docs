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

Pulumi ESC support for dynamic configuration providers allow ESC to integrate with secrets stored in any other provider. Organizations often use AWS OIDC, AWS Secrets Manager, Vault, Azure OIDC, Azure KeyVault, GCP OIDC, and GCP Secrets Manager plus many more sources of truth for their secrets and configuration. Pulumi ESC supports them all, providing a single interface to your configuration and secrets, no matter where their source of truth is. Pulumi ESC works with these tools to provide improved management of secrets and configuration.

ESC also integrates with tools like Direnv, Terraform, and Docker to help manage environment variables, interact with existing infrastructure, and support containerized workflows.

## Dynamic login providers

- [AWS Login Provider](/docs/esc/integrations/dynamic-login-providers/aws-login)
- [Azure Login Provider](/docs/esc/integrations/dynamic-login-providers/azure-login)
- [GCP Login Provider](/docs/esc/integrations/dynamic-login-providers/gcp-login)
- [Vault Login Provider](/docs/esc/integrations/dynamic-login-providers/vault-login)

## Secrets providers

- [AWS Secrets Manager](/docs/esc/integrations/secrets-providers/aws-secrets)
- [Azure KeyVault](/docs/esc/integrations/secrets-providers/azure-secrets)
- [GCP Secrets Manager](/docs/esc/integrations/secrets-providers/gcp-secrets)
- [Vault Secrets Management](/docs/esc/integrations/secrets-providers/vault-secrets)

## Developer tool providers

- [Cloudflare](/docs/esc/integrations/dev-tools/cloudflare)
- [Direnv](/docs/esc/integrations/dev-tools/direnv)
- [Terraform](/docs/esc/integrations/dev-tools/terraform)
- [Docker](/docs/esc/integrations/dev-tools/docker)
