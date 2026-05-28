---
title: Secrets and configuration providers
title_tag: Pulumi ESC secrets and configuration providers
h1: Secrets and configuration providers
meta_desc: Pulumi ESC providers dynamically import secrets, configuration, Pulumi stack outputs, and Terraform state values into your environment.
menu:
  esc:
    name: Secrets & config
    identifier: esc-providers-secrets
    parent: esc-providers
    weight: 2
aliases:
  - /docs/esc/guides/external-secrets/
  - /docs/esc/get-started/retrieve-external-secrets/
  - /docs/pulumi-cloud/esc/get-started/retrieve-external-secrets/
  - /docs/esc/integrations/dynamic-secrets/
  - /docs/esc/providers/secrets/
  - /docs/esc/concepts/providers/secrets/
---

Secrets and configuration providers dynamically import values from an external system of record into your environment. Each provider is invoked through `fn::open::<name>` and the returned values are evaluated lazily — secrets are fetched at open time, not at definition time.

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
| [pulumi-stacks](/docs/esc/providers/secrets/pulumi-stacks/) | Import outputs from a Pulumi stack (including Terraform state stored in Pulumi Cloud). |
| [terraform-state](/docs/esc/providers/secrets/terraform-state/) | Import outputs from a Terraform state file in S3 or Terraform Cloud. |
| [external](/docs/esc/providers/secrets/external/) | Import secrets from a custom service adapter. |
