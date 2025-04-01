---
title: "Github actions with Pulumi ESC managed secrets"
title_tag: "Deploy with GitHub Actions and Pulumi ESC"
layout: single
description: Use Pulumi ESC and Github Actions to manage secrets.
meta_desc: Use Pulumi ESC and Github Actions to manage secrets.
meta_image: meta.png
weight: 999
summary: |
    This tutorial demonstrates how you can use GitHub Actions and Pulumi ESC to inject secrets dynamically at runtime, instead of storing long-lived credentials in GitHub. You will use OpenID Connect (OIDC) to fetch a short-lived Pulumi token and AWS credentials for secure infrastructure deployments.
youll_learn:
    - How to authenticate GitHub Actions with Pulumi Cloud using OIDC
    - How to Retrieve AWS credentials from Pulumi ESC dynamically
    - How to Deploy infrastructure on AWS using Pulumi in GitHub Actions
prereqs:
    - A [Pulumi Cloud](https://app.pulumi.com/signup) account
    - The [Pulumi ESC CLI](/docs/install/esc/)
    - Complete the [configure OIDC guide](/docs/pulumi-cloud/access-management/oidc/provider/aws/)
    - A GitHub repository
estimated_time: 15
collections:
    - pulumi-esc
collections_weight: 1
---

## What are we building

You can use GitHub Actions and Pulumi ESC to deploy infrastructure to AWS without storing long-lived secrets. This tutorial shows how to authenticate with Pulumi Cloud using GitHub's OpenID Connect (OIDC) support, fetch a short-lived Pulumi access token, and use that token to open a Pulumi ESC environment that provides dynamic AWS credentials. These credentials are injected into your GitHub Actions workflow and used to run `pulumi up`.

This helps you:

- Avoid storing sensitive AWS credentials or Pulumi access tokens in GitHub
- Use identity-based access control with Pulumi ESC
- Follow security best practices for CI/CD

## Step 1: Create a Pulumi IaC project

Let's start by creating a new Pulumi IaC Project using a template. In this example we'll use the TypeScript AWS template to deploy an S3 bucket, but you can follow along with your favorite language of choice.

```bash
$ mkdir github-and-esc && cd github-and-esc
$ pulumi new aws-typescript
```

Follow the prompts to set up the project name and descriptions, and accept the default values or specify preferred values such as for the AWS region you want to deploy into.

Commit and push the project to your GitHub repository.

### Step 2: Register GitHub OIDC as an issuer in Pulumi Cloud

GitHub Actions uses OpenID Connect (OIDC) to authenticate with Pulumi Cloud. You'll first register GitHub as an OIDC identity provider.

1. In Pulumi Cloud, go to your organization's settings and select **OIDC Issuers**.

{{< figure src="pulumi-oidc-issuers.png" caption="Figure: Pulumi Cloud Org settings">}}

1. Click **Register issuer**, then fill in the following:
   - **Name:** A descriptive name like `GitHubActions`
   - **URL:** `https://token.actions.githubusercontent.com`
1. Click **Create issuer** to save.
1. Under **Rules**, do the following:
   - Set **Decision** to **Allow**
   - For the audience (`aud`), use `urn:pulumi:org:your-org`
   - Set the subject (`sub`) value to `repo:<github-org>/<repo>:*`, replacing with your actual GitHub values (case-sensitive)
1. Click **Save policy** to finish.

{{< figure src="pulumi-add-oidc-issuer.png" caption="Figure: Pulumi Cloud Add issuer">}}

### Step 3: Create a Pulumi ESC environment that returns temporary AWS credentials

You’ll now create an ESC environment in Pulumi Cloud that issues short-lived AWS credentials using the AWS role you configured for OIDC. These credentials will be injected into your GitHub Actions workflow at runtime.

1. In Pulumi Cloud, go to **Environments**, then click **Create Environment**.
2. Set the following values:
   - **Project:** `my-github-action-deployment` (or your preferred name)
   - **Environment name:** `shared-aws-dev`
   - **Description:** `AWS credentials for GitHub OIDC deployments`
3. Click **Create** to finish.

Next, define the environment by editing the YAML configuration. This definition tells Pulumi ESC how to authenticate to AWS using your OIDC role. This environment will be used in your GitHub Actions workflow to inject the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` environment.

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::123456789012:role/aws-esc-role
          sessionName: esc-${context.pulumi.user.login}
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
```

{{< figure src="esc-add-env.png" caption="Figure: Pulumi ESC add environment">}}

{{% notes type="warning" %}}
Replace the roleArn value with the ARN of your AWS IAM role configured for Pulumi Cloud OIDC access. See the [configuring OIDC guide](/docs/pulumi-cloud/access-management/oidc/provider/aws/ for details.
{{% /notes %}}

## Step 4: Add a GitHub Actions workflow to deploy your stack

Now you'll create a GitHub Actions workflow that authenticates with Pulumi Cloud, retrieves AWS credentials from your ESC environment, and runs `pulumi up` to deploy your infrastructure.

1. In your Pulumi project, create a new directory called `.github/workflows`

```bash
mkdir -p .github/workflows
```

## Step 4: Configure a deployment GitHub action

1. In your Pulumi project, create a new directory called `.github/workflows`.
2. Inside that directory, create a new file named `pulumi.yaml`.
3. Add the following workflow configuration:

```yaml
name: Pulumi Deployment

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Authenticate with Pulumi Cloud
        uses: pulumi/auth-actions@v1
        with:
          organization: tutorials
          requested-token-type: urn:pulumi:token-type:access_token:organization

      - name: Install and inject AWS credentials
        uses: pulumi/esc-action@v1
        with:
          environment: '<your-organization>/<your-esc-env>'

      - name: Verify environment variables
        run: |
          echo "AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID"

      - name: Pulumi Preview
        uses: pulumi/actions@v6
        with:
          command: preview
          stack-name: <your-org>/<stack-project>/<stack>

      - name: Pulumi Up
        uses: pulumi/actions@v6
        with:
          command: up
          stack-name: tutorials/pulumi-esc-github-action/dev
          up-args: --yes
```

{{% notes type="info" %}}
Replace <your-org>/<your-esc-env> with the name of your Pulumi ESC environment, and update stack-name values with your organization, project, and stack replacing stack-name: <your-org>/<stack-project>/<stack>.
{{% /notes %}}

### Run the GitHub actions workflow

Commit and push the `pulumi.yaml` file to trigger the GitHub Actions workflow.

```bash
git add .github/workflows/pulumi.yaml
git commit -m "Add Pulumi GitHub Actions workflow" git push
```

Go to your repository’s **Actions** tab to view the running workflow and monitor its progress.

{{< figure src="github-actions.png" caption="Figure: GitHub Actions workflow">}}

## Conclusion

Pulumi ESC can help you securely manage cloud credentials and configuration across your CI/CD pipelines. This tutorial covered how to use GitHub Actions and OIDC to deploy infrastructure using short-lived AWS credentials stored in a Pulumi ESC environment.

Explore other [ESC tutorials](/tutorials/pulumi-esc/) to learn how to version your environments, tag and update configuration sets, and manage secrets across Kubernetes and cloud applications.
