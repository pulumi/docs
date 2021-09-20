---
title: Akamai
meta_desc: This page provides an overview of the Akamai Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-akamai
    weight: 2
---

<img src="/logos/tech/akamai.svg" align="right" class="h-16 px-8 pb-4">

The Akamai provider for Pulumi can be used to provision any of the cloud resources available in [Akamai](https://www.akamai.com/).
The Akamai provider must be configured with credentials to deploy and update resources in Akamai.

See the [full API documentation]({{< relref "/docs/reference/pkg/akamai" >}}) for complete details of the available Akamai provider APIs.

## Setup

The Akamai provider supports several options for providing access to Akamai credentials.  See the [Akamai setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const akamai = require("@pulumi/akamai")

const contractId = akamai.getContract().then(x => x.id)
const groupId = akamai.getGroup().then(x => x.id)

const tsdomain = new akamai.properties.EdgeHostName("test", {
    contract: contractId,
    group: groupId,
    product: "prd_Fresca",
    edgeHostname: "test-js.mycompany.io",
    ipv4: true,
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as akamai from "@pulumi/akamai";

const contractId = akamai.getContract().then(x => x.id)
const groupId = akamai.getGroup().then(x => x.id)

const tsdomain = new akamai.properties.EdgeHostName("test", {
    contract: contractId,
    group: groupId,
    product: "prd_Fresca",
    edgeHostname: "test-ts.mycompany.io",
    ipv4: true,
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_akamai as akamai

contract_id = pulumi.Output.from_input(akamai.get_contract()).id
group_id = pulumi.Output.from_input(akamai.get_group()).id

pydomain = akamai.properties.EdgeHostName("test",
          contract=contract_id,
          group=group_id,
          product="prd_Fresca",
          edge_hostname="test-py.mycompany.io",
          ipv4="true")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi-akamai/sdk/v2/go/akamai"
	"github.com/pulumi/pulumi-akamai/sdk/v2/go/akam/properties"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		contract, err := akamai.GetContract(ctx)
		if err != nil {
			return err
		}

		group, err := akamai.GetGroup(ctx)
		if err != nil {
			return err
		}

		user, err := properties.NewEdgeHostName(ctx, "demo", &properties.EdgeHostNameArgs{
			Contract:     pulumi.String(contract.Id),
			Group:        pulumi.String(group.Id),
			Product:      pulumi.String("prd_Fresca"),
			EdgeHostname: pulumi.String("test-go.mycompany.io"),
			Ipv4:         pulumi.Bool(true),
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
using Pulumi.Akamai;
using Properties = Pulumi.Akamai.Properties;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {

            var group = Output.Create(GetGroup.InvokeAsync());
            var contract = Output.Create(GetContract.InvokeAsync());

            var hostname = new Properties.EdgeHostName("demo", new Properties.EdgeHostNameArgs
            {
                Contract = contract.Id,
                Group = group.Id,
                Product = "prd_Fresca",
                EdgeHostName = "test-cs.mycompany.io",
                Ipv4 = true,
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/akamai`](https://www.npmjs.com/package/@pulumi/akamai)
* Python: [`pulumi-akamai`](https://pypi.org/project/pulumi-akamai/)
* Go: [`github.com/pulumi/pulumi-akamai/sdk/v2/go/akamai`](https://github.com/pulumi/pulumi-akamai)
* .NET: [`Pulumi.Akamai`](https://www.nuget.org/packages/Pulumi.Akamai)

The Akamai provider is open source and available in the [pulumi/pulumi-akamai](https://github.com/pulumi/pulumi-akamai) repo.
