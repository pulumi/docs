---
title: "Pulumi AWS Provider 7.0: Multi-Region Support, IAM Role Chaining, and S3 Resource Simplification"
allow_long_title: true
date: 2025-08-05T09:00:00-04:00
draft: false
meta_desc: "Pulumi AWS Provider 7.0 adds multi-region support, IAM role chaining, and improved S3 resource management for seamless AWS infrastructure as code."
meta_image: meta.png
authors:
    - cory-hall
tags:
    - aws
    - providers

---


[Pulumi AWS provider 7.0](https://www.pulumi.com/registry/packages/aws/) is here with powerful new capabilities that simplify and scale **infrastructure as code on AWS**. As the most widely used provider in the Pulumi ecosystem, it offers access to the full surface area of the upstream Terraform AWS Provider in Pulumi projects in all supported languages, like TypeScript, Python, Go, C#, Java, and YAML. 

The [7.0 release](https://github.com/pulumi/pulumi-aws/releases/tag/v7.0.0) brings fixes and improvements to the provider, including several breaking changes as part of the major version release.

<!--more-->

## What’s New in Pulumi AWS Provider 7.0

### Multi-Region AWS Deployments with a Single Provider

Previously the Pulumi AWS provider each provider configuration could target a single AWS region. This meant that users would need to create a separate provider configuration for each region they wanted to deploy resources to. As the number of providers configured in an application grew, it could sometimes lead to increased memory usage.

With the 7.0 release, the AWS provider now supports multiple regions with a single provider. Each resource now has a `region` input property that allows the user to specify the region at the resource level, while still utilizing the same provider.

Some key highlights of this feature include:

- **Single provider configuration**: This reduces the need to load multiple instances of the AWS provider, lowering memory usage.
- **Region input property**: The `region` input property is added to all resources (except global resources)
- **Resource import enhancements**: A new `@<regionID>` suffix allows importing resources from different regions

This example shows how to use the new region input property to configure cross-region VPC peering.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const provider = new aws.Provider("provider", {region: "us-east-1"});
const mainVpc = new aws.ec2.Vpc("mainVpc", {cidrBlock: "10.0.0.0/16"}, {
    provider: provider,
});
const peerVpc = new aws.ec2.Vpc("peerVpc", {cidrBlock: "10.1.0.0/16"}, {
    provider: provider,
});
const peerConnection = new aws.ec2.VpcPeeringConnection("peerConnection", {
    vpcId: mainVpc.id,
    peerVpcId: peerVpc.id,
    peerRegion: "us-west-2",
    autoAccept: false,
}, {
    provider: provider,
});
const peerAcceptor = new aws.ec2.VpcPeeringConnectionAccepter("peerAcceptor", {
    region: "us-west-2",
    vpcPeeringConnectionId: peerConnection.id,
    autoAccept: true,
}, {
    provider: provider,
});

```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

provider = aws.Provider("provider", region="us-east-1")
main_vpc = aws.ec2.Vpc("mainVpc", cidr_block="10.0.0.0/16",
opts = pulumi.ResourceOptions(provider=provider))
peer_vpc = aws.ec2.Vpc("peerVpc", cidr_block="10.1.0.0/16",
opts = pulumi.ResourceOptions(provider=provider))
peer_connection = aws.ec2.VpcPeeringConnection("peerConnection",
    vpc_id=main_vpc.id,
    peer_vpc_id=peer_vpc.id,
    peer_region="us-west-2",
    auto_accept=False,
    opts = pulumi.ResourceOptions(provider=provider))
peer_acceptor = aws.ec2.VpcPeeringConnectionAccepter("peerAcceptor",
    region="us-west-2",
    vpc_peering_connection_id=peer_connection.id,
    auto_accept=True,
    opts = pulumi.ResourceOptions(provider=provider))

```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws"
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		provider, err := aws.NewProvider(ctx, "provider", &aws.ProviderArgs{
			Region: pulumi.String("us-east-1"),
		})
		if err != nil {
			return err
		}
		mainVpc, err := ec2.NewVpc(ctx, "mainVpc", &ec2.VpcArgs{
			CidrBlock: pulumi.String("10.0.0.0/16"),
		}, pulumi.Provider(provider))
		if err != nil {
			return err
		}
		peerVpc, err := ec2.NewVpc(ctx, "peerVpc", &ec2.VpcArgs{
			CidrBlock: pulumi.String("10.1.0.0/16"),
		}, pulumi.Provider(provider))
		if err != nil {
			return err
		}
		peerConnection, err := ec2.NewVpcPeeringConnection(ctx, "peerConnection", &ec2.VpcPeeringConnectionArgs{
			VpcId:      mainVpc.ID(),
			PeerVpcId:  peerVpc.ID(),
			PeerRegion: pulumi.String("us-west-2"),
			AutoAccept: pulumi.Bool(false),
		}, pulumi.Provider(provider))
		if err != nil {
			return err
		}
		_, err = ec2.NewVpcPeeringConnectionAccepter(ctx, "peerAcceptor", &ec2.VpcPeeringConnectionAccepterArgs{
			Region:                 pulumi.String("us-west-2"),
			VpcPeeringConnectionId: peerConnection.ID(),
			AutoAccept:             pulumi.Bool(true),
		}, pulumi.Provider(provider))
		if err != nil {
			return err
		}
		return nil
	})
}

```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var provider = new Aws.Provider("provider", new()
    {
        Region = "us-east-1",
    });

    var mainVpc = new Aws.Ec2.Vpc("mainVpc", new()
    {
        CidrBlock = "10.0.0.0/16",
    }, new CustomResourceOptions
    {
        Provider = provider,
    });

    var peerVpc = new Aws.Ec2.Vpc("peerVpc", new()
    {
        CidrBlock = "10.1.0.0/16",
    }, new CustomResourceOptions
    {
        Provider = provider,
    });

    var peerConnection = new Aws.Ec2.VpcPeeringConnection("peerConnection", new()
    {
        VpcId = mainVpc.Id,
        PeerVpcId = peerVpc.Id,
        PeerRegion = "us-west-2",
        AutoAccept = false,
    }, new CustomResourceOptions
    {
        Provider = provider,
    });

    var peerAcceptor = new Aws.Ec2.VpcPeeringConnectionAccepter("peerAcceptor", new()
    {
        Region = "us-west-2",
        VpcPeeringConnectionId = peerConnection.Id,
        AutoAccept = true,
    }, new CustomResourceOptions
    {
        Provider = provider,
    });

});


```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.Provider;
import com.pulumi.aws.ProviderArgs;
import com.pulumi.aws.ec2.Vpc;
import com.pulumi.aws.ec2.VpcArgs;
import com.pulumi.aws.ec2.VpcPeeringConnection;
import com.pulumi.aws.ec2.VpcPeeringConnectionArgs;
import com.pulumi.aws.ec2.VpcPeeringConnectionAccepter;
import com.pulumi.aws.ec2.VpcPeeringConnectionAccepterArgs;
import com.pulumi.resources.CustomResourceOptions;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var provider = new Provider("provider", ProviderArgs.builder()
            .region("us-east-1")
            .build());

        var mainVpc = new Vpc("mainVpc", VpcArgs.builder()
            .cidrBlock("10.0.0.0/16")
            .build(), CustomResourceOptions.builder()
                .provider(provider)
                .build());

        var peerVpc = new Vpc("peerVpc", VpcArgs.builder()
            .cidrBlock("10.1.0.0/16")
            .build(), CustomResourceOptions.builder()
                .provider(provider)
                .build());

        var peerConnection = new VpcPeeringConnection("peerConnection", VpcPeeringConnectionArgs.builder()
            .vpcId(mainVpc.id())
            .peerVpcId(peerVpc.id())
            .peerRegion("us-west-2")
            .autoAccept(false)
            .build(), CustomResourceOptions.builder()
                .provider(provider)
                .build());

        var peerAcceptor = new VpcPeeringConnectionAccepter("peerAcceptor", VpcPeeringConnectionAccepterArgs.builder()
            .region("us-west-2")
            .vpcPeeringConnectionId(peerConnection.id())
            .autoAccept(true)
            .build(), CustomResourceOptions.builder()
                .provider(provider)
                .build());

    }
}

```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: cross-region-peering
runtime: yaml

resources:
  provider:
    type: pulumi:providers:aws
    properties:
      region: us-east-1
  mainVpc:
    type: aws:ec2:Vpc
    properties:
      cidrBlock: 10.0.0.0/16
    options:
      provider: ${provider}
  peerVpc:
    type: aws:ec2:Vpc
    properties:
      cidrBlock: 10.1.0.0/16
    options:
      provider: ${provider}
  peerConnection:
    type: aws:ec2:VpcPeeringConnection
    properties:
      vpcId: ${mainVpc.id}
      peerVpcId: ${peerVpc.id}
      peerRegion: us-west-2
      autoAccept: false
    options:
      provider: ${provider}
  peerAcceptor:
    type: aws:ec2:VpcPeeringConnectionAccepter
    properties:
      region: us-west-2
      vpcPeeringConnectionId: ${peerConnection.id}
      autoAccept: true
    options:
      provider: ${provider}
```

{{% /choosable %}}

{{< /chooser >}}

See the [Enhanced Region Support](https://www.pulumi.com/registry/packages/aws/how-to-guides/aws-enhanced-region-support/) guide for more details.

### IAM Role Chaining for Secure AWS IaC Workflows

One of the most [requested features](https://github.com/pulumi/pulumi-aws/issues/4459), **IAM role chaining**, is now supported. This allows the Pulumi AWS Provider to assume multiple IAM roles in sequence to obtain credentials, streamlining **secure AWS access across accounts and teams**.

To assume a role with role chaining, you can now do the following:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const provider = new aws.Provider("provider", {assumeRoles: [
    {
        roleArn: "arn:aws:iam::123456789012:role/INITIAL_ROLE_NAME",
    },
    {
        roleArn: "arn:aws:iam::123456789012:role/FINAL_ROLE_NAME",
    },
]});

```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

provider = aws.Provider("provider", assume_roles=[
    {
        "role_arn": "arn:aws:iam::123456789012:role/INITIAL_ROLE_NAME",
    },
    {
        "role_arn": "arn:aws:iam::123456789012:role/FINAL_ROLE_NAME",
    },
])

```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := aws.NewProvider(ctx, "provider", &aws.ProviderArgs{
			AssumeRoles: aws.ProviderAssumeRoleArray{
				&aws.ProviderAssumeRoleArgs{
					RoleArn: pulumi.String("arn:aws:iam::123456789012:role/INITIAL_ROLE_NAME"),
				},
				&aws.ProviderAssumeRoleArgs{
					RoleArn: pulumi.String("arn:aws:iam::123456789012:role/FINAL_ROLE_NAME"),
				},
			},
		})
		if err != nil {
			return err
		}
		return nil
	})
}

```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var provider = new Aws.Provider("provider", new()
    {
        AssumeRoles = new[]
        {
            new Aws.Inputs.ProviderAssumeRoleArgs
            {
                RoleArn = "arn:aws:iam::123456789012:role/INITIAL_ROLE_NAME",
            },
            new Aws.Inputs.ProviderAssumeRoleArgs
            {
                RoleArn = "arn:aws:iam::123456789012:role/FINAL_ROLE_NAME",
            },
        },
    });

});


```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.Provider;
import com.pulumi.aws.ProviderArgs;
import com.pulumi.aws.inputs.ProviderAssumeRoleArgs;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var provider = new Provider("provider", ProviderArgs.builder()
            .assumeRoles(
                ProviderAssumeRoleArgs.builder()
                    .roleArn("arn:aws:iam::123456789012:role/INITIAL_ROLE")
                    .build(),
                ProviderAssumeRoleArgs.builder()
                    .roleArn("arn:aws:iam::123456789012:role/FINAL_ROLE")
                    .build())
            .build());

    }
}

```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: example
runtime: yaml
resources:
  provider:
    type: pulumi:providers:aws
    properties:
      assumeRoles:
        - roleArn: arn:aws:iam::123456789012:role/INITIAL_ROLE_NAME
        - roleArn: arn:aws:iam::123456789012:role/FINAL_ROLE_NAME
```

{{% /choosable %}}

{{< /chooser >}}

With this configuration the provider will use the `INITIAL_ROLE` to assume the `FINAL_ROLE` which will then be used as the credentials for the provider.

### Simplified S3 Bucket Resource Model

In `v6` of the Pulumi AWS Provider the S3 `Bucket` and `BucketV2` resources represented different resource implementations. `BucketV2` represented the latest version of the upstream Terraform resource, while `Bucket` was a separate resource maintained by Pulumi to keep backwards compatibility with the `v4` release of the upstream Terraform Provider.

In `v7` we are taking the first step in unifying these two resources by moving the S3 `Bucket` resource to the latest upstream implementation. As a result, in `v7` both `Bucket` and `BucketV2` will represent the latest version of the upstream Terraform S3 Bucket resource. As part of this work `BucketV2` has been deprecated and will be removed in `v8` of the Pulumi AWS Provider.

We have also introduced new S3 Bucket configuration resources that are alternatives to their `V2` counterparts. The `V2` versions will be removed in `v8` of the Pulumi AWS Provider.

- `BucketAccelerateConfigurationV2` => `BucketAccelerateConfiguration`
- `BucketRequestPaymentConfigurationV2` => `BucketRequestPaymentConfiguration`
- `BucketAclV2` => `BucketAcl`
- `BucketCorsConfigurationV2` => `BucketCorsConfiguration`
- `BucketLifecycleConfigurationV2` => `BucketLifecycleConfiguration`
- `BucketLoggingV2` => `BucketLogging`
- `BucketObjectLockConfigurationV2` => `BucketObjectLockConfiguration`
- `BucketServerSideEncryptionConfigurationV2` => `BucketServerSideEncryptionConfiguration`
- `BucketVersioningV2` => `BucketVersioning`
- `BucketWebsiteConfigurationV2` => `BucketWebsiteConfiguration`

See the [Migration Guide](https://www.pulumi.com/registry/packages/aws/how-to-guides/7-0-migration) for more details on this change.

### Upstream Improvements and Breaking Changes

Pulumi AWS 7.0 includes all improvements and bug fixes from the upstream (terraform-provider-aws) versions from 6.0.0 to 6.3.0. It also contains a number of upstream breaking changes. Please refer to the [changelog](https://github.com/hashicorp/terraform-provider-aws/blob/main/CHANGELOG.md) to navigate the entire list.

### Migration Guide

You can see a full list of changes and learn more about migrating your existing programs in our [Migration Guide](https://www.pulumi.com/registry/packages/aws/how-to-guides/7-0-migration).

### Getting Started with Pulumi AWS 7.0

Pulumi makes it easy to define, deploy, and manage modern AWS infrastructure with code:

- Use your favorite languages: TypeScript, Python, Go, C#, Java, YAML
- Explore the [Pulumi AWS Provider repro](https://github.com/pulumi/pulumi-aws)
- Check out the [API reference docs](https://www.pulumi.com/registry/packages/aws/)
