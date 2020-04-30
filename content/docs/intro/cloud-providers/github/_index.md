---
title: GitHub
meta_desc: This page provides an overview of the GitHub Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-github
    weight: 2
---

<img src="/logos/tech/github.svg" align="right" class="h-16 px-8 pb-4">

The GitHub provider for Pulumi can be used to provision any of the cloud resources available in [GitHub](https://github.com/).
The GitHub provider must be configured with credentials to deploy and update resources in GitHub.

See the [full API documentation]({{< prelref "/docs/reference/pkg/github" >}}) for complete details of the available GitHub provider APIs.

## Setup

The GitHub provider supports several options for providing access to GitHub credentials.  See the [GitHub setup page]({{< prelref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const github = require("@pulumi/github")

const repo = new github.Repository("demo-repo", {
  description: "Generated from automated test",
  private: true,
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as github from "@pulumi/github";

const repo = new github.Repository("demo-repo", {
  description: "Generated from automated test",
  private: true,
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_github as github

repo = github.Repository("demo-repo",
  description="Generated from automated test",
  private="true",
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  github "github.com/pulumi/pulumi-github/sdk/go/github"
)

repository, _ := github.NewRepository(ctx, "demo-repo", &github.RepositoryArgs{
  Description: pulumi.String("Generated from automated test"),
  Private:     pulumi.Boolean(true),
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Github;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var repo = new Repository("test", new RepositoryArgs
            {
                Description = "Generated from automated test",
                Private = true,
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/github`](https://www.npmjs.com/package/@pulumi/github)
* Python: [`pulumi-github`](https://pypi.org/project/pulumi-github/)
* Go: [`github.com/pulumi/pulumi-github/sdk/go/github`](https://github.com/pulumi/pulumi-github)
* .NET: [`Pulumi.Github`](https://www.nuget.org/packages/Pulumi.Github)

The GitHub provider is open source and available in the [pulumi/pulumi-github](https://github.com/pulumi/pulumi-github) repo.
