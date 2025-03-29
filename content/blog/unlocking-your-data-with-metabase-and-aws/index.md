---
title: "Unlocking Your Data With Metabase and AWS Fargate"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-08-09T08:57:51-07:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: In this blog post, you will learn how Pulumi solved their data visualizing
  challenges and how you can solve your challenges with Pulumi's Metabase Package.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
  - zack-chase

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
  - aws
  - metabase

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
search:
  keywords:
    - Metabase
    - AWS
    - AWS Fargate
    - Data Warehouse
    - Business Intelligence
    - Cloud Native
---

I love data. I mean, I really love data. Data gives you the ability to understand the world around you and, to a certain degree, project what the future could look like. At Pulumi we use data every day to help make smarter product and business decisions.

Though one hurdle we encountered was not only the sheer volume of data we have but also the large disparity of systems storing that data. Like many companies before us, we chose to build a data warehouse, specifically AWS Redshift, to store all of our data.

After grinding through the work to consolidate our data into a single source of truth, we felt like we had conquered the world. That feeling was fleeting as we quickly realized we needed a scalable way to save, abstract, and collaborate with our data across the entire organization.

## Using Metabase to unlock our data

As an early stage start-up at the time, we needed a low-cost solution (free) which limited our available options. One advantage we did have at the time was that as a cloud native start-up we were comfortable with the upfront investment and operational overhead of self-hosting the solution. With all of our parameters set, we eventually settled on using <a href="https://www.metabase.com/" target="_blank" rel="noopener noreferrer">Metabase <i class="text-xs fas fa-external-link-alt"></i></a>.

### What is Metabase?

Metabase is a Business Intelligence Tool that enables you to visualize and collaborate using data from a variety of databases. You do not need to understand the underlying database’s query language, SQL for example, because Metabase provides a UI to interact with your data. You can however drop into a query editor at any moment to perform more advanced queries.

Metabase provides you with two options to run <a href="https://www.metabase.com/blog/how-to-run-metabase-in-production" target="_blank" rel="noopener noreferrer">Metabase in production <i class="text-xs fas fa-external-link-alt"></i></a>, Open Source (self-managed) and Enterprise (managed). The main difference between the two is that with Open Source you have to manage the infrastructure yourself, whereas with Enterprise, Metabase will manage the infrastructure for you for a fee.

## Deploying Metabase to production

Once we settled on our business intelligence tool it was time to wire it up and start living that sweet data-driven lifestyle. To run the service yourself, Metabase provides you with two options: a Docker Image or a .JAR. We were already running our SaaS service on ECS, so naturally, we opted to go with the Docker approach. In addition to running the Docker Image, we also needed to provision a database so that Metabase could store the relevant data it needs to run the service.

To accomplish the task of provisioning all the required resources, the team wrote a [Pulumi Component](/docs/concepts/resources/components/) to encapsulate all the complexity and provide a simple interface for provisioning and updating the service. Unfortunately, this was before we had developed [Pulumi Packages](/docs/iac/packages-and-automation/pulumi-packages/debugging-provider-packages/) and the Component was only available within the program itself.

## The Metabase Package

That brings us to today, and we are happy to deliver an open source Pulumi Package for running Metabase on [AWS ECS](/docs/iac/clouds/aws/guides/ecs/). With Pulumi’s Metabase Package, you can quickly get started with Metabase without having to worry about the underlying infrastructure.

In the below sections we will look at example configurations of the Metabase resource, all the way from a bare bones configuration to a more complex configuration with a custom VPC, subnets, and domain.

### Default

By default, the Package accepts zero arguments and will deploy your resources into your default VPC, on public subnets, and without a custom domain name.

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as metabase from "@pulumi/metabase";

const metabaseService = new metabase.Metabase("metabaseService", {});

export const url = metabaseService.dnsName;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_metabase as metabase

metabase_service = metabase.Metabase("metabaseService")

pulumi.export("url", metabase_service.dns_name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-metabase/sdk/go/metabase"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		metabaseService, err := metabase.NewMetabase(ctx, "metabaseService", nil)
		if err != nil {
			return err
		}
		ctx.Export("url", metabaseService.DnsName)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Metabase = Pulumi.Metabase;

return await Deployment.RunAsync(() =>
{
    var metabaseService = new Metabase.Metabase("metabaseService");

    return new Dictionary<string, object?>
    {
        ["url"] = metabaseService.DnsName,
    };
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: metabase-yaml
runtime: yaml
resources:
    metabaseService:
        type: "metabase:index:Metabase"
outputs:
    url: ${metabaseService.dnsName}
```

{{% /choosable %}}

### Custom VPC

If you would like to run the service in a specific VPC, then you can provide a VPC ID as an argument. The example below will provision your resources in your defined VPC, on public subnets, and without a custom domain.

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as metabase from "@pulumi/metabase";

const metabaseService = new metabase.Metabase("metabaseService", {
    vpcId: "vpc-123",
});

export const url = metabaseService.dnsName;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_metabase as metabase

metabase_service = metabase.Metabase("metabaseService",
    vpc_id="vpc-123")

pulumi.export("url", metabase_service.dns_name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-metabase/sdk/go/metabase"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		metabaseService, err := metabase.NewMetabase(ctx, "metabaseService", &metabase.MetabaseArgs{
			VpcId: pulumi.String("vpc-123"),
		})
		if err != nil {
			return err
		}
		ctx.Export("url", metabaseService.DnsName)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Metabase = Pulumi.Metabase;

return await Deployment.RunAsync(() =>
{
    var metabaseService = new Metabase.Metabase("metabaseService", new()
    {
        VpcId = "vpc-123",
    });

    return new Dictionary<string, object?>
    {
        ["url"] = metabaseService.DnsName,
    };
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: metabase-yaml
runtime: yaml
resources:
    metabaseService:
        type: "metabase:index:Metabase"
        properties:
            vpcId: "vpc-123"
outputs:
    url: ${metabaseService.dnsName}
```

{{% /choosable %}}

### Custom Networking

If you would like to run the Load Balancer, Database, or ECS Service on specific subnets you can provide the IDs of those subnets. The subnets you provide need to be a part of the VPC you are deploying into. The example below will provision your resources in your defined VPC (or default if you do not provide a VPC ID), on your specified subnets, and without a custom domain.

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as metabase from "@pulumi/metabase";

const metabaseService = new metabase.Metabase("metabaseService", {
    vpcId: "vpc-123",
    networking: {
        ecsSubnetIds: [
            "subnet-123",
            "subnet-456",
        ],
        dbSubnetIds: [
            "subnet-789",
            "subnet-abc",
        ],
        lbSubnetIds: [
            "subnet-def",
            "subnet-ghi",
        ],
    },
});

export const url = metabaseService.dnsName;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_metabase as metabase

metabase_service = metabase.Metabase("metabaseService",
    vpc_id="vpc-123",
    networking=metabase.NetworkingArgs(
        ecs_subnet_ids=[
            "subnet-123",
            "subnet-456",
        ],
        db_subnet_ids=[
            "subnet-789",
            "subnet-abc",
        ],
        lb_subnet_ids=[
            "subnet-def",
            "subnet-ghi",
        ],
    ))

pulumi.export("url", metabase_service.dns_name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-metabase/sdk/go/metabase"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		metabaseService, err := metabase.NewMetabase(ctx, "metabaseService", &metabase.MetabaseArgs{
			VpcId: pulumi.String("vpc-123"),
			Networking: &metabase.NetworkingArgs{
				EcsSubnetIds: pulumi.StringArray{
					pulumi.String("subnet-123"),
					pulumi.String("subnet-456"),
				},
				DbSubnetIds: pulumi.StringArray{
					pulumi.String("subnet-789"),
					pulumi.String("subnet-abc"),
				},
				LbSubnetIds: pulumi.StringArray{
					pulumi.String("subnet-def"),
					pulumi.String("subnet-ghi"),
				},
			},
		})
		if err != nil {
			return err
		}
		ctx.Export("url", metabaseService.DnsName)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Metabase = Pulumi.Metabase;

return await Deployment.RunAsync(() =>
{
    var metabaseService = new Metabase.Metabase("metabaseService", new()
    {
        VpcId = "vpc-123",
        Networking = new Metabase.Inputs.NetworkingArgs
        {
            EcsSubnetIds = new[]
            {
                "subnet-123",
                "subnet-456",
            },
            DbSubnetIds = new[]
            {
                "subnet-789",
                "subnet-abc",
            },
            LbSubnetIds = new[]
            {
                "subnet-def",
                "subnet-ghi",
            },
        },
    });

    return new Dictionary<string, object?>
    {
        ["url"] = metabaseService.DnsName,
    };
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: metabase-yaml
runtime: yaml
resources:
    metabaseService:
        type: "metabase:index:Metabase"
        properties:
            vpcId: "vpc-123"
            networking:
                ecsSubnetIds: [ "subnet-123", "subnet-456" ]
                dbSubnetIds: [ "subnet-789", "subnet-abc" ]
                lbSubnetIds: [ "subnet-def", "subnet-ghi" ]
outputs:
    url: ${metabaseService.dnsName}
```

{{% /choosable %}}

### Custom Domain

If you would like to have your service run behind a custom domain, you can specify the hosted zone and domain name as arguments. The example below will provision your resources in your default VPC, on public subnets, with a custom domain name.

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as metabase from "@pulumi/metabase";

const metabaseService = new metabase.Metabase("metabaseService", {
    domain: {
        hostedZoneName: "example.com",
        domainName: "metabase.example.com",
    },
});

export const url = metabaseService.dnsName;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_metabase as metabase

metabase_service = metabase.Metabase("metabaseService",
    domain=metabase.CustomDomainArgs(
        hosted_zone_name="example.com",
        domain_name="metabase.example.com",
    ))

pulumi.export("url", metabase_service.dns_name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-metabase/sdk/go/metabase"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		metabaseService, err := metabase.NewMetabase(ctx, "metabaseService", &metabase.MetabaseArgs{
			Domain: &metabase.CustomDomainArgs{
				HostedZoneName: pulumi.String("example.com"),
				DomainName:     pulumi.String("metabase.example.com"),
			},
		})
		if err != nil {
			return err
		}
		ctx.Export("url", metabaseService.DnsName)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Metabase = Pulumi.Metabase;

return await Deployment.RunAsync(() =>
{
    var metabaseService = new Metabase.Metabase("metabaseService", new()
    {
        VpcId = "vpc-123",
        Domain = new Metabase.Inputs.CustomDomainArgs
        {
            HostedZoneName = "example.com",
            DomainName = "metabase.example.com",
        },
    });

    return new Dictionary<string, object?>
    {
        ["url"] = metabaseService.DnsName,
    };
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: metabase-yaml
runtime: yaml
resources:
    metabaseService:
        type: "metabase:index:Metabase"
        properties:
            vpcId: "vpc-123"
            domain:
                hostedZoneName: "example.com"
                domainName: "metabase.example.com"
outputs:
    url: ${metabaseService.dnsName}
```

{{% /choosable %}}

### All Together Now

You can provide all the arguments at once if you would like more control over your infrastructure. The below example will provision your resources in your defined VPC, with your defined subnets, and have a custom domain.

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as metabase from "@pulumi/metabase";

const metabaseService = new metabase.Metabase("metabaseService", {
    vpcId: "vpc-123",
    networking: {
        ecsSubnetIds: [
            "subnet-123",
            "subnet-456",
        ],
        dbSubnetIds: [
            "subnet-789",
            "subnet-abc",
        ],
        lbSubnetIds: [
            "subnet-def",
            "subnet-ghi",
        ],
    },
    domain: {
        hostedZoneName: "example.com",
        domainName: "metabase.example.com",
    },
});

export const url = metabaseService.dnsName;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_metabase as metabase

metabase_service = metabase.Metabase("metabaseService",
    vpc_id="vpc-123",
    networking=metabase.NetworkingArgs(
        ecs_subnet_ids=[
            "subnet-123",
            "subnet-456",
        ],
        db_subnet_ids=[
            "subnet-789",
            "subnet-abc",
        ],
        lb_subnet_ids=[
            "subnet-def",
            "subnet-ghi",
        ],
    ),
    domain=metabase.CustomDomainArgs(
        hosted_zone_name="example.com",
        domain_name="metabase.example.com",
    ))

pulumi.export("url", metabase_service.dns_name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-metabase/sdk/go/metabase"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		metabaseService, err := metabase.NewMetabase(ctx, "metabaseService", &metabase.MetabaseArgs{
			VpcId: pulumi.String("vpc-123"),
			Networking: &metabase.NetworkingArgs{
				EcsSubnetIds: pulumi.StringArray{
					pulumi.String("subnet-123"),
					pulumi.String("subnet-456"),
				},
				DbSubnetIds: pulumi.StringArray{
					pulumi.String("subnet-789"),
					pulumi.String("subnet-abc"),
				},
				LbSubnetIds: pulumi.StringArray{
					pulumi.String("subnet-def"),
					pulumi.String("subnet-ghi"),
				},
			},
			Domain: &metabase.CustomDomainArgs{
				HostedZoneName: pulumi.String("example.com"),
				DomainName:     pulumi.String("metabase.example.com"),
			},
		})
		if err != nil {
			return err
		}
		ctx.Export("url", metabaseService.DnsName)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Metabase = Pulumi.Metabase;

return await Deployment.RunAsync(() =>
{
    var metabaseService = new Metabase.Metabase("metabaseService", new()
    {
        VpcId = "vpc-123",
        Networking = new Metabase.Inputs.NetworkingArgs
        {
            EcsSubnetIds = new[]
            {
                "subnet-123",
                "subnet-456",
            },
            DbSubnetIds = new[]
            {
                "subnet-789",
                "subnet-abc",
            },
            LbSubnetIds = new[]
            {
                "subnet-def",
                "subnet-ghi",
            },
        },
        Domain = new Metabase.Inputs.CustomDomainArgs
        {
            HostedZoneName = "example.com",
            DomainName = "metabase.example.com",
        },
    });

    return new Dictionary<string, object?>
    {
        ["url"] = metabaseService.DnsName,
    };
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: metabase-yaml
runtime: yaml
resources:
    metabaseService:
        type: "metabase:index:Metabase"
        properties:
            vpcId: "vpc-123"
            networking:
                ecsSubnetIds: [ "subnet-123", "subnet-456" ]
                dbSubnetIds: [ "subnet-789", "subnet-abc" ]
                lbSubnetIds: [ "subnet-def", "subnet-ghi" ]
            domain:
                hostedZoneName: "example.com"
                domainName: "metabase.example.com"
outputs:
    url: ${metabaseService.dnsName}
```

{{% /choosable %}}

## Delivery in 30 minutes or less

To get started unlocking your data with Metabase, head on over to the [Metabase Package](/registry/packages/metabase/). Follow the quick walkthrough and have your Metabase service running in 30 minutes or less (in most cases). Once your service is up and running, we recommend popping over the Metabase Documentation to learn <a href="https://www.metabase.com/docs/latest/setting-up-metabase.html" target="_blank" rel="noopener noreferrer">How to Set Up Metabase <i class="text-xs fas fa-external-link-alt"></i></a>.

If you encounter an issue or have a feature request, please file an issue in the Package’s <a href="https://github.com/pulumi/pulumi-metabase" target="_blank" rel="noopener noreferrer">Github Repo <i class="text-xs fas fa-external-link-alt"></i></a>.
