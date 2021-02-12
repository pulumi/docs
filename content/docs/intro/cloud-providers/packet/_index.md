---
title: Equinix Metal
meta_desc: This page provides an overview of the Equinix Metal provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-packet
    weight: 2

aliases: ["/docs/reference/clouds/packet/"]
---

The Equinix Metal provider for Pulumi can be used to provision any of the cloud resources available in [Equinix Metal](https://metal.equinix.com/).
The Equinix Metal provider must be configured with credentials to deploy and update resources in Packet.

See the [full API documentation]({{< relref "/docs/reference/pkg/packet" >}}) for complete details of the available Equinix Metal provider APIs.

## Setup

The Equinix Metal provider supports several options for providing access to Equinix Metal credentials.  See [Equinix Metal setup page]({{< relref "/docs/intro/cloud-providers/packet/setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const equinixmetal = require("@pulumi/equinix-metal")

const equinixmetal = new equinixmetal.Project("my-project", {
  name: "DevelopmentEnvironment"
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as equinixmetal from "@pulumi/equinix-metal";

const project = new equinixmetal.Project("my-project", {
  name: "DevelopmentEnvironment"
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_equinix-metal as equinixmetal
project = equinixmetal.Project("my-project",
  name='DevelopmentEnvironment'
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
	packet "github.com/pulumi/pulumi-packet/sdk/v2/go/packet"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		project, err := packet.NewProject(ctx, "test", &packet.ProjectArgs{
			Name: pulumi.String("DevelopmentEnvironment"),
		})
		if err != nil {
			return err
		}

		return nil
	})
}
```


{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/packet`](https://github.com/pulumi/pulumi-equinix-metal)
* Python: [`pulumi-packet`](https://github.com/pulumi/pulumi-equinix-metal)
* Go: [`github.com/pulumi/pulumi-packet/sdk/go/packet`](https://github.com/pulumi/pulumi-equinix-metal)
* .NET: [`Pulumi.EquinixMetal`](https://github.com/pulumi/pulumi-equinix-metal)

PLEASE NOTE: The pulumi-packet provider has been renamed to pulumi-equinix-metal. The existing pulumi-packet provider will no longer have any new updates published to it.

The Equinix Metal provider is open source and available in the [pulumi/pulumi-equinix-metal](https://github.com/pulumi/pulumi-equinix-metal) repo.
