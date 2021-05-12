---
title: Azure-Native
meta_desc: The native Azure provider for Pulumi can be used to provision any of the cloud resources available in Azure via Azure Resource Manager (ARM).
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-azure
    weight: 1
aliases: ["/docs/reference/clouds/azure/"]
---

<img src="/logos/tech/azure.svg" align="right" class="h-16 px-8 pb-4">

The native Azure provider for Pulumi can be used to provision any of the cloud resources available in [Azure](https://azure.microsoft.com/en-us/) via Azure Resource Manager (ARM). The Azure provider must be configured with credentials to deploy and update resources in Azure.

See the [full API documentation]({{< relref "/docs/reference/pkg/azure-native" >}}) for complete details of the available Azure provider APIs.

## Setup

The native Azure provider supports several options for providing access to Azure credentials.  See [Azure setup page]({{< relref "/docs/intro/cloud-providers/azure/setup" >}}) for details.

## Getting Started

The quickest way to get started with Azure is to follow the [Get Started]({{< relref "/docs/get-started/azure" >}}) guide.

From there, you can dive deeper with additional Azure examples:

* [Azure Function Apps](https://github.com/pulumi/examples/tree/master/azure-ts-functions): Create a serverless function
* [Azure AppService with SQL and AppInsights](https://github.com/pulumi/examples/tree/master/azure-ts-appservice): Build an AppService web application that uses SQL and AppInsights
* [Azure Kubernetes Service (AKS) Cluster](https://github.com/pulumi/examples/tree/master/azure-ts-aks): Create an AKS cluster
* [Azure Container Instances](https://github.com/pulumi/examples/tree/master/azure-ts-aci): Deploy a web app to Azure Container Intances

## Migration

The differences between the classic Azure provider and the native Azure provider and the process of migration are outlined in the [Migration Guide]({{< relref "./from-classic" >}}) guide.

If you are migrating from Azure Resource Manager templates, read our [Migrate From Azure Resource Manager]({{< relref "/docs/guides/adopting/from_azure" >}}) guide.

## Example

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```typescript
import * as resources from "@pulumi/azure-native/resources";

const resourceGroup = new resources.ResourceGroup("resourceGroup");
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_azure_native as azure_native

resource_group = azure_native.resources.ResourceGroup("resourceGroup")
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.AzureNative.Resources;

class MyStack : Stack
{
    public MyStack()
    {
        var resourceGroup = new ResourceGroup("resourceGroup");
    }

}

class Program
{
    static Task<int> Main(string[] args) => Deployment.RunAsync<MyStack>();
}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-azure-native/sdk/go/azure/resources"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        _, err := resources.NewResourceGroup(ctx, "resourceGroup", nil)
        if err != nil {
            return err
        }
        return nil
    })
}
```

{{% /choosable %}}

{{< /chooser >}}

Above is one example of an Azure resource group using Pulumi. You can find additional examples in [the Pulumi examples repo](https://github.com/pulumi/examples).

## Libraries

The following packages are available in package managers:

* JavaScript/TypeScript: [`@pulumi/azure-native`](https://www.npmjs.com/package/@pulumi/azure-native)
* Python: [`pulumi-azure-native`](https://pypi.org/project/pulumi-azure-native/)
* Go: [`github.com/pulumi/pulumi-azure-native/sdk/go/azure`](https://github.com/pulumi/pulumi-azure-native)
* .NET: [`Pulumi.AzureNative`](https://www.nuget.org/packages/Pulumi.AzureNative)

The native Azure provider SDKs are open source and available in the [pulumi/pulumi-azure-native](https://github.com/pulumi/pulumi-azure-native) repo.

## Easy SDK Integration

The native Azure provider SDKs provide convenience helpers to hydrate an Azure SDK client in each supported language seeded with the provider's configured credentials. This allows users to operate on resources that are not compatible with Pulumi's resource model and may not be included in the Pulumi SDKs. See below for links to examples in each of the supported languages that demonstrate invoking the Azure SDK client:

* [Typescript](https://github.com/pulumi/examples/tree/master/azure-ts-call-azure-sdk)
* [Go](https://github.com/pulumi/examples/tree/master/azure-go-call-azure-sdk)
* [C#](https://github.com/pulumi/examples/tree/master/azure-cs-call-azure-api)
* [Python](https://github.com/pulumi/examples/tree/master/azure-py-call-azure-sdk)

## Versioning

The native Azure provider SDKs provide access to all API versions of each Azure resource. This way, you can access the entire Azure API surface and pin to the version you prefer.

The [Version Guide]({{< relref "./version-guide" >}}) describes the versioning in detail, including both module-per-version and top-level-resources approaches.

## Configuration

The native Azure provider accepts the following configuration settings. These can be provided via `pulumi config set azure-native:<option>`, or passed to the constructor of [Provider]({{< relref "/docs/reference/pkg/azure-native/provider" >}}) to construct a specific instance of the Azure provider.

* `auxiliaryTenantIds`: (Optional) It can also be sourced from the following environment variable: ARM_AUXILIARY_TENANT_IDS
* `clientCertificatePassword`: (Optional) The password associated with the Client Certificate. For use when authenticating as a Service Principal using a Client Certificate It can also be sourced from the following environment variable: ARM_CLIENT_CERTIFICATE_PASSWORD
* `clientCertificatePath`: (Optional) The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate. It can also be sourced from the following environment variable: ARM_CLIENT_CERTIFICATE_PATH
* `clientId`: (Optional) The Client ID which should be used. It can also be sourced from the following environment variable: ARM_CLIENT_ID
* `clientSecret`: (Optional) The Client Secret which should be used. For use When authenticating as a Service Principal using a Client Secret. It can also be sourced from the following environment variable: ARM_CLIENT_SECRET
* `disablePulumiPartnerId`: (Optional) This will disable the Pulumi Partner ID which is used if a custom partnerId isn’t specified. It can also be sourced from the following environment variable: ARM_DISABLE_PULUMI_PARTNER_ID
* `environment`: (Optional) The Cloud Environment which should be used. Possible values are public, usgovernment, german, and china. Defaults to public. It can also be sourced from the following environment variable: ARM_ENVIRONMENT
* `msiEndpoint`: (Optional) The path to a custom endpoint for Managed Service Identity - in most circumstances this should be detected automatically. It can also be sourced from the following environment variable: ARM_MSI_ENDPOINT
* `partnerId`: (Optional) A GUID/UUID that is registered with Microsoft to facilitate partner resource usage attribution. It can also be sourced from the following environment variable: ARM_PARTNER_ID
* `subscriptionId`: (Optional) The Subscription ID which should be used. It can also be sourced from the following environment variable: ARM_SUBSCRIPTION_ID
* `tenantId`: (Optional) The Tenant ID which should be used. It can also be sourced from the following environment variable: ARM_TENANT_ID
* `useMsi`: (Optional) Allowed Managed Service Identity be used for Authentication. It can also be sourced from the following environment variable: ARM_USE_MSI

For Pulumi support and troubleshooting, click the links in the sidebar on the left of the page.
