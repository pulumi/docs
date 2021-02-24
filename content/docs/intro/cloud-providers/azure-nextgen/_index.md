---
title: Azure Next Gen
meta_desc: The Azure Next Gen provider for Pulumi can be used to provision any of the cloud resources available in Azure via Azure Resource Manager (ARM).
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-azure-nextgen
    weight: 1
---

<img src="/logos/tech/azure.svg" align="right" class="h-16 px-8 pb-4">

The Azure Next Gen provider for Pulumi can be used to provision any of the cloud resources available in [Azure](https://azure.microsoft.com/en-us/) via Azure Resource Manager (ARM).  The Azure provider must be configured with credentials to deploy and update resources in Azure.

See the [full API documentation]({{< relref "/docs/reference/pkg/azure-nextgen" >}}) for complete details of the available Azure provider APIs.

## Setup

The Azure Next Gen provider supports several options for providing access to Azure credentials.  See [Azure setup page]({{< relref "/docs/intro/cloud-providers/azure-nextgen/setup" >}}) for details.

## Getting Started

**TODO: Update this section.**

The quickest way to get started with Azure is to follow the [Get Started]({{< relref "/docs/get-started/azure" >}}) guide.

Additionally, a tutorial is available to follow:

* [Azure Container Instances Web Server]({{< relref "/docs/tutorials/azure/container-webserver" >}}): Create an NGINX web server Azure Container Instance

In addition to the tutorial, several interesting examples are available complete with instructions:

* [Azure Function Apps](https://github.com/pulumi/examples/tree/master/azure-ts-functions): Create a serverless function
* [Azure AppService with SQL and AppInsights](https://github.com/pulumi/examples/tree/master/azure-ts-appservice): Build an AppService web application that uses SQL and AppInsights
* [Azure Kubernetes Service (AKS) Cluster](https://github.com/pulumi/examples/tree/master/azure-ts-aks-helm): Create an AKS cluster and deploy a Helm Chart into it
* [Azure CosmosDB, AKS and Node.js](https://github.com/pulumi/examples/tree/master/azure-ts-aks-mean): Stands up an AKS cluster and a MongoDB-flavored instance of CosmosDB used by a Node.js application.

## Example

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```typescript
import * as resources from "@pulumi/azure-nextgen/resources/latest";

const resourceGroup = new resources.ResourceGroup("resourceGroup", {
  resourceGroupName: "my-rg",
  location: "WestUS",
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_azure_nextgen as azure_nextgen

resource_group = azure_nextgen.resources.latest.ResourceGroup("resourceGroup",
                                                              resource_group_name="my-rg",
                                                              location="WestUS")
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using AzureNextGen = Pulumi.AzureNextGen;

class MyStack : Stack
{
    public MyStack()
    {
        var resourceGroup = new AzureNextGen.Resources.Latest.ResourceGroup("resourceGroup", new AzureNextGen.Resources.Latest.ResourceGroupArgs
        {
            ResourceGroupName = "my-rg",
            Location = "WestUS",
        });
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
    resources "github.com/pulumi/pulumi-azure-nextgen/sdk/go/azure/resources/latest"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        _, err := resources.NewResourceGroup(ctx, "resourceGroup", &resources.ResourceGroupArgs{
            ResourceGroupName: pulumi.String("my-rg"),
            Location:          pulumi.String("WestUS"),
        })
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

* JavaScript/TypeScript: [`@pulumi/azure-nextgen`](https://www.npmjs.com/package/@pulumi/azure-nextgen)
* Python: [`pulumi-azure-nextgen`](https://pypi.org/project/pulumi-azure-nextgen/)
* Go: [`github.com/pulumi/pulumi-azure-nextgen/sdk/go/azure`](https://github.com/pulumi/pulumi-azure-nextgen)
* .NET: [`Pulumi.AzureNextGen`](https://www.nuget.org/packages/Pulumi.AzureNextGen)

The Azure Next Gen provider is open source and available in the [pulumi/pulumi-azure-nextgen](https://github.com/pulumi/pulumi-azure-nextgen) repo.

## Configuration

The Azure provider accepts the following configuration settings.  These can be provided to the default Azure provider via `pulumi config set azure-nextgen:<option>`, or passed to the constructor of [Provider]({{< relref "/docs/reference/pkg/azure-nextgen/provider" >}}) to construct a specific instance of the Azure provider.

* `auxiliaryTenantIds`: (Optional)
* `clientCertificatePassword`: (Optional) The password associated with the Client Certificate. For use when authenticating as a Service Principal using a Client Certificate.
* `clientCertificatePath`: (Optional) The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service Principal using a Client Certificate.
* `clientId`: (Optional) The Client ID which should be used.
* `clientSecret`: (Optional) The Client Secret which should be used. For use When authenticating as a Service Principal using a Client Secret.
* `disablePulumiPartnerId`: (Optional) This will disable the Pulumi Partner ID which is used if a custom partnerId isn’t specified.
* `environment`: (Optional) The Cloud Environment which should be used. Possible values are public, usgovernment, german, and china. Defaults to public.
* `msiEndpoint`: (Optional) The path to a custom endpoint for Managed Service Identity - in most circumstances this should be detected automatically.
* `partnerId`: (Optional) A GUID/UUID that is registered with Microsoft to facilitate partner resource usage attribution.
* `subscriptionId`: (Optional) The Subscription ID which should be used.
* `tenantId`: (Optional) The Tenant ID which should be used.
* `useMsi`: (Optional) Allowed Managed Service Identity be used for Authentication.

For Pulumi support and troubleshooting, click the links in the sidebar on the left of the page.
