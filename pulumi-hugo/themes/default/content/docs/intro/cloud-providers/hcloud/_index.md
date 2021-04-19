---
title: Hetzner Cloud
meta_desc: This page provides an overview of the Hetzner Cloud Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-hcloud
    weight: 2
---

<img src="/logos/tech/hetzner.png" align="right" class="h-16 px-8 pb-4">

The Hetzner Cloud provider for Pulumi can be used to provision any of the cloud resources available in [Hetzner Cloud](https://www.hetzner.com/cloud).
The Hetzner Cloud provider must be configured with credentials to deploy and update resources in Hetzner Cloud.

See the [full API documentation]({{< relref "/docs/reference/pkg/hcloud" >}}) for complete details of the available Hetzner Cloud provider APIs.

## Setup

The Hetzner Cloud provider supports several options for providing access to Hetzner Cloud credentials.  See the [Hetzner Cloud setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const hcloud = require("@pulumi/hcloud")

const network = new hcloud.Network("demo-network", {
    ipRange: "10.0.1.0/24",
})
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as hcloud from "@pulumi/hcloud";

const network = new hcloud.Network("demo-network", {
    ipRange: "10.0.1.0/24",
})
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_hcloud as hcloud

network = hcloud.Network("demo-network",
  ip_range="10.0.1.0/24",
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	hcloud "github.com/pulumi/pulumi-hcloud/sdk/go/hcloud"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		network, err := hcloud.NewNetwork(ctx, "demo-network", &hcloud.NetworkArgs{
			IpRange: pulumi.String("10.0.1.0/24"),
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
using Pulumi.HCloud;

class Program
{
    static Task Main() =>
        Deployment.RunAsync(() => {
            var network = new Network("demo-network", new NetworkArgs
            {
                IpRange = "10.0.1.0/24",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/hcloud`](https://www.npmjs.com/package/@pulumi/hcloud)
* Python: [`pulumi-hcloud`](https://pypi.org/project/pulumi-hcloud/)
* Go: [`github.com/pulumi/pulumi-hcloud/sdk/go/hcloud`](https://github.com/pulumi/pulumi-hcloud)
* .NET: [`Pulumi.HCloud`](https://www.nuget.org/packages/Pulumi.HCloud)

The Hetzner Cloud provider is open source and available in the [pulumi/pulumi-hcloud](https://github.com/pulumi/pulumi-hcloud) repo.
