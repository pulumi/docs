---
title_tag: "Migration Best Practices"
meta_desc: Practical guidance for real-world infrastructure migrations to Pulumi, including finding IDs, handling diffs, and using AI-assisted tools.
title: Best practices
h1: Migration best practices in the real world
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Best Practices
        parent: iac-guides-migration
        weight: 1
---

Pulumi's migration tools ([converters](/docs/iac/guides/migration/converters/), [`pulumi import`](/docs/iac/cli/commands/pulumi_import/), the [`import` resource option](/docs/iac/concepts/resources/options/import/), and [visual import](/docs/insights/discovery/visual-import/)) provide powerful building blocks for bringing existing infrastructure under Pulumi's management. However, real-world migrations involve challenges that go beyond running a single command.

This guide provides an opinionated path through real-world migrations. The goal is **zero downtime and zero resource recreation**. Your infrastructure should continue running exactly as-is while ownership transfers to Pulumi.

{{% notes type="info" %}}
[Pulumi Neo](/docs/ai/) can handle this entire workflow automatically. It understands these best practices, reacts to problems, and iterates until your preview is clean. This is faster and requires far less toil than doing it manually. See [AI-assisted migration](#ai-assisted-migration) for details.
{{% /notes %}}

## The golden path: incremental migration

The safest migration approach is **incremental**: migrate one logical group of resources at a time, verify each group before proceeding, and maintain the ability to roll back.

### Recommended workflow

1. **Start with low-risk resources**: Begin with stateless or easily-recreatable resources (DNS records, IAM policies, security groups) before tackling databases or production compute.

1. **Migrate one environment first**: Import into dev, iterate until the preview is clean, then repeat for staging and prod. This reveals parameterization needs early.

1. **Coexist during transition**: Use [stack references](/docs/iac/concepts/stack/#stackreferences) and [external state references](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/#referencing-terraform-state) to connect Pulumi-managed resources with resources still in the original tool.

1. **Verify at each step**: After every import, run `pulumi preview` and confirm zero changes before proceeding. Any diff is a signal to stop and investigate.

1. **Retire the old tool last**: Only delete resources from Terraform state or CloudFormation stacks after Pulumi successfully manages them with clean previews.

### Choosing your import approach

Pulumi offers multiple ways to import resources. The best approach depends on whether you have source templates to convert.

**Convert + Import (recommended when you have source templates)**

If you're migrating from Terraform, ARM, Bicep, CloudFormation, or Kubernetes YAML, convert the templates first. Converted code preserves structure better than import-generated code.

For Terraform:

```bash
# 1. Convert HCL to Pulumi code
pulumi convert --from terraform --language typescript

# 2. Import state without generating conflicting code
pulumi import --from terraform ./terraform.tfstate --generate-code=false

# 3. Preview and iterate until clean
pulumi preview --diff
```

For ARM, CloudFormation, or Kubernetes:

```bash
# 1. Convert templates to Pulumi code
pulumi convert --from arm --language typescript  # or cloudformation, kubernetes

# 2. Create import file with resource IDs from your cloud
# 3. Import state
pulumi import --file import.json --generate-code=false

# 4. Preview and iterate until clean
pulumi preview --diff
```

The `--generate-code=false` flag is important: it imports state without generating code that conflicts with your converted code.

**Import only (when you don't have source templates)**

For CDK migrations or ad-hoc resources without source IaC, let `pulumi import` generate code for you:

```bash
# Import generates both code and state
pulumi import aws:s3/bucket:Bucket my-bucket bucket-name
```

For CDK, list resources from the CloudFormation stack that CDK deployed:

```bash
aws cloudformation list-stack-resources --stack-name my-cdk-stack
```

Then import each resource. The generated code won't have the same structure as your CDK constructs, but you can refactor it into components afterward.

**Preserving construct/module structure**

If you want to preserve Terraform modules or CDK constructs as Pulumi components, see [Importing into components](#importing-into-components) below. This is an advanced optimization you can do after the basic import works.

### Testing converted code before importing

When using `pulumi convert` to migrate from Terraform, CloudFormation, or ARM, consider testing the generated code on a fresh stack before importing existing resources:

1. Convert your source code to Pulumi
1. Create a temporary test stack: `pulumi stack init test`
1. Run `pulumi up` to deploy fresh infrastructure
1. Verify everything works as expected
1. Destroy the test stack: `pulumi destroy && pulumi stack rm test`
1. Now import your real resources with confidence

This catches code errors, missing dependencies, and conversion issues before you touch production infrastructure. It's particularly valuable when:

- You're converting complex modules or nested stacks
- The source code uses features that may not convert perfectly
- You want to verify the code compiles and runs before importing

**Skip this step when**:

- Resources have globally unique names that would conflict
- Creating duplicate infrastructure is costly or time-consuming
- You're importing directly without conversion (no generated code to test)
- Resources involve data that can't be duplicated (databases, storage with data)

### One-at-a-time vs bulk import

You can import resources individually or in bulk using an import file. Each approach has tradeoffs:

**One-at-a-time** (recommended for learning):

```bash
pulumi import aws:s3/bucket:Bucket my-bucket my-bucket-name
```

- Know exactly which resource caused a failure
- Easier to debug ID format issues
- Clear recovery point if something goes wrong
- Best for your first migration or unfamiliar resource types

**Bulk import** (recommended once comfortable):

```bash
pulumi import --file import.json
```

Where `import.json` contains:

```json
{
    "resources": [
        {
            "type": "aws:s3/bucket:Bucket",
            "name": "my-bucket",
            "id": "my-bucket-name"
        },
        {
            "type": "aws:s3/bucketPolicy:BucketPolicy",
            "name": "my-bucket-policy",
            "id": "my-bucket-name"
        }
    ]
}
```

- Faster for large migrations
- Harder to pinpoint failures
- Partial state is harder to recover from
- Best when you're confident in the ID formats and resource types

**When bulk importing, group resources by dependency layer**: import VPCs before subnets, subnets before instances. If a bulk import fails partway through, check which resources made it into state with `pulumi stack export` and remove already-imported resources from your import file before retrying.

### What to avoid

- **Big bang migrations**: Converting everything at once leaves you with too many variables when something goes wrong.
- **Skipping verification**: Never assume an import worked. Always run preview and confirm no changes.
- **Deleting source state early**: Keep your Terraform state or CloudFormation stacks intact until Pulumi fully owns the resources.
- **Refactoring while migrating**: Get the migration working first, then optimize. Trying to improve code structure, switch providers, or clean up resources during the initial import creates compound problems. Decouple these concerns.
- **Quitting early**: Iterate until your preview is completely clean—no diffs, no updates, no replacements. "Close enough" isn't good enough when the goal is zero disruption.

## Planning your target structure

Before importing resources, design how your Pulumi project should be organized. Migration tools import resources and generate code, but they don't organize that code for long-term maintainability.

### Consolidating multiple source states

If you have separate Terraform workspaces, CloudFormation stacks, or ARM deployments for each environment, you're probably maintaining near-duplicate configurations with subtle differences. This leads to copy-paste errors when promoting changes, drift between environments that's hard to detect, and no clear way to see what actually differs.

Migration is an opportunity to consolidate into a single Pulumi project with multiple stacks:

```
my-infrastructure/
├── Pulumi.yaml              # Project definition
├── Pulumi.dev.yaml          # Dev stack configuration
├── Pulumi.staging.yaml      # Staging stack configuration
├── Pulumi.prod.yaml         # Production stack configuration
├── index.ts                 # Shared infrastructure code
└── ...
```

You'll go from maintaining N copies of similar infrastructure to maintaining one codebase where environment-specific values come from configuration files, not duplicated code.

**Identify what varies between environments**:

- Resource names and tags
- Instance sizes and counts
- Network ranges
- Feature flags (e.g., debug logging in dev)

**Extract these to configuration**:

```typescript
const config = new pulumi.Config();
const environment = pulumi.getStack();  // "dev", "staging", or "prod"

// Required config (deployment fails if missing)
const dbInstanceClass = config.require("dbInstanceClass");

// Optional config with defaults
const enableDebugLogs = config.getBoolean("enableDebugLogs") ?? false;

// Environment-based naming
const bucket = new aws.s3.Bucket("data", {
    bucket: `mycompany-data-${environment}`,
    // ...
});
```

With this structure, a single PR promotes changes to all environments, configuration files make differences explicit, and IDE support catches errors before deployment.

### Code organization

Converters typically output a single file. For maintainability, split resources into logical groups:

```
my-infrastructure/
├── index.ts           # Main entry point, exports
├── network.ts         # VPC, subnets, security groups
├── database.ts        # RDS, ElastiCache
├── compute.ts         # ECS, Lambda, EC2
└── dns.ts             # Route53, certificates
```

**Preserve structure from your source**: If your original Terraform modules, CloudFormation nested stacks, or CDK constructs had a logical organization, preserve it in Pulumi. The original authors were probably thoughtful about this structure. Map Terraform modules and CDK constructs to [Pulumi components](/docs/iac/concepts/resources/components/)—these are reusable abstractions that encapsulate related resources and can be shared across projects.

Because Pulumi uses general-purpose languages, you can use functions and classes for abstraction, loops and conditionals that work naturally, and components to encapsulate patterns your team uses repeatedly.

You can do this refactoring after migration. The first priority is getting resources imported cleanly—start with the generated code, then progressively improve the structure without changing the underlying infrastructure.

### Importing into components

CDK constructs and Terraform modules encapsulate multiple leaf resources. When you list resources from CloudFormation or Terraform state, you see the physical resources (like `MyVpc/PublicSubnet1/Subnet`), not the abstractions. To preserve these abstractions as Pulumi components, you have two options.

**Option 1: Import first, then refactor into components**

This is the simpler approach. Import resources flat, then reorganize:

1. Import resources using the approaches above
2. Create a component class and move resources inside it
3. Add aliases to indicate the resources used to be at the root level:

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
class MyVpc extends pulumi.ComponentResource {
    public vpc: aws.ec2.Vpc;

    constructor(name: string, opts?: pulumi.ComponentResourceOptions) {
        super("myinfra:network:MyVpc", name, {}, opts);

        // Resource was imported at root, now under this component
        this.vpc = new aws.ec2.Vpc(`${name}-vpc`, {
            cidrBlock: "10.0.0.0/16",
        }, {
            parent: this,
            aliases: [{ parent: pulumi.rootStackResource }],
        });

        this.registerOutputs();
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
class MyVpc(pulumi.ComponentResource):
    def __init__(self, name: str, opts: Optional[pulumi.ResourceOptions] = None):
        super().__init__("myinfra:network:MyVpc", name, {}, opts)

        # Resource was imported at root, now under this component
        self.vpc = aws.ec2.Vpc(
            f"{name}-vpc",
            cidr_block="10.0.0.0/16",
            opts=pulumi.ResourceOptions(
                parent=self,
                aliases=[pulumi.Alias(parent=None)],
            ),
        )

        self.register_outputs({})
```

{{% /choosable %}}

{{% choosable language go %}}

```go
type MyVpc struct {
    pulumi.ResourceState
    Vpc *ec2.Vpc
}

func NewMyVpc(ctx *pulumi.Context, name string, opts ...pulumi.ResourceOption) (*MyVpc, error) {
    component := &MyVpc{}
    err := ctx.RegisterComponentResource("myinfra:network:MyVpc", name, component, opts...)
    if err != nil {
        return nil, err
    }

    // Resource was imported at root, now under this component
    component.Vpc, err = ec2.NewVpc(ctx, name+"-vpc", &ec2.VpcArgs{
        CidrBlock: pulumi.String("10.0.0.0/16"),
    }, pulumi.Parent(component), pulumi.Aliases([]pulumi.Alias{{Parent: pulumi.RootStackResource}}))
    if err != nil {
        return nil, err
    }

    return component, nil
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
class MyVpc : ComponentResource
{
    public Vpc Vpc { get; private set; }

    public MyVpc(string name, ComponentResourceOptions? opts = null)
        : base("myinfra:network:MyVpc", name, opts)
    {
        // Resource was imported at root, now under this component
        Vpc = new Vpc($"{name}-vpc", new VpcArgs
        {
            CidrBlock = "10.0.0.0/16",
        }, new CustomResourceOptions
        {
            Parent = this,
            Aliases = { new Alias { Parent = Pulumi.Deployment.Instance.Stack } },
        });

        RegisterOutputs();
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

**Option 2: Import directly into component hierarchy**

If you write your component code first, you can import directly into the hierarchy using an import file with parent references:

```json
{
    "nameTable": {
        "network": "urn:pulumi:prod::myproject::myinfra:network:MyVpc::network"
    },
    "resources": [
        {
            "type": "aws:ec2/vpc:Vpc",
            "name": "network-vpc",
            "id": "vpc-0abc123",
            "parent": "network"
        }
    ]
}
```

This requires the parent component to already exist in state or be defined in your code.

**Identifying construct/module boundaries**: The logical resource IDs often encode the hierarchy. CloudFormation shows paths like `MyVpc/PublicSubnet1/Subnet`, and Terraform state shows `module.vpc.aws_subnet.public[0]`. Use these to determine which physical resources belong together.

## Finding resource IDs

Every import requires a resource ID. Finding these IDs varies by source.

### From Terraform state

Use `pulumi import --from terraform` to read IDs directly from state:

```bash
pulumi import --from terraform ./terraform.tfstate
```

This generates an import file with IDs pre-populated. If you need to inspect the state manually:

```bash
# List all resources with IDs
terraform show -json | jq '.values.root_module.resources[] | {type: .type, name: .name, id: .values.id}'
```

### From CloudFormation (including CDK)

AWS CDK deploys through CloudFormation, so the same approach works for CDK applications.

Extract physical resource IDs from your stack:

```bash
# List all resources in a stack
aws cloudformation list-stack-resources --stack-name my-stack \
    --query 'StackResourceSummaries[].{Type:ResourceType,Logical:LogicalResourceId,Physical:PhysicalResourceId}' \
    --output table
```

The `PhysicalResourceId` is what you need for Pulumi import.

### From Azure Resource Manager

Get resource IDs from your resource group:

```bash
# List all resources
az resource list --resource-group my-rg \
    --query '[].{Name:name,Type:type,Id:id}' \
    --output table
```

Azure resource IDs are full ARM paths: `/subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Storage/storageAccounts/{name}`

### From cloud consoles and CLIs

When migrating infrastructure that wasn't managed by IaC:

**AWS**:

```bash
# EC2 instances
aws ec2 describe-instances \
    --query 'Reservations[].Instances[].{Name:Tags[?Key==`Name`].Value|[0],Id:InstanceId}' \
    --output table

# S3 buckets (ID is the bucket name)
aws s3 ls

# RDS instances
aws rds describe-db-instances \
    --query 'DBInstances[].DBInstanceIdentifier' \
    --output table
```

**Azure**:

```bash
# All resources in a subscription
az resource list --query '[].{Name:name,Type:type,Id:id}' --output table
```

**Google Cloud**:

```bash
# Compute instances
gcloud compute instances list --format='table(name,zone,selfLink)'
```

### Using Pulumi Insights

[Pulumi Insights](/docs/insights/) discovers resources across your cloud accounts. The [visual import](/docs/insights/discovery/visual-import/) feature lets you browse resources and generate import commands directly from the Pulumi Cloud console.

## Mapping to Pulumi types

Each resource needs a Pulumi type token. The [Pulumi Registry](/registry/) documents every resource's type token and expected ID format in its **Import** section.

### Type token format

Type tokens follow the pattern `provider:module/resource:Resource`:

```bash
pulumi import aws:s3/bucket:Bucket my-bucket my-bucket-name
#            └─────────┬────────┘ └───┬───┘ └─────┬──────┘
#               type token         name      ID value
```

### Provider selection

For AWS, Azure, and Google Cloud, Pulumi offers classic providers (Terraform-based) and native providers (direct API-based):

| Cloud | Classic | Native |
|-------|---------|--------|
| AWS | `aws` | `aws-native` |
| Azure | `azure` | `azure-native` |
| Google Cloud | `gcp` | `google-native` |

**Recommendation**: Use **classic providers** for migrations. They have broader resource coverage and closer type mappings to Terraform.

Use native providers when you need same-day support for new cloud features or direct API parity.

### Mapping from source types

**Terraform to Pulumi**: Replace underscores with slashes and use camelCase:

- `aws_s3_bucket` → `aws:s3/bucket:Bucket`
- `azurerm_virtual_network` → `azure:network/virtualNetwork:VirtualNetwork`

**CloudFormation to AWS Native**: Drop "AWS::" and adjust casing:

- `AWS::S3::Bucket` → `aws-native:s3:Bucket`
- `AWS::Lambda::Function` → `aws-native:lambda:Function`

**ARM to Azure Native**: Convert the resource type path:

- `Microsoft.Storage/storageAccounts` → `azure-native:storage:StorageAccount`

### ID format reference

ID formats vary by resource. Common patterns:

| Resource | ID Format | Example |
|----------|-----------|---------|
| AWS S3 Bucket | Bucket name | `my-bucket` |
| AWS EC2 Instance | Instance ID | `i-1234567890abcdef0` |
| AWS IAM Role | Role name | `my-role` |
| AWS RDS Instance | DB identifier | `my-database` |
| Azure resources | Full ARM path | `/subscriptions/.../storageAccounts/mystorage` |
| GCP Compute | Full self-link | `projects/my-proj/zones/us-central1-a/instances/my-vm` |

Always check the Registry's Import section. Getting the ID format wrong is a common source of "resource not found" errors.

## Achieving a clean preview

After importing, your goal is `pulumi preview` showing **zero changes**. This confirms Pulumi's view of the resource matches the cloud exactly, and no modifications will occur on `pulumi up`.

### Why previews show unexpected diffs

Diffs don't mean the import failed. They mean your code doesn't perfectly match the cloud's current state. Common causes:

**Over-specified properties**: Import captures every property, including cloud defaults. Remove properties that just restate defaults:

```typescript
// Generated code includes defaults
const bucket = new aws.s3.Bucket("my-bucket", {
    acl: "private",                    // This is the default, remove it
    forceDestroy: false,               // This is the default, remove it
    versioning: { enabled: false },    // This is the default, remove it
});

// Cleaned up
const bucket = new aws.s3.Bucket("my-bucket", {
    // Only specify non-default values
});
```

**Computed properties**: Properties set by the cloud shouldn't be in input code:

```typescript
// Remove these, they're outputs not inputs
const bucket = new aws.s3.Bucket("my-bucket", {
    arn: "arn:aws:s3:::my-bucket",         // Remove
    bucketDomainName: "...",               // Remove
    hostedZoneId: "Z3BJ4Q6RFIQJ6N",        // Remove
});
```

**Format mismatches**: The cloud may return values differently than your code specifies:

```typescript
// Cloud returns "STANDARD", your code says "standard"
storageClass: "standard",  // Change to "STANDARD"
```

### Example: resolving a diff

Here's what the iteration workflow looks like in practice. Running `pulumi preview --diff` shows:

```
~ aws:ec2/instance:Instance (update)
    [id=i-0abc123def456789]
    [urn=urn:pulumi:prod::infra::aws:ec2/instance:Instance::web-server]
  ~ tags: {
      ~ Environment: "production" => "Production"
    }
```

This diff tells you:

- The `~` means update (not create or delete)
- The `tags.Environment` value differs: cloud has `"Production"`, your code has `"production"`

**Fix**: Update your code to match the cloud's casing:

```typescript
// Before
tags: {
    Environment: "production",
},

// After
tags: {
    Environment: "Production",
},
```

Run `pulumi preview --diff` again. If clean, you're done with this resource. If more diffs appear, repeat until the preview shows no changes.

### Iteration workflow

1. **Run preview with diff**: `pulumi preview --diff` shows property-level differences.

1. **For each diff**, determine if you should:
   - **Remove the property** (it's a computed value or default)
   - **Adjust the value** (format mismatch)
   - **Accept the change** (rare, meaning you actually want to modify the resource)

1. **Update code and repeat** until preview shows no changes.

1. **Run `pulumi up`** only after achieving a clean preview.

**Using import output as validation**: When you run `pulumi import`, it generates code for the imported resources. If you converted code separately (from Terraform, CloudFormation, or CDK), prefer your converted code over the import-generated code—it preserves structure, abstractions, and logical groupings that import can't infer. However, compare the import output against your code to catch mistakes. Import-generated code is often over-specified with default values, but it can reveal properties you missed or got wrong.

If you suspect the cloud state changed since import, run `pulumi refresh` to update Pulumi's state from the cloud before iterating on your code.

### Critical: avoiding replacements

{{% notes type="warning" %}}
If preview shows a resource will be **replaced** (deleted and recreated), **stop immediately**. Replacements cause downtime and data loss.
{{% /notes %}}

Common causes of replacements:

- **Name changes**: Most cloud resources can't be renamed in-place. Ensure the Pulumi resource name generates the same physical name.
- **Immutable properties**: Some properties (like EC2 AMI, RDS engine, Lambda runtime) require replacement to change. Keep the original values.
- **Wrong import ID**: You may have imported a different resource than intended.

**Before proceeding with any replacement**:

1. Verify you're importing the correct resource
1. Check if the property is actually immutable
1. Consider if you need the change at all

For critical resources during migration, use [`protect`](/docs/iac/concepts/resources/options/protect/) to prevent accidental deletion:

```typescript
const database = new aws.rds.Instance("main", {
    // ...
}, { protect: true });
```

Remove `protect` only after you've confirmed everything works correctly.

## Common issues and solutions

### "Resource not found" during import

**Causes**:

- Wrong ID format (ARN vs name vs full path)
- Resource is in a different region than configured
- Resource was deleted

**Fix**: Check the Registry's Import section for correct ID format. Verify the resource exists and your provider configuration (region, subscription, project) is correct.

### "Resource already exists in state"

**Cause**: The resource is already managed by this Pulumi stack.

**Fix**: Check your state with `pulumi stack export`. If you need to re-import, first remove it: `pulumi state delete <urn>`.

### Converter produces `notImplemented` TODOs

**Cause**: The converter doesn't support a specific feature.

**Fix**: Manually implement the TODO. For Terraform modules you can't convert, use them directly via [Terraform module support](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/).

### Preview shows resources will be deleted

**Cause**: Resources in state but not in code.

**Fix**: Add the missing code, or use `pulumi state delete` to remove resources you intentionally want to stop managing (they'll remain in the cloud).

### Large state files timeout

**Fix**: Import in batches. Edit the generated import JSON to include subsets of resources, then run `pulumi import --file` multiple times.

## AI-assisted migration

Pulumi's AI tools understand migration challenges and can automate much of the complexity.

### Pulumi Neo

[Pulumi Neo](/docs/ai/) is an infrastructure automation agent that excels at migrations. Neo understands all of the best practices in this guide and follows them automatically. It reacts to problems (failed imports, unexpected diffs, partial failures) without manual intervention and iterates relentlessly until your preview is clean.

Point it at your repository and cloud account, and it will:

- Discover resources to migrate
- Map source types to Pulumi types
- Find correct resource IDs
- Generate code that preserves structure from your source
- Import resources in dependency order
- React to diffs and fix them automatically
- Iterate until previews are completely clean
- Parameterize for multiple environments

Neo handles the tedious parts of migration: looking up ID formats, debugging type mismatches, removing over-specified defaults, and retrying failed imports. It does this faster than a human and without the toil.

Neo works with human-in-the-loop approvals by default: before executing import commands or other state-changing operations, it asks for permission. You can set it to auto-approve if you prefer, but either way you stay in control of what happens to your infrastructure.

To use Neo, navigate to [Pulumi Cloud](https://app.pulumi.com), start a task, and describe your migration goal.

### MCP Server

The [Pulumi MCP Server](/docs/iac/guides/ai-integration/mcp-server/) brings migration capabilities to AI assistants like Claude Code, Cursor, Windsurf, and GitHub Copilot.

The MCP Server provides:

- **Resource discovery** across your cloud accounts
- **Registry lookups** for type tokens and ID formats
- **Neo delegation** for complex tasks

This lets you stay in your preferred development environment while accessing Pulumi's migration intelligence.

### When to use each approach

| Scenario | Recommended approach |
|----------|----------------------|
| Few resources, familiar with the cloud | `pulumi import` CLI |
| Converting existing IaC code | `pulumi convert` + manual cleanup |
| Large migration, many resources | Pulumi Neo |
| Migration help in your IDE | MCP Server with your AI assistant |
| Exploring what to migrate | Pulumi Insights visual import |

## Next steps

- [Import resources](/docs/iac/guides/migration/import/) - Detailed import command reference
- [Converters](/docs/iac/guides/migration/converters/) - Converting from Terraform, ARM, Kubernetes
- [Migrate from Terraform](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/) - Terraform-specific guidance
- [Migrate from CloudFormation](/docs/iac/guides/migration/migrating-to-pulumi/from-cloudformation/) - CloudFormation-specific guidance
- [Pulumi Neo](/docs/ai/) - AI-assisted infrastructure automation
- [MCP Server](/docs/iac/guides/ai-integration/mcp-server/) - AI integration for your favorite tools
