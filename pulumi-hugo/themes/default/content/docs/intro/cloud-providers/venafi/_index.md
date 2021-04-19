---
title: Venafi
meta_desc: This page provides an overview of the Venafi Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-venafi
    weight: 2
---

<img src="/logos/tech/venafi.svg" align="right" class="h-16 px-8 pb-4">

The Venafi provider for Pulumi can be used to provision cloud resources available in [Venafi](https://www.venafi.com/).
The Venafi provider must be configured with credentials to deploy and update resources in Venafi.

See the [full API documentation]({{< relref "/docs/reference/pkg/venafi" >}}) for complete details of the available Venafi provider APIs.

## Setup

The Venafi provider supports several options for providing access to Venafi credentials.  See the [Venafi setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const venafi = require("@pulumi/venafi")

const webserver = new venafi.Certificate("webserver", {
    algorithm: "RSA",
    commonName: "web.venafi.example",
    customFields: {
        "Cost Center": "AB1234",
        Environment: "UAT|Staging",
    },
    keyPassword: "Password123!",
    rsaBits: 2048,
    sanDns: [
        "web01.venafi.example",
        "web02.venafi.example",
    ],
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as venafi from "@pulumi/venafi";

const webserver = new venafi.Certificate("webserver", {
    algorithm: "RSA",
    commonName: "web.venafi.example",
    customFields: {
        "Cost Center": "AB1234",
        Environment: "UAT|Staging",
    },
    keyPassword: "Password123!",
    rsaBits: 2048,
    sanDns: [
        "web01.venafi.example",
        "web02.venafi.example",
    ],
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_venafi as venafi

webserver = venafi.Certificate("webserver",
    algorithm="RSA",
    common_name="web.venafi.example",
    key_password="Password123!",
    rsa_bits=2048,
    san_dns=[
        "web01.venafi.example",
        "web02.venafi.example",
    ])
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi-venafi/sdk/go/venafi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		cert, err := venafi.NewCertificate(ctx, "webserver", &venafi.CertificateArgs{
			Algorithm:   pulumi.String("RSA"),
			CommonName:  pulumi.String("web.venafi.example"),
			KeyPassword: pulumi.String("Password123!"),
			RsaBits:     pulumi.Int(2048),
			SanDns: pulumi.StringArray{
				pulumi.String("web01.venafi.example"),
				pulumi.String("web02.venafi.example"),
			},
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
using Venafi = Pulumi.Venafi;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var webserver = new Venafi.Certificate("webserver", new Venafi.CertificateArgs
            {
                Algorithm = "RSA",
                CommonName = "web.venafi.example",
                KeyPassword = "Password123!",
                RsaBits = 2048,
                SanDns =
                {
                    "web01.venafi.example",
                    "web02.venafi.example",
                },
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/venafi`](https://www.npmjs.com/package/@pulumi/venafi)
* Python: [`pulumi-venafi`](https://pypi.org/project/pulumi-venafi/)
* Go: [`github.com/pulumi/pulumi-venafi/sdk/go/venafi`](https://github.com/pulumi/pulumi-venafi)
* .NET: [`Pulumi.Venafi`](https://www.nuget.org/packages/Pulumi.Venafi)

The Venafi provider is open source and available in the [pulumi/pulumi-venafi](https://github.com/pulumi/pulumi-venafi) repo.
