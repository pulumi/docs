---
title: Spotinst
meta_desc: This page provides an overview of the Spotinst Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-spotinst
    weight: 2
---

<img src="/logos/tech/spotinst.png" align="right" class="h-16 px-8 pb-4">

The Spotinst provider for Pulumi can be used to provision any of the resources available in [Spotinst](https://spotinst.com/).

See the [full API documentation]({{< prelref "/docs/reference/pkg/spotinst" >}}) for complete details of the available Spotinst provider APIs.

## Setup

The Spotinst provider supports several options for interacting with Spotinst.  See the [Spotinst setup page]({{< prelref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const spotinst = require("@pulumi/spotinst")

const deployment = new spotinst.multai.Deployment("myDeployment", {});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as spotinst from "@pulumi/spotinst";

const deployment = new spotinst.multai.Deployment("myDeployment");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_spotinst as spotinst

deployment = spotinst.multai.Deployment("my_deployment")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  multai "github.com/pulumi/pulumi-spotinst/sdk/v2/go/spotinst/multai"
)

deployment, _ := multai.NewDeployment(ctx, "example", &multai.DeploymentArgs{})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.SpotInst.Multai;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var deployment = new Multai.Deployment("example", new Multai.DeploymentArgs{});
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/spotinst`](https://www.npmjs.com/package/@pulumi/spotinst)
* Python: [`pulumi-spotinst`](https://pypi.org/project/pulumi-spotinst/)
* Go: [`github.com/pulumi/pulumi-spotinst/sdk/go/spotinst`](https://github.com/pulumi/pulumi-spotinst)
* .NET: [`Pulumi.Spotinst`](https://www.nuget.org/packages/Pulumi.Spotinst)

The Spotinst provider is open source and available in the [pulumi/pulumi-spotinst](https://github.com/pulumi/pulumi-spotinst) repo.
