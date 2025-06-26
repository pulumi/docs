---
title: Dynamic secrets
title_tag: Integrate Pulumi ESC with Dynamic Secrets providers | Pulumi ESC
h1: Import and use secrets from providers
meta_desc: Pulumi ESC enables integration with secrets providers like 1Password, AWS, Azure, Google Cloud, and Vault, to securely manage secrets in your environments.
menu:
  esc:
    name: Dynamic secrets
    identifier: esc-dynamic-secrets
    parent: esc-integrations
    weight: 2
---

Pulumi ESC providers enable you to dynamically import secrets and configuration from the provider into your environment.

To learn how to set up and use each provider, follow the links below. To learn how to configure OpenID Connect (OIDC) for the providers that support it, see [OpenID Connect integration](/docs/esc/environments/configuring-oidc) in the Pulumi ESC documentation.

| Provider                                                                           | Description                                                                                                                     |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [1password-secrets](/docs/esc/integrations/dynamic-secrets/1password-secrets/)     | The `1password-secrets` provider enables you to dynamically import Secrets from 1Password into your Environment.                |
| [aws-parameter-store](/docs/pulumi-cloud/esc/providers/aws-parameter-store/)       | The `aws-parameter-store` provider enables you to dynamically import parameters from AWS Parameter Store into your Environment. |
| [aws-secrets](/docs/esc/integrations/dynamic-secrets/aws-secrets/)                 | The `aws-secrets` provider enables you to dynamically import Secrets from AWS Secrets Manager into your Environment.            |
| [azure-secrets](/docs/esc/integrations/dynamic-secrets/azure-secrets/)             | The `azure-secrets` provider enables you to dynamically import Secrets from Azure Key Vault into your Environment.              |
| [doppler-secrets](/docs/esc/integrations/dynamic-secrets/doppler-secrets/)      | The `doppler-secrets` provider enables you to dynamically import Secrets from Doppler into your Environment.
| [gcp-secrets](/docs/esc/integrations/dynamic-secrets/gcp-secrets/)                 | The `gcp-secrets` provider enables you to dynamically import Secrets from Google Cloud Secrets Manager into your Environment.   |
| [infisical-secrets](/docs/esc/integrations/dynamic-secrets/infisical-secrets/)      | The `infisical-secrets` provider enables you to dynamically import Secrets from Infisical Secrets into your Environment.
| [vault-secrets](/docs/esc/integrations/dynamic-secrets/vault-secrets/)             | The `vault-secrets` provider enables you to dynamically import Secrets from HashiCorp Vault into your Environment.              |
