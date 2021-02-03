---
title: "Importing Infrastructure"
meta_desc: Learn how to import existing cloud infrastructure into Pulumi no matter how it was provisioned.
menu:
  userguides:
    parent: adopting
    weight: 1
---

Most infrastructure projects require working with existing cloud resources, either by building on top of existing
resources or adopting existing resources under management with a new and more robust infrastructure provisioning solution.

No matter how you've provisioned these resources &mdash; manually in your cloud provider's console or CLI, using an
infrastructure as code tool like Terraform or AWS CloudFormation &mdash; Pulumi enables you to adopt and manage your resources.

<!--more-->

When working with existing resources, there are two primary scenarios:

* You need to reference existing resources to use as inputs to new resources in Pulumi
* You need to adopt existing resources under management so they can be managed by Pulumi

For the first situation, consult [the user guide index]({{< relref "/docs/guides/adopting#coexistence" >}}). For the
second, let's now see how to adopt existing resources.

## Adopting Existing Resources

There are two ways to adopt existing resources so that Pulumi is able to manage subsequent updates to them. The first way is to use the
[`import`]({{< relref "/docs/reference/cli/pulumi_import" >}}) cli command. This command specifies that a resource defined in
your Pulumi program should adopt an existing resource from a cloud provider rather than creating a new one after running `pulumi up`.
Another way is to use the [`import`]({{< relref "/docs/intro/concepts/resources#import" >}}) resource option.
This resource option is defined in your Pulumi program, and like the `import` command, the `import` resource option adopts an existing resource in the cloud provider rather
creating a new one. Using this option lets you specify
the `import` behavior inside the Pulumi code for your infrastructure deployment, instead of outside of it in a manual workflow.

{{% notes type="warning" %}}
Your Pulumi stack must be configured correctly---e.g., using the same AWS region as the resource your importing---otherwise the resource will not be found.
{{% /notes %}}

### Pulumi Import Command

This example imports an existing AWS S3 bucket named `company-infra-logs` and defines the resource name for your
Pulumi program as `infra-logs`:

```bash
pulumi import aws:s3/bucket:Bucket infra-logs company-infra-logs
```

```
     Type                 Name             Plan
 +   pulumi:pulumi:Stack  import-post-dev  create
 =   └─ aws:s3:Bucket     infra-logs       import

Resources:
    + 1 to create
    = 1 to import
    2 changes
```

Pulumi will perform the import of the S3 bucket and generate the code required for you to add it to your
application.

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

After successfully importing a resource and adding the generated code to your program, you can run `pulumi up` and all subsequent operations
will behave as though Pulumi provisioned the resource from the outset. The resource is added to the Pulumi
[state]({{ relref "/docs/intro/concepts/state#state" >}}), and marked as a [protected]({{< relref "/docs/intro/concepts/resources#protect" >}})
resource (by default) to ensure that imported infrastructure is not accidentally deleted if the user forgets to include the code for the resource in their program before doing a deployment.

### Pulumi Import Resource Operation

This example imports an existing AWS EC2 security group with ID `sg-04aeda9a214730248`:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let aws = require("@pulumi/aws");

let group = new aws.ec2.SecurityGroup("my-sg", {
    name: "my-sg-62a569b",
    ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] }],
}, { import: "sg-04aeda9a214730248" });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

let group = new aws.ec2.SecurityGroup("my-sg", {
    name: "my-sg-62a569b",
    ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] }],
}, { import: "sg-04aeda9a214730248" });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
# IMPORTANT: Python appends an underscore (`import_`) to avoid conflicting with the keyword.

import pulumi_aws as aws
from pulumi import ResourceOptions

group = aws.ec2.SecurityGroup('my-sg',
    name='my-sg-62a569b',
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] }
    ],
    opts=ResourceOptions(import_='sg-04aeda9a214730248'))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
group, err := ec2.NewSecurityGroup(ctx, "web-sg",
    &ec2.SecurityGroupArgs{
        Name:        pulumi.String("web-sg-62a569b"),
        Description: pulumi.String("Enable HTTP access"),
        Ingress: ec2.SecurityGroupIngressArray{
            ec2.SecurityGroupIngressArgs{
                Protocol:   pulumi.String("tcp"),
                FromPort:   pulumi.Int(80),
                ToPort:     pulumi.Int(80),
                CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
            },
        },
    },
    pulumi.Import(pulumi.ID("sg-04aeda9a214730248")),
)
if err != nil {
    return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var group = new SecurityGroup("my-sg",
    new SecurityGroupArgs {
        Name = "my-sg-62a569b",
        Description = "Enable HTTP access",
        Ingress = {
            new SecurityGroupIngressArgs {
                Protocol = "tcp",
                FromPort = 80,
                ToPort = 80,
                CidrBlocks = { "0.0.0.0/0" }
            }
        }
    },
    new CustomResourceOptions {
        ImportId = "sg-04aeda9a214730248"
    }
);
```

{{% /choosable %}}

{{< /chooser >}}

> **Note:** Import IDs are resource specific. The ID to use is the same as the ID that gets assigned when Pulumi has provisioned a resource of that type from scratch.

When Pulumi first sees a resource with an `import` option set (in this case `my-sg`), it will adopt the existing resource by querying the target cloud provider for a resource of that type with the given ID, instead of creating a new resource as usual.

To perform the import, run `pulumi up` as usual, and you will see `=` instead of the usual `+`, indicating an import operation:

```
$ pulumi up
Previewing update (dev):

     Type                       Name              Plan
     pulumi:pulumi:Stack        import-dev
 =   └─ aws:ec2:SecurityGroup   my-sg             import

Resources:
    = 1 to import
    1 unchanged
```

If the resource is not found, an error will occur:

```
error: Preview failed: importing sg-04aeda9a214730248: security group not found
```

After successfully importing a resource, you can delete the `import` statement, rerun `pulumi up`, and all subsequent operations will behave as though Pulumi provisioned the resource from the outset. Be careful, as this applies to `destroy` operations also.

#### Mismatched State

An important part of importing resources using the `import` resource option is that the resulting Pulumi program, after the import is complete, will faithfully generate the same desired state as your existing infrastructure's actual state. After the import, you may edit your program to generate and apply new desired states to update your infrastructure.

Because of this, all properties need to be fully specified. If you forget to specify a property, or that property's value is incorrect, you'll first receive a warning during preview, and then an error during the actual import update.

For instance, keeping with the example above, let's say we specified the wrong `ingress` rule by choosing port 22 instead of port 80. We'll see a warning:

```
$ pulumi preview
Previewing update (dev):
     Type                      Name        Plan       Info
     pulumi:pulumi:Stack       import-dev
 =   └─ aws:ec2:SecurityGroup  my-sg       import     [diff: ~ingress]; 1 warning

Diagnostics:
  aws:ec2:SecurityGroup (my-sg):
    warning: imported resource sg-04aeda9a214730248's property 'ingress' does not match the existing value;
             importing this resource will fail
```

If we'd like to see details on what specifically did not match, select the `details` option:

```
+ pulumi:pulumi:Stack: (create)
    [urn=urn:pulumi:dev::import::pulumi:pulumi:Stack::import-dev]
    = aws:ec2/securityGroup:SecurityGroup: (import)
        [id=sg-0d188488272df7df8]
        [urn=urn:pulumi:dev::import::aws:ec2/securityGroup:SecurityGroup::my-sg]
        [provider=urn:pulumi:dev::import::pulumi:providers:aws::default_1_22_0::04da6b54-80e4-46f7-96ec-b56ff0331ba9]
      ~ ingress: [
          ~ [0]: {
                  ~ cidrBlocks : [
                      ~ [0]: "0.0.0.0/0" => "0.0.0.0/0"
                    ]
                  - description: ""
                  ~ fromPort   : 80 => 22
                  ~ protocol   : "tcp" => "tcp"
                  ~ self       : false => false
                  ~ toPort     : 80 => 22
                }
        ]
```

Attempting to proceed will fail completely with an error:

```
Diagnostics:
  pulumi:pulumi:Stack (import-dev):
    error: update failed

  aws:ec2:SecurityGroup (my-sg):
    error: imported resource sg-04aeda9a214730248's property 'ingress' does not match the existing value
```

> **Note:** Because of [auto-naming]({{< relref "/docs/intro/concepts/resources#autonaming" >}}), it's common to accidentally get in a situation where names don't match. For example, if we left off the security group's name, `"my-sg-62a569b"`, in the earlier example, Pulumi would still auto-name the resource, leading to an error `imported resource sg-04aeda9a214730248's property 'name' does not match the existing value`. To fix this problem, make sure to specify names for all resources explicitly.

### Bulk Import Operations

If you need to import multiple resources, the CLI `import` command can be used with a JSON file that contains references to existing cloud resources. Using a JSON file with the `import` command can be helpful as part of scripting large bulk imports of cloud resources.

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

We can then see Pulumi will generate all of the resource code for us as follows:

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
