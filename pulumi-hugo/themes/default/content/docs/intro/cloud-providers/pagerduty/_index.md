---
title: PagerDuty
meta_desc: This page provides an overview of the PagerDuty Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-pagerduty
    weight: 2
---

<img src="/logos/tech/pagerduty.svg" align="right" class="h-16 px-8 pb-4">

The PagerDuty provider for Pulumi can be used to provision any of the cloud resources available in [PagerDuty](https://www.pagerduty.com/).
The PagerDuty provider must be configured with credentials to deploy and update resources in PagerDuty.

See the [full API documentation]({{< relref "/docs/reference/pkg/pagerduty" >}}) for complete details of the available PagerDuty provider APIs.

## Setup

The PagerDuty provider supports several options for providing access to PagerDuty credentials.  See the [PagerDuty setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const pagerduty = require("@pulumi/pagerduty")

const demoTeam = new pagerduty.Team("demo-team", {
    description: "Demo team generated from examples",
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pagerduty from "@pulumi/pagerduty";

const demoTeam = new pagerduty.Team("demo-team", {
    description: "Demo team generated from examples",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_pagerduty as pagerduty

demo_team = pagerduty.Team("demo-team",
  description="Demo team generated from examples")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	pagerduty "github.com/pulumi/pulumi-pagerduty/sdk/v2/go/pagerduty"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		demoTeam, err := pagerduty.NewTeam(ctx, "demo-team", &pagerduty.TeamArgs{
			Description: pulumi.String("Demo team generated from examples"),
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
using Pulumi.Pagerduty;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var demoTeam = new Team("demo-team", new TeamArgs
            {
                Description = "Demo team generated from examples",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/pagerduty`](https://www.npmjs.com/package/@pulumi/pagerduty)
* Python: [`pulumi-pagerduty`](https://pypi.org/project/pulumi-pagerduty/)
* Go: [`github.com/pulumi/pulumi-pagerduty/sdk/v2/go/pagerduty`](https://github.com/pulumi/pulumi-pagerduty)
* .NET: [`Pulumi.Pagerduty`](https://www.nuget.org/packages/Pulumi.Pagerduty)

The PagerDuty provider is open source and available in the [pulumi/pulumi-pagerduty](https://github.com/pulumi/pulumi-pagerduty) repo.
