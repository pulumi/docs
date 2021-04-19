---
title: Civo
meta_desc: This page provides an overview of the Civo Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-civo
    weight: 2
---

<img src="/logos/tech/civo.png" align="right" class="h-16 px-8 pb-4">

The Civo provider for Pulumi can be used to provision any of the cloud resources available in [Civo](https://www.civo.com/).
The Civo provider must be configured with credentials to deploy and update resources in Civo.

See the [full API documentation]({{< relref "/docs/reference/pkg/civo" >}}) for complete details of the available Civo provider APIs.

## Setup

The Civo provider supports several options for providing access to Civo credentials.  See the [Civo setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const civo = require("@pulumi/civo")

const network = new civo.Network("demo", {
    label: "demo-network"
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as civo from "@pulumi/civo";

const network = new civo.Network("demo", {
    label: "demo-network-typescript"
});

```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_civo as civo

network = civo.Network("demo",
  label="demo-network")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi-civo/sdk/go/civo"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		network, err := civo.NewNetwork(ctx, "demo", &civo.NetworkArgs{
			Label: pulumi.String("demo-network"),
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
using Pulumi.Civo;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var network = new Network("demo", new NetworkArgs
            {
                Label = "demo-network",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/civo`](https://www.npmjs.com/package/@pulumi/civo)
* Python: [`pulumi-civo`](https://pypi.org/project/pulumi-civo/)
* Go: [`github.com/pulumi/pulumi-civo/sdk/go/civo`](https://github.com/pulumi/pulumi-civo)
* .NET: [`Pulumi.Civo`](https://www.nuget.org/packages/Pulumi.Civo)

The Civo provider is open source and available in the [pulumi/pulumi-civo](https://github.com/pulumi/pulumi-civo) repo.
