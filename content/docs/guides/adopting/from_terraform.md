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

This range of techniques helps to either temporarily or permenanely use Pulumi alongside Terraform, in addition to fully migrating existing infrastructure to Pulumi.

## Referencing Terraform State

Let's say your team already has some infrastructure stood up with Terraform. Maybe now isn't the time to convert it or maybe some part of your team wants to keep using Terraform for awhile, while you start adopting Pulumi. Often you'll want to interact with that infrastructure, maybe because it exports important IDs, IP addresses, configuration information, and so on. For example, it might define a VPC and you need its ID to create some new VMs in your new Pulumi project; or it may provision a Kubernetes cluster and you need the `kubeconfig` to deploy some application services into the cluster; etc.

In each of these cases, you can use the `RemoteStateReference` resource to reference output variables exported from the Terraform project. This works for manually managed state files in addition to Terraform Cloud or Enterprise ones.

To use this class, first install the relevant package on your system:

{{< langchoose csharp >}}

<div class="language-prologue-javascript"></div>

```bash
$ npm install @pulumi/terraform
```

<div class="language-prologue-typescript"></div>

```bash
$ npm install @pulumi/terraform
```

<div class="language-prologue-python"></div>

```bash
$ pip3 install pulumi_terraform
```

<div class="language-prologue-go"></div>

> Terraform RemoteStateReference is not yet supported in Go. See <https://github.com/pulumi/pulumi-terraform/issues/518>.

<div class="language-prologue-csharp"></div>

> Terraform RemoteStateReference is not yet supported in .NET. See <https://github.com/pulumi/pulumi-terraform/issues/516>.

For example, this code reads AWS EC2 VPC and subnet IDs from `terraform.tfstate` file and provisions new EC2 instances that use them:

{{< langchoose csharp >}}

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

```go
// Terraform RemoteStateReference is not yet supported in Go.
//
// See https://github.com/pulumi/pulumi-terraform/issues/518.
```

```csharp
// Terraform RemoteStateReference is not yet supported in .NET.
//
// See https://github.com/pulumi/pulumi-terraform/issues/516.
```

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

{{< langchoose csharp >}}

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

```go
// Terraform RemoteStateReference is not yet supported in Go.
//
// See https://github.com/pulumi/pulumi-terraform/issues/518.
```

```csharp
// Terraform RemoteStateReference is not yet supported in .NET.
//
// See https://github.com/pulumi/pulumi-terraform/issues/516.
```

Notice also that we've used [Pulumi secrets]({{< relref "/docs/intro/concepts/config#secrets" >}}) to ensure the Terraform Cloud or Enterprise token is secure and encrypted.

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

Please refer to the API documentation for these libraries for full details on configuration options for each backend type: [Node.js (JavaScript or TypeScript)]({{< relref "/docs/reference/pkg/nodejs/pulumi/terraform/state#RemoteStateReference" >}}) or [Python]({{< relref "/docs/reference/pkg/python/pulumi_terraform/state" >}}).

## Converting Terraform HCL to Pulumi

The [`tf2pulumi`](https://github.com/pulumi/tf2pulumi) tool can convert existing Terraform source code written in the HashiCorp Configuration Language (HCL) into Pulumi source code. In addition to converting source code, this tool also offers the option to automatically insert import IDs [as described here]({{< relref "import" >}}), so that you can also import state during the conversion. This ensures live resources are brought under the control of Pulumi as well as letting you deploy and manage new copies of that inrastruture.

### How to Use the Tool

To use this tool, [first install it](https://github.com/pulumi/tf2pulumi#building-and-installation).

> At the moment, this tool needs to be built from source. Regularly released binaries across macOS, Linux, and Windows [will soon be available](https://github.com/pulumi/tf2pulumi/issues/119).

Next, `cd` into a Terraform project you'd like to convert. Create a new stack in a subdirectory:

```bash
$ pulumi new typescript --dir my-stack
```

> At the moment, TypeScript is the only language target. [Python is under active development](https://github.com/pulumi/tf2pulumi/issues/98). Please let us know if your desired language isn't available.

Next, run `tf2pulumi`. It will conver the entire project whose directory you are in and print the resulting code to `stdout`. You'll probably want to redirect its output, for instance to a file named `index.ts` in the directory that contains the Pulumi project you just created:

```bash
$ tf2pulumi >my-stack/index.ts
```

This will generate a Pulumi TypeScript program in index.ts that when run with pulumi update will deploy the infrastructure originally described by the Terraform project. Note that if your infrastructure references files or directories with paths relative to the location of the Terraform project, you will most likely need to update these paths such that they are relative to the generated index.ts file.

> If `tf2pulumi` complains about missing Terraform resource plugins, install those plugins as per the instructions in the error message and re-run the command above. The `--allow-missing-plugins` option allows you to proceed even in the face of missing plugins.

If you'd like to record the original HCL source code positions in the resulting generated code, pass the `--record-locations` flag. This can help with subsequent refactorings which may require that you consult back with the origin source code.

### Importing Resources

That command converted the static HCL source code to Pulumi code. What if you want to import existing resource states from a `.tfstate` file, however, to avoid unnecessarily recreating your infrastructure?

To do so, [copy the `import.ts` file from this repo](https://github.com/pulumi/tf2pulumi/blob/master/misc/import/import.ts) into your new stack's directory, and add the following near the top of your generated `index.ts` file just before any resource creations:

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

While the majority of Terraform constructs are supported, there are some known gaps that we are working to address. If you run into a problem, please [let us know on GitHub](https://github.com/pulumi/tf2pulumi/issues/new) and we would be happy to work through it with you.

### Example Conversion

For an example of a full end-to-end conversion, including some improvements made possible after the conversion is finished, please see the blog post, [From Terraform to Infrastructure as Software]({{< relref "/blog/from-terraform-to-infrastructure-as-software" >}}).
