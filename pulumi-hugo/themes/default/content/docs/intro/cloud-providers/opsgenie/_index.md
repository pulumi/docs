---
title: Opsgenie
meta_desc: This page provides an overview of the Opsgenie Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-opsgenie
    weight: 2
---

<img src="/logos/tech/opsgenie.svg" align="right" class="h-16 px-8 pb-4">

The Opsgenie provider for Pulumi can be used to provision any of the resources available for Opsgenie.
The Opsgenie provider must be configured with credentials to deploy and update resources in Opsgenie.

See the [full API documentation]({{< relref "/docs/reference/pkg/opsgenie" >}}) for complete details of the available Opsgenie provider APIs.

## Setup

The Opsgenie provider supports several options for providing access to Opsgenie credentials.  See the [Opsgenie setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const opsgenie = require("@pulumi/opsgenie")

const team = new opsgenie.Team('test');
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as opsgenie from "@pulumi/opsgenie";

const team = new opsgenie.Team('test');
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_opsgenie as opsgenie

team = opsgenie.Team("test")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi-opsgenie/sdk/go/opsgenie"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		team, err := opsgenie.NewTeam(ctx, "my-team", &opsgenie.TeamArgs{})
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
using Pulumi.Opsgenie;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var team = new Team("my-team", new TeamArgs{});
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/opsgenie`](https://www.npmjs.com/package/@pulumi/opsgenie)
* Python: [`pulumi-opsgenie`](https://pypi.org/project/pulumi-opsgenie/)
* Go: [`github.com/pulumi/pulumi-opsgenie/sdk/go/opsgenie`](https://github.com/pulumi/pulumi-opsgenie)
* .NET: [`Pulumi.Opsgenie`](https://www.nuget.org/packages/Pulumi.Opsgenie)

The Opsgenie provider is open source and available in the [pulumi/pulumi-opsgenie](https://github.com/pulumi/pulumi-opsgenie) repo.
