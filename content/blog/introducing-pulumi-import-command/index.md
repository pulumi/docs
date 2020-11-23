---
title: "Introducing The Pulumi Import Command"
date: "2020-11-23"
meta_desc: "Introducing the new pulumi import command that will scaffold your Pulumi application code."
authors: ["paul-stack"]
tags: ["import","New-Features", "Pulumi-News", "Features"]
---

In June 2019, Pulumi introduced the ability to import existing infrastructure resources to be part of Pulumi management.
Today, we are happy to announce a richer resource import experience.

As of [v2.12.0](https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#2120-2020-10-14), Pulumi has introduced
a `pulumi import` command. This command will not only import the resource, but it will also ensure that the user
can have the resource code, in the appropriate language, available for their use.

<!--more-->

## The Anatomy of the Import Command

No matter how resources have been provisioned in the cloud, Pulumi enables you to adopt and manage those resources as
part of your infrastructure project. The `pulumi import` command is made of the following:

```bash
pulumi import [type] [name] [id]
```

By default, Pulumi will import your resource and mark that resource as "protected". This means that the resource can not
be destroyed unless the resource is specifically opted out of the protection.

### Importing an S3 Bucket

A resource needs to be imported into an existing Pulumi project. Let's consider that a user wants to import an S3 bucket
that was manually created in their AWS Account. To do this, we can execute the following command:

```bash
pulumi import aws:s3/bucket:Bucket infra-logs cloud-infra-logs
```

This command instructs Pulumi to import the S3 bucket called `cloud-infra-logs` with the Pulumi resource name
`infra-logs`. The import command will output as follows:

```bash
Previewing import (dev)

View Live: https://app.pulumi.com/demo/import-example/dev/previews/74cafc2f-e9b8-42b1-9da2-09d1330b7950

     Type                 Name                 Plan
 +   pulumi:pulumi:Stack  import-example-dev   create
 =   └─ aws:s3:Bucket     demo                 import

Resources:
    + 1 to create
    = 1 to import
    2 changes

Do you want to perform this import?  [Use arrows to move, enter to select, type to filter]
  yes
> no
  details
```

Let's instruct Pulumi to continue to import:

```bash
Importing (dev)

View Live: https://app.pulumi.com/demo/import-example/dev/updates/1

     Type                 Name                 Status
 +   pulumi:pulumi:Stack  import-example-dev   created
 =   └─ aws:s3:Bucket     demo                 imported

Resources:
    + 1 created
    = 1 imported
    2 changes

Duration: 10s

Please copy the following code into your Pulumi application. Not doing so
will cause Pulumi to report that an update will happen on the next update command.

Please note, that the imported resources are marked as protected. To destroy them
you will need to remove the `protect` option and run `pulumi update` *before*
the destroy will take effect.
```

The user can then see the generated code they need to use as part of their application. I imported this resource into a
TypeScript application:

{{< chooser language "typescript,python,csharp,go" >}}

{{< choosable language typescript >}}
```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const demo = new aws.s3.Bucket("infra-logs", {
    acl: "private",
    bucket: "cloud-infra-logs",
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
    bucket="cloud-infra-logs",
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
			Bucket:       pulumi.String("cloud-infra-logs"),
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
            Bucket = "cloud-infra-logs",
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
scenario for us. We can assemble all of the resources into a JSON document as follows:

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

Pulumi will preview that it will import the resources as expected:

```bash
Previewing import (dev3)

View Live: https://app.pulumi.com/demo/import-example/dev/previews/53ff7162-2181-42e2-9712-72bbc0889e41

     Type                 Name                 Plan
 +   pulumi:pulumi:Stack  import-example-dev   create
 =   ├─ aws:ec2:Subnet    public-1             import
 =   ├─ aws:ec2:Vpc       application-vpc      import
 =   └─ aws:ec2:Subnet    private-1            import

Resources:
    + 1 to create
    = 3 to import
    4 changes

Do you want to perform this import?  [Use arrows to move, enter to select, type to filter]
  yes
> no
  details
```

On instructing Pulumi to proceed, the resources will be imported and the resource generated code is as follows:

```bash
Importing (dev3)

View Live: https://app.pulumi.com/demo/import-example/dev/updates/1

     Type                 Name                 Status
 +   pulumi:pulumi:Stack  import-example-dev   created
 =   ├─ aws:ec2:Subnet    public-1             imported
 =   ├─ aws:ec2:Vpc       application-vpc      imported
 =   └─ aws:ec2:Subnet    private-1            imported

Resources:
    + 1 created
    = 3 imported
    4 changes

Duration: 11s

Please copy the following code into your Pulumi application. Not doing so
will cause Pulumi to report that an update will happen on the next update command.

Please note, that the imported resources are marked as protected. To destroy them
you will need to remove the `protect` option and run `pulumi update` *before*
the destroy will take effect.
```

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


```

## Documentation

Full CLI Documentation is [available](https://www.pulumi.com/docs/reference/cli/pulumi_import/) so that all of the different
import command flags can be examined. The flags include writing directly to a file and also specifing the ability to ensure
a resource is not protected on import. Examples of importing resources can be found on their specifc resource documentation
pages, such an example for importing a VPC can be found in the [VPC import documentation](https://www.pulumi.com/docs/reference/pkg/aws/ec2/vpc/#import).
