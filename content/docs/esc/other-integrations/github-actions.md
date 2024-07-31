---
title_tag: Integrate with GitHub Actions | Pulumi ESC
title: GitHub Actions
h1: "Pulumi ESC: Integrate with GitHub Actions"
meta_desc: This page provides an overview of how to use Pulumi ESC with GitHub Actions.
weight: 2
menu:
  pulumiesc:
    parent: esc-other-integrations
    identifier: esc-other-integrations-github-actions
---

## Overview

Pulumi ESC integrates with [GitHub Actions](https://docs.github.com/en/actions) (GHA) to help developers automatically manage configuration and secrets when running workflows. Additionally, Pulumi ESC works with the [Pulumi CLI Action](https://github.com/marketplace/actions/pulumi-cli-action#pulumi-github-actions) to provide secrets to defined GitHub Actions resources, such as workflow jobs and steps.

{{< notes type="info" >}}
**What is Pulumi ESC?** Pulumi ESC (Environments, Secrets, and Configuration) allows you to define collections of configuration settings and secrets, known as environments, and utilize them in any application or service. [Learn more](https://www.pulumi.com/docs/esc/)
{{< /notes >}}

## Prerequisites

Ensure you have:

- installed [Pulumi ESC](https://www.pulumi.com/docs/install/esc/)
- installed [GitHub CLI](https://cli.github.com/)
- a Pulumi Cloud account. You can sign up for an [always-free, individual account](https://app.pulumi.com/signup)
- a GitHub account. You can sign up for an [account here](https://github.com/join)

{{< notes type="info" >}}
**New to Pulumi ESC?** Complete the [Getting Started tutorial](https://www.pulumi.com/docs/esc/get-started/)
{{< /notes >}}

In addition to the Pulumi ESC and GHA configurations below, consider authenticating to your Pulumi Cloud with GitHub OIDC. [Follow the guide](https://www.pulumi.com/docs/pulumi-cloud/oidc/client/github/) to enable the [Pulumi Auth Action](https://github.com/marketplace/actions/pulumi-auth-action)

### Log in to your GitHub account

A fine-grained GitHub personal access token is required. Follow the [GitHub instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) to create one.

#### Create an ESC Environment

Use the Pulumi ESC CLI to create and configure an Environment. Alternatively, follow the [Pulumi Cloud console instructions](https://www.pulumi.com/docs/esc/get-started/create-environment/#create-via-the-console).

```bash
# login
$ esc login

## create a new ESC Environment
$ ESC_ENV=my-gh-login
$ esc env init ${ESC_ENV}
Environment created.
```

Add your fine-grained GitHub personal access token to the Environment

```bash
# Replace github_pat_123abc with your valid token
$ esc env set ${ESC_ENV} files.GH_PAT github_pat_123abc --secret
```

Note: the GitHub token is declared as a secret. Once the Environment is saved, Pulumi will encrypt its value and replace it with ciphertext.

Now that the Pulumi ESC Environment is created, it can be consumed in a variety of ways, such as running other shell commands without having to set the environment variables locally first.

The `esc run` command opens the Environment you previously created, sets the specified environment variables into a temporary environment, and then uses those environment variables in the context of the `gh` commands.

#### 2. Use ESC with `gh login`

Log into your GitHub account without needing to manage the credentials locally:

```bash
# Ensure you're currently not logged in
$ gh auth logout

# Retrieve the esc environment, and
# authenticate programmatically against github.com
$ esc run -i ${ESC_ENV}  -- sh -c 'gh auth login --with-token < $GH_PAT'

# confirm you're logged in
$ gh auth status
github.com
  ✓ Logged in to github.com account desteves (keyring)
  - Active account: true
  - Git operations protocol: https
  - Token: github_pat_11AAW2NYI0gtUYVcFfShHL_***********************************************************
```

For additional options and details, see `esc run --help`.

Using Pulumi Infrastructure as Code (IaC) with GHA? See the next section to see how to leverage Pulumi ESC alongside.

### Manage AWS credentials for GitHub Action workflows

Pulumi ESC works hand-in-hand with [Pulumi IaC](https://www.pulumi.com/docs/get-started/) to simplify configuration management.

Learn how to:

- Create an ESC Environment
- Add AWS credentials to the ESC Environment
- Add your ESC Environment to a Pulumi program
- Expose the AWS credentials in your workflows and jobs.

You may follow a similar approach to the one shown here for Google Cloud, Azure, and any other configuration or secret.

#### Additional Prerequisites

In addition to the [prerequisites above](#prerequisites), ensure you have:

- installed [Pulumi CLI](https://www.pulumi.com/docs/install/)
- installed a [Pulumi-supported programming language](https://www.pulumi.com/docs/languages-sdks/)

{{< notes type="info" >}}
**New to Pulumi IaC?** Complete the [Getting Started tutorial](https://developers.cloudflare.com/pulumi/tutorial/hello-world/).
{{< /notes >}}

#### Create an ESC Environment and add AWS credentials

Use the Pulumi ESC CLI to create and configure an Environment. Alternatively, follow the [Pulumi Cloud console instructions](https://www.pulumi.com/docs/esc/get-started/create-environment/#create-via-the-console).

```bash
$ esc login

# create a new ESC Environment
$ ESC_ENV=my-pulumi-environment
$ esc env init ${ESC_ENV}
Environment created.

# store AWS credentials
$ esc env set ${ESC_ENV} pulumiConfig.AWS_ACCESS_KEY_ID abc123
$ esc env set ${ESC_ENV} pulumiConfig.AWS_SECRET_ACCESS_KEY abc123 --secret
$ esc env set ${ESC_ENV} pulumiConfig.AWS_REGION us-west-2
```

{{< notes type="info" >}}
**Recommended** Use AWS OIDC credentials instead of static ones. Complete the [Configuring OpenID Connect for AWS guide](https://www.pulumi.com/docs/pulumi-cloud/oidc/provider/aws/#configuring-openid-connect-for-aws)
{{< /notes >}}

#### Add ESC to a Pulumi program

If needed, create a new Pulumi program. The example below defines an AWS S3 Bucket.

  ```bash
  # from the root directory of your GitHub repo, create an empty directory
  $ mkdir my-pulumi-program
  $ cd my-pulumi-program

  # log in if needed
  $ pulumi login

  # for other programming languages, pick one of
  # pulumi new aws-native-[csharp|go|javascript|python|typescript|yaml] --yes
  # example for Golang:
  $ pulumi new aws-native-go --yes
  # download dependencies
  $ go get ./...
  ```

Link your `dev` stack to your Pulumi ESC Environment. Optionally, create a new Stack.

  ```bash
  $ ESC_ENV=my-pulumi-environment
  $ pulumi config env add ${ESC_ENV} --stack dev
  ```

#### Automatically fetch Cloud Credentials

You'll define a simple workflow file that leverages the [Pulumi CLI Action](https://github.com/marketplace/actions/pulumi-cli-action#pulumi-github-actions).

```yml
name: Pulumi
on:
  push:
    branches:
      - main
jobs:
  up:
    name: Update Infra
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pulumi/actions@v5
        with:
          command: up
          # Provide the fully qualified stack name
          # The URL field from `pulumi stack ls` shows this value
          # https://app.pulumi.com/
          # <pulumi org>/<pulumi project>/<stack> 
          stack-name: pulumi-sandbox-diana/my-pulumi-program/dev
        env:
          # Consider authenticating to your Pulumi Cloud with GitHub OIDC instead
          # Follow the guide at
          # https://www.pulumi.com/docs/pulumi-cloud/oidc/client/github/
          # to enable the Pulumi Auth Action
          # See https://github.com/marketplace/actions/pulumi-auth-action
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```
