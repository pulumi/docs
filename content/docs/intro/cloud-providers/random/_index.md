---
title: Random
meta_desc: This page provides an overview of the Random Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-random
    weight: 2
---

The Random provider for Pulumi can be used to help introduce random values when dealing with Pulumi resources.

See the [full API documentation]({{< prelref "/docs/reference/pkg/nodejs/pulumi/random" >}}) for complete details of the available Random provider APIs.

## Example

{{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const random = require("@pulumi/random")

const username = new random.Pet("my-user-name");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as random from "@pulumi/random";

const username = new random.Pet("my-user-name");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_random as random

username = random.Pet("my-user-name")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  random "github.com/pulumi/pulumi-random/sdk/v2/go/random"
)

username, _ := random.NewPet(ctx, "my-user-name", &random.PetArgs{})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Random;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var username = new Pet("my-user-name", new PetArgs{});
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/random`](https://www.npmjs.com/package/@pulumi/random)
* Python: [`pulumi-random`](https://pypi.org/project/pulumi-random/)
* Go: [`github.com/pulumi/pulumi-random/sdk/go/random`](https://github.com/pulumi/pulumi-random)
* .NET: [`Pulumi.Random`](https://www.nuget.org/packages/Pulumi.Random)

The Random provider is open source and available in the [pulumi/pulumi-random](https://github.com/pulumi/pulumi-random) repo.
