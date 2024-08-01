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

Pulumi ESC integrates with [GitHub Actions](https://docs.github.com/en/actions) (GHA) to help developers automatically manage configuration and secrets when running workflows. Additionally, Pulumi ESC works with the [Pulumi CLI Action](https://github.com/marketplace/actions/pulumi-cli-action#pulumi-github-actions) to provide secrets to workflow jobs and steps, such as AWS Credentials.

{{< notes type="info" >}}
**What is Pulumi ESC?** Pulumi ESC (Environments, Secrets, and Configuration) allows you to define collections of configuration settings and secrets, known as environments, and utilize them in any application or service. [Learn more](https://www.pulumi.com/docs/esc/)
{{< /notes >}}

## Prerequisites

Ensure you have:

- installed [Pulumi ESC](https://www.pulumi.com/docs/install/esc/)
- installed [GitHub CLI](https://cli.github.com/)
- a Pulumi Cloud account. You can sign up for an [always-free, individual account](https://app.pulumi.com/signup).
- a GitHub account. You can sign up for an [account here](https://github.com/join).

{{< notes type="info" >}}
**New to Pulumi ESC?** Complete the [Getting Started tutorial](https://www.pulumi.com/docs/esc/get-started/)
{{< /notes >}}

In addition to the Pulumi ESC and GHA integrations below, consider authenticating to your Pulumi Cloud with GitHub OIDC. [Follow the guide](https://www.pulumi.com/docs/pulumi-cloud/oidc/client/github/) to enable the [Pulumi Auth Action](https://github.com/marketplace/actions/pulumi-auth-action).

## Log in to your GitHub account

Programmatically log in to your GitHub account from your terminal without having to locally store your token. Note, that a fine-grained GitHub personal access token is required. Follow the [GitHub instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) to create one.

### Create an ESC Environment

Use the Pulumi ESC CLI to create and configure an Environment. Alternatively, follow the [Pulumi Cloud console instructions](https://www.pulumi.com/docs/esc/get-started/create-environment/#create-via-the-console).

```bash
# ensure you're logged in
$ esc login
# Logged in to pulumi.com as ...

# create a new ESC Environment
$ ESC_ENV=my-gh-login
$ esc env init ${ESC_ENV}
# Environment created.
```

Add your fine-grained GitHub personal access token to the Environment.

```bash
# Replace github_pat_123abc with your valid token
$ esc env set ${ESC_ENV} files.GH_PAT github_pat_123abc --secret
```

Note: the GitHub token is declared as a `secret`. Once the Environment is saved, Pulumi will encrypt its value and replace it with ciphertext.

Now that the Pulumi ESC Environment is created, it can be consumed in a variety of ways, such as running other shell commands without having to set the environment variables locally first.

### Use ESC with `gh login`

The `esc run` command opens the Environment you previously created, sets the specified environment variables into a temporary environment, and then uses those environment variables in the context of the `gh` commands.

Log into your GitHub account without needing to manage the credentials locally.

```bash
# ensure you're currently not logged in
$ gh auth logout

# retrieve the esc environment, and
# authenticate programmatically against github.com
$ ESC_ENV=my-gh-login
$ esc run -i ${ESC_ENV}  -- sh -c 'gh auth login --with-token < $GH_PAT'

# confirm you're now logged in
$ gh auth status
# github.com
#   ✓ Logged in to github.com account desteves (keyring)
#   - Active account: true
#   - Git operations protocol: https
#   - Token: github_pat_11AAW2NYI0gtUYVcFfShHL_***
```

For additional options and details, see `esc run --help`.

Using Pulumi Infrastructure as Code (IaC) with GHA? See the next section to see how to leverage Pulumi ESC alongside.

## Manage credentials for the [Pulumi CLI Action](https://github.com/marketplace/actions/pulumi-cli-action#pulumi-github-actions)

Pulumi ESC works hand-in-hand with Pulumi Infrastructure as Code (IaC) to simplify configuration and secrets management. This integration enables you to set up workflows that automatically provision cloud resources defined in your IaC, while securely accessing all necessary credentials for deployment.

{{< notes type="info" >}}
**New to Pulumi IaC?** Complete the [Getting Started tutorial](https://developers.cloudflare.com/pulumi/tutorial/hello-world/).
{{< /notes >}}

Learn how to:

- Create an ESC Environment with AWS credentials
- Add your ESC Environment to a Pulumi program
- Use the [Pulumi CLI Action](https://github.com/marketplace/actions/pulumi-cli-action#pulumi-github-actions) to deploy AWS resources

You may follow a similar approach for Google Cloud, Azure, and any other configuration or secrets your IaC requires.

### Create an ESC Environment

Use the Pulumi ESC CLI to create and configure an Environment. Alternatively, follow the [Pulumi Cloud console instructions](https://www.pulumi.com/docs/esc/get-started/create-environment/#create-via-the-console).

```bash
# ensure you're logged in
$ esc login
# Logged in to pulumi.com as ...

# create a new ESC Environment
$ ESC_ENV=my-pulumi-environment
$ esc env init ${ESC_ENV}
# Environment created.
```

### Add AWS Credentials to your ESC Environment

{{< notes type="warning" >}}
**Recommended** Per AWS, it is strongly recommended that you use temporary credentials provided by IAM roles and federated users instead of the long-term credentials provided by IAM users and access keys. Complete the [OpenID Connect for AWS Configuration guide](https://www.pulumi.com/docs/pulumi-cloud/oidc/provider/aws/#configuring-openid-connect-for-aws) to adopt this security best practice.
{{< /notes >}}

The example below stores static AWS credentials in Pulumi ESC. These will be accessed programmatically in a workflow.

```bash
# store your AWS credentials
$ esc env set ${ESC_ENV} pulumiConfig.AWS_ACCESS_KEY_ID abc123
$ esc env set ${ESC_ENV} pulumiConfig.AWS_SECRET_ACCESS_KEY abc123 --secret
$ esc env set ${ESC_ENV} pulumiConfig.AWS_REGION us-west-2
```

### Add ESC to a Pulumi program

Pulumi ESC can be added to any existing Pulumi program. Any configurations defined under `environmentVariables`, `pulumiConfig`, or `files` will be available to your program at runtime. Visit the [Pulumi ESC Syntax Reference](https://www.pulumi.com/docs/esc/reference/) for more options.

In addition to the [prerequisites above](#prerequisites), ensure you have:

- installed [Pulumi CLI](https://www.pulumi.com/docs/install/)
- installed a [Pulumi-supported programming language](https://www.pulumi.com/docs/languages-sdks/)

If needed, create a new Pulumi program. The example below defines an AWS S3 Bucket in Golang.

```bash
# from the root directory of your GitHub repo,
# create an empty directory
$ mkdir my-pulumi-program
$ cd my-pulumi-program

# ensure you're logged in
$ pulumi login
# Logged in to pulumi.com as ...

# example for Golang:
$ pulumi new aws-native-go --yes
# download dependencies
$ go get ./...

# Other programming languages available
# aws-native-[csharp|go|javascript|python|typescript|yaml]
```

Link your `dev` stack to your Pulumi ESC Environment. Optionally, create a new Stack.

```bash
$ ESC_ENV=my-pulumi-environment
$ pulumi config env add ${ESC_ENV} --stack dev --yes
# a summary of the environment will be displayed
```

### Define a workflow that uses the [Pulumi CLI Action](https://github.com/marketplace/actions/pulumi-cli-action#pulumi-github-actions)

Below is a simple example of a workflow that will be triggered upon a push to the `main` branch. It uses `pulumi/actions@v5` to perform a `pulumi up` command against the `dev` stack.

You will need to [create a new Pulumi Access Token](https://app.pulumi.com/account/tokens) for this example.

{{< notes type="info" >}}
**Recommended** Consider authenticating to your Pulumi Cloud with GitHub OIDC instead.  Complete the [Configuring OpenID Connect for GitHub
 guide](https://www.pulumi.com/docs/pulumi-cloud/oidc/client/github/) to enable the [Pulumi Auth Action](https://github.com/marketplace/actions/pulumi-auth-action)
{{< /notes >}}

In your GitHub repo, provide the Pulumi Cloud token as a `PULUMI_ACCESS_TOKEN` secret. This enables your GitHub Action to communicate with the Pulumi Cloud on your behalf.

```bash
$ gh secret set PULUMI_ACCESS_TOKEN
```

Define a new workflow file as `main.yml`.

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
          # https://app.pulumi.com/<pulumi org>/<pulumi project>/<stack>
          stack-name: pulumi-sandbox-diana/my-pulumi-program/dev
          work-dir: ./my-pulumi-program
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

For more examples, see the [GitHub Actions for Pulumi](https://www.pulumi.com/docs/using-pulumi/continuous-delivery/github-actions/) page.
