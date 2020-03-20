---
title: SignalFx
meta_desc: This page provides an overview of the SignalFx Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-signalfx
    weight: 2
---

<img src="/logos/tech/signalfx.png" align="right" class="h-16 px-8 pb-4">

The SignalFx provider for Pulumi can be used to provision any of the cloud resources available in [SignalFx](https://datadoghq.com/).
The SignalFx provider must be configured with credentials to deploy and update resources in SignalFx.

See the [full API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/signalfx" >}}) for complete details of the available SignalFx provider APIs.

## Setup

The SignalFx provider supports several options for providing access to SignalFx credentials.  See the [SignalFx setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const signalfx = require("@pulumi/signalfx")

const group = new signalfx.DashboardGroup("my-group", {
  description: "my demo dashboard group"
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as signalfx from "@pulumi/signalfx";

const group = new signalfx.DashboardGroup("my-group", {
  description: "my demo dashboard group"
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_signalfx as signalfx

group = signalfx.DashboardGroup("my-group",
  description="my demo dashboard group"
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  signalfx "github.com/pulumi/pulumi-signalfx/sdk/go/signalfx"
)

group, _ := signalfx.NewDashboardGroup(ctx, "my-group", &signalfx.DashboardGroupArgs{
  Description: "my demo dashboard group"
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Signalfx;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var group = new DashboardGroup("my-group", new DashboardGroupArgs
            {
                Description = "my demo dashboard group"
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/signalfx`](https://www.npmjs.com/package/@pulumi/signalfx)
* Python: [`pulumi-signalfx`](https://pypi.org/project/pulumi-signalfx/)
* Go: [`github.com/pulumi/pulumi-signalfx/sdk/go/signalfx`](https://github.com/pulumi/pulumi-signalfx)
* .NET: [`Pulumi.Signalfx`](https://www.nuget.org/packages/Pulumi.Signalfx)

The SignalFx provider is open source and available in the [pulumi/pulumi-signalfx](https://github.com/pulumi/pulumi-signalfx) repo.
