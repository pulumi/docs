---
title: Providers
title_tag: Providers
h1: Providers
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
menu:
  esc:
    parent: esc-reference
    identifier: esc-ref-providers
    weight: 5
---

ESC providers allow users to access credentials, configuration, and secrets stored outside of ESC. These providers are accessed via the [`fn::open` built-in function](/docs/esc/reference/builtin-functions/fn-open).

## Credential providers

| Provider                                                                             | Description                                                                                                   |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [aws-login](/docs/esc/integrations/dynamic-login-credentials/aws-login/)             | The `aws-login` provider enables you to log in to your AWS account using OpenID Connect or static credentials. |
| [azure-login](/docs/esc/integrations/dynamic-login-credentials/azure-login/)         | The `azure-login` provider enables you to log in to Azure using OpenID Connect or static credentials.         |
| [gcp-login](/docs/esc/integrations/dynamic-login-credentials/gcp-login/)             | The `gcp-login` provider enables you to log in to Google Cloud using OpenID Connect or static credentials.    |
| [gh-login](/docs/esc/integrations/dynamic-login-credentials/gh-login/)               | The `gh-login` provider enables you to log in to GitHub using app credentials.                                |
| [snowflake-login](/docs/esc/integrations/dynamic-login-credentials/snowflake-login/) | The `snowflake-login` provider enables authentication to Snowflake using OpenID Connect.                      |
| [vault-login](/docs/esc/integrations/dynamic-login-credentials/vault-login/)         | The `vault-login` provider enables you to log in to HashiCorp Vault using OpenID Connect or static credentials. |

## Configuration and secrets providers

| Provider                                                                           | Description                                                                                                                     |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [1password-secrets](/docs/esc/integrations/dynamic-secrets/1password-secrets/)     | The `1password-secrets` provider enables you to dynamically import Secrets from 1Password into your Environment.                |
| [aws-parameter-store](/docs/pulumi-cloud/esc/providers/aws-parameter-store/)       | The `aws-parameter-store` provider enables you to dynamically import parameters from AWS Parameter Store into your Environment. |
| [aws-secrets](/docs/esc/integrations/dynamic-secrets/aws-secrets/)                 | The `aws-secrets` provider enables you to dynamically import Secrets from AWS Secrets Manager into your Environment.            |
| [azure-secrets](/docs/esc/integrations/dynamic-secrets/azure-secrets/)             | The `azure-secrets` provider enables you to dynamically import Secrets from Azure Key Vault into your Environment.              |
| [gcp-secrets](/docs/esc/integrations/dynamic-secrets/gcp-secrets/)                 | The `gcp-secrets` provider enables you to dynamically import Secrets from Google Cloud Secrets Manager into your Environment.   |
| [pulumi-stacks](/docs/esc/integrations/infrastructure/pulumi-iac/pulumi-stacks)    | The `pulumi-stacks` provider enables you to dynamically import Stack outputs from Pulumi IaC into your Environment.
| [vault-secrets](/docs/esc/integrations/dynamic-secrets/vault-secrets/)             | The `vault-secrets` provider enables you to dynamically import Secrets from HashiCorp Vault into your Environment.              |
