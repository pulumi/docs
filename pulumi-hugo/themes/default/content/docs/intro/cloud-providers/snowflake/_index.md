---
title: Snowflake
meta_desc: This page provides an overview of the Snowflake Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-snowflake
    weight: 2
---

<img src="/logos/tech/snowflake.png" align="right" class="h-16 px-8 pb-4">

The Snowflake provider for Pulumi can be used to provision any of the cloud resources available in [Snowflake](https://www.snowflake.com/).
The Snowflake provider must be configured with credentials to deploy and update resources in Snowflake.

## Setup

The Snowflake provider supports several options for providing access to Snowflake credentials.  See the [Snowflake setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const snowflake = require("@pulumi/snowflake")

const user = new snowflake.User("ts-user")
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as snowflake from "@pulumi/snowflake";

const user = new snowflake.User("ts-user")
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_snowflake as snowflake

user = snowflake.User("py-user")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    snowflake "github.com/pulumi/pulumi-snowflake/sdk/go/snowflake"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        user, err := snowflake.NewUser(ctx, "go-user", nil)
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
using Pulumi.Snowflake;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var user = new Snowflake.User("cs-user", new Snowflake.UserArgs{});
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/snowflake`](https://www.npmjs.com/package/@pulumi/snowflake)
* Python: [`pulumi-snowflake`](https://pypi.org/project/pulumi-snowflake/)
* Go: [`github.com/pulumi/pulumi-snowflake/sdk/go/snowflake`](https://github.com/pulumi/pulumi-snowflake)
* .NET: [`Pulumi.Snowflake`](https://www.nuget.org/packages/Pulumi.Snowflake)

The Snowflake provider is open source and available in the [pulumi/pulumi-snowflake](https://github.com/pulumi/pulumi-snowflake) repo.
