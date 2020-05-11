---
title: HashiCorp Consul
meta_desc: This page provides an overview of the HashiCorp Consul Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-consul
    weight: 2
---

<img src="/logos/tech/consul.png" align="right" class="h-16 px-8 pb-4">

The HashiCorp Consul provider for Pulumi can be used to provision any of the resources available in [Consul](https://www.consul.io/).

See the [full API documentation]({{< relref "/docs/reference/pkg/consul" >}}) for complete details of the available Consul provider APIs.

## Setup

The Consul provider supports several options for interacting with HashiCorp Consul.  See the [Consul setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const consul = require("@pulumi/consul")

const node = new consul.Node("compute", {
  address: "www.google.com"
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as consul from "@pulumi/consul";

const node = new consul.Node("compute", {
  address: "www.google.com"
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_consul as consul

node = consul.Node("compute",
  address='www.google.com'
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  consul "github.com/pulumi/pulumi-consul/sdk/v2/go/consul"
)

node, _ := consul.NewNode(ctx, "compute", &consul.NodeArgs{
  Address: "www.google.com",
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Consul;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var node = new Consul.Node("compute", new Consul.NodeArgs
            {
                Address = "www.google.com",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/consul`](https://www.npmjs.com/package/@pulumi/consul)
* Python: [`pulumi-consul`](https://pypi.org/project/pulumi-consul/)
* Go: [`github.com/pulumi/pulumi-consul/sdk/go/consul`](https://github.com/pulumi/pulumi-consul)
* .NET: [`Pulumi.Consul`](https://www.nuget.org/packages/Pulumi.Consul)

The HashiCorp Consul provider is open source and available in the [pulumi/pulumi-consul](https://github.com/pulumi/pulumi-consul) repo.
