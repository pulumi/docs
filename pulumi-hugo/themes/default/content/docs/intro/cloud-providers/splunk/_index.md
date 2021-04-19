---
title: Splunk
meta_desc: This page provides an overview of the Splunk Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-splunk
    weight: 2
---

<img src="/logos/tech/splunk.svg" align="right" class="h-16 px-8 pb-4">

The Splunk provider for Pulumi can be used to provision any of the cloud resources available in [Splunk](https://www.splunk.com/).
The Splunk provider must be configured with credentials to deploy and update resources in Splunk.

See the [full API documentation]({{< relref "/docs/reference/pkg/splunk" >}}) for complete details of the available Splunk provider APIs.

## Setup

The Splunk provider supports several options for providing access to Splunk credentials.  See the [Splunk setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const splunk = require("@pulumi/splunk")

const adminSamlGroup = new splunk.AdminSamlGroups("demo-ts-group", {
  roles: ["admin", "power"]
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as splunk from "@pulumi/splunk";

const adminSamlGroup = new splunk.AdminSamlGroups("demo-ts-group", {
  roles: ["admin", "power"]
});

```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_splunk as splunk

saml_group = splunk.AdminSamlGroups("demo-py-group", roles=[
  "admin",
  "power",
])
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi-splunk/sdk/go/splunk"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		group, err := splunk.NewAdminSamlGroups(ctx, "demo", &splunk.AdminSamlGroupsArgs{
            Roles: pulumi.StringArray{
                pulumi.String("admin"),
                pulumi.String("power"),
            }
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
using Pulumi.Splunk;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var group = new AdminSamlGroups("saml-group", new AdminSamlGroupsArgs
            {
                Roles =
                {
                  "admin",
                  "power",
                }
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/splunk`](https://www.npmjs.com/package/@pulumi/splunk)
* Python: [`pulumi-splunk`](https://pypi.org/project/pulumi-splunk/)
* Go: [`github.com/pulumi/pulumi-splunk/sdk/go/splunk`](https://github.com/pulumi/pulumi-splunk)
* .NET: [`Pulumi.Splunk`](https://www.nuget.org/packages/Pulumi.Splunk)

The Splunk provider is open source and available in the [pulumi/pulumi-splunk](https://github.com/pulumi/pulumi-splunk) repo.
