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
This allows you to leverage the thousands of existing modules without rewriting them in Pulumi.

## Add Terraform modules

Use the `pulumi package add` command to add Terraform modules to your project:

```bash
# Add a module from the Terraform Registry
pulumi package add terraform-module-vpc-aws

# Add a module from a Git repository
pulumi package add terraform-module-vpc-aws --git-url https://github.com/terraform-aws-modules/terraform-aws-vpc

# Add a local module
pulumi package add terraform-module-custom --local-path ./modules/custom
```

## Example: AWS VPC module

Let's use the popular `terraform-aws-vpc` module to create a VPC with subnets, and then deploy an EC2 instance in that VPC:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

First, add the VPC module:

```bash
pulumi package add terraform-module-vpc-aws
```

Then use it in your Pulumi program:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as vpc from "@pulumi/terraform-module-vpc-aws";

// Use the Terraform VPC module
const myVpc = new vpc.Vpc("my-vpc", {
    name: "my-vpc",
    cidr: "10.0.0.0/16",

    azs: ["us-west-2a", "us-west-2b", "us-west-2c"],
    privateSubnets: ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"],
    publicSubnets: ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"],

    enableNatGateway: true,
    enableVpnGateway: true,

    tags: {
        Terraform: "true",
        Environment: "dev",
    },
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

// Create a security group
const webSg = new aws.ec2.SecurityGroup("web-sg", {
    name: "web-sg",
    description: "Security group for web servers",
    vpcId: myVpc.vpcId,
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

// Create an EC2 instance in the VPC
const webServer = new aws.ec2.Instance("web-server", {
    ami: amazonLinux.id,
    instanceType: "t3.micro",
    subnetId: myVpc.publicSubnets.apply(subnets => subnets[0]),
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
export const vpcId = myVpc.vpcId;
export const publicSubnets = myVpc.publicSubnets;
export const privateSubnets = myVpc.privateSubnets;
export const instanceId = webServer.id;
export const publicIp = webServer.publicIp;
export const websiteUrl = pulumi.interpolate`http://${webServer.publicIp}`;
```

{{% /choosable %}}

{{% choosable language "python" %}}

First, add the VPC module:

```bash
pulumi package add terraform-module-vpc-aws
```

Then use it in your Pulumi program:

```python
import pulumi
import pulumi_aws as aws
import pulumi_terraform_module_vpc_aws as vpc

# Use the Terraform VPC module
my_vpc = vpc.Vpc("my-vpc",
    name="my-vpc",
    cidr="10.0.0.0/16",

    azs=["us-west-2a", "us-west-2b", "us-west-2c"],
    private_subnets=["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"],
    public_subnets=["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"],

    enable_nat_gateway=True,
    enable_vpn_gateway=True,

    tags={
        "Terraform": "true",
        "Environment": "dev",
    }
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

# Create a security group
web_sg = aws.ec2.SecurityGroup("web-sg",
    name="web-sg",
    description="Security group for web servers",
    vpc_id=my_vpc.vpc_id,
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
pulumi.export("publicSubnets", my_vpc.public_subnets)
pulumi.export("privateSubnets", my_vpc.private_subnets)
pulumi.export("instanceId", web_server.id)
pulumi.export("publicIp", web_server.public_ip)
pulumi.export("websiteUrl", pulumi.Output.format("http://{0}", web_server.public_ip))
```

{{% /choosable %}}

{{% choosable language "go" %}}

First, add the VPC module:

```bash
pulumi package add terraform-module-vpc-aws
```

Then use it in your Pulumi program:

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	"github.com/pulumi/pulumi-terraform-module-vpc-aws/sdk/go/vpc"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Use the Terraform VPC module
		myVpc, err := vpc.NewVpc(ctx, "my-vpc", &vpc.VpcArgs{
			Name: pulumi.String("my-vpc"),
			Cidr: pulumi.String("10.0.0.0/16"),

			Azs:            pulumi.StringArray{pulumi.String("us-west-2a"), pulumi.String("us-west-2b"), pulumi.String("us-west-2c")},
			PrivateSubnets: pulumi.StringArray{pulumi.String("10.0.1.0/24"), pulumi.String("10.0.2.0/24"), pulumi.String("10.0.3.0/24")},
			PublicSubnets:  pulumi.StringArray{pulumi.String("10.0.101.0/24"), pulumi.String("10.0.102.0/24"), pulumi.String("10.0.103.0/24")},

			EnableNatGateway: pulumi.Bool(true),
			EnableVpnGateway: pulumi.Bool(true),

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
			VpcId:       myVpc.VpcId,
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
			SubnetId: myVpc.PublicSubnets.ApplyT(func(subnets []string) string {
				return subnets[0]
			}).(pulumi.StringOutput),
			VpcSecurityGroupIds:       pulumi.StringArray{webSg.ID()},
			AssociatePublicIpAddress:  pulumi.Bool(true),

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
		ctx.Export("vpcId", myVpc.VpcId)
		ctx.Export("publicSubnets", myVpc.PublicSubnets)
		ctx.Export("privateSubnets", myVpc.PrivateSubnets)
		ctx.Export("instanceId", webServer.ID())
		ctx.Export("publicIp", webServer.PublicIp)
		ctx.Export("websiteUrl", pulumi.Sprintf("http://%s", webServer.PublicIp))
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

First, add the VPC module:

```bash
pulumi package add terraform-module-vpc-aws
```

Then use it in your Pulumi program:

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.TerraformModuleVpcAws;

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

First, add the VPC module:

```bash
pulumi package add terraform-module-vpc-aws
```

Then use it in your Pulumi program:

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
import com.pulumi.core.Output;
import com.pulumi.terraformmodulevpcaws.Vpc;
import com.pulumi.terraformmodulevpcaws.VpcArgs;

import java.util.List;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Use the Terraform VPC module
            var myVpc = new Vpc("my-vpc", VpcArgs.builder()
                .name("my-vpc")
                .cidr("10.0.0.0/16")
                .azs("us-west-2a", "us-west-2b", "us-west-2c")
                .privateSubnets("10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24")
                .publicSubnets("10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24")
                .enableNatGateway(true)
                .enableVpnGateway(true)
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
                .vpcId(myVpc.vpcId())
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

            // Create an EC2 instance in the VPC
            var webServer = new Instance("web-server", InstanceArgs.builder()
                .ami(amazonLinux.applyValue(ami -> ami.id()))
                .instanceType("t3.micro")
                .subnetId(myVpc.publicSubnets().applyValue(subnets -> subnets.get(0)))
                .vpcSecurityGroupIds(webSg.id())
                .associatePublicIpAddress(true)
                .userData("""
                    #!/bin/bash
                    yum update -y
                    yum install -y httpd
                    systemctl start httpd
                    systemctl enable httpd
                    echo "<h1>Hello from Pulumi and Terraform modules!</h1>" > /var/www/html/index.html
                    """)
                .tags(Map.of(
                    "Name", "web-server",
                    "Environment", "dev"
                ))
                .build());

            // Output important information
            ctx.export("vpcId", myVpc.vpcId());
            ctx.export("publicSubnets", myVpc.publicSubnets());
            ctx.export("privateSubnets", myVpc.privateSubnets());
            ctx.export("instanceId", webServer.id());
            ctx.export("publicIp", webServer.publicIp());
            ctx.export("websiteUrl", webServer.publicIp().applyValue(ip -> String.format("http://%s", ip)));
        });
    }
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

First, add the VPC module:

```bash
pulumi package add terraform-module-vpc-aws
```

Then use it in your Pulumi program:

```yaml
name: terraform-modules-example
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
    type: terraform-module-vpc-aws:index:Vpc
    properties:
      name: my-vpc
      cidr: 10.0.0.0/16
      azs: ["us-west-2a", "us-west-2b", "us-west-2c"]
      privateSubnets: ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
      publicSubnets: ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
      enableNatGateway: true
      enableVpnGateway: true
      tags:
        Terraform: "true"
        Environment: "dev"

  # Create a security group
  web-sg:
    type: aws:ec2:SecurityGroup
    properties:
      name: web-sg
      description: Security group for web servers
      vpcId: ${my-vpc.vpcId}
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
      subnetId: ${my-vpc.publicSubnets[0]}
      vpcSecurityGroupIds: [${web-sg.id}]
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
  vpcId: ${my-vpc.vpcId}
  publicSubnets: ${my-vpc.publicSubnets}
  privateSubnets: ${my-vpc.privateSubnets}
  instanceId: ${web-server.id}
  publicIp: ${web-server.publicIp}
  websiteUrl: http://${web-server.publicIp}
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
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

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

output "public_subnets" {
  value = module.vpc.public_subnets
}

output "private_subnets" {
  value = module.vpc.private_subnets
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

## Module versioning

Specify module versions for consistency:

```bash
# Add a specific version
pulumi package add terraform-module-vpc-aws --version 5.0.0

# Add from Git with a specific tag
pulumi package add terraform-module-vpc-aws --git-url https://github.com/terraform-aws-modules/terraform-aws-vpc.git --git-tag v5.0.0
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
pulumi up

# Visit the website URL from the output
# When done, destroy the resources
pulumi destroy
```

{{< get-started-stepper >}}
