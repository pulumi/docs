---
title: OpenStack
meta_desc: This page provides an overview of the OpenStack Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-openstack
    weight: 5

aliases: ["/docs/reference/clouds/openstack/"]
---

<img src="/logos/tech/openstack.svg" align="right" class="h-16 px-8 pb-4">

The OpenStack provider for Pulumi can be used to provision any of the cloud resources available in [OpenStack](https://www.openstack.org/).  The OpenStack provider must be configured with credentials to deploy and update resources in an OpenStack cloud.

See the [full API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/openstack" >}}) for complete details of the available OpenStack provider APIs.

## Setup

The OpenStack provider supports several options for providing access to OpenStack credentials.  See the [OpenStack setup page]({{< relref "setup.md" >}}) for details.

## Example

{{< langchoose csharp >}}

```javascript
const os = require("@pulumi/openstack")

const instance = new os.compute.Instance("test", {
	flavorName: "s1-2",
	imageName: "Ubuntu 16.04",
});
```

```typescript
import * as os from "@pulumi/openstack";

const instance = new os.compute.Instance("test", {
	flavorName: "s1-2",
	imageName: "Ubuntu 16.04",
});
```

```python
from pulumi_openstack import compute

instance = compute.Instance("test",
  flavor_name='s1-2',
  image_name='Ubuntu 16.04'
)
```

```go
import "github.com/pulumi/pulumi-openstack/sdk/go/openstack/compute"

instance, _ := compute.NewInstance(ctx, "test", &compute.InstanceArgs{
  FlavorName: "s1-2",
  ImageName: "Ubuntu 16.04",
})
```

```csharp
using System.Threading.Tasks;
using Pulumi;
using Pulumi.OpenStack;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var instance = new OpenStack.Compute.Instance("test", new OpenStack.Compute.InstanceArgs
            {
                FlavorName = "s1-2",
                ImageName = "Ubuntu 16.04",
            });
        });
}
```

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/openstack`](https://www.npmjs.com/package/@pulumi/openstack)
* Python: [`pulumi-openstack`](https://pypi.org/project/pulumi-openstack/)
* Go: [`github.com/pulumi/pulumi-openstack/sdk/go/openstack`](https://github.com/pulumi/pulumi-openstack)

The OpenStack provider is open source and available in the [pulumi/pulumi-openstack](https://github.com/pulumi/pulumi-openstack) repo.
