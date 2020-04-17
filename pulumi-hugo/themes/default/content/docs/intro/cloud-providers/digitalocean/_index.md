---
title: DigitalOcean
meta_desc: This page provides an overview of the DigitalOcean Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-digitalocean
    weight: 2

aliases: ["/docs/reference/clouds/digitalocean/"]
---

<img src="/logos/tech/digitalocean.svg" align="right" class="h-16 px-8 pb-4">

The DigitalOcean provider for Pulumi can be used to provision any of the cloud resources available in [DigitalOcean](https://www.digitalocean.com/).
The DigitalOcean provider must be configured with credentials to deploy and update resources in a DigitalOcean cloud.

See the [full API documentation]({{< relref "/docs/reference/pkg/digitalocean" >}}) for complete details of the available DigitalOcean provider APIs.

## Setup

The DigitalOcean provider supports several options for providing access to DigitalOcean credentials.  See the [DigitalOcean setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const do = require("@pulumi/digitalocean")

const domain = new do.Domain("test", {
  name: "mydomain.com",
  ipAddress: "192.168.10.10",
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as do from "@pulumi/digitalocean";

const instance = new do.Domain("test", {
  name: "mydomain.com",
  ipAddress: "192.168.10.10",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_digitalocean as do

instance = do.Domain("test",
  name='mydomain.com',
  ip_address='192.168.10.10'
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  do "github.com/pulumi/pulumi-digitalocean/sdk/go/digitalocean"
)

domain, _ := do.NewDomain(ctx, "test", &do.DomainArgs{
  Name: "mydomain.com",
  IpAddress: "192.168.10.10",
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.DigitalOcean;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var instance = new DigitalOcean.Domain("test", new DigitalOcean.DomainArgs
            {
                Name = "mydomain.com",
                IpAddress = "192.168.10.10",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/digitalocean`](https://www.npmjs.com/package/@pulumi/digitalocean)
* Python: [`pulumi-digitalocean`](https://pypi.org/project/pulumi-digitalocean/)
* Go: [`github.com/pulumi/pulumi-digitalocean/sdk/go/digitalocean`](https://github.com/pulumi/pulumi-digitalocean)
* .NET: [`Pulumi.DigitalOcean`](https://www.nuget.org/packages/Pulumi.DigitalOcean)

The DigitalOcean provider is open source and available in the [pulumi/pulumi-digitalocean](https://github.com/pulumi/pulumi-digitalocean) repo.
