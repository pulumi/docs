---
title: Cloudflare
meta_desc: This page provides an overview of the Cloudflare Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-cloudflare
    weight: 2
---

<img src="/logos/tech/cloudflare.png" align="right" class="h-16 px-8 pb-4">

The Cloudflare provider for Pulumi can be used to provision any of the resources available in [Cloudflare](https://www.cloudflare.com/).

See the [full API documentation]({{< relref "/docs/reference/pkg/cloudflare" >}}) for complete details of the available Cloudflare provider APIs.

## Setup

The Cloudflare provider supports several options for interacting with Cloudflare.  See the [Cloudflare setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const cloudflare = require("@pulumi/cloudflare")

const record = new cloudflare.Record("sample-record", {
  name: "my-record",
  zoneId: "xxsdfhsfkashadf",
  type: "A",
  value: "192.168.0.11",
  ttl: 3600
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as cloudflare from "@pulumi/cloudflare";

const record = new cloudflare.Record("sample-record", {
  name: "my-record",
  zoneId: "xxsdfhsfkashadf",
  type: "A",
  value: "192.168.0.11",
  ttl: 3600
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_cloudflare as cloudflare

record = cloudflare.Record("sample-record",
  name="my-record",
  zone_id="xxsdfhsfkashadf",
  type="A",
  value="192.168.0.11",
  ttl=3600
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
  cloudflare "github.com/pulumi/pulumi-cloudflare/sdk/v2/go/cloudflare"
)

record, _ := cloudflare.NewRecord(ctx, "sample-record", &cloudflare.RecordArgs{
  Name:   pulumi.String("my-record"),
  ZoneId: pulumi.String("xxsdfhsfkashadf"),
  Type:   pulumi.String("A"),
  Value:  pulumi.String("192.168.0.11"),
  Ttl:    pulumi.Int(3600),
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Cloudflare;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var record = new Cloudflare.Record("sample-record", new Cloudflare.RecordArgs
            {
                Name = "my-record",
                ZoneId = "xxsdfhsfkashadf",
                Type = "A",
                Value = "192.168.0.11",
                Ttl = 3600,
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/cloudflare`](https://www.npmjs.com/package/@pulumi/cloudflare)
* Python: [`pulumi-cloudflare`](https://pypi.org/project/pulumi-cloudflare/)
* Go: [`github.com/pulumi/pulumi-cloudflare/sdk/go/cloudflare`](https://github.com/pulumi/pulumi-cloudflare)
* .NET: [`Pulumi.Cloudflare`](https://www.nuget.org/packages/Pulumi.Cloudflare)

The Cloudflare provider is open source and available in the [pulumi/pulumi-cloudflare](https://github.com/pulumi/pulumi-cloudflare) repo.
