---
title: Kong
meta_desc: This page provides an overview of the Kong Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-kong
    weight: 2
---

<img src="/logos/tech/kong.svg" align="right" class="h-16 px-8 pb-4">

The Kong provider for Pulumi can be used to provision any of the cloud resources available in [Kong](https://konghq.com/kong).
The Kong provider must be configured with credentials to deploy and update resources in Mailgun.

See the [full API documentation]({{< relref "/docs/reference/pkg/kong" >}}) for complete details of the available Kong provider APIs.

## Setup

The Kong provider supports several options for providing access to Kong credentials.  See the [Kong setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const kong = require("@pulumi/kong")

const consumer = new kong.Consumer("my-consumer", {
  username: "my-username-1",
  customId: "123"
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as kong from "@pulumi/kong";

const consumer = new kong.Consumer("my-consumer", {
  username: "my-username-1",
  customId: "123"
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_kong as kong

consumer = kong.Consumer("my-consumer",
  username="my-username-1",
  custom_id="123")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	kong "github.com/pulumi/pulumi-kong/sdk/v4/go/kong"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		consumer, err := kong.NewConsumer(ctx, "test-route", &kong.ConsumerArgs{
            CustomId: pulumi.String("123"),
            Username: pulumi.String("my-username-1"),
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
using Pulumi.Kong;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var consumer = new Kong.Consumer("consumer", new Kong.ConsumerArgs
            {
                CustomId = "123",
                Username = "my-username-1",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/kong`](https://www.npmjs.com/package/@pulumi/kong)
* Python: [`pulumi-kong`](https://pypi.org/project/pulumi-kong/)
* Go: [`github.com/pulumi/pulumi-kong/sdk/v4/go/kong`](https://github.com/pulumi/pulumi-kong)
* .NET: [`Pulumi.Kong`](https://www.nuget.org/packages/Pulumi.Kong)

The Kong provider is open source and available in the [pulumi/pulumi-kong](https://github.com/pulumi/pulumi-kong) repo.
