---
title: F5 BIG-IP
meta_desc: This page provides an overview of the F5 BIG-IP Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-f5bigip
    weight: 2
---

<img src="/logos/tech/f5bigip.svg" align="right" class="h-16 px-8 pb-4">

The F5 BIG-IP provider for Pulumi can be used to provision any of the resources available with [F5 BIG-IP](https://www.f5.com/products/big-ip-services).
The F5 BIG-IP provider must be configured with credentials to deploy and update the resources.

See the [full API documentation]({{< relref "/docs/reference/pkg/f5bigip" >}}) for complete details of the available F5 BIG-IP provider APIs.

## Setup

The F5 BIG-IP provider supports several options for providing access to F5 BIG-IP credentials.  See the [F5 BIG-IP setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const f5bigip = require("@pulumi/f5bigip")

const monitor = new f5bigip.ltm.Monitor("backend", {
    name: "/Common/backend",
    parent: "/Common/http",
    send: "GET /\r\n",
    timeout: 5,
    interval: 10,
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as f5bigip from "@pulumi/f5bigip";

const monitor = new f5bigip.ltm.Monitor("backend", {
    name: "/Common/backend",
    parent: "/Common/http",
    send: "GET /\r\n",
    timeout: 5,
    interval: 10,
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_f5bigip as f5bigip

monitor = f5bigip.ltm.Monitor("backend",
  name="/Common/backend",
  parent="/Common/http",
  send="GET /\r\n",
  timeout=5,
  interval=10,
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
  ltm "github.com/pulumi/pulumi-f5bigip/sdk/v2/go/f5bigip/ltm"
)

monitor, _ := ltm.NewMonitor(ctx, "backend", &ltm.MonitorArgs{
  Name:     pulumi.String("/Common/backend"),
  Parent:   pulumi.String("/Common/http"),
  Send:     pulumi.String("GET /\r\n"),
  Timeout:  pulumi.Int(5),
  Interval: pulumi.Int(10),
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.F5bigip.Ltm;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var monitor = new Monitor("backend", new MonitorArgs
            {
                Name = "/Common/backend",
                Parent = "/Common/http",
                Send = "GET /\r\n",
                Timeout = 5,
                Interval = 100,
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/f5bigip`](https://www.npmjs.com/package/@pulumi/f5bigip)
* Python: [`pulumi-f5bigip`](https://pypi.org/project/pulumi-f5bigip/)
* Go: [`github.com/pulumi/pulumi-f5bigip/sdk/go/f5bigip`](https://github.com/pulumi/pulumi-f5bigip)
* .NET: [`Pulumi.F5bigip`](https://www.nuget.org/packages/Pulumi.F5bigip)

The F5 BIG-IP provider is open source and available in the [pulumi/pulumi-f5bigip](https://github.com/pulumi/pulumi-f5bigip) repo.
