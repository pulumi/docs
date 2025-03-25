---
title: Dynamic login credentials
title_tag: Integrate Pulumi ESC with dynamic login credential providers | Pulumi ESC
h1: Dynamic login credentials
meta_desc: Pulumi ESC integrates with dynamic login providers, allowing you to securely log in using OpenID Connect (OIDC) to access resources and secrets.
menu:
  esc:
    name: Dynamic login credentials
    identifier: esc-dynamic-login-credentials
    parent: esc-integrations
    weight: 1
---

Pulumi ESC integrates with the following dynamic login providers to enables you to log in to your account using OpenID Connect (OIDC) or by providing static credentials. The provider will return a set of credentials that can be used to access resources or fetch secrets.

To learn how to set up and use each provider, follow the links below. To learn how to configure OpenID Connect (OIDC) for the providers that support it, see [OpenID Connect integration](/docs/pulumi-cloud/oidc/) in the Pulumi Cloud documentation.

| Provider                                                                 | Description                                                                                                                   |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [aws-login](/docs/esc/integrations/dynamic-login-credentials/aws-login/)                 | The `aws-login` provider enables you to log in to your AWS account using OpenID Connect or static credentials.                |
| [azure-login](/docs/esc/integrations/dynamic-login-credentials/azure-login/)             | The `azure-login` provider enables you to log in to Azure using OpenID Connect or static credentials.                         |
| [gcp-login](/docs/esc/integrations/dynamic-login-credentials/gcp-login/)                 | The `gcp-login` provider enables you to log in to Google Cloud using OpenID Connect or static credentials.                    |
| [gh-login](/docs/esc/integrations/dynamic-login-credentials/gh-login/)                   | The `gh-login` provider enables you to log in to GitHub using app credentials.                                                |
| [vault-login](/docs/esc/integrations/dynamic-login-credentials/vault-login/)             | The `vault-login` provider enables you to log in to HashiCorp Vault using OpenID Connect or static credentials.               |
