---
title_tag: "Google Cloud | Pulumi Integrations"
meta_desc: Google Cloud integration with Pulumi — providers, packages, architecture templates, ESC integrations, Insights account scanning, and pre-built policy packs.
title: Google Cloud
linktitle: Google Cloud
h1: Google Cloud
meta_image: /images/docs/meta-images/docs-clouds-google-cloud-meta-image.png
menu:
  integrations:
    name: Google Cloud
    identifier: google-clouds
    parent: integrations-clouds
    weight: 3
aliases:
- /docs/iac/clouds/gcp/
- /docs/iac/clouds/gcp/guides/
- /docs/iac/clouds/gcp/guides/providers/
- /docs/clouds/gcp/
- /docs/clouds/gcp/guides/
- /docs/clouds/gcp/guides/providers/
---

Build, deploy, and manage Google Cloud infrastructure with Pulumi. This page links to every Pulumi capability for Google Cloud: Infrastructure as Code, Environments, Secrets, and Configuration (ESC), Insights account scanning, and policy packs.

To start from scratch, follow the [Google Cloud get-started guide](/docs/iac/get-started/gcp/).

## Infrastructure as Code

[Pulumi IaC](/docs/iac/) lets you define cloud infrastructure using TypeScript, Python, Go, C#, Java, or YAML — with deterministic deployments, a state backend, and a rich ecosystem of packages.

- [Google Cloud provider](/registry/packages/gcp/) — the default Google Cloud provider. Manages a broad set of Google Cloud resources.
- [Docker](/registry/packages/docker/) — build and push Docker images to Artifact Registry, Container Registry, or other registries.
- [Kubernetes](/registry/packages/kubernetes/) — deploy application workloads to GKE or any Kubernetes cluster.

## Architecture templates

[Pulumi templates](/templates/) are ready-to-deploy starting points for common architectures. Run `pulumi new <template>` to bootstrap a new project.

Start new Google Cloud projects from a pre-built template:

- [Container service on Google Cloud](/templates/container-service/gcp/) — containerized service on Cloud Run.
- [Serverless application on Google Cloud](/templates/serverless-application/gcp/) — Cloud Functions with supporting resources.
- [Static website on Google Cloud](/templates/static-website/gcp/) — Cloud Storage static site.
- [Virtual machine on Google Cloud](/templates/virtual-machine/gcp/) — Compute Engine VM with configurable networking.
- [Kubernetes cluster on Google Cloud](/templates/kubernetes/gcp/) — Google Kubernetes Engine (GKE) cluster ready for workloads.

## Guides

Hands-on Infrastructure as Code guides for building on Google Cloud with Pulumi.

- [Google Cloud Build CI/CD](/docs/iac/operations/continuous-delivery/google-cloud-build/) — drive Pulumi stack updates from Cloud Build pipelines.

## Secrets & configuration (ESC)

[Pulumi ESC (Environments, Secrets, and Configuration)](/docs/esc/) is a centralized service for managing secrets, configuration, and short-lived credentials. It composes values from many sources — including Google Cloud — into environments that Pulumi programs, CLIs, and CI/CD workflows can consume.

ESC integrates directly with Google Cloud for short-lived credentials and secret retrieval:

- [Google Cloud OIDC login](/docs/esc/providers/login/gcp-login/) — generate short-lived Google Cloud credentials for Pulumi programs and workflows.
- [Google Cloud Secret Manager](/docs/esc/providers/secrets/gcp-secrets/) — pull secrets from Secret Manager into ESC environments.

## Insights

[Pulumi Insights](/docs/insights/) continuously scans your clouds to build a searchable inventory of every resource — whether created by Pulumi or not — so you can find, audit, and govern cloud infrastructure across accounts, regions, and providers.

For Google Cloud, Insights connects projects to inventory existing resources, search across projects, and export data. See [Add a Google Cloud account](/docs/insights/discovery/get-started/create-accounts/) for a step-by-step setup guide and [Insights discovery overview](/docs/insights/discovery/accounts/) for background.

## Policy packs

[Pulumi Policies](/docs/insights/policy/) lets you enforce rules on infrastructure at preview and update time, rejecting stacks that violate security, cost, or compliance standards. [Pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) are maintained by Pulumi and cover common regulatory and best-practice frameworks.

For Google Cloud:

- [Pulumi best practices for Google Cloud](/docs/reference/pre-built-policy-packs/pulumi-best-practices/google-cloud/) — Pulumi-authored policies for common Google Cloud misconfigurations.
- [CIS Google Cloud Platform Foundations Benchmark](/docs/reference/pre-built-policy-packs/cis/google-cloud/)
- [HITRUST CSF for Google Cloud](/docs/reference/pre-built-policy-packs/hitrust/google-cloud/)
- [CIS Kubernetes Benchmark on Google Cloud](/docs/reference/pre-built-policy-packs/cis-kubernetes/google-cloud/) — for GKE clusters.

## Migration

Migrate existing Google Cloud infrastructure from another IaC tool to Pulumi.

- [From Terraform](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) — convert Terraform HCL and state to Pulumi.
