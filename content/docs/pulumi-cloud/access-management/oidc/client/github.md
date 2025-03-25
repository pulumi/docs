---
title_tag: Configure OpenID Connect for Github | OIDC
meta_desc: This page describes how to configure Pulumi to accept Github OIDC tokens
title: Github
h1: Configuring OpenID Connect for Github
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Github
    parent: pulumi-cloud-access-management-oidc-client
    weight: 1
    identifier: pulumi-cloud-access-management-oidc-client-github
aliases:
  - /docs/pulumi-cloud/oidc/client/github/
search:
  keywords:
    - github
    - oidc
    - accept
    - describes
    - tokens
    - actions
    - configure
---

This document outlines the steps required to configure Pulumi to accept Github id_tokens to be exchanged by Organization access tokens.

## Prerequisites

* You must be an admin of your Pulumi organization.

{{< notes type="warning" >}}
Please note that this guide provides step-by-step instructions based on the official provider documentation which is subject to change. For the most current and precise information, always refer to the [official Github documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).
{{< /notes >}}

## Register the OIDC issuer

1. Navigate to **OIDC Issuers** under your Organization's **Settings** and click on **Register a new issuer**.
1. Name the issuer and complete the url: `https://token.actions.githubusercontent.com`
   ![Register Github](../register-github.png)
1. Submit the form

## Configure the Authorization Policies

1. Click on the issuer name
2. Change the policy decision to `Allow`
3. Change the token type to `Organization`
4. Add a policy to allow OIDC and configure the sub and audience for your organization and repositories:

<!-- markdownlint-disable no-bare-urls -->
* **Aud**: urn:pulumi:org:***org-name***

* **Sub**: repo:***organization***/***repo***:*
<!-- markdownlint-enable no-bare-urls -->
For further information about Github token claims refer to the [official Github documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#understanding-the-oidc-token).
   ![Github policy example](../github-policies.png)
5. Click on update

## Set up the Github Actions to use Pulumi's authentication action

```yaml
      - uses: pulumi/auth-actions@v1
        with:
          organization: org-name
          requested-token-type: urn:pulumi:token-type:access_token:organization
```

Replace `org-name` with the right Pulumi organization. For more information, check the [Pulumi Auth Action documentation](https://github.com/marketplace/actions/pulumi-auth-action).

## Sample Github Actions workflow

```
name: Pulumi preview
on:
  workflow_dispatch:

permissions:
  id-token: write
  contents: read

jobs:
  run_cron_job:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: pulumi/auth-actions@v1
        with:
          organization: org-name
          requested-token-type: urn:pulumi:token-type:access_token:organization

      - uses: pulumi/actions@v6
        with:
          command: preview
          stack-name: org-name/stack-name
```
