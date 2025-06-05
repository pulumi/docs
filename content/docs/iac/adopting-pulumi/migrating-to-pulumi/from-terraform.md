---
title_tag: "Migrating from Terraform"
meta_desc: Migrate your existing Terraform HCL and/or coexist with existing workspaces.
title: Terraform
h1: Migrating from Terraform to Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Terraform
        parent: iac-adopting-migrate
        weight: 1
    usingpulumi:
        identifier: from-terraform
        parent: migrating
        weight: 2
aliases:
- /docs/guides/adopting/from_terraform/
- /docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-terraform/
---

If your infrastructure was provisioned with Terraform, there are a number of options that will help you adopt Pulumi.

* **Coexist** with resources provisioned by Terraform by referencing a `.tfstate` file.
* **Import** existing resources into Pulumi [in the usual way](/docs/using-pulumi/adopting-pulumi/import/) or using `pulumi convert --from terraform` along with some `pulumi import --from terraform` to adopt all resources from an existing `.tfstate` file.
* **Convert** any Terraform HCL to Pulumi code using `pulumi convert --from terraform`.
* **Use Terraform Modules** directly within your Pulumi programs through the [Terraform Module](/docs/iac/using-pulumi/extending-pulumi/use-terraform-module/) feature.

This range of techniques helps to either temporarily or permanently use Pulumi alongside Terraform, in addition to fully migrating existing infrastructure to Pulumi.

## Referencing Terraform State

Pulumi allows you to reference output values from existing Terraform state files, enabling you to build new infrastructure that depends on resources provisioned with Terraform. This capability is particularly useful for:

* Organizations with existing Terraform infrastructure where the cost of migration isn't justified
* Teams transitioning gradually from Terraform to Pulumi
* Scenarios where some infrastructure must remain in Terraform due to organizational constraints
* Accessing shared infrastructure (like VPCs, networks, or databases) managed by other teams

You can use the [Terraform provider](/registry/packages/terraform) functions to reference output values from a Terraform configuration:

* For local state files, use [`terraform.state.getLocalReference`](/registry/packages/terraform/api-docs/state/getlocalreference)
* For state files stored in Terraform Cloud or Terraform Enterprise, use [`terraform.state.getRemoteReference`](/registry/packages/terraform/api-docs/state/getremotereference/#terraform-state-getremotereference)

The following code reads VPC and subnet IDs from a local `terraform.tfstate` file and provisions an EKS cluster that uses the read IDs:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as terraform from "@pulumi/terraform";
import * as eks from "@pulumi/eks";

const tfState = terraform.state.getLocalReferenceOutput({
  path: "../terraform/terraform.tfstate",
});

const vpcId = tfState.outputs["vpc_id"] as pulumi.Output<string>;
const publicSubnetIds = tfState.outputs["public_subnet_ids"] as pulumi.Output<string[]>;
const privateSubnetIds = tfState.outputs["private_subnet_ids"] as pulumi.Output<string[]>;

const cluster = new eks.Cluster("my-cluster", {
  vpcId: vpcId,
  publicSubnetIds: publicSubnetIds,
  privateSubnetIds: privateSubnetIds,
});

```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_terraform as terraform
import pulumi_eks as eks

tf_state = terraform.state.get_local_reference_output(
    path="../terraform/terraform.tfstate"
)

vpc_id = tf_state.outputs["vpc_id"]
public_subnet_ids = tf_state.outputs["public_subnet_ids"]
private_subnet_ids = tf_state.outputs["private_subnet_ids"]

cluster = eks.Cluster("my-cluster",
    vpc_id=vpc_id,
    public_subnet_ids=public_subnet_ids,
    private_subnet_ids=private_subnet_ids
)

```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
 "github.com/pulumi/pulumi-eks/sdk/v2/go/eks"
 "github.com/pulumi/pulumi-terraform/sdk/v6/go/terraform/state"
 "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
 pulumi.Run(func(ctx *pulumi.Context) error {
  tfState := state.GetLocalReferenceOutput(ctx, state.GetLocalReferenceOutputArgs{
   Path: pulumi.String("../terraform/terraform.tfstate"),
  })

  outputs := tfState.Outputs()

  vpcId := outputs.ApplyT(func(outputs map[string]interface{}) string {
   return outputs["vpc_id"].(string)
  }).(pulumi.StringOutput)

  publicSubnetIds := outputs.ApplyT(func(outputs map[string]interface{}) []string {
   ids := outputs["public_subnet_ids"].([]interface{})
   result := make([]string, len(ids))
   for i, id := range ids {
    result[i] = id.(string)
   }
   return result
  }).(pulumi.StringArrayOutput)

  privateSubnetIds := outputs.ApplyT(func(outputs map[string]interface{}) []string {
   ids := outputs["private_subnet_ids"].([]interface{})
   result := make([]string, len(ids))
   for i, id := range ids {
    result[i] = id.(string)
   }
   return result
  }).(pulumi.StringArrayOutput)

  _, err := eks.NewCluster(ctx, "my-cluster", &eks.ClusterArgs{
   VpcId:            vpcId,
   PublicSubnetIds:  publicSubnetIds,
   PrivateSubnetIds: privateSubnetIds,
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
using System.Linq;
using System.Collections.Immutable;
using Pulumi;
using Pulumi.Terraform.State;
using Pulumi.Eks;

return await Deployment.RunAsync(() =>
{
    var tfState = GetLocalReference.Invoke(new GetLocalReferenceInvokeArgs
    {
        Path = "../terraform/terraform.tfstate"
    });

    var vpcId = tfState.Apply(state => (string)state.Outputs["vpc_id"]);

    var publicSubnetIds = tfState.Apply(state =>
        ((ImmutableArray<object>)state.Outputs["public_subnet_ids"])
            .Select(id => (string)id)
            .ToArray());

    var privateSubnetIds = tfState.Apply(state =>
        ((ImmutableArray<object>)state.Outputs["private_subnet_ids"])
            .Select(id => (string)id)
            .ToArray());

    var cluster = new Cluster("my-cluster", new ClusterArgs
    {
        VpcId = vpcId,
        PublicSubnetIds = publicSubnetIds,
        PrivateSubnetIds = privateSubnetIds
    });
});

{{% /choosable %}}

{{% choosable language java %}}

```java
import com.pulumi.Pulumi;
import com.pulumi.terraform.state.inputs.GetLocalReferenceArgs;
import com.pulumi.terraform.state.StateFunctions;
import com.pulumi.eks.Cluster;
import com.pulumi.eks.ClusterArgs;

import java.util.List;
import java.util.stream.Collectors;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var tfState = StateFunctions.getLocalReference(GetLocalReferenceArgs.builder()
                    .path("../terraform/terraform.tfstate")
                    .build());

            var vpcId = tfState.applyValue(state -> (String) state.outputs().get("vpc_id"));

            var publicSubnetIds = tfState.applyValue(state -> {
                @SuppressWarnings("unchecked")
                List<Object> ids = (List<Object>) state.outputs().get("public_subnet_ids");
                return ids.stream()
                        .map(id -> (String) id)
                        .collect(Collectors.toList());
            });

            var privateSubnetIds = tfState.applyValue(state -> {
                @SuppressWarnings("unchecked")
                List<Object> ids = (List<Object>) state.outputs().get("private_subnet_ids");
                return ids.stream()
                        .map(id -> (String) id)
                        .collect(Collectors.toList());
            });

            var cluster = new Cluster("my-cluster", ClusterArgs.builder()
                    .vpcId(vpcId)
                    .publicSubnetIds(publicSubnetIds)
                    .privateSubnetIds(privateSubnetIds)
                    .build());
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: my-terraform-state-example
runtime: yaml

variables:
  tfState:
    fn::invoke:
      function: terraform:state:getLocalReference
      arguments:
        path: "../terraform/terraform.tfstate"

resources:
  my-cluster:
    type: eks:Cluster
    properties:
      vpcId: ${tfState.outputs["vpc_id"]}
      publicSubnetIds: ${tfState.outputs["public_subnet_ids"]}
      privateSubnetIds: ${tfState.outputs["private_subnet_ids"]}
```

{{% /choosable %}}

{{< /chooser >}}

## Converting Terraform HCL to Pulumi

The Pulumi CLI can convert existing Terraform source code written in the HashiCorp Configuration Language (HCL) into Pulumi source code via `pulumi convert --from terraform`. In addition to converting source code, there is an option to [automatically insert import IDs](/docs/using-pulumi/adopting-pulumi/import/), so that you can also import state during the conversion. This ensures live resources are brought under the control of Pulumi as well as letting you deploy and manage new copies of that infrastructure.

### How to Use the Converter

To use the converter, [Install Pulumi](/docs/install/) or [try it out online](/tf2pulumi/).

Next, `cd` into a Terraform project you'd like to convert. Then run `pulumi convert --from terraform`. It will convert the entire project whose directory you are in and put the resulting code in the local directory.

{{< chooser language "typescript,python,go,csharp" >}}
{{% choosable language typescript %}}

```bash
pulumi convert --from terraform --language typescript
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
pulumi convert --from terraform --language python
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
pulumi convert --from terraform --language go
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
pulumi convert --from terraform --language csharp
```

{{% /choosable %}}
{{< /chooser >}}

This will generate a Pulumi program that when run with `pulumi up` will deploy the infrastructure originally described by the Terraform project. Note that if your infrastructure references files or directories with paths relative to the location of the Terraform project, you will most likely need to update these paths such that they are relative to the generated {{< langfile >}} file.

### Supported Terraform Features

The following major features are supported:

* Variables, outputs, resources, and data sources
* Terraform modules are converted to Pulumi components
* Almost all HCL2 expression syntax

In cases where the converter does not yet support a feature, the `pulumi convert` command succeeds but generates a TODO in the form of a call to a <pulumi-chooser type="language" options="typescript,python,go,csharp" option-style="none" class="inline">
    <pulumi-choosable type="language" value="typescript"><code>notImplemented</code></pulumi-choosable>
    <pulumi-choosable type="language" value="python"><code>not_implemented</code></pulumi-choosable>
    <pulumi-choosable type="language" value="go"><code>notImplemented</code></pulumi-choosable>
    <pulumi-choosable type="language" value="csharp"><code>NotImplemented</code></pulumi-choosable>
</pulumi-chooser> function that will need to be filled in manually. For most projects, the converter should be able to convert 90-95% of the code without any TODOs, with only a small percentage of items to address manually, significantly reducing migration time compared to doing an entire migration by hand. We are actively improving the converter by adding support for missing features and improving the overall quality of the converted code to reduce the amount of manual fix-ups required.

### Importing Resources

That command converted the static HCL source code to Pulumi code. What if you want to import existing resource states from a `.tfstate` file, however, to avoid unnecessarily recreating your infrastructure?

Call `pulumi import --from terraform ./terraform.tfstate` ensuring a valid location of a `.tfstate` file to import resources from that state.

This will read the resources and their ID's out of the terraform state file and run a standard Pulumi import deployment to read them into the Pulumi state.

Before running the deployment the import file generated will be written out to the current directory, if there are issues importing you can manually edit this file and try again with `pulumi import --file`.

### Example Conversion

For an example of a full conversion, see the [Converting Full Terraform Programs to Pulumi](/blog/converting-full-terraform-programs-to-pulumi/) blog post.

## Using Terraform Modules Directly

Pulumi allows you to use existing Terraform modules directly in your Pulumi programs without converting or rewriting them. This feature is particularly useful for:

* Organizations with significant investment in custom Terraform modules
* Teams that want to leverage the vast ecosystem of modules in the Terraform Registry
* Gradual migration scenarios where some teams continue using Terraform while others adopt Pulumi
* Maintaining consistency across infrastructure while transitioning between tools

### Adding a Terraform Module to Your Pulumi Project

To use a Terraform module in Pulumi, you can add it to your project using the `pulumi package add` command:

```bash
pulumi package add terraform-module <module-source> [<version>] <pulumi-package-name>
```

For example, to add the AWS VPC module from the Terraform Registry:

```bash
pulumi package add terraform-module terraform-aws-modules/vpc/aws 5.19.0 vpc
```

This will generate a local SDK in your programming language that you can import into your Pulumi program. You can then use this module like any other Pulumi package:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const vpc = require("@pulumi/vpc");

// Create a VPC using the terraform-aws-modules/vpc module
const myVpc = new vpc.Module("my-vpc", {
    name: "pulumi-vpc",
    cidr: "10.0.0.0/16",
    azs: ["us-west-2a", "us-west-2b", "us-west-2c"],
    private_subnets: ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"],
    public_subnets: ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"],
    enable_nat_gateway: true
});

// Access outputs from the module
exports.vpcId = myVpc.vpc_id;
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as vpc from "@pulumi/vpc";

// Create a VPC using the terraform-aws-modules/vpc module
const myVpc = new vpc.Module("my-vpc", {
    name: "pulumi-vpc",
    cidr: "10.0.0.0/16",
    azs: ["us-west-2a", "us-west-2b", "us-west-2c"],
    private_subnets: ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"],
    public_subnets: ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"],
    enable_nat_gateway: true
});

// Access outputs from the module
export const vpcId = myVpc.vpc_id;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_vpc as vpc

# Create a VPC using the terraform-aws-modules/vpc module
my_vpc = vpc.Module("my-vpc",
    name="pulumi-vpc",
    cidr="10.0.0.0/16",
    azs=["us-west-2a", "us-west-2b", "us-west-2c"],
    private_subnets=["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"],
    public_subnets=["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"],
    enable_nat_gateway=True
)

# Access outputs from the module
pulumi.export("vpc_id", my_vpc.vpc_id)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    vpc "github.com/pulumi/pulumi-vpc/sdk/go/vpc"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create a VPC using the terraform-aws-modules/vpc module
        myVpc, err := vpc.NewModule(ctx, "my-vpc", &vpc.ModuleArgs{
            Name: pulumi.String("pulumi-vpc"),
            Cidr: pulumi.String("10.0.0.0/16"),
            Azs: pulumi.StringArray{
                pulumi.String("us-west-2a"),
                pulumi.String("us-west-2b"),
                pulumi.String("us-west-2c"),
            },
            PrivateSubnets: pulumi.StringArray{
                pulumi.String("10.0.1.0/24"),
                pulumi.String("10.0.2.0/24"),
                pulumi.String("10.0.3.0/24"),
            },
            PublicSubnets: pulumi.StringArray{
                pulumi.String("10.0.101.0/24"),
                pulumi.String("10.0.102.0/24"),
                pulumi.String("10.0.103.0/24"),
            },
            EnableNatGateway: pulumi.Bool(true),
        })
        if err != nil {
            return err
        }

        // Access outputs from the module
        ctx.Export("vpc_id", myVpc.VpcId)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Vpc = Pulumi.Vpc;

class MyStack : Stack
{
    public MyStack()
    {
        // Create a VPC using the terraform-aws-modules/vpc module
        var myVpc = new Vpc.Module("my-vpc", new Vpc.ModuleArgs
        {
            Name = "pulumi-vpc",
            Cidr = "10.0.0.0/16",
            Azs = new[] { "us-west-2a", "us-west-2b", "us-west-2c" },
            PrivateSubnets = new[] { "10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24" },
            PublicSubnets = new[] { "10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24" },
            EnableNatGateway = true
        });

        // Access outputs from the module
        this.VpcId = myVpc.VpcId;
    }

    [Output]
    public Output<string> VpcId { get; set; }
}
```

{{% /choosable %}}

{{< /chooser >}}

This feature also works seamlessly with local Terraform modules:

```bash
pulumi package add terraform-module ./path/to/module mylocalmod
```

For more information about using Terraform modules directly in Pulumi, see the [Use a Terraform Module in Pulumi](/docs/iac/using-pulumi/extending-pulumi/use-terraform-module/) guide.
