---
title_tag: Import Terraform Modules | Pulumi for Terraform Users
title: Import Terraform Modules
h1: "Import Terraform Modules"
meta_desc: Learn how to use existing Terraform modules directly in Pulumi programs, leveraging the Terraform Registry ecosystem.
weight: 5
menu:
    iac:
        name: Import Terraform Modules
        parent: terraform-get-started
        weight: 5

aliases:
- /docs/iac/get-started/terraform/terraform-modules/
---

## Leverage the module ecosystem

Pulumi can directly use existing Terraform modules from the Terraform Registry, private registries, or local sources.
This allows you to access thousands of existing modules without rewriting them in Pulumi.

## Add Terraform modules

Use the `pulumi package add` command to add Terraform modules to your project:

```bash
# Add a module from the Terraform Registry
$ pulumi package add terraform-module terraform-aws-modules/vpc/aws 6.0.0 vpc

# Add a local module
$ pulumi package add terraform-module ./path/to/module localmod
```

## Example: AWS VPC module

Let's use the popular AWS `vpc` module to create a VPC with subnets, and then deploy an EC2 instance in that VPC:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-modules-test && cd pulumi-terraform-modules-test
$ pulumi new aws-typescript --yes
```

Next, add the VPC module:

```bash
$ pulumi package add terraform-module terraform-aws-modules/vpc/aws 6.0.0 vpc
```

Then use it in your Pulumi program:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as vpc from "@pulumi/vpc";

// Use the Terraform VPC module
const myVpc = new vpc.Module("my-vpc", {
    name: "my-vpc",
    cidr: "10.0.0.0/16",

    azs: ["us-west-2a", "us-west-2b", "us-west-2c"],
    public_subnets: ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"],
    private_subnets: ["10.0.10.0/24", "10.0.11.0/24", "10.0.12.0/24"],

    enable_nat_gateway: true,
    enable_vpn_gateway: true,

    tags: {
        Terraform: "true",
        Environment: "dev",
    },
});

// Create a security group

const webSg = new aws.ec2.SecurityGroup("web-sg", {
    name: "web-sg",
    description: "Security group for web servers",
    vpcId: myVpc.vpc_id.apply(id => id!),
    ingress: [
        {
            description: "HTTP",
            fromPort: 80,
            toPort: 80,
            protocol: "tcp",
            cidrBlocks: ["0.0.0.0/0"],
        },
        {
            description: "SSH",
            fromPort: 22,
            toPort: 22,
            protocol: "tcp",
            cidrBlocks: ["0.0.0.0/0"],
        },
    ],
    egress: [
        {
            fromPort: 0,
            toPort: 0,
            protocol: "-1",
            cidrBlocks: ["0.0.0.0/0"],
        },
    ],
});

// Get the latest Amazon Linux 2 AMI
const amazonLinux = aws.ec2.getAmiOutput({
    mostRecent: true,
    owners: ["amazon"],
    filters: [
        {
            name: "name",
            values: ["amzn2-ami-hvm-*-x86_64-gp2"],
        },
    ],
});

// Create an EC2 instance in the VPC
const webServer = new aws.ec2.Instance("web-server", {
    ami: amazonLinux.id,
    instanceType: "t3.micro",
    subnetId: myVpc.public_subnets.apply(subnets => subnets![0]),
    vpcSecurityGroupIds: [webSg.id],
    associatePublicIpAddress: true,

    userData: `#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from Pulumi and Terraform modules!</h1>" > /var/www/html/index.html
`,

    tags: {
        Name: "web-server",
        Environment: "dev",
    },
});


// Output important information
export const vpcId = myVpc.vpc_id;
export const instanceId = webServer.id;
export const publicIp = webServer.publicIp;
export const websiteUrl = pulumi.interpolate`http://${webServer.publicIp}`;
```

{{% /choosable %}}

{{% choosable language "python" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-modules-test && cd pulumi-terraform-modules-test
$ pulumi new aws-python --yes
```

Next, add the VPC module:

```bash
$ pulumi package add terraform-module terraform-aws-modules/vpc/aws 6.0.0 vpc
```

Then use it in your Pulumi program:

```python
import pulumi
import pulumi_aws as aws
import pulumi_vpc as vpc

# Use the Terraform VPC module
my_vpc = vpc.Module("my-vpc",
    name="my-vpc",
    cidr="10.0.0.0/16",

    azs=["us-west-2a", "us-west-2b", "us-west-2c"],
    public_subnets=["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"],
    private_subnets=["10.0.10.0/24", "10.0.11.0/24", "10.0.12.0/24"],

    enable_nat_gateway=True,
    enable_vpn_gateway=True,

    tags={
        "Terraform": "true",
        "Environment": "dev",
    }
)

# Create a security group
web_sg = aws.ec2.SecurityGroup("web-sg",
    name="web-sg",
    description="Security group for web servers",
    vpc_id=my_vpc.vpc_id.apply(lambda id: id),
    ingress=[
        {
            "description": "HTTP",
            "from_port": 80,
            "to_port": 80,
            "protocol": "tcp",
            "cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "description": "SSH",
            "from_port": 22,
            "to_port": 22,
            "protocol": "tcp",
            "cidr_blocks": ["0.0.0.0/0"],
        },
    ],
    egress=[
        {
            "from_port": 0,
            "to_port": 0,
            "protocol": "-1",
            "cidr_blocks": ["0.0.0.0/0"],
        }
    ]
)

# Get the latest Amazon Linux 2 AMI
amazon_linux = aws.ec2.get_ami(
    most_recent=True,
    owners=["amazon"],
    filters=[
        {
            "name": "name",
            "values": ["amzn2-ami-hvm-*-x86_64-gp2"],
        }
    ]
)

# Create an EC2 instance in the VPC
web_server = aws.ec2.Instance("web-server",
    ami=amazon_linux.id,
    instance_type="t3.micro",
    subnet_id=my_vpc.public_subnets.apply(lambda subnets: subnets[0]),
    vpc_security_group_ids=[web_sg.id],
    associate_public_ip_address=True,

    user_data="""#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from Pulumi and Terraform modules!</h1>" > /var/www/html/index.html
""",

    tags={
        "Name": "web-server",
        "Environment": "dev",
    }
)

# Output important information
pulumi.export("vpcId", my_vpc.vpc_id)
pulumi.export("instanceId", web_server.id)
pulumi.export("publicIp", web_server.public_ip)
pulumi.export("websiteUrl", pulumi.Output.format("http://{0}", web_server.public_ip))
```

{{% /choosable %}}

{{% choosable language "go" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-modules-test && cd pulumi-terraform-modules-test
$ pulumi new aws-go --yes
```

Next, add the VPC module:

```bash
$ pulumi package add terraform-module terraform-aws-modules/vpc/aws 6.0.0 vpc
```

Then use it in your Pulumi program:

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	vpc "github.com/pulumi/pulumi-terraform-module/sdks/go/vpc/v6/vpc"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Use the Terraform VPC module
		myVpc, err := vpc.NewModule(ctx, "my-vpc", &vpc.ModuleArgs{
			Name: pulumi.String("my-vpc"),
			Cidr: pulumi.String("10.0.0.0/16"),

			Azs:             pulumi.StringArray{pulumi.String("us-west-2a"), pulumi.String("us-west-2b"), pulumi.String("us-west-2c")},
			Private_subnets: pulumi.StringArray{pulumi.String("10.0.1.0/24"), pulumi.String("10.0.2.0/24"), pulumi.String("10.0.3.0/24")},
			Public_subnets:  pulumi.StringArray{pulumi.String("10.0.10.0/24"), pulumi.String("10.0.11.0/24"), pulumi.String("10.0.12.0/24")},

			Enable_nat_gateway: pulumi.Bool(true),
			Enable_vpn_gateway: pulumi.Bool(true),

			Tags: pulumi.StringMap{
				"Terraform":   pulumi.String("true"),
				"Environment": pulumi.String("dev"),
			},
		})
		if err != nil {
			return err
		}

		// Get the latest Amazon Linux 2 AMI
		amazonLinux, err := ec2.LookupAmi(ctx, &ec2.LookupAmiArgs{
			MostRecent: pulumi.BoolRef(true),
			Owners:     []string{"amazon"},
			Filters: []ec2.GetAmiFilter{
				{
					Name:   "name",
					Values: []string{"amzn2-ami-hvm-*-x86_64-gp2"},
				},
			},
		})
		if err != nil {
			return err
		}

		// Create a security group
		webSg, err := ec2.NewSecurityGroup(ctx, "web-sg", &ec2.SecurityGroupArgs{
			Name:        pulumi.String("web-sg"),
			Description: pulumi.String("Security group for web servers"),
			VpcId:       myVpc.Vpc_id,
			Ingress: ec2.SecurityGroupIngressArray{
				&ec2.SecurityGroupIngressArgs{
					Description: pulumi.String("HTTP"),
					FromPort:    pulumi.Int(80),
					ToPort:      pulumi.Int(80),
					Protocol:    pulumi.String("tcp"),
					CidrBlocks:  pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
				&ec2.SecurityGroupIngressArgs{
					Description: pulumi.String("SSH"),
					FromPort:    pulumi.Int(22),
					ToPort:      pulumi.Int(22),
					Protocol:    pulumi.String("tcp"),
					CidrBlocks:  pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
			},
			Egress: ec2.SecurityGroupEgressArray{
				&ec2.SecurityGroupEgressArgs{
					FromPort:   pulumi.Int(0),
					ToPort:     pulumi.Int(0),
					Protocol:   pulumi.String("-1"),
					CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
			},
		})
		if err != nil {
			return err
		}

		// Create an EC2 instance in the VPC
		webServer, err := ec2.NewInstance(ctx, "web-server", &ec2.InstanceArgs{
			Ami:          pulumi.String(amazonLinux.Id),
			InstanceType: pulumi.String("t3.micro"),
			SubnetId: myVpc.Public_subnets.ApplyT(func(subnets []string) string {
				return subnets[0]
			}).(pulumi.StringOutput),
			VpcSecurityGroupIds:      pulumi.StringArray{webSg.ID()},
			AssociatePublicIpAddress: pulumi.Bool(true),

			UserData: pulumi.String(`#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from Pulumi and Terraform modules!</h1>" > /var/www/html/index.html
`),

			Tags: pulumi.StringMap{
				"Name":        pulumi.String("web-server"),
				"Environment": pulumi.String("dev"),
			},
		})
		if err != nil {
			return err
		}

		// Output important information
		ctx.Export("vpcId", myVpc.Vpc_id)
		ctx.Export("instanceId", webServer.ID())
		ctx.Export("publicIp", webServer.PublicIp)
		ctx.Export("websiteUrl", pulumi.Sprintf("http://%s", webServer.PublicIp))
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-modules-test && cd pulumi-terraform-modules-test
$ pulumi new aws-csharp --yes
```

Next, add the VPC module:

```bash
$ pulumi package add terraform-module terraform-aws-modules/vpc/aws 6.0.0 vpc
```

{{% notes type="tip" %}}
The `pulumi package add ...` command will add the required dependencies to the solution file, but you'll need to manually add the following directive:

```xml {hl_lines=[3]}
  <PropertyGroup>
    <!-- ... -->
    <DefaultItemExcludes>$(DefaultItemExcludes);sdks/**/*.cs</DefaultItemExcludes>
  </PropertyGroup>
```

{{% /notes %}}

Then use it in your Pulumi program:

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Vpc;

return await Deployment.RunAsync(() =>
{
    // Use the Terraform VPC module
    var myVpc = new Vpc("my-vpc", new VpcArgs
    {
        Name = "my-vpc",
        Cidr = "10.0.0.0/16",

        Azs = new[] { "us-west-2a", "us-west-2b", "us-west-2c" },
        PrivateSubnets = new[] { "10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24" },
        PublicSubnets = new[] { "10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24" },

        EnableNatGateway = true,
        EnableVpnGateway = true,

        Tags = new Dictionary<string, string>
        {
            ["Terraform"] = "true",
            ["Environment"] = "dev",
        },
    });

    // Get the latest Amazon Linux 2 AMI
    var amazonLinux = GetAmi.Invoke(new GetAmiInvokeArgs
    {
        MostRecent = true,
        Owners = new[] { "amazon" },
        Filters = new[]
        {
            new GetAmiFilterInputArgs
            {
                Name = "name",
                Values = new[] { "amzn2-ami-hvm-*-x86_64-gp2" },
            },
        },
    });

    // Create a security group
    var webSg = new SecurityGroup("web-sg", new SecurityGroupArgs
    {
        Name = "web-sg",
        Description = "Security group for web servers",
        VpcId = myVpc.VpcId,
        Ingress = new[]
        {
            new SecurityGroupIngressArgs
            {
                Description = "HTTP",
                FromPort = 80,
                ToPort = 80,
                Protocol = "tcp",
                CidrBlocks = new[] { "0.0.0.0/0" },
            },
            new SecurityGroupIngressArgs
            {
                Description = "SSH",
                FromPort = 22,
                ToPort = 22,
                Protocol = "tcp",
                CidrBlocks = new[] { "0.0.0.0/0" },
            },
        },
        Egress = new[]
        {
            new SecurityGroupEgressArgs
            {
                FromPort = 0,
                ToPort = 0,
                Protocol = "-1",
                CidrBlocks = new[] { "0.0.0.0/0" },
            },
        },
    });

    // Create an EC2 instance in the VPC
    var webServer = new Instance("web-server", new InstanceArgs
    {
        Ami = amazonLinux.Apply(ami => ami.Id),
        InstanceType = "t3.micro",
        SubnetId = myVpc.PublicSubnets.Apply(subnets => subnets[0]),
        VpcSecurityGroupIds = new[] { webSg.Id },
        AssociatePublicIpAddress = true,

        UserData = @"#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo ""<h1>Hello from Pulumi and Terraform modules!</h1>"" > /var/www/html/index.html
",

        Tags = new Dictionary<string, string>
        {
            ["Name"] = "web-server",
            ["Environment"] = "dev",
        },
    });

    return new Dictionary<string, object?>
    {
        ["vpcId"] = myVpc.VpcId,
        ["publicSubnets"] = myVpc.PublicSubnets,
        ["privateSubnets"] = myVpc.PrivateSubnets,
        ["instanceId"] = webServer.Id,
        ["publicIp"] = webServer.PublicIp,
        ["websiteUrl"] = webServer.PublicIp.Apply(ip => $"http://{ip}"),
    };
});
```

{{% /choosable %}}

{{% choosable language "java" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-modules-test && cd pulumi-terraform-modules-test
$ pulumi new aws-java --yes
```

Next, add the VPC module:

```bash
$ pulumi package add terraform-module terraform-aws-modules/vpc/aws 6.0.0 vpc
```

{{% notes type="tip" %}}
The `pulumi package add ...` command will output some important instructions. There are two steps you must perform manually: copy the contents of the generated SDK to your Java project, and add the dependencies to `pom.xml`:

```xml {hl_lines=["3-12"]}
     <dependencies>
        <!-- ... -->
         <dependency>
             <groupId>com.google.code.findbugs</groupId>
             <artifactId>jsr305</artifactId>
             <version>3.0.2</version>
         </dependency>
         <dependency>
             <groupId>com.google.code.gson</groupId>
             <artifactId>gson</artifactId>
             <version>2.8.9</version>
         </dependency>
     </dependencies>
```

{{% /notes %}}

Then use it in your Pulumi program, by replacing the contents of `src/main/java/myproject/App.java` with:

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.ec2.Ec2Functions;
import com.pulumi.aws.ec2.Instance;
import com.pulumi.aws.ec2.InstanceArgs;
import com.pulumi.aws.ec2.SecurityGroup;
import com.pulumi.aws.ec2.SecurityGroupArgs;
import com.pulumi.aws.ec2.inputs.GetAmiArgs;
import com.pulumi.aws.ec2.inputs.GetAmiFilterArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupEgressArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupIngressArgs;
import java.util.Collections;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Use the Terraform VPC module
            var myVpc = new com.pulumi.vpc.Module("my-vpc", com.pulumi.vpc.ModuleArgs.builder()
                .name("my-vpc")
                .cidr("10.0.0.0/16")
                .azs("us-west-2a", "us-west-2b", "us-west-2c")
                .private_subnets("10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24")
                .public_subnets("10.0.10.0/24", "10.0.11.0/24", "10.0.12.0/24")
                .enable_nat_gateway(true)
                .enable_vpn_gateway(true)
                .tags(Map.of(
                    "Terraform", "true",
                    "Environment", "dev"
                ))
                .build());

            // Get the latest Amazon Linux 2 AMI
            var amazonLinux = Ec2Functions.getAmi(GetAmiArgs.builder()
                .mostRecent(true)
                .owners("amazon")
                .filters(GetAmiFilterArgs.builder()
                    .name("name")
                    .values("amzn2-ami-hvm-*-x86_64-gp2")
                    .build())
                .build());

            // Create a security group
            var webSg = new SecurityGroup("web-sg", SecurityGroupArgs.builder()
                .name("web-sg")
                .description("Security group for web servers")
                .vpcId(myVpc.vpc_id().applyValue(id->id.get()).applyValue(String::valueOf))
                .ingress(
                    SecurityGroupIngressArgs.builder()
                        .description("HTTP")
                        .fromPort(80)
                        .toPort(80)
                        .protocol("tcp")
                        .cidrBlocks("0.0.0.0/0")
                        .build(),
                    SecurityGroupIngressArgs.builder()
                        .description("SSH")
                        .fromPort(22)
                        .toPort(22)
                        .protocol("tcp")
                        .cidrBlocks("0.0.0.0/0")
                        .build()
                )
                .egress(SecurityGroupEgressArgs.builder()
                    .fromPort(0)
                    .toPort(0)
                    .protocol("-1")
                    .cidrBlocks("0.0.0.0/0")
                    .build())
                .build());

            // Output<List<String>> secGrps = webSg.id().applyValue(s -> Collections.singletonList(s));

            // Create an EC2 instance in the VPC
            var webServer = new Instance("web-server", InstanceArgs.builder()
                .ami(amazonLinux.applyValue(ami -> ami.id()))
                .instanceType("t3.micro")
                .subnetId(myVpc.public_subnets().applyValue(subnets -> subnets.get().get(0)))
                .vpcSecurityGroupIds(webSg.id().applyValue(s -> Collections.singletonList(s)))
                .associatePublicIpAddress(true)
                .userData(String.join("\n",
                    "#!/bin/bash",
                    "yum update -y",
                    "yum install -y httpd",
                    "systemctl start httpd",
                    "systemctl enable httpd",
                    "echo \"<h1>Hello from Pulumi and Terraform modules!</h1>\" > /var/www/html/index.html"
                ))
                .tags(Map.of(
                    "Name", "web-server",
                    "Environment", "dev"
                ))
                .build());

            // Output important information
            ctx.export("vpcId", myVpc.vpc_id());
            ctx.export("instanceId", webServer.id());
            ctx.export("publicIp", webServer.publicIp());
            ctx.export("websiteUrl", webServer.publicIp().applyValue(ip -> String.format("http://%s", ip)));
        });
    }
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-modules-test && cd pulumi-terraform-modules-test
$ pulumi new aws-yaml --yes
```

Next, add the VPC module:

```bash
$ pulumi package add terraform-module terraform-aws-modules/vpc/aws 6.0.0 vpc
```

Then use it in your Pulumi program:

```yaml
name: pulumi-terraform-modules-example
runtime: yaml
description: Use Terraform modules in Pulumi

variables:
  # Get the latest Amazon Linux 2 AMI
  amazonLinux:
    fn::invoke:
      function: aws:ec2:getAmi
      arguments:
        mostRecent: true
        owners: ["amazon"]
        filters:
          - name: name
            values: ["amzn2-ami-hvm-*-x86_64-gp2"]

resources:
  # Use the Terraform VPC module
  my-vpc:
    type: vpc:index:Module
    properties:
      name: my-vpc
      cidr: 10.0.0.0/16
      azs: ["us-west-2a", "us-west-2b", "us-west-2c"]
      private_subnets: ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
      public_subnets: ["10.0.10.0/24", "10.0.11.0/24", "10.0.12.0/24"]
      enable_nat_gateway: true
      enable_vpn_gateway: true
      tags:
        Terraform: "true"
        Environment: "dev"

  # Create a security group
  web-sg:
    type: aws:ec2:SecurityGroup
    properties:
      name: web-sg
      description: Security group for web servers
      vpcId: ${my-vpc.vpc_id}
      ingress:
        - description: HTTP
          fromPort: 80
          toPort: 80
          protocol: tcp
          cidrBlocks: ["0.0.0.0/0"]
        - description: SSH
          fromPort: 22
          toPort: 22
          protocol: tcp
          cidrBlocks: ["0.0.0.0/0"]
      egress:
        - fromPort: 0
          toPort: 0
          protocol: "-1"
          cidrBlocks: ["0.0.0.0/0"]

  # Create an EC2 instance in the VPC
  web-server:
    type: aws:ec2:Instance
    properties:
      ami: ${amazonLinux.id}
      instanceType: t3.micro
      subnetId: ${my-vpc.public_subnets[0]}
      vpcSecurityGroupIds:
        - ${web-sg.id}
      associatePublicIpAddress: true
      userData: |
        #!/bin/bash
        yum update -y
        yum install -y httpd
        systemctl start httpd
        systemctl enable httpd
        echo "<h1>Hello from Pulumi and Terraform modules!</h1>" > /var/www/html/index.html
      tags:
        Name: web-server
        Environment: dev

outputs:
  vpcId: ${my-vpc.vpc_id}
  instanceId: ${web-server.id}
  publicIp: ${web-server.publicIp}
  websiteUrl: http://${web-server.publicIp}

# The vpc Terraform module package definition
packages:
  vpc:
    source: terraform-module
    version: 0.1.4
    parameters:
      - terraform-aws-modules/vpc/aws
      - 6.0.0
      - vpc
```

{{% /choosable %}}

## Compare with Terraform

The same functionality in Terraform would look like:

```hcl
# Terraform equivalent
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-west-2a", "us-west-2b", "us-west-2c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.10.0/24", "10.0.11.0/24", "10.0.12.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = true

  tags = {
    Terraform = "true"
    Environment = "dev"
  }
}

data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

resource "aws_security_group" "web_sg" {
  name        = "web-sg"
  description = "Security group for web servers"
  vpc_id      = module.vpc.vpc_id

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web_server" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
  subnet_id     = module.vpc.public_subnets[0]
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  associate_public_ip_address = true

  user_data = <<-EOF
    #!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo "<h1>Hello from Pulumi and Terraform modules!</h1>" > /var/www/html/index.html
  EOF

  tags = {
    Name = "web-server"
    Environment = "dev"
  }
}

output "vpc_id" {
  value = module.vpc.vpc_id
}

output "instance_id" {
  value = aws_instance.web_server.id
}

output "public_ip" {
  value = aws_instance.web_server.public_ip
}

output "website_url" {
  value = "http://${aws_instance.web_server.public_ip}"
}
```

## Best practices

1. **Pin module versions**: Always specify module versions in production
2. **Review module source**: Understand what the module does before using it
3. **Test module outputs**: Verify that module outputs work as expected
4. **Monitor module updates**: Keep track of module updates and breaking changes
5. **Use reputable sources**: Prefer well-maintained modules from trusted sources
6. **Document module usage**: Document why you chose specific modules and their configuration

## Clean up

Test your deployment and clean up resources:

```bash
# Deploy the stack
$ pulumi up

# Visit the website URL from the output
# When done, destroy the resources
$ pulumi destroy
```

{{< get-started-stepper >}}
