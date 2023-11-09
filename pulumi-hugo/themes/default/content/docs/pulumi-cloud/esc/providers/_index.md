---
title_tag: Pulumi ESC Providers
meta_desc: This page provides an overview of the various Pulumi ESC providers.
title: Providers
h1: Pulumi ESC Providers
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: esc
        identifier: esc-providers
---

Pulumi ESC Providers enable you to dynamically import Secrets and Configuration from the provider into your Environment.

To learn more about how to set up and use the various providers, please refer to their individual pages below. You can also learn how to configure OIDC and trust relationships for each provider by referring to the relevant [Pulumi documentation](/docs/pulumi-cloud/oidc/).

| Provider                                                         | Description                                                                                                                   |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [aws-login](/docs/pulumi-cloud/esc/providers/aws-login/)         | The `aws-login` provider enables you to log in to your AWS account using OpenID Connect or static credentials.                |
| [aws-secrets](/docs/pulumi-cloud/esc/providers/aws-secrets/)     | The `aws-secrets` provider enables you to dynamically import Secrets from AWS Secrets Manager into your Environment.          |
| [azure-login](/docs/pulumi-cloud/esc/providers/azure-login/)     | The `azure-login` provider enables you to log in to Azure using OpenID Connect or static credentials.                         |
| [azure-secrets](/docs/pulumi-cloud/esc/providers/azure-secrets/) | The `azure-secrets` provider enables you to dynamically import Secrets from Azure Key Vault into your Environment.            |
| [gcp-login](/docs/pulumi-cloud/esc/providers/gcp-login/)         | The `gcp-login` provider enables you to log in to Google Cloud using OpenID Connect or static credentials.                    |
| [gcp-secrets](/docs/pulumi-cloud/esc/providers/gcp-secrets/)     | The `gcp-secrets` provider enables you to dynamically import Secrets from Google Cloud Secrets Manager into your Environment. |
| [vault-login](/docs/pulumi-cloud/esc/providers/vault-login/)     | The `vault-login` provider enables you to log in to HashiCorp Vault using OpenID Connect or static credentials.               |
| [vault-secrets](/docs/pulumi-cloud/esc/providers/vault-secrets/) | The `vault-secrets` provider enables you to dynamically import Secrets from HashiCorp Vault into your Environment.            |
