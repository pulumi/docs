---
title: CloudAMQP
meta_desc: This page provides an overview of the CloudAMQP Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-cloudamqp
    weight: 5
---

<img src="/logos/tech/cloudamqp.png" align="right" class="h-16 px-8 pb-4">

The CloudAMQP provider for Pulumi can be used to provision any of the cloud resources available in [CloudAMQP](https://www.cloudamqp.com/).
The CloudAMQP provider must be configured with credentials to deploy and update resources in CloudAMQP.

## Setup

The CloudAMQP provider supports several options for providing access to CloudAMQP credentials.  See the [CloudAMQP setup page]({{< relref "setup" >}}) for details.

## Example

{{< langchoose csharp >}}

```javascript
const cloudamqp = require("@pulumi/cloudamqp")

const instance = new cloudamqp.Instance("demo-instance", {
    plan: "lemur",
    region: "amazon-web-services::us-west-2"
});
```

```typescript
import * as cloudamqp from "@pulumi/cloudamqp";

const instance = new cloudamqp.Instance("demo-instance", {
    plan: "lemur",
    region: "amazon-web-services::us-west-2"
});
```

```python
import pulumi_cloudamqp as cloudamqp

instance = cloudamqp.Instance("demo-instance",
    plan="lemur",
    region="amazon-web-services::us-west-2"
)
```

```go
import (
  cloudamqp "github.com/pulumi/pulumi-cloudamqp/sdk/go/cloudamqp"
)

instance, _ := cloudamqp.NewInstance(ctx, "demo-instance", &cloudamqp.InstanceArgs{
	Plan: "lemur",
	Region: "amazon-web-services::us-west-2"
})
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Cloudamqp;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var instance = new Instance("demo-instance", new InstanceArgs
            {
                Plan = "lemur",
                Region = "amazon-web-services::us-west-2",
            });
        });
}
```

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/cloudamqp`](https://www.npmjs.com/package/@pulumi/cloudamqp)
* Python: [`pulumi-cloudamqp`](https://pypi.org/project/pulumi-cloudamqp/)
* Go: [`github.com/pulumi/pulumi-cloudamqp/sdk/go/cloudamqp`](https://github.com/pulumi/pulumi-cloudamqp)
* .NET: [`Pulumi.Cloudamqp`](https://www.nuget.org/packages/Pulumi.Cloudamqp)

The Fastly provider is open source and available in the [pulumi/pulumi-cloudamqp](https://github.com/pulumi/pulumi-cloudamqp) repo.
