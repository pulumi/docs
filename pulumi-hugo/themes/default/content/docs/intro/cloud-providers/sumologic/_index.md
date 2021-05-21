---
title: SumoLogic
meta_desc: This page provides an overview of the SumoLogic Provider for Pulumi.
menu:
intro:
parent: cloud-providers
identifier: clouds-sumologic
weight: 2
---

<img src="/logos/tech/sumologic.svg" align="right" class="h-16 px-8 pb-4">

The SumoLogic provider for Pulumi can be used to provision any of the cloud resources available in [SumoLogic](https://www.sumologic.com/).
The SumoLogic provider must be configured with credentials to deploy and update resources in SumoLogic.

See the [full API documentation]({{< relref "/docs/reference/pkg/sumologic" >}}) for complete details of the available SumoLogic provider APIs.

## Setup

The SumoLogic provider supports several options for providing access to SumoLogic credentials.  See the [SumoLogic setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const sumologic = require("@pulumi/sumologic")

const folder = new sumologic.Folder("folder", {
  description: "A test folder",
  parentId: "<personal folder id>",
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as sumologic from "@pulumi/sumologic";

const folder = new sumologic.Folder("folder", {
  description: "A test folder",
  parentId: "<personal folder id>",
});

```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_sumologic as sumologic

folder = sumologic.Folder("folder",
                          description="A test folder",
                          parent_id="<personal folder id>")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi-sumologic/sdk/go/sumologic"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := sumologic.NewFolder(ctx, "folder", &sumologic.FolderArgs{
			Description: pulumi.String("A test folder"),
            ParentId:    pulumi.String("<personal folder id>"),
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
using Pulumi.SumoLogic;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var folder = new SumoLogic.Folder("folder", new SumoLogic.FolderArgs
            {
                Description = "A test folder",
                 ParentId = "<personal folder id>",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/sumologic`](https://www.npmjs.com/package/@pulumi/sumologic)
* Python: [`pulumi-sumologic`](https://pypi.org/project/pulumi-sumologic/)
* Go: [`github.com/pulumi/pulumi-sumologic/sdk/go/sumologic`](https://github.com/pulumi/pulumi-sumologic)
* .NET: [`Pulumi.SumoLogic`](https://www.nuget.org/packages/Pulumi.SumoLogic)

The SumoLogic provider is open source and available in the [pulumi/pulumi-sumologic](https://github.com/pulumi/pulumi-sumologic) repo.
