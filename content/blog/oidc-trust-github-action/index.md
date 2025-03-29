---
title: "Simplify OIDC Trust with the New Pulumi GitHub Action"

date: 2024-05-20T21:45:13Z

meta_desc: Introducing Pulumi GitHub Action for OIDC Trust Relationships

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
  - german-lena
  - arun-loganathan


# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
  - oidc
  - openid-connect
  - features

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
search:
  keywords:
    - OIDC
    - GitHub
    - OIDC Trust
    - GitHub Action
---

We're excited to announce a new GitHub Action that simplifies the integration of Pulumi's powerful [OpenID Connect](/docs/pulumi-cloud/oidc/client/) (OIDC) Trust feature into your [GitHub Actions](/docs/pulumi-cloud/oidc/client/github/) workflows. This action streamlines secure authentication with Pulumi Cloud, allowing you to leverage GitHub as an identity provider and eliminate the need for long-lived Pulumi access tokens.

<!--more-->

## A Quick Refresher on Pulumi's OIDC Trust

The OIDC Trust feature allows you to configure trusted OIDC identity providers, such as GitHub, GitLab, or Google Cloud, within your Pulumi organization. This feature ensures secure and straightforward integration of [Pulumi Cloud](/docs/pulumi-cloud/) within any OIDC-compliant system. Once set up, you can securely exchange short-lived OIDC tokens from these providers for temporary Pulumi access tokens. These tokens can then be used to authenticate to Pulumi and perform actions such as deploying your infrastructure using Pulumi IaC, retrieving secrets stored in Pulumi ESC, etc. This approach enhances security by eliminating the need to store long-lived sensitive credentials and aligns with best cloud practices.

## Streamlining OIDC Trust with GitHub Actions

Our new GitHub Action makes using OIDC Trust even easier. It automates the secure retrieval of Pulumi access tokens directly within your [GitHub workflows](/docs/iac/packages-and-automation/continuous-delivery/github-actions/), streamlining the authentication process and eliminating manual steps. This automation reduces errors, enhances security by reducing potential token leakage, and improves the maintainability of your workflows, making them cleaner, more readable, and easier to update.

## Example Usage

This example demonstrates how to use the Action to authenticate with OIDC and run the `pulumi preview` command.

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

      - uses: pulumi/auth-actions@v1
        with:
          organization: org-name
          requested-token-type: urn:pulumi:token-type:access_token:organization

      - uses: pulumi/actions@v5
        with:
          command: preview
          stack-name: org-name/stack-name
```

For more information about the `pulumi/auth-actions@v1` Action, check the [Pulumi Auth Action documentation](https://github.com/marketplace/actions/pulumi-auth-action).

## Conclusion

The new GitHub Action for Pulumi OIDC Trust makes it easier than ever to incorporate secure, short-lived credential management into your GitHub Actions workflows. Embrace the power of OIDC, eliminate the "secret zero" problem, and streamline your Pulumi deployments with ease.

Give the action a try in your next GitHub Actions workflow and let us know what you think! Check out our [documentation](/docs/pulumi-cloud/oidc/client/github/) for more details.
