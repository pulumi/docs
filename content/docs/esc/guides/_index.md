---
title: Guides
title_tag: Pulumi ESC guides
h1: Guides
meta_desc: Step-by-step guides for using Pulumi ESC with Docker, direnv, GitHub Actions, Kubernetes, Cloudflare, and Pulumi IaC.
menu:
  esc:
    identifier: esc-guides
    parent: esc-home
    weight: 6
---

How-to guides for consuming Pulumi ESC from the tools you already use. Each page is a self-contained walkthrough — install steps, the YAML or commands you need, and where ESC fits in the flow.

For first-party ESC integrations (the Pulumi Service Provider, Automation API, the VS Code extension, the External Secrets Operator, and the Secrets Store CSI Driver), see [Integrations](/docs/esc/integrations/).

## Authentication

- [Configuring OIDC](/docs/esc/guides/configuring-oidc/) — set up OpenID Connect trust between ESC and AWS, Azure, GCP, Doppler, Infisical, or Vault.

## Use ESC with Pulumi IaC

- [Manage ESC with Pulumi IaC](/docs/esc/guides/integrate-with-pulumi-iac/) — consume environments from a Pulumi program.
- [Sync secrets to external platforms](/docs/esc/guides/sync-secrets-to-external-platforms/) — push ESC secrets and config to AWS Secrets Manager, Azure Key Vault, GitHub, Vault, and more.

## Run commands

- [Run commands with pulumi env run](/docs/esc/guides/running-commands/) — inject environment values into any command or script.

## Integrate with external tools

Use ESC with tools that don't have a dedicated Pulumi-built integration component:

- [GitHub Actions](/docs/esc/guides/integrate-with/github-actions/) — inject ESC values and short-lived cloud credentials into workflows.
- [Docker](/docs/esc/guides/integrate-with/docker/) — load environment variables and secrets into Docker workflows.
- [direnv](/docs/esc/guides/integrate-with/direnv/) — load ESC values automatically when you `cd` into a directory.
- [Terraform](/docs/esc/guides/integrate-with/terraform/) — supply temporary credentials and input variables to the Terraform CLI via `pulumi env run`.
- [Cloudflare](/docs/esc/guides/integrate-with/cloudflare/) — manage Cloudflare Workers secrets via ESC.
- [Kubernetes cluster access](/docs/esc/guides/integrate-with/kubernetes-cluster-access/) — store and consume `kubeconfig` files and cluster credentials in ESC.
