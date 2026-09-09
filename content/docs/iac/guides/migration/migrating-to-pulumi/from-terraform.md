---
title_tag: "Migrating from Terraform"
meta_desc: Migrate your existing Terraform HCL and/or coexist with existing workspaces.
title: Terraform
h1: Migrating from Terraform or CDKTF to Pulumi
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

If your infrastructure was provisioned with Terraform or the CDK for Terraform (CDKTF), there are a number of options that will help you adopt Pulumi. Not all of them involve converting code: you can put your Terraform state under Pulumi Cloud's management, or run your existing HCL on the Pulumi engine, without rewriting anything.

**Adopt Pulumi without converting your code:**

* **[Use Pulumi Cloud as your state backend](/docs/iac/get-started/terraform/terraform-state-backend/)** and keep running the Terraform or OpenTofu CLI, adding a standard `backend "remote"` block and nothing else.
* **[Keep writing HCL](/docs/iac/languages-sdks/hcl/)** with `runtime: hcl`, which runs your `.tf` files on the Pulumi engine.
* **[Use Terraform modules](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/)** directly within your Pulumi programs.
* **Coexist** with resources provisioned by Terraform or CDKTF by referencing a `.tfstate` file.

**Convert to a Pulumi program:**

* **[Neo](/product/neo/) (Recommended)**: Use Neo to automatically convert your Terraform code and import existing resources with zero downtime
* **State-first migration**: Use [`pulumi-terraform-migrate`](https://github.com/pulumi/pulumi-tool-terraform-migrate) to translate your Terraform state to Pulumi state, then use an LLM agent to convert your code.
* **Agent-driven import**: Use [`pulumi-tool-import`](/docs/iac/guides/migration/migrating-to-pulumi/terraform-import-tool/) and its agent skills to hand-author a Pulumi program and import an entire workspace to a zero-diff preview.
* **Import** existing resources into Pulumi [in the usual way](/docs/iac/guides/migration/import/) or using `pulumi convert --from terraform` along with `pulumi import --from terraform` to adopt all resources from an existing `.tfstate` file.
* **Convert** any Terraform HCL to Pulumi code using `pulumi convert --from terraform`.

## Adopting Pulumi without converting your code

Converting is not a prerequisite for getting value from Pulumi. Two options let a team keep its existing Terraform investment as-is.

### Pulumi Cloud as your Terraform state backend

[Pulumi Cloud implements the Terraform remote backend API](/docs/iac/get-started/terraform/terraform-state-backend/), so pointing an existing project at it means adding a standard `backend "remote"` block. Your resource code and day-to-day workflow are unchanged, and the guide covers migrating state from HCP Terraform, Amazon S3, Azure Blob Storage, Google Cloud Storage, and local files.

Terraform state held in Pulumi Cloud gets encrypted storage, update history, state locking, RBAC, audit policies, and unified visibility in [Resource Search](/docs/insights/discovery/search/). Root module outputs surface as Pulumi [stack outputs](/docs/iac/concepts/stacks/#stackreferences), so Pulumi stacks can consume them directly. Stacks created through the Terraform or OpenTofu CLI also [run their plans and applies on Pulumi Cloud](/docs/iac/get-started/terraform/terraform-remote-execution/) by default.

### Writing Pulumi programs in HCL

[Pulumi HCL](/docs/iac/languages-sdks/hcl/) is a supported Pulumi language. A project is a `Pulumi.yaml` with `runtime: hcl` alongside ordinary `.tf` files, so an existing HCL codebase moves onto the Pulumi engine without a rewrite. A general-purpose language is still the recommended destination, since that is where language-native testing, package management, and IDE tooling live, but it becomes a later decision rather than a precondition.

## Pulumi Neo (recommended)

* **Automated conversion**: Neo converts your Terraform HCL and state to Pulumi automatically
* **Safety verification**: Neo runs `pulumi preview` to prove no changes before you commit

### Quick start with Neo

1. **Prerequisites**:
   * Ensure you have access to your state file (`.tfstate`)
   * Install the [Pulumi GitHub app](/docs/integrations/version-control/github-app/) with access to your repository that contains your Terraform configuration files
   * Configure cloud credentials in [Pulumi ESC](/docs/esc/)
   * Have [Pulumi Neo](/product/neo/) access

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

### When to use manual migration instead

While Neo handles most Terraform configurations automatically, you might need manual migration for:

* Terraform modules with complex dynamic blocks not yet supported by Neo
* Edge cases with custom providers or unusual state configurations

If you want to fundamentally restructure your infrastructure, we recommend completing the migration first and then refactoring your Pulumi code.

Continue reading below for manual migration approaches if Neo doesn't fit your specific needs.

## Alternative migration paths

If Neo doesn't support your specific use case, or if you prefer manual control over the migration process, the options below provide flexibility to coexist with or migrate from Terraform at your own pace.

### Keep your code in HCL

If your configuration is fine as it stands and it's the platform you want to change, you don't have to convert anything. Set `runtime: hcl` in `Pulumi.yaml` and Pulumi runs your existing `.tf` files unchanged. See the [HCL language docs](/docs/iac/languages-sdks/hcl/) for details.

State migration still applies. Pulumi does not reuse a Terraform state file in place — state lives in whichever backend `pulumi login` points at — so bring your existing resources across with:

```bash
$ pulumi import --from hcl terraform.tfstate
```

This reads a Terraform or OpenTofu state file and imports every managed resource in the root module into your stack. Resources nested inside modules are skipped with a warning; import those [in the usual way](/docs/iac/guides/migration/import/).

`--from hcl` reads your `.tf` files alongside the state file, so run it from the project directory. If you have converted to a general-purpose language and no longer have `.tf` files on disk, use [`--from terraform`](#importing-resources) instead.

### State-first migration with pulumi-terraform-migrate

The [`pulumi-terraform-migrate`](https://github.com/pulumi/pulumi-tool-terraform-migrate) tool provides a state-first approach to migration by translating your Terraform state into Pulumi state. You then use an LLM agent to convert your Terraform code to Pulumi. This approach is useful when:

* You don't have access to Neo
* You want precise control over the state migration process

#### Migration workflow

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
   * Your target programming language (TypeScript, Python, Go, .NET, etc.)
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

### Referencing Terraform state

Pulumi allows you to reference output values from existing Terraform state files, enabling you to build new infrastructure that depends on resources provisioned with Terraform. This capability is particularly useful for:

* Organizations with existing Terraform infrastructure where the cost of migration isn't justified, including teams that keep running Terraform against [Pulumi Cloud as their state backend](/docs/iac/get-started/terraform/terraform-state-backend/)
* Teams transitioning gradually from Terraform or CDKTF to Pulumi
* Scenarios where some infrastructure must remain under management by Terraform due to organizational constraints
* Accessing shared infrastructure (like VPCs, networks, or databases) managed by other teams

You can use the [Terraform provider](/registry/packages/terraform) functions to reference output values from a Terraform state source:

* For local state files, use [`terraform.state.getLocalReference`](/registry/packages/terraform/api-docs/state/getlocalreference)
* For state files stored in a remote backend — HCP Terraform, Terraform Enterprise, or [Pulumi Cloud](/docs/iac/get-started/terraform/terraform-state-backend/) — use [`terraform.state.getRemoteReference`](/registry/packages/terraform/api-docs/state/getremotereference/#terraform-state-getremotereference)

The following code reads VPC and subnet IDs from a local `terraform.tfstate` file and provisions an EKS cluster that uses the read IDs:

{{< example-program path="tf-state-ref" >}}

### Converting Terraform HCL to Pulumi

The Pulumi CLI can convert existing Terraform source code written in the HashiCorp Configuration Language (HCL) into Pulumi source code using the `pulumi convert` command.

If you're coming to Pulumi from CDKTF, you can generate the HCL for the stacks in your project with `cdktf synth`:

```bash
cdktf synth --hcl
```

This produces a single HCL file for each stack at `./cdktf.out/stacks/<stack-name>/cdk.tf`.

#### Using the converter

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

#### Supported Terraform features

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

#### Importing resources

The `convert` command translates static HCL source code into Pulumi program code. Often, however, you'll also need to import existing resource state from your Terraform or CDKTF project in order to begin managing those resources with Pulumi.

To do so, you can use `pulumi import --from terraform`:

```bash
pulumi import --from terraform ./terraform.tfstate
```

Given a path to a valid `.tfstate` file and a target Pulumi stack, Pulumi will import the resources defined in that file into the stack and mark them [protected](/docs/iac/concepts/resources/options/protect/) to allow you to make follow-up changes to their source code safely. You can also import resources individually using the [`import`](https://www.pulumi.com/docs/iac/concepts/resources/options/import/) resource option.

Two converters can read a state file, selected with `--from`, and the choice follows the same rule as it does for [`pulumi convert`](/docs/iac/get-started/terraform/convert-hcl/#automated-conversion-with-pulumi-convert):

* `--from terraform` reads the state file on its own, so it works from a Pulumi project in any language. Reach for it after converting your configuration to a general-purpose language, as above.
* `--from hcl` parses the `.tf` files in the project directory alongside the state file. Reach for it when you are [running those `.tf` files under `runtime: hcl`](#keep-your-code-in-hcl).

To learn more about importing resources with Pulumi, see [Importing Resources](/docs/iac/guides/migration/import/).

#### Conversion examples

To help make migration from Terraform and CDKTF more approachable, we've prepared the following examples for reference:

* [Converting Full Terraform Programs to Pulumi](/blog/converting-full-terraform-programs-to-pulumi/): A blog post that covers the process of converting a real-world Terraform codebase
* [Migrating from CDKTF to Pulumi](https://github.com/pulumi/cdktf-to-pulumi-example): An end-to-end example that covers converting and importing a multi-stack CDKTF project

### Using Terraform modules directly

Pulumi allows you to use existing Terraform modules directly in your Pulumi programs without converting or rewriting them. This feature is particularly useful for:

* Organizations with significant investment in custom Terraform modules
* Teams that want to leverage the vast ecosystem of modules in the Terraform Registry
* Gradual migration scenarios where some teams continue using Terraform while others adopt Pulumi
* Maintaining consistency across infrastructure while transitioning between tools

#### Adding a Terraform module to your Pulumi project

To use a Terraform module in Pulumi, you can add it to your project using the `pulumi package add` command:

```bash
pulumi package add hcl module <module-source> [<version>]
```

For example, to add the AWS VPC module from the Terraform Registry:

```bash
pulumi package add hcl module terraform-aws-modules/vpc/aws 5.19.0
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
pulumi package add hcl module ./path/to/module
```

For more information about using Terraform modules directly in Pulumi, see the [Use a Terraform Module in Pulumi](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) guide.
