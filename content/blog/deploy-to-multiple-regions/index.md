---
title: "Deploy Infrastructure to Multiple Cloud Regions at Once"
date: 2022-08-03T08:00:00-07:00
meta_desc: "Use infrastructure as code to deploy to multiple regions, accounts, or
  clusters at the same time, using Pulumi explicit provider configuration."
meta_image: deployinfra.png
authors: ["joe-duffy"]
tags: ["aws", "regions", "rds", "multi-cloud", "multi-region", "architecture"]
search:
  keywords:
    - clusters
    - regions
    - multiple
    - deploy
    - explicit
    - infrastructure
    - accounts
---

Pulumi makes it easy to flexibly deploy your cloud infrastructure using code. Usually deployments encompass a single slack and a single region in your cloud of choice. If you need to go multi-region, that usually means creating a stack per-region, which Pulumi's configuration system makes easy. A stack per region isn't required, though! Sometimes we want a single stack to span regions for performance, scalability, resilience, or just hard requirements. In these cases, Pulumi can seamlessly orchestrate deployments to, or even across, multiple regions,  accounts, or clusters. In this article, we'll see this in action by provisioning an AWS RDS primary database into one region and a read replica in an entirely different region -- all from a single Pulumi program, stack, and `pulumi up` incantation.

<!--more-->

## Recap of Stack Configuration

Before seeing how to span regions, let's review how you'd typically configure your region. Every Pulumi project can have any number of stacks. These stacks are often things like dev, test, prod -- and sometimes, things like prod-us-east, prod-us-west, prod-euro, and so on, to represent instances of our infrastructure running in different regions. Each stack is isolated from all others and it's easy to switch between them.

The standard way to vary regions between stacks is to use Pulumi's configuration system. If you've used Pulumi to deploy to AWS, for instance, you've probably uttered a CLI command like this:

```bash
$ pulumi config set aws:region us-east-1
```

This isn't just about regions: it applies to anything that varies between stacks. It might include accounts, secrets like tokens and passwords, sizes or counts of instances, among many other things.

This is normally very convenient and aligns with how we want to configure our projects and stacks. But there are some relatively common circumstances in which it breaks down:

* Managing a large number of multi-tenanted resources spanning multiple accounts or clusters.
* Cases where a few pieces of infrastructure must run somewhere different than most of it, as is often the case with DNS or SSL/TLS certificate management services.
* Situations where we want to provision resources in many places for performance, scalability, or resilience purposes.
* Highly programmatic scenarios where some configuration might be fetched dynamically from an external resource.

In all of these cases, thankfully Pulumi has an answer: [explicit provider configuration](/docs/concepts/resources/providers#explicit-provider-configuration).

## How Explicit Provider Configuration Works

Before diving into our example, let's take a quick look at how explicit provider configuration works. Unlike ordinary configuration, which is set at the CLI, provider configuration is set programmatically inside your Pulumi program. Every Pulumi package exports a `Provider` resource class which can be instantiated like any other resource, with the sole difference that these resources exist to pass around to configure _other_ resources, and don't represent infrastructure that is to be provisioned in a cloud of any kind.

For instance, if we wanted to programmatically create an AWS provider that targets a different region than `us-east-1`, as shown earlier, we can do so as follows:

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
const awsWest2 = new aws.Provider("aws-west-2", { region: "us-west-2" });
```

{{% /choosable %}}

{{% choosable language python %}}

```python
aws_west_2 = aws.Provider('aws-west-2', region='us-west-2')
```

{{% /choosable %}}

{{% choosable language go %}}

```go
awsWest2, err := aws.NewProvider(ctx, "aws-west-2", &aws.ProviderArgs{
    Region: pulumi.String("aws-west-2")
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var awsWest2 = new Aws.Provider("aws-west-2", new Aws.ProviderArgs
{
    Region = "us-west-2"
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
    awsWest2:
        type: pulumi:providers:aw
        properties:
            region: us-west-2
```

{{% /choosable %}}

This configuration is _not_ used automatically, however. You must pass it to any resources you'd like to use it:

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
const buck = new aws.s3.Bucket("my-bucket", {
    // ...
}, { provider: awsWest2 });
```

{{% /choosable %}}

{{% choosable language python %}}

```python
buck = aws.s3.Bucket('my-bucket',
    # ...
    opts=pulumi.ResourceOptions(provider=aws_west_2)
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
buck, err := s3.NewBucket("my-bucket",
    &s3.BucketArgs{
        // ...
    },
    pulumi.Provider(awsWest2)
)
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var buck = new Aws.S3.Bucket("my-bucket",
    new Aws.S3.BucketArgs
    {
        // ...
    },
    new ResourceArgs
    {
        Provider = awsWest2
    }
);
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
    # ...
    buck:
        type: aws:s3:Bucket
        properties:
            # ...
        options:
            provider: ${awsWest2}
```

{{% /choosable %}}

This overrides the default of using whatever was set at the CLI, and will instead use the programmatically configured settings. Note also that anything you can set at the CLI is available, not just the region. You can see the full settings available in the package's registry documentation for its `Provider` class (for instance, the [AWS Provider](/registry/packages/aws/api-docs/provider/).

## Multi-Region Deployment In Action!

The architecture for our multi-region setup is going to be relatively straightforward so we can focus on the essentials. We will provision a single RDS primary database in one region (us-east-1) and backup to a read replica in an entirely different region -- in fact, on an entirely different continent (eu-west-2)! This is relatively straightforward because many scenarios demand that we deploy to a dynamic number of regions, perhaps across dozens or hundreds of resources. By keeping it to just two resources across two regions, we can see the fundamentals in action which can scale easily to more sophisticated use cases.

This is [described in AWS's docs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.XRgn) and is depicted in this diagram:

![AWS RDS Read Replica Architecture](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/read-replica-cross-region.png)

Now let's dive into some infrastructure as code. There's a bit of preamble before getting to the meat of the example:

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as random from "@pulumi/random";

// Code from below will goes here.
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_random as random

# Code from below goes here.
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws"
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/rds"
	"github.com/pulumi/pulumi-random/sdk/v4/go/random"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        // Code from below goes here.
    })
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Aws = Pulumi.Aws;
using Random = Pulumi.Random;

return await Deployment.RunAsync(() =>
{
    // Code from below goes here.
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: aws-multireg-rds
runtime: yaml
description: A multi-region example creating an RDS primary and read-replica in different regions

# Code from below goes here.
```

{{% /choosable %}}

Next, we'll make the retention period configurable, by default it is 30 days. Note how we can still use standard configuration features _as well_ as explicit providers alongside one another:

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
// Enable backup retention to be configured, but default to 30 days.
const config = new pulumi.Config();
const retentionPeriod = config.getNumber("retentionPeriod") || 30;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Enable backup retention to be configured, but default to 30 days.
config = pulumi.Config()
retention_period = config.get_float('retentionPeriod') or 30
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Enable backup retention to be configured, but default to 30 days.
cfg := config.New(ctx, "")
retentionPeriod := 30
if param := cfg.GetFloat("retentionPeriod"); param != 0 {
    retentionPeriod = param
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// Enable backup retention to be configured, but default to 30 days.
var config = new Config();
var retentionPeriod = config.GetNumber("retentionPeriod") ?? 30;
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
# Enable backup retention to be configured, but default to 30 days.
configuration:
  retentionPeriod:
    type: Number
    default: 30
```

{{% /choosable %}}

Next, we'll create a random password for our database so we don't need to hard-code one:

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
// Create a random password for the database's admin user.
const dbPassword = new random.RandomPassword("dbPassword", { length: 12 });
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Create a random password for the database's admin user.
db_password = random.RandomPassword('dbPassword', length = 12)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Create a random password for the database's admin user.
dbPassword, err := random.NewRandomPassword(ctx, "dbPassword", &random.RandomPasswordArgs{
    Length: pulumi.Int(12),
})
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// Create a random password for the database's admin user.
var dbPassword = new Random.RandomPassword("dbPassword", new()
{
    Length = 12,
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
  # Create a random password for the database's admin user.
  dbPassword:
    type: random:RandomPassword
    properties:
      length: 12
```

{{% /choosable %}}

Now we're ready to create the providers. We'll create one per region that we will deploy into:

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
// Create two AWS providers, one for each region we'll deploy into.
const euProvider = new aws.Provider("euProvider", { region: "eu-west-2" });
const usProvider = new aws.Provider("usProvider", { region: "us-east-1" });
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Create two AWS providers, one for each region we'll deploy into.
eu_provider = aws.Provider('euProvider', region = 'eu-west-2')
us_provider = aws.Provider('usProvider', region = 'us-east-1')
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Create two AWS providers, one for each region we'll deploy into.
euProvider, err := aws.NewProvider(ctx, "euProvider", &aws.ProviderArgs{
    Region: pulumi.String("eu-west-2"),
})
if err != nil {
    return err
}
usProvider, err := aws.NewProvider(ctx, "usProvider", &aws.ProviderArgs{
    Region: pulumi.String("us-east-1"),
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// Create two AWS providers, one for each region we'll deploy into.
var euProvider = new Aws.Provider("euProvider", new()
{
    Region = "eu-west-2",
});

var usProvider = new Aws.Provider("usProvider", new()
{
    Region = "us-east-1",
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  # Create two AWS providers, one for each region we'll deploy into.
  euProvider:
    type: pulumi:providers:aws
    properties:
      region: eu-west-2
  usProvider:
    type: pulumi:providers:aws
    properties:
      region: us-east-1
```

{{% /choosable %}}

To keep things straightforward, we've hard-coded the regions into the program. There are more sophisticated possibilities, however. For example, we could have made the regions themselves configurable too, much like the retention period. Even more powerfully, we could use our programming language's expressiveness to create them dynamically. For instance, we could have looped over a list of them so that the number of regions isn't even known in advance. These advanced capabilities are helpful for many real-world scenarios.

Next up, we'll create the primary database instance in us-east-1:

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
// Create the primary RDS database instance.
const primaryDb = new aws.rds.Instance("primary", {
    allocatedStorage: 10,
    engine: "mysql",
    engineVersion: "5.7",
    instanceClass: "db.t3.micro",
    username: "admin",
    password: dbPassword.result,
    backupRetentionPeriod: retentionPeriod,
    skipFinalSnapshot: true,
}, {
    provider: usProvider,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Create the primary RDS database instance.
primary_db = aws.rds.Instance('primary',
    allocated_storage=10,
    engine='mysql',
    engine_version='5.7',
    instance_class='db.t3.micro',
    username='admin',
    password=db_password.result,
    backup_retention_period=retention_period,
    skip_final_snapshot=True,
    opts=pulumi.ResourceOptions(provider=us_provider)
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Create the primary RDS database instance.
primaryDb, err := rds.NewInstance(ctx, "primary", &rds.InstanceArgs{
    AllocatedStorage:      pulumi.Int(10),
    Engine:                pulumi.String("mysql"),
    EngineVersion:         pulumi.String("5.7"),
    InstanceClass:         pulumi.String("db.t3.micro"),
    Username:              pulumi.String("admin"),
    Password:              dbPassword.Result,
    BackupRetentionPeriod: pulumi.Float64(retentionPeriod),
    SkipFinalSnapshot:     pulumi.Bool(true),
}, pulumi.Provider(usProvider))
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// Create the primary RDS database instance.
var primaryDb = new Aws.Rds.Instance("primary", new()
{
    AllocatedStorage = 10,
    Engine = "mysql",
    EngineVersion = "5.7",
    InstanceClass = "db.t3.micro",
    Username = "admin",
    Password = dbPassword.Result,
    BackupRetentionPeriod = retentionPeriod,
    SkipFinalSnapshot = true,
}, new CustomResourceOptions
{
    Provider = usProvider,
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
  # Create the primary RDS database instance.
  primary:
    type: aws:rds:Instance
    properties:
      allocatedStorage: 10
      engine: mysql
      engineVersion: "5.7"
      instanceClass: db.t3.micro
      username: admin
      password: ${dbPassword.result}
      backupRetentionPeriod: ${retentionPeriod}
      skipFinalSnapshot: true
    options:
      provider: ${usProvider}
```

{{% /choosable %}}

The key here is that we explicitly passed the `provider` that was configured to use us-east-1, instructing Pulumi to use that configuration rather than the implicit default configuration set at the CLI as usual.

Now we will create the secondary database instance in eu-west-2:

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
// Now set up our secondary read replica database in an entirely different region.
const secondaryDb = new aws.rds.Instance("secondary", {
    instanceClass: "db.t3.micro",
    replicateSourceDb: primaryDb.arn,
    backupRetentionPeriod: retentionPeriod,
    skipFinalSnapshot: true,
}, {
    provider: euProvider,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Now set up our secondary read replica database in an entirely different region.
secondary_db = aws.rds.Instance("secondary",
    instance_class="db.t3.micro",
    replicate_source_db=primary_db.arn,
    backup_retention_period=retention_period,
    skip_final_snapshot=True,
    opts=pulumi.ResourceOptions(provider=eu_provider)
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Now set up our secondary read replica database in an entirely different region.
secondaryDb, err := rds.NewInstance(ctx, "secondary", &rds.InstanceArgs{
    InstanceClass:         pulumi.String("db.t3.micro"),
    ReplicateSourceDb:     primaryDb.Arn,
    BackupRetentionPeriod: pulumi.Float64(retentionPeriod),
    SkipFinalSnapshot:     pulumi.Bool(true),
}, pulumi.Provider(euProvider))
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// Now set up our secondary read replica database in an entirely different region.
var secondaryDb = new Aws.Rds.Instance("secondary", new()
{
    InstanceClass = "db.t3.micro",
    ReplicateSourceDb = primaryDb.Arn,
    BackupRetentionPeriod = retentionPeriod,
    SkipFinalSnapshot = true,
}, new CustomResourceOptions
{
    Provider = euProvider,
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
  # Now set up our secondary read replica database in an entirely different region.
  secondary:
    type: aws:rds:Instance
    properties:
      instanceClass: db.t3.micro
      replicateSourceDb: ${primary.arn}
      backupRetentionPeriod: ${retentionPeriod}
      skipFinalSnapshot: true
    options:
      provider: ${euProvider}
```

{{% /choosable %}}

As expected, we passed the `provider` configured to use eu-west-2. Notice also that, although these resources are deployed into entirely different regions, they can reference one another! Thanks to Pulumi's dependency system, it understands that referencing `primary.arn` means the secondary database depends on the primary, which Pulumi will use to ensure correct ordering of operations.

Finally, we'll emit the primary and secondary database endpoints plus auto-generated password:

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```typescript
// Output the primary and secondary database ARNs, and the auto-generated admin password.
export const primary = primaryDb.endpoint;
export const secondary = secondaryDb.endpoint;
export const password = dbPassword.result;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Output the primary and secondary database ARNs, and the auto-generated admin password.
pulumi.export('primary', primary_db.endpoint)
pulumi.export('secondary', secondary_db.endpoint)
pulumi.export('password', db_password.result)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Output the primary and secondary database ARNs, and the auto-generated admin password.
ctx.Export("primary", primaryDb.Endpoint)
ctx.Export("secondary", secondaryDb.Endpoint)
ctx.Export("password", dbPassword.Result)
return nil
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// Output the primary and secondary database ARNs, and the auto-generated admin password.
return new Dictionary<string, object?>
{
    ["primary"] = primaryDb.Endpoint,
    ["secondary"] = secondaryDb.Endpoint,
    ["password"] = dbPassword.Result,
};
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
# Output the primary and secondary database ARNs, and the auto-generated admin password.
outputs:
  primary: ${primary.endpoint}
  secondary: ${secondary.endpoint}
  password: ${dbPassword.result}
```

{{% /choosable %}}

Using these, we can easily access our new instance. Don't worry, the password is automatically encrypted!

For good measure, since all of our AWS resources are meant to use the explicit providers, and not the ambient default configuration, we can [disable default providers altogether](https://www.pulumi.com/blog/disable-default-providers/):

```bash
$ pulumi config set --path pulumi:disable-default-providers[0] "aws"
```

If we forget to pass an explicit provider, we now get an error:

```
error: Default provider for 'aws' disabled. 'urn:pulumi:dev::aws-multireg-rds::aws:rds/instance:Instance::primary' must use an explicit provider.
```

Now that we've got everything set up, we run `pulumi up` which orchestrates everything end-to-end:

```bash
$ pulumi up
Updating (dev)

     Type                            Name                  Status
 +   pulumi:pulumi:Stack             aws-multireg-rds-dev  created
 +   ├─ pulumi:providers:aws         euProvider            created
 +   ├─ pulumi:providers:aws         usProvider            created
 +   ├─ random:index:RandomPassword  dbPassword            created
 +   ├─ aws:rds:Instance             primary               created
 +   └─ aws:rds:Instance             secondary             created

Outputs:
    password : [secret]
    primary  : "primarybe35b53.c0q7bvujknic.us-east-1.rds.amazonaws.com:3306"
    secondary: "secondaryacb6a3d.c8qninoaapw8.eu-west-2.rds.amazonaws.com:3306"

Resources:
    + 6 created

Duration: 27m0s
```

## Winding Down

In this article, you saw some reasons why deploying your infrastructure across multiple regions, accounts, or clusters may be necessary. You saw that Pulumi supports two forms of configuration -- implicit configuration set at the CLI with `pulumi config` as well as explicit provider configuration which is constructed and passed programmatically -- and how and when to use them, often in tandem with one another.

The specific example shown to demonstrate multi-region in action deployed an AWS RDS primary database to a US region and a secondary read replica to Europe, which is a common architecture to improve resilience and performance. The power of full programming languages gives you a ton of flexibility in how you orchestrate such complex architectures.

Hopefully this post put a new tool in your infrastructure as code toolbelt! Happy cloud spelunking.
