---
title_tag: "Azure Guides | Pulumi IaC"
title: Guides
h1: Azure Guides
meta_desc: Guides for working with Azure services using Pulumi's Azure providers.
meta_image: /images/docs/meta-images/docs-clouds-azure-meta-image.png
menu:
  iac:
    name: Guides
    identifier: azure-clouds-guides
    parent: azure-clouds
    weight: 1

aliases:
- /docs/clouds/azure/guides/
---

This section contains guides for working with Azure using Pulumi. If you are unsure which Azure
package to use for your project, see [Choosing a Pulumi Azure provider](providers/) for a comparison of the
available packages and guidance on when to use each one.

The guides use the following packages:

- [Azure Native provider (`@pulumi/azure-native`)](/registry/packages/azure-native/) — the primary, recommended
  provider for managing Azure infrastructure using the full Azure Resource Manager (ARM) API surface
- [Azure Active Directory / Entra ID provider (`@pulumi/azuread`)](/registry/packages/azuread/) — a provider for
  managing Microsoft Entra ID (formerly Azure Active Directory) resources such as users, groups, service
  principals, and app registrations
- [Azure DevOps provider (`@pulumi/azuredevops`)](/registry/packages/azuredevops/) — a provider for managing
  Azure DevOps projects, repositories, pipelines, and related resources

## Getting started

- [Choosing a provider](providers/)
- [Get started with Azure](/docs/iac/get-started/azure/)
