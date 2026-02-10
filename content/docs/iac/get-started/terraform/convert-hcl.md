---
title_tag: Convert HCL Code | Pulumi for Terraform Users
title: Convert HCL Code
h1: "Convert HCL Code"
meta_desc: Learn when and how to convert existing Terraform HCL code to Pulumi programs using automated tools and manual techniques.
weight: 7
menu:
    iac:
        name: Convert HCL Code
        parent: terraform-get-started
        weight: 7

aliases:
---

## When to convert

Converting HCL to Pulumi code makes sense in several scenarios:

* **Complex logic**: Terraform's HCL limitations make certain operations difficult
* **Testing requirements**: You need unit testing capabilities for infrastructure code
* **Integration needs**: Infrastructure code needs to integrate with application code
* **Team preferences**: Your team prefers general-purpose programming languages
* **Advanced features**: You want to use Pulumi-specific features like Pulumi Policies or Automation API

## Conversion approaches

### Automated conversion with `pulumi convert`

The `pulumi convert` command can automatically translate Terraform configurations to Pulumi programs.

First, ensure you have a Terraform configuration:

```hcl
# main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "main-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-west-2a"
  map_public_ip_on_launch = true

  tags = {
    Name = "public-subnet"
  }
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "main-igw"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name = "public-rt"
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Security group for web servers"
  vpc_id      = aws_vpc.main.id

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

  tags = {
    Name = "web-sg"
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type
  subnet_id     = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.web.id]

  user_data = <<-EOF
    #!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo "<h1>Hello from Pulumi converted infrastructure!</h1>" > /var/www/html/index.html
  EOF

  tags = {
    Name = "web-server"
  }
}

output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "public_ip" {
  description = "Public IP address of the web server"
  value       = aws_instance.web.public_ip
}

output "website_url" {
  description = "URL of the website"
  value       = "http://${aws_instance.web.public_ip}"
}
```

Now convert it to Pulumi:

```bash
# Convert to TypeScript
$ pulumi convert --from terraform --language typescript --out ./pulumi-converted

# Convert to Python
$ pulumi convert --from terraform --language python --out ./pulumi-converted

# Convert to Go
$ pulumi convert --from terraform --language go --out ./pulumi-converted

# Convert to C#
$ pulumi convert --from terraform --language csharp --out ./pulumi-converted

# Convert to Java
$ pulumi convert --from terraform --language java --out ./pulumi-converted

# Convert to YAML
$ pulumi convert --from terraform --language yaml --out ./pulumi-converted
```

### Converted TypeScript example

The `pulumi convert` command would generate something like this:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create configuration
const config = new pulumi.Config();
const awsRegion = config.get("awsRegion") || "us-west-2";
const instanceType = config.get("instanceType") || "t3.micro";

// Data source for Amazon Linux AMI
const amazonLinux = aws.ec2.getAmiOutput({
    mostRecent: true,
    owners: ["amazon"],
    filters: [{
        name: "name",
        values: ["amzn2-ami-hvm-*-x86_64-gp2"],
    }],
});

// Create VPC
const main = new aws.ec2.Vpc("main", {
    cidrBlock: "10.0.0.0/16",
    enableDnsHostnames: true,
    enableDnsSupport: true,
    tags: {
        Name: "main-vpc",
    },
});

// Create public subnet
const publicSubnet = new aws.ec2.Subnet("public", {
    vpcId: main.id,
    cidrBlock: "10.0.1.0/24",
    availabilityZone: "us-west-2a",
    mapPublicIpOnLaunch: true,
    tags: {
        Name: "public-subnet",
    },
});

// Create internet gateway
const mainIgw = new aws.ec2.InternetGateway("main", {
    vpcId: main.id,
    tags: {
        Name: "main-igw",
    },
});

// Create route table
const publicRt = new aws.ec2.RouteTable("public", {
    vpcId: main.id,
    routes: [{
        cidrBlock: "0.0.0.0/0",
        gatewayId: mainIgw.id,
    }],
    tags: {
        Name: "public-rt",
    },
});

// Associate route table with subnet
const publicRtAssociation = new aws.ec2.RouteTableAssociation("public", {
    subnetId: publicSubnet.id,
    routeTableId: publicRt.id,
});

// Create security group
const webSg = new aws.ec2.SecurityGroup("web", {
    name: "web-sg",
    description: "Security group for web servers",
    vpcId: main.id,
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
    egress: [{
        fromPort: 0,
        toPort: 0,
        protocol: "-1",
        cidrBlocks: ["0.0.0.0/0"],
    }],
    tags: {
        Name: "web-sg",
    },
});

// Create EC2 instance
const webInstance = new aws.ec2.Instance("web", {
    ami: amazonLinux.id,
    instanceType: instanceType,
    subnetId: publicSubnet.id,
    vpcSecurityGroupIds: [webSg.id],
    userData: `#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from Pulumi converted infrastructure!</h1>" > /var/www/html/index.html
`,
    tags: {
        Name: "web-server",
    },
});

// Outputs
export const vpcId = main.id;
export const publicIp = webInstance.publicIp;
export const websiteUrl = pulumi.interpolate`http://${webInstance.publicIp}`;
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
import pulumi
import pulumi_aws as aws

# Create configuration
config = pulumi.Config()
aws_region = config.get("aws_region") or "us-west-2"
instance_type = config.get("instance_type") or "t3.micro"

# Data source for Amazon Linux AMI
amazon_linux = aws.ec2.get_ami(
    most_recent=True,
    owners=["amazon"],
    filters=[{
        "name": "name",
        "values": ["amzn2-ami-hvm-*-x86_64-gp2"],
    }]
)

# Create VPC
main_vpc = aws.ec2.Vpc("main",
    cidr_block="10.0.0.0/16",
    enable_dns_hostnames=True,
    enable_dns_support=True,
    tags={
        "Name": "main-vpc",
    }
)

# Create public subnet
public_subnet = aws.ec2.Subnet("public",
    vpc_id=main_vpc.id,
    cidr_block="10.0.1.0/24",
    availability_zone="us-west-2a",
    map_public_ip_on_launch=True,
    tags={
        "Name": "public-subnet",
    }
)

# Create internet gateway
main_igw = aws.ec2.InternetGateway("main",
    vpc_id=main_vpc.id,
    tags={
        "Name": "main-igw",
    }
)

# Create route table
public_rt = aws.ec2.RouteTable("public",
    vpc_id=main_vpc.id,
    routes=[{
        "cidr_block": "0.0.0.0/0",
        "gateway_id": main_igw.id,
    }],
    tags={
        "Name": "public-rt",
    }
)

# Associate route table with subnet
public_rt_association = aws.ec2.RouteTableAssociation("public",
    subnet_id=public_subnet.id,
    route_table_id=public_rt.id
)

# Create security group
web_sg = aws.ec2.SecurityGroup("web",
    name="web-sg",
    description="Security group for web servers",
    vpc_id=main_vpc.id,
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
    egress=[{
        "from_port": 0,
        "to_port": 0,
        "protocol": "-1",
        "cidr_blocks": ["0.0.0.0/0"],
    }],
    tags={
        "Name": "web-sg",
    }
)

# Create EC2 instance
web_instance = aws.ec2.Instance("web",
    ami=amazon_linux.id,
    instance_type=instance_type,
    subnet_id=public_subnet.id,
    vpc_security_group_ids=[web_sg.id],
    user_data="""#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from Pulumi converted infrastructure!</h1>" > /var/www/html/index.html
""",
    tags={
        "Name": "web-server",
    }
)

# Outputs
pulumi.export("vpc_id", main_vpc.id)
pulumi.export("public_ip", web_instance.public_ip)
pulumi.export("website_url", pulumi.Output.format("http://{0}", web_instance.public_ip))
```

{{% /choosable %}}

{{% choosable language "go" %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create configuration
		cfg := config.New(ctx, "")
		awsRegion := cfg.Get("awsRegion")
		if awsRegion == "" {
			awsRegion = "us-west-2"
		}
		instanceType := cfg.Get("instanceType")
		if instanceType == "" {
			instanceType = "t3.micro"
		}

		// Data source for Amazon Linux AMI
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

		// Create VPC
		mainVpc, err := ec2.NewVpc(ctx, "main", &ec2.VpcArgs{
			CidrBlock:          pulumi.String("10.0.0.0/16"),
			EnableDnsHostnames: pulumi.Bool(true),
			EnableDnsSupport:   pulumi.Bool(true),
			Tags: pulumi.StringMap{
				"Name": pulumi.String("main-vpc"),
			},
		})
		if err != nil {
			return err
		}

		// Create public subnet
		publicSubnet, err := ec2.NewSubnet(ctx, "public", &ec2.SubnetArgs{
			VpcId:                 mainVpc.ID(),
			CidrBlock:             pulumi.String("10.0.1.0/24"),
			AvailabilityZone:      pulumi.String("us-west-2a"),
			MapPublicIpOnLaunch:   pulumi.Bool(true),
			Tags: pulumi.StringMap{
				"Name": pulumi.String("public-subnet"),
			},
		})
		if err != nil {
			return err
		}

		// Create internet gateway
		mainIgw, err := ec2.NewInternetGateway(ctx, "main", &ec2.InternetGatewayArgs{
			VpcId: mainVpc.ID(),
			Tags: pulumi.StringMap{
				"Name": pulumi.String("main-igw"),
			},
		})
		if err != nil {
			return err
		}

		// Create route table
		publicRt, err := ec2.NewRouteTable(ctx, "public", &ec2.RouteTableArgs{
			VpcId: mainVpc.ID(),
			Routes: ec2.RouteTableRouteArray{
				&ec2.RouteTableRouteArgs{
					CidrBlock: pulumi.String("0.0.0.0/0"),
					GatewayId: mainIgw.ID(),
				},
			},
			Tags: pulumi.StringMap{
				"Name": pulumi.String("public-rt"),
			},
		})
		if err != nil {
			return err
		}

		// Associate route table with subnet
		_, err = ec2.NewRouteTableAssociation(ctx, "public", &ec2.RouteTableAssociationArgs{
			SubnetId:     publicSubnet.ID(),
			RouteTableId: publicRt.ID(),
		})
		if err != nil {
			return err
		}

		// Create security group
		webSg, err := ec2.NewSecurityGroup(ctx, "web", &ec2.SecurityGroupArgs{
			Name:        pulumi.String("web-sg"),
			Description: pulumi.String("Security group for web servers"),
			VpcId:       mainVpc.ID(),
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
			Tags: pulumi.StringMap{
				"Name": pulumi.String("web-sg"),
			},
		})
		if err != nil {
			return err
		}

		// Create EC2 instance
		webInstance, err := ec2.NewInstance(ctx, "web", &ec2.InstanceArgs{
			Ami:          pulumi.String(amazonLinux.Id),
			InstanceType: pulumi.String(instanceType),
			SubnetId:     publicSubnet.ID(),
			VpcSecurityGroupIds: pulumi.StringArray{webSg.ID()},
			UserData: pulumi.String(`#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from Pulumi converted infrastructure!</h1>" > /var/www/html/index.html
`),
			Tags: pulumi.StringMap{
				"Name": pulumi.String("web-server"),
			},
		})
		if err != nil {
			return err
		}

		// Outputs
		ctx.Export("vpcId", mainVpc.ID())
		ctx.Export("publicIp", webInstance.PublicIp)
		ctx.Export("websiteUrl", pulumi.Sprintf("http://%s", webInstance.PublicIp))
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Aws.Ec2;

return await Deployment.RunAsync(() =>
{
    // Create configuration
    var config = new Pulumi.Config();
    var awsRegion = config.Get("awsRegion") ?? "us-west-2";
    var instanceType = config.Get("instanceType") ?? "t3.micro";

    // Data source for Amazon Linux AMI
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

    // Create VPC
    var mainVpc = new Vpc("main", new VpcArgs
    {
        CidrBlock = "10.0.0.0/16",
        EnableDnsHostnames = true,
        EnableDnsSupport = true,
        Tags = new Dictionary<string, string>
        {
            ["Name"] = "main-vpc",
        },
    });

    // Create public subnet
    var publicSubnet = new Subnet("public", new SubnetArgs
    {
        VpcId = mainVpc.Id,
        CidrBlock = "10.0.1.0/24",
        AvailabilityZone = "us-west-2a",
        MapPublicIpOnLaunch = true,
        Tags = new Dictionary<string, string>
        {
            ["Name"] = "public-subnet",
        },
    });

    // Create internet gateway
    var mainIgw = new InternetGateway("main", new InternetGatewayArgs
    {
        VpcId = mainVpc.Id,
        Tags = new Dictionary<string, string>
        {
            ["Name"] = "main-igw",
        },
    });

    // Create route table
    var publicRt = new RouteTable("public", new RouteTableArgs
    {
        VpcId = mainVpc.Id,
        Routes = new[]
        {
            new RouteTableRouteArgs
            {
                CidrBlock = "0.0.0.0/0",
                GatewayId = mainIgw.Id,
            },
        },
        Tags = new Dictionary<string, string>
        {
            ["Name"] = "public-rt",
        },
    });

    // Associate route table with subnet
    var publicRtAssociation = new RouteTableAssociation("public", new RouteTableAssociationArgs
    {
        SubnetId = publicSubnet.Id,
        RouteTableId = publicRt.Id,
    });

    // Create security group
    var webSg = new SecurityGroup("web", new SecurityGroupArgs
    {
        Name = "web-sg",
        Description = "Security group for web servers",
        VpcId = mainVpc.Id,
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
        Tags = new Dictionary<string, string>
        {
            ["Name"] = "web-sg",
        },
    });

    // Create EC2 instance
    var webInstance = new Instance("web", new InstanceArgs
    {
        Ami = amazonLinux.Apply(ami => ami.Id),
        InstanceType = instanceType,
        SubnetId = publicSubnet.Id,
        VpcSecurityGroupIds = new[] { webSg.Id },
        UserData = @"#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo ""<h1>Hello from Pulumi converted infrastructure!</h1>"" > /var/www/html/index.html
",
        Tags = new Dictionary<string, string>
        {
            ["Name"] = "web-server",
        },
    });

    return new Dictionary<string, object?>
    {
        ["vpcId"] = mainVpc.Id,
        ["publicIp"] = webInstance.PublicIp,
        ["websiteUrl"] = webInstance.PublicIp.Apply(ip => $"http://{ip}"),
    };
});
```

{{% /choosable %}}

{{% choosable language "java" %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.ec2.Ec2Functions;
import com.pulumi.aws.ec2.Instance;
import com.pulumi.aws.ec2.InstanceArgs;
import com.pulumi.aws.ec2.InternetGateway;
import com.pulumi.aws.ec2.InternetGatewayArgs;
import com.pulumi.aws.ec2.RouteTable;
import com.pulumi.aws.ec2.RouteTableArgs;
import com.pulumi.aws.ec2.RouteTableAssociation;
import com.pulumi.aws.ec2.RouteTableAssociationArgs;
import com.pulumi.aws.ec2.SecurityGroup;
import com.pulumi.aws.ec2.SecurityGroupArgs;
import com.pulumi.aws.ec2.Subnet;
import com.pulumi.aws.ec2.SubnetArgs;
import com.pulumi.aws.ec2.Vpc;
import com.pulumi.aws.ec2.VpcArgs;
import com.pulumi.aws.ec2.inputs.GetAmiArgs;
import com.pulumi.aws.ec2.inputs.GetAmiFilterArgs;
import com.pulumi.aws.ec2.inputs.RouteTableRouteArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupEgressArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupIngressArgs;
import com.pulumi.core.Output;

import java.util.List;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create configuration
            var config = new com.pulumi.Config();
            var awsRegion = config.get("awsRegion").orElse("us-west-2");
            var instanceType = config.get("instanceType").orElse("t3.micro");

            // Data source for Amazon Linux AMI
            var amazonLinux = Ec2Functions.getAmi(GetAmiArgs.builder()
                .mostRecent(true)
                .owners("amazon")
                .filters(GetAmiFilterArgs.builder()
                    .name("name")
                    .values("amzn2-ami-hvm-*-x86_64-gp2")
                    .build())
                .build());

            // Create VPC
            var mainVpc = new Vpc("main", VpcArgs.builder()
                .cidrBlock("10.0.0.0/16")
                .enableDnsHostnames(true)
                .enableDnsSupport(true)
                .tags(Map.of("Name", "main-vpc"))
                .build());

            // Create public subnet
            var publicSubnet = new Subnet("public", SubnetArgs.builder()
                .vpcId(mainVpc.id())
                .cidrBlock("10.0.1.0/24")
                .availabilityZone("us-west-2a")
                .mapPublicIpOnLaunch(true)
                .tags(Map.of("Name", "public-subnet"))
                .build());

            // Create internet gateway
            var mainIgw = new InternetGateway("main", InternetGatewayArgs.builder()
                .vpcId(mainVpc.id())
                .tags(Map.of("Name", "main-igw"))
                .build());

            // Create route table
            var publicRt = new RouteTable("public", RouteTableArgs.builder()
                .vpcId(mainVpc.id())
                .routes(RouteTableRouteArgs.builder()
                    .cidrBlock("0.0.0.0/0")
                    .gatewayId(mainIgw.id())
                    .build())
                .tags(Map.of("Name", "public-rt"))
                .build());

            // Associate route table with subnet
            var publicRtAssociation = new RouteTableAssociation("public", RouteTableAssociationArgs.builder()
                .subnetId(publicSubnet.id())
                .routeTableId(publicRt.id())
                .build());

            // Create security group
            var webSg = new SecurityGroup("web", SecurityGroupArgs.builder()
                .name("web-sg")
                .description("Security group for web servers")
                .vpcId(mainVpc.id())
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
                .tags(Map.of("Name", "web-sg"))
                .build());

            // Create EC2 instance
            var webInstance = new Instance("web", InstanceArgs.builder()
                .ami(amazonLinux.applyValue(ami -> ami.id()))
                .instanceType(instanceType)
                .subnetId(publicSubnet.id())
                .vpcSecurityGroupIds(webSg.id())
                .userData("""
                    #!/bin/bash
                    yum update -y
                    yum install -y httpd
                    systemctl start httpd
                    systemctl enable httpd
                    echo "<h1>Hello from Pulumi converted infrastructure!</h1>" > /var/www/html/index.html
                    """)
                .tags(Map.of("Name", "web-server"))
                .build());

            // Outputs
            ctx.export("vpcId", mainVpc.id());
            ctx.export("publicIp", webInstance.publicIp());
            ctx.export("websiteUrl", webInstance.publicIp().applyValue(ip -> String.format("http://%s", ip)));
        });
    }
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

```yaml
name: converted-infrastructure
runtime: yaml
description: Converted from Terraform HCL

config:
  awsRegion:
    type: string
    default: us-west-2
  instanceType:
    type: string
    default: t3.micro

variables:
  # Data source for Amazon Linux AMI
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
  # Create VPC
  main:
    type: aws:ec2:Vpc
    properties:
      cidrBlock: 10.0.0.0/16
      enableDnsHostnames: true
      enableDnsSupport: true
      tags:
        Name: main-vpc

  # Create public subnet
  public:
    type: aws:ec2:Subnet
    properties:
      vpcId: ${main.id}
      cidrBlock: 10.0.1.0/24
      availabilityZone: us-west-2a
      mapPublicIpOnLaunch: true
      tags:
        Name: public-subnet

  # Create internet gateway
  main-igw:
    type: aws:ec2:InternetGateway
    properties:
      vpcId: ${main.id}
      tags:
        Name: main-igw

  # Create route table
  public-rt:
    type: aws:ec2:RouteTable
    properties:
      vpcId: ${main.id}
      routes:
        - cidrBlock: 0.0.0.0/0
          gatewayId: ${main-igw.id}
      tags:
        Name: public-rt

  # Associate route table with subnet
  public-rt-association:
    type: aws:ec2:RouteTableAssociation
    properties:
      subnetId: ${public.id}
      routeTableId: ${public-rt.id}

  # Create security group
  web-sg:
    type: aws:ec2:SecurityGroup
    properties:
      name: web-sg
      description: Security group for web servers
      vpcId: ${main.id}
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
      tags:
        Name: web-sg

  # Create EC2 instance
  web:
    type: aws:ec2:Instance
    properties:
      ami: ${amazonLinux.id}
      instanceType: ${instanceType}
      subnetId: ${public.id}
      vpcSecurityGroupIds: [${web-sg.id}]
      userData: |
        #!/bin/bash
        yum update -y
        yum install -y httpd
        systemctl start httpd
        systemctl enable httpd
        echo "<h1>Hello from Pulumi converted infrastructure!</h1>" > /var/www/html/index.html
      tags:
        Name: web-server

outputs:
  vpcId: ${main.id}
  publicIp: ${web.publicIp}
  websiteUrl: http://${web.publicIp}
```

{{% /choosable %}}

## Testing the converted code

Deploy and verify that the converted code produces the same infrastructure:

```bash
# Initialize the new Pulumi project
$ cd pulumi-converted
$ pulumi up

# Test the deployment
$ curl $(pulumi stack output websiteUrl)

# Compare with original Terraform outputs
$ terraform output -json > tf-outputs.json
$ pulumi stack output --json > pulumi-outputs.json

# Clean up
$ pulumi destroy
```

## Verifying conversion accuracy

After converting existing infrastructure, verify that your Pulumi program produces identical results by importing the Terraform state and running a preview:

```bash
# Import the existing Terraform state
$ pulumi import aws:ec2/vpc:Vpc main vpc-12345
$ pulumi import aws:ec2/subnet:Subnet public subnet-67890
$ pulumi import aws:ec2/instance:Instance web i-abcdef123

# Run preview to ensure no changes
$ pulumi preview

# Expected result: "no changes required"
```

This verification step is crucial when converting production infrastructure, as it confirms your Pulumi program exactly matches the existing Terraform-managed resources.

## AI-assisted conversion with the Pulumi MCP server

For complex Terraform configurations, you can use AI tools like [Claude](https://www.anthropic.com/claude-code) with the [Pulumi MCP (Model Context Protocol) server](/docs/iac/using-pulumi/mcp-server), which provides comprehensive Pulumi integration, including a specialized Terraform conversion prompt.

### Using the Pulumi MCP server (recommended)

The [Pulumi MCP server](/docs/iac/using-pulumi/mcp-server) enables AI assistants to interact with Pulumi programmatically. Beyond conversion, it provides full infrastructure management capabilities including stack operations, resource querying, and automated deployments.

The MCP server includes a sophisticated `convert-terraform-to-typescript` prompt that ensures:

* **Type safety**: Proper use of `pulumi.Input<T>` and `pulumi.Output<T>` types
* **Best practices**: Idiomatic TypeScript patterns and Pulumi conventions
* **Configuration handling**: Safe access to config values with null checking
* **Resource naming**: Consistent and descriptive resource naming
* **Multi-provider support**: Proper handling of multiple provider configurations

**Installation and setup:**

1. **Install via Claude Code** (if using Claude):

   ```bash
   $ claude mcp add -s user pulumi -- npx @pulumi/mcp-server@latest stdio
   ```
  
   Follow the complete setup instructions in the [Pulumi MCP server docs](/docs/iac/using-pulumi/mcp-server).

2. **Prepare your Terraform code**: Gather your complete Terraform configuration files (`.tf`, `terraform.tfvars`, etc.)

3. **Use the conversion prompt**: Once configured, you can attach the specific conversion prompt in Claude:

   ```
   @convert-terraform-to-typescript

   Please convert this Terraform configuration to Pulumi TypeScript:

   [Paste your Terraform HCL code here]
   ```

The MCP server provides additional capabilities beyond conversion, including:

* Infrastructure previews with `pulumi preview`
* Automated deployments with `pulumi up`
* Stack output retrieval
* Resource querying and management

### Alternative: Manual prompt usage

If you prefer not to use the MCP server, you can access the conversion prompt directly:

1. **Access the prompt**: The "convert-terraform-to-typescript" prompt is available in the [Pulumi MCP server](/docs/iac/using-pulumi/mcp-server)

2. **Prepare your Terraform code**: Gather your complete Terraform configuration files (`.tf`, `terraform.tfvars`, etc.)

3. **Use with Claude**: Copy the conversion prompt and your Terraform code, then ask Claude to perform the conversion:

   ```
   [Paste the complete conversion prompt]

   Please convert this Terraform configuration to Pulumi TypeScript:

   [Paste your Terraform HCL code here]
   ```

## Review the output

Any time you use an automated conversion tool, you will want to review and validate the output. Some things to check for:

* Proper error handling and validation
* Type-safe configuration access
* Idiomatic resource definitions
* Comprehensive resource labeling

## Best practices for conversion

1. **Start small**: Convert simple configurations first to understand the process
2. **Verify outputs**: Ensure converted code produces identical infrastructure
3. **Test thoroughly**: Write tests for critical infrastructure components
4. **Preserve structure**: Keep similar resource organization when possible
5. **Document changes**: Note any differences between original and converted code
6. **Version control**: Use Git to track conversion changes

{{< get-started-stepper >}}
