---
title: Rancher2
meta_desc: This page provides an overview of the Rancher2 Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-rancher2
    weight: 2
---

<img src="/logos/tech/rancher.svg" align="right" class="h-16 px-8 pb-4">

The Rancher2 provider for Pulumi can be used to provision any of the cloud resources available via [Rancher](https://rancher.com/).
The Rancher2 provider must be configured with credentials to deploy and update resources for Rancher.

See the [full API documentation]({{< relref "/docs/reference/pkg/rancher2" >}}) for complete details of the available Rancher2 provider APIs.

## Setup

The Rancher2 provider supports several options for providing access to Rancher credentials.  See the [Rancher2 setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const rancher2 = require("@pulumi/rancher2")

const myUser = new rancher2.User("my-user", {
  name: "Foo user",
  username: "foo",
  password: "initialPassw0rd",
  enabled: true,
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as rancher2 from "@pulumi/rancher2";

const myUser = new rancher2.User("my-user", {
  name: "Foo user",
  username: "foo",
  password: "initialPassw0rd",
  enabled: true,
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_rancher2 as rancher2

user = rancher2.User("my-user",
  name="Foo user",
  username="foo",
  password="initialPassw0rd",
  enabled=true
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  rancher2 "github.com/pulumi/pulumi-rancher2/sdk/v2/go/rancher2"
)

user, _ := rancher2.NewUser(ctx, "my-user", &rancher2.UserArgs{
  Name:     "Foo user",
  Username: "foo",
  Password: "initialPassw0rd",
  Enabled:  true,
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Rancher2;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var user = new User("my-user", new UserArgs
            {
                Name = "Foo user",
                Username = "foo",
                Password = "initialPassw0rd",
                Enabled = true,
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/rancher2`](https://www.npmjs.com/package/@pulumi/rancher2)
* Python: [`pulumi-rancher2`](https://pypi.org/project/pulumi-rancher2/)
* Go: [`github.com/pulumi/pulumi-rancher2/sdk/go/rancher2`](https://github.com/pulumi/pulumi-rancher2)
* .NET: [`Pulumi.Rancher2`](https://www.nuget.org/packages/Pulumi.Rancher2)

The Rancher2 provider is open source and available in the [pulumi/pulumi-rancher2](https://github.com/pulumi/pulumi-rancher2) repo.
