---
title: Rancher Kubernetes Engine
meta_desc: This page provides an overview of the RKE Provider for Pulumi.
menu:
  intro:
    parent: cloud-providers
    identifier: clouds-rke
    weight: 2
---

<img src="/logos/tech/rke.svg" align="right" class="h-16 px-8 pb-4">

The RKE provider for Pulumi can be used to provision Kubernetes clusters using the [Rancher Kubernetes Engine](https://github.com/rancher/rke).

See the [full API documentation]({{< relref "/docs/reference/pkg/rke" >}}) for complete details of the available RKE provider APIs.

## Example

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const rke = require("@pulumi/rke")

const cluster = new rke.Cluster('my-cluster', {
  cloudProvider: {
    name: "aws"
  },
  nodes: [{
    address: "<public ip address of host machine>",
    internalAddress: "<private ip address of host machine>",
    user: "<ssh username of host machine>",
    sshKey: "<private key to use when sshing to the host machine>",
    roles: [ "controlplane", "etcd", "worker" ],
  }],
  clusterName: "nodejs-test-cluster",
})
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as rke from "@pulumi/rancher2";

const cluster = new rke.Cluster('my-cluster', {
  cloudProvider: {
    name: "aws"
  },
  nodes: [{
    address: "<public ip address of host machine>",
    internalAddress: "<private ip address of host machine>",
    user: "<ssh username of host machine>",
    sshKey: "<private key to use when sshing to the host machine>",
    roles: [ "controlplane", "etcd", "worker" ],
  }],
  clusterName: "nodejs-test-cluster",
})
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_rke as rke

rke_cluster = rke.Cluster("my-cluster", cloud_provider=rke.ClusterCloudProviderArgs(name="aws"),
                          nodes=[
                            rke.ClusterNodeArgs(address="<public ip address of host machine>",
                                                internal_address="<private ip address of host machine>",
                                                user="<ssh username of host machine>",
                                                ssh_key="<private key to use when sshing to the host machine>",
                                                roles=["controlplane", "etcd", "worker"])
                          ],
                          cluster_name="python-test-cluster")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	rke "github.com/pulumi/pulumi-rke/sdk/go/rke"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		user, err := rke.NewCluster(ctx, "my-cluster", &rke.ClusterArgs{
			CloudProvider: &rke.CloudProviderArgs{
				Name: pulumi.String("aws"),
            },
            Nodes: &rke.ClusterNodeArray{
				&rke.ClusterNode{
				    Address:         pulumi.String("<public ip address of host machine>"),
				    InternalAddress: pulumi.String("<private ip address of host machine>"),
				    User:            pulumi.String("<ssh username of host machine>"),
				    SshKey:          pulumi.String("<private key to use when sshing to the host machine>"),
				    Roles:           pulumi.StringArray{
				        &pulumi.String("controlplane"),
				        &pulumi.String("etcd"),
				        &pulumi.String("worker")
                    },
                },
            },
			ClusterName: pulumi.String("go-test-cluster"),
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
using Pulumi.Rke;

class Program
{
    static Task Main() =>
        Deployment.Run(() => {
            var cluster = new Cluster("my-cluster", new ClusterArgs
            {
                CloudProvider =
                {
                    Name = "aws",
                },
                ClusterName = "dotnet-test-cluster",
                Nodes =
                {
                  new ClusterNodeArgs
                  {
                    Address = "<public ip address of host machine>",
                    InternalAddress = "<private ip address of host machine>",
                    User = "<ssh username of host machine>",
                    SshKey = "<private key to use when sshing to the host machine>",
                    Roles =  { "controlplan", "etcd", "worker" },
                  },
                },
                Password = "initialPassw0rd",
                Enabled = true,
            });
        });
}
```

{{% /choosable %}}

{{< /chooser >}}

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/rke`](https://www.npmjs.com/package/@pulumi/rke)
* Python: [`pulumi-rke`](https://pypi.org/project/pulumi-rke/)
* Go: [`github.com/pulumi/pulumi-rke/sdk/go/rke`](https://github.com/pulumi/pulumi-rke)
* .NET: [`Pulumi.Rke`](https://www.nuget.org/packages/Pulumi.Rke)

The RKE provider is open source and available in the [pulumi/pulumi-rke](https://github.com/pulumi/pulumi-rke) repo.
