---
title: "Programming Model"
meta_desc: An in depth overview of the the Pulumi Programming Model and common terms associated with the platform.
menu:
  intro:
    parent: concepts
    weight: 1

aliases: ["/docs/reference/programming-model/"]
---

This page describes the Pulumi programming model. These are the core concepts used when authoring an infrastructure as code program. Each program describes a set of desired infrastructure resources; the Pulumi CLI knows how to run, preview, and deploy those resources, both for the initial provisioning, as well as subsequent updating.

## Introduction {#introduction}

In this section, we will see the most basic concepts required to start declaring your infrastructure with Pulumi. Throughout the remainder of this page, we'll examine the ins and outs of Pulumi's programming model concepts.

## Programs {#programs}

Pulumi programs are written in general-purpose programming languages, including [JavaScript]({{< relref "/docs/intro/languages/javascript" >}}), [TypeScript]({{< relref "/docs/intro/languages/javascript" >}}), [Python]({{< relref "/docs/intro/languages/python" >}}), [Go]({{< relref "/docs/intro/languages/go" >}}) or [any .NET language]({{< relref "/docs/intro/languages/dotnet" >}}) such as C#, F#, or VB. You use the language's native tools and libraries, including [Pulumi's own packages]({{< relref "/docs/reference/pkg" >}}) containing infrastructure resource types.

Although you use general-purpose languages, Pulumi is still a declarative infrastructure as code tool. After writing a program, you run the Pulumi CLI command `pulumi up`, which executes the program and determines the desired infrastructure state for all resources declared. The CLI will show you a preview of changes to be made, including all new resources to be created and existing resources to update or destroy. After confirming, Pulumi will carry out the changes.

### Program Structure

Pulumi programs are structured as projects and stacks. The distinction between them is:

* [Program](#programs): a collection of files written in your chosen programming language
* [Project]({{< relref "project" >}}): a directory containing a program, with metadata, so Pulumi knows how to run it
* [Stack]({{< relref "stack" >}}): an instance of your project, each often corresponding to a different cloud environment

Infrastructure and application artifacts can be managed together or separately. For instance, Pulumi can build and publish Docker container images containing application code when you do a `pulumi up`, alongside the private registry and container service infrastructure that consumes it. Equally as well, however, your infrastructure can reference independently deployed artifacts.

A program becomes a project by virtue of a `Pulumi.yaml` manifest that describes it in the root directory. Each project can be instantiated multiple times. For instance, you can have distinct development, staging, and production stacks. Learn more about projects [here]({{< relref "project" >}}) and stacks [here]({{< relref "stack" >}}).

### Declaring Infrastructure

To declare new infrastructure in your program, allocate a [resource](#resources) _object_ whose _properties_ correspond to the desired state of your infrastructure. Because Pulumi uses existing general-purpose languages, this is done using standard [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming) techniques.

For example, this complete program creates a new AWS EC2 security group and an instance that uses it:

{{< langchoose csharp >}}

```javascript
let aws = require("@pulumi/aws");

let group = new aws.ec2.SecurityGroup("web-sg", {
    description: "Enable HTTP access",
    ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] }],
});

let server = new aws.ec2.Instance("web-server", {
    ami: "ami-6869aa05",
    instanceType: "t2.micro",
    securityGroups: [ group.name ], // reference the security group resource above
});
```

```typescript
import * as aws from "@pulumi/aws";

let group = new aws.ec2.SecurityGroup("web-sg", {
    description: "Enable HTTP access",
    ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] }],
});

let server = new aws.ec2.Instance("web-server", {
    ami: "ami-6869aa05",
    instanceType: "t2.micro",
    securityGroups: [ group.name ], // reference the security group resource above
});
```

```python
import pulumi_aws as aws

group = aws.ec2.SecurityGroup('web-sg',
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] }
    ])

server = aws.ec2.Instance('web-server',
    ami='ami-6869aa05',
    instance_type='t2.micro',
    security_groups=[group.name]) # reference the security group resource above
```

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws/ec2"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        group, err := ec2.NewSecurityGroup(ctx, "web-sg", &ec2.SecurityGroupArgs{
            Description: pulumi.String("Enable HTTP access"),
            Ingress: ec2.SecurityGroupIngressArray{
                ec2.SecurityGroupIngressArgs{
                    Protocol:   pulumi.String("tcp"),
                    FromPort:   pulumi.Int(80),
                    ToPort:     pulumi.Int(80),
                    CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
                },
            },
        })
        if err != nil {
            return err
        }
        server, err := ec2.NewInstance(ctx, "web-server", &ec2.InstanceArgs{
            Ami:            pulumi.String("ami-6869aa05"),
            InstanceType:   pulumi.String("t2.micro"),
            SecurityGroups: pulumi.StringArray{group.Name},
        })
        if err != nil {
            return err
        }
        return nil
    })
}
```

```csharp
using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Aws.Ec2.Inputs;

class Program
{
    static Task<int> Main()
    {
        return Deployment.RunAsync(async () => {
            var group = new SecurityGroup("web-sg", new SecurityGroupArgs {
                Description = "Enable HTTP access",
                Ingress = {
                    new SecurityGroupIngressArgs {
                        Protocol = "tcp",
                        FromPort = 80,
                        ToPort = 80,
                        CidrBlocks = { "0.0.0.0/0" }
                    }
                }
            });
            var server = new Instance("web-server", new InstanceArgs {
                Ami = "ami-6869aa05",
                InstanceType = "t2.micro",
                SecurityGroups = { group.Name }
            });
        });
    }
}
```

In this example, the two resource objects, plus their names and properties, tells Pulumi everything it needs to create, update, or delete your infrastructure. For example, Pulumi now knows you'd like an EC2 security group named `web-sg`, with a single ingress rule, and a `t2.micro`-sized EC2 instance running AMI `ami-8689aa05` using that security group. Pulumi understands the dependencies between resources---thanks to [output properties](#outputs)---which maximizes parallelism and ensures correct ordering. When you run the `pulumi up` command, Pulumi will compute this desired state, compare it to the current infrastructure you already have (if any), show you the delta, and let you confirm and carry out the changes.

You can export resulting infrastructure values that you wish to access outside your application. For example, adding this code to the example above exports the server's resulting IP address and DNS name:

{{< langchoose csharp >}}

```javascript
// ...
module.exports = {
    publicIp: server.publicIp,
    publicDns: server.publicDns,
};
```

```typescript
// ...
export let publicIp = server.publicIp;
export let publicDns = server.publicDns;
```

```python
# ...
pulumi.export('public_ip', server.public_ip)
pulumi.export('public_dns', server.public_dns)
```

```go
// ...
        ctx.Export("publicIp", server.PublicIp)
        ctx.Export("publicHostName", server.PublicDns)
        return nil
    })
}
```

```csharp
// ...
            return new Dictionary<string, object?> {
                { "publicIp",  server.PublicIp },
                { "publicDns",  server.PublicDns }
            };
        });
    }
}
```

The exported values are printed after you do a `pulumi up` and they are easy to access from the CLI's `pulumi stack output` command. To learn more, see [stack outputs](#stack-outputs) below.

## Pulumi SDK {#pulumipulumi}

The Pulumi SDK library defines Pulumi's most fundamental types and functions:

{{< langchoose csharp >}}

```javascript
let pulumi = require("@pulumi/pulumi");
```

```typescript
import * as aws from "@pulumi/pulumi";
```

```python
import pulumi
```

```go
import "github.com/pulumi/pulumi/sdk/go/pulumi"
```

```csharp
using Pulumi;
```

These are the most essential concepts defined by the Pulumi SDK:

* [Resources](#resources): how infrastructure is represented in Pulumi
* [Components](#components): create abstractions and aggregate other resources
* [Inputs and Outputs](#outputs): how resource properties and dependencies are represented
* [Secrets](#secrets): a type for encoding and using secrets inside your program
* [Config](#config): using configuration in your program
* [Providers](#providers): classes to control resource provider configuration
* [Stack Outputs](#stack-outputs): functions to export values from a stack
* [Stack References](#stack-references): reference one stack's outputs from another
* [Runtime Functions](#funcs): access important metadata and capabilities at runtime

### Resources {#resources}

All infrastructure resources are described by subclasses of the {{< pulumi-resource >}} class. There are two families of resources that branch from this base class:

* {{< pulumi-customresource >}}: external resources managed by a resource provider (most common)
* {{< pulumi-componentresource >}}: an aggregation of many resources to form a larger abstraction

#### Custom Resources

A resource's desired state is declared by constructing an instance:

{{< langchoose csharp >}}

```javascript
let res = new Resource(name, args, options);
```

```typescript
let res = new Resource(name, args, options);
```

```python
res = Resource(name, args, options)
```

```go
res, err := NewResource(ctx, name, args, opt1, opt2)
```

```csharp
var res = new Resource(name, args, options);
```

All resources have a required [`name`](#names) argument, which must be unique across resources of the same kind in a [stack]({{< relref "stack" >}}). This _logical name_ influences the _physical name_ assigned by your infrastructure's cloud provider, although [Pulumi auto-names resources](#autonaming) by default, so they may differ.

The `args` argument is an object with a set of named property input values that are used to initialize the resource. These can be normal raw values---such as strings, integers, lists, and maps---or [outputs from other resources](#outputs).

The `options` argument is optional, but [lets you control certain aspects of the resource](#resourceoptions), like custom provider configuration, explicit dependencies, or importing existing infrastructure.

##### Resource Names {#names}

Every resource managed by Pulumi has a logical name that you specify as an argument to its constructor. For instance, the logical name of this IAM role is `my-role`:

{{< langchoose csharp >}}

```javascript
let role = new aws.iam.Role("my-role");
```

```typescript
let role = new aws.iam.Role("my-role");
```

```python
role = iam.Role("my-role")
```

```go
role, err := iam.NewRole(ctx, "my-role", &iam.RoleArgs{})
```

```csharp
var role = new Aws.Iam.Role("my-role");
```

This logical name is used by Pulumi to track the identity of a resource across multiple deployments of the same program and is how Pulumi knows to choose between creating new resources and updating existing ones.

The name specified during resource creation is used in two key ways:

1. As a default prefix for the resource's physical name, assigned by the cloud provider.
2. To construct the [Universal Resource Name (URN)](#urns) used to track the resource across updates.

> Note that the variable names you use for resource objects aren't used in any way for either logical or physical resource naming. The variable simply lets you refer to that resource elsewhere in your program.

##### Physical Names and Auto-Naming {#autonaming}

A resource's logical and physical names may not match. In fact, most physical resource names in Pulumi are "auto-named." As a result, even if you give your IAM role has a logical name of `my-role`, as shown above, the physical name will typically look something like `my-role-d7c2fa0`.

This random suffix is added for two reasons:

* It ensures that two stacks for the same project can be deployed without risk of collision. This helps you to multi-instance your project more easily, whether that's for many development or testing stacks, or even scaling to new regions. Without auto-naming, you would need to manually distinguish these resources with different physical names.

* It allows Pulumi to do zero-downtime resource updates. Certain updates require replacing resources, rather than updating them in place, due to the way cloud providers work. By default, Pulumi creates replacements first, then updates existing references to them, and finally deletes the old resources. If it weren't for auto-naming, Pulumi would need to do things in a very different order: namely, it would need to delete resources first, and create new instances afterwards, which is far more impactful and leads to downtime.

Auto-naming can be overridden by manually specifying a physical name on your resource for use cases that require precise names. Most resources offer this option by way of a `name` property that may be specified in the argument object to the constructor:

{{< langchoose csharp >}}

```javascript
let role = new aws.iam.Role("my-role", {
    name: "my-role-001",
});
```

```typescript
let role = new aws.iam.Role("my-role", {
    name: "my-role-001",
});
```

```python
role = iam.Role('my-role', {
    name='my-role-001'
})
```

```go
role, err := iam.NewRole(ctx, "my-role", &iam.RoleArgs{
    Name: pulumi.String("my-role-001"),
})
```

```csharp
var role = new Aws.Iam.Role("my-role", new Aws.Iam.RoleArgs
{
    Name = "my-role-001",
});
```

> If `name` doesn't work, consult the documentation for the specific resource you are creating. Some resources use a different property to override the auto-naming. For instance, the `aws.s3.Bucket` type uses the property `bucket` instead of `name`. Other resources, like `aws.kms.Key`, don't even have physical names and instead use other auto-generated IDs to uniquely identify them.

Overriding auto-naming opens your project up to naming collisions. As a result, for resources that may need to be replaced, you should specify [`deleteBeforeReplace: true` in the resources's options](#deletebeforereplace). This ensures old resources are deleted before new ones are recreated.

The physical and logical names don't need to match. You may even elect to construct the name using your project and stack names. This protects you from naming collisions similar to auto-naming while still having nice names, although `deleteBeforeReplace` is still necessary:

{{< langchoose csharp >}}

```javascript
let role = new aws.iam.Role("my-role", {
    name: "my-role-" + pulumi.getProject() + "-" + pulumi.getStack(),
}, { deleteBeforeReplace: true });
```

```typescript
let role = new aws.iam.Role("my-role", {
    name: `my-role-${pulumi.getProject()}-${pulumi.getStack()}`,
}, { deleteBeforeReplace: true });
```

```python
role = iam.Role('my-role', {
    name='my-role-%s-%s'.format(pulumi.get_project(), pulumi.get_stack())
}, opts=ResourceOptions(delete_before_replace=True))
```

```go
role, _ := iam.NewRole(ctx, "my-role", &iam.RoleArgs{
    Name: fmt.Sprintf("my-role-%s-%s", ctx.Project(), ctx.Stack()),
}, pulumi.DeleteBeforeReplace(true))
```

```csharp
var role = new Aws.Iam.Role("my-role", new Aws.Iam.RoleArgs
    {
        Name = "my-role-" + Deployment.Instance.ProjectName + "-" + Deployment.Instance.StackName,
    },
    new CustomResourceOptions { DeleteBeforeReplace = true }
);
```

##### Resource URNs {#urns}

Each resource is assigned a [Uniform Resource Name (URN)](https://en.wikipedia.org/wiki/Uniform_Resource_Name) which globally uniquely identifies that resource. You will seldom need to interact with an URN directly, unless you are writing a tool, but it is fundamental to how Pulumi works, so it's good to have a general awareness of it.

The URN is automatically constructed from the project name, stack name, resource name, resource type, and the types of all the parent resources (in the case of component resources). For example:

```
urn:pulumi:production::acmecorp-website::custom:resources:Resource$aws:s3/bucket:Bucket::my-bucket
           ^^^^^^^^^^  ^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^
          <stack-name>  <project-name>        <parent-type>          <resource-type>  <resource-name>
```

The URN must be globally unique. This means all of the components that go into a URN must be unique within your program. If you create two resources of the same name, type, and parent path, for instance, you will see an error:

```
error: Duplicate resource URN 'urn:pulumi:production::acmecorp-website::custom:resources:Resource$aws:s3/bucket:Bucket::my-bucket'; try giving it a unique name
```

Any change to the URN of a resource will cause the old and new resources to be treated as unrelated---the new one will be created (since it was not in the prior state) and the old one will be deleted (since it is not in the new desired state). This happens when you change the `name` used to construct the resource or the structure of a resource's parent hierarchy. Both of these operations will lead to a different URN, and thus `create` and `delete` operations instead of an `update` or `replace` operation on the existing resource. As a result, changes to names must be made with care.

> If you'd like to rename a resource without destroying the old one, refer to the [`aliases`](#aliases) capability.

Resources constructed as children of a [component](#components) should make sure that their names will be unique across multiple instances of the component.  In general, the name of the component instance itself (the `name` parameter passed in to the component constructor) shoud be used as part of the name of the child resources.

##### Resource Arguments

A resource's expected argument parameter will differ by resource type. Each resource specifies a number of named input properties that control all of the behavior of the resulting infrastructure. To determine what arguments a resource supports, refer to that resource's [API documentation]({{< relref "/docs/reference/pkg" >}}).

##### Resource Options {#resourceoptions}

All resource constructors also accept an `options` argument which can provide the following additional resource options controlling how the resource will be managed by Pulumi:

* [`additionalSecretOutputs`](#additionalsecretoutputs): specify properties that must be encrypted as secrets
* [`aliases`](#aliases): specify aliases for this resource, so that renaming or refactoring doesn't replace it
* [`customTimeouts`](#customtimeouts): override the default retry/timeout behavior for resource provisioning
* [`deleteBeforeReplace`](#deletebeforereplace): override the default create-before-delete behavior when replacing
* [`dependsOn`](#dependson): specify additional explicit dependencies in addition to the automatic ones
* [`ignoreChanges`](#ignorechanges): declare that changes to certain properties should be ignored during diffing
* [`import`](#import): adopt an existing resource from your cloud account under the control of Pulumi
* [`parent`](#parent): establish a parent/child relationship between resources
* [`protect`](#protect): prevent accidental deletion of a resource by marking it protected
* [`provider`](#provider): pass an [explicitly configured provider](#explicit-provider-configuration), instead of using the default global provider
* [`transformations`](#transformations): dynamically transform a resource's properties on the fly

###### `additionalSecretOutputs`

This option specifies a list of named output properties which should be treated as [secrets](#secrets), ensuring that they are encrypted. This augments the list of values that Pulumi detects itself based on secret inputs to the resource.

This example ensures the password generated for a database resource is an encrypted secret:

{{< langchoose csharp >}}

```javascript
let db = new Database("new-name-for-db", { /*...*/ },
    { additionalSecretOutputs: ["password"] });
```

```typescript
let db = new Database("new-name-for-db", { /*...*/ },
    { additionalSecretOutputs: ["password"] });
```

```python
db = Database('db',
    opts=ResourceOptions(additional_secret_outputs=['password']))
```

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.AdditionalSecretOutputs([]string{"password"}))
```

```csharp
var db = new Database("new-name-for-db", new DatabaseArgs(),
    new CustomResourceOptions { AdditionalSecretOutputs = { "password" } });
```

Only entire top-level resource properties can be marked secret, so if there is sensitive data nested inside of a property, the entire top-level output property must be marked as secret.

###### `aliases`

This option provides a list of aliases for a resource or component. If you're changing the name, type, or parent path of a resource or component, you can add the old name to the list of `aliases` for a resource to ensure that existing resources will be migrated to the new name instead of being deleted and replaced with the new named resource.

For example, imagine we changed our database resource's name from `"old-name-for-db"` to `"new-name-for-db"`. By default, when we run `pulumi up`, we will see that the old resource will be deleted, and the new one created. If we annotate that resource with the `aliases` option, however, it will be updated in-place instead:

{{< langchoose csharp >}}

```javascript
let db = new Database("new-name-for-db", {/*...*/},
    { aliases: [{ name: "old-name-for-db" }] });
```

```typescript
let db = new Database("new-name-for-db", {/*...*/},
    { aliases: [{ name: "old-name-for-db" }] });
```

```python
db = Database('db',
    opts=ResourceOptions(aliases=[Alias(name='old-name-for-db')]))
```

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.Aliases(pulumi.Alias{Name: pulumi.String("old-name-for-db")}))
```

```csharp
var db = new Database("new-name-for-db", new DatabaseArgs(),
    new CustomResourceOptions { Aliases = { new Alias { Name = "old-name-for-db"} } });
```

The `aliases` option accepts a list of old identifiers. If a resource has been renamed multiple times, it may contain many. This list may contain old `Alias` objects and/or old [resource URNs](#urns).

The above example used `Alias` objects with the old resource names. These values may specify any combination of the old name, type, parent, stack, and/or project values. Alternatively, you can just specify the URN directly:

{{< langchoose csharp >}}

```javascript
let db = new Database("new-name-for-db", {/*...*/},
    { aliases: [ "urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db" ] });
```

```typescript
let db = new Database("new-name-for-db", {/*...*/},
    { aliases: [ "urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db" ] });
```

```python
db = Database('db',
    opts=ResourceOptions(aliases=['urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db']))
```

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.Aliases([]pulumi.Alias{pulumi.Alias{
        URN: pulumi.URN("urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db"),
    }})
)
```

```csharp
var db = new Database("new-name-for-db", new DatabaseArgs(),
    new CustomResourceOptions { Aliases = { new Alias {
        Urn = "urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db" } } });
```

###### `customTimeouts`

This option provides a set of custom timeouts for `create`, `update`, and `delete` operations on a resource. These timeouts are specified using a duration string like `"5m"` (5 minutes), `"40s"` (40 seconds), or `"1d"` (1 day). Supported duration units are `"ns"`, `"us"` (or `"µs"`), `"ms"`, `"s"`, `"m"`, and `"h"` (nanoseconds, microseconds, milliseconds, seconds, minutes, and hours, respectively).

> For the most part, Pulumi automatically waits for operations to complete, and times out appropriately. In some circumstances, however, including working around bugs in the infrastructure provider, custom timeouts may be necessary.

This example specifies that the create operation should wait up to 30 minutes to complete, before timing out:

{{< langchoose csharp >}}

```javascript
let db = new Database("db", {/*...*/},
    { customTimeouts: { create: "30m" } });
```

```typescript
let db = new Database("db", {/*...*/},
    { customTimeouts: { create: "30m" } });
```

```python
db = Database('db',
    opts=ResourceOptions(custom_timeouts=CustomTimeouts(create='30m')))
```

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.Timeouts(&pulumi.CustomTimeouts{Create: "30m"}))
```

```csharp
var db = new Database("db", new DatabaseArgs(),
    new CustomResourceOptions { CustomTimeouts = new CustomTimeouts { Create = TimeSpan.FromMinutes(30) } });
```

###### `deleteBeforeReplace`

A resource may need to be replaced if an immutable property is changed. In these cases, the cloud provider does not support updating an existing resource, and so a new instance will be created, and the old one deleted. By default, Pulumi will create new instances of resources, before deleting old ones, during a replacement operation. This minimizes downtime.

Setting the `deleteBeforeReplace` option to `true` specifies that replacements of the resource should _first_ delete the existing resource _before_ creating its replacement. This has a cascading impact on dependencies and may result in replacement of many more resources than the default behavior, often leading to downtime. However, this may be necessary for some resources that manage scarce resources behind the scenes, and/or resources that cannot exist side-by-side.

This example requests that our database is deleted entirely before its replacement is created:

{{< langchoose csharp >}}

```javascript
let db = new Database("db", {/*...*/},
    { deleteBeforeReplace: true});
```

```typescript
let db = new Database("db", {/*...*/},
    { deleteBeforeReplace: true});
```

```python
db = Database("db",
    opts=ResourceOptions(delete_before_replace=True))
```

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.DeleteBeforeReplace(true))
```

```csharp
// The resource will be deleted before it's replacement is created
var db = new Database("db", new DatabaseArgs(),
    new CustomResourceOptions { DeleteBeforeReplace = true });
```

###### `dependsOn`

The `dependsOn` option provides a list of explicit resource dependency resources.

Pulumi automatically tracks dependencies between resources when you supply an input argument that came from another resource's [output properties](#outputs). In some cases, however, you may need to explicitly specify additional dependencies that Pulumi doesn't know about, but must respect. This might happen if a dependency is external to the infrastructure itself---such as an application dependency---or is implied due to an ordering or eventual consistency requirement. These dependencies ensure that resource creation, update, and deletion is done in the correct order.

This example demonstrates making `res2` dependent on `res1`, even if there is no property-level dependency:

{{< langchoose csharp >}}

```javascript
let res1 = new MyResource("res1", {/*...*/});
let res2 = new MyResource("res2", {/*...*/}, { dependsOn: [res1] });
```

```typescript
let res1 = new MyResource("res1", {/*...*/});
let res2 = new MyResource("res2", {/*...*/}, { dependsOn: [res1] });
```

```python
res1 = MyResource("res1");
res2 = MyResource("res2", opts=ResourceOptions(depends_on=[res1]));
```

```go
res1, _ := NewMyResource(ctx, "res1", &MyResourceArgs{/*...*/})
res2, _ := NewMyResource(ctx, "res2", &MyResourceArgs{/*...*/}, pulumi.DependsOn([]Resource{res1}))
```

```csharp
var res1 = new MyResource("res1", new MyResourceArgs());
var res2 = new MyResource("res2", new MyResourceArgs(), new CustomResourceOptions { DependsOn = { res1 } });
```

###### `ignoreChanges`

This option specifies a list of properties which will be ignored when updating existing resources. Any properties specified in this list, that are also specified in the resource's arguments, will only be used when creating the resource---and ignored entirely while updating it.

For instance, in this example, the resource's `prop` property will have its value of `"new-value"` set when initially creating resource, but from then on, any and all changes will be ignored:

{{< langchoose csharp >}}

```javascript
let res = new MyResource("res",
    { prop: "new-value" }, { ignoreChanges: ["prop"] });
```

```typescript
let res = new MyResource("res",
    { prop: "new-value" }, { ignoreChanges: ["prop"] });
```

```python
res = MyResource("res",
    prop="new-value",
    opts=ResourceOptions(ignore_changes=["prop"]))
```

```go
res, _ := NewMyResource(ctx, "res",
    &MyResourceArgs{Prop: "new-value"},
    pulumi.IgnoreChanges([]string{"prop"}))
```

```csharp
var res = new MyResource("res",
    new MyResourceArgs { Prop = "new-value" },
    new CustomResourceOptions { IgnoreChanges = { "prop" } });
```

You would use the `ignoreChanges` option to avoid changes in properties leading to diffs or to change defaults for a property without forcing all existing deployed stacks to update or replace the affected resource. This is common after you've imported existing infrastructure provisioned by another method into Pulumi, where there may be historical drift that you'd prefer to retain than have to replace and reconstruct some critical parts of your infrastructure.

> **Note:** The property names passed to `ignoreChanges` should always be the "camelCase" version of
> the property name as used in the core Pulumi resource model.

###### `import`

This option lets you import an existing cloud resource, such that Pulumi takes over management of it. Imported resources may have been provisioned by any method, including manually in the cloud console or cloud CLI, with a different infrastructure as code tool, and so on.

To import a resource, first specify the `import` option with the resource's ID. This ID is the same that would be returned by the `id` property for any resource created by Pulumi; this is resource-specific. Pulumi reads the current state of the resource with the given ID from the backing provider, such as AWS, Azure, GCP, or Kubernetes.

Next, you must also specify all required arguments to the resource constructor, such that it exactly matches the state to import. In this manner, the final program you end up with is capable of accurately generating matching desired state.

This example imports an existing EC2 security group with ID `sg-04aeda9a214730248` and instance with ID `i-06a1073de86f4adef`:

{{< langchoose csharp >}}

```javascript
let aws = require("@pulumi/aws");

let group = new aws.ec2.SecurityGroup("web-sg", {
    name: "web-sg-62a569b",
    ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] }],
}, { import: "sg-04aeda9a214730248" });

let server = new aws.ec2.Instance("web-server", {
    ami: "ami-6869aa05",
    instanceType: "t2.micro",
    securityGroups: [ group.name ],
}, { import: "i-06a1073de86f4adef" });
```

```typescript
import * as aws from "@pulumi/aws";

let group = new aws.ec2.SecurityGroup("web-sg", {
    name: "web-sg-62a569b",
    ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] }],
}, { import: "sg-04aeda9a214730248" });

let server = new aws.ec2.Instance("web-server", {
    ami: "ami-6869aa05",
    instanceType: "t2.micro",
    securityGroups: [ group.name ],
}, { import: "i-06a1073de86f4adef" });
```

```python
# IMPORTANT: Python appends an underscore (`import_`) to avoid conflicting with the keyword.

import pulumi_aws as aws

group = aws.ec2.SecurityGroup('web-sg',
    name='web-sg-62a569b',
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] }
    ],
    opts=ResourceOptions(import_='sg-04aeda9a214730248'))

server = aws.ec2.Instance('web-server',
    ami='ami-6869aa05',
    instance_type='t2.micro',
    security_groups=[group.name],
    opts=ResourceOptions(import_='i-06a1073de86f4adef'))
```

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
server, err := ec2.NewInstance(ctx, "web-server",
    &ec2.InstanceArgs{
        Ami:            pulumi.String("ami-6869aa05"),
        InstanceType:   pulumi.String("t2.micro"),
        SecurityGroups: pulumi.StringArray{group.Name},
    },
    pulumi.Import(pulumi.ID("i-06a1073de86f4adef")),
)
if err != nil {
    return err
}
```

```csharp
var group = new SecurityGroup("web-sg",
    new SecurityGroupArgs {
        Name = "web-sg-62a569b",
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
var server = new Instance("web-server",
    new InstanceArgs {
        Ami = "ami-6869aa05",
        InstanceType = "t2.micro",
        SecurityGroups = { group.Name }
    },
    new CustomResourceOptions {
        ImportId = "i-06a1073de86f4adef"
    }
);
```

For this to work, your Pulumi stack must be configured correctly---e.g., in this case, the correct AWS region.

If the resource's arguments differ from the imported state, the import will fail. This will result in a message, `warning: inputs to import do not match the existing resource; importing this resource will fail`; selecting "details" in the `pulumi up` preview will show you exactly what differs. Attempting to proceed will fail with a message, `error: inputs to import do not match the existing resource`. To fix these errors, ensure that your program computes state that matches the resource to be imported fully.

> Because of auto-naming, it is common to run into this when importing a resource's name property. Unless you explicitly specify a name, Pulumi will auto-generate one, which is guaranteed not to match, because it will have a random hex suffix. To fix this problem, explicitly specify the resource's name [as described here](#autonaming). Notice that has been done in the above example for the EC2 security group, by passing `"web-sg-62a569b"` as its name property in its arguments.

Once a resource has been successfully imported, remove the `import` option, and Pulumi will have adopted the resource fully.

###### `parent`

This option specifies a parent for the resource. This is used to associate children to the parents that encapsulate or are responsible for them, as with [component resources](#components). The default behavior is to parent each resource to the implicitly-created `pulumi:pulumi:Stack` component resource that is a root resource for all Pulumi stacks.

For example, this code creates two resources, a `parent` and `child`, the latter of which is parented to the former:

{{< langchoose csharp >}}

```javascript
let parent = new MyResource("parent", {/*...*/});
let child = new MyResource("child", {/*...*/}, { parent: parent });
```

```typescript
let parent = new MyResource("parent", {/*...*/});
let child = new MyResource("child", {/*...*/}, { parent: parent });
```

```python
parent = MyResource("parent");
child = MyResource("child", opts=ResourceOptions(parent=parent));
```

```go
parent, _ := NewMyResource(ctx, "parent", &MyResourceArgs{/*...*/})
child, _ := NewMyResource(ctx, "child", &MyResourceArgs{/*...*/}, pulumi.Parent(parent))
```

```csharp
var parent = new MyResource("parent", new MyResourceArgs());
var child = new MyResource("child", new MyResourceArgs(),
    new CustomResourceOptions { Parent = parent });
```

Using parents can help to understand causality; that is, why a given resource was created in the first place. For example, this `pulumi up` output shows that we have an AWS Virtual Private Cloud (VPC) with two subnets attached to it, and that this VPC directly belongs to the implicit `pulumi:pulumi:Stack` resource:

```
Previewing update (dev):

     Type                       Name                             Plan
     pulumi:pulumi:Stack        parent-demo-dev
 +   ├─ awsx:x:ec2:Vpc          default-vpc-866580ff             create
 +   │  ├─ awsx:x:ec2:Subnet    default-vpc-866580ff-public-1    create
 +   │  └─ awsx:x:ec2:Subnet    default-vpc-866580ff-public-0    create
```

###### `protect`

Marks a resource as protected. A protected resource cannot be deleted directly: First, you must set `protect: false` and run `pulumi up`. Then, you can delete the resource by removing the line of code or by running `pulumi destroy`.  The default is to inherit this value from the parent resource, and `false` for resources without a parent.

{{< langchoose csharp >}}

```javascript
let db = new Database("db", {}, { protect: true});
```

```typescript
let db = new Database("db", {}, { protect: true});
```

```python
db = Database("db", opts=ResourceOptions(protect=True))
```

```go
db, _ := NewDatabase(ctx, "db", &DatabaseArgs{}, pulumi.Protect(true));
```

```csharp
var db = new Database("db", new DatabaseArgs(), new CustomResourceOptions { Protect = true });
```

###### `provider`

A provider for the resource. See [Providers](#providers).  The default is to inherit this value from the parent resource, and to use the ambient provider specified by Pulumi configuration for resources without a parent.

{{< langchoose csharp >}}

```javascript
let provider = new aws.Provider("provider", { region: "us-west-2" });
let vpc = new aws.ec2.Vpc("vpc", {}, { provider: provider });
```

```typescript
let provider = new aws.Provider("provider", { region: "us-west-2" });
let vpc = new aws.ec2.Vpc("vpc", {}, { provider: provider });
```

```python
provider = Provider("provider", region="us-west-2")
vpc = ec2.Vpc("vpc", opts=ResourceOptions(provider=provider))
```

```go
provider, _ := aws.NewProvider(ctx, "provider", &aws.ProviderArgs{Region: pulumi.StringPtr("us-west-2")})
vpc, _ := ec2.NewVpc(ctx, "vpc", &ec2.VpcArgs{}, pulumi.Provider(provider))
```

```csharp
var provider = new Aws.Provider("provider", new Aws.ProviderArgs { Region = "us-west-2" });
var vpc = new Aws.Ec2.Vpc("vpc", new Aws.Ec2.VpcArgs(), new CustomResourceOptions { Provider = provider });
```

###### `transformations`

The `transformations` option provides a list of transformations to apply to the resource and all of its children. This can be used to override or modify the inputs to child resources of a component, for example to add other resource options (like `ignoreChanges` or `protect`) or to modify an input property (like adding to `tags` or changing a property which is not configurable via the component directly).

Each transformation is a callback that gets invoked by the Pulumi runtime, and receives the resource type, name, input properties, resource options, and the resource instance object itself. The callback can return a new set of resource input properties and resource options which will replace and be used to construct the resource instead of the original values.

This example looks for all VPC and Subnet resources inside of a component's child hierarchy, and adds an option to ignore any changes for `tags` properties on them (perhaps because we manage all VPC and Subnet tags outside of Pulumi):

{{< langchoose >}}

```javascript
const vpc = new MyVpcComponent("vpc", {}, {
    transformations: [args => {
        if (args.type === "aws:ec2/vpc:Vpc" || args.type === "aws:ec2/subnet:Subnet") {
            return {
                props: args.props,
                opts: pulumi.mergeOptions(args.opts, { ignoreChanges: ["tags"] })
            }
        }
        return undefined;
    }],
});
```

```typescript
const vpc = new MyVpcComponent("vpc", {}, {
    transformations: [args => {
        if (args.type === "aws:ec2/vpc:Vpc" || args.type === "aws:ec2/subnet:Subnet") {
            return {
                props: args.props,
                opts: pulumi.mergeOptions(args.opts, { ignoreChanges: ["tags"] })
            }
        }
        return undefined;
    }],
});
```

```python
def transformation(args: ResourceTransformationArgs):
    if args.type_ == "aws:ec2/vpc:Vpc" or args.type_ == "aws:ec2/subnet:Subnet":
        return ResourceTransformationResult(
            props=args.props,
            opts=ResourceOptions.merge(args.opts, ResourceOptions(
                ignore_changes=["tags"],
            )))

vpc = MyVpcComponent("vpc", opts=ResourceOptions(transformations=[transformation]))
```

```go
transformation := func(args *pulumi.ResourceTransformationArgs) *pulumi.ResourceTransformationResult {
    if args.Type == "aws:ec2/vpc:Vpc" || args.Type == "aws:ec2/subnet:Subnet" {
        return &pulumi.ResourceTransformationResult{
            Props: args.Props,
            Opts:  append(args.Opts, pulumi.IgnoreChanges([]string{"tags"}))
        }
    }
    return nil
}

vpc := MyVpcComponent("vpc", pulumi.Transformations([]pulumi.ResourceTransformation{transformation}))
```

```csharp
var vpc = new MyVpcComponent("vpc", new ComponentResourceOptions
{
    Transformations =
    {
        args =>
        {
            if (args.Resource.GetResourceType() == "aws:ec2/vpc:Vpc" ||
                args.Resource.GetResourceType() === "aws:ec2/subnet:Subnet")
            {
                return new ResourceTransformationResult
                {
                    Args: args.Args,
                    Options: ResourceOptions.Merge(
                        args.Options,
                        new CustomResourceOptions { IgnoreChanges =  { "tags" } }),
                };
            }

            return null;
        }
    },
});
```

Transformations can also be applied in bulk to many resources in a stack by using the `registerStackTransformation` function.

##### Resource Getter Functions {#resource-get}

It's possible to look up an existing resource by its ID using the static `get` function that is available on all resource types. This differs from `import` functionality in that, although the resulting resource object's state will match the live state from an existing environment, its management will not come under the control of Pulumi. A resource read in this manner will never be updated or deleted by Pulumi during the course of an update.

This can be used to consume properties from a resource provisioned elsewhere. For example, this program reads an existing EC2 Security Group whose ID is `sg-0dfd33cdac25b1ec9` and uses it as input when creating an EC2 Instance:

{{< langchoose csharp >}}

```javascript
let aws = require("@pulumi/aws");

let group = aws.ec2.SecurityGroup.get("sg-0dfd33cdac25b1ec9");

let server = new aws.ec2.Instance("web-server", {
    ami: "ami-6869aa05",
    instanceType: "t2.micro",
    securityGroups: [ group.name ], // reference the security group resource above
});
```

```typescript
import * as aws from "@pulumi/aws";

let group = aws.ec2.SecurityGroup.get("sg-0dfd33cdac25b1ec9");

let server = new aws.ec2.Instance("web-server", {
    ami: "ami-6869aa05",
    instanceType: "t2.micro",
    securityGroups: [ group.name ], // reference the security group resource above
});
```

```python
import pulumi_aws as aws

group = aws.ec2.SecurityGroup.get('sg-0dfd33cdac25b1ec9')

server = aws.ec2.Instance('web-server',
    ami='ami-6869aa05',
    instance_type='t2.micro',
    security_groups=[group.name]) # reference the security group resource above
```

```go
import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws/ec2"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        group, err := ec2.GetSecurityGroup(ctx, "group", pulumi.ID("sg-0dfd33cdac25b1ec9"), nil)
        if err != nil {
            return err
        }
        server, err := ec2.NewInstance(ctx, "web-server", &ec2.InstanceArgs{
            Ami:            pulumi.String("ami-6869aa05"),
            InstanceType:   pulumi.String("t2.micro"),
            SecurityGroups: pulumi.StringArray{group.Name},
        })
        if err != nil {
            return err
        }
        return nil
    })
}
```

```csharp
using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Aws.Ec2.Inputs;

class Program
{
    static Task<int> Main()
    {
        return Deployment.RunAsync(async () => {
            var group = SecurityGroup.Get("sg-0dfd33cdac25b1ec9");

            var server = new Instance("web-server", new InstanceArgs {
                Ami = "ami-6869aa05",
                InstanceType = "t2.micro",
                SecurityGroups = { group.Name }
            });
        });
    }
}
```

Importantly, Pulumi will never attempt to modify the Security Group in this example. It simply reads back its state from your currently configured cloud account, and then uses it as input for the EC2 Instance.

#### Component Resources {#components}

A component resource is a logical grouping of other resources. Components usually instantiate a set of other related resources in their constructor, aggregating them as children, and creating a larger, useful abstraction that encapsulates its implementation details.

Here are a few examples of components:

* A `Vpc` that automatically comes with built-in best practices.
* An `AcmeCorpVirtualMachine` that adheres to your company's requirements, like tagging.
* A `KubernetesCluster` that can create EKS, AKS, and GKE clusters depending on the target.

The implicit `pulumi:pulumi:Stack` resource is itself a component that contains all top-level resources in a program.

##### Authoring a New Component

To author your own new component, either in a program or in a reusable library, create a subclass of {{< pulumi-componentresource >}}. Inside of its constructor, you will chain to the base constructor, passing its type string, name, arguments, and options. Also inside of its constructor, you will allocate any child resources, passing the [`parent`](#parent) option as appropriate to ensure component children are parented correctly.

Here's a simple component example:

{{< langchoose csharp >}}

```javascript
class MyComponent extends pulumi.ComponentResource {
    constructor(name, opts) {
        super("pkg:index:MyComponent", name, {}, opts);
    }
}
```

```typescript
class MyComponent extends pulumi.ComponentResource {
    constructor(name, opts) {
        super("pkg:index:MyComponent", name, {}, opts);
    }
}
```

```python
class MyComponent(pulumi.ComponentResource):
    def __init__(self, name, opts = None):
        super().__init__('pkg:index:MyComponent', name, None, opts)
```

```go
type MyComponent struct {
    pulumi.ResourceState
}

func NewMyComponent(ctx *pulumi.Context, name string, opts ...pulumi.ResourceOption) (*MyComponent, error) {
    myComponent := &MyComponent{}
    err := ctx.RegisterComponentResource("pkg:index:MyComponent", name, myComponent, opts...)
    if err != nil {
        return nil, err
    }

    return myComponent, nil
}
```

```csharp
class MyComponent : Pulumi.ComponentResource
{
    public MyComponent(string name, ComponentResourceOptions opts)
        : base("pkg:index:MyComponent", name, opts);
    {
        // initialization logic.

        // Signal to the UI that this resource has completed construction.
        this.RegisterOutputs();
    }
}
```

Upon creating a new instance of `MyComponent`, the call to the base constructor (using `super`/`base`) registers the component instance with the Pulumi engine. This records the resource's state and tracks it across program deployments so that you see diffs during updates like a regular resource (even though components have no provider logic associated with them). Since all resources must have a name, a component constructor should accept a name and pass it to `super`.

> If you wish to have full control over a custom resource's lifecycle---including running specific code when a resource has been updated or deleted---you should look into [dynamic providers](#dynamicproviders). These let you create full-blown resource abstractions in your language of choice.

A component must register a unique type name, such as `pkg:index:MyComponent` in the previous example. To reduce the potential of other type name conflicts, this name contains the package and module name, in addition to the type:  `<package>:<module>:<type>`. These names are namespaced alongside non-component resources, such as `aws:lambda:Function`.

For more information about components, [see the Pulumi Components tutorial]({{< relref "/docs/tutorials/aws/s3-folder-component" >}}).

##### Creating Child Resources

Components will often contain child resources. This entails two things. First, the names are often derived from the component's name, to ensure uniqueness, such as by using the component's name as a prefix. Second, children must be registered as such, by passing the component itself as [the `parent` option](#parent) when constructing a resource.

This example demonstrates both:

{{< langchoose csharp >}}

```javascript
let bucket = new aws.s3.Bucket(`${name}-bucket`,
    {/*...*/}, { parent: this });
```

```typescript
let bucket = new aws.s3.Bucket(`${name}-bucket`,
    {/*...*/}, { parent: this });
```

```python
bucket = s3.Bucket(f"{name}-bucket",
    opts=pulumi.ResourceOptions(parent=self))
```

```go
bucket, err := s3.NewBucket(ctx, fmt.Sprintf("%s-bucket", name),
    &s3.BucketArgs{ /*...*/ }, pulumi.Parent(myComponent))
```

```csharp
var bucket = new Aws.S3.Bucket($"{name}-bucket",
    new Aws.S3.BucketArgs(/*...*/), new CustomResourceOptions { Parent = this });
```

##### Registering Component Outputs

Components can define their own output properties using {{< pulumi-componentresource-registeroutputs >}}. The Pulumi engine uses this information to display the logical outputs of the component and any changes will be shown during an update.

For example, this registers an S3 bucket's computed domain name, which won't be known until the bucket is created:

{{< langchoose csharp >}}

```javascript
this.registerOutputs({
    bucketDnsName: bucket.bucketDomainName,
})
```

```typescript
this.registerOutputs({
    bucketDnsName: bucket.bucketDomainName,
})
```

```python
self.register_outputs({
    bucketDnsName: bucket.bucketDomainName
})
```

```go
ctx.RegisterResourceOutputs(myComponent, pulumi.Map{
    "bucketDnsName": bucket.BucketDomainName,
})
```

```csharp
this.RegisterOutputs(new Dictionary<string, object>
{
    { "bucketDnsName", bucket.BucketDomainName }
});
```

The call to register outputs typically happens at the very end of the component's constructor.

The call to `registerOutputs` also tells Pulumi that the resource is done registering children and should be considered fully constructed, so---although it's not enforced---the best practice is to call it in all components even if no outputs need to be registered.

##### Inheriting Resource Providers

One option all resources have is the ability to pass an [explicit resource provider](#providers) to supply explicit configuration settings. For instance, you may want to ensure that all AWS resources are created in a different region than the globally configured region. In the case of components, the challenge is that these providers must flow from parent to children.

To support, this component resources accept a new `providers` option that other custom resources don't have. This value contains a map from provider name to the explicit provider instance to use for that package. This can then be used by a component to fetch the proper `provider` object to use for any child resources.

{{< langchoose csharp >}}

```javascript
let component = new MyComponent("...", {
    providers: {
        aws: useast1,
        kubernetes: myk8s,
    },
});
```

```typescript
let component = new MyComponent("...", {
    providers: {
        aws: useast1,
        kubernetes: myk8s,
    },
});
```

```python
component = MyComponent('...', ResourceOptions(providers={
    'aws': useast1,
    'kubernetes': myk8s,
}))
```

```go
component, err := NewMyResource(ctx, "...", nil, pulumi.ProviderMap(
    map[string]pulumi.ProviderResource{
        "aws":        awsUsEast1,
        "kubernetes": myk8s,
    },
))
```

```csharp
var component = new MyResource("...", new ComponentResourceOptions {
    Providers = {
        { "aws", awsUsEast1 },
        { "kubernetes", myk8s }
    }
});
```

If a component is itself a child of another component, its set of providers is inherited from its parent by default.

### Inputs and Outputs {#outputs}

Resource properties are treated specially in Pulumi, both for purposes of input and output.

All resource arguments accept so-called _inputs_. Inputs are values of type {{< pulumi-input >}}, a type that permits either a raw value of a given type (like string, integer, boolean, list, map, and so on), an asynchronously computed value (i.e., a `Promise` or `Task`), or an output read from another resource's properties.

All resource properties on the instance object itself are so-called _outputs_. Outputs are values of type {{< pulumi-output >}}, which behave very much like [promises](https://en.wikipedia.org/wiki/Futures_and_promises); this is necessary because outputs are not fully known until the infrastructure resource has actually completed provisioning, which happens asynchronously. Outputs are also how Pulumi tracks dependencies between resources.

Outputs, therefore, represent two things:

1. The eventual raw value of the output
2. The dependency on the source(s) of the output value

Pulumi automatically captures dependencies when you pass an output from one resource as input to another, ensuring that physical infrastructure resources are not created or updated until all their dependencies are available and up-to-date.

Because outputs are asynchronous, their actual raw values are not immediately available. If you need to access an output's raw value---for example, to compute a derived, new value, or because you want to log it---you have these options:

* [Apply](#apply): a callback that receives the raw value, and computes a new output
* [Lifting](#lifting): directly read properties off an output value
* [Interpolation](#outputs-and-strings): concatenate string outputs with other strings directly

#### Apply {#apply}

To access the raw value of an output, and transform that value into a new value, use {{< pulumi-apply >}}. This method accepts a callback that will be eventually invoked with the raw value, once it is available.

For example, the following creates an HTTPS URL from the DNS name of a virtual machine:

{{< langchoose csharp >}}

```javascript
let url = virtualmachine.dnsName.apply(dnsName => "https://" + dnsName);
```

```typescript
let url = virtualmachine.dnsName.apply(dnsName => "https://" + dnsName);
```

```python
url = virtual_machine.dns_name.apply(
    lambda dns_name: "https://" + dns_name
)
```

```go
url := vpc.DnsName.ApplyString(func(dnsName string) string {
    return "https://" + dnsName
})
```

```csharp
var url = virtualmachine.DnsName.Apply(dnsName => "https://" + dnsName);
```

The result of the call to {{< pulumi-apply >}} is a new {{< pulumi-output >}}. So in this example, the `url` variable itself is also an {{< pulumi-output >}}. It will resolve to the new new value returned from the callback, and carries the dependencies of the original {{< pulumi-output >}}. If the callback itself returns an {{< pulumi-output >}}, the dependencies of that output are also kept in the resulting {{< pulumi-output >}}.

> **Note:** during some program executions, {{< pulumi-apply >}} won't be run, such as during a preview when resource output values may remain unknown, so you should avoid side-effects within the callbacks. For this reason, you should not allocate new resources inside of your callbacks either, as it could lead to `pulumi preview` being wrong.

If you have multiple outputs and need to join them, the [all](#all) function acts like an apply over many resources.

##### All {#all}

The {{< pulumi-all >}} function acts like an {{< pulumi-apply >}} over multiple {{< pulumi-output >}}s. This function joins over an entire list of outputs, waiting for all of them to become available, and then provides them to the supplied callback. This can be used to compute an entirely new output value, such as adding or concatenating outputs from two different resources together, or creating a new data structure that uses them. Just like with {{< pulumi-apply >}}, the result of {{< pulumi-all >}} is itself an {{< pulumi-output >}}.

For example, let's take a server and database name, and use them to create a database connection string:

{{< langchoose csharp >}}

```javascript
var pulumi = require("@pulumi/pulumi");
// ...
let connectionString = pulumi.all([sqlServer.name, database.name])
    .apply(([server, db]) => `Server=tcp:${server}.database.windows.net;initial catalog=${db}...`);
```

```typescript
import * as pulumi from "@pulumi/pulumi";
// ...
let connectionString = pulumi.all([sqlServer.name, database.name])
    .apply(([server, db]) => `Server=tcp:${server}.database.windows.net;initial catalog=${db}...`);
```

```python
from pulumi import Output
# ...
connection_string = Output.all(sql_server.name, database.name) \
    .apply(lambda args: f"Server=tcp:{args[0]}.database.windows.net;initial catalog={args[1]}...")
```

```go
connectionString := pulumi.All(sqlServer.Name, database.Name).ApplyT(
    func (args []interface{}) (string, error) {
        server := args[0].(string)
        db := args[1].(string)
        return fmt.Sprintf("Server=tcp:%s.database.windows.net;initial catalog=%s...", server, db)
    },
)
```

```csharp
// In .NET 'Output.Tuple' is used so that each unwrapped value will preserve their distinct type.
// 'Output.All' can be used when all input values have the same type (i.e. all are Output<string>)
var connectionString = Output.Tuple(sqlServer.name, database.name)
    .Apply(t => `Server=tcp:${t.Item1}.database.windows.net;initial catalog=${t.Item2}...`);
```

Notice that {{< pulumi-all >}} works by itself returning an output that represents the combination of multiple outputs, so that within the callback, the raw values are available inside of [a tuple](https://en.wikipedia.org/wiki/Tuple).

##### Accessing Properties of an Output {#lifting}

If you just need to access a property of an {{< pulumi-output >}} value, in order to pass that property's value as an argument to another resource's constructor, you can often just directly access it.

For example, if you need to read a domain record from an ACM certificates, that requires drilling into a resource's property value. Because that value is an output, we would normally need to use {{< pulumi-apply >}}:

{{< langchoose csharp >}}

```javascript
let certCertificate = new aws.acm.Certificate("cert", {
    domainName: "example.com",
    validationMethod: "DNS",
});
let certValidation = new aws.route53.Record("cert_validation", {
    records: [
        // Need to pass along a deep subproperty of this Output
        certCertificate.domainValidationOptions.apply(
            domainValidationOptions => domainValidationOptions[0].resourceRecordValue),
    ],
...
```

```typescript
let certCertificate = new aws.acm.Certificate("cert", {
    domainName: "example.com",
    validationMethod: "DNS",
});
let certValidation = new aws.route53.Record("cert_validation", {
    records: [
        // Need to pass along a deep subproperty of this Output
        certCertificate.domainValidationOptions.apply(
            domainValidationOptions => domainValidationOptions[0].resourceRecordValue),
    ],
...
```

```python
certificate = aws.acm.Certificate('cert',
    domain_name='example.com',
    validation_method='DNS'
)

record = aws.route53.Record('validation',
    records=[
        # Need to pass along a deep subproperty of this Output
        certificate.domain_validation_options.apply(
            lambda domain_validation_options: domain_validation_options[0]['resourceRecordValue']
        )
    ],
...
```

```go
// Helpers for accessing properties are not yet available in Go.
```

```csharp
// Helpers for accessing properties are not yet available in .NET.
```

To ease simple property and array element access, an {{< pulumi-output >}} _lifts_ the properties of the underlying value, behaving very much like an instance of it. This allows you to access properties and elements directly from the {{< pulumi-output >}} itself without needing {{< pulumi-apply >}}. If we return to the above example, we can now simplify it:

{{< langchoose csharp >}}

```javascript
let certCertificate = new aws.acm.Certificate("cert", {
    domainName: "example.com",
    validationMethod: "DNS",
});
let certValidation = new aws.route53.Record("cert_validation", {
    records: [
        certCertificate.domainValidationOptions[0].resourceRecordValue
    ],
...
```

```typescript
let certCertificate = new aws.acm.Certificate("cert", {
    domainName: "example.com",
    validationMethod: "DNS",
});
let certValidation = new aws.route53.Record("cert_validation", {
    records: [
        certCertificate.domainValidationOptions[0].resourceRecordValue
    ],
...
```

```python
certificate = aws.acm.Certificate('cert',
    domain_name='example.com',
    validation_method='DNS'
)

record = aws.route53.Record('validation',
    records=[
        certificate.domain_validation_options[0].resource_record_value
    ],
...
```

```go
// Helpers for accessing properties are not yet available in Go.
```

```csharp
// Helpers for accessing properties are not yet available in .NET.
```

This approach is easier to read and write, while not losing any important dependency information that is needed to properly create and maintain the stack. This approach doesn't work in all cases, but when it does, it can be a great help.

> In JavaScript and TypeScript, a 'lifted' property access on an `Output<T>` that wraps `undefined` will produce another `Output<T>` with the `undefined` value instead of throwing or producing a 'faulted' `Output<T>`. In this manner lifted property accesses behave like the [`?.` (optional chaining operator)](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html#optional-chaining) in JavaScript and TypeScript. This makes it much easier to form a chain of property accesses on an `Output<T>`.

```javascript
let certValidation = new aws.route53.Record("cert_validation", {
  records: [certCertificate.domainValidationOptions[0].resourceRecordValue],

// instead of

let certValidation = new aws.route53.Record("cert_validation", {
  records: [certCertificate.apply(cc => cc ? cc.domainValidationOptions : undefined)
                           .apply(dvo => dvo ? dvo[0] : undefined)
                           .apply(o => o ? o.resourceRecordValue : undefined)],
```

```typescript
let certValidation = new aws.route53.Record("cert_validation", {
  records: [certCertificate.domainValidationOptions[0].resourceRecordValue],

// instead of

let certValidation = new aws.route53.Record("cert_validation", {
  records: [certCertificate.apply(cc => cc ? cc.domainValidationOptions : undefined)
                           .apply(dvo => dvo ? dvo[0] : undefined)
                           .apply(o => o ? o.resourceRecordValue : undefined)],
```

##### Working with Outputs and Strings {#outputs-and-strings}

Outputs containing strings cannot be used directly in operations like string concatenation. _String interpolation_ lets you more easily build a string out of various output values, without needing {{< pulumi-apply >}} or {{< pulumi-all >}}. This can be used to export a stack output, provide a dynamically computed string as a new resource argument, or even just for diagnostic purposes.

For example, say you want to create a URL from hostname and port output values:

{{< langchoose csharp >}}

```javascript
let hostname = // get some Output
let port = // get some Output

// Would like to produce a string equivalent to: http://${hostname}:${port}/
let url = // ?
```

```typescript
let hostname: Output<string> = // get some Output
let port: Output<number> = // get some Output

// Would like to produce a string equivalent to: http://${hostname}:${port}/
let url = // ?
```

```python
hostname: Output[str] = # get some Output
port: Output[int] = # get some Output

# Would like to produce a string equivalent to: http://${hostname}:${port}/
url = # ?
```

```go
var hostname pulumi.StringOutput
var port pulumi.NumberOutput

url := // ?
```

```csharp
Output<string> hostname = // get some Output
Output<int> port = // get some Output

// Would like to produce a string equivalent to: http://{hostname}:{port}/
var url = // ?
```

It is possible to use [apply](#apply) and [all](#all) to do this, of course:

```javascript
let url = pulumi.all([hostname, port]).
    apply(([hostname, port]) => `http://${hostname}:${port}/`);
```

```typescript
let url: Output<string> = pulumi.all([hostname, port]).
    apply(([hostname, port]) => `http://${hostname}:${port}/`);
```

```python
url = Output.all(hostname, port).apply(lambda l: f"http://{l[0]}:{l[1]}/")
```

```go
url := pulumi.All(hostname, port).ApplyString(func (args []interface{}) string {
    return fmt.Sprintf("http://%s:%d/", args[0], args[1])
})
```

```csharp
var url = pulumi.Tuple(hostname, port).Apply(t => `http://{t.Item1}:{t.Item2}/`);
```

This is verbose and unwieldy, however. To make this common task easier, Pulumi exposes helpers that allow you to create strings that contain outputs---internally hiding all of the messiness required to join them together:

```javascript
// concat takes a list of args and concatenates all of them into a single output:
const url1 = pulumi.concat("http://", hostname, ":", port, "/");
// interpolate takes a JavaScript "template literal" and expands outputs correctly:
const url2 = pulumi.interpolate `http://${hostname}:${port}/`;
```

```typescript
// concat takes a list of args and concatenates all of them into a single output:
const url1: Output<string> = pulumi.concat("http://", hostname, ":", port, "/");
// interpolate takes a JavaScript "template literal" and expands outputs correctly:
const url2: Output<string> = pulumi.interpolate `http://${hostname}:${port}/`;
```

```python
# concat takes a list of args and concatenates all of them into a single output:
url = Output.concat("http://", hostname, ":", port, "/")
```

```go
url := pulumi.Sprintf("http://%s:%d/", hostname, port)
```

```csharp
// Interpolate takes a JavaScript "template literal" and expands outputs correctly:
var url = Output.Format($"http://{hostname}:{port}/");
```

##### Convert Input to Output {#frominput}

It is possible to turn an {{< pulumi-input >}} into an {{< pulumi-output >}} value. Resource arguments already accept outputs as input values, however in some cases you need to know that a value is definitely an {{< pulumi-output >}} at runtime. This can be helpful because, since {{< pulumi-input >}} values have many possible representations---a raw value, a promise, or an output---you would normally need to handle all possible cases; by first transforming that value into an {{< pulumi-output >}}, you can treat it uniformly instead.

For example, this code transforms an {{< pulumi-input >}} into an {{< pulumi-output >}} so that it can use the {{< pulumi-apply >}} function:

{{< langchoose csharp >}}

```javascript
function split(input) {
    let output = pulumi.output(input);
    return output.apply(v => v.split());
}
```

```typescript
function split(input: pulumi.Input<string>): pulumi.Output<string[]> {
    let output = pulumi.output(input);
    return output.apply(v => v.split());
}
```

```python
def split(input):
    output = Output.from_input(input);
    return output.apply(lambda v: v.split());
}
```

```go
func split(input pulumi.StringInput) pulumi.StringArrayOutput {
    return input.ToStringOutput().ApplyStringArray(func(s string) []string {
        return strings.Split(s, ",")
    })
}
```

```csharp
Output<string[]> Split(Input<string> input)
{
    var output = input.ToOutput()
    return output.Apply(v => v.Split(","));
}
```

### Secrets {#secrets}

All resource input and output values are recorded as [state]({{< relref "state" >}}), either stored in the Pulumi Service, a file, or a pluggable provider of your own choosing. These raw values are usually just server names, configuration settings, and so on. In some cases, however, these values contain sensitive data, such as database passwords or service tokens.

The Pulumi Service transmits and stores entire state files securely, however, Pulumi also supports encrypting specific values as "secrets" beyond this for extra protection. This ensures that these values never appear as plaintext in your state. The encryption uses automatic per-stack encryption keys provided by the Pulumi Service by default, or [you can use a provider of your own choosing]({{< relref "config#configuring-secrets-encryption" >}}).

There is a CLI aspect to secrets, in that the CLI's [`config set` command]({{< relref "config#configuration" >}}) supports a [`--secret` flag]({{< relref "config#secrets" >}}) to encrypt your stack's configuration settings.

There is also a runtime aspect to secrets, in that any {{< pulumi-output >}} value may be marked secret. If an output is a secret, then any computed values from it---such as those derived through an {{< pulumi-apply >}} call---will themselves be marked secret. All such values are stored encrypted inside of your state, and never in plaintext.

An {{< pulumi-output >}} can be marked secret a number of ways:

* Reading a secret from configuration using {{< pulumi-config-getsecret >}} or {{< pulumi-config-requiresecret >}}
* Creating a new secret value with {{< pulumi-secret-new >}}, like when generating a new random password
* Marking a resource as having secret properties using [`additionalSecretOutputs`](#additionalsecretoutputs)
* Computing a secret value by using {{< pulumi-apply >}} or {{< pulumi-all >}} with another secret value

As soon as an {{< pulumi-output >}} is marked secret, you can trust that the Pulumi engine will encrypt it no matter where it goes.

> *Note*: Inside of an {{< pulumi-apply >}} or {{< pulumi-all >}}, your secret will be decrypted for use within the callback in plaintext. It is up to your program to treat this value sensitively and only pass the value to code that you trust.

#### Programmatically Creating Secrets

There are two ways to programmatically create secret values:

{{< langchoose csharp >}}

<div class="language-prologue-javascript"></div>

* Using [`getSecret(key)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-getSecret" >}}) or [`requireSecret(key)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-requireSecret" >}}) when reading a value from config.
* Calling [`pulumi.secret(value)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#secret" >}}) to construct a secret from an existing value.

<div class="language-prologue-typescript"></div>

* Using [`getSecret(key)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-getSecret" >}}) or [`requireSecret(key)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-requireSecret" >}}) when reading a value from config.
* Calling [`pulumi.secret(value)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#secret" >}}) to construct a secret from an existing value.

<div class="language-prologue-python"></div>

* Using [`get_secret`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Config.get_secret" >}}) or [`require_secret`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Config.require_secret" >}}) when reading a value from config.
* Calling [`Output.secret`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Output.secret" >}}) to construct a secret from an existing value.

<div class="language-prologue-go"></div>

* Using `config.GetSecret(key)` or `config.RequireSecret(key)` when reading a value from config.
* Calling `pulumi.ToSecret(value)` to construct a secret from an existing value.

<div class="language-prologue-csharp"></div>

* Using `Config.GetSecret(key)` or `Config.RequireSecret(key)` when reading a value from config.
* Calling `Output.CreateSecret(value)` to construct a secret from an existing value.

To illustrate using these functions, let's create an AWS Parameter Store secure value. To do so, we need to pass an argument to initialize its `value` property. Unfortunately, the obvious thing to do---passing a raw, unencrypted value---will lead to its value also being stored unencrypted in the Pulumi state! Instead, we will ensure that the value is a secret:

{{< langchoose csharp >}}

```javascript
const cfg = new pulumi.Config()
const param = new aws.ssm.Parameter("a-secret-param", {
    type: "SecureString",
    value: cfg.requireSecret("my-secret-value"),
});
```

```typescript
const cfg = new pulumi.Config()
const param = new aws.ssm.Parameter("a-secret-param", {
    type: "SecureString",
    value: cfg.requireSecret("my-secret-value"),
});
```

```python
cfg = pulumi.Config()
param = ssm.Parameter("a-secret-param",
    type="SecureString",
    value=cfg.require_secret("my-secret-value"))
```

```go
cfg := config.New(ctx, "")
param, err := ssm.NewParameter(ctx, "a-secret-param", &ssm.ParameterArgs{
    Type:  "SecureString",
    Value: cfg.RequireSecret("my-secret-value"),
})
if err != nil {
    return err
}
```

```csharp
var cfg = new Pulumi.Config()
var param = new Aws.Ssm.Parameter("a-secret-param", new Aws.Ssm.ParameterArgs
{
    type = pulumi.String("SecureString"),
    value = cfg.RequireSecret("my-secret-value"),
});
```

As written, the `Parameter` resource's `value` property will be encrypted in the state file.

> Pulumi tracks the transitive usage of secrets, so that your secret won't end up accidentally leaking into the state file. This includes automatically marking data generated from secret inputs itself as secret, as well as fully encrypting any resource properties that include secrets in them.

#### How Secrets Relate to Outputs

Secrets have the same type {{< pulumi-output >}} as do other unencrypted resource outputs. The difference is that they are marked internally as needing encryption before persisting in the state file. When you combine an existing output that is marked as a secret using {{< pulumi-apply >}} or {{< pulumi-all >}}, the resulting output is also marked as a secret.

An {{< pulumi-apply >}}'s callback is given the plaintext value of the underlying secret. Although Pulumi ensures that the value returned from an {{< pulumi-apply >}} on a secret is also marked as secret, Pulumi cannot guarantee that the {{< pulumi-apply >}} callback itself will not expose the secret value---for instance, by explicitly printing the value to the console or saving it to a file. Be careful that you do not pass this plaintext value to code that might intentionally or accidentally expose it.

> Unlike regular outputs, secrets cannot be captured by Pulumi closure serialization system for use in serverless code. Attempting to do so will lead to an exception. We do plan to support this once we can ensure that the values will be persisted securely. See [pulumi/pulumi#2718](https://github.com/pulumi/pulumi/issues/2718).

#### Explicitly Marking Resource Outputs as Secrets

It is possible to mark resource outputs as containg secrets. In this case, Pulumi will automatically treat those outputs
as secrets and encrypt them in the state file and anywhere they flow to. To do so,
[use the "additional secret outputs" option, as described above]({{< relref "#additionalsecretoutputs" >}}).

### Stack Outputs {#stack-outputs}

A stack may export values as [stack outputs]({{< relref "stack#outputs" >}}). These outputs are shown during an update, can be easily retrieved from the Pulumi CLI, and are displayed in the Pulumi Console. They can be used for important values like resource IDs and computed IP addresses and DNS names. They can also be used for [inter-stack dependencies](#stack-references), such as when a lower layer of infrastructure needs to export values for consumption elsewhere.

To export values from a stack, use the following definition in the top-level of the entrypoint for your project:

{{< langchoose csharp >}}

```javascript
exports.url = resource.url;
```

```typescript
export let url = resource.url;
```

```python
pulumi.export("url", resource.url)
```

```go
ctx.Export("url", resource.Url)
```

```csharp
// The dictionary returned by the function passed to Deployment.Run will be used to provide all the exported values.
static Task Main() =>
    Deployment.Run(async () =>
    {
        return new Dictionary<string, object> {
            { "url", resource.Url }
        };
    });
```

From the CLI, you can then use [`pulumi stack output url`]({{< relref "/docs/reference/cli/pulumi_stack_output" >}}) to get the value and incorporate into other scripts or tools.

The right-hand side of a stack export can be a regular value, an [Output](#outputs), or a `Promise` (effectively, the same as an [Input](#outputs)). The actual values are resolved at the end of `pulumi up`.

Stack exports are effectively JSON serialized, though quotes are removed when exporting strings.

For example, this program:

{{< langchoose csharp >}}

```javascript
exports.x = "hello"
exports.o = {num: 42}
```

```typescript
export let x = "hello";
export let o = {num: 42};
```

```python
pulumi.export("x", "hello")
pulumi.export("o", {'num': 42})
```

```go
ctx.Export("x", pulumi.String("hello"))
ctx.Export("o", pulumi.Map(map[string]pulumi.Input{
    "num": pulumi.Int(42),
}))
```

```csharp
// The dictionary returned by the function passed to Deployment.Run will be used to provide all the exported values.
static Task Main() =>
    Deployment.Run(async () =>
    {
        return new Dictionary<string, object>
        {
            { "x", "hello" },
            { "o", new Dictionary<string, int> { { "num", 42 } } },
        };
    });
```

will lead to the following stack outputs:

```bash
$ pulumi stack output x
hello
$ pulumi stack output o
{"num": 42}
```

The full set of outputs can be rendered as JSON using `pulumi stack output --json`:

```bash
$ pulumi stack output --json
{
  "x": "hello",
  "o": {
      "num": 42
  }
}
```

> **Note**: If you export a resource, it too will be JSON serialized. This usually isn't what you want, especially as some resources can be quite large. If you only wanted to export its ID or name, for example, just export those properties directly.

Stack outputs respect secret annotations and will also be encrypted appropriately. If a stack contains any secret values, their plaintext values will not be shown by default. Instead, they will be displayed as `[secret]` in the CLI. Pass `--show-secrets` to `pulumi stack output` to see the plaintext value.

### Stack References {#stack-references}

Stack references allow you to access the [outputs](#stack-outputs) of one stack from another stack.

To reference values from another stack, create an instance of the `StackReference` type using the fully qualified name of the stack as an input, and then read exported stack outputs by their name:

{{< langchoose csharp >}}

```javascript
const pulumi = require("@pulumi/pulumi");
const other = new pulumi.StackReference("acmecorp/infra/other");
const otherOutput = other.getOutput("x");
```

```typescript
import * as pulumi from "@pulumi/pulumi";
const other = new pulumi.StackReference("acmecorp/infra/other");
const otherOutput = other.getOutput("x");
```

```python
from pulumi import StackReference

other = StackReference(f"acmecorp/infra/other")
other_output = other.get_output("x");
```

```go
other, err := pulumi.NewStackReference(ctx, "acmecorp/infra/other", nil)
if err != nil {
    return err
}
otherOutput := other.GetOutput(pulumi.String("x"))
```

```csharp
// StackReference is not currently supported in .NET.
//
// https://github.com/pulumi/pulumi/issues/3406.
```

Stack names must be fully qualified, including the organization, project, and stack name components, in the format `<organization>/<project>/<stack>`. For individual accounts, use your account name for the organization component.

### Config {#config}

Configuration allows you to parameterize your program based on externally managed configuration. This can be helpful if you want to, say, have a different number of servers in your production stack than in development.

> This section describes how to programmatically interact with configuration that has already been set. For more information on how to do so using the CLI, see [Configuration and Secrets]({{< relref "/docs/intro/concepts/config" >}}).

#### Reading Configuration Values

To read configuration set in your current stack, use the {{< pulumi-config >}} class.

Configuration values can be retrieved using either {{< pulumi-config-get >}} or {{< pulumi-config-require >}}. Using {{< pulumi-config-get >}} will return {{< language-null >}} if the configuration value was not provided, and {{< pulumi-config-require >}} will raise an exception with a helpful error message to prevent the deployment from continuing until the variable has been set using the CLI.

In this example, the name is required, and a lucky number is optional:

{{< langchoose csharp >}}

```javascript
let config = new pulumi.Config();
let name = config.require("name");
let lucky = config.getNumber("lucky") || 42;
console.log(`Hello, ${name} -- I see your lucky number is ${lucky}!`);
```

```typescript
let config = new pulumi.Config();
let name = config.require("name");
let lucky = config.getNumber("lucky") || 42;
console.log(`Hello, ${name} -- I see your lucky number is ${lucky}!`);
```

```python
config = pulumi.Config();
name = config.require('name');
lucky = config.get_number('lucky') or 42
print(f'Hello, {name} -- I see your lucky number is {lucky}!')
```

```go
conf := config.New(ctx, "")
name := conf.Require("name")
lucky, err := conf.TryInt("lucky")
if err != nil {
    lucky = 42
}
fmt.Printf("Hello, %v -- I see your lucky number is %v!", name, lucky)
```

```csharp
var config = new Pulumi.Config();
var name = config.Require("name");
var lucky = config.GetInt32("lucky") ?? 42;
Console.WriteLine($"Hello, {name} -- I see your lucky number is {lucky}!");
```

In this example, we have created an instance of the {{< pulumi-config >}} class, which is a bag of key/value pairs. On that instance, a number of getter functions allow us to read the currently-set values.

> This code uses the simple, empty constructor. If you are writing code that will be imported into a broader project, such as your own library of components, you should pass your library's name to the constructor. This string is used as a namespace for all configuration keys. The default constructor automatically uses the current project for that namespace.

The {{< pulumi-config >}} object also provides getters that ensure a value is marked secret, ensuring the underlying raw value is encrypted no matter where it goes. Read more about this in the [Secrets documentation](#secrets).

#### Typed Configuration Values

Configuration values are stored as strings, but can be parsed and retrieved as typed values. In addition to {{< pulumi-config-get >}} and {{< pulumi-config-require >}}, which are untyped, there are a family of typed functions.

For example, {{< pulumi-config-getnumber >}} will convert the string value to a number and return a {{< language-int32 >}} value instead of a string, and raise an exception if the value cannot be parsed as a number. We saw this in action above.

For richer structured data, the {{< pulumi-config-getobject >}} method can be used to parse JSON values which can be set on the command line with `pulumi config set` and the `--path` flag. For example:

```bash
$ pulumi config set --path data.active true
$ pulumi config set --path data.nums[0] 1
$ pulumi config set --path data.nums[1] 2
$ pulumi config set --path data.nums[2] 3
```

A program can read the `data` config into a rich object with:

{{< langchoose csharp >}}

```javascript
let config = new pulumi.Config();
let data = config.requireObject("data");
console.log(`Active: ${data.active}`);
```

```typescript
interface Data {
    active: boolean;
    nums: number[];
}

let config = new pulumi.Config();
let data = config.requireObject<Data>("data");
console.log(`Active: ${data.active}`);
```

```python
config = pulumi.Config()
data = config.require_object("data")
print(f"Active: ${data.active}")
```

```go
type Data struct {
    Active bool
    Nums   []int
}

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        var d Data
        cfg := config.New(ctx, "")
        cfg.RequireObject("data", &d)
        fmt.Printf("Active: %v\n", d.Active)
        return nil
    })
}
```

```csharp
var config = new Pulumi.Config();
var data = config.RequireObject<JsonElement>("data");
Console.WriteLine($"Active: {data.GetProperty("active")}");
```

### Providers {#providers}

You can use packages from your language's native package manager: for example, NPM for Node.js, Pip for Python, Go modules for Go, and NuGet for .NET. These packages may transitively depend on the Pulumi SDK, which itself is just a native package. The Pulumi SDK defines how resources created by a program will be communicated to the Pulumi engine. The ability to register resources with the Pulumi engine is the only difference between a Pulumi package and any other native package.

Any packages that create custom resources---classes that derive from the {{< pulumi-customresource >}} base class---will cause Pulumi to load an associated "resource provider plugin" at runtime, which is a binary that implements the Create, Read, Update, and Delete resources defined by the package. Normally plugins are installed automatically when you install the package, but you can also [manage plugins explicitly using the CLI]({{< relref "/docs/reference/cli/pulumi_plugin" >}}).

This is in contrast to a component resource---classes that derive from the {{< pulumi-componentresource >}} base class--whose logic is written entirely within that library itself, without any external plugin required. A component resource does not manage any external infrastructure state; instead, it simply aggregates existing resources into a larger abstraction.

Finally, _dynamic providers_ let you write an entire provider within your language of choice, without needing to create a resource provider plugin. This has the advantage that you can flexibly create new resource types---but with the disadvantage that you can't share them easily across multiple languages, as resource plugins are language-neutral.

#### Resource Providers

The resource provider for a custom resource is determined based on its package name. For example, the `aws` package will load a plugin named `pulumi-resource-aws`, and the `kubernetes` package will load a plugin named `pulumi-resource-kubernetes`. Each provider uses the configuration from its package to alter its behavior.

##### Default Provider Configuration

By default, each provider uses its package's global configuration settings, which are controlled by your stack's configuration. For example, if you run this CLI command:

```bash
$ pulumi config set aws:region us-west-2
```

Then deploying the following Pulumi program will create a single EC2 instance in the `us-west-2` region:

{{< langchoose csharp >}}

```javascript
let aws = require("@pulumi/aws");

let instance = new aws.ec2.Instance("myInstance", {
    instanceType: "t2.micro",
    ami: "myAMI",
});
```

```typescript
let aws = require("@pulumi/aws");

let instance = new aws.ec2.Instance("myInstance", {
    instanceType: "t2.micro",
    ami: "myAMI",
});
```

```python
from pulumi_aws import ec2

instance = ec2.Instance("myInstance", instance_type="t2.micro", ami="myAMI")
```

```go
vpc, err := ec2.NewInstance(ctx, "myInstance", &ec2.InstanceArgs{
    InstanceType: pulumi.String("t2.micro"),
    Ami:          pulumi.String("myAMI"),
})
```

```csharp
using Pulumi.Aws;

// Inside call to Deployment.Run(...)
var instance = new Aws.Ec2.Instance("myInstance", new Aws.Ec2.InstanceArgs
{
    InstanceType = "t2.micro",
    Ami = "myAMI",
});
```

##### Explicit Provider Configuration

While this works for the majority of Pulumi programs, some programs may have special requirements. For example, it may require the ability to deploy to multiple AWS regions simultaneously, or to deploy to a Kubernetes cluster created earlier in the program that requires explicitly creating, configuring, and referencing providers. This is typically done by instantiating the relevant package's `Provider` type and passing in the options for each {{< pulumi-customresource >}} or {{< pulumi-componentresource >}} that needs to use it. For example, the following configuration and program will create an ACM certificate in the `us-east-1` region and a load balancer listener in the `us-west-2` region.

{{< langchoose csharp >}}

```javascript
let pulumi = require("@pulumi/pulumi");
let aws = require("@pulumi/aws");

// Create an AWS provider for the us-east-1 region.
let useast1 = new aws.Provider("useast1", { region: "us-east-1" });

// Create an ACM certificate in us-east-1.
let cert = new aws.acm.Certificate("cert", {
    domainName: "foo.com",
    validationMethod: "EMAIL",
}, { provider: useast1 });

// Create an ALB listener in the default region that references the ACM certificate created above.
let listener = new aws.lb.Listener("listener", {
    loadBalancerArn: loadBalancerArn,
    port: 443,
    protocol: "HTTPS",
    sslPolicy: "ELBSecurityPolicy-2016-08",
    certificateArn: cert.arn,
    defaultAction: {
        targetGroupArn: targetGroupArn,
        type: "forward",
    },
})
```

```typescript
let pulumi = require("@pulumi/pulumi");
let aws = require("@pulumi/aws");

// Create an AWS provider for the us-east-1 region.
let useast1 = new aws.Provider("useast1", { region: "us-east-1" });

// Create an ACM certificate in us-east-1.
let cert = new aws.acm.Certificate("cert", {
    domainName: "foo.com",
    validationMethod: "EMAIL",
}, { provider: useast1 });

// Create an ALB listener in the default region that references the ACM certificate created above.
let listener = new aws.lb.Listener("listener", {
    loadBalancerArn: loadBalancerArn,
    port: 443,
    protocol: "HTTPS",
    sslPolicy: "ELBSecurityPolicy-2016-08",
    certificateArn: cert.arn,
    defaultAction: {
        targetGroupArn: targetGroupArn,
        type: "forward",
    },
});
```

```python
import pulumi
import pulumi_aws as aws

# Create an AWS provider for the us-east-1 region.
useast1 = aws.Provider("useast1", region="us-east-1")

# Create an ACM certificate in us-east-1.
cert = aws.acm.Certificate("cert",
    domain_name="foo.com",
    validation_method="EMAIL",
    __opts__=pulumi.ResourceOptions(provider=useast1))

# Create an ALB listener in the default region that references the ACM certificate created above.
listener = aws.lb.Listener("listener",
    load_balancer_arn=load_balancer_arn,
    port=443,
    protocol="HTTPS",
    ssl_policy="ELBSecurityPolicy-2016-08",
    certificate_arn=cert.arn,
    default_action={
        "target_group_arn": target_group_arn,
        "type": "forward",
    })
```

```go
// Create an AWS provider for the us-east-1 region.
useast1, err := aws.NewProvider(ctx, "useast1", &aws.ProviderArgs{
    Region: pulumi.String("us-east-1"),
})
if err != nil {
    return err
}

// Create an ACM certificate in us-east-1.
cert, err := acm.NewCertificate(ctx, "myInstance", &acm.CertificateArgs{
    DomainName:       pulumi.String("foo.com"),
    ValidationMethod: pulumi.String("EMAIL"),
}, pulumi.Provider(useast1))
if err != nil {
    return err
}

// Create an ALB listener in the default region that references the ACM certificate created above.
listener, err := lb.NewListener(ctx, "myInstance", &lb.ListenerArgs{
    LoadBalancerArn: loadBalancerArn,
    Port:            pulumi.Int(443),
    Protocol:        pulumi.String("HTTPS"),
    SslPolicy:       pulumi.String("ELBSecurityPolicy-2016-08"),
    CertificateArn:  cert.Arn,
    DefaultActions: lb.ListenerDefaultActionArray{
        &lb.ListenerDefaultActionArgs{
            TargetGroupArn: targetGroupArn,
            Type:           pulumi.String("forward"),
        },
    },
})
if err != nil {
    return err
}
```

```csharp
using Pulumi;
using Pulumi.Aws;

class Program
{
   async Task Main() =>
       Deployment.Run(() =>
       {
           // Create an AWS provider for the us-east-1 region.
           var useast1 = new Aws.Provider("useast1", new Aws.ProviderArgs { Region = "us-east-1" });

           // Create an ACM certificate in us-east-1.
           var cert = new Aws.Acm.Certificate("cert", new Aws.Acm.CertifiateArgs
           {
               DomainName = "foo.com",
               ValidationMethod = "EMAIL",
           }, new ResourceArgs { Provider = useast1 });

           // Create an ALB listener in the default region that references the ACM certificate created above.
           var listener = new Aws.Lb.Listener("listener", new Aws.Lb.ListenerArgs
           {
               LoadBalancerArn = loadBalancerArn,
               Port = 443,
               Protocol = "HTTPS",
               SslPolicy = "ELBSecurityPolicy-2016-08",
               CertificateArn = cert.arn,
               DefaultAction: new Aws.Lb.ListenerDefaultAction
               {
                   TargetGroupArn = targetGroupArn,
                   Type = "forward",
               },
           });
       });
}
```

```bash
$ pulumi config set aws:region us-west-2
```

Component resources also accept a set of providers to use with their child resources. For example, the EC2 instance parented to `myResource` in the program below will be created in `us-east-1`, and the Kubernetes pod parented to `myResource` will be created in the cluster targeted by the "test-ci" context.

{{< langchoose csharp >}}

```javascript
class MyResource extends pulumi.ComponentResource {
    constructor(name, opts) {
        let instance = new aws.ec2.Instance("instance", { ... }, { parent: this });
        let pod = new kubernetes.core.v1.Pod("pod", { ... }, { parent: this });
    }
}

let useast1 = new aws.Provider("useast1", { region: "us-east-1" });
let myk8s = new kubernetes.Provider("myk8s", { context: "test-ci" });
let myResource = new MyResource("myResource", { providers: { aws: useast1, kubernetes: myk8s } });
```

```typescript
class MyResource extends pulumi.ComponentResource {
    constructor(name, opts) {
        let instance = new aws.ec2.Instance("instance", { ... }, { parent: this });
        let pod = new kubernetes.core.v1.Pod("pod", { ... }, { parent: this });
    }
}

let useast1 = new aws.Provider("useast1", { region: "us-east-1" });
let myk8s = new kubernetes.Provider("myk8s", { context: "test-ci" });
let myResource = new MyResource("myResource", { providers: { aws: useast1, kubernetes: myk8s } });
```

```python
class MyResource(pulumi.ComponentResource):
    def __init__(self, name, opts):
        instance = aws.ec2.Instance("instance", ..., __opts__=pulumi.ResourceOptions(parent=self))
        pod = kubernetes.core.v1.Pod("pod", ..., __opts__=pulumi.ResourceOptions(parent=self))

useast1 = aws.Provider("useast1", region="us-east-1")
myk8s = kubernetes.Provider("myk8s", context="test-ci")
my_resource = MyResource("myResource", pulumi.ResourceOptions(providers={
    "aws": useast1,
    "kubernetes": myk8s,
})
```

```go
useast1, err := aws.NewProvider(ctx, "useast1", &aws.ProviderArgs{
    Region: pulumi.String("us-east-1"),
})
if err != nil {
    return err
}
myk8s, err := kubernetes.NewProvider(ctx, "myk8s", &kubernetes.ProviderArgs{
    Context: pulumi.String("test-ci"),
})
if err != nil {
    return err
}
myResource, err := NewMyResource(ctx, "myResource", pulumi.ProviderMap(map[string]pulumi.ProviderResource{
    "aws": useast1,
    "kubernetes": myk8s,
}))
if err != nil {
    return err
}
```

```csharp
using Pulumi;
using Pulumi.Aws;
using Pulumi.Kubernetes;

class MyResource : pulumi.ComponentResource
{
    public MyResource(string name, ComponentResourceOptions opts)
        : base(name, opts)
    {
        var instance = new Aws.Ec2.Instance("instance", new Aws.Ec2.InstanceArgs { ... }, new CustomResourceOptions { Parent = this });
        var pod = new Kubernetes.Core.V1.Pod("pod", new Kubernetes.Core.V1.PodArgs { ... }, new CustomResourceOptions { Parent = this });
    }
}

class Program
{
   async Task Main() =>
       Deployment.Run(() =>
       {
           var useast1 = new Aws.Provider("useast1", new Aws.ProviderArgs { Region = "us-east-1" });
           var myk8s = new Kubernetes.Provider("myk8s", new Kubernetes.ProviderArgs { Context = "test-ci" });
           var myResource = new MyResource("myResource", new ComponentResourceOptions { Providers = { useast1, myk8s } });
       });
}
```

#### Dynamic Providers <span class="badge badge-preview">PREVIEW</span> {#dynamicproviders}

Every {{< pulumi-customresource >}} has a provider associated with it which knows how to `create`, `read`, `update`, and `delete` instances of the custom resource in the backing cloud provider. This provider plugin is defined by implementing the Pulumi Resource Provider gRPC interface. Most resources implement this without you needing to know how.

This plugin model is flexible and allows multi-language consumption of a shared set of resource providers. It does mean, however, that you need to implement a gRPC interface, and create and distribute a plugin. In some cases, it's useful to more rapidly create new resource types---for instance, if a feature is missing from your favorite provider, you'd like to create a resource model over some REST APIs, or you need to implement some custom CRUD logic.

Pulumi supports a concept called **dynamic providers** for this. Dynamic providers provide a flexible approach to defining custom resource types directly within the source code of your Pulumi program. They aren't as easy to share with other programs, and cannot be used across languages, but are as easy to create as implementing an interface.

You should consider implementing a dynamic provider if:

1. You need to manage a cloud resource that doesn't have provider support, and you expect to only use it from within one program. If you expect to use it from many programs, and in many languages, implementing a full provider is preferable.
2. You need to integrate custom logic into the deployment workflow that runs exactly during one or more of the `create`, `read`, `update`, or `delete` steps, instead of running "always" as part of a normal Pulumi program.

Dynamic providers are defined by first implementing the `pulumi.dynamic.ResourceProvider` interface. This interface supports all CRUD operations, but only the create function is required. A minimal implementation might look like this:

{{< langchoose csharp >}}

```javascript
const myProvider = {
    async create(inputs) {
        return { id: "foo", outs: {}};
    }
}
```

```typescript
const myProvider: pulumi.dynamic.ResourceProvider = {
    async create(inputs) {
        return { id: "foo", outs: {}};
    }
}
```

```python
from pulumi.dynamic import ResourceProvider, CreateResult

class MyProvider(ResourceProvider):
    def create(self, inputs):
        return CreateResult(id_="foo", outs={})
```

```go
// Dynamic Providers are currently not supported in Go.
```

```csharp
// Dynamic Providers are currently not supported in .NET.
```

This resource provider is then used to create a new kind of custom resource by inheriting from the `pulumi.dynamic.Resource` base class which is a subclass of `pulumi.CustomResource`:

{{< langchoose csharp >}}

```javascript
class MyResource extends pulumi.dynamic.Resource {
    constructor(name, props, opts) {
        super(myProvider, name, props, opts);
    }
}
```

```typescript
class MyResource extends pulumi.dynamic.Resource {
    constructor(name: string, props: {}, opts?: pulumi.CustomResourceOptions) {
        super(myProvider, name, props, opts);
    }
}
```

```python
from pulumi import ResourceOptions
from pulumi.dynamic import Resource
from typing import Any, Optional

class MyResource(Resource):
    def __init__(self, name: str, props: Any, opts: Optional[ResourceOptions] = None):
         super().__init__(MyProvider(), name, props, opts)
```

```go
// Dynamic Providers are currently not supported in Go.
```

```csharp
// Dynamic Providers are currently not supported in .NET.
```

We can now create instances of the new `MyResource` resource type in our program with `new MyResource("name", args)`, just like we would any ordinary resource. Pulumi understands how to use our custom provider logic at the right time.

Specifically, if Pulumi determines the resource has not yet been created, it will call the `create` method on the resource provider interface. If another Pulumi deployment happens and the resource already exists, Pulumi will call the `diff` method to determine whether a change can be made in place or whether a replacement is needed. If a replacement is needed, Pulumi will call `create` for the new resource and then `delete` for the old resource. If no replacement is needed, Pulumi will call `update`. In all cases, Pulumi first calls the `check` method with the resource arguments to give the provider a chance to validate that the arguments are valid. And finally, if Pulumi needs to read an existing resource without managing it directly, it will call `read`. See below for details on the details of each of these functions.

##### How Dynamic Providers Work

Dynamic providers are a flexible and low-level mechanism to plug arbitrary code directly into the deployment process. Whereas most code in a Pulumi program runs as part of constructing the desired state of resources (the "resource graph"), the code inside a dynamic provider's interface implementation, such as `create` or `update`, runs instead during resource provisioning (while the resource graph is being turned into a set of CRUD operations scheduled against the cloud providers).

In fact, these two phases of execution actually run in completely separate processes. The construction of a `new MyResource` happens inside the JavaScript, Python, or Go process running your Pulumi program. But your implementations of `create` or `update` are executed by a special resource provider binary called `pulumi-resource-pulumi-nodejs`. This binary is what actually implements the Pulumi resource provider gRPC interface and speaks directly to the Pulumi engine.

Because your implementation of the resource provider interface must be used by a different process, potentially at a different point in time, dynamic providers are built on top of the same [function serialization]({{< relref "/docs/tutorials/aws/serializing-functions" >}}) that is used for turning callbacks into AWS Lambdas or Google Cloud Functions. Because of this serialization, there are some limits on what can be done inside the implementation of the resource provider interface, which you can read more about in the function serialization documentation.

##### Dynamic Resource Inputs

The inputs to your `pulumi.dynamic.ResourceProvider`'s functions come from subclasses of `pulumi.dynamic.Resource`. These include any values in the input arguments passed to the `pulumi.dynamic.Resource` constructor. This is just a map of key/value pairs, however in statically typed languages, you can declare types for these input shapes.

For example, `props` in this code ends up becoming the inputs to the resource provider functions:

{{< langchoose csharp >}}

```javascript
class MyResource extends pulumi.dynamic.Resource {
    constructor(name, props, opts) {
        super(myprovider, name, props, opts);
    }
}
```

```typescript
interface MyResourceInputs {
    myStringProp: pulumi.Input<string>;
    myBoolProp: pulumi.Input<boolean>;
    ...
}

class MyResource extends pulumi.dynamic.Resource {
    constructor(name: string, props: MyResourceInputs, opts?: pulumi.CustomResourceOptions) {
        super(myprovider, name, props, opts);
    }
}
```

```python
from pulumi import Input, ResourceOptions
from pulumi.dynamic import Resource
from typing import Any, Optional

class MyResourceInputs(object):
    my_string_prop: Input[str]
    my_bool_prop: Input[bool]
    def __init__(self, my_string_prop, my_bool_prop):
        self.my_string_prop = my_string_prop
        self.my_bool_prop = my_bool_prop

class MyResource(Resource):
    def __init__(self, name: str, props: MyResourceInputs, opts: Optional[ResourceOptions] = None):
         super().__init__(MyProvider(), name, {**vars(props)}, opts)
```

```go
// Dynamic Providers are currently not supported in Go.
```

```csharp
// Dynamic Providers are currently not supported in .NET.
```

##### Resource Provider Interface

Implementing the `pulumi.dynamic.ResourceProvider` interface requires implementing a subset of the following methods. Each of these methods may be asynchronous, and most implementations of these methods will perform network I/O to provision resources in a backing cloud provider or other resource model. There are several important contracts between a dynamic provider and the Pulumi CLI that inform when these methods are called and with what data.

Though the input properties passed to a `pulumi.dynamic.Resource` instance will usually be [`Input` values](#outputs) the dynamic provider's functions are invoked with the fully resolved input values in order to compose well with Pulumi resources. Strong typing for the inputs to your provider's functions can help clarify this. You can achieve this by creating a second interface with the same properties as your resource's inputs, but with fully unwrapped types.

{{< langchoose csharp >}}

```typescript
// Exported type.
export interface MyResourceInputs {
    myStringProp: pulumi.Input<string>;
    myBoolProp: pulumi.Input<boolean>;
    ...
}

// Non-exported type used by the provider functions.
// This interface contains the same inputs, but as un-wrapped types.
interface MyResourceProviderInputs {
    myStringProp: string;
    myBoolProp: boolean;
    ...
}

class MyResourceProvider extends pulumi.dynamic.ResourceProvider {
    async create(inputs: MyResourceProviderInputs): Promise<pulumi.dynamic.CreateResult> {
        ...
    }

    async diff(id: string, oldOutputs: MyResourceProviderOutputs, newInputs: MyResourceProviderInputs): Promise<pulumi.dynamic.DiffResult> {
        ...
    }
    ...
}

class MyResource extends pulumi.dynamic.Resource {
    constructor(name: string, props: MyResourceInputs, opts?: pulumi.CustomResourceOptions) {
        super(myprovider, name, props, opts);
    }
}
```

```python
from pulumi import Input, Output, ResourceOptions
from pulumi.dynamic import *
from typing import Any, Optional

class MyResourceInputs(object):
    my_string_prop: Input[str]
    my_bool_prop: Input[bool]

    def __init__(self, my_string_prop, my_bool_prop):
        self.my_string_prop = my_string_prop
        self.my_bool_prop = my_bool_prop

class _MyResourceProviderInputs(object):
    """
    MyResourceProviderInputs is the unwrapped version of the same inputs
    from the MyResourceInputs class.
    """
    my_string_prop: str
    my_bool_prop: bool

    def __init__(self, my_string_prop: str, my_bool_prop: bool):
        self.my_bool_prop = my_bool_prop
        self.my_string_prop = my_string_prop

class MyResourceProvider(ResourceProvider):
    def create(self, inputs: _MyResourceProviderInputs) -> CreateResult:
        ...
        return CreateResult()

    def diff(self, id: str, oldInputs: _MyResourceProviderInputs, newInputs: _MyResourceProviderInputs) -> DiffResult:
        ...
        return DiffResult()

class MyResource(Resource):
    def __init__(self, name: str, props: MyResourceInputs, opts: Optional[ResourceOptions] = None):
        super().__init__(MyResourceProvider(), name, {**vars(props)}, opts)
```

```go
// Dynamic Providers are currently not supported in Go.
```

```csharp
// Dynamic Providers are currently not supported in .NET.
```

###### `check(olds, news)`

`check` is invoked before any other methods, and is passed the resolved input properties that were originally provided to the resource constructor by the user. It is passed both the old input properties that were stored in the _state file_ after the previous update to the resource, as well as the new inputs from the current deployment. It has two jobs: (1) Verify that the inputs (particularly the news) are valid and return useful error messages if they are not, and (2) Return a set of checked inputs. The inputs returned from the call to `check` will be the inputs that the Pulumi engine uses for all further processing of the resource, including the values that will be passed back in to `diff`, `create`, `update`, or other operations. In many cases, the `news` can be returned directly as the checked inputs. But in cases where the provider needs to populate defaults, or do some normalization on values, it may want to do that in the `check` method so that this data is complete and normalized prior to being passed in to other methods.

###### `create(inputs)`

`create` is invoked when the URN of the resource created by the user is not found in the existing state of the deployment.  The engine passes the provider the checked inputs returned from the call to `check`. The `create` method is expected to do the work in the backing cloud provider to create the requested resource. It then returns two pieces of data: (1) an `id` that can uniquely identify the resource in the backing provider for later lookups, and (2) a set of `outputs` from the backing provider that should be returned to the user code as properties on the {{< pulumi-customresource >}} object, and stored in the _checkpoint_ file. If an error occurs, an exception can be thrown from the `create` method to return this error to the user.

###### `diff(id, olds, news)`

`diff` is invoked when the URN of the resource created by the user is found in the existing state of the deployment. This means the resource already exists, and will need to be either updated or replaced.  The `diff` method is passed the `id` of the resource---as returned by `create`, as well as the old outputs from the checkpoint file which are values returned from a previous call to either `create` or `update`. It is also passed the new checked inputs from the current deployment.  It returns four optional values:

* `changes`: `true` if the provider believes there is a difference between the `olds` and `news` and wants to do an `update` or `replace` to affect this change.
* `replaces`: An array of property names that have changed that should force a replacement. Returning a non-zero length array here will tell the Pulumi engine to schedule a replacement instead of an update, which might involve downtime, so this should only be used when a `diff` requested by the user cannot be implemented as an in-place update on the backing cloud provider.
* `stables`: An array of property names that are known not to change between updates. Pulumi will use this information to allow some {{< pulumi-apply >}} calls on {{< pulumi-output >}} to be processed during `previews` because it knows that the values of these will stay the same during an update.
* `deleteBeforeReplace`: `true` if the proposed replacements require deleting the existing resource before creating the new one. By default Pulumi will try to create the new resource before deleting the old one to avoid downtime.
If an error occurs, an exception can be thrown from the `diff` method to return this error to the user.

###### `update(id, olds, news)`

Update is invoked if the call to `diff` indicates replacement is not needed. It is passed the `id` of the resource as returned by `create`, and the old outputs from the checkpoint file which are values returned from a previous call to either `create` or `update`. It is also passed the new checked inputs from the current deployment. The `update` method is expected to do the work in the backing cloud provider to update an existing resource to the new desired state. It then returns a new set of `outputs` from the backing provider that should be returned to the user code as properties on the {{< pulumi-customresource >}} object, and stored into the checkpoint file. If an error occurs, an exception can be thrown from the `update` method to return this error to the user.

###### `delete(id, props)`

Delete is invoked if the URN exists in the previous state but not in the new desired state, or if a replacement is needed.  It is passed the `id` of the resource as returned by `create`, and the old outputs from the checkpoint file which are values returned from a previous call to either `create` or `update`. It is expected to delete the corresponding resource from the backing cloud provider. Nothing needs to be returned.  If an error occurs, an exception can be thrown from the `delete` method to return this error to the user.

###### `read(id, props)`

Read is invoked when the Pulumi engine needs to get data about a resource that is not managed by Pulumi. It is passed the `id` of the resource as tracked in the backing cloud provider, and an optional bag of additional properties that can be used to disambiguate the request if needed. The `read` method is expected to look up the requested resource, and return the canonical `id` and output properties of this resource if found. If an error occurs, an exception can be thrown from the `read` method to return this error to the user.

##### Dynamic Resource Outputs

Any outputs can be returned by your `create` function in the `outs` property of `pulumi.dynamic.CreateResult`.

> **Note:** The following only applies to statically typed languages.

If you need to access the outputs of your custom resource outside it with strong typing support, declare each output property returned in the `outs` property by your `create` function as a class member of the `pulumi.dynamic.Resource` itself. For example, in TypeScript, these must be declared as `public readonly` class members in your `pulumi.dynamic.Resource` class. These class members must also have the type `pulumi.Output<T>`.

> **Note:** The name of the class member must match the names of the output properties as returned by the `create` function.

{{< langchoose csharp >}}

```typescript
...

interface MyResourceProviderOutputs {
    myNumberOutput: number;
    myStringOutput: string;
}

class MyResourceProvider extends pulumi.dynamic.ResourceProvider {
    async create(inputs: MyResourceProviderInputs): Promise<pulumi.dynamic.CreateResult> {
        ...
        // Values are for an example only.
        return { id: "...", outs: { myNumberOutput: 12, myStringOutput: "some value" }};
    }
}

export class MyResource extends pulumi.dynamic.Resource {
    public readonly myStringOutput!: pulumi.Output<string>;
    public readonly myNumberOutput!: pulumi.Output<number>;

    constructor(name: string, props: MyResourceInputs, opts?: pulumi.CustomResourceOptions) {
        super(myprovider, name, { myStringOutput: undefined, myNumberOutput: undefined, ...props }, opts);
    }
}
```

```javascript
JavaScript does not support types.
```

```python
from pulumi import ResourceOptions, Input, Output
from pulumi.dynamic import Resource, ResourceProvider, CreateResult
from typing import Any, Optional

...
...

class MyProvider(ResourceProvider):
    def create(self, inputs):
        return CreateResult(id_="foo", outs={ 'my_number_output': 12, 'my_string_output': "some value" })

class MyResource(Resource):
    my_string_output: Output[str]
    my_number_output: Output[str]

    def __init__(self, name: str, props: MyResourceInputs, opts: Optional[ResourceOptions] = None):
         super().__init__(MyProvider(), name, { 'my_string_output': None, 'my_number_output': None, **vars(props) }, opts)
```

```go
// Dynamic Providers are not yet supported in Go.
```

```csharp
// Dynamic Providers are currently not supported in .NET.
```

##### Dynamic Provider Examples

###### Example: Random

This example generates a random number using a dynamic provider. It highlights using dynamic providers to run some code only when a resource is created, and then store the results of that in the state file so that this value is maintained across deployments of the resource. Because we want our random number to be created once, and then remain stable for subsequent updates, we cannot simply use a random number generator in our program; we need dynamic providers. The result is a provider similar to the one provided in `@pulumi/random`, just specific to our program and language.

Implementing this example requires that we have a provider and resource type:

{{< langchoose >}}

```javascript
let pulumi = require("@pulumi/pulumi");
let crypto = require("crypto");

let randomprovider = {
    async create(inputs) {
        return { id: crypto.randomBytes(16).toString('hex'), outs: {}};
    },
}

class Random extends pulumi.dynamic.Resource {
    constructor(name, opts) {
        super(randomprovider, name, {}, opts);
    }
}

exports.Random = Random;
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as crypto from "crypto";

const randomprovider: pulumi.dynamic.ResourceProvider = {
    async create(inputs) {
        return { id: crypto.randomBytes(16).toString('hex'), outs: {}};
    },
}

export class Random extends pulumi.dynamic.Resource {
    constructor(name: string, opts?: pulumi.CustomResourceOptions) {
        super(randomprovider, name, {}, opts);
    }
}
```

```python
from pulumi import ResourceOptions
from pulumi.dynamic import Resource, ResourceProvider, CreateResult
from typing import Optional
import binascii
import os

class RandomProvider(ResourceProvider):
    def create(self, inputs):
        return CreateResult(id_=binascii.b2a_hex(os.urandom(16)), outs={})

class Random(Resource):
    def __init__(self, name: str, opts: Optional[ResourceOptions] = None):
         super().__init__(RandomProvider(), name, {}, opts)
```

```go
// Dynamic Providers are currently not supported in Go.
```

Now, with this, we can construct new `Random` resource instances, and Pulumi will drive the right calls at the right time.

###### Example: GitHub Labels REST API

This example highlights making REST API calls to some backing provider---the GitHub API in this case---to perform CRUD operations. Because the resource provider method implementations will be serialized and used in a different process, we keep all the work to initialize the REST client and make calls to it local to each function.

{{< langchoose csharp >}}

```javascript
let pulumi = require("@pulumi/pulumi");
let Octokit = require("@octokit/rest");

// Set this value before creating an instance to configure the authentication token to use for deployments
let auth = "token invalid";
exports.setAuth = function(token) { auth = token; }

const githubLabelProvider = {
    async create(inputs) {
        const ocktokit = new Ocktokit({auth});
        const label = await ocktokit.issues.createLabel(inputs);
        return { id: label.data.id.toString(), outs: label.data };
    },
    async update(id, olds, news) {
        const ocktokit = new Ocktokit({auth});
        const label = await ocktokit.issues.updateLabel({ ...news, current_name: olds.name });
        return { outs: label.data };
    },
    async delete(id, props) {
        const ocktokit = new Ocktokit({auth});
        await ocktokit.issues.deleteLabel(props);
    }
}

class Label extends pulumi.dynamic.Resource {
    constructor(name, args, opts) {
        super(githubLabelProvider, name, args, opts);
    }
}

exports.Label = Label;
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as Ocktokit from "@octokit/rest";

// Set this value before creating an instance to configure the authentication token to use for deployments
let auth = "token invalid";
export function setAuth(token: string) { auth = token; }

export interface LabelResourceInputs {
    owner: pulumi.Input<string>;
    repo: pulumi.Input<string>;
    name: pulumi.Input<string>;
    color: pulumi.Input<string>;
    description?: pulumi.Input<string>;
}

interface LabelInputs {
    owner: string;
    repo: string;
    name: string;
    color: string;
    description?: string;
}

const githubLabelProvider: pulumi.dynamic.ResourceProvider = {
    async create(inputs: LabelInputs) {
        const ocktokit = new Ocktokit({auth});
        const label = await ocktokit.issues.createLabel(inputs);
        return { id: label.data.id.toString(), outs: label.data };
    },
    async update(id, olds: LabelInputs, news: LabelInputs) {
        const ocktokit = new Ocktokit({auth});
        const label = await ocktokit.issues.updateLabel({ ...news, current_name: olds.name });
        return { outs: label.data };
    },
    async delete(id, props: LabelInputs) {
        const ocktokit = new Ocktokit({auth});
        await ocktokit.issues.deleteLabel(props);
    }
}

export class Label extends pulumi.dynamic.Resource {
    constructor(name: string, args: LabelResourceInputs, opts?: pulumi.CustomResourceOptions) {
        super(githubLabelProvider, name, args, opts);
    }
}
```

```python
from pulumi import ComponentResource, export, Input, Output
from pulumi.dynamic import Resource, ResourceProvider, CreateResult, UpdateResult
from typing import Optional
from github import Github, GithubObject

auth = "<auth token>"
g = Github(auth)

class GithubLabelArgs(object):
    owner: Input[str]
    repo: Input[str]
    name: Input[str]
    color: Input[str]
    description: Optional[Input[str]]
    def __init__(self, owner, repo, name, color, description=None):
        self.owner = owner
        self.repo = repo
        self.name = name
        self.color = color
        self.description = description

class GithubLabelProvider(ResourceProvider):
    def create(self, props):
        l = g.get_user(props["owner"]).get_repo(props["repo"]).create_label(
            name=props["name"],
            color=props["color"],
            description=props.get("description", GithubObject.NotSet))
        return CreateResult(l.name, {**props, **l.raw_data})
    def update(self, id, _olds, props):
        l = g.get_user(props["owner"]).get_repo(props["repo"]).get_label(id)
        l.edit(name=props["name"],
               color=props["color"],
               description=props.get("description", GithubObject.NotSet))
        return UpdateResult({**props, **l.raw_data})
    def delete(self, id, props):
        l = g.get_user(props["owner"]).get_repo(props["repo"]).get_label(id)
        l.delete()

class GithubLabel(Resource):
    name: Output[str]
    color: Output[str]
    url: Output[str]
    description: Output[str]
    def __init__(self, name, args: GithubLabelArgs, opts = None):
        full_args = {'url':None, 'description':None, 'name':None, 'color':None, **vars(args)}
        super().__init__(GithubLabelProvider(), name, full_args, opts)

label = GithubLabel("foo", GithubLabelArgs("lukehoban", "todo", "mylabel", "d94f0b"))

export("label_color", label.color)
export("label_url", label.url)
```

```go
// Dynamic Providers are not currently supported in Go.
```

```csharp
// Dynamic Providers are currently not supported in .NET.
```

#### Additional Examples

* [Enable Azure Storage’s Static Websites Feature](https://github.com/pulumi/examples/tree/master/azure-ts-static-website)
    * The Azure resource provider does not support enabling the static website feature for a storage account. However, there is a REST API that can be called to enable the feature, so we can easily call the API from within the dynamic provider.
* [Add a Custom Domain to an Azure CDN endpoint](https://github.com/pulumi/examples/tree/master/azure-ts-dynamicresource)
    * Similar to the previous example, this is another example of a shortcoming of the regular Azure resource provider available in Pulumi. However, due to the availability of a REST API, we can easily add a custom domain to an Azure CDN resource using a dynamic provider.
* [Dynamic Providers as Provisioners](https://github.com/pulumi/examples/tree/master/aws-ts-ec2-provisioners)
    * Provisioning a VM after it is created is a common problem. Developers have the option to run user-supplied scripts while creating the VM itself. For example, the AWS EC2 resource has a userData parameter, that allows you to specify an inline script, which EC2 will run at instance startup. However, this example of dynamic providers as provisioners allows you to copy/execute scripts on the target instance without replacing the instance itself.

### Runtime Functions

The Pulumi SDK library also offers a number of helper functions.

* [Current Project or Stack](#current-project-stack): get information about the current deployment
* [Logging](#logging): for diagnostics, warnings, or errors pertaining to the deployment
* [Serializing Lambdas](#runtime): for turning JavaScript callbacks into data which can be used as application code

#### Getting the Current Project or Stack {#current-project-stack}

The {{< pulumi-getproject >}} and {{< pulumi-getstack >}} functions give you the currently deploying project and stack, respectively. This can be useful for naming or tagging resources.

{{< langchoose csharp >}}

```javascript
let project = pulumi.getProject();
let stack = pulumi.getStack();
```

```typescript
let project = pulumi.getProject();
let stack = pulumi.getStack();
```

```python
project = pulumi.get_project()
stack = pulumi.get_stack()
```

```go
project := ctx.Project()
stack := ctx.Stack()
```

```csharp
var project = Deployment.Instance.ProjectName
var stack = Deployment.Instance.StackName
```

#### Logging

The {{< pulumi-log >}} collection of functions allows you to log diagnostics, warnings, or errors with the Pulumi engine. These will be displayed alongside all other Pulumi output in the CLI and in the Pulumi Console. They will also be logged and kept for historical purposes if you ever want to use them to audit or diagnose what has transpired.

{{< langchoose csharp >}}

```javascript
pulumi.log.info("message")
pulumi.log.info("message", resource)
pulumi.log.debug("hidden by default")
pulumi.log.warn("warning")
pulumi.log.error("fatal error")
```

```typescript
pulumi.log.info("message")
pulumi.log.info("message", resource)
pulumi.log.debug("hidden by default")
pulumi.log.warn("warning")
pulumi.log.error("fatal error")
```

```python
log.info("message")
log.info("message", resource)
log.debug("hidden by default")
log.warn("warning")
log.error("fatal error")
```

```go
// Optional arguments for logging.
args := &pulumi.LogArgs{
    Resource: resource,
    StreamID: 0,
    Ephemeral: false,
}

ctx.Log.Info("message", nil)
ctx.Log.Info("message", args)
ctx.Log.Debug("hidden by default", nil)
ctx.Log.Warn("warning", nil)
ctx.Log.Error("fatal error", nil)
```

```csharp
Pulumi.Log.Info("message");
Pulumi.Log.Info("message", resource);
Pulumi.Log.Debug("hidden by default");
Pulumi.Log.Warn("warning");
Pulumi.Log.Error("fatal error");

```

#### Serializing Lambdas <span class="badge">NODE.JS ONLY</span> {#runtime}

You can create libraries and components that allow the caller to pass in JavaScript callbacks to invoke at runtime. For example, you can create an AWS Lambda function or an Azure Function by providing a JavaScript callback to be used as its implementation.

{{< langchoose csharp >}}

```javascript
let bucket = new aws.s3.Bucket("mybucket");
bucket.onObjectCreated("onObject", async (ev) => {
    // This is the code that will be run when the Lambda is invoked (any time an object is added to the bucket).
    console.log(JSON.stringify(ev));
});
```

```typescript
let bucket = new aws.s3.Bucket("mybucket");
bucket.onObjectCreated("onObject", async (ev: aws.s3.BucketEvent) => {
    // This is the code that will be run when the Lambda is invoked (any time an object is added to the bucket).
    console.log(JSON.stringify(ev));
});
```

```python
# Runtime code provided via callbacks are currently not supported in Python.
#
# See https://github.com/pulumi/pulumi/issues/1535.
```

```go
// Runtime code provided via callbacks are currently not supported in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
// Runtime code provided via callbacks are currently not supported in .NET.
//
// See https://github.com/pulumi/pulumi/issues/3406.
```

Libraries which use JavaScript callbacks as inputs to be provided as source text to resource construction---like the Lambda that is created by the `onObjectCreated` function in the previous example---are built on top of the [pulumi.runtime.serializeFunction]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi/runtime#serializeFunction" >}}) API, which takes a JavaScript `Function` object as input, and returns a `Promise` containing the serialized form of that function.

When serializing a function to text, the following steps are taken:

1. Any captured variables referenced by the function are evaluated when the function is serialized.
2. The values of those variables are serialized.
3. When the values are objects, all properties and prototype chains are serialized.  When the values are functions, those functions are serialized by following these same steps.

See [Serializing Functions]({{< relref "/docs/tutorials/aws/serializing-functions" >}}) for more details.
