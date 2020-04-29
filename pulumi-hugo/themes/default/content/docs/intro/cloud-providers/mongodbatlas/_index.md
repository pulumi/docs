---
title: MongoDB Atlas
meta_desc: This page provides an overview of the MongoDB Atlas Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-mongodbatlas
    weight: 2
---

<img src="/logos/tech/mongodb.png" align="right" class="h-16 px-8 pb-4">

The MongoDB Atlas provider for Pulumi can be used to provision any of the resources available for MongoDB Atlas.
The MongoDB Atlas provider must be configured with credentials to deploy and update resources in MongoDB Atlas.

See the [full API documentation]({{< relref "/docs/reference/pkg/mongodbatlas" >}}) for complete details of the available MongoDB Atlas provider APIs.

## Setup

The MongoDB Atlas provider supports several options for providing access to MongoDB Atlas credentials.  See the [MongoDB Atlas setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const mongodbatlas = require("@pulumi/mongodbatlas")

const project = new mongodbatlas.Project("my-demo-project");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as mongodbatlas from "@pulumi/mongodbatlas";

const project = new mongodbatlas.Project("my-demo-project");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_mongodbatlas as mongodbatlas

project = mongodbatlas.Project("my-demo-project")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  mongodbatlas "github.com/pulumi/pulumi-mongodbatlas/sdk/go/mongodbatlas"
)

project, _ := mongodb.NewProject(ctx, "my-demo-project", &mongodb.ProjectArgs{})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Mongodbatlas;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            project = new Project("my-demo-project", new ProjectArgs{});
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/mongodbatlas`](https://www.npmjs.com/package/@pulumi/mongodbatlas)
* Python: [`pulumi-mongodbatlas`](https://pypi.org/project/pulumi-mongodbatlas/)
* Go: [`github.com/pulumi/pulumi-mongodbatlas/sdk/go/mongodbatlas`](https://github.com/pulumi/pulumi-mongodbatlas)
* .NET: [`Pulumi.Mongodbatlas`](https://www.nuget.org/packages/Pulumi.Mongodbatlas)

The MongoDB Atlas provider is open source and available in the [pulumi/pulumi-mongodbatlas](https://github.com/pulumi/pulumi-mongodbatlas) repo.
