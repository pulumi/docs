---
title: vSphere
meta_desc: This page provides an overview of the vSphere provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-vsphere
    weight: 2

aliases: ["/docs/reference/clouds/vsphere/"]
---

The vSphere provider for Pulumi can be used to provision any of the cloud resources available in [vSphere](https://www.vmware.com/products/vsphere.html).
The vSphere provider must be configured with credentials to deploy and update resources in vSphere.

See the [full API documentation]({{< relref "/docs/reference/pkg/vsphere" >}}) for complete details of the available vSphere provider APIs.

## Setup

The vSphere provider supports several options for providing access to vSphere credentials.  See [vSphere setup page]({{< relref "/docs/intro/cloud-providers/vsphere/setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const vsphere = require("@pulumi/vsphere")
const dc = new vsphere.Datacenter("my-dc", {
  name: "Production-DataCenter",
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as vsphere from "@pulumi/vsphere";
const dc = new vsphere.Datacenter("my-dc", {
  name: "Production-DataCenter",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_vsphere as vsphere
dc = vsphere.Datacenter("my-dc",
  name='Production-DataCenter',
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
    vsphere "github.com/pulumi/pulumi-vsphere/sdk/v2/go/vsphere"
)
dc, _ := vsphere.NewDatacenter(ctx, "test", &vsphere.DatacenterArgs{
  Name: pulumi.String("Production-DataCenter")
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Vsphere;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var dc = new Vsphere.Datacenter("my-dc", new Vsphere.DatacenterArgs
            {
                Name = "Production-DataCenter",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/vsphere`](https://www.npmjs.com/package/@pulumi/vsphere)
* Python: [`pulumi-vsphere`](https://pypi.org/project/pulumi-vsphere/)
* Go: [`github.com/pulumi/pulumi-vsphere/sdk/go/vsphere`](https://github.com/pulumi/pulumi-vsphere)
* .NET: [`Pulumi.Vsphere`](https://www.nuget.org/packages/Pulumi.Vsphere)

The vSphere provider is open source and available in the [pulumi/pulumi-vsphere](https://github.com/pulumi/pulumi-vsphere) repo.
