---
title: NS1
meta_desc: This page provides an overview of the NS1 Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-ns1
    weight: 2
---

<img src="/logos/tech/ns1.png" align="right" class="h-16 px-8 pb-4">

The NS1 provider for Pulumi can be used to provision any of the cloud resources available in [NS1](https://www.ns1.com/).
The NS1 provider must be configured with credentials to deploy and update resources in NS1.

See the [full API documentation]({{< relref "/docs/reference/pkg/ns1" >}}) for complete details of the available NS1 provider APIs.

## Setup

The NS1 provider supports several options for providing access to NS1 credentials.  See the [NS1 setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const ns1 = require("@pulumi/ns1")

const myZone = new ns1.Zone("demo-zone", {
    zone: "demo.pulumi.io"
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as ns1 from "@pulumi/ns1";

const myZone = new ns1.Zone("demo-zone", {
    zone: "demo.pulumi.io"
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_ns1 as ns1

zone = ns1.Zone("demo-zone",
  zone="demo.pulumi.io",
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	ns1 "github.com/pulumi/pulumi-ns1/sdk/v2/go/ns1"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		zone, err := ns1.NewZone(ctx, "demo-zone", &ns1.ZoneArgs{
			Zone: pulumi.String("demo.pulumi.io"),
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
using Pulumi.Ns1;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var zone = new Zone("demo-zone", new ZoneArgs
            {
                ZoneName = "demo.pulumi.io",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/ns1`](https://www.npmjs.com/package/@pulumi/ns1)
* Python: [`pulumi-ns1`](https://pypi.org/project/pulumi-ns1/)
* Go: [`github.com/pulumi/pulumi-ns1/sdk/v2/go/ns1`](https://github.com/pulumi/pulumi-ns1)
* .NET: [`Pulumi.NS1`](https://www.nuget.org/packages/Pulumi.Ns1)

The NS1 provider is open source and available in the [pulumi/pulumi-ns1](https://github.com/pulumi/pulumi-ns1) repo.
