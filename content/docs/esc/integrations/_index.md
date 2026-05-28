---
title: Integrations
title_tag: Pulumi ESC integrations
h1: Integrations
meta_desc: First-party Pulumi ESC integrations — Pulumi Service Provider, Automation API, VS Code extension, External Secrets Operator, and Secrets Store CSI Driver.
menu:
  esc:
    identifier: esc-integrations
    parent: esc-home
    weight: 7
aliases:
  - /docs/esc/providers/
  - /docs/pulumi-cloud/esc/providers/
---

Integrations with a dedicated ESC component — a Pulumi-built provider, extension, operator, or driver — that consumes environments. For "use ESC with X" walkthroughs of tools without a dedicated integration component (Docker, direnv, GitHub Actions, Cloudflare, Kubernetes cluster access, Pulumi IaC), see [Guides](/docs/esc/guides/) instead.

For built-in plugins that run *inside* an environment definition with `fn::open::*` or `fn::rotate::*`, see [Providers](/docs/esc/providers/).

## Programmatic access from Pulumi

- [Pulumi Service Provider](/docs/esc/integrations/pulumi-service-provider/) — define environments, permissions, and version tags from a Pulumi program.
- [Automation API](/docs/esc/integrations/automation-api/) — drive ESC operations alongside Pulumi IaC deployments.

## Editor

- [VS Code](/docs/esc/integrations/vs-code/) — browse and edit environments from inside the editor.

## Kubernetes

- [External Secrets Operator (ESO)](/docs/esc/integrations/kubernetes/external-secrets-operator/) — project ESC values into Kubernetes `Secret` objects via ESO.
- [Secrets Store CSI Driver](/docs/esc/integrations/kubernetes/secret-store-csi-driver/) — mount ESC values directly into pods.
