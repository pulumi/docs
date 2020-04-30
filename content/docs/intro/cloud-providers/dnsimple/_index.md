---
title: DNSimple
meta_desc: This page provides an overview of the DNSimple Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-dnsimple
    weight: 2
---

<img src="/logos/tech/dnsimple.svg" align="right" class="h-16 px-8 pb-4">

The DNSimple provider for Pulumi can be used to provision any of the cloud resources available in [DNSimple](https://dnsimple.com/).
The DNSimple provider must be configured with credentials to deploy and update resources in DNSimple.

See the [full API documentation]({{< prelref "/docs/reference/pkg/dnsimple" >}}) for complete details of the available DNSimple provider APIs.

## Setup

The DNSimple provider supports several options for providing access to DNSimple credentials.  See the [DNSimple setup page]({{< prelref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const dnsimple = require("@pulumi/dnsimple")

const record = new dnsimple.Record("test", {
  name: "test",
  domain: "mydomain.dev",
  type: dnsimple.RecordTypes.CNAME,
  value: "api.devflix.watch.herokudns.com"
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as dnsimple from "@pulumi/dnsimple";

const record = new dnsimple.Record("test", {
  name: "test",
  domain: "mydomain.dev",
  type: dnsimple.RecordTypes.CNAME,
  value: "api.devflix.watch.herokudns.com"
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_dnsimple as dnsimple

record = dnsimple.Record("test",
  name="test",
  domain="mydomain.dev",
  type="CNAME",
  value="api.devflix.watch.herokudns.com"
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  dnsimple "github.com/pulumi/pulumi-dnsimple/sdk/v2/go/dnsimple"
)

record, _ := dnsimple.NewRecord(ctx, "test", &dnsimple.RecordArgs{
  Name: "test",
  Domain: "mydomain.dev",
  Type: "CNAME",
  Value: "api.devflix.watch.herokudns.com",
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Dnsimple;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var record = new Record("test", new RecordArgs
            {
                Name = "test",
                Domain = "mydomain.dev",
                Type = "CNAME",
                Value = "api.devflix.watch.herokudns.com",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/dnsimple`](https://www.npmjs.com/package/@pulumi/dnsimple)
* Python: [`pulumi-dnsimple`](https://pypi.org/project/pulumi-dnsimple/)
* Go: [`github.com/pulumi/pulumi-dnsimple/sdk/go/dnsimple`](https://github.com/pulumi/pulumi-dnsimple)
* .NET: [`Pulumi.Dnsimple`](https://www.nuget.org/packages/Pulumi.Dnsimple)

The DNSimple provider is open source and available in the [pulumi/pulumi-dnsimple](https://github.com/pulumi/pulumi-dnsimple) repo.
