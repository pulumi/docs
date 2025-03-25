---
title: "Announcing the Pulumi ESC GitHub Action"
date: "2025-03-05"
meta_desc: "Securely inject secrets into GitHub Actions with Pulumi ESC. Automate
  secret rotation, environment variables, and CI/CD pipelines—no long-lived credentials."
authors:
  - "komal-ali"
tags:
  - esc
  - secrets
  - github
  - features
search:
  keywords:
    - esc
    - github
    - action
    - announcing
    - inject
    - rotation
    - lived
---

We’re excited to share our latest addition to the Pulumi Ecosystem: the [Pulumi ESC GitHub Action](https://github.com/marketplace/actions/esc-action). This Action lets you inject secrets and configuration securely into your GitHub Actions workflows as they are needed, rather than storing them as static, long-lived secrets.

<!--more-->

## Why we built it

[Secret management](/what-is/what-is-secrets-management/) continues to be a challenge for organizations of all sizes. Storing long-lived credentials in multiple places (e.g., GitHub, third-party CI systems, and internal servers) often leads to “secret sprawl” and potential security gaps. With Pulumi ESC, you can migrate to dynamic credentials, and ensure secrets don’t persist beyond their necessary lifetime. If your process requires longer-lived static credentials, with ESC you can manage credentials in a central place and [rotate them automatically](/docs/esc/environments/rotation).

By packaging ESC functionality into a GitHub Action, we’re enabling teams to inject secrets and run ESC commands directly within their GitHub workflows. This allows for a streamlined approach to environment management and secrets rotation—without leaving GitHub.

## Key benefits

1.	**Secure Secrets Injection** - Inject secrets into your GitHub Actions workflows as they are needed, rather than storing them as static, long-lived secrets. This dynamic approach reduces the risk of secrets leaking in logs or pulled from unauthorized sources.
2.	**Automatic Secret Rotation** - Pulumi ESC handles rotation for you behind the scenes, ensuring that any secrets or credentials you inject into GitHub Actions are valid at the time of use, but rotated on a regular schedule to avoid the risks that come with long-lived static secrets.
3.	**Streamlined CI/CD Pipeline** - In addition to injecting environment variables, you can run any Pulumi ESC command directly in your GitHub Actions workflows. Automate the creation, update, or teardown of ESC Environments as part of your CI/CD process.
4.	**Seamless Integration with Pulumi Cloud** - Combine the Pulumi ESC GitHub Action with [pulumi/auth-actions](https://github.com/marketplace/actions/pulumi-auth-action) to authenticate securely with Pulumi Cloud. No need for long-lived tokens — simply leverage short-lived tokens provided at runtime.

## How it works

At a high level, the Pulumi ESC GitHub Action can do three things:

1. **Download the Pulumi ESC CLI** - By default, the action ensures the ESC CLI is installed in your GitHub Actions environment. If you provide a specific version, that version is installed.
2. **Inject all environment variables from an ESC environment** - If you specify an environment (for example, `tinyco/someProject/myEnv`), the action will inject all environment variables and projected files associated with that environment into the GitHub Actions context.
3. **Inject specific environment variables from an ESC environment** - If you only need certain keys, you can specify them in the action’s inputs to pick and choose what gets injected, giving you fine-grained control.

## Example workflow

Below is a minimal workflow that showcases injecting an entire environment’s variables into your GitHub Actions job:

```yaml
on:
  - pull_request

permissions:
  id-token: write
  contents: read

jobs:
  test-env-injection:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Authenticate with Pulumi Cloud
        uses: pulumi/auth-actions@v1
        with:
          organization: pulumi
          requested-token-type: urn:pulumi:token-type:access_token:organization
      - name: Install and inject ESC environment variables
        uses: pulumi/esc-action@v1
        with:
          environment: 'tinyco/someProject/myEnv@stable'
      - name: Verify environment variables
        run: |
          echo "FOO=$FOO"
          echo "SOME_IMPORTANT_KEY=$SOME_IMPORTANT_KEY"
          echo "TEST_ENV=$TEST_ENV"
```

The GitHub Action workflow above does the following:

1.	Authenticate with Pulumi Cloud using pulumi/auth-actions. Instead of storing a permanent token, we use a [short-lived token to authenticate with Pulumi Cloud](https://www.pulumi.com/docs/pulumi-cloud/access-management/oidc/client/github/).
2.	Inject the environment variables from `tinyco/someProject/myEnv` into the current GitHub Actions environment, making them accessible to subsequent steps in the workflow.

## What’s Next?

- Explore More ESC Features: Dive deeper into ESC’s [environment management](/docs/esc/environments/working-with-environments), [secret rotation](/docs/esc/environments/rotation), and [dynamic credentials](/docs/esc/integrations/dynamic-login-credentials).
- Contribute to the GitHub Action: The Pulumi ESC GitHub Action is [open source](https://github.com/pulumi/esc-action). Feel free to open issues, submit PRs, or suggest enhancements.
- Join the Pulumi Community: Connect with other Pulumi users and share best practices in our Community Slack.

We’re thrilled to bring you the Pulumi ESC GitHub Action, allowing you to automate your infrastructure and streamline secrets management from within GitHub. This integration makes it simpler than ever to adopt best-in-class secrets management and environment configuration practices, all while speeding up your CI/CD pipelines.

Have questions or feedback? Feel free to reach out to us in our [Community Slack](https://pulumi-community.slack.com/join/shared_invite/zt-2amio1u4h-5Y35enT27Y0dk4N8ZYHbMg#/shared-invite/email) or submit an [issue on GitHub](https://github.com/pulumi/esc-action/issues?q=sort%3Aupdated-desc+is%3Aissue+is%3Aopen). We can’t wait to see what you build!
