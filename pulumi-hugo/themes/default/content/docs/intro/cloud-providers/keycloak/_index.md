---
title: Keycloak
meta_desc: This page provides an overview of the Keycloak Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-keycloak
    weight: 2
---

<img src="/logos/tech/keycloak.svg" align="right" class="h-16 px-8 pb-4">

The Keycloak provider for Pulumi can be used to provision any of the cloud resources available via [Keycloak](https://rancher.com/).
The Keycloak provider must be configured with credentials to deploy and update resources for Rancher.

See the [full API documentation]({{< relref "/docs/reference/pkg/keycloak" >}}) for complete details of the available Keycloak provider APIs.

## Setup

The Keycloak provider supports several options for providing access to Keycloak credentials.  See the [Keycloak setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const keycloak = require("@pulumi/keycloak")

const realm = new keycloak.Realm("new-typescript-realm", {
  realm: "my-example-typescript-realm"
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as keycloak from "@pulumi/keycloak";

const realm = new keycloak.Realm("new-typescript-realm", {
  realm: "my-example-typescript-realm"
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_keycloak as keycloak

realm = keycloak.Realm("new-python-realm",
                       realm="my-example-python-realm"
                       )
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	keycloak "github.com/pulumi/pulumi-keycloak/sdk/v4/go/keycloak"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        realm, err := keycloak.NewRealm(ctx, "new-go-realm", &keycloak.RealmArgs{
            Realm: pulumi.String("my-example-go-realm"),
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
using Pulumi.Keycloak;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var realm = new Keycloak.Realm("new-csharp-realm", new Keycloak.RealmArgs
            {
                RealmName = "my-example-csharp-realm",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/keycloak`](https://www.npmjs.com/package/@pulumi/keycloak)
* Python: [`pulumi-keycloak`](https://pypi.org/project/pulumi-keycloak/)
* Go: [`github.com/pulumi/pulumi-keycloak/sdk/v4/go/keycloak`](https://github.com/pulumi/pulumi-keycloak)
* .NET: [`Pulumi.Keycloak`](https://www.nuget.org/packages/Pulumi.Keycloak)

The Keycloak provider is open source and available in the [pulumi/pulumi-keycloak](https://github.com/pulumi/pulumi-keycloak) repo.
