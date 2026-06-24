---
title: Providers
title_tag: Pulumi ESC providers reference
h1: Providers
meta_desc: Reference catalog of Pulumi ESC login providers and secrets and configuration providers.
menu:
  esc:
    identifier: esc-providers
    parent: esc-home
    weight: 4
aliases:
  - /docs/pulumi-cloud/esc/providers/
---

Reference catalog of the login and secrets/configuration provider plugins shipped with Pulumi ESC. All providers are invoked through `fn::open::<name>`. For an introduction to how providers work — when they run and how they fit into the evaluation flow — see [Providers](/docs/esc/concepts/providers/).

## Login providers

Issue short-lived credentials for downstream services. Prefer OpenID Connect over static keys where supported; see [OIDC setup](/docs/esc/guides/configuring-oidc/) for per-provider trust configuration.

| Provider | Description |
|---|---|
| [aws-login](/docs/esc/providers/login/aws-login/) | Log in to AWS using OIDC or static credentials. |
| [azure-login](/docs/esc/providers/login/azure-login/) | Log in to Azure using OIDC or static credentials. |
| [doppler-login](/docs/esc/providers/login/doppler-login/) | Log in to Doppler using OIDC. |
| [gcp-login](/docs/esc/providers/login/gcp-login/) | Log in to Google Cloud using OIDC or static credentials. |
| [gh-login](/docs/esc/providers/login/gh-login/) | Log in to GitHub using app credentials. |
| [infisical-login](/docs/esc/providers/login/infisical-login/) | Log in to Infisical using OIDC or static credentials. |
| [snowflake-login](/docs/esc/providers/login/snowflake-login/) | Authenticate to Snowflake using OIDC. |
| [vault-login](/docs/esc/providers/login/vault-login/) | Log in to HashiCorp Vault using OIDC or static credentials. |

## Secrets and configuration providers

Dynamically import values from an external system of record into your environment.

| Provider | Description |
|---|---|
| [1password-secrets](/docs/esc/providers/secrets/1password-secrets/) | Import secrets from 1Password. |
| [aws-parameter-store](/docs/esc/providers/secrets/aws-parameter-store/) | Import parameters from AWS Systems Manager Parameter Store. |
| [aws-secrets](/docs/esc/providers/secrets/aws-secrets/) | Import secrets from AWS Secrets Manager. |
| [azure-secrets](/docs/esc/providers/secrets/azure-secrets/) | Import secrets from Azure Key Vault. |
| [doppler-secrets](/docs/esc/providers/secrets/doppler-secrets/) | Import secrets from Doppler. |
| [gcp-secrets](/docs/esc/providers/secrets/gcp-secrets/) | Import secrets from Google Cloud Secret Manager. |
| [infisical-secrets](/docs/esc/providers/secrets/infisical-secrets/) | Import secrets from Infisical. |
| [vault-secrets](/docs/esc/providers/secrets/vault-secrets/) | Import secrets from HashiCorp Vault. |
| [external](/docs/esc/providers/secrets/external/) | Import secrets from a custom service adapter. |

## Infrastructure as code providers

Import the outputs of an existing Pulumi stack or Terraform state file into your environment.

| Provider | Description |
|---|---|
| [pulumi-stacks](/docs/esc/providers/iac/pulumi-stacks/) | Import outputs from a Pulumi stack (includes Terraform state stored in Pulumi Cloud). |
| [terraform-state](/docs/esc/providers/iac/terraform-state/) | Import outputs from a Terraform state file in S3 or Terraform Cloud. |
