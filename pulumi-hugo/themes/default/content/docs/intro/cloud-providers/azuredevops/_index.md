---
title: AzureDevOps
meta_desc: This page provides an overview of the AzureDevOps Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-azuredevops
    weight: 2
---

<img src="/logos/tech/azuredevops.png" align="right" class="h-16 px-8 pb-4">

The AzureDevOps provider for Pulumi can be used to provision any of the cloud resources available in [AzureDevOps](https://azure.microsoft.com/en-us/services/devops/).
The AzureDevOps provider must be configured with credentials to deploy and update resources in AzureDevOps.

See the [full API documentation]({{< relref "/docs/reference/pkg/azuredevops" >}}) for complete details of the available AzureDevOps provider APIs.

## Setup

The AzureDevOps provider supports several options for providing access to AzureDevOps credentials.  See the [AzureDevOps setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const ado = require("@pulumi/azuredevops")

const project = new ado.Core.Project("demo-project", {
    projectName: "my-project",
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as ado from "@pulumi/azuredevops";

const project = new ado.Core.Project("demo-project", {
    projectName: "my-project",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_azuredevops as ado

project = ado.core.Project("demo-project",
                           project_name="my-project")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	ado "github.com/pulumi/pulumi-azuredevops/sdk/v2/go/azuredevops"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		project, err := ado.NewProject(ctx, "test", &ado.ProjectArgs{
			ProjectName: pulumi.String("my-project"),
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
using Pulumi.AzureDevOps.Core;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var project = new Project("test", new ProjectArgs
            {
                ProjectName = "my-project",
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/azuredevops`](https://www.npmjs.com/package/@pulumi/azuredevops)
* Python: [`pulumi-azuredevops`](https://pypi.org/project/pulumi-azuredevops/)
* Go: [`github.com/pulumi/pulumi-azuredevops/sdk/v2/go/azuredevops`](https://github.com/pulumi/pulumi-azuredevops)
* .NET: [`Pulumi.AzureDevOps`](https://www.nuget.org/packages/Pulumi.AzureDevOps)

The AzureDevOps provider is open source and available in the [pulumi/pulumi-azuredevops](https://github.com/pulumi/pulumi-azuredevops) repo.
