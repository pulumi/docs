---
title: libvirt
meta_desc: This page provides an overview of the libvirt Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-libvirt
    weight: 2
---

A Pulumi provider that lets you provision servers on a libvirt host using Pulumi.

See the [full API documentation]({{< relref "/docs/reference/pkg/libvirt" >}}) for complete details of the available libvirt provider APIs.

### Requirements

Please note, there is a requirement to have [libvirt](https://libvirt.org/) on the machine using the libvirt provider. You can
install this as follows:

{{< chooser os "linux,macos,windows" >}}

{{% choosable os linux %}}

* Refer to [Libvirt downloads](https://libvirt.org/downloads.html)

{{% /choosable %}}

{{% choosable os macos %}}

```bash
$ brew install libvirt
```

{{% /choosable %}}

{{% choosable os windows %}}

* Refer to [Libvirt Windows Instructions](https://libvirt.org/windows.html)

{{% /choosable %}}
{{< /chooser >}}

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const libvirt = require("@pulumi/libvirt")

const myPool = new libvirt.Pool("test", {
  type: "dir",
  path: "/home/user/cluster_storage"
})
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as libvirt from "@pulumi/libvirt";

const myPool = new libvirt.Pool("test", {
  type: "dir",
  path: "/home/user/cluster_storage"
})
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_libvirt as libvirt

pool = libvirt.Pool("demo-py-pool", type="dir", path="/home/user/cluster_storage")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  "github.com/pulumi/pulumi-libvirt/sdk/go/libvirt"
  "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
  pulumi.Run(func(ctx *pulumi.Context) error {
    pool, err := libvirt.NewPool(ctx, "cluster", &libvirt.PoolArgs{
        Type: pulumi.String("dir"),
        Path: pulumi.String("/home/user/cluster_storage"),
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
using Pulumi.Libvirt;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
          var cluster = new Libvirt.Pool("cluster", new Libvirt.PoolArgs
          {
              Type = "dir",
              Path = "/home/user/cluster_storage",
          });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/libvirt`](https://www.npmjs.com/package/@pulumi/libvirt)
* Python: [`pulumi-libvirt`](https://pypi.org/project/pulumi-libvirt/)
* Go: [`github.com/pulumi/pulumi-libvirt/sdk/go/libvirt`](https://github.com/pulumi/pulumi-libvirt)
* .NET: [`Pulumi.Libvirt`](https://www.nuget.org/packages/Pulumi.Libvirt)

The libvirt provider is open source and available in the [pulumi/pulumi-libvirt](https://github.com/pulumi/pulumi-libvirt) repo.
