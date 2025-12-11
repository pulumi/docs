---
title: "Native OIDC Token Exchange for Pulumi CLI"
date: 2025-12-11
draft: false
meta_desc: The Pulumi CLI now supports native OIDC token exchange, enabling secure authentication without long-lived credentials in automated workflows.
meta_image: meta.png
authors:
    - boris-schlosser
tags:
    - features
    - security
    - oidc
    - authentication
    - ci-cd
---

Managing credentials in CI/CD pipelines has always involved tradeoffs. Long-lived access tokens are convenient but create security risks when they leak or fall into the wrong hands. Short-lived credentials are more secure but require additional tooling to obtain and manage. Today, we're eliminating this tradeoff with native OIDC token exchange support in the Pulumi CLI.

<!--more-->

The Pulumi CLI now includes built-in support for exchanging OIDC tokens from your identity provider for short-lived Pulumi Cloud access tokens. This means you can authenticate to Pulumi Cloud directly from CI/CD environments like GitHub Actions, GitLab CI, or Kubernetes without storing any long-lived Pulumi credentials as secrets.

## Why OIDC token exchange matters

Most CI/CD workflows authenticate to Pulumi Cloud using personal access tokens or organization tokens stored as secrets. While this approach works, it comes with significant security concerns:

- **Credential exposure**: If a token is accidentally committed to a repository or logged in CI output, attackers gain long-term access to your infrastructure
- **Rotation complexity**: Rotating tokens requires updating secrets across multiple CI/CD systems
- **Over-privileged access**: Tokens often have broader permissions than needed for specific workflows
- **Audit trail gaps**: Difficult to trace which workflow run used which credentials

With OIDC token exchange, you eliminate these risks by leveraging short-lived tokens that your CI/CD platform or identity provider already issues. No long-lived secrets to manage, rotate, or secure.

## How it works

The new `pulumi login` command accepts OIDC tokens directly:

```bash
pulumi login --oidc-token <token> --oidc-org <org-name>
```

The CLI exchanges your OIDC token for a short-lived Pulumi Cloud access token, which is then used for all subsequent operations. Tokens expire after 2 hours by default, though you can customize this with the `--oidc-expiration` flag.

You can scope tokens to specific teams or users:

```bash
# Scope to a team
pulumi login --oidc-token <token> --oidc-org my-org --oidc-team platform-team

# Scope to a user
pulumi login --oidc-token <token> --oidc-org my-org --oidc-user alice
```

The `--oidc-token` flag accepts either a raw token string or a file path prefixed with `file://`, making it easy to integrate with various token delivery mechanisms.

## Example: GitHub Actions

GitHub Actions provides OIDC tokens automatically when you configure the appropriate permissions. Here's a complete workflow that uses native OIDC token exchange:

```yaml
name: Pulumi Up
on:
  push:
    branches:
      - main

permissions:
  id-token: write
  contents: read

jobs:
  pulumi:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/my-github-actions-role
          aws-region: us-east-1

      - name: Login to Pulumi
        run: |
          pulumi login --oidc-token ${{ github.token }} --oidc-org my-org

      - name: Deploy infrastructure
        run: |
          pulumi up --yes
        working-directory: ./infrastructure
```

No `PULUMI_ACCESS_TOKEN` secret required. The GitHub token is exchanged automatically for a Pulumi access token valid for this specific workflow run.

## Example: Google Kubernetes Engine

For workloads running in Kubernetes, you can mount OIDC tokens as projected volumes and exchange them for Pulumi access tokens:

```typescript
import * as kubernetes from "@pulumi/kubernetes";

const job = new kubernetes.batch.v1.Job("pulumi-runner", {
    spec: {
        template: {
            spec: {
                containers: [{
                    name: "runner",
                    image: "pulumi/pulumi:latest",
                    command: ["/bin/bash", "-c"],
                    args: [`
                        OIDC_TOKEN=$(</var/run/secrets/pulumi/token)
                        pulumi login --oidc-token $OIDC_TOKEN --oidc-org my-org
                        pulumi up --yes
                    `],
                    volumeMounts: [{
                        name: "pulumi-oidc-token",
                        mountPath: "/var/run/secrets/pulumi",
                    }],
                }],
                volumes: [{
                    name: "pulumi-oidc-token",
                    projected: {
                        sources: [{
                            serviceAccountToken: {
                                audience: "urn:pulumi:org:my-org",
                                expirationSeconds: 3600,
                                path: "token",
                            },
                        }],
                    },
                }],
                restartPolicy: "Never",
            },
        },
    },
});
```

This approach works with any Kubernetes cluster that supports service account token projection, including GKE, EKS, and AKS.

## Prerequisites

Before using OIDC token exchange with the Pulumi CLI, you need to:

1. Register your OIDC provider as a trusted issuer in your Pulumi organization settings
1. Configure authorization policies that specify which tokens can be exchanged and what permissions they receive
1. Ensure your CI/CD system or identity provider is configured to issue OIDC tokens with the appropriate audience claim

## Get started

Native OIDC token exchange is available now in the latest version of the Pulumi CLI. To get started:

1. Update to the latest Pulumi CLI version
1. Configure your OIDC provider and authorization policies in [Pulumi Cloud](https://app.pulumi.com/)
1. Update your CI/CD workflows to use `pulumi login --oidc-token`

For complete documentation, including setup guides for specific identity providers, see:

- [`pulumi login` command reference](/docs/iac/cli/commands/pulumi_login/#oidc-token-exchange)
- [OIDC client integration guide](/docs/administration/access-identity/oidc-client/)
- [GitHub OIDC setup](/docs/administration/access-identity/oidc-client/github/)
- [GKE OIDC setup](/docs/administration/access-identity/oidc-client/kubernetes-gke/)
- [EKS OIDC setup](/docs/administration/access-identity/oidc-client/kubernetes-eks/)

We're excited to see how this feature helps you build more secure infrastructure automation workflows. If you have questions or feedback, join us in the [Pulumi Community Slack](https://slack.pulumi.com).
