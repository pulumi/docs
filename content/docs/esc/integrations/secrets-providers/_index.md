---
title: Secrets providers
title_tag: Secrets providers | Pulumi ESC
h1: ESC secrets providers
meta_desc: Pulumi ESC enables integration with secrets providers like 1Password, AWS, Azure, Google Cloud, and Vault, to securely manage secrets in your environments.
menu:
  pulumiesc:
    identifier: esc-secrets-providers
    parent: esc-integrations
    weight: 2
---

Pulumi ESC providers enable you to dynamically import secrets and configuration from the provider into your environment.

To learn how to set up and use each provider, follow the links below. To learn how to configure OpenID Connect (OIDC) for the providers that support it, see [OpenID Connect integration](/docs/pulumi-cloud/oidc/) in the Pulumi Cloud documentation.

| Provider                                                                 | Description                                                                                                                   |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [1password-secrets](/docs/pulumi-cloud/esc/providers/1password-secrets/) | The `1password-secrets` provider enables you to dynamically import Secrets from 1Password into your Environment.              |
| [aws-secrets](/docs/pulumi-cloud/esc/providers/aws-secrets/)             | The `aws-secrets` provider enables you to dynamically import Secrets from AWS Secrets Manager into your Environment.          |
| [azure-secrets](/docs/pulumi-cloud/esc/providers/azure-secrets/)         | The `azure-secrets` provider enables you to dynamically import Secrets from Azure Key Vault into your Environment.            |
| [gcp-secrets](/docs/pulumi-cloud/esc/providers/gcp-secrets/)             | The `gcp-secrets` provider enables you to dynamically import Secrets from Google Cloud Secrets Manager into your Environment. |  
| [vault-secrets](/docs/pulumi-cloud/esc/providers/vault-secrets/)         | The `vault-secrets` provider enables you to dynamically import Secrets from HashiCorp Vault into your Environment.            |
