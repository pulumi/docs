---
title: "Using Terraform Remote State with Pulumi"
authors: ["paul-stack"]
tags: ["Infrastructure","Features"]
date: "2019-06-07"
meta_desc: "Pulumi allows resources which were provisioned by CloudFormation, ARM, or Terraform to remain, while allowing those resources to be consumed by Pulumi."

---

While some people coming to Pulumi are entirely new to Infrastructure as
Code, increasingly teams are moving from other tools - whether
cloud-specific in the form of
[CloudFormation](https://aws.amazon.com/cloudformation/) or
[ARM Templates](https://docs.microsoft.com/en-us/azure/azure-resource-manager/),
or cloud-agnostic tools such as [Terraform](https://terraform.io). In
these organizations, new infrastructure provisioned with Pulumi must
co-exist with existing resources provisioned with other tools, and often
by different teams. For example, it's common to see an application team
deploying into a VPC owned and managed by a network operations team.

Pulumi supports
[this kind of workflow]({{< prelref "/docs/intro/concepts/organizing-stacks-projects#inter-stack-dependencies" >}})
natively using the [`StackReference`]({{< prelref "/docs/reference/pkg/nodejs/pulumi/pulumi#StackReference" >}})
type from the Pulumi SDK. Integration with the most popular
cloud-specific tools have been supported by Pulumi since the earliest
days:

- The [`aws.cloudformation.getStack()`]({{< prelref "/docs/reference/pkg/nodejs/pulumi/aws/cloudformation#getStack" >}})
  function can be used to obtain the outputs from a CloudFormation
  Stack.

- The [`get`]({{< prelref "/docs/reference/pkg/nodejs/pulumi/azure/core#TemplateDeployment-get" >}})
  method of the
  [`azure.core.TemplateDeployment`]({{< prelref "/docs/reference/pkg/nodejs/pulumi/azure/core#TemplateDeployment" >}})
  class can be used to obtain the outputs of an ARM Template Deployment.

We recently added similar support for reading the outputs of a Terraform
state file - both from local `.tfstate` files, and from all of the
remote state backends supported by Terraform. This is exposed via the
[`terraform.state.RemoteStateReference`]({{< prelref "/docs/reference/pkg/nodejs/pulumi/terraform/state#RemoteStateReference" >}}) type in the
[`@pulumi/terraform`](https://www.npmjs.com/package/@pulumi/terraform)
NPM package.
<!--more-->

## Example - Terraform Enterprise Backend

To demonstrate the use of the `RemoteStateReference` type, let's imagine
we want to use the IDs of subnets in a simple AWS VPC was defined by
another team using Terraform 0.12, with remote state stored in Terraform
Enterprise, using the following HCL:

```
  terraform {
    required_version = ">= 0.12"

    backend "remote" {
      organization = "acme"

      workspaces {
        name = "production"
      }
    }
  }

  provider "aws" {
    region = "us-west-2"
  }

  resource "aws_vpc" "vpc" {
    cidr_block = "172.21.0.0/16"

    tags = {
      Name = "VPC"
    }
  }

  resource "aws_internet_gateway" "gw" {
    vpc_id = aws_vpc.vpc.id

    tags = {
      Name = "VPC IG"
    }
  }

  resource "aws_subnet" "public" {
    count = 2

    cidr_block = "172.21.${count.index}.0/24"
    vpc_id = aws_vpc.vpc.id
    map_public_ip_on_launch = true

    tags = {
      Name = "Public Subnet ${count.index +1}"
    }
  }

  resource "aws_route_table" "rt_public" {
    vpc_id = aws_vpc.vpc.id

    route {
      cidr_block = "0.0.0.0/0"
      gateway_id = aws_internet_gateway.gw.id
    }

    tags = {
      Name = "VPC Public"
    }
  }

  output "vpc_id" {
    value = aws_vpc.vpc.id
  }

  output "public_subnet_ids" {
    value = aws_subnet.public.*.id
  }
```

To consume the outputs of this Terraform state in our Pulumi program we
can do the following:

1. Create a new Pulumi program written in TypeScript

        $ pulumi new --yes typescript

2. Install the `@pulumi/terraform` package from NPM:

        $ npm install @pulumi/terraform

3. In the `index.ts` file, create a
    `terraform.state.RemoteStateReference` resource to access the state.
    Note that we can use [Pulumi
    secrets]({{< prelref "managing-secrets-with-pulumi" >}})
    to ensure that our Terraform Enterprise token is encrypted and never
    stored in plaintext by Pulumi:

    ```typescript
    import * as pulumi from "@pulumi/pulumi";
    import * as terraform from "@pulumi/terraform";

    const config = new pulumi.Config();
    const tfeToken = config.requireSecret("tfeToken");

    const networkState = new terraform.state.RemoteStateReference("network", {
        backendType: "remote",
        token: tfeToken,
        organization: "acme",
        workspaces: {
            name: "production-network"
        },
    });
    ```

4. We can now use either the `outputs` property or the `getOutput()`
    function on `networkState` to obtain individual outputs:

    ```typescript
    const vpcId = networkState.getOutput("vpc_id");
    const publicSubnetIds = networkState.outputs["public_subnet_ids"] as pulumi.Output<string[]>;

    // Create our webservers in each subnet
    for (let i = 0; i < 2; i++) {
        new aws.ec2.Instance(`instance${i}`, {
            ami: nginxAmi,
            instanceType: "t2.medium",
            subnetId: publicSubnetIds[i],
        })
    }
    ```

Using Pulumi to read the outputs of other deployment tools provides a
great deal of flexibility for adopting Pulumi into existing
environments. Resources which were provisioned by CloudFormation, ARM or
Terraform can remain in place, while still allowing those values to be
dynamically consumed by a Pulumi program.

Pulumi is free and open-source, and you can [get started today]({{< prelref "/docs/get-started" >}}).
To learn more about migrating
from Terraform to Pulumi, check out
[From Terraform to Infrastructure as Software]({{< prelref "from-terraform-to-infrastructure-as-software" >}})
and the [Terraform comparison documentation]({{< prelref "/docs/intro/vs/terraform" >}}), or join us in
the [Pulumi Community Slack](https://slack.pulumi.com/) to discuss with
the Pulumi community.
