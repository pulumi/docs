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
---

## Do you need to convert?

Converting is not the only way to run Terraform configuration with Pulumi. Pulumi's [HCL runtime](/docs/iac/languages-sdks/hcl/) runs your existing `.tf` files directly: set `runtime: hcl` in `Pulumi.yaml` and `pulumi up` deploys the configuration you already have, unchanged.

Which path you take comes down to what you want out of the move:

* **Run your HCL natively** when you want to keep writing HCL and are after Pulumi's engine, state management, secrets, and cloud platform.
* **Convert** when you want the infrastructure code itself in a general-purpose language, for the testing, abstraction, and IDE support that comes with TypeScript, JavaScript, Python, Go, .NET, or Java.

If you haven't written much code in one of these languages, [Language Essentials](/docs/iac/guides/basics/language-essentials/) translates the HCL you already know into the small set of constructs a Pulumi program actually uses.

The rest of this page covers converting.

## When to convert

Converting HCL to Pulumi code makes sense in several scenarios:

* **Complex logic**: Operations that need rich runtime logic can be more natural in a general-purpose language
* **Testing requirements**: You need unit testing capabilities for infrastructure code
* **Integration needs**: Infrastructure code needs to integrate with application code
* **Team preferences**: Your team prefers general-purpose programming languages
* **Advanced features**: You want to use Pulumi-specific features like Pulumi Policies or Automation API

## Conversion approaches

### Automated conversion with `pulumi convert`

The `pulumi convert` command can automatically translate Terraform configurations to Pulumi programs. Two converters read HCL, selected with `--from`:

* `--from terraform` is the long-standing Terraform converter. Reach for it for a one-off translation of Terraform configuration you have been running with the Terraform or OpenTofu CLI.
* `--from hcl` is the converter that ships alongside Pulumi's [HCL runtime](/docs/iac/languages-sdks/hcl/), and reads your configuration the same way the runtime executes it. Reach for it when you have been running your `.tf` files under `runtime: hcl` and now want that same program in another language.

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

# Convert with the HCL runtime's converter instead of the Terraform converter
$ pulumi convert --from hcl --language typescript --out ./pulumi-converted
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

// Configure the AWS provider
const awsProvider = new aws.Provider("aws", {
    region: awsRegion,
});

// Data source for Amazon Linux AMI
const amazonLinux = aws.ec2.getAmiOutput({
    mostRecent: true,
    owners: ["amazon"],
    filters: [{
        name: "name",
        values: ["amzn2-ami-hvm-*-x86_64-gp2"],
    }],
}, {
    provider: awsProvider,
});

// Create VPC
const main = new aws.ec2.Vpc("main", {
    cidrBlock: "10.0.0.0/16",
    enableDnsHostnames: true,
    enableDnsSupport: true,
    tags: {
        Name: "main-vpc",
    },
}, {
    provider: awsProvider,
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
}, {
    provider: awsProvider,
});

// Create internet gateway
const mainIgw = new aws.ec2.InternetGateway("main", {
    vpcId: main.id,
    tags: {
        Name: "main-igw",
    },
}, {
    provider: awsProvider,
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
}, {
    provider: awsProvider,
});

// Associate route table with subnet
const publicRtAssociation = new aws.ec2.RouteTableAssociation("public", {
    subnetId: publicSubnet.id,
    routeTableId: publicRt.id,
}, {
    provider: awsProvider,
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
}, {
    provider: awsProvider,
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
}, {
    provider: awsProvider,
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

# Configure the AWS provider
aws_provider = aws.Provider("aws", region=aws_region)

# Data source for Amazon Linux AMI
amazon_linux = aws.ec2.get_ami(
    most_recent=True,
    owners=["amazon"],
    filters=[{
        "name": "name",
        "values": ["amzn2-ami-hvm-*-x86_64-gp2"],
    }],
    opts=pulumi.InvokeOptions(provider=aws_provider)
)

# Create VPC
main_vpc = aws.ec2.Vpc("main",
    cidr_block="10.0.0.0/16",
    enable_dns_hostnames=True,
    enable_dns_support=True,
    tags={
        "Name": "main-vpc",
    },
    opts=pulumi.ResourceOptions(provider=aws_provider)
)

# Create public subnet
public_subnet = aws.ec2.Subnet("public",
    vpc_id=main_vpc.id,
    cidr_block="10.0.1.0/24",
    availability_zone="us-west-2a",
    map_public_ip_on_launch=True,
    tags={
        "Name": "public-subnet",
    },
    opts=pulumi.ResourceOptions(provider=aws_provider)
)

# Create internet gateway
main_igw = aws.ec2.InternetGateway("main",
    vpc_id=main_vpc.id,
    tags={
        "Name": "main-igw",
    },
    opts=pulumi.ResourceOptions(provider=aws_provider)
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
    },
    opts=pulumi.ResourceOptions(provider=aws_provider)
)

# Associate route table with subnet
public_rt_association = aws.ec2.RouteTableAssociation("public",
    subnet_id=public_subnet.id,
    route_table_id=public_rt.id,
    opts=pulumi.ResourceOptions(provider=aws_provider)
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
    },
    opts=pulumi.ResourceOptions(provider=aws_provider)
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
    },
    opts=pulumi.ResourceOptions(provider=aws_provider)
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
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws"
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

		// Configure the AWS provider
		awsProvider, err := aws.NewProvider(ctx, "aws", &aws.ProviderArgs{
			Region: pulumi.StringPtr(awsRegion),
		})
		if err != nil {
			return err
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
		}, pulumi.Provider(awsProvider))
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
		}, pulumi.Provider(awsProvider))
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
		}, pulumi.Provider(awsProvider))
		if err != nil {
			return err
		}

		// Create internet gateway
		mainIgw, err := ec2.NewInternetGateway(ctx, "main", &ec2.InternetGatewayArgs{
			VpcId: mainVpc.ID(),
			Tags: pulumi.StringMap{
				"Name": pulumi.String("main-igw"),
			},
		}, pulumi.Provider(awsProvider))
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
		}, pulumi.Provider(awsProvider))
		if err != nil {
			return err
		}

		// Associate route table with subnet
		_, err = ec2.NewRouteTableAssociation(ctx, "public", &ec2.RouteTableAssociationArgs{
			SubnetId:     publicSubnet.ID(),
			RouteTableId: publicRt.ID(),
		}, pulumi.Provider(awsProvider))
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
		}, pulumi.Provider(awsProvider))
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
		}, pulumi.Provider(awsProvider))
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

    // Configure the AWS provider
    var awsProvider = new Pulumi.Aws.Provider("aws", new Pulumi.Aws.ProviderArgs
    {
        Region = awsRegion,
    });

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
    }, new InvokeOptions { Provider = awsProvider });

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
    }, new CustomResourceOptions { Provider = awsProvider });

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
    }, new CustomResourceOptions { Provider = awsProvider });

    // Create internet gateway
    var mainIgw = new InternetGateway("main", new InternetGatewayArgs
    {
        VpcId = mainVpc.Id,
        Tags = new Dictionary<string, string>
        {
            ["Name"] = "main-igw",
        },
    }, new CustomResourceOptions { Provider = awsProvider });

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
    }, new CustomResourceOptions { Provider = awsProvider });

    // Associate route table with subnet
    var publicRtAssociation = new RouteTableAssociation("public", new RouteTableAssociationArgs
    {
        SubnetId = publicSubnet.Id,
        RouteTableId = publicRt.Id,
    }, new CustomResourceOptions { Provider = awsProvider });

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
    }, new CustomResourceOptions { Provider = awsProvider });

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
    }, new CustomResourceOptions { Provider = awsProvider });

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
import com.pulumi.aws.Provider;
import com.pulumi.aws.ProviderArgs;
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
import com.pulumi.deployment.InvokeOptions;
import com.pulumi.resources.CustomResourceOptions;

import java.util.List;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create configuration
            var config = new com.pulumi.Config();
            var awsRegion = config.get("awsRegion").orElse("us-west-2");
            var instanceType = config.get("instanceType").orElse("t3.micro");

            // Configure the AWS provider
            var awsProvider = new Provider("aws", ProviderArgs.builder()
                .region(awsRegion)
                .build());

            var providerOptions = CustomResourceOptions.builder()
                .provider(awsProvider)
                .build();

            // Data source for Amazon Linux AMI
            var amazonLinux = Ec2Functions.getAmi(GetAmiArgs.builder()
                .mostRecent(true)
                .owners("amazon")
                .filters(GetAmiFilterArgs.builder()
                    .name("name")
                    .values("amzn2-ami-hvm-*-x86_64-gp2")
                    .build())
                .build(),
                InvokeOptions.builder()
                    .provider(awsProvider)
                    .build());

            // Create VPC
            var mainVpc = new Vpc("main", VpcArgs.builder()
                .cidrBlock("10.0.0.0/16")
                .enableDnsHostnames(true)
                .enableDnsSupport(true)
                .tags(Map.of("Name", "main-vpc"))
                .build(), providerOptions);

            // Create public subnet
            var publicSubnet = new Subnet("public", SubnetArgs.builder()
                .vpcId(mainVpc.id())
                .cidrBlock("10.0.1.0/24")
                .availabilityZone("us-west-2a")
                .mapPublicIpOnLaunch(true)
                .tags(Map.of("Name", "public-subnet"))
                .build(), providerOptions);

            // Create internet gateway
            var mainIgw = new InternetGateway("main", InternetGatewayArgs.builder()
                .vpcId(mainVpc.id())
                .tags(Map.of("Name", "main-igw"))
                .build(), providerOptions);

            // Create route table
            var publicRt = new RouteTable("public", RouteTableArgs.builder()
                .vpcId(mainVpc.id())
                .routes(RouteTableRouteArgs.builder()
                    .cidrBlock("0.0.0.0/0")
                    .gatewayId(mainIgw.id())
                    .build())
                .tags(Map.of("Name", "public-rt"))
                .build(), providerOptions);

            // Associate route table with subnet
            var publicRtAssociation = new RouteTableAssociation("public", RouteTableAssociationArgs.builder()
                .subnetId(publicSubnet.id())
                .routeTableId(publicRt.id())
                .build(), providerOptions);

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
                .build(), providerOptions);

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
                .build(), providerOptions);

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
      options:
        provider: ${aws-provider}

resources:
  # Configure the AWS provider
  aws-provider:
    type: pulumi:providers:aws
    properties:
      region: ${awsRegion}

  # Create VPC
  main:
    type: aws:ec2:Vpc
    properties:
      cidrBlock: 10.0.0.0/16
      enableDnsHostnames: true
      enableDnsSupport: true
      tags:
        Name: main-vpc
    options:
      provider: ${aws-provider}

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
    options:
      provider: ${aws-provider}

  # Create internet gateway
  main-igw:
    type: aws:ec2:InternetGateway
    properties:
      vpcId: ${main.id}
      tags:
        Name: main-igw
    options:
      provider: ${aws-provider}

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
    options:
      provider: ${aws-provider}

  # Associate route table with subnet
  public-rt-association:
    type: aws:ec2:RouteTableAssociation
    properties:
      subnetId: ${public.id}
      routeTableId: ${public-rt.id}
    options:
      provider: ${aws-provider}

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
    options:
      provider: ${aws-provider}

  # Create EC2 instance
  web:
    type: aws:ec2:Instance
    properties:
      ami: ${amazonLinux.id}
      instanceType: ${instanceType}
      subnetId: ${public.id}
      vpcSecurityGroupIds: ["${web-sg.id}"]
      userData: |
        #!/bin/bash
        yum update -y
        yum install -y httpd
        systemctl start httpd
        systemctl enable httpd
        echo "<h1>Hello from Pulumi converted infrastructure!</h1>" > /var/www/html/index.html
      tags:
        Name: web-server
    options:
      provider: ${aws-provider}

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
$ pulumi stack init dev
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

The resource IDs below (`vpc-12345`, `subnet-67890`, `i-abcdef123`) are placeholders. Replace them with the actual IDs of your existing resources, which you can find in your Terraform state (for example, with `terraform state show <resource>`) or in your cloud provider's console. Run these commands from within your converted Pulumi project directory.

```bash
# Import individual resources by ID
$ pulumi import aws:ec2/vpc:Vpc main vpc-12345
$ pulumi import aws:ec2/subnet:Subnet public subnet-67890
$ pulumi import aws:ec2/instance:Instance web i-abcdef123

# Run preview to ensure no changes
$ pulumi preview

# Expected result: "no changes required"
```

For anything beyond a handful of resources, import in bulk from the Terraform state file instead:

```bash
$ pulumi import --from hcl terraform.tfstate
```

This reads a Terraform or OpenTofu state file and imports every managed resource in its root module in one pass. Resources nested inside modules are skipped with a warning, so import those individually with the per-resource form above. The state file itself is only read — Pulumi does not adopt or reuse it, and subsequent updates use Pulumi's own state.

This verification step is crucial when converting production infrastructure, as it confirms your Pulumi program exactly matches the existing Terraform-managed resources.

## AI-assisted conversion with the Pulumi MCP server

For complex Terraform configurations, you can use AI tools like [Claude](https://www.anthropic.com/claude-code) with the [Pulumi MCP (Model Context Protocol) server](/docs/ai/mcp-server/), which provides comprehensive Pulumi integration, including a specialized Terraform conversion prompt.

### Using the Pulumi MCP server (recommended)

The [Pulumi MCP server](/docs/ai/mcp-server/) enables AI assistants to interact with Pulumi programmatically. Beyond conversion, it provides full infrastructure management capabilities including stack operations, resource querying, and automated deployments.

The MCP server includes a sophisticated `convert-terraform-to-typescript` prompt that ensures:

* **Type safety**: Proper use of `pulumi.Input<T>` and `pulumi.Output<T>` types
* **Best practices**: Idiomatic TypeScript patterns and Pulumi conventions
* **Configuration handling**: Safe access to config values with null checking
* **Resource naming**: Consistent and descriptive resource naming
* **Multi-provider support**: Proper handling of multiple provider configurations

**Installation and setup:**

1. **Install via Claude Code** (if using Claude):

   ```bash
   $ claude mcp add --transport http pulumi https://mcp.ai.pulumi.com/mcp
   ```

   Follow the complete setup instructions in the [Pulumi MCP server docs](/docs/ai/mcp-server/).

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

### Alternative: manual prompt usage

If you prefer not to use the MCP server, you can access the conversion prompt directly:

1. **Access the prompt**: The "convert-terraform-to-typescript" prompt is available in the [Pulumi MCP server](/docs/ai/mcp-server/)

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

1. **Start small**: Convert smaller configurations first to understand the process
2. **Verify outputs**: Ensure converted code produces identical infrastructure
3. **Test thoroughly**: Write tests for critical infrastructure components
4. **Preserve structure**: Keep similar resource organization when possible
5. **Document changes**: Note any differences between original and converted code
6. **Version control**: Use Git to track conversion changes

{{< get-started-stepper >}}
