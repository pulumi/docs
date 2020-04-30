---
title: TLS
meta_desc: This page provides an overview of the TLS Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-tls
    weight: 2
---

The TLS provider for Pulumi can be used to help to create TLS keys and certitifcate for use with Pulumi resources.

See the [full API documentation]({{< prelref "/docs/reference/pkg/tls" >}}) for complete details of the available TLS provider APIs.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const tls = require("@pulumi/tls")

const key = new tls.PrivateKey("my-private-key", {
    algorithm: "ECDSA",
    ecdsaCurve: "P384",
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as tls from "@pulumi/tls";

const key = new tls.PrivateKey("my-private-key", {
    algorithm: "ECDSA",
    ecdsaCurve: "P384",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_tls as tls

key = tls.PrivateKey("my-private-key",
  algorithm="ECDSA",
  ecdsa_curve="P384"
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  tls "github.com/pulumi/pulumi-tls/sdk/v2/go/tls"
)

key, _ := tls.NewPrivateKey(ctx, "my-private-key", &tls.PrivateKeyArgs{
  Algorithm: "ECDSA",
  EcdsaCurve: "P384",
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Tls;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var key = new PrivateKey("my-private-key", new PrivateKeyArgs{
                Algorithm = "ECDSA",
                EcdsaCurve = "P384",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/tls`](https://www.npmjs.com/package/@pulumi/tls)
* Python: [`pulumi-tls`](https://pypi.org/project/pulumi-tls/)
* Go: [`github.com/pulumi/pulumi-tls/sdk/go/tls`](https://github.com/pulumi/pulumi-tls)
* .NET: [`Pulumi.Tls`](https://www.nuget.org/packages/Pulumi.Tls)

The TLS provider is open source and available in the [pulumi/pulumi-tls](https://github.com/pulumi/pulumi-tls) repo.
