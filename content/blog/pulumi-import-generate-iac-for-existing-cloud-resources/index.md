---
title: "Pulumi Import: Generate IaC for Existing Cloud Resources"
date: "2020-11-24"
meta_desc: "Introducing the new pulumi import command that will automatically scaffold your Pulumi application code when importing existing cloud resources."
meta_image: cloud_engineering.png
authors: ["paul-stack"]
tags: ["import","New-Features", "Pulumi-News", "Features"]
---

Most infrastructure projects require working with existing cloud resources, either by building on top of existing resources
or adopting existing resources under management with a new and more robust infrastructure provisioning solution.

In June 2019, Pulumi introduced the ability to [import existing infrastructure resources to be under Pulumi management](https://www.pulumi.com/docs/guides/adopting/import/)
no matter how you’ve provisioned these resources — manually in your cloud provider’s console or CLI, using an infrastructure
as code tool like Terraform or AWS CloudFormation. Today, we are happy to announce a richer resource import experience.

As of [v2.12.0](https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#2120-2020-10-14), Pulumi has introduced
a `pulumi import` command. This command will import the cloud resource into the Pulumi state and generate the code
for the user's Pulumi program in the appropriate language.

<!--more-->

## The Anatomy of the Import Command

No matter how resources have been provisioned in the cloud, Pulumi enables you to adopt and manage those resources as
part of your infrastructure project. The `pulumi import` command is made of the following:

```bash
pulumi import [type] [name] [id]
```

When Pulumi performs an import, the resource is added to the Pulumi [state](https://www.pulumi.com/docs/intro/concepts/state/#state),
it is marked as a [protected]({{< relref "/docs/intro/concepts/resources#protect" >}}) resource (by default),
and it will emit the generated code that the user can add to their program before running a `pulumi up`. The resources are
marked as protected to ensure that imported infrastructure is not accidentally deleted if the user forgets to include
the code for the resource in their program before doing a deployment.

### Importing an S3 Bucket

A resource needs to be imported into an existing Pulumi project. Let's consider that a user wants to import an S3 bucket
manually created in their AWS Account. To do this, we can execute the following command:

```bash
pulumi import aws:s3/bucket:Bucket infra-logs company-infra-logs
```

This command instructs Pulumi to import the S3 bucket called `company-infra-logs` with the Pulumi resource name
`infra-logs`. The import command will output as follows:

{{< asciicast id="374902" >}}

The user can then see the generated code they need to use as part of their application. I imported this resource into a
TypeScript application:

{{< chooser language "typescript,python,csharp,go" >}}

{{< choosable language typescript >}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const demo = new aws.s3.Bucket("infra-logs", {
    acl: "private",
    bucket: "company-infra-logs",
    forceDestroy: false,
}, {
    protect: true,
});
```

{{< /choosable >}}
{{< choosable language python >}}

```python
import pulumi
import pulumi_aws as aws

demo = aws.s3.Bucket("infra-logs",
    acl="private",
    bucket="company-infra-logs",
    force_destroy=False,
    opts=ResourceOptions(protect=True))
```

{{< /choosable >}}
{{< choosable language go >}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := s3.NewBucket(ctx, "infra-logs", &s3.BucketArgs{
			Acl:          pulumi.String("private"),
			Bucket:       pulumi.String("company-infra-logs"),
			ForceDestroy: pulumi.Bool(false),
		}, pulumi.Protect(true))
		if err != nil {
			return err
		}
		return nil
	})
}
```

{{< /choosable >}}
{{< choosable language csharp >}}

```csharp
using Pulumi;
using Aws = Pulumi.Aws;

class MyStack : Stack
{
    public MyStack()
    {
        var demo = new Aws.S3.Bucket("infra-logs", new Aws.S3.BucketArgs
        {
            Acl = "private",
            Bucket = "company-infra-logs",
            ForceDestroy = false,
        }, new CustomResourceOptions
        {
            Protect = true,
        });
    }

}
```

{{< /choosable >}}
{{< /chooser >}}

This is valid Pulumi application code and can be added to your Pulumi application. Notice that the Pulumi resource is
marked as `protect: true`. This means Pulumi will not delete that resource unless this protection attribute is removed
from the resource. If this code is not added to your Pulumi application, then a Pulumi update will return the following:

```bash
Diagnostics:
  pulumi:pulumi:Stack (import-example-dev):
    error: preview failed

  aws:s3:Bucket (demo):
    error: Preview failed: refusing to delete protected resource 'urn:pulumi:dev::import-example::aws:s3/bucket:Bucket::infra-logs'
```

## Importing Multiple Resources

Should a user need to import multiple resources to be managed by Pulumi, the CLI `import command` can handle this
scenario for us. This is helpful when using the pulumi import command as part of scripting larger bulk imports of
cloud resource:

```json
{
	"resources": [{
			"type": "aws:ec2/vpc:Vpc",
			"name": "application-vpc",
			"id": "vpc-0ad77710973388316"
		},
		{
			"type": "aws:ec2/subnet:Subnet",
			"name": "public-1",
			"id": "subnet-0fb5fdff92b9e5a3b"
		},
		{
			"type": "aws:ec2/subnet:Subnet",
			"name": "private-1",
			"id": "subnet-0a39d25dd9f7b7808"
		}
	]
}
```

We can then run the command:

```bash
pulumi import -f resources.json
```

{{< asciicast id="374901" >}}

We can see the resultant code generation:

{{< chooser language "typescript,python,csharp,go" >}}

{{< choosable language typescript >}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const application_vpc = new aws.ec2.Vpc("application-vpc", {
    assignGeneratedIpv6CidrBlock: false,
    cidrBlock: "172.16.0.0/16",
    enableDnsSupport: true,
    instanceTenancy: "default",
    tags: {
        Name: "pulumi-vpc",
        Owner: "pulumi",
        Project: "pulumi-k8s-aws-cluster",
    },
}, {
    protect: true,
});
const public_1 = new aws.ec2.Subnet("public-1", {
    assignIpv6AddressOnCreation: false,
    cidrBlock: "172.16.32.0/19",
    mapPublicIpOnLaunch: true,
    tags: {
        Name: "pulumi-vpc-public-1",
        Owner: "pulumi",
        Project: "pulumi-k8s-aws-cluster",
        "kubernetes.io/role/elb": "1",
        type: "public",
    },
    vpcId: "vpc-0ad77710973388316",
}, {
    protect: true,
});
const private_1 = new aws.ec2.Subnet("private-1", {
    assignIpv6AddressOnCreation: false,
    cidrBlock: "172.16.160.0/19",
    mapPublicIpOnLaunch: false,
    tags: {
        Name: "pulumi-vpc-private-1",
        Owner: "pulumi",
        Project: "pulumi-k8s-aws-cluster",
        "kubernetes.io/role/internal-elb": "1",
        type: "private",
    },
    vpcId: "vpc-0ad77710973388316",
}, {
    protect: true,
});
```

{{< /choosable >}}
{{< choosable language python >}}

```python
import pulumi
import pulumi_aws as aws

application_vpc = aws.ec2.Vpc("application-vpc",
    assign_generated_ipv6_cidr_block=False,
    cidr_block="172.16.0.0/16",
    enable_dns_support=True,
    instance_tenancy="default",
    tags={
        "Name": "pulumi-vpc",
        "Owner": "pulumi",
        "Project": "pulumi-k8s-aws-cluster",
    },
    opts=ResourceOptions(protect=True))
public_1 = aws.ec2.Subnet("public-1",
    assign_ipv6_address_on_creation=False,
    cidr_block="172.16.32.0/19",
    map_public_ip_on_launch=True,
    tags={
        "Name": "pulumi-vpc-public-1",
        "Owner": "pulumi",
        "Project": "pulumi-k8s-aws-cluster",
        "kubernetes.io/role/elb": "1",
        "type": "public",
    },
    vpc_id="vpc-0ad77710973388316",
    opts=ResourceOptions(protect=True))
private_1 = aws.ec2.Subnet("private-1",
    assign_ipv6_address_on_creation=False,
    cidr_block="172.16.160.0/19",
    map_public_ip_on_launch=False,
    tags={
        "Name": "pulumi-vpc-private-1",
        "Owner": "pulumi",
        "Project": "pulumi-k8s-aws-cluster",
        "kubernetes.io/role/internal-elb": "1",
        "type": "private",
    },
    vpc_id="vpc-0ad77710973388316",
    opts=ResourceOptions(protect=True))
```

{{< /choosable >}}
{{< choosable language go >}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := ec2.NewVpc(ctx, "application_vpc", &ec2.VpcArgs{
			AssignGeneratedIpv6CidrBlock: pulumi.Bool(false),
			CidrBlock:                    pulumi.String("172.16.0.0/16"),
			EnableDnsSupport:             pulumi.Bool(true),
			InstanceTenancy:              pulumi.String("default"),
			Tags: pulumi.StringMap{
				"Name":    pulumi.String("pulumi-vpc"),
				"Owner":   pulumi.String("pulumi"),
				"Project": pulumi.String("pulumi-k8s-aws-cluster"),
			},
		}, pulumi.Protect(true))
		if err != nil {
			return err
		}
		_, err = ec2.NewSubnet(ctx, "public_1", &ec2.SubnetArgs{
			AssignIpv6AddressOnCreation: pulumi.Bool(false),
			CidrBlock:                   pulumi.String("172.16.32.0/19"),
			MapPublicIpOnLaunch:         pulumi.Bool(true),
			Tags: pulumi.StringMap{
				"Name":                   pulumi.String("pulumi-vpc-public-1"),
				"Owner":                  pulumi.String("pulumi"),
				"Project":                pulumi.String("pulumi-k8s-aws-cluster"),
				"kubernetes.io/role/elb": pulumi.String("1"),
				"type":                   pulumi.String("public"),
			},
			VpcId: pulumi.String("vpc-0ad77710973388316"),
		}, pulumi.Protect(true))
		if err != nil {
			return err
		}
		_, err = ec2.NewSubnet(ctx, "private_1", &ec2.SubnetArgs{
			AssignIpv6AddressOnCreation: pulumi.Bool(false),
			CidrBlock:                   pulumi.String("172.16.160.0/19"),
			MapPublicIpOnLaunch:         pulumi.Bool(false),
			Tags: pulumi.StringMap{
				"Name":                            pulumi.String("pulumi-vpc-private-1"),
				"Owner":                           pulumi.String("pulumi"),
				"Project":                         pulumi.String("pulumi-k8s-aws-cluster"),
				"kubernetes.io/role/internal-elb": pulumi.String("1"),
				"type":                            pulumi.String("private"),
			},
			VpcId: pulumi.String("vpc-0ad77710973388316"),
		}, pulumi.Protect(true))
		if err != nil {
			return err
		}
		return nil
	})
}
```

{{< /choosable >}}
{{< choosable language csharp >}}

```csharp
using Pulumi;
using Aws = Pulumi.Aws;

class MyStack : Stack
{
    public MyStack()
    {
        var application_vpc = new Aws.Ec2.Vpc("application-vpc", new Aws.Ec2.VpcArgs
        {
            AssignGeneratedIpv6CidrBlock = false,
            CidrBlock = "172.16.0.0/16",
            EnableDnsSupport = true,
            InstanceTenancy = "default",
            Tags =
            {
                { "Name", "pulumi-vpc" },
                { "Owner", "pulumi" },
                { "Project", "pulumi-k8s-aws-cluster" },
            },
        }, new CustomResourceOptions
        {
            Protect = true,
        });
        var public_1 = new Aws.Ec2.Subnet("public-1", new Aws.Ec2.SubnetArgs
        {
            AssignIpv6AddressOnCreation = false,
            CidrBlock = "172.16.32.0/19",
            MapPublicIpOnLaunch = true,
            Tags =
            {
                { "Name", "pulumi-vpc-public-1" },
                { "Owner", "pulumi" },
                { "Project", "pulumi-k8s-aws-cluster" },
                { "kubernetes.io/role/elb", "1" },
                { "type", "public" },
            },
            VpcId = "vpc-0ad77710973388316",
        }, new CustomResourceOptions
        {
            Protect = true,
        });
        var private_1 = new Aws.Ec2.Subnet("private-1", new Aws.Ec2.SubnetArgs
        {
            AssignIpv6AddressOnCreation = false,
            CidrBlock = "172.16.160.0/19",
            MapPublicIpOnLaunch = false,
            Tags =
            {
                { "Name", "pulumi-vpc-private-1" },
                { "Owner", "pulumi" },
                { "Project", "pulumi-k8s-aws-cluster" },
                { "kubernetes.io/role/internal-elb", "1" },
                { "type", "private" },
            },
            VpcId = "vpc-0ad77710973388316",
        }, new CustomResourceOptions
        {
            Protect = true,
        });
    }

}
```

{{< /choosable >}}
{{< /chooser >}}

Check out the video clip below for a demo.

{{< youtube "6qHVbu8vb4w" >}}

## Documentation

Full CLI Documentation is [available](https://www.pulumi.com/docs/reference/cli/pulumi_import/), showing all of the different
import command flags. The flags include writing directly to a file and the ability to ensure
a resource is not protected on import. Examples of importing resources can be found on their specifc resource documentation
pages. Such an example for importing a VPC can be found in the [VPC import documentation](https://www.pulumi.com/docs/reference/pkg/aws/ec2/vpc/#import).
