---
title: Minio
meta_desc: This page provides an overview of the Minio Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-minio
    weight: 2
---

<img src="/logos/tech/minio.svg" align="right" class="h-16 px-8 pb-4">

The Minio provider for Pulumi can be used to provision any of the cloud resources available in [Minio](https://min.io/).
The Minio provider must be configured with credentials to deploy and update resources in Minio.

See the [full API documentation]({{< relref "/docs/reference/pkg/minio" >}}) for complete details of the available Minio provider APIs.

## Setup

The Minio provider supports several options for providing access to Minio credentials.  See the [Minio setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const minio = require("@pulumi/minio")

const user = new minio.IamUser("ts-user");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as minio from "@pulumi/minio";

const user = new minio.IamUser("ts-user")
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_minio as minio

user = minio.IamUser("python-user")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    minio "github.com/pulumi/pulumi-minio/sdk/go/minio"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		user, err := minio.NewIamUser(ctx, "go-user", nil)
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
using Pulumi.Minio;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var user = new Minio.IamUser("csharp-user");
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/minio`](https://www.npmjs.com/package/@pulumi/minio)
* Python: [`pulumi-minio`](https://pypi.org/project/pulumi-minio/)
* Go: [`github.com/pulumi/pulumi-minio/sdk/go/minio`](https://github.com/pulumi/pulumi-minio)
* .NET: [`Pulumi.Minio`](https://www.nuget.org/packages/Pulumi.Minio)

The Minio provider is open source and available in the [pulumi/pulumi-minio](https://github.com/pulumi/pulumi-minio) repo.
