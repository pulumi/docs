---
title_tag: "Use a Terraform Module in Pulumi"
meta_desc: "Learn how to use existing Terraform modules directly in your Pulumi programs."
title: Use a Terraform Module in Pulumi
h1: Use a Terraform Module in Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Use a Terraform Module
        parent: iac-extending-pulumi
        weight: 6
aliases:
- /docs/iac/using-pulumi/extending-pulumi/use-terraform-module/
---

This guide will walk you through the process of using existing Terraform modules directly in your Pulumi programs, allowing you to leverage the vast Terraform module ecosystem.

{{< notes type="info" >}}
**Prerequisites:**

- The [Pulumi CLI](/docs/install/)
- One of Pulumi's [supported language runtimes](/docs/languages-sdks/) installed
- Access to a cloud provider account for deployment (e.g., AWS, Azure, Google Cloud)

{{< /notes >}}

## Why Use Terraform Modules in Pulumi?

Terraform has a mature ecosystem with thousands of modules available in the [Terraform Registry](https://registry.terraform.io/). These modules encapsulate well-tested infrastructure patterns that you might want to leverage in your Pulumi projects without having to rewrite them.

Also, many Terraform users have created their own custom modules and would like to avoid re-writing them in order to use Pulumi. Using Terraform modules directly within Pulumi allows you to use Terraform and Pulumi side-by-side, enabling the two technologies to coexist, taking a slower gentler migration path from Terraform to Pulumi. This is especially powerful in larger organizations, where some teams prefer Pulumi's workflows, and others prefer to continue using Terraform.

### Key benefits:

- **Leverage Existing Modules**: Use the rich ecosystem of Terraform modules directly in Pulumi.
- **Migrate Gradually**: Incrementally migrate from Terraform to Pulumi without rewriting everything at once.
- **Consistency**: Maintain consistency across teams that may be using a mix of Terraform and Pulumi.

## How It Works

Pulumi's Terraform Module provider allows you to consume Terraform modules as if they were native Pulumi packages. It works by:

1. Automatically installing and managing [OpenTofu](https://opentofu.org/) (an open-source Terraform-compatible implementation) to execute the module.
2. Translating Pulumi resource declarations to Terraform configurations.
3. Managing state through your standard Pulumi state backend.
4. Exposing module outputs as native Pulumi outputs.

## Getting Started

### Adding a Terraform Module to Your Pulumi Project

To use a Terraform module in Pulumi, first add it to your project using the `pulumi package add` command:

```bash
pulumi package add terraform-module <module-source> [<version>] <pulumi-package-name>
```

Where:

- `<module-source>` is either a registry module identifier (e.g. `terraform-aws-modules/rds/aws`) or a local path
- `<version>` is an optional version constraint (e.g. `3.5.0`)
- `<pulumi-package-name>` is the name you want to use for the Pulumi package

For example, to add the AWS VPC module from the Terraform Registry:

```bash
pulumi package add terraform-module terraform-aws-modules/vpc/aws 5.19.0 vpc
```

This will generate a local SDK in your programming language that you can import into your Pulumi program.

### Using a Local Terraform Module

You can also use local Terraform modules:

```bash
pulumi package add terraform-module ./path/to/module localmod
```

Any directory containing `.tf` files and optionally `variables.tf` and `outputs.tf` is considered a valid module.

## Example: Using the AWS RDS Module

Here's an example of how to use the AWS RDS module to provision a MySQL database in your Pulumi program.

First, start by installing the Terraform modules:

```bash
$ pulumi package add terraform-module terraform-aws-modules/vpc/aws 5.19.0 vpc
$ pulumi package add terraform-module terraform-aws-modules/rds/aws 6.10.0 rdsmod
```

After adding the packages, your `Pulumi.yaml` will be updated, and any necessary dependencies will be added to your project.

***Example:** Pulumi.yaml*

```yaml
name: rds-example
runtime:
  name: nodejs
  options:
    packagemanager: npm
packages:
  vpc:
    source: terraform-module
    version: 0.1.4
    parameters:
      - terraform-aws-modules/vpc/aws
      - 5.19.0
      - vpc
  rdsmod:
    source: terraform-module
    version: 0.1.4
    parameters:
      - terraform-aws-modules/rds/aws
      - 6.10.0
      - rdsmod
```

{{% chooser language "typescript,python,yaml" %}}

{{% choosable language typescript %}}

Since this was a TypeScript project, Pulumi generated a TypeScript SDK for the modules, making those available to use as `@pulumi/vpcmod` and `@pulumi/rdsmod` respectively. We can now use the Terraform modules directly in our TypeScript code:

***Example:** index.ts - Using the Terraform VPC and RDS module in a Pulumi program*

```typescript
import * as vpcmod from '@pulumi/vpcmod';
import * as pulumi from '@pulumi/pulumi';
import * as rdsmod from '@pulumi/rdsmod';
import * as aws from '@pulumi/aws';
import * as std from '@pulumi/std';

// Get available availability zones
const azs = aws.getAvailabilityZonesOutput({
  filters: [{
        name: "opt-in-status",
        values: ["opt-in-not-required"],
    }]
}).names.apply(names => names.slice(0, 3));

const cidr = "10.0.0.0/16";

const cfg = new pulumi.Config();
const prefix = cfg.get("prefix") ?? pulumi.getStack();

// Create a VPC using the terraform-aws-modules/vpc module
const vpc = new vpcmod.Module("test-vpc", {
  azs: azs,
  name: `test-vpc-${prefix}`,
  cidr,
  public_subnets: azs.apply(azs => azs.map((_, i) => {
    return getCidrSubnet(cidr, i+1);
  })),
  private_subnets: azs.apply(azs => azs.map((_, i) => {
    return getCidrSubnet(cidr, i+1+4);
  })),
  database_subnets: azs.apply(azs => azs.map((_, i) => {
    return getCidrSubnet(cidr, i+1 + 8);
  })),
  create_database_subnet_group: true,
});

// Create a security group for the RDS instance
const rdsSecurityGroup = new aws.ec2.SecurityGroup('test-rds-sg', {
  vpcId: vpc.vpc_id.apply(id => id!),
});

new aws.vpc.SecurityGroupIngressRule('test-rds-sg-ingress', {
  ipProtocol: 'tcp',
  securityGroupId: rdsSecurityGroup.id,
  cidrIpv4: vpc.vpc_cidr_block.apply(cidr => cidr!),
  fromPort: 3306,
  toPort: 3306,
});

// Create an RDS instance using the terraform-aws-modules/rds module
new rdsmod.Module("test-rds", {
  engine: "mysql",
  identifier: `test-rds-${prefix}`,
  manage_master_user_password: true,
  publicly_accessible: false,
  allocated_storage: 20,
  max_allocated_storage: 100,
  instance_class: "db.t4g.large",
  engine_version: "8.0",
  family: "mysql8.0",
  db_name: "completeMysql",
  username: "complete_mysql",
  port: '3306',
  multi_az: true,
  db_subnet_group_name: vpc.database_subnet_group_name.apply(name => name!),
  vpc_security_group_ids: [rdsSecurityGroup.id],
  skip_final_snapshot: true,
  deletion_protection: false,
  create_db_option_group: false,
  create_db_parameter_group: false,
});

// Utility function to calculate subnet CIDRs
function getCidrSubnet(cidr: string, netnum: number): pulumi.Output<string> {
    return std.cidrsubnetOutput({
    input: cidr,
    newbits: 8,
    netnum,
  }).result;
}
```

{{% /choosable %}}

{{% choosable language python %}}

Since this was a Python project, Pulumi generated a Python SDK for the modules, making those available to use as `pulumi_vpcmod` and `pulumi_rdsmod` respectively. We can now use the Terraform modules directly in our code:

```python
import pulumi
import pulumi_aws as aws
import pulumi_vpcmod as vpcmod
import pulumi_rdsmod as rdsmod
import pulumi_std as std

# Get available availability zones
azs = aws.get_availability_zones_output(
    filters=[{
        "name": "opt-in-status",
        "values": ["opt-in-not-required"],
    }]
).names.apply(lambda names: names[:3])

cidr = "10.0.0.0/16"

cfg = pulumi.Config()
prefix = cfg.get("prefix") or pulumi.get_stack()

# Utility function to calculate subnet CIDRs
def get_cidr_subnet(cidr, netnum):
    return std.cidrsubnet_output(
        input=cidr,
        newbits=8,
        netnum=netnum
    ).result

# Create a VPC using the terraform-aws-modules/vpc module
vpc = vpcmod.Module("test-vpc",
    azs=azs,
    name=f"test-vpc-{prefix}",
    cidr=cidr,
    public_subnets=azs.apply(lambda azs: [get_cidr_subnet(cidr, i+1) for i in range(len(azs))]),
    private_subnets=azs.apply(lambda azs: [get_cidr_subnet(cidr, i+1+4) for i in range(len(azs))]),
    database_subnets=azs.apply(lambda azs: [get_cidr_subnet(cidr, i+1+8) for i in range(len(azs))]),
    create_database_subnet_group=True
)

# Create a security group for the RDS instance
rds_security_group = aws.ec2.SecurityGroup('test-rds-sg',
    vpc_id=vpc.vpc_id
)

aws.vpc.SecurityGroupIngressRule('test-rds-sg-ingress',
    ip_protocol='tcp',
    security_group_id=rds_security_group.id,
    cidr_ipv4=vpc.vpc_cidr_block,
    from_port=3306,
    to_port=3306
)

# Create an RDS instance using the terraform-aws-modules/rds module
rdsmod.Module("test-rds",
    engine="mysql",
    identifier=f"test-rds-{prefix}",
    manage_master_user_password=True,
    publicly_accessible=False,
    allocated_storage=20,
    max_allocated_storage=100,
    instance_class="db.t4g.large",
    engine_version="8.0",
    family="mysql8.0",
    db_name="completeMysql",
    username="complete_mysql",
    port='3306',
    multi_az=True,
    db_subnet_group_name=vpc.database_subnet_group_name,
    vpc_security_group_ids=[rds_security_group.id],
    skip_final_snapshot=True,
    deletion_protection=False,
    create_db_option_group=False,
    create_db_parameter_group=False
)
```

{{% /choosable %}}

{{% choosable language yaml %}}

When authoring in YAML, there's no need for Pulumi to generate a SDK. In the YAML you can reference the Terraform module by its schema token, which takes the format `<module-name>:index:Module`:

**Example:** Pulumi.yaml - Using an imported Terraform module in a Pulumi YAML program*

TODO expand this example to match TypeScript above.

```yaml
resources:
  my-rds:
    type: rdsmod:index:Module
    properties:
      engine: mysql
      identifier: my-rds-instance
      manage_master_user_password: true
      # other properties...
```

{{% /choosable %}}

{{% /chooser %}}

In the above code, the imported Terraform module works the same as any other Pulumi code. Outputs are returned, and resource state is stored in your Pulumi state storage, alongside all your other Pulumi-native resources. This also means that resource dependencies work as expected between Pulumi-native resources and resources created by Terraform modules.

## Configuring Terraform Providers

Some modules require Terraform providers to be configured with specific settings. You can configure these providers from within Pulumi:

{{% chooser language "typescript" %}}

{{% choosable language typescript %}}

**Example:** index.ts - Configuring the imported Terraform bucket module*

```typescript
import * as bucket from "@pulumi/bucket";

// Configure the AWS provider for the module
const provider = new bucket.Provider("test-provider", {
    aws: {
        "region": "us-west-2"
    }
});

// Use the provider with the module
const testBucket = new bucket.Module("test-bucket", {
    bucket: `${prefix}-test-bucket`
}, { provider: provider });
```

{{% /choosable %}}

{{% /chooser %}}

Provider configuration is module-specific, so refer to the module's documentation for available configuration options.

## Troubleshooting

### Fixing Invalid Relative Paths

When using modules that accept file paths, use absolute paths instead of relative paths.

**Example:** index.ts - Using absolute paths to reference external files*

```typescript
import * as path from "path";
import * as process from "process";

const pwd = process.cwd();

const lambdaModule = new lambda.Module("my-lambda", {
    source_path: `${pwd}/src/app.ts`,
});
```

This is important because the Terraform modules have a different working directory, to allow for relative import of other modules, which means during execution the working directory will be different. Using `process.cwd()` here captures the Pulumi working directory, which we then use to build an absolute path to the external file.

### Fixing Incorrect Output Types

If Pulumi infers an incorrect type for a module output, you can override it as documented in the [Config Reference](https://github.com/pulumi/pulumi-terraform-module/blob/main/docs/config-reference.md).

## Limitations

Current limitations include:

- Using the `transforms` resource option
- Targeted updates via `pulumi up --target ...`
- Protecting individual resources deployed by the module

## Conclusion

Using Terraform modules directly in Pulumi allows you to leverage the vast ecosystem of Terraform modules and your existing investments into custom modules, while maintaining all the benefits of Pulumi's rich programming model. This approach enables the two products to coexist, allowing teams continue to collaborate while using the best tools for their specific needs, and enables a gradual migration path from Terraform to Pulumi.
