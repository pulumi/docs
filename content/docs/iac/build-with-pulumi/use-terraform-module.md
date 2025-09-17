---
title_tag: "Use a Terraform Module in Pulumi"
meta_desc: "Learn how to use existing Terraform modules directly in your Pulumi programs."
title: Use a Terraform Module in Pulumi
h1: Use a Terraform Module in Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Use a Terraform Module
        parent: iac-build-with-pulumi
        weight: 50
aliases:
- /docs/iac/using-pulumi/extending-pulumi/use-terraform-module/
- /docs/iac/extending-pulumi/use-terraform-module/
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

{{% notes type="tip" %}}
See [Local Packages](./local-packages.md) for details on generating and using SDKs from local or parameterized providers.
{{% /notes %}}

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

**Example:** Pulumi.yaml*

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

{{% chooser language "typescript,python,go,csharp,java,yaml" %}}

{{% choosable language typescript %}}

Since this was a TypeScript project, Pulumi generated a TypeScript SDK for the modules, making those available to use as `@pulumi/vpcmod` and `@pulumi/rdsmod` respectively. We can now use the Terraform modules directly in our TypeScript code.

**Example:** index.ts - Using the Terraform VPC and RDS module in a Pulumi program*

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

**Example:** `__main__.py` - Using the Terraform VPC and RDS module in a Pulumi program

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

{{% choosable language go %}}

**Example:** `main.go` - Using the Terraform VPC and RDS module in a Pulumi program

Since this was a Go project, Pulumi generated a Go SDK for the modules, making those available to use as `github.com/pulumi/pulumi-terraform-module/sdks/go/rdsmod/v6/rdsmod` and `github.com/pulumi/pulumi-terraform-module/sdks/go/vpcmod/v5/vpcmod`. We can now use the Terraform modules directly in our code:

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/vpc"
	"github.com/pulumi/pulumi-std/sdk/go/std"
	rdsmod "github.com/pulumi/pulumi-terraform-module/sdks/go/rdsmod/v6/rdsmod"
	vpcmod "github.com/pulumi/pulumi-terraform-module/sdks/go/vpcmod/v5/vpcmod"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func run(ctx *pulumi.Context) error {
	// Get available availability zones
	azs := aws.GetAvailabilityZonesOutput(ctx, aws.GetAvailabilityZonesOutputArgs{
		Filters: aws.GetAvailabilityZonesFilterArray{
			aws.GetAvailabilityZonesFilterArgs{
				Name:   pulumi.String("opt-in-status"),
				Values: pulumi.StringArray{pulumi.String("opt-in-not-required")},
			},
		},
	})

	azNames := azs.Names().ApplyT(func(names []string) []string {
		if len(names) > 3 {
			return names[:3]
		}
		return names
	}).(pulumi.StringArrayOutput)

	cidr := "10.0.0.0/16"
	cfg := config.New(ctx, "")
	prefix := cfg.Get("prefix")
	if prefix == "" {
		prefix = ctx.Stack()
	}

	// Create a VPC using the terraform-aws-modules/vpc module
	vpcInstance, err := vpcmod.NewModule(ctx, "test-vpc", &vpcmod.ModuleArgs{
		Azs:                          azNames,
		Name:                         pulumi.Sprintf("test-vpc-%s", prefix),
		Cidr:                         pulumi.String(cidr),
		Public_subnets:               applyAznamesForSubnet(ctx, azNames, cidr, 1),
		Private_subnets:              applyAznamesForSubnet(ctx, azNames, cidr, 5),
		Database_subnets:             applyAznamesForSubnet(ctx, azNames, cidr, 9),
		Create_database_subnet_group: pulumi.Bool(true),
	})
	if err != nil {
		return err
	}

	// Create a security group for the RDS instance
	rdsSecurityGroup, err := ec2.NewSecurityGroup(ctx, "test-rds-sg", &ec2.SecurityGroupArgs{
		VpcId: vpcInstance.Vpc_id,
	})
	if err != nil {
		return err
	}
	_, err = vpc.NewSecurityGroupIngressRule(ctx, "test-rds-sg-ingress", &vpc.SecurityGroupIngressRuleArgs{
		IpProtocol:      pulumi.String("tcp"),
		SecurityGroupId: rdsSecurityGroup.ID(),
		CidrIpv4:        vpcInstance.Vpc_cidr_block,
		FromPort:        pulumi.Int(3306),
		ToPort:          pulumi.Int(3306),
	})
	if err != nil {
		return err
	}

	// Create an RDS instance using the terraform-aws-modules/rds module
	_, err = rdsmod.NewModule(ctx, "test-rds", &rdsmod.ModuleArgs{
		Engine:                      pulumi.String("mysql"),
		Identifier:                  pulumi.Sprintf("test-rds-%s", prefix),
		Manage_master_user_password: pulumi.Bool(true),
		Publicly_accessible:         pulumi.Bool(false),
		Allocated_storage:           pulumi.Float64(20),
		Max_allocated_storage:       pulumi.Float64(100),
		Instance_class:              pulumi.String("db.t4g.large"),
		Engine_version:              pulumi.String("8.0"),
		Family:                      pulumi.String("mysql8.0"),
		Db_name:                     pulumi.String("completeMysql"),
		Username:                    pulumi.String("complete_mysql"),
		Port:                        pulumi.String("3306"),
		Multi_az:                    pulumi.Bool(true),
		Db_subnet_group_name:        vpcInstance.Database_subnet_group_name,
		Vpc_security_group_ids:      pulumi.StringArray{rdsSecurityGroup.ID()},
		Skip_final_snapshot:         pulumi.Bool(true),
		Deletion_protection:         pulumi.Bool(false),
		Create_db_option_group:      pulumi.Bool(false),
		Create_db_parameter_group:   pulumi.Bool(false),
	})
	return err
}

func applyAznamesForSubnet(
	ctx *pulumi.Context,
	azNames pulumi.StringArrayOutput,
	cidr string,
	offset int,
) pulumi.StringArrayOutput {
	return azNames.ApplyT(func(azs []string) ([]string, error) {
		subnets := make([]string, len(azs))
		for i := range azs {
			netnum := offset + i
			r, err := std.Cidrsubnet(ctx, &std.CidrsubnetArgs{
				Input:   cidr,
				Newbits: 8,
				Netnum:  netnum,
			})
			if err != nil {
				return nil, err
			}
			subnets[i] = r.Result
		}
		return subnets, nil
	}).(pulumi.StringArrayOutput)
}

func main() {
	pulumi.Run(run)
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

Since this was a C# project, Pulumi generated a C# SDK for the modules, making those available to use as `Pulumi.Rdsmod` and `Pulumi.Vpcmod`. We can now use the Terraform modules directly in our code:

**Example:** `Program.cs` - Using the Terraform VPC and RDS module in a Pulumi program

```csharp
using System;
using System.Linq;
using System.Threading.Tasks;
using System.Collections.Generic;
using System.Collections.Immutable;
using Pulumi;
using Aws = Pulumi.Aws;
using Rdsmod = Pulumi.Rdsmod;
using Std = Pulumi.Std;
using Vpcmod = Pulumi.Vpcmod;

return await Deployment.RunAsync(() =>
{
    // Get available availability zones
    var azs = Aws.GetAvailabilityZones.Invoke(new Aws.GetAvailabilityZonesInvokeArgs
    {
        Filters =
            {
                new Aws.Inputs.GetAvailabilityZonesFilterInputArgs
                {
                    Name = "opt-in-status",
                    Values = { "opt-in-not-required" }
                }
            }
    }).Apply(result => result.Names.Take(3).ToArray());

    var cidr = "10.0.0.0/16";

    var config = new Pulumi.Config();
    var prefix = config.Get("prefix") ?? Deployment.Instance.StackName;

    // Create a VPC using the terraform-aws-modules/vpc module
    var vpc = new Vpcmod.Module("test-vpc", new Vpcmod.ModuleArgs
    {
        Azs = azs,
        Name = Output.Format($"test-vpc-{prefix}"),
        Cidr = cidr,
        Public_subnets = Utils.Subnets(cidr, azs, 1),
        Private_subnets = Utils.Subnets(cidr, azs, 5),
        Database_subnets = Utils.Subnets(cidr, azs, 9),
        Create_database_subnet_group = true,
    });

    // Create a security group for the RDS instance
    var rdsSecurityGroup = new Aws.Ec2.SecurityGroup("test-rds-sg", new Aws.Ec2.SecurityGroupArgs
    {
        VpcId = vpc.Vpc_id.Apply(id => id ?? string.Empty),
    });

    _ = new Aws.Vpc.SecurityGroupIngressRule("test-rds-sg-ingress", new Aws.Vpc.SecurityGroupIngressRuleArgs
    {
        IpProtocol = "tcp",
        SecurityGroupId = rdsSecurityGroup.Id,
        CidrIpv4 = vpc.Vpc_cidr_block.Apply(x => x!),
        FromPort = 3306,
        ToPort = 3306,
    });

    // Create an RDS instance using the terraform-aws-modules/rds module
    _ = new Rdsmod.Module("test-rds", new Rdsmod.ModuleArgs
    {
        Engine = "mysql",
        Identifier = Output.Format($"test-rds-{prefix}"),
        Manage_master_user_password = true,
        Publicly_accessible = false,
        Allocated_storage = 20,
        Max_allocated_storage = 100,
        Instance_class = "db.t4g.large",
        Engine_version = "8.0",
        Family = "mysql8.0",
        Db_name = "completeMysql",
        Username = "complete_mysql",
        Port = "3306",
        Multi_az = true,
        Db_subnet_group_name = vpc.Database_subnet_group_name,
        Vpc_security_group_ids = { rdsSecurityGroup.Id },
        Skip_final_snapshot = true,
        Deletion_protection = false,
        Create_db_option_group = false,
        Create_db_parameter_group = false,
    });
});

// Utilities to calculate subnet CIDRs
internal class Utils {
    public static Output<ImmutableArray<string>> Subnets(string cidr, Output<string[]> azs, int offset) {
        return azs.Apply(names => Pulumi.Output.All(names.Select((_, i) => Utils.GetCidrSubnet(cidr, i + 1))));
    }

    public static Output<string> GetCidrSubnet(string cidr, int netnum)
    {
        return Std.Cidrsubnet.Invoke(new Std.CidrsubnetInvokeArgs
        {
            Input = cidr,
            Newbits = 8,
            Netnum = netnum
        }).Apply(result => result.Result);
    }
}
```

{{% /choosable %}}

{{% choosable language java %}}

Since this was a Java project, Pulumi generated a Java SDK for the modules, making those available to use as `com.pulumi.rdsmod` and `com.pulumi.vpcmod`. We can now use the Terraform modules directly in our code:

**Example:** `App.java` - Using the Terraform VPC and RDS module in a Pulumi program

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.AwsFunctions;
import com.pulumi.aws.inputs.GetAvailabilityZonesArgs;
import com.pulumi.aws.inputs.GetAvailabilityZonesFilterArgs;
import com.pulumi.std.StdFunctions;
import com.pulumi.aws.ec2.SecurityGroup;
import com.pulumi.aws.ec2.SecurityGroupArgs;
import com.pulumi.aws.vpc.SecurityGroupIngressRule;
import com.pulumi.aws.vpc.SecurityGroupIngressRuleArgs;
import com.pulumi.Config;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.List;
import java.util.Collections;

public class App {
    public static void stack(Context ctx) {

        // Get available availability zones
        final var azNames = AwsFunctions.getAvailabilityZones(GetAvailabilityZonesArgs.builder()
            .filters(GetAvailabilityZonesFilterArgs.builder()
                     .name("opt-in-status")
                     .values("opt-in-not-required")
                     .build())
            .build())
            .applyValue(result -> result.names().subList(0, 3));

        final var cidr = "10.0.0.0/16";
        final var prefix = ctx.config().get("prefix").orElse(ctx.stackName());

        // Create a VPC using the terraform-aws-modules/vpc module
        final var vpc = new com.pulumi.vpcmod.Module("test-vpc", com.pulumi.vpcmod.ModuleArgs.builder()
            .azs(azNames)
            .name("test-vpc-" + prefix)
            .cidr(cidr)
            .public_subnets(subnets(cidr, azNames, 1))
            .private_subnets(subnets(cidr, azNames, 5))
            .database_subnets(subnets(cidr, azNames, 9))
            .create_database_subnet_group(true)
            .build());

        final var rdsSecurityGroup = new SecurityGroup("test-rds-sg", SecurityGroupArgs.builder()
            .vpcId(vpc.vpc_id().applyValue(x -> x.get()))
            .build());

        new SecurityGroupIngressRule("test-rds-sg-ingress", SecurityGroupIngressRuleArgs.builder()
            .ipProtocol("tcp")
            .securityGroupId(rdsSecurityGroup.id())
            .cidrIpv4(vpc.vpc_cidr_block().applyValue(x -> x.get()))
            .fromPort(3306)
            .toPort(3306)
            .build());

        new com.pulumi.rdsmod.Module("test-rds", com.pulumi.rdsmod.ModuleArgs.builder()
            .engine("mysql")
            .identifier("test-rds-" + prefix)
            .manage_master_user_password(true)
            .publicly_accessible(false)
            .allocated_storage(20.0)
            .max_allocated_storage(100.0)
            .instance_class("db.t4g.large")
            .engine_version("8.0")
            .family("mysql8.0")
            .db_name("completeMysql")
            .username("complete_mysql")
            .port("3306")
            .multi_az(true)
            .db_subnet_group_name(vpc.database_subnet_group_name().applyValue(x -> x.get()))
            .vpc_security_group_ids(rdsSecurityGroup.id().applyValue(x -> Collections.singletonList(x)))
            .skip_final_snapshot(true)
            .deletion_protection(false)
            .create_db_option_group(false)
            .create_db_parameter_group(false)
            .build());
    }

    private static Output<List<String>> subnets(String cidr, Output<List<String>> azNames, int offset) {
        return azNames.apply(names -> Output.all(IntStream.range(0, names.size())
                                                 .mapToObj(i -> getCidrSubnet(cidr, i+offset))
                                                 .collect(Collectors.toList())));
    }

    private static Output<String> getCidrSubnet(String cidr, int netnum) {
        return StdFunctions.cidrsubnet(com.pulumi.std.inputs.CidrsubnetArgs.builder()
            .input(cidr)
            .newbits(8)
            .netnum(netnum)
            .build()).applyValue(x -> x.result());
    }

    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

When authoring in YAML, there is no need for Pulumi to generate a SDK. Pulumi generates some metadata instead:

```bash
$ ls sdks/vpcmod/
sdks/vpcmod/vpcmod-5.19.0.yaml
```

In the YAML you can reference the Terraform module by its schema token, which takes the format `<module-name>:index:Module`:

**Example:** `Pulumi.yaml` - Using the Terraform VPC and RDS module in a Pulumi program

```yaml
name: testproj-yaml
description: testproj-yaml
runtime: yaml
resources:
  testVpc:
    type: vpcmod:index:Module
    properties:
      name: test-vpc-${pulumi.stack}
      azs:
        - us-west-2a
        - us-west-2b
        - us-west-2c
      cidr: 10.0.0.0/16
      public_subnets:
        - 10.0.1.0/24
        - 10.0.2.0/24
        - 10.0.3.0/24
      private_subnets:
        - 10.0.5.0/24
        - 10.0.6.0/24
        - 10.0.7.0/24
      database_subnets:
        - 10.0.9.0/24
        - 10.0.10.0/24
        - 10.0.11.0/24
      create_database_subnet_group: true
  testRdsSg:
    type: aws:ec2:SecurityGroup
    properties:
      vpcId: ${testVpc.vpc_id}
  testRdsSgIngress:
    type: aws:vpc:SecurityGroupIngressRule
    properties:
      ipProtocol: tcp
      securityGroupId: ${testRdsSg.id}
      cidrIpv4: ${testVpc.vpc_cidr_block}
      fromPort: 3306
      toPort: 3306
  testRds:
    type: rdsmod:index:Module
    properties:
      engine: mysql
      identifier: test-rds-${pulumi.stack}
      manage_master_user_password: true
      publicly_accessible: false
      allocated_storage: 20
      max_allocated_storage: 100
      instance_class: db.t4g.large
      engine_version: 8
      family: mysql8.0
      db_name: completeMysql
      username: complete_mysql
      port: '3306'
      multi_az: true
      db_subnet_group_name: ${testVpc.database_subnet_group_name}
      vpc_security_group_ids:
        - ${testRdsSg.id}
      skip_final_snapshot: true
      deletion_protection: false
      create_db_option_group: false
      create_db_parameter_group: false
packages:
  rdsmod:
    source: terraform-module
    version: 0.1.7
    parameters:
      - terraform-aws-modules/rds/aws
      - 6.10.0
      - rdsmod
  vpcmod:
    source: terraform-module
    version: 0.1.7
    parameters:
      - terraform-aws-modules/vpc/aws
      - 5.19.0
      - vpcmod
```

{{% /choosable %}}

{{% /chooser %}}

In the above code, the imported Terraform module works the same as any other Pulumi code. Outputs are returned, and resource state is stored in your Pulumi state storage, alongside all your other Pulumi-native resources. This also means that resource dependencies work as expected between Pulumi-native resources and resources created by Terraform modules.

## Configuring Terraform Providers

Some modules require Terraform providers to be configured with specific settings. You can configure these providers from within Pulumi:

{{% chooser language "typescript,python,go,csharp,java" %}}

{{% choosable language typescript %}}

**Example:** `index.ts` - Configuring the imported Terraform bucket module

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

{{% choosable language python %}}

**Example:** `__main__.py` - Configuring the imported Terraform bucket module

```python
import pulumi
import pulumi_bucket as bucket

# Configure the AWS provider for the module
provider = bucket.Provider("bucket-provider", aws={
    "region": "us-west-2"
})

# Use the provider with the module
test_bucket = bucket.Module("test-bucket",
    bucket=f"${prefix}-test-bucket"
    opts=pulumi.ResourceOptions(provider=provider)
)
```

{{% /choosable %}}

{{% choosable language go %}}

**Example:** `main.go` - Configuring the imported Terraform bucket module

```go
package main

import (
	bucket "github.com/pulumi/pulumi-terraform-module/sdks/go/bucket/v3/bucket"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)


func run(ctx *pulumi.Context) error {
	// Configure the AWS provider for the module
	prov, err := bucket.NewProvider(ctx, "provider", &bucket.ProviderArgs{
		Aws: pulumi.ToMap(map[string]any{
			"region": "us-west-2",
		}),
	})
	if err != nil {
		return err
	}

	// Use the provider with the module
	bucketInstance, err := bucket.NewModule(ctx, "test-bucket", &bucket.ModuleArgs{
		Bucket: pulumi.Sprintf("test-vpc-%s", prefix),
	}, pulumi.Provider(prov))
	if err != nil {
		return err
	}
}

func main() {
	pulumi.Run(run)
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

**Example:** `Program.cs` - Configuring the imported Terraform bucket module

```csharp
using Pulumi;
using Bucket = Pulumi.Bucket;

return await Deployment.RunAsync(() =>
{
    // Configure the AWS provider for the module
    var provider = new Bucket.Provider("test-provider", new Bucket.ProviderArgs
    {
        Aws = {{"region", "us-west-2"}}
    });

    // Use the provider with the module
    var bucket = new Bucket.Module("test-bucket", new Bucket.Args
    {
        Bucket = $"{prefix}-test-bucket"
    }, new CustomResourceOptions
    {
        Provider = provider
    });
```

{{% /choosable %}}

{{% choosable language java %}}

**Example:** `App.java` - Configuring the imported Terraform bucket module

```java
import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.resources.CustomResourceOptions;

public class App {
    public static void stack(Context ctx) {

        // Configure the AWS provider for the module
        final var provider = new com.pulumi.bucket.Provider("test-provider",
            com.pulumi.bucket.ProviderArgs.builder()
            .aws(Collections.singletonMap("region", "us-west-2"))
            .build());

        // Use the provider with the module
        final var bucket = new com.pulumi.bucket.Module("test-bucket",
            com.pulumi.bucket.ModuleArgs.builder()
                .bucket(prefix+"-test-bucket")
                .build(),
            CustomResourceOptions.builder().provider(provider).build());
    }

    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }
}
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
