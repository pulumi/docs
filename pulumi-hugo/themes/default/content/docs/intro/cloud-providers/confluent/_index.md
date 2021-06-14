---
title: Confluent Cloud
meta_desc: This page provides an overview of the Confluent Cloud Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-confluent
    weight: 2
---

<img src="/logos/tech/confluent.svg" align="right" class="h-16 px-8 pb-4">

The Confluent Cloud provider for Pulumi can be used to provision any of the cloud resources available in [Confluent Cloud](https://confluent.cloud/).
The Confluent Cloud provider must be configured with credentials to deploy and update resources in Confluent Cloud.

See the [full API documentation]({{< relref "/docs/reference/pkg/confluent" >}}) for complete details of the available Confluent Cloud provider APIs.

## Setup

The Confluent Cloud provider supports several options for providing access to Confluent Cloud credentials.  See the [Confluent Cloud setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const ccloud = require("@pulumi/confluent")

const env = new ccloud.ConfluentEnvironment("ts-environment");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as confluent from "@pulumi/confluent";

const env = new ccloud.ConfluentEnvironment("ts-environment");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_confluent as confluent

environment = ccloud.ConfluentEnvironment("py-env")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
  "github.com/pulumi/pulumi-confluent/sdk/go/confluent"
  "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
  pulumi.Run(func(ctx *pulumi.Context) error {

    env, err := confluent.NewConfluentEnvironment(ctx, "py-env", nil)
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
using Pulumi.Confluent;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var environment = new CCloud.ConfluentEnvironment("csharp-env");
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/confluent`](https://www.npmjs.com/package/@pulumi/confluent)
* Python: [`pulumi-confluent`](https://pypi.org/project/pulumi-confluent/)
* Go: [`github.com/pulumi/pulumi-confluent/sdk/go/confluent`](https://github.com/pulumi/pulumi-confluent)
* .NET: [`Pulumi.Confluent`](https://www.nuget.org/packages/Pulumi.Confluent)

The Confluent Cloud provider is open source and available in the [pulumi/pulumi-confluent](https://github.com/pulumi/pulumi-confluent) repo.
