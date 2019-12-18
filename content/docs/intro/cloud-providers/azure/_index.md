---
title: Azure
meta_desc: This page provides an overview of the Azure Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-azure
    weight: 2

aliases: ["/docs/reference/clouds/azure/"]
---

<img src="/logos/tech/azure.svg" align="right" class="h-16 px-8 pb-4">

The Azure provider for Pulumi can be used to provision any of the cloud resources available in [Azure](https://azure.microsoft.com/en-us/) via Azure Resource Manager (ARM).  The Azure provider must be configured with credentials to deploy and update resources in Azure.

See the [full API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/azure" >}}) for complete details of the available Azure provider APIs.

## Setup

The Azure provider supports several options for providing access to Azure credentials.  See [Azure setup page]({{< relref "/docs/intro/cloud-providers/azure/setup.md" >}}) for details.

## Getting Started

The quickest way to get started with Azure is to follow the [Get Started]({{< relref "/docs/get-started/azure" >}}) guide.

Additionally, a tutorial is available to follow:

* [Azure Container Instances Web Server]({{< relref "/docs/tutorials/azure/container-webserver" >}}): Create an NGINX web server Azure Container Instance

In addition to the tutorial, several interesting examples are available complete with instructions:

* [Azure Function Apps](https://github.com/pulumi/examples/tree/master/azure-ts-functions): Create a serverless function
* [Azure AppService with SQL and AppInsights](https://github.com/pulumi/examples/tree/master/azure-ts-appservice): Build an AppService web application that uses SQL and AppInsights
* [Azure Kubernetes Service (AKS) Cluster](https://github.com/pulumi/examples/tree/master/azure-ts-aks-helm): Create an AKS cluster and deploy a Helm Chart into it
* [Azure CosmosDB, AKS and Node.js](https://github.com/pulumi/examples/tree/master/azure-ts-aks-mean): Stands up an AKS cluster and a MongoDB-flavored instance of CosmosDB used by a Node.js application.

## Example

```javascript
const azure = require("@pulumi/azure")

const resourceGroupName = new azure.core.ResourceGroup("my-group", {
    location: "westus2",
});
```

You can find additional examples of using Azure in [the Pulumi examples repo](https://github.com/pulumi/examples).

## Libraries

The following packages are available in package managers:

* JavaScript/TypeScript: [`@pulumi/azure`](https://www.npmjs.com/package/@pulumi/azure)
* Python: [`pulumi-azure`](https://pypi.org/project/pulumi-azure/)
* Go: [`github.com/pulumi/pulumi-azure/sdk/go/azure`](https://github.com/pulumi/pulumi-azure)

The Azure provider is open source and available in the [pulumi/pulumi-azure](https://github.com/pulumi/pulumi-azure) repo.

## Configuration

The Azure provider accepts the following configuration settings.  These can be provided to the default Azure provider via `pulumi config set azure:<option>`, or passed to the constructor of `new azure.Provider` to construct a specific instance of the Azure provider.

* `environment`: (Required) The cloud environment to use. It can also be sourced from the ARM_ENVIRONMENT environment variable. Supported values are: `public` (default), `usgovernment`, `german`, `china`.
* `location`: (Optional) The location to use. ResourceGroups will consult this property for a default location, if one was not supplied explicitly.
* `clientId`: (Optional) The client ID to use. It can also be sourced from the `ARM_CLIENT_ID` environment variable.
* `clientSecret`: (Optional) The client secret to use. It can also be sourced from the `ARM_CLIENT_SECRET` environment variable.
* `msiEndpoint`: (Optional) The REST endpoint to retrieve an MSI token from. Pulumi will attempt to discover this automatically but it can be specified manually here. It can also be sourced from the `ARM_MSI_ENDPOINT` environment variable.
* `skipCredentialsValidation`: (Optional) Prevents the provider from validating the given credentials. When set to true, `skip_provider_registration` is assumed. It can also be sourced from the `ARM_SKIP_CREDENTIALS_VALIDATION` environment variable; defaults to `false`.
* `skipProviderRegistration`: (Optional) Prevents the provider from registering the ARM provider namespaces, this can be used if you don't wish to give the Active Directory Application permission to register resource providers. It can also be sourced from the `ARM_SKIP_PROVIDER_REGISTRATION` environment variable; defaults to `false`.
* `subscriptionId`: (Optional) The subscription ID to use. It can also be sourced from the `ARM_SUBSCRIPTION_ID` environment variable.
* `tenantId`: (Optional) The tenant ID to use. It can also be sourced from the `ARM_TENANT_ID` environment variable.
* `useMsi`: (Optional) Set to true to authenticate using managed service identity. It can also be sourced from the `ARM_USE_MSI` environment variable.
