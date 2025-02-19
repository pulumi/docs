---
title_tag: Integrate with GitHub | Pulumi ESC
title: GitHub
h1: "Pulumi ESC: Integrate with GitHub"
meta_desc: This page provides an overview of how to use Pulumi ESC with GitHub.
weight: 3
menu:
  esc:
    identifier: esc-dev-tools-integrations-github
    parent: esc-dev-tools-integrations
---

## Overview

Pulumi ESC integrates with the GitHub in a variety of ways. In this article we will show how to improve your security footprint within [GitHub Actions](https://docs.github.com/en/actions) when using the [Pulumi CLI Action](https://github.com/marketplace/actions/pulumi-cli-action#pulumi-github-actions) to run Pulumi IaC workflows from GitHub. We'll also describe how you can use ESC to provide login credentials to the [GitHub CLI](https://cli.github.com/).

## Prerequisites

Ensure you have:

- installed [Pulumi ESC](https://www.pulumi.com/docs/install/esc/)
- installed [GitHub CLI](https://cli.github.com/)
- a Pulumi Cloud account. You can sign up for an [always-free, individual account](https://app.pulumi.com/signup).
- a GitHub account. You can sign up for an [account here](https://github.com/join).

{{< notes type="info" >}}
**New to Pulumi ESC?** Complete the [Getting Started tutorial](https://www.pulumi.com/docs/esc/get-started/)
{{< /notes >}}

In addition to the GitHub CLI and GitHub Actions integrations below, consider authenticating to your Pulumi Cloud with GitHub OIDC. [Follow the guide](https://www.pulumi.com/docs/pulumi-cloud/oidc/client/github/) to enable the [Pulumi Auth Action](https://github.com/marketplace/actions/pulumi-auth-action).

## GitHub Actions Integration

Using Pulumi Infrastructure as Code (IaC) within GitHub Actions? This section demonstrates using Pulumi ESC alongside Pulumi IaC deployments to avoid having important cloud credentials in more than one place.

### Manage credentials for the Pulumi CLI Action

The [Pulumi CLI Action](https://github.com/marketplace/actions/pulumi-cli-action#pulumi-github-actions) is a GitHub Action available in the [GitHub Marketplace](https://github.com/marketplace). It allows you to run Pulumi Infrastructure as Code (IaC) deployments directly from GitHub.

We showed how to use this in the Pulumi IaC documentation article "[GitHub Actions for Pulumi](https://www.pulumi.com/docs/iac/packages-and-automation/continuous-delivery/github-actions/)". However, that article only shows how to [configure your cloud credentials as GitHub secrets](https://www.pulumi.com/docs/iac/packages-and-automation/continuous-delivery/github-actions/#configuring-your-secrets), making them available to your Pulumi Program.

A better approach is to manage those secrets with Pulumi ESC by providing them to a Pulumi Program directly, without the need to store them separately in GitHub secrets. This means you have a central place to manage and share those secrets via Pulumi ESC, making updates a much easier and safer process.

Using this approach you can also take advantage of Pulumi ESC's support for AWS OIDC to provide dynamically generated temporary credentials rather than static token values. Read more about that in our [OpenID Connect for AWS Configuration guide](https://www.pulumi.com/docs/pulumi-cloud/oidc/provider/aws/#configuring-openid-connect-for-aws).

{{< notes type="info" >}}
**New to Pulumi IaC?** Complete a [Getting Started tutorial](https://www.pulumi.com/docs/get-started/).
{{< /notes >}}

Learn how to:

- Create an ESC Environment with static AWS credentials
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

### Define a workflow that uses the Pulumi CLI Action

Below is a simple example of a workflow using the [Pulumi CLI Action](https://github.com/marketplace/actions/pulumi-cli-action#pulumi-github-actions). This workflow will be triggered upon a push to the `main` branch. It uses `pulumi/actions@v6` to perform a `pulumi up` command against the `dev` stack.

You will need to [create a new Pulumi Access Token](https://app.pulumi.com/account/tokens) for this example.

{{< notes type="info" >}}
**Recommended** Consider authenticating to your Pulumi Cloud with GitHub OIDC instead.  Complete the [Configuring OpenID Connect for GitHub guide](https://www.pulumi.com/docs/pulumi-cloud/oidc/client/github/) to enable the [Pulumi Auth Action](https://github.com/marketplace/actions/pulumi-auth-action)
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
      - uses: pulumi/actions@v6
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

For more examples, see the [GitHub Actions for Pulumi](https://www.pulumi.com/docs/iac/packages-and-automation/continuous-delivery/github-actions/) page.

## GitHub CLI Integration

Pulumi ESC enables you to log into your GitHub account via the [`gh` CLI](https://cli.github.com/) using credentials stored in an ESC Environment. This allows you to programmatically log in to your GitHub account from your terminal without having to locally store your GitHub Personal Access Token (PAT).

Note, that a fine-grained GitHub personal access token is required. Follow the [GitHub instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) to create one.

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

The GitHub token is declared as a `secret` within ESC. Pulumi will encrypt its value and replace it with ciphertext, ensuring that it is secured both at rest, and in transit.

Now that the Pulumi ESC environment is created, it can be used in a variety of ways, such as running other shell commands without having to set the environment variables locally first.

### Use ESC with `gh login`

The `esc run` command opens the ESC environment you previously created, and launches a new process with any environment variables defined in it, as well as a copy of your shell's environment. By launching `gh` via `esc env run` we can provide it with the .

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
