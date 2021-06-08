---
title: AzureAD
meta_desc: This page provides an overview of the Azure Active Directoy Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-azuread
    weight: 2
---

<img src="/logos/tech/azuread.svg" align="right" class="h-16 px-8 pb-4">

The AzureAD provider for Pulumi can be used to provision any of the Azure Active Directory resources available in [Azure](https://azure.microsoft.com/en-us/).
The AzureAD provider must be configured with credentials to deploy and update resources in Azure.

See the [full API documentation]({{< relref "/docs/reference/pkg/azuread" >}}) for complete details of the available AzureAD provider APIs.

## Setup

The AzureAD provider supports several options for providing access to Azure credentials.  See the [Azure setup page]({{< relref "/docs/intro/cloud-providers/azure-classic/setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const azad = require("@pulumi/azuread")

const group = new azad.Group("my-group", {
    name: "my-group",
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as azad from "@pulumi/azuread";

const group = new azad.Group("my-group", {
    name: "my-group",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_azuread as azad

group = azad.Group("my-group",
            name="my-group")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	azad "github.com/pulumi/pulumi-azuread/sdk/v4/go/azuread"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		group, err := azad.NewGroup(ctx, "my-group", &azad.GroupArgs{
			Name: pulumi.String("my-group"),
		})
		if err != nil {
			return err
		}

		return nil
	})
}

```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.AzureAD;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var group = new Group("my-group", new GroupArgs
            {
                Name = "my-group",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/azuread`](https://www.npmjs.com/package/@pulumi/azuread)
* Python: [`pulumi-azuread`](https://pypi.org/project/pulumi-azuread/)
* Go: [`github.com/pulumi/pulumi-azuread/sdk/v4/go/azuread`](https://github.com/pulumi/pulumi-azuread)
* .NET: [`Pulumi.AzureAD`](https://www.nuget.org/packages/Pulumi.AzureAD)

The AzureAD provider is open source and available in the [pulumi/pulumi-azuread](https://github.com/pulumi/pulumi-azuread) repo.
