---
title_tag: "Azure | Pulumi Integrations"
meta_desc: Azure integration with Pulumi — providers, packages, templates, ARM conversion, ESC integrations, Insights, and policy packs.
title: Azure
linktitle: Azure
h1: Azure
meta_image: /images/docs/meta-images/docs-clouds-azure-meta-image.png
menu:
  integrations:
    name: Azure
    identifier: azure-clouds
    parent: integrations-clouds
    weight: 2
aliases:
- /docs/iac/clouds/azure/
- /docs/clouds/azure/
---

Build, deploy, and manage Azure infrastructure with Pulumi. This page links to every Pulumi capability for Azure: Infrastructure as Code, Environments, Secrets, and Configuration (ESC), Insights account scanning, and policy packs.

To start from scratch, follow the [Azure get-started guide](/docs/iac/get-started/azure/).

## Infrastructure as Code

[Pulumi IaC](/docs/iac/) lets you define cloud infrastructure using TypeScript, Python, Go, C#, Java, or YAML — with deterministic deployments, a state backend, and a rich ecosystem of packages.

Pulumi provides several packages for Azure. For core infrastructure, Azure Native is the recommended choice; Azure Classic is the older alternative. Additional packages cover identity (azuread), Azure DevOps, and static websites. For a deeper comparison, see [Choosing a Pulumi Azure provider](/docs/iac/guides/clouds/azure/).

- [Azure Native provider](/registry/packages/azure-native/) — always up to date; covers 100% of the resources in Azure Resource Manager.
- [Azure Classic provider](/registry/packages/azure/) — older provider with fewer resources and slower feature coverage.
- [Azure Active Directory (Azure AD)](/registry/packages/azuread/) — manage Azure AD identities, groups, and applications.
- [Azure DevOps](/registry/packages/azuredevops/) — provision Azure DevOps projects, pipelines, and repositories.
- [Azure Static Website](/registry/packages/azure-static-website/) — high-level component for static sites on Azure.
- [Docker](/registry/packages/docker/) — build and push Docker images to Azure Container Registry or other registries.
- [Kubernetes](/registry/packages/kubernetes/) — deploy application workloads to AKS or any Kubernetes cluster.

## Architecture templates

[Pulumi templates](/templates/) are ready-to-deploy starting points for common architectures. Run `pulumi new <template>` to bootstrap a new project.

Start new Azure projects from a pre-built template:

- [Container service on Azure](/templates/container-service/azure/) — containerized service on Azure Container Apps or App Service.
- [Serverless application on Azure](/templates/serverless-application/azure/) — Azure Functions with supporting resources.
- [Static website on Azure](/templates/static-website/azure/) — storage-account static site with CDN.
- [Virtual machine on Azure](/templates/virtual-machine/azure/) — Azure VM with configurable networking.
- [Kubernetes cluster on Azure](/templates/kubernetes/azure/) — Azure Kubernetes Service (AKS) cluster ready for workloads.

## Guides

Hands-on Infrastructure as Code guides for building on Azure with Pulumi.

- [Choosing a Pulumi Azure provider](/docs/iac/guides/clouds/azure/) — compare Azure Native and Azure Classic.
- [Convert ARM templates to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-arm/) — migrate existing ARM templates.
- [Azure DevOps CI/CD](/docs/iac/operations/continuous-delivery/azure-devops/) — drive Pulumi stack updates from Azure DevOps pipelines.

## Secrets & configuration (ESC)

[Pulumi ESC (Environments, Secrets, and Configuration)](/docs/esc/) is a centralized service for managing secrets, configuration, and short-lived credentials. It composes values from many sources — including Azure — into environments that Pulumi programs, CLIs, and CI/CD workflows can consume.

ESC integrates directly with Azure for short-lived credentials and secret retrieval:

- [Azure OIDC login](/docs/esc/integrations/dynamic-login-credentials/azure-login/) — generate short-lived Azure credentials for Pulumi programs and workflows.
- [Azure Key Vault](/docs/esc/integrations/dynamic-secrets/azure-secrets/) — pull secrets from Key Vault into ESC environments.
- [Azure application secret rotation](/docs/esc/integrations/rotated-secrets/azure-app-secret/) — rotate Azure AD application secrets on a schedule.

## Insights

[Pulumi Insights](/docs/insights/) continuously scans your clouds to build a searchable inventory of every resource — whether created by Pulumi or not — so you can find, audit, and govern cloud infrastructure across accounts, regions, and providers.

For Azure, Insights connects subscriptions to inventory existing resources, search across subscriptions, and export data. See [Add an Azure account](/docs/insights/discovery/get-started/create-accounts/) for a step-by-step setup guide and [Insights discovery overview](/docs/insights/discovery/accounts/) for background.

## Policy packs

[Pulumi Policies](/docs/insights/policy/) lets you enforce rules on infrastructure at preview and update time, rejecting stacks that violate security, cost, or compliance standards. [Pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/) are maintained by Pulumi and cover common regulatory and best-practice frameworks.

For Azure:

- [Pulumi best practices for Azure](/docs/reference/pre-built-policy-packs/pulumi-best-practices/azure/) — Pulumi-authored policies for common Azure misconfigurations.
- [CIS Microsoft Azure Foundations Benchmark](/docs/reference/pre-built-policy-packs/cis/azure/)
- [HITRUST CSF for Azure](/docs/reference/pre-built-policy-packs/hitrust/azure/)
- [CIS Kubernetes Benchmark on Azure](/docs/reference/pre-built-policy-packs/cis-kubernetes/azure/) — for AKS clusters.

## Migration

Migrate existing Azure infrastructure from another IaC tool to Pulumi. The guides below walk through converting or coexisting with each source format.

- [From ARM and Bicep](/docs/iac/guides/migration/migrating-to-pulumi/from-arm/) — convert ARM templates and Bicep files to Pulumi in your preferred language.
- [From Terraform](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) — convert Terraform HCL and state to Pulumi.
