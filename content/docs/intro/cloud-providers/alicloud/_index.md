---
title: Alibaba Cloud
meta_desc: This page provides an overview of the Alibaba Cloud Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-alicloud
    weight: 2
---

<img src="/logos/tech/alicloud.png" align="right" class="h-16 px-8 pb-4">

The Alibaba Cloud provider for Pulumi can be used to provision any of the cloud resources available in [Alibaba Cloud](https://www.alibabacloud.com/).
The Alibaba Cloud provider must be configured with credentials to deploy and update resources in Alibaba Cloud.

## Setup

The Alibaba Cloud provider supports several options for providing access to Alibaba Cloud credentials.  See the [Alibaba Cloud setup page]({{< relref "setup" >}}) for details.

## Example

{{< langchoose csharp >}}

```javascript
const alicloud = require("@pulumi/alicloud")

const vpc = new alicloud.vpc.Network("my-vpc", {
    cidrBlock: "10.0.0.0/16",
});
```

```typescript
import * as alicloud from "@pulumi/alicloud";

const vpc = new alicloud.vpc.Network("my-vpc", {
    cidrBlock: "10.0.0.0/16",
});
```

```python
import pulumi_alicloud as alicloud

vpc = alicloud.vpc.Network("my-vpc",
    cidr_block="10.0.0.0/16"
)
```

```go
import (
  vpc "github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc"
)

vpc, _ := vpc.NewVpc(ctx, "demo-instance", &vpc.VpcArgs{
	CidrBlock: "10.0.0.0/16",
})
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Alicloud.Vpc;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var vpc = new Vpc("demo-instance", new VpcArgs
            {
                CidrBlock = "10.0.0.0/16"
            });
        });
}
```

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/alicloud`](https://www.npmjs.com/package/@pulumi/alicloud)
* Python: [`pulumi-alicloud`](https://pypi.org/project/pulumi-alicloud/)
* Go: [`github.com/pulumi/pulumi-alicloud/sdk/go/alicloud`](https://github.com/pulumi/pulumi-alicloud)
* .NET: [`Pulumi.Alicloud`](https://www.nuget.org/packages/Pulumi.Alicloud)

The Alibaba Cloud provider is open source and available in the [pulumi/pulumi-alicloud](https://github.com/pulumi/pulumi-alicloud) repo.
