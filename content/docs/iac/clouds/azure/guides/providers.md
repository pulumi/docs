---
title_tag: "Choosing a Pulumi Azure Provider"
title: Choosing a Provider
h1: Choosing a Pulumi Azure Provider
meta_desc: Learn which Pulumi Azure provider to use for your project, including azure-native, azuread, azuredevops, and the community azapi package.
meta_image: /images/docs/meta-images/docs-clouds-azure-meta-image.png
menu:
  iac:
    parent: azure-clouds-guides
    name: Choosing a Provider
    identifier: azure-guides-providers
    weight: 0
aliases:
- /docs/clouds/azure/guides/providers/
---

Pulumi offers several packages for working with Azure. Rather than a single monolithic provider, the Azure
ecosystem is divided along the lines of the underlying Azure APIs: one package for Azure infrastructure
(Resource Manager), one for identity management (Microsoft Graph), one for DevOps platform resources, and
a community-maintained package for low-level ARM access. This guide explains what each package does, how
they compare, and which ones to use for your project.

{{% notes type="info" %}}
For all new Azure infrastructure projects, use the **[Azure Native provider (`@pulumi/azure-native`)](/registry/packages/azure-native/)**.
It is auto-generated from the Azure Resource Manager (ARM) API specifications and covers 100% of ARM
resources, with new resources and API updates available the same day Microsoft publishes them. Use the
other providers alongside it to cover the parts of Azure that ARM does not manage, such as Entra ID
identities and Azure DevOps platform configuration.
{{% /notes %}}

## Packages at a glance

### Providers

| | [Azure Native](/registry/packages/azure-native/) | [Azure Classic](/registry/packages/azure/) | [Azure AD / Entra ID](/registry/packages/azuread/) | [Azure DevOps](/registry/packages/azuredevops/) |
|---|---|---|---|---|
| **Node.js** | `@pulumi/azure-native` | `@pulumi/azure` | `@pulumi/azuread` | `@pulumi/azuredevops` |
| **Python** | `pulumi-azure-native` | `pulumi-azure` | `pulumi-azuread` | `pulumi-azuredevops` |
| **Go** | `github.com/pulumi/pulumi-azure-native-sdk/...` | `github.com/pulumi/pulumi-azure/sdk/v6/go/azure` | `github.com/pulumi/pulumi-azuread/sdk/v6/go/azuread` | `github.com/pulumi/pulumi-azuredevops/sdk/v3/go/azuredevops` |
| **.NET** | `Pulumi.AzureNative` | `Pulumi.Azure` | `Pulumi.AzureAD` | `Pulumi.AzureDevOps` |
| **Java** | `com.pulumi/azure-native` | `com.pulumi/azure` | `com.pulumi/azuread` | `com.pulumi/azuredevops` |
| **Built on** | ARM API specs (auto-generated) | Terraform AzureRM (bridged) | Microsoft Graph API | Azure DevOps REST API |
| **Manages** | All Azure cloud resources | Azure cloud resources (subset) | Entra ID users, groups, apps, SPs | Projects, repos, pipelines |
| **Maintenance** | Pulumi (official) | Pulumi (official) | Pulumi (official) | Pulumi (official) |
| **Best for** | All new Azure projects | Existing Azure Classic projects | Identity and access management | DevOps platform automation |

## The Azure Native provider

The [Azure Native provider (`@pulumi/azure-native`)](/registry/packages/azure-native/) is the recommended
choice for managing Azure cloud resources with Pulumi. It is generated directly from the Azure Resource
Manager (ARM) OpenAPI specifications that Microsoft publishes, which means it achieves 100% API coverage
on the day new services and properties become available. Resources in Azure Native use PascalCase property
names that match the ARM API, and each resource type can be pinned to a specific ARM API version,
giving you granular control over compatibility and upgrade cadence.

```typescript
import * as resources from "@pulumi/azure-native/resources";
import * as network from "@pulumi/azure-native/network";

const rg = new resources.ResourceGroup("my-rg", {
    location: "eastus",
});

const vnet = new network.VirtualNetwork("my-vnet", {
    resourceGroupName: rg.name,
    location: rg.location,
    addressSpace: { addressPrefixes: ["10.0.0.0/16"] },
});
```

### azure-native versioning

The Azure Native provider follows semantic versioning and has gone through three major versions since its
introduction. The current major version is **v3**, and all new projects should target it. Earlier major
versions are still supported for existing users:

| Version | Status | Registry |
|---|---|---|
| v3 (current) | Actively developed | [/registry/packages/azure-native/](/registry/packages/azure-native/) |
| v2 | Supported, maintenance only | [/registry/packages/azure-native-v2/](/registry/packages/azure-native-v2/) |
| v1 | Supported, maintenance only | Available via version selector on the registry page |

Major version upgrades are documented with migration guides on the registry page. Within a major version,
upgrades are backward compatible and straightforward.

## The Azure Classic provider

The [Azure Classic provider (`@pulumi/azure`)](/registry/packages/azure/) is built on the Terraform
AzureRM provider via the Pulumi Terraform bridge. It was Pulumi's original Azure provider, predating the
auto-generated Azure Native approach. Pulumi continues to support it for teams that have existing
infrastructure managed with Azure Classic, but it is not recommended for new projects.

Azure Classic covers a subset of Azure resources and receives new resources and API updates more slowly
than Azure Native, since changes must flow through the upstream Terraform provider first. If you are
currently using Azure Classic and want to migrate, see the
[migration guide from Azure Classic to Azure Native](/registry/packages/azure-native/from-classic/).

## The Azure AD / Entra ID provider

The [Azure Active Directory provider (`@pulumi/azuread`)](/registry/packages/azuread/) manages identity
resources in Microsoft Entra ID (formerly known as Azure Active Directory). It is a distinct provider from
`azure-native` because it targets the **Microsoft Graph API** rather than the Azure Resource Manager API.
Microsoft Graph is a separate API surface that governs directory objects — users, groups, application
registrations, service principals, conditional access policies, and other Entra ID constructs.

{{% notes type="info" %}}
Microsoft rebranded Azure Active Directory (Azure AD) to **Microsoft Entra ID** in 2023. The Pulumi
package retains the `azuread` name for backward compatibility, but the resources it manages are the same
as those in the Microsoft Entra admin center.
{{% /notes %}}

The `azuread` provider is used together with `azure-native` in almost every real-world Azure deployment,
because applications running on Azure infrastructure typically need service principals and managed identity
configurations. For example, an AKS cluster provisioned with `azure-native` commonly requires a service
principal or an Entra ID application registration, which you configure with `azuread` in the same Pulumi
program.

```typescript
import * as azuread from "@pulumi/azuread";
import * as resources from "@pulumi/azure-native/resources";
import * as containerservice from "@pulumi/azure-native/containerservice";

// Create an Entra ID application and service principal for AKS
const app = new azuread.Application("aks-app", {
    displayName: "aks-service-principal",
});

const sp = new azuread.ServicePrincipal("aks-sp", {
    clientId: app.clientId,
});

const spPassword = new azuread.ServicePrincipalPassword("aks-sp-password", {
    servicePrincipalId: sp.id,
});

// Create an AKS cluster using the Azure Native provider
const rg = new resources.ResourceGroup("aks-rg", { location: "eastus" });

const cluster = new containerservice.ManagedCluster("aks-cluster", {
    resourceGroupName: rg.name,
    location: rg.location,
    agentPoolProfiles: [{
        count: 2,
        vmSize: "Standard_DS2_v2",
        name: "agentpool",
        mode: "System",
    }],
    servicePrincipalProfile: {
        clientId: app.clientId,
        secret: spPassword.value,
    },
    dnsPrefix: "my-aks",
});
```

The `azuread` provider requires credentials to your Entra ID tenant. Configuration is typically shared
with `azure-native` via the common `ARM_TENANT_ID`, `ARM_CLIENT_ID`, and `ARM_CLIENT_SECRET` environment
variables, or via the Azure CLI (`az login`).

## The Azure DevOps provider

The [Azure DevOps provider (`@pulumi/azuredevops`)](/registry/packages/azuredevops/) manages Azure DevOps
organizational resources via the Azure DevOps Service REST API. It is independent of both ARM and Microsoft
Graph — it targets the DevOps platform itself rather than Azure cloud resources or identity objects.

Use the Azure DevOps provider to automate the configuration of your DevOps platform: creating projects,
configuring Git repositories, defining build pipelines, managing service connections, setting branch
policies, and administering agent pools. This is useful in platform engineering contexts where teams
want to treat DevOps configuration as code and manage it with the same tools they use to manage their
cloud infrastructure.

```typescript
import * as azuredevops from "@pulumi/azuredevops";

const project = new azuredevops.Project("my-project", {
    name: "my-project",
    visibility: "private",
    versionControl: "Git",
    workItemTemplate: "Agile",
});

const repo = new azuredevops.Git("my-repo", {
    projectId: project.id,
    name: "my-repo",
    initialization: {
        initType: "Clean",
    },
});

const pipeline = new azuredevops.BuildDefinition("my-pipeline", {
    projectId: project.id,
    name: "CI Pipeline",
    repository: {
        repoId: repo.id,
        repoType: "TfsGit",
        ymlPath: "azure-pipelines.yml",
    },
});
```

The Azure DevOps provider requires an organization service URL and a Personal Access Token (PAT), supplied
via the `AZDO_ORG_SERVICE_URL` and `AZDO_PERSONAL_ACCESS_TOKEN` environment variables, or through the
Pulumi provider configuration.

## The community AzAPI package

The [`azapi` package](/registry/packages/azapi/) is a community-maintained provider built by
[`@dirien`](https://github.com/dirien/pulumi-azapi) on top of the Terraform AzAPI provider. It provides a
generic approach to ARM resource management using JSON body definitions and ARM type strings (e.g.,
`"Microsoft.Web/serverfarms@2020-06-01"`), without requiring typed resource classes for each resource.

This approach is analogous to using raw ARM templates or making direct REST calls, just with Pulumi's
dependency graph and state management layered on top.

{{% notes type="warning" %}}
The `azapi` package is **community-maintained**, not an official Pulumi product. It is published under
the `@ediri/` package namespace (not `@pulumi/`). The package has historically seen limited
maintenance activity. For most use cases, the Azure Native provider is the better choice: it is
Pulumi-maintained, auto-generated from the same ARM specifications, and provides typed, Pulumi-idiomatic
resources for every ARM resource type.
{{% /notes %}}

A scenario where `azapi` has historically been useful is accessing a brand-new or preview ARM resource
type before Pulumi has published an updated `azure-native` release. In practice, because `azure-native`
auto-generates from the ARM spec with a very fast release cadence, this gap is rarely significant.

## Composing providers in a single program

In most real-world Azure deployments, you will use `azure-native` and `azuread` together. Occasionally
you will add `azuredevops` as well if you are also automating DevOps platform configuration. Pulumi
programs support any number of providers simultaneously, and provider credentials are configured
independently so that each provider can authenticate to its respective API surface.

The following example shows a complete pattern combining `azure-native` and `azuread`:

{{< example-program path="azure-providers" >}}

## Choosing the right provider

The following table summarizes which provider to use for common Azure tasks:

| Task | Provider |
|------|----------|
| Create a resource group, VNet, VM, storage account, AKS cluster, etc. | `azure-native` |
| Create Entra ID users, groups, or administrative units | `azuread` |
| Register an application in Entra ID | `azuread` |
| Create a service principal for a workload | `azuread` |
| Manage role assignments and RBAC | `azure-native` (Authorization module) |
| Create Azure DevOps projects and repositories | `azuredevops` |
| Define build pipelines and agent pools | `azuredevops` |
| Manage service connections in Azure DevOps | `azuredevops` |
| Migrate from Azure Classic to Azure Native | See the [migration guide](/registry/packages/azure-native/from-classic/) |

## Next steps

- [Get started with Azure](/docs/iac/get-started/azure/)
- [Azure Native API reference](/registry/packages/azure-native/api-docs/)
- [Azure Native installation and configuration](/registry/packages/azure-native/installation-configuration/)
- [Migrate from Azure Classic to Azure Native](/registry/packages/azure-native/from-classic/)
