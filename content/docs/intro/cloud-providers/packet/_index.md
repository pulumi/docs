---
title: Packet.net
meta_desc: This page provides an overview of the Packet.net provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-packet
    weight: 2

aliases: ["/docs/reference/clouds/packet/"]
---

<img src="/logos/tech/packet.svg" align="right" class="h-16 px-8 pb-4">

The Packet.net provider for Pulumi can be used to provision any of the cloud resources available in [Packet.net](https://www.packet.com).
The Packet.net provider must be configured with credentials to deploy and update resources in Packet.

See the [full API documentation]({{< relref "/docs/reference/pkg/packet" >}}) for complete details of the available Packet.net provider APIs.

## Setup

The Packet.net provider supports several options for providing access to Packet.net credentials.  See [Packet setup page]({{< relref "/docs/intro/cloud-providers/packet/setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const packet = require("@pulumi/packet")

const packet = new packet.Project("my-project", {
  name: "DevelopmentEnvironment"
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as packet from "@pulumi/packet";

const project = new packet.Project("my-project", {
  name: "DevelopmentEnvironment"
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_packet as packet
project = packet.Project("my-project",
  name='DevelopmentEnvironment'
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
    packet "github.com/pulumi/pulumi-packet/sdk/go/packet"
)

project, _ := packet.NewProject(ctx, "test", &packet.ProjectArgs{
  Name: "DevelopmentEnvironment"
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Packet;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var project = new Packet.Project("my-project", new Packet.ProjectArgs
            {
                Name = "DevelopmentEnvironment"
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/packet`](https://www.npmjs.com/package/@pulumi/packet)
* Python: [`pulumi-packet`](https://pypi.org/project/pulumi-packet/)
* Go: [`github.com/pulumi/pulumi-packet/sdk/go/packet`](https://github.com/pulumi/pulumi-packet)
* .NET: [`Pulumi.Packet`](https://www.nuget.org/packages/Pulumi.Packet)

The Packet.net provider is open source and available in the [pulumi/pulumi-packet](https://github.com/pulumi/pulumi-packet) repo.
