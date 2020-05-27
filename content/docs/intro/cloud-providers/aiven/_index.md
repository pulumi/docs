---
title: Aiven
meta_desc: This page provides an overview of the Aiven Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-aiven
    weight: 2
---

<img src="/logos/tech/aiven.svg" align="right" class="h-16 px-8 pb-4">

The Aiven provider for Pulumi can be used to provision any of the cloud resources available in [Aiven](https://aiven.io/).
The Aiven provider must be configured with credentials to deploy and update resources in Aiven.

See the [full API documentation]({{< relref "/docs/reference/pkg/aiven" >}}) for complete details of the available Aiven provider APIs.

## Setup

The Aiven provider supports several options for providing access to Aiven credentials.  See the [Aiven setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const aiven = require("@pulumi/aiven")

const service = new aiven.Service("my-new-service", {
    project: "my-project",
    cloudName: "google-europe-west1",
    plan:"startup-4",
    serviceName: "my-service",
    serviceType: "grafana",
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as aiven from "@pulumi/aiven";

const service = new aiven.Service("my-new-service", {
    project: "my-project",
    cloudName: "google-europe-west1",
    plan:"startup-4",
    serviceName: "my-service",
    serviceType: "grafana",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_aiven as aiven

service = aiven.Service("my-service",
  project="my-project",
  cloud_name="google-europe-west1",
  plan="startup-4",
  service_name="my-service",
  service_type="grafana",
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
  aiven "github.com/pulumi/pulumi-aiven/sdk/v2/go/aiven"
)

service, _ := aiven.NewService(ctx, "test", &aiven.ServiceArgs{
  Project:     pulumi.String("my-project"),
  CloudName:   pulumi.String("google-europe-west1"),
  Plan:        pulumi.String("startup-4"),
  ServiceName: pulumi.String("my-service"),
  ServiceType: pulumi.String("grafana"),
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Aiven;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var service = new Servicev1("test", new Servicev1Args
            {
                Project = "my-project",
                CloudName = "google-europe-west1",
                Plan = "startup-4",
                ServiceName = "my-service",
                ServiceType = "grafana",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/aiven`](https://www.npmjs.com/package/@pulumi/aiven)
* Python: [`pulumi-aiven`](https://pypi.org/project/pulumi-aiven/)
* Go: [`github.com/pulumi/pulumi-aiven/sdk/go/aiven`](https://github.com/pulumi/pulumi-aiven)
* .NET: [`Pulumi.Aiven`](https://www.nuget.org/packages/Pulumi.Aiven)

The Aiven provider is open source and available in the [pulumi/pulumi-aiven](https://github.com/pulumi/pulumi-aiven) repo.
