---
title_tag: First Look - Terraform HCL vs Pulumi Programs | Pulumi for Terraform Users
title: First Look - Terraform HCL vs Pulumi Programs
h1: "First Look - Terraform HCL vs Pulumi Programs"
stepper_link: "Try it out"
meta_desc: Compare Terraform HCL to Pulumi programs with a basic example showing key differences in infrastructure as code approaches.
weight: 3
menu:
    iac:
        name: First Look - Terraform HCL vs Pulumi Programs
        parent: terraform-get-started
        weight: 3
---

Let's try creating the same resources using both Terraform HCL and a Pulumi program. This basic example will also serve to verify your cloud connectivity.

## The Terraform way of doing things

In Terraform, if you wanted to query an AMI ID you might write something like this in [Hashicorp Configuration Language (HCL)](https://github.com/hashicorp/hcl/blob/main/hclsyntax/spec.md):

```hcl
data "aws_ami" "ubuntu" {
  region      = "us-west-2"
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

If you run this Terraform config, you should see output showing the latest Ubuntu AMI information. However, it's important to note that HCL is *not* a programming language. It is a configuration language, similar to YAML or JSON, with a bit more expressiveness and modularization capabilities. In Pulumi, you use general purpose programming languages to express your desired state of your cloud resources, in the context of a Pulumi program.

## Pulumi programs

Let's try creating the same resources in a Pulumi program. The key difference between Terraform and Pulumi is that Pulumi allows you to use your preferred programming language instead of HCL. Both approaches query the same AWS API and return identical results:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

```bash
$ mkdir pulumi-terraform-test && cd pulumi-terraform-test
$ pulumi new aws-typescript --yes
```

Replace the contents of `index.ts` with:

```typescript
import * as aws from "@pulumi/aws";

// Query existing Ubuntu AMIs (read-only operation)
const ubuntu = aws.ec2.getAmiOutput({
    region: "us-west-2",
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
$ mkdir pulumi-terraform-test && cd pulumi-terraform-test
$ pulumi new aws-python --yes
```

Replace the contents of `__main__.py` with:

```python
import pulumi
import pulumi_aws as aws

# Query existing Ubuntu AMIs (read-only operation)
ubuntu = aws.ec2.get_ami(
    region="us-west-2",
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
$ mkdir pulumi-terraform-test && cd pulumi-terraform-test
$ pulumi new aws-go --yes
```

Replace the contents of `main.go` with:

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Query existing Ubuntu AMIs (read-only operation)
		ubuntu, err := ec2.LookupAmi(ctx, &ec2.LookupAmiArgs{
            Region: pulumi.StringRef("us-west-2"),
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
$ mkdir pulumi-terraform-test && cd pulumi-terraform-test
$ pulumi new aws-csharp --yes
```

Replace the contents of `Program.cs` with:

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Aws.Ec2.Inputs;

return await Deployment.RunAsync(() =>
{
    // Query existing Ubuntu AMIs (read-only operation)
    var ubuntu = GetAmi.Invoke(new()
    {
        Region = "us-west-2",
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
$ mkdir pulumi-terraform-test && cd pulumi-terraform-test
$ pulumi new aws-java --yes
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
                .region("us-west-2")
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
$ mkdir pulumi-terraform-test && cd pulumi-terraform-test
$ pulumi new aws-yaml --yes
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
        region: us-west-2
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
$ pulumi up
```

You should see output showing the latest Ubuntu AMI information, confirming that Pulumi can successfully query your AWS environment.

## Clean up

Remove the test resources:

```bash
$ pulumi destroy --yes
$ pulumi stack rm --yes
$ cd .. && rm -rf pulumi-terraform-test
```

{{< get-started-stepper >}}
