---
title_tag: Install and Configure | Pulumi for Terraform Users
title: Install and Configure
h1: "Get started with Pulumi for Terraform Users"
stepper_link: "I'm ready to begin"
meta_desc: This page provides setup instructions for Pulumi alongside existing Terraform infrastructure.
weight: 2
menu:
    iac:
        name: Install and Configure
        parent: terraform-get-started
        weight: 2

aliases:
- /docs/iac/get-started/terraform/begin/
---

## Install Pulumi

Download and install Pulumi alongside your existing Terraform setup:

{{< install-pulumi >}}
{{% notes info %}}
All Windows examples in this tutorial assume you are running in PowerShell.
{{% /notes %}}
{{< /install-pulumi >}}

## Configure cloud provider

Pulumi can use the same cloud provider credentials as Terraform.
If you're already using Terraform with AWS, your existing configuration will work with Pulumi.

### AWS configuration

If you have AWS credentials configured for Terraform, Pulumi will automatically use them.
You can verify your configuration:

```bash
aws sts get-caller-identity
```

If you need to configure AWS credentials, you can:

* Use the AWS CLI: `aws configure`
* Set environment variables: `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
* Use IAM roles for EC2 instances or Lambda functions

{{% notes info %}}
For teams managing multiple environments, consider [Pulumi ESC](/docs/esc/) for centralized credential management that works with both Terraform and Pulumi.
{{% /notes %}}

## Verify installation

Test that Pulumi is properly installed and can access your cloud provider:

```bash
pulumi version
```

Create a simple test to verify cloud connectivity:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

```bash
mkdir pulumi-terraform-test && cd pulumi-terraform-test
pulumi new typescript --yes
```

Replace the contents of `index.ts` with:

```typescript
import * as aws from "@pulumi/aws";

// Query existing Ubuntu AMIs (read-only operation)
const ubuntu = aws.ec2.getAmiOutput({
    mostRecent: true,
    owners: ["099720109477"], // Canonical
    filters: [
        {
            name: "name",
            values: ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"],
        },
    ],
});

export const latestUbuntuAmiId = ubuntu.id;
export const latestUbuntuAmiName = ubuntu.name;
```

{{% /choosable %}}

{{% choosable language "python" %}}

```bash
mkdir pulumi-terraform-test && cd pulumi-terraform-test
pulumi new python --yes
```

Replace the contents of `__main__.py` with:

```python
import pulumi
import pulumi_aws as aws

# Query existing Ubuntu AMIs (read-only operation)
ubuntu = aws.ec2.get_ami(
    most_recent=True,
    owners=["099720109477"],  # Canonical
    filters=[
        {
            "name": "name",
            "values": ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"],
        }
    ],
)

pulumi.export("latestUbuntuAmiId", ubuntu.id)
pulumi.export("latestUbuntuAmiName", ubuntu.name)
```

{{% /choosable %}}

{{% choosable language "go" %}}

```bash
mkdir pulumi-terraform-test && cd pulumi-terraform-test
pulumi new go --yes
```

Replace the contents of `main.go` with:

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Query existing Ubuntu AMIs (read-only operation)
		ubuntu, err := ec2.LookupAmi(ctx, &ec2.LookupAmiArgs{
			MostRecent: pulumi.BoolRef(true),
			Owners:     []string{"099720109477"}, // Canonical
			Filters: []ec2.GetAmiFilter{
				{
					Name:   "name",
					Values: []string{"ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"},
				},
			},
		})
		if err != nil {
			return err
		}

		ctx.Export("latestUbuntuAmiId", pulumi.String(ubuntu.Id))
		ctx.Export("latestUbuntuAmiName", pulumi.String(ubuntu.Name))
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

```bash
mkdir pulumi-terraform-test && cd pulumi-terraform-test
pulumi new csharp --yes
```

Replace the contents of `Program.cs` with:

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Aws.Ec2;

return await Deployment.RunAsync(() =>
{
    // Query existing Ubuntu AMIs (read-only operation)
    var ubuntu = GetAmi.Invoke(new()
    {
        MostRecent = true,
        Owners = new[] { "099720109477" }, // Canonical
        Filters = new[]
        {
            new GetAmiFilterInputArgs
            {
                Name = "name",
                Values = new[] { "ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*" },
            },
        },
    });

    return new Dictionary<string, object?>
    {
        ["latestUbuntuAmiId"] = ubuntu.Apply(ubuntu => ubuntu.Id),
        ["latestUbuntuAmiName"] = ubuntu.Apply(ubuntu => ubuntu.Name),
    };
});
```

{{% /choosable %}}

{{% choosable language "java" %}}

```bash
mkdir pulumi-terraform-test && cd pulumi-terraform-test
pulumi new java --yes
```

Replace the contents of `src/main/java/myproject/App.java` with:

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.ec2.Ec2Functions;
import com.pulumi.aws.ec2.inputs.GetAmiArgs;
import com.pulumi.aws.ec2.inputs.GetAmiFilterArgs;
import com.pulumi.core.Output;

import java.util.List;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Query existing Ubuntu AMIs (read-only operation)
            var ubuntu = Ec2Functions.getAmi(GetAmiArgs.builder()
                .mostRecent(true)
                .owners("099720109477") // Canonical
                .filters(GetAmiFilterArgs.builder()
                    .name("name")
                    .values("ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*")
                    .build())
                .build());

            ctx.export("latestUbuntuAmiId", ubuntu.applyValue(ami -> ami.id()));
            ctx.export("latestUbuntuAmiName", ubuntu.applyValue(ami -> ami.name()));
        });
    }
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

```bash
mkdir pulumi-terraform-test && cd pulumi-terraform-test
pulumi new yaml --yes
```

Replace the contents of `Pulumi.yaml` with:

```yaml
name: pulumi-terraform-test
runtime: yaml
description: Test Pulumi and AWS connectivity

variables:
  ubuntu:
    fn::invoke:
      function: aws:ec2:getAmi
      arguments:
        mostRecent: true
        owners: ["099720109477"] # Canonical
        filters:
          - name: name
            values: ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]

outputs:
  latestUbuntuAmiId: ${ubuntu.id}
  latestUbuntuAmiName: ${ubuntu.name}
```

{{% /choosable %}}

Run the test:

```bash
pulumi up
```

You should see output showing the latest Ubuntu AMI information, confirming that Pulumi can successfully query your AWS environment.

## Comparison with Terraform

The example above demonstrates the same functionality as this Terraform data source:

```hcl
# Terraform equivalent
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}

output "latest_ubuntu_ami_id" {
  value = data.aws_ami.ubuntu.id
}

output "latest_ubuntu_ami_name" {
  value = data.aws_ami.ubuntu.name
}
```

Both approaches query the same AWS API and return identical results.
The key difference is that Pulumi uses your chosen programming language instead of HCL.

## Clean up

Remove the test resources:

```bash
pulumi destroy --yes
cd .. && rm -rf pulumi-terraform-test
```

{{< get-started-stepper >}}