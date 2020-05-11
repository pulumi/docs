---
title: Datadog
meta_desc: This page provides an overview of the Datadog Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-datadog
    weight: 2
---

<img src="/logos/tech/datadog.svg" align="right" class="h-16 px-8 pb-4">

The Datadog provider for Pulumi can be used to provision any of the cloud resources available in [Datadog](https://datadoghq.com/).
The Datadog provider must be configured with credentials to deploy and update resources in Datadog.

See the [full API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/datadog" >}}) for complete details of the available Datadog provider APIs.

## Setup

The Datadog provider supports several options for providing access to Datadog credentials.  See the [Datadog setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const datadog = require("@pulumi/datadog")

const user = new datadog.User("my-user", {
  email: "new@example.com",
  handle: "new@example.com",
  name: "New User",
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as datadog from "@pulumi/datadog";

const user = new datadog.User("my-policy", {
  email: "new@example.com",
  handle: "new@example.com",
  name: "New User",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_datadog as datadog

user = datadog.User("my-policy",
  email="new@example.com",
  handle="new@example.com",
  name="New User",
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  datadog "github.com/pulumi/pulumi-datadog/sdk/v2/go/datadog"
)

user, _ := datadog.NewUser(ctx, "my-user", &datadog.UserArgs{
 Email: "new@example.com",
 Handle: "new@example.com",
 Name: "New User",
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Datadog;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var user = new User("my-user", new UserArgs
            {
                Name = "New User",
                Email = "new@example.com",
                Handle = "new@example.com",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/datadog`](https://www.npmjs.com/package/@pulumi/datadog)
* Python: [`pulumi-datadog`](https://pypi.org/project/pulumi-datadog/)
* Go: [`github.com/pulumi/pulumi-datadog/sdk/go/datadog`](https://github.com/pulumi/pulumi-datadog)
* .NET: [`Pulumi.Datadog`](https://www.nuget.org/packages/Pulumi.Datadog)

The Datadog provider is open source and available in the [pulumi/pulumi-datadog](https://github.com/pulumi/pulumi-datadog) repo.
