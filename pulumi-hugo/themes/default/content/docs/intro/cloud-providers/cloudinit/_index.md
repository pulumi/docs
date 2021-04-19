---
title: cloud-init
meta_desc: This page provides an overview of the cloud-init Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-cloudinit
    weight: 2
---

The cloud-init provider for Pulumi can be used to render valid MIME-multipart cloud-init config.

See the [full API documentation]({{< relref "/docs/reference/pkg/cloudinit" >}}) for complete details of the available cloud-init provider APIs.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const cloudinit = require("@pulumi/cloudinit")

const resourceConf = new cloudinit.Config("config", {
    gzip: false,
    base64Encode: false,
    parts: [{
        contentType: "text/x-shellscript",
        content: "baz",
        filename: "foobar.sh",
    }]
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as cloudinit from "@pulumi/cloudinit";

const resourceConf = new cloudinit.Config("config", {
    gzip: false,
    base64Encode: false,
    parts: [{
        contentType: "text/x-shellscript",
        content: "baz",
        filename: "foobar.sh",
    }]
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_cloudinit as cloudinit

resource_config = cloudinit.Config("resource", base64_encode=False,
                                   gzip=False,
                                   parts=[cloudinit.GetConfigPartArgs(
                                       content="baz",
                                       content_type="text/x-shellscript",
                                       filename="foobar.sh",
                                   )])
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  "github.com/pulumi/pulumi-cloudinit/sdk/go/cloudinit"
  "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
  pulumi.Run(func(ctx *pulumi.Context) error {
    conf, err := cloudinit.NewConfig(ctx, "test", &cloudinit.ConfigArgs{
      Gzip:         pulumi.Bool(false),
      Base64Encode: pulumi.Bool(false),
      Parts: cloudinit.ConfigPartArray{
        &cloudinit.ConfigPartArgs{
          Content:     pulumi.String("baz"),
          ContentType: pulumi.String("text/x-shellscript"),
          Filename:    pulumi.String("foobar.sh"),
        },
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
using Pulumi.CloudInit;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
          var conf = new Pulumi.CloudInit.Config("demo", new Pulumi.CloudInit.ConfigArgs
          {
              Gzip = false,
              Base64Encode = false,
              Parts =
              {
                  new ConfigPartArgs()
                  {
                      Content = "baz",
                      ContentType = "text/x-shellscript",
                      Filename = "foobar.sh",
                  }
              }
          });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/cloudinit`](https://www.npmjs.com/package/@pulumi/cloudinit)
* Python: [`pulumi-cloudinit`](https://pypi.org/project/pulumi-cloudinit/)
* Go: [`github.com/pulumi/pulumi-cloudinit/sdk/go/cloudinit`](https://github.com/pulumi/pulumi-cloudinit)
* .NET: [`Pulumi.CloudInit`](https://www.nuget.org/packages/Pulumi.CloudInit)

The cloud-init provider is open source and available in the [pulumi/pulumi-cloudinit](https://github.com/pulumi/pulumi-cloudinit) repo.
