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

Managing credentials in CI/CD pipelines has always involved tradeoffs. Long-lived access tokens are convenient but
create security risks when they leak or fall into the wrong hands. Short-lived credentials are more secure but require
additional tooling to obtain and manage. Today, we're eliminating this tradeoff with native OIDC token exchange support
in the Pulumi CLI.

<!--more-->

The Pulumi CLI now includes built-in support for exchanging OIDC tokens from your identity provider for short-lived
Pulumi Cloud access tokens. This means you can authenticate to Pulumi Cloud directly from CI/CD environments like GitHub
Actions, GitLab CI, or Kubernetes without storing any long-lived Pulumi credentials as secrets.

## Why OIDC token exchange matters

Most CI/CD workflows authenticate to Pulumi Cloud using personal access tokens or organization tokens stored as secrets.
While this approach works, it comes with significant security concerns:

- **Credential exposure**: If a token is accidentally committed to a repository or logged in CI output, attackers gain
  long-term access to your infrastructure
- **Rotation complexity**: Rotating tokens requires updating secrets across multiple CI/CD systems
- **Over-privileged access**: Tokens often have broader permissions than needed for specific workflows
- **Audit trail gaps**: Difficult to trace which workflow run used which credentials

With OIDC token exchange, you eliminate these risks by leveraging short-lived tokens that your CI/CD platform or
identity provider already issues. No long-lived secrets to manage, rotate, or secure.

## How it works

The `pulumi login` command now accepts OIDC tokens directly:

```bash
pulumi login --oidc-token <token> --oidc-org <org-name>
```

The CLI exchanges your OIDC token for a short-lived Pulumi Cloud access token, which is then used for all subsequent
operations. Tokens expire after 2 hours by default, though you can customize this with the `--oidc-expiration` flag.

You can scope tokens to specific teams or users:

```bash
# Scope to a team
pulumi login --oidc-token <token> --oidc-org my-org --oidc-team platform-team

# Scope to a user
pulumi login --oidc-token <token> --oidc-org my-org --oidc-user alice
```

The `--oidc-token` flag accepts either a raw token string or a file path prefixed with `file://`, making it easy to
integrate with various token delivery mechanisms.

## Example: Kubernetes (EKS)

For workloads running in Kubernetes, you can use service account tokens and exchange them for Pulumi access tokens. The
following example uses a Pulumi program to define a Kubernetes Job resource.

```typescript
import * as kubernetes from "@pulumi/kubernetes";

const script = new kubernetes.core.v1.ConfigMap("script", {
    data: {
        "entrypoint.sh": `#!/bin/bash
EKS_ID_TOKEN=$(cat /var/run/secrets/eks.amazonaws.com/serviceaccount/token)
pulumi login --oidc-token $EKS_ID_TOKEN --oidc-org MY_ORG_NAME
pulumi whoami
`
    }
});

const job = new kubernetes.batch.v1.Job("runner", {
    metadata: {},
    spec: {
        template: {
            spec: {
                serviceAccountName: "pulumi-service-account",
                containers: [{
                    name: "runner",
                    image: "pulumi/pulumi:latest",
                    command: ["/bin/entrypoint.sh"],
                    volumeMounts: [
                        {
                            name: "script",
                            mountPath: "/bin/entrypoint.sh",
                            readOnly: true,
                            subPath: "entrypoint.sh",
                        },
                    ],
                }],
                restartPolicy: "Never",
                volumes: [
                    {
                        name: "script",
                        configMap: {
                            defaultMode: 0o700,
                            name: script.metadata.name,
                        },
                    },
                ],
            },
        },
        backoffLimit: 0,
    },
});

export const jobName = job.metadata.name;
```

This approach works with any Kubernetes cluster that supports service account token projection, including EKS, GKE, and
AKS. The example uses EKS's default token location at `/var/run/secrets/eks.amazonaws.com/serviceaccount/token`, but you
can adapt the token path for other Kubernetes distributions.

## Prerequisites

Before using OIDC token exchange with the Pulumi CLI, you need to:

1. [Register your OIDC provider as a trusted issuer in your Pulumi organization settings](/docs/administration/access-identity/oidc-client/#configuring-trust-relationships)
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

We're excited to see how this feature helps you build more secure infrastructure automation workflows. If you have
questions or feedback, join us in the [Pulumi Community Slack](https://slack.pulumi.com).
