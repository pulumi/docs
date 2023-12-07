---
title_tag: Pulumi ESC Providers
meta_desc: This page provides an overview of the various Pulumi ESC providers.
title: Providers
h1: Pulumi ESC Providers
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: esc
        weight: 5
        identifier: esc-providers
---

Pulumi ESC providers enable you to dynamically import secrets and configuration from the provider into your environment.

To learn how to set up and use each provider, follow the links below. To learn how to configure OpenID Connect (OIDC) for the providers that support it, see [OpenID Connect integration](/docs/pulumi-cloud/oidc/) in the Pulumi Cloud documentation.

| Provider                                                         | Description                                                                                                                   |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [aws-login](/docs/pulumi-cloud/esc/providers/aws-login/)         | The `aws-login` provider enables you to log in to your AWS account using OpenID Connect or static credentials.                |
| [aws-secrets](/docs/pulumi-cloud/esc/providers/aws-secrets/)     | The `aws-secrets` provider enables you to dynamically import Secrets from AWS Secrets Manager into your Environment.          |
| [azure-login](/docs/pulumi-cloud/esc/providers/azure-login/)     | The `azure-login` provider enables you to log in to Azure using OpenID Connect or static credentials.                         |
| [azure-secrets](/docs/pulumi-cloud/esc/providers/azure-secrets/) | The `azure-secrets` provider enables you to dynamically import Secrets from Azure Key Vault into your Environment.            |
| [gcp-login](/docs/pulumi-cloud/esc/providers/gcp-login/)         | The `gcp-login` provider enables you to log in to Google Cloud using OpenID Connect or static credentials.                    |
| [gcp-secrets](/docs/pulumi-cloud/esc/providers/gcp-secrets/)     | The `gcp-secrets` provider enables you to dynamically import Secrets from Google Cloud Secrets Manager into your Environment. |
| [pulumi-stacks](/docs/pulumi-cloud/esc/providers/pulumi-stacks/) | The `pulumi-stacks` provider enables you to import Stack outputs from Pulumi into your Environment.                           |
| [vault-login](/docs/pulumi-cloud/esc/providers/vault-login/)     | The `vault-login` provider enables you to log in to HashiCorp Vault using OpenID Connect or static credentials.               |
| [vault-secrets](/docs/pulumi-cloud/esc/providers/vault-secrets/) | The `vault-secrets` provider enables you to dynamically import Secrets from HashiCorp Vault into your Environment.            |
