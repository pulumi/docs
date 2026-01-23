---
title_tag: "Migrating from Terraform"
meta_desc: Migrate your existing Terraform HCL and/or coexist with existing workspaces.
title: Terraform
h1: Migrating from Terraform or CDKTF to Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Terraform
        parent: iac-guides-migration-from
        weight: 1
aliases:
- /docs/guides/adopting/from_terraform/
- /docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-terraform/
- /docs/iac/adopting-pulumi/migrating-to-pulumi/from-terraform/
---

If your infrastructure was provisioned with Terraform or the CDK for Terraform (CDKTF), there are a number of options that will help you adopt Pulumi:

* **[Neo](/product/neo/) (Recommended)**: Use Neo to automatically convert your Terraform code and import existing resources with zero downtime
* **State-first migration**: Use [`pulumi-terraform-migrate`](https://github.com/pulumi/pulumi-tool-terraform-migrate) to translate your Terraform state to Pulumi state, then use an LLM agent to convert your code.
* **Coexist** with resources provisioned by Terraform or CDKTF by referencing a `.tfstate` file.
* **Import** existing resources into Pulumi [in the usual way](/docs/using-pulumi/adopting-pulumi/import/) or using `pulumi convert --from terraform` along with `pulumi import --from terraform` to adopt all resources from an existing `.tfstate` file.
* **Convert** any Terraform HCL to Pulumi code using `pulumi convert --from terraform`.
* **Use Terraform Modules** directly within your Pulumi programs through the [Terraform Module](/docs/iac/using-pulumi/extending-pulumi/use-terraform-module/) feature.

## Choosing a Terraform migration path

### Pulumi Neo (Recommended)

* **Automated conversion**: Neo converts your Terraform HCL and state to Pulumi automatically
* **Safety verification**: Neo runs `pulumi preview` to prove no changes before you commit

#### Quick start with Neo

1. **Prerequisites**:
   * Ensure you have access to your state file (`.tfstate`)
   * Install the [Pulumi GitHub app](https://github.com/apps/pulumi-cloud) with access to your repository that contains your Terraform configuration files
   * Configure cloud credentials in [Pulumi ESC](/docs/esc/)
   * Have Neo access (available in [Pulumi Cloud](/product/pulumi-cloud/))

2. **Start the migration**:

   ```text
   "Migrate my Terraform configuration to Pulumi"
   ```

3. **Neo will**:
   * Convert your Terraform state to Pulumi state
   * Generate equivalent Pulumi code using your Terraform configuration
   * Verify no changes with `pulumi preview`

4. **Review and commit**:
   * Examine the generated Pulumi code
   * Confirm the preview shows no changes
   * Commit your new Pulumi program

For a detailed technical walkthrough, see our [Neo migration blog post](/blog/neo-migration/).

#### When to use manual migration instead

While Neo handles most Terraform configurations automatically, you might need manual migration for:

* Terraform modules with complex dynamic blocks not yet supported by Neo
* Edge cases with custom providers or unusual state configurations

If you want to fundamentally restructure your infrastructure, we recommend completing the migration first and then refactoring your Pulumi code.

Continue reading below for manual migration approaches if Neo doesn't fit your specific needs.

### Alternative migration paths

If Neo doesn't support your specific use case, or if you prefer manual control over the migration process, the options below provide flexibility to coexist with or migrate from Terraform at your own pace.

## State-first migration with pulumi-terraform-migrate

The [`pulumi-terraform-migrate`](https://github.com/pulumi/pulumi-tool-terraform-migrate) tool provides a state-first approach to migration by translating your Terraform state into Pulumi state. You then use an LLM agent to convert your Terraform code to Pulumi. This approach is useful when:

* You don't have access to Neo
* You want precise control over the state migration process

### Migration workflow

1. **Install the tool**:

   The tool runs as a Pulumi plugin. Ensure you have the [Pulumi CLI](/docs/install/) installed.

1. **Set up your Pulumi project**:

   Create a new Pulumi project in your target language and initialize a stack:

   ```bash
   mkdir my-pulumi-project && cd my-pulumi-project
   pulumi new typescript # or python, go, csharp, etc.
   pulumi up
   ```

1. **Translate your Terraform state**:

   Run the migration tool to translate your Terraform state into Pulumi state:

   ```bash
   pulumi plugin run terraform-migrate -- stack \
       --from path/to/terraform-sources \
       --to path/to/pulumi-project \
       --out /tmp/pulumi-state.json \
       --plugins /tmp/required-plugins.json
   ```

   This generates:
   * `pulumi-state.json`: The translated Pulumi state file
   * `required-plugins.json`: A list of required Pulumi plugins and versions
  
   Note that this step must be repeated for each Terraform stack.

1. **Install required plugins and import state**:

   Install the recommended plugins and import the translated state:

   ```bash
   # Install plugins (example for AWS)
   pulumi plugin install resource aws 7.12.0

   # Import the translated state
   pulumi stack import --file /tmp/pulumi-state.json
   ```

1. **Convert your code with an LLM agent**:

   Use an AI coding assistant to translate your Terraform HCL files into Pulumi code. Popular options include:

   * [Neo](https://www.pulumi.com/product/neo/) - the advantage of Neo is that it already knows about this flow.
   * [Claude Code](https://claude.com/product/claude-code)
   * [Cursor](https://cursor.com)
   * [Codex](https://openai.com/codex/)

   When prompting the LLM, provide:
   * Your original `.tf` files
   * Your target programming language (TypeScript, Python, Go, C#, etc.)
   * The generated `pulumi-state.json` for context on resource names and structure
   * Ask the agent to iterate on the code changes until `pulumi preview --diff` generates as few diffs as possible. If it fails, prompt it to try again.

1. **Verify with pulumi preview**:

   Run `pulumi preview` to confirm the translated code matches your migrated state with no unexpected changes:

   ```bash
   pulumi preview
   ```

   A clean preview with no changes indicates a successful migration. Some minor diffs might be OK.

1. **Run pulumi up**
   
   Once you are satisfied with the migration, run `pulumi up` to finalize the state translation. The migration tool produces an intermediate state file that requires one `pulumi up` run to complete.

## Referencing Terraform State

Pulumi allows you to reference output values from existing Terraform state files, enabling you to build new infrastructure that depends on resources provisioned with Terraform. This capability is particularly useful for:

* Organizations with existing Terraform infrastructure where the cost of migration isn't justified
* Teams transitioning gradually from Terraform or CDKTF to Pulumi
* Scenarios where some infrastructure must remain under management by Terraform due to organizational constraints
* Accessing shared infrastructure (like VPCs, networks, or databases) managed by other teams

You can use the [Terraform provider](/registry/packages/terraform) functions to reference output values from a Terraform state source:

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

The Pulumi CLI can convert existing Terraform source code written in the HashiCorp Configuration Language (HCL) into Pulumi source code using the `pulumi convert` command.

If you're coming to Pulumi from CDKTF, you can generate the HCL for the stacks in your project with `cdktf synth`:

```bash
cdktf synth --hcl
```

This produces a single HCL file for each stack at `./cdktf.out/stacks/<stack-name>/cdk.tf`.

### Using the Converter

To use the converter, first [install Pulumi](/docs/install/), then change to a folder containing the HCL source files you'd like to convert.  Next, run `pulumi convert --from terraform` from within that folder:

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
* Terraform modules, which are converted to Pulumi components
* Almost all HCL2 expression syntax

In cases where the converter does not yet support a certain feature, the `pulumi convert` command succeeds, but generates a TODO in the form of a call to a <pulumi-chooser type="language" options="typescript,python,go,csharp" option-style="none" class="inline">
    <pulumi-choosable type="language" value="typescript"><code>notImplemented</code></pulumi-choosable>
    <pulumi-choosable type="language" value="python"><code>not_implemented</code></pulumi-choosable>
    <pulumi-choosable type="language" value="go"><code>notImplemented</code></pulumi-choosable>
    <pulumi-choosable type="language" value="csharp"><code>NotImplemented</code></pulumi-choosable>
</pulumi-chooser> function that will need to be filled in manually. For most projects, the converter should be able to convert 90-95% of the code without any TODOs, with only a small percentage of items to address manually, significantly reducing migration time compared to doing an entire migration by hand.

If you notice a feature that's not yet implemented or you encounter a bug, please consider [filing an issue](https://github.com/pulumi/pulumi-converter-terraform).

### Importing Resources

The `convert` command translates static HCL source code into Pulumi program code. Often, however, you'll also need to import existing resource state from your Terraform or CDKTF project in order to begin managing those resources with Pulumi.

To do so, you can use `pulumi import --from terraform`:

```bash
pulumi import --from terraform ./terraform.tfstate
```

Given a path to a valid `.tfstate` file and a target Pulumi stack, Pulumi will import the resources defined in that file into the stack and mark them [protected](/docs/iac/concepts/resources/options/protect/) to allow you to make follow-up changes to their source code safely. You can also import resources individually using the [`import`](https://www.pulumi.com/docs/iac/concepts/resources/options/import/) resource option.

To learn more about importing resources with Pulumi, see [Importing Resources](/docs/iac/guides/migration/import/).

### Conversion Examples

To help make migration from Terraform and CDKTF more approachable, we've prepared the following examples for reference:

* [Converting Full Terraform Programs to Pulumi](/blog/converting-full-terraform-programs-to-pulumi/): A blog post that covers the process of converting a real-world Terraform codebase
* [Migrating from CDKTF to Pulumi](https://github.com/pulumi/cdktf-to-pulumi-example): An end-to-end example that covers converting and importing a multi-stack CDKTF project

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

{{< chooser language "typescript,python,go,csharp" >}}

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
