---
title_tag: Configure OpenID Connect for GitHub | OIDC
meta_desc: This page describes how to configure Pulumi Cloud to accept GitHub OIDC tokens for organization, team, and personal access.
title: GitHub
h1: Configuring OpenID Connect for GitHub
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

This document outlines the steps required to configure Pulumi Cloud to accept GitHub id_tokens and exchange them for Pulumi access tokens. Three token types are supported — [organization](#organization-tokens), [team](#team-tokens), and [personal](#personal-tokens) — subject to your [Pulumi edition](/docs/administration/access-identity/oidc-issuers/#token-types-by-edition).

{{< notes type="info" >}}
This guide walks through the Pulumi Cloud UI. You can also configure OIDC Issuers via the [REST API](/docs/reference/cloud-rest-api/oidc-issuers/) or the [`OidcIssuer`](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/oidcissuer/) resource in the Pulumi Service provider.
{{< /notes >}}

## Prerequisites

- You must be an admin of your Pulumi organization.

{{< notes type="warning" >}}
This guide provides step-by-step instructions based on the official provider documentation, which is subject to change. For the most current information, refer to the [official GitHub documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).
{{< /notes >}}

## Register the OIDC Issuer

The registration steps are the same for all token types.

1. Navigate to **Settings → Access Management → OIDC Issuers** and select **Register issuer**.
1. Name the issuer and set the issuer URL to `https://token.actions.githubusercontent.com`.
1. Submit the form.

## Organization tokens

Organization tokens grant access on behalf of the entire Pulumi organization. They are appropriate for CI/CD pipelines that need broad access across stacks in the organization.

### Authorization policy

1. Select the issuer name.
1. Set **Decision** to **Allow**.
1. Set **Token type** to **Organization**.
1. Add a policy and configure the audience and subject claims for your organization and repositories:

   <!-- markdownlint-disable no-bare-urls -->
   - **Aud**: `urn:pulumi:org:<org-name>`
   - **Sub**: `repo:<organization>/<repo>:*`
   <!-- markdownlint-enable no-bare-urls -->

   For more information about GitHub token claims, see the [official GitHub documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#understanding-the-oidc-token).
1. Select **Save policies**.

### GitHub Actions step

```yaml
      - uses: pulumi/auth-actions@v2
        with:
          organization: org-name
          requested-token-type: urn:pulumi:token-type:access_token:organization
```

Replace `org-name` with your Pulumi organization name. For more information, see the [Pulumi Auth Action documentation](https://github.com/marketplace/actions/pulumi-auth-action).

### Sample workflow

```yaml
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

      - uses: pulumi/auth-actions@v2
        with:
          organization: org-name
          requested-token-type: urn:pulumi:token-type:access_token:organization

      - uses: pulumi/actions@v6
        with:
          command: preview
          stack-name: org-name/stack-name
```

## Team tokens

Team tokens are scoped to a specific team within your Pulumi organization. They are useful when you want to limit CI/CD access to only the stacks a particular team is authorized to manage. Team tokens require the Enterprise or Business Critical edition.

### Authorization policy

1. Select the issuer name.
1. Set **Decision** to **Allow**.
1. Set **Token type** to **Team** and set **Scope** to `team:<team-slug>`, where `<team-slug>` is the slug of the team within your Pulumi organization.
1. Add a policy and configure the audience and subject claims:

   <!-- markdownlint-disable no-bare-urls -->
   - **Aud**: `urn:pulumi:org:<org-name>`
   - **Sub**: `repo:<organization>/<repo>:*`
   <!-- markdownlint-enable no-bare-urls -->

1. Select **Save policies**.

### GitHub Actions step

```yaml
      - uses: pulumi/auth-actions@v2
        with:
          organization: org-name
          requested-token-type: urn:pulumi:token-type:access_token:team
          scope: team:<team-slug>
```

Replace `org-name` with your Pulumi organization name and `<team-slug>` with the team's slug.

### Sample workflow

```yaml
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

      - uses: pulumi/auth-actions@v2
        with:
          organization: org-name
          requested-token-type: urn:pulumi:token-type:access_token:team
          scope: team:<team-slug>

      - uses: pulumi/actions@v6
        with:
          command: preview
          stack-name: org-name/stack-name
```

## Personal tokens

Personal tokens are issued on behalf of a specific Pulumi user and carry that user's permissions. For most automated workflows, organization or team tokens are preferred because they run with organizational identity and do not depend on an individual account. Personal tokens are available on all Pulumi editions and are appropriate when you want a workflow to operate with exactly the access that a particular user has been granted.

### Authorization policy

1. Select the issuer name.
1. Set **Decision** to **Allow**.
1. Set **Token type** to **Personal** and set **Scope** to `user:<pulumi-username>`, where `<pulumi-username>` is the Pulumi username of the user the token should represent.
1. Add a policy and configure the audience and subject claims:

   <!-- markdownlint-disable no-bare-urls -->
   - **Aud**: `urn:pulumi:org:<org-name>`
   - **Sub**: `repo:<organization>/<repo>:*`
   <!-- markdownlint-enable no-bare-urls -->

1. Select **Save policies**.

### GitHub Actions step

```yaml
      - uses: pulumi/auth-actions@v2
        with:
          organization: org-name
          requested-token-type: urn:pulumi:token-type:access_token:personal
          scope: user:<pulumi-username>
```

Replace `org-name` with your Pulumi organization name and `<pulumi-username>` with the Pulumi username.

### Sample workflow

```yaml
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

      - uses: pulumi/auth-actions@v2
        with:
          organization: org-name
          requested-token-type: urn:pulumi:token-type:access_token:personal
          scope: user:<pulumi-username>

      - uses: pulumi/actions@v6
        with:
          command: preview
          stack-name: org-name/stack-name
```
