---
title: Login providers
title_tag: Pulumi ESC login providers
h1: Login providers
meta_desc: Pulumi ESC login providers issue short-lived credentials for AWS, Azure, GCP, GitHub, and other services using OpenID Connect or static credentials.
menu:
  esc:
    name: Login & OIDC
    identifier: esc-providers-login
    parent: esc-providers
    weight: 1
aliases:
  - /docs/esc/guides/setting-up-oidc/
  - /docs/esc/get-started/use-short-term-credentials/
  - /docs/pulumi-cloud/esc/get-started/use-short-term-credentials/
  - /docs/esc/integrations/dynamic-login-credentials/
  - /docs/esc/providers/login/
  - /docs/esc/concepts/providers/login/
---

Login providers issue short-lived credentials for downstream services. Each provider is invoked through `fn::open::<name>-login` in an environment definition and returns a set of credentials that other providers (and your own code) can consume.

OpenID Connect (OIDC) is the recommended authentication mode wherever supported — see [Configuring OIDC](/docs/esc/integrations/configuring-oidc/) for per-provider setup.

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
