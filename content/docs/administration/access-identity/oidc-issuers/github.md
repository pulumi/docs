---
title_tag: Configure OpenID Connect for GitHub | OIDC
meta_desc: This page describes how to configure Pulumi Cloud to accept GitHub OIDC tokens.
title: GitHub
h1: Configuring OpenID Connect for GitHub
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: GitHub
    parent: administration-access-identity-oidc-issuers
    weight: 1
    identifier: pulumi-cloud-access-management-oidc-issuers-github
aliases:
- /docs/administration/access-identity/oidc-client/github/
- /docs/pulumi-cloud/oidc/client/github/
- /docs/pulumi-cloud/access-management/oidc-client/github/
---

This document outlines the steps required to configure Pulumi Cloud to accept GitHub id_tokens and exchange them for organization access tokens.

{{< notes type="info" >}}
This guide walks through the Pulumi Cloud UI. You can also configure OIDC Issuers via the [REST API](/docs/reference/cloud-rest-api/oidc-issuers/) or the [`OidcIssuer`](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/oidcissuer/) resource in the Pulumi Service provider.
{{< /notes >}}

{{< notes type="info" >}}
This guide demonstrates using `organization` tokens. Depending on your [Pulumi edition](/docs/administration/access-identity/oidc-issuers/#token-types-by-edition), you can also use `personal` or `team` tokens by adjusting the token type in the authorization policies and the `requested-token-type` parameter.
{{< /notes >}}

## Prerequisites

- You must be an admin of your Pulumi organization.

{{< notes type="warning" >}}
This guide provides step-by-step instructions based on the official provider documentation, which is subject to change. For the most current information, refer to the [official GitHub documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).
{{< /notes >}}

## Register the OIDC Issuer

1. Navigate to **Settings → Access Management → OIDC Issuers** and select **Register issuer**.
1. Name the issuer and set the issuer URL to `https://token.actions.githubusercontent.com`.
1. Submit the form.

## Configure the authorization policies

1. Select the issuer name.
1. Set **Decision** to **Allow**.
1. Set **Token type** to **Organization**.
1. Add a policy to allow OIDC and configure the audience and subject claims for your organization and repositories:

   <!-- markdownlint-disable no-bare-urls -->
   - **Aud**: `urn:pulumi:org:<org-name>`
   - **Sub**: `repo:<organization>/<repo>:*`
   <!-- markdownlint-enable no-bare-urls -->

   For more information about GitHub token claims, see the [official GitHub documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#understanding-the-oidc-token).
1. Select **Save policies**.

## Set up GitHub Actions to use Pulumi's authentication action

```yaml
      - uses: pulumi/auth-actions@v1
        with:
          organization: org-name
          requested-token-type: urn:pulumi:token-type:access_token:organization
```

Replace `org-name` with your Pulumi organization name. For more information, see the [Pulumi Auth Action documentation](https://github.com/marketplace/actions/pulumi-auth-action).

## Sample GitHub Actions workflow

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
