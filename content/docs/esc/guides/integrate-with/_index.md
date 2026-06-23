---
title: Integrate with external tools
title_tag: Integrate Pulumi ESC with external tools
h1: Integrate ESC with external tools
meta_desc: How-to guides for consuming Pulumi ESC from the external tools you already use — Docker, direnv, GitHub Actions, Terraform, Cloudflare, and Kubernetes.
menu:
  esc:
    name: Integrate with…
    identifier: esc-guides-integrate-with
    parent: esc-guides
    weight: 60
---

Self-contained walkthroughs for consuming Pulumi ESC from tools that don't have a dedicated Pulumi-built integration component. Each page covers install steps, the YAML or commands you need, and where ESC fits in the flow.

For first-party ESC integrations with a dedicated component (the Pulumi Service Provider, Automation API, the VS Code extension, the External Secrets Operator, and the Secrets Store CSI Driver), see [Integrations](/docs/esc/integrations/).

## CI / CD

- [GitHub Actions](/docs/esc/guides/integrate-with/github-actions/) — inject ESC values and short-lived cloud credentials into workflows.

## Development tools

- [Docker](/docs/esc/guides/integrate-with/docker/) — load environment variables and secrets into Docker workflows.
- [direnv](/docs/esc/guides/integrate-with/direnv/) — load ESC values automatically when you `cd` into a directory.

## Infrastructure tools

- [Terraform](/docs/esc/guides/integrate-with/terraform/) — supply temporary credentials and input variables to the Terraform CLI via `pulumi env run`.

## Cloud platforms

- [Cloudflare](/docs/esc/guides/integrate-with/cloudflare/) — manage Cloudflare Workers secrets via ESC.

## Kubernetes

- [Kubernetes cluster access](/docs/esc/guides/integrate-with/kubernetes-cluster-access/) — store and consume `kubeconfig` files and cluster credentials in ESC.
