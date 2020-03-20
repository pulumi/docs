---
title: Docker
meta_desc: This page provides an overview of the Docker Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-docker
    weight: 2
---

<img src="/logos/tech/docker.png" align="right" class="h-16 px-8 pb-4">

The Docker provider for Pulumi can be used to provision any of the resources available in [Docker](https://www.docker.com/).

See the [full API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/docker" >}}) for complete details of the available Docker provider APIs.

## Setup

The Docker provider supports several options for interacting with Docker.  See the [Docker setup page]({{< relref "setup" >}}) for details.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const docker = require("@pulumi/docker")

const image = new docker.RemoteImage("ubuntu", {
  name: "ubuntu:precise"
});

const container = new docker.Container("ubuntu", {
  image: image.latest,
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as docker from "@pulumi/docker";

const image = new docker.RemoteImage("ubuntu", {
  name: "ubuntu:precise"
});

const container = new docker.Container("ubuntu", {
  image: image.latest,
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_docker as docker

image = docker.RemoteImage("ubuntu",
  name='ubuntu:precise'
)

container = docker.Container("ubuntu",
  image=image.latest
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
  do "github.com/pulumi/pulumi-docker/sdk/go/docker"
)

image, _ := docker.NewRemoteImage(ctx, "ubuntu", &docker.RemoteImageArgs{
  Name: "ubuntu:precise",
})

container, _ := docker.NewContainer(ctx, "ubuntu", &docker.ContainerArgs{
  Image: image.Latest()
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Docker;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var image = new Docker.RemoteImage("ubuntu", new Docker.RemoteImageArgs
            {
                Name = "ubuntu:precise",
            });

            var container = new Docker.Container("ubuntu", new Docker.ContainerArgs
            {
                Image = image.Latest,
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/docker`](https://www.npmjs.com/package/@pulumi/docker)
* Python: [`pulumi-docker`](https://pypi.org/project/pulumi-docker/)
* Go: [`github.com/pulumi/pulumi-docker/sdk/go/docker`](https://github.com/pulumi/pulumi-docker)
* .NET: [`Pulumi.Docker`](https://www.nuget.org/packages/Pulumi.Docker)

The Docker provider is open source and available in the [pulumi/pulumi-docker](https://github.com/pulumi/pulumi-docker) repo.
