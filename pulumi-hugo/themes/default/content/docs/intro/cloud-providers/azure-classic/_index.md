---
title: Azure Classic
meta_desc: The classic Azure provider for Pulumi can be used to provision any of the cloud resources available in Azure.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-azure-classic
    weight: 2
---

{{% notes %}}
We recommend using the [Azure Native provider]({{< relref "/docs/intro/cloud-providers/azure" >}}) to provision Azure infrastructure. Azure Native provides complete coverage of Azure resources and same-day access to new resources and resource updates because it’s built and automatically from the Azure Resource Manager API.

Azure Classic is based on the Terraform AzureRM provider. It has fewer resources and resource options and receives new Azure features more slowly than Azure Native. However, Azure Classic remains fully-supported for existing usage.
{{% /notes %}}

<img src="/logos/tech/azure.svg" align="right" class="h-16 px-8 pb-4">

The classic Azure provider for Pulumi can be used to provision any of the cloud resources available in [Azure](https://azure.microsoft.com/en-us/) via Azure Resource Manager (ARM).  The Azure provider must be configured with credentials to deploy and update resources in Azure.

See the [full API documentation]({{< relref "/docs/reference/pkg/azure" >}}) for complete details of the available Azure provider APIs.

## Setup

The Azure provider supports several options for providing access to Azure credentials.  See [Azure setup page]({{< relref "/docs/intro/cloud-providers/azure-classic/setup" >}}) for details.

## Example

```javascript
const azure = require("@pulumi/azure")

const resourceGroupName = new azure.core.ResourceGroup("my-group", {
    location: "westus2",
});
```

Above is one example of an Azure resource group using Pulumi. You can find additional examples in [the Pulumi examples repo](https://github.com/pulumi/examples).

## Libraries

The following packages are available in package managers:

* JavaScript/TypeScript: [`@pulumi/azure`](https://www.npmjs.com/package/@pulumi/azure)
* Python: [`pulumi-azure`](https://pypi.org/project/pulumi-azure/)
* Go: [`github.com/pulumi/pulumi-azure/sdk/v4/go/azure`](https://github.com/pulumi/pulumi-azure)
* .NET: [`Pulumi.Azure`](https://www.nuget.org/packages/Pulumi.Azure)

The classic Azure provider is open source and available in the [pulumi/pulumi-azure](https://github.com/pulumi/pulumi-azure) repo.

## Configuration

The Azure provider accepts the following configuration settings.  These can be provided to the default Azure provider via `pulumi config set azure:<option>`, or passed to the constructor of [Provider]({{< relref "/docs/reference/pkg/azure/provider" >}}) to construct a specific instance of the Azure provider.

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

For Pulumi support and troubleshooting, click the links in the sidebar on the left of the page.
