---
title: "Announcing the Pulumi ESC GitHub Action"
date: "2025-03-04"
meta_desc: "Simplify Secrets Management and CI/CD with Pulumi ESC."
authors: 
  - "komal-ali"
tags:
  - esc
  - secrets
  - github
---

We’re excited to share our latest addition to the Pulumi Ecosystem: the [Pulumi ESC GitHub Action](https://github.com/marketplace/actions/esc-action). This new GitHub Action streamlines how you manage secrets, configurations, and CI/CD tasks using Pulumi ESC, helping your team securely scale and automate your software delivery pipelines.

## Why We Built It

Secrets management continues to be a challenge for organizations of all sizes. Storing long-lived credentials in multiple places (e.g., GitHub, third-party CI systems, and internal servers) often leads to “secret sprawl” and potential security gaps. With Pulumi ESC, you can centralize and manage short-lived dynamic credentials, rotate them automatically, and ensure secrets don’t persist beyond their necessary lifetime.

By packaging ESC functionality into a GitHub Action, we’re enabling teams to inject secrets and run ESC commands directly within their GitHub workflows. This allows for a streamlined approach to environment management and secrets rotation—without leaving GitHub.

## Key Benefits

1.	**Secure Secrets Injection** - Inject secrets into your GitHub Actions workflows as they are needed, rather than storing them as static, long-lived secrets. This dynamic approach reduces the risk of secrets leaking in logs or pulled from unauthorized sources.
2.	**Automatic Secret Rotation** - Pulumi ESC handles rotation for you, ensuring that any secrets or credentials you inject into GitHub Actions remain fresh and invalid once your workflow completes.
3.	**Streamlined CI/CD Pipeline** - In addition to secrets management, you can run any Pulumi ESC command directly in your GitHub Actions workflows. Automate the creation, update, or teardown of environments as part of your CI/CD process.
4.	**Seamless Integration with Pulumi Cloud** - Combine the Pulumi ESC GitHub Action with [pulumi/auth-actions](https://github.com/marketplace/actions/pulumi-auth-action) to authenticate securely with Pulumi Cloud. No need for long-lived tokens—simply leverage short-lived tokens provided at runtime.

## How It Works

At a high level, the Pulumi ESC GitHub Action can do three things:

1. **Download the Pulumi ESC CLI** - By default, the action ensures the ESC CLI is installed in your GitHub Actions environment. If you provide a specific version, that version is installed.
2. **Inject all environment variables from an ESC environment** - If you specify an environment (for example, tinyco/someProject/myEnv), the action will inject all environment variables and projected files associated with that environment into the GitHub Actions context.
3. **Inject specific environment variables from an ESC environment** - If you only need certain keys, you can specify them in the action’s inputs to pick and choose what gets injected, giving you fine-grained control.

## Example Workflow

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
          environment: 'tinyco/someProject/myEnv'
      - name: Verify environment variables
        run: |
          echo "FOO=$FOO"
          echo "SOME_IMPORTANT_KEY=$SOME_IMPORTANT_KEY"
          echo "TEST_ENV=$TEST_ENV"
```

## What This Does

1.	Authenticate with Pulumi Cloud using pulumi/auth-actions. Instead of storing a permanent token, we use a short-lived token to authenticate with Pulumi Cloud.
2.	Inject the environment variables from tinyco/someProject/myEnv into the current GitHub Actions environment, making them accessible to subsequent steps in the workflow.

## Use Cases

1.	**Dynamic Credentials in CI/CD** - Inject ephemeral secrets for short-lived tasks, such as integrating with third-party APIs or standing up ephemeral infrastructure. This ensures credentials are invalidated once your pipeline finishes running.
2.	**Automated Environment Management** - Use Pulumi ESC commands to create and manage environments directly from GitHub Actions. This can be part of a larger GitOps strategy where infrastructure changes are tracked in version control.
3.	**Secret Rotation for Compliance** - By using ESC’s built-in rotation, you can achieve compliance requirements and best practices without manual overhead or reliance on multiple external secrets stores.

## Getting Started

1.	**Add the Pulumi ESC Action** - In your existing GitHub Actions workflow, reference pulumi/esc-action@v1.
2.	**Set Up Pulumi ESC** - Ensure you have your environment defined in Pulumi ESC with the required variables and files.
3.	**Authenticate Securely with Pulumi Cloud** - We recommend using pulumi/auth-actions to generate and pass a short-lived token as PULUMI_ACCESS_TOKEN.
4.	**Run and Validate** - Push your changes to GitHub, run your workflow, and verify that your secrets and environment variables are successfully injected.

## What’s Next?

- Explore More ESC Features: Dive deeper into ESC’s environment management, secrets rotation, and dynamic credentials.
- Contribute to the GitHub Action: The Pulumi ESC GitHub Action is open source. Feel free to open issues, submit PRs, or suggest enhancements.
- Join the Pulumi Community: Connect with other Pulumi users and share best practices in our Community Slack.

We’re thrilled to bring you the Pulumi ESC GitHub Action, allowing you to automate your infrastructure and streamline secrets management from within GitHub. This integration makes it simpler than ever to adopt best-in-class secrets management and environment configuration practices, all while speeding up your CI/CD pipelines.

Have questions or feedback? Feel free to reach out to us in our [Community Slack](https://pulumi-community.slack.com/join/shared_invite/zt-2amio1u4h-5Y35enT27Y0dk4N8ZYHbMg#/shared-invite/email) or submit an [issue on GitHub](https://github.com/pulumi/esc-action/issues?q=sort%3Aupdated-desc+is%3Aissue+is%3Aopen). We can’t wait to see what you build!
