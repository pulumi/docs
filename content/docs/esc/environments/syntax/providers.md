---
title: Providers
title_tag: Providers
h1: Providers
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets and consume them in various ways.
aliases:
  - /docs/reference/esc-syntax/providers/
  - /docs/esc/reference/providers/
menu:
  esc:
    parent: esc-syntax
    identifier: esc-syntax-providers
    weight: 5
---

ESC providers allow users to access credentials, configuration, and secrets stored outside of ESC. These providers are accessed via the [`fn::open` built-in function](/docs/esc/environments/syntax/builtin-functions/fn-open).

## Credential providers

| Provider                                                                             | Description                                                                                                   |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [aws-login](/docs/esc/providers/login/aws-login/)             | The `aws-login` provider enables you to log in to your AWS account using OpenID Connect or static credentials. |
| [azure-login](/docs/esc/providers/login/azure-login/)         | The `azure-login` provider enables you to log in to Azure using OpenID Connect or static credentials.         |
| [gcp-login](/docs/esc/providers/login/gcp-login/)             | The `gcp-login` provider enables you to log in to Google Cloud using OpenID Connect or static credentials.    |
| [gh-login](/docs/esc/providers/login/gh-login/)               | The `gh-login` provider enables you to log in to GitHub using app credentials.                                |
| [snowflake-login](/docs/esc/providers/login/snowflake-login/) | The `snowflake-login` provider enables authentication to Snowflake using OpenID Connect.                      |
| [vault-login](/docs/esc/providers/login/vault-login/)         | The `vault-login` provider enables you to log in to HashiCorp Vault using OpenID Connect or static credentials. |

## Configuration and secrets providers

| Provider                                                                           | Description                                                                                                                     |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [1password-secrets](/docs/esc/providers/secrets/1password-secrets/)     | The `1password-secrets` provider enables you to dynamically import Secrets from 1Password into your Environment.                |
| [aws-parameter-store](/docs/pulumi-cloud/esc/providers/aws-parameter-store/)       | The `aws-parameter-store` provider enables you to dynamically import parameters from AWS Parameter Store into your Environment. |
| [aws-secrets](/docs/esc/providers/secrets/aws-secrets/)                 | The `aws-secrets` provider enables you to dynamically import Secrets from AWS Secrets Manager into your Environment.            |
| [azure-secrets](/docs/esc/providers/secrets/azure-secrets/)             | The `azure-secrets` provider enables you to dynamically import Secrets from Azure Key Vault into your Environment.              |
| [gcp-secrets](/docs/esc/providers/secrets/gcp-secrets/)                 | The `gcp-secrets` provider enables you to dynamically import Secrets from Google Cloud Secrets Manager into your Environment.   |
| [pulumi-stacks](/docs/esc/integrations/pulumi-iac/pulumi-stacks)    | The `pulumi-stacks` provider enables you to dynamically import Stack outputs from Pulumi IaC into your Environment.
| [vault-secrets](/docs/esc/providers/secrets/vault-secrets/)             | The `vault-secrets` provider enables you to dynamically import Secrets from HashiCorp Vault into your Environment.              |
