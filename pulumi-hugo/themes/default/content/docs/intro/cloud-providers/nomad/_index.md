---
title: HashiCorp Nomad
meta_desc: This page provides an overview of the HashiCorp Nomad Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-nomad
    weight: 2
---

<img src="/logos/tech/nomad.svg" align="right" class="h-16 px-8 pb-4">

The HashiCorp Nomad provider for Pulumi can be used to provision any of the resources available in [Nomad](https://www.nomadproject.io/).

See the [full API documentation]({{< relref "/docs/reference/pkg/nomad" >}}) for complete details of the available Nomad provider APIs.

## Setup

The Nomad provider supports several options for interacting with HashiCorp Nomad.  See the [Nomad setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const nomad = require("@pulumi/nomad")

const ns = new nomad.Namespace("test-ns-ts");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as nomad from "@pulumi/nomad";

const ns = new nomad.Namespace("test-ns-ts");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_nomad as nomad

ns = nomad.Namespace("test-ns-py")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	nomad "github.com/pulumi/pulumi-nomad/sdk/go/nomad"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        _, err := nomad.NewNamespace(ctx, "test-ns-go", nil)
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
using Pulumi.Nomad;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var ns = new Nomad.Namespace("test-ns-cs", new Nomad.NamespaceArgs{});
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/nomad`](https://www.npmjs.com/package/@pulumi/nomad)
* Python: [`pulumi-nomad`](https://pypi.org/project/pulumi-nomad/)
* Go: [`github.com/pulumi/pulumi-nomad/sdk/go/nomad`](https://github.com/pulumi/pulumi-nomad)
* .NET: [`Pulumi.Nomad`](https://www.nuget.org/packages/Pulumi.Nomad)

The HashiCorp Nomad provider is open source and available in the [pulumi/pulumi-nomad](https://github.com/pulumi/pulumi-nomad) repo.
