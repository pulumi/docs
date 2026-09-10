---
title: "Set Up Cloud OIDC From the Pulumi CLI"
date: 2026-09-10
draft: false
meta_desc: "The new `pulumi env setup` command configures OIDC trust for AWS, Azure, and Google Cloud, and creates ESC Environments with the login provider."
feature_image: feature.png
authors:
    - sean-yeh
tags:
    - esc
    - pulumi-cli
    - security
category: product
schema_type: auto
---

[Pulumi ESC can act as an OpenID Connect (OIDC) provider](/docs/esc/environments/configuring-oidc/) for AWS, Azure, and Google Cloud. Last year, we introduced an onboarding flow in the Pulumi Cloud console that simplified the setup process, making it super easy to set up OIDC with your favorite cloud provider in a guided flow. Today, we're announcing the new `pulumi env setup` command, which brings this capability to the Pulumi CLI.

<!--more-->

## `pulumi env setup` - How it works

Run the command with your desired cloud provider (`aws`, `azure`, `gcp`). For example:

```bash
pulumi env setup aws
```

The command then asks what it needs to configure your cloud, including your credentials, the accounts to configure, and the level of access. The questions differ per cloud.

For AWS, it asks:
1. How to authenticate to AWS. It uses the credentials you already have, or it signs you in with AWS SSO.
1. Which accounts to configure.
1. Which policy to attach to the OIDC role. Choose `AdministratorAccess` for Pulumi Deployments, `ReadOnlyAccess` for Pulumi Insights, or any other policy ARN.

Then, it will print out the plan:

```
About to configure OIDC for organization my-org:
  account 111111111111:
    create role pulumi-esc-oidc-622e86ea-319ba4c675bb3c00-role
    attach arn:aws:iam::aws:policy/AdministratorAccess
    create ESC environment my-org/aws-login/sandbox-account-env

Proceed? [yes/no]
```

After you confirm, the command creates the identity provider, the IAM role, and the policy attachment in each account. It then creates one ESC Environment per account, with the `aws-login` provider already configured.

### Non-interactive setup

You can also run the command without interactive prompts by passing in the necessary flags. Each cloud has its own flags, so be sure to check `pulumi env setup <cloud> --help`. Running non-interactively is great for automated use cases or agents!

Example:

```bash
pulumi env setup aws \
  --account 111111111111 \
  --policy AdministratorAccess \
  --project my-project \
  --yes
```

## Get started

`pulumi env setup` ships with the latest Pulumi CLI. To configure your first cloud:

1. Authenticate to Pulumi Cloud with `pulumi login`.
1. Run `pulumi env setup aws`, `pulumi env setup azure`, or `pulumi env setup gcp`.

See the [OIDC configuration docs](/docs/esc/guides/configuring-oidc/) to learn more about using OIDC with Pulumi, and the [Pulumi ESC docs](/docs/esc/) to explore what you can do with ESC.
