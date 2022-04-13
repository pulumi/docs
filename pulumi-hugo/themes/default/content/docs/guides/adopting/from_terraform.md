---
title: "From Terraform"
meta_desc: Migrate your existing Terraform HCL and/or coexist with existing workspaces.
menu:
  userguides:
    parent: adopting
    weight: 2
---

If your infrastructure was provisioned with Terraform, there are a number of options that will help you adopt Pulumi.

* **Coexist** with resources provisioned by Terraform by referencing a `.tfstate` file.
* **Import** existing resources into Pulumi [in the usual way]({{< relref "import" >}}) or using the `tf2pulumi` to adopt all resources from an existing `.tfstate` file.
* **Convert** any Terraform HCL to Pulumi code using `tf2pulumi`.

This range of techniques helps to either temporarily or permanently use Pulumi alongside Terraform, in addition to fully migrating existing infrastructure to Pulumi.

## Referencing Terraform State

Let's say your team already has some infrastructure stood up with Terraform. Maybe now isn't the time to convert it or maybe some part of your team wants to keep using Terraform for awhile, while you start adopting Pulumi. Often you'll want to interact with that infrastructure, maybe because it exports important IDs, IP addresses, configuration information, and so on. For example, it might define a VPC and you need its ID to create some new VMs in your new Pulumi project; or it may provision a Kubernetes cluster and you need the `kubeconfig` to deploy some application services into the cluster; etc.

In each of these cases, you can use the `RemoteStateReference` resource to reference output variables exported from the Terraform project. This works for manually managed state files in addition to Terraform Cloud or Enterprise ones.

To use this class, first install the relevant package on your system:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```bash
$ npm install @pulumi/terraform
```

{{% /choosable %}}
{{% choosable language typescript %}}

```bash
$ npm install @pulumi/terraform
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ pip3 install pulumi_terraform
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
$ go get github.com/pulumi/pulumi-terraform/sdk/v4
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
$ dotnet add package Pulumi.Terraform
```

{{% /choosable %}}

{{< /chooser >}}

For example, this code reads AWS EC2 VPC and subnet IDs from `terraform.tfstate` file and provisions new EC2 instances that use them:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let aws = require("@pulumi/aws");
let terraform = require("@pulumi/terraform");

// Reference the Terraform state file:
let networkState = new terraform.state.RemoteStateReference("network", {
    backendType: "local",
    path: "/path/to/terraform.tfstate",
});

// Read the VPC and subnet IDs into variables:
let vpcId = networkState.getOutput("vpc_id");
let publicSubnetIds = networkState.getOutput("public_subnet_ids");

// Now spin up servers in the first two subnets:
for (let i = 0; i < 2; i++) {
    new aws.ec2.Instance(`instance-${i}`, {
        ami: "ami-7172b611",
        instanceType: "t2.medium",
        subnetId: publicSubnetIds[i],
    });
}
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";
import * as terraform from "@pulumi/terraform";

// Reference the Terraform state file:
const networkState = new terraform.state.RemoteStateReference("network", {
    backendType: "local",
    path: "/path/to/terraform.tfstate",
});

// Read the VPC and subnet IDs into variables:
const vpcId = networkState.getOutput("vpc_id");
const publicSubnetIds = networkState.getOutput("public_subnet_ids");

// Now spin up servers in the first two subnets:
for (let i = 0; i < 2; i++) {
    new aws.ec2.Instance(`instance-${i}`, {
        ami: "ami-7172b611",
        instanceType: "t2.medium",
        subnetId: publicSubnetIds[i],
    });
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_aws as aws
import pulumi_terraform as terraform

# Reference the Terraform state file:
network_state = terraform.state.RemoteStateReference('network',
    backend_type='local',
    args=terraform.state.LocalBackendArgs(path='../terraform.tfstate'))

# Read the VPC and subnet IDs into variables:
vpc_id = network_state.get_output('vpc_id')
public_subnet_ids = network_state.get_output('public_subnet_ids')

# Now spin up servers in the first two subnets:
for i in range(2):
    aws.ec2.Instance(f'instance-{i}',
        ami='ami-7172b611',
        instance_type='t2.medium',
        subnet_id=public_subnet_ids[i])
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "os"

    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi-terraform/sdk/v4/go/state"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        cwd, err := os.Getwd()
        if err != nil {
            return err
        }

        state, err := state.NewRemoteStateReference(ctx, "localstate", &state.LocalStateArgs{
            Path: pulumi.String(filepath.Join(cwd, "terraform.tfstate")),
        })
        if err != nil {
            return err
        }

        publicSubnetIds := stateRef.Outputs.ApplyT(func(args interface{}) ([]string, error) {
            ids := args.(map[string]interface{})["public_subnet_ids"].([]interface{})
            subnetIds := make([]string, len(ids))
            for i, v := range ids {
                subnetIds[i] = v.(string)
            }
            return subnetIds, nil
        }).(pulumi.StringArrayOutput)

        for x := 0; x < 2; x++ {
            _, err := ec2.NewInstance(ctx, fmt.Sprintf("instance-%d", ii), &ec2.InstanceArgs{
                Ami:          pulumi.String("ami-7172b611"),
                InstanceType: pulumi.String("t2.medium"),
                SubnetId:     publicSubnetIds.Index(pulumi.Int(x)),
            })
            if err != nil {
                return err
            }
        }

        return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Immutable;
using System.Linq;
using System.Threading.Tasks;

using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Terraform.State;

class MyStack : Stack
{
    public MyStack()
    {
          var remoteState = new RemoteStateReference("localstate", new LocalBackendRemoteStateReferenceArgs
          {
              Path = Path.GetFullPath("terraform.tfstate"),
          });

          var subnetIds = remoteState.GetOutput("public_subnet_ids").
              Apply(ids => ((ImmutableArray<object>) ids).Cast<string>().ToImmutableArray());

          for (int i = 0; i < 2; i++)
          {
              var server = new Instance($"instance-{i}", new InstanceArgs
              {
                  Ami = "ami-7172b611",
                  InstanceType = "t2.micro",
                  SubnetId = subnetIds.GetAt(i),
              });
          }
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

If we run `pulumi up`, well see the two new servers get spun up:

```bash
$ pulumi up
Updating (dev):

     Type                 Name             Status
     pulumi:pulumi:Stack  tfimport-dev
 +   ├─ aws:ec2:Instance  instance-0       created
 +   └─ aws:ec2:Instance  instance-1       created

Resources:
    + 2 created
    1 unchanged
```

This example uses the `"local"` backend type which simply reads a `tfstate` file on disk. There are multiple backends available. For example, this slight change to how the `RemoteStateReference` object is constructed will use a Terraform Cloud or Enterprise workspace:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let aws = require("@pulumi/aws");
let pulumi = require("@pulumi/pulumi");
let terraform = require("@pulumi/terraform");

// Reference the Terraform remote workspace:
let config = new pulumi.Config();
let tfeToken = config.requireSecret("tfeToken");
let networkState = new terraform.state.RemoteStateReference("network", {
    backendType: "remote",
    token: tfeToken,
    organization: "acmecorp",
    workspaces: {
        name: "production-network"
    },
});

// Same as above ...
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";
import * as terraform from "@pulumi/terraform";

// Reference the Terraform remote workspace:
const config = new pulumi.Config();
const tfeToken = config.requireSecret("tfeToken");
const networkState = new terraform.state.RemoteStateReference("network", {
    backendType: "remote",
    token: tfeToken,
    organization: "acmecorp",
    workspaces: {
        name: "production-network"
    },
});

// Same as above ...
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_terraform as terraform

# Reference the Terraform state file:
config = pulumi.Config()
tfe_token = config.require_secret('tfeToken')
network_state = terraform.state.RemoteStateReference('network',
    backend_type='remote',
    args=terraform.state.RemoteBackendArgs(
        organization='acmecorp',
        token=tfe_token,
        workspace_name='production-network'))

# Same as above ...
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"

	"github.com/pulumi/pulumi-terraform/sdk/v4/go/state"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

        conf := config.New(ctx, "")
        token := conf.RequireSecret("tfeToken")
        organization := conf.Require("organization")
        workspace := conf.Require("workspaceName")

        state, err := state.NewRemoteStateReference(ctx, "remote-backend-state", &state.RemoteBackendStateArgs{
            Organization: pulumi.String(organization),
            Token:        token.(pulumi.StringOutput),
            Workspaces: state.WorkspaceStateArgs{
                Name: pulumi.String(workspace),
            },
        })
        if err != nil {
            return err
        }

        // Same as above ...

        return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Terraform.State;

class MyStack : Stack
{
    public MyStack()
    {
        var config = new Config();
        var tfeToken = config.RequireSecret("tfeToken");
        var organization = config.Require("organization");
        var workspace = config.Require("workspaceName");
        var remoteState = new RemoteStateReference("localstate", new RemoteBackendRemoteStateReferenceArgs()
        {
            Token = tfeToken,
            Organization = organization,
            Workspaces = new RemoteBackendWorkspaceConfig()
            {
                Name = workspace,
            }
        });

        // Same as above...
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

Notice also that we've used [Pulumi secrets]({{< relref "/docs/intro/concepts/secrets" >}}) to ensure the Terraform Cloud or Enterprise token is secure and encrypted.

The full list of available backends are as follows:

* Artifactory (`"artifactory"`)
* Azure Resource Manager (`"azurerm"`)
* Consul (`"consul"`)
* etcd v2 (`"etcd"`)
* etcd v3 (`"etcdv3"`)
* Google Cloud Storage (`"gcs"`)
* HTTP (`"http"`)
* Local `.tfstate` File (`"local"`)
* Manta (`"manta"`)
* Postgres (`"pg"`)
* Terraform Enterprise or Terraform Cloud (`"remote"`)
* AWS S3 (`"s3"`)
* Swift (`"swift"`)

Refer to the API documentation for these libraries for full details on configuration options for each backend type: [Node.js (JavaScript or TypeScript)]({{< relref "/docs/reference/pkg/nodejs/pulumi/terraform/state#RemoteStateReference" >}}) or [Python]({{< relref "/docs/reference/pkg/python/pulumi_terraform/state" >}}).

## Converting Terraform HCL to Pulumi

The [`tf2pulumi`](https://github.com/pulumi/tf2pulumi) tool can convert existing Terraform source code written in the HashiCorp Configuration Language (HCL) into Pulumi source code. In addition to converting source code, this tool also offers the option to [automatically insert import IDs]({{< relref "import" >}}), so that you can also import state during the conversion. This ensures live resources are brought under the control of Pulumi as well as letting you deploy and manage new copies of that inrastruture.

### How to Use the Tool

To use this tool, [first install it](https://github.com/pulumi/tf2pulumi#building-and-installation) or [try it out online]({{< relref "/tf2pulumi" >}}).

Next, `cd` into a Terraform project you'd like to convert. Create a new Pulumi project:

{{< chooser language "typescript,python,go,csharp" >}}
{{% choosable language typescript %}}

```bash
$ pulumi new typescript -f
```

Next, run `tf2pulumi`. It will convert the entire project whose directory you are in and put the resulting code in the local directory.

```bash
$ tf2pulumi --target-language typescript
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ pulumi new python -f
```

Next, run `tf2pulumi`. It will convert the entire project whose directory you are in and put the resulting code in the local directory.

```bash
$ tf2pulumi --target-language python
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
$ pulumi new go -f
```

Next, run `tf2pulumi`. It will convert the entire project whose directory you are in and put the resulting code in the local directory.

```bash
$ tf2pulumi --target-language go
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
$ pulumi new csharp -f
```

Next, run `tf2pulumi`. It will convert the entire project whose directory you are in and put the resulting code in the local directory.

```bash
$ tf2pulumi --target-language csharp
```

{{% /choosable %}}
{{< /chooser >}}

This will generate a Pulumi TypeScript program in index.ts that when run with pulumi update will deploy the infrastructure originally described by the Terraform project. Note that if your infrastructure references files or directories with paths relative to the location of the Terraform project, you will most likely need to update these paths such that they are relative to the generated index.ts file.

> If `tf2pulumi` complains about missing Terraform resource plugins, install those plugins as per the instructions in the error message and re-run the command above. The `--allow-missing-plugins` option allows you to proceed even in the face of missing plugins.

If you'd like to record the original HCL source code positions in the resulting generated code, pass the `--record-locations` flag. This can help with subsequent refactorings which may require that you consult back with the origin source code.

### Importing Resources

That command converted the static HCL source code to Pulumi code. What if you want to import existing resource states from a `.tfstate` file, however, to avoid unnecessarily recreating your infrastructure?

If you are using TypeScript, [copy the `import.ts` file from this repo](https://github.com/pulumi/tf2pulumi/blob/master/misc/import/import.ts) into your new stack's directory and add the following near the top of your generated `index.ts` file just before any resource creations:

```typescript
...
import "./import";
...
```

Next, set the `importFromStatefile` config setting on your project to a valid location of a `.tfstate` file to import resources from that state:

```bash
$ pulumi config set importFromStatefile ./terraform.tfstate
```

After doing this, the first `pulumi up` for a new stack with this configuration variable set will import instead of create all of the resources defined in the code. Once imported, the existing resources in your cloud provider can now be managed by Pulumi going forward. See the [Importing Infrastructure User Guide]({{< relref "import" >}}) for more details on importing existing resources.

### Limitations

While the majority of Terraform constructs are supported, there are some known gaps that we are working to address. If you run into a problem, [open an issue on GitHub](https://github.com/pulumi/tf2pulumi/issues/new) and we would be happy to work through it with you.

### Example Conversion

For an example of a full end-to-end conversion, including some improvements made possible after the conversion is finished, see the blog post, [From Terraform to Infrastructure as Software]({{< relref "/blog/from-terraform-to-infrastructure-as-software" >}}).
