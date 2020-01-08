---
title: "Programming Model"
meta_desc: An in depth overview of the the Pulumi Programming Model and common terms associated with the platform.
menu:
  intro:
    parent: concepts
    weight: 1

aliases: ["/docs/reference/programming-model/"]
---

## Overview {#overview}

In Pulumi, [resources](#resources) are defined by allocating resource objects in a program.  For example, your program would contain a statement such as `new aws.ec2.Instance(...)` in order to create a new AWS EC2 instance.  The first argument passed to the resource constructor is its `name`, which must be unique within the Pulumi program.

Dependencies between resources are expressed in Pulumi by using the [output properties](#outputs) of one resource in the construction of another resource.  For example, this definition of an EC2 instance creates a dependency on a `SecurityGroup`:

{{< langchoose csharp >}}

```javascript
let group = new aws.ec2.SecurityGroup(...);
let server = new aws.ec2.Instance("webserver-www", {
    ...
    securityGroups: [ group.name ], // reference the security group resource above
});
```

```typescript
let group = new aws.ec2.SecurityGroup(...);
let server = new aws.ec2.Instance("webserver-www", {
    ...
    securityGroups: [ group.name ], // reference the security group resource above
});
```

```python
group = aws.ec2.SecurityGroup(...)
server = aws.ec2.Instance('webserver-www',
    ...
    security_groups=[group.name]) # reference the security group resource above
```

```go
group, err := ec2.NewSecurityGroup(ctx, "webserver-securitygroup", &ec2.SecurityGroupArgs{
    ...
})
if err != nil {
    return err
}
server, err := ec2.NewInstance(ctx, "webserver-www", &ec2.InstanceArgs{
    ...
    SecurityGroups: []interface{}{group}, // reference the security group resource above
})
if err != nil {
    return err
}
```

```csharp
using Pulumi;
using Pulumi.Aws.Ec2;

// Inside call to Deployment.Run
var group = new SecurityGroup(...);
var server = new Instance("webserver-www", new InstanceArgs
{
    //...
    SecurityGroups = { group.Name }, // reference the security group resource above
});
```

To publish values that you wish to access outside your application, create a [stack output](#stack-outputs) via module exports.

In Pulumi, you can group multiple resources in a [component](#components). A component is a logical container for physical cloud resources and affects how resources are grouped in the CLI and the pulumi.com console.

## Programs {#programs}

Pulumi programs are authored in general-purpose programming languages such as [JavaScript]({{< relref "/docs/intro/languages/javascript" >}}) or [Python]({{< relref "/docs/intro/languages/python" >}}) or a .NET Language (in preview). You can use any packages supported by the language's package manager, as well as [Pulumi packages]({{< relref "/docs/reference/pkg" >}}).

When `pulumi up` is run, your Pulumi program is run and the Pulumi CLI determines the desired state of application resources. A Pulumi program can reference artifacts that have already been published (such as S3 objects or prebuilt Docker images) or it can define application resources itself so that everything is versioned together. For example, if your program uses `cloud.Service` with a `build` step, or defines a Lambda for an S3 trigger, you're defining application code that is implicitly deployed during the `pulumi up`.

A Pulumi program is contained within a [project]({{< relref "project.md" >}}). In JavaScript, the `main` property of `package.json` defines the entry point for the Pulumi program.

## Pulumi SDK {#pulumipulumi}

The [@pulumi/pulumi] package is the core library for working with the Pulumi engine. This package defines the following kinds of resources which can be deployed with Pulumi:

- Resources ([pulumi.Resource])
- External cloud platform resources ([pulumi.CustomResource])
- Components defined entirely in JavaScript ([pulumi.ComponentResource])

Dependencies between resources are encoded with [pulumi.Output](#outputs).

This package also provides the following helpers:

- [pulumi.getStack] for getting information about the current stack
- [pulumi.log] for logging deployment information
- [pulumi.runtime.serializeFunction] for turning JavaScript callbacks into data which can be [used as application code](#runtime)

## Resources {#resources}

A resource is created with the following:

{{< langchoose csharp >}}

```javascript
let res = new Resource(name, args, options)
```

```typescript
let res = new Resource(name, args, options)
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

All resources have a [`name`](#names), which must be unique in the Pulumi program.

The `args` provided to a resource determine what inputs will be used to initialize the resource.  These can be either raw values or [outputs from other resources](#outputs).

### Resource options {#resourceoptions}

All resource constructors also accept an `options` argument which can provide the following additional resource options controlling how the resource will be managed by Pulumi.

#### `additionalSecretOutputs`

Provides a list of output properties which should be treated as secrets. This value augments any values that Pulumi detects itself, based on what secret inputs to the resource has. This is typically used to express that for a specific instance of a resource, some of its output properties should be treated as secrets (when they would not normally be).  Currently only top-level resource properties can be passed to `additionalSecretOutputs`, so if there is sensitive data nested inside output properties, the entire top-level output property must be marked as secret.

{{< langchoose csharp >}}

```javascript
// Ensure the password generated for the database is marked as a secret
let db = new Database("new-name-for-db", {}, { additionalSecretOutputs: ["password"] });
```

```typescript
// Ensure the password generated for the database is marked as a secret
let db = new Database("new-name-for-db", {}, { additionalSecretOutputs: ["password"] });
```

```python
# Ensure the password generated for the database is marked as a secret
db = Database("db", opts=ResourceOptions(additional_secret_outputs=["password"]))
```

```go
// AdditionalSecretOutputs is not yet supported in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
// Ensure the password generated for the database is marked as a secret
var db = new Database("new-name-for-db", new DatabaseArgs(), new CustomResourceOptions { AdditionalSecretOutputs = { "password" } });
```

##### `aliases`

Provides a list of aliases for a resource or component. When making a breaking change to the name or type of a resource or component, you can add the old name to the list of `aliases` for a resource to ensure that existing resources will be migrated to the new name instead of being deleted and replaced with the new named resource.

For example, a resource can be aliased to a full previous [resource URN](#urns):

`aliases: ["urn:pulumi:stackname::projectname::aws:s3/bucket:Bucket::app-function"]`

Or it can be aliased to a relative change to the resource's name, parent, and/or type:

`aliases: [{ name: "otherchild", parent: this }]`

{{< langchoose csharp >}}

```javascript
// Provide an alias to ensure migration of the existing resource.
let db = new Database("new-name-for-db", {}, { aliases: [{name: "old-name-for-db"}] });
```

```typescript
// Provide an alias to ensure migration of the existing resource.
let db = new Database("new-name-for-db", {}, { aliases: [{name: "old-name-for-db"}] });
```

```python
# Provide an alias to ensure migration of the existing resource.
db = Database("db", opts=ResourceOptions(aliases=[Alias(name="old-name-for-db")]))
```

```go
// Aliases is not yet supported in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
// Provide an alias to ensure migration of the existing resource.
var db = new Database("new-name-for-db", new DatabaseArgs(), new ResourceOptions { Aliases = { new Alias { Name = "old-name-for-db"} } });
```

##### `customTimeouts`

Provides a set of custom timeouts for `create`, `update`, and `delete` operations on a resource. These timeouts can be specified as a string like "5m", "40s", or "1d" (5 minutes, 40 seconds, or 1 day, respectively). For example, `customTimeouts: { create: "1m" }`.

{{< langchoose csharp >}}

```javascript
// Wait up to 30m for the database to be created
let db = new Database("db", {}, { customTimeouts: { create: "30m" } });
```

```typescript
// Wait up to 30m for the database to be created
let db = new Database("db", {}, { customTimeouts: { create: "30m" } });
```

```python
# Wait up to 30m for the database to be created
db = Database("db", opts=ResourceOptions(custom_timeouts=CustomTimeouts(create="30m")))
```

```go
// Wait up to 30m for the database to be created
db, _ := Database(ctx, "db", &DatabaseArgs{}, pulumi.ResourceOpt{CustomTimeouts: &CustomTimeouts{Create: "30m"}});
```

```csharp
// Wait up to 30m for the database to be created
var db = new Database("db", new DatabaseArgs(), new ResourceOptions { CustomTimeouts = new CustomTimeouts { Create = TimeSpan.FromMinutes(30) } });
```

##### `deleteBeforeReplace`

Set this option to `true` to specify that replacements of the resource will delete the existing resource before creating its replacement.  This will lead to downtime during the replacement, but may be necessary for some resources that manage scarce resources behind the scenes.  The default is `false`.

{{< langchoose csharp >}}

```javascript
// The resource will be deleted before it's replacement is created
let db = new Database("db", {}, { deleteBeforeReplace: true});
```

```typescript
// The resource will be deleted before it's replacement is created
let db = new Database("db", {}, { deleteBeforeReplace: true});
```

```python
# The resource will be deleted before it's replacement is created
db = Database("db", opts=ResourceOptions(delete_before_replace=True))
```

```go
// The resource will be deleted before it's replacement is created
db, _ := Database(ctx, "db", &DatabaseArgs{}, pulumi.ResourceOpt{DeleteBeforeReplace: true});
```

```csharp
// The resource will be deleted before it's replacement is created
var db = new Database("db", new DatabaseArgs(), new CustomResourceOptions { DeleteBeforeReplace = true });
```

##### `dependsOn`

Provides a list of explicit resource dependencies to add to the resource. Every resource referenced either directly or indirectly by an `Output` that is passed in to the resource constructor will implicitly be included, so this additional information is only needed when the dependency is on something that is not already an input to the resource. The default is `[]`.

{{< langchoose csharp >}}

```javascript
let res1 = new MyResource("res1", {});
let res2 = new MyResource("res2", {}, { dependsOn: [res1] });
```

```typescript
let res1 = new MyResource("res1", {});
let res2 = new MyResource("res2", {}, { dependsOn: [res1] });
```

```python
res1 = MyResource("res1");
res2 = MyResource("res2", opts=ResourceOptions(depends_on=[res1]));
```

```go
res1, _ := MyResource(ctx, "res1");
res2, _ := MyResource(ctx, "res2", pulumi.ResourceOpt{DependsOn: []Resource{res1}});
```

```csharp
var res1 = new MyResource("res1", new MyResourceArgs());
var res2 = new MyResource("res2", new MyResourceArgs(), new ResourceOptions { DependsOn = { res1 } });
```

##### `ignoreChanges`

Provides a list of properties which will be ignored as part of updates. The value of the property will be used for newly created resources, but will not be used as part of updates. You would use this option to avoid changes in properties leading to diffs or to change defaults for a property without forcing all existing deployed stacks to update or replace the affected resource.

{{< langchoose csharp >}}

```javascript
// Changes to the value of `prop` will not lead to updates/replacements
let res = new MyResource("res", { prop: "new-value" }, { ignoreChanges: ["prop"] });
```

```typescript
// Changes to the value of `prop` will not lead to updates/replacements
let res = new MyResource("res", { prop: "new-value" }, { ignoreChanges: ["prop"] });
```

```python
# Changes to the value of `prop` will not lead to updates/replacements
res = MyResource("res", prop="new-value", opts=ResourceOptions(ignore_changes=["prop"]))
```

```go
// IgnoreChanges is not yet supported in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
// Changes to the value of `prop` will not lead to updates/replacements
var res = new MyResource("res", new MyResourceArgs { prop = "new-value" }, new ResourceOptions { IgnoreChanges = { "prop" } });
```

##### `import`

The ID of an existing resource to import for Pulumi to manage. When set, Pulumi will read the current state of the resource with the given ID from the backing provider &ndash; AWS, Azure, GCP, or Kubernetes for example. The inputs to the resource's constructor must not differ from this state or the import will fail.

Either make sure the import id exactly matches the id after importing, or remove the property after importing. Failing to do so will cause the resource to be continuously imported for "import-replacement", which leads to unnecessary deletes & recreates and is problematic for protected resources. When keeping the imports, you can for example use (with GCP Firewalls) `projects/<myproject>/global/firewalls/<name>` as id, instead of just `<name>`.

{{< langchoose csharp >}}

```javascript
// The input properties must match the values for the exsiting resource `my-database-id`
let db = new Database("db", { /*...*/ }, { import: "my-database-id" });
```

```typescript
// The input properties must match the values for the exsiting resource `my-database-id`
let db = new Database("db", { /*...*/ }, { import: "my-database-id" });
```

```python
# The input properties must match the values for the exsiting resource `my-database-id`
db = Database("db", opts=ResourceOptions(import_="my-database-id"))
```

```go
// The input properties must match the values for the exsiting resource `my-database-id`
db, _ := Database(ctx, "db", &DatabaseArgs{ /*...*/ }, pulumi.ResourceOpt{Import: "my-database-id"});
```

```csharp
// The input properties must match the values for the exsiting resource `my-database-id`
var db = new Database("db", new DatabaseArgs { /*...*/ }, new CustomResourceOptions { ImportId = "my-database-id" });
```

##### `parent`

A parent for the resource. See [Components](#components).  The default is to parent to the implicitly-created `Stack` resource that is a root resource for all Pulumi stacks.

{{< langchoose csharp >}}

```javascript
let parent = new MyResource("parent", {});
let child = new MyResource("child", {}, { parent: parent });
```

```typescript
let parent = new MyResource("parent", {});
let child = new MyResource("child", {}, { parent: parent });
```

```python
parent = MyResource("parent");
child = MyResource("child", opts=ResourceOptions(parent=parent));
```

```go
parent, _ := MyResource(ctx, "parent");
child, _ := MyResource(ctx, "child", pulumi.ResourceOpt{Parent: parent});
```

```csharp
var parent = new MyResource("parent", new MyResourceArgs());
var child = new MyResource("child", new MyResourceArgs(), new ResourceOptions { Parent = parent });
```

##### `protect`

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
db, _ := Database(ctx, "db", &DatabaseArgs{}, pulumi.ResourceOpt{Protect: true});
```

```csharp
var db = new Database("db", new DatabaseArgs(), new ResourceOptions { Protect = true });
```

##### `provider`

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
provider, _ := aws.Provider(ctx, "provider", { region: "us-west-2" });
vpc, _ := ec2.Vpc(ctx, "vpc", &VpcArgs{}, pulumi.ResourceOpt{Provider: provider});
```

```csharp
var provider = new Aws.Provider("provider", new Aws.ProviderArgs { Region = "us-west-2" });
var vpc = new Aws.Ec2.Vpc("vpc", new Aws.Ec2.VpcArgs(), new ResourceOptions { Provider = provider });
```

##### `transformations`

A list of transformations to apply to the resource and all of its children. This can be used to override or modify the inputs to child resources of a component, for example to add other resource options (like `ignoreChanges` or `protect`) or to modify an input property (like adding to `tags` or changing a property which is not configurable via the component directly).  Transformations can also be applied to all resources in a stack using `pulumi.runtime.registerStackTransformation`.  Transformations are passed the resource type, name, input properties resource options and the resource instance itself.  They can optionally return a new set of resource input properties and resource options which will be used to construct the resource.

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
// Transformations is not yet supported in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
var vpc = new MyVpcComponent("vpc", new ResourceOptions
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
                        new ResourceOptions { IgnoreChanges =  { "tags" } }),
                };
            }

            return null;
        }
    },
});

### Resource names {#names}

Every resource managed by Pulumi has a **logical name** that you specify as an argument to its constructor. For instance, the logical name of this IAM role is `my-role`:

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
role, _ := iam.Role(ctx, "my-role", &iam.RoleArgs{}, pulumi.ResourceOpt{})
```

```csharp
var role = new Aws.Iam.Role("my-role");
```

This logical name is used by Pulumi to track the identity of a resource across multiple deployments of the same program and is how Pulumi knows to choose between creating new resources versus updating existing ones.

The name specified during resource creation is used in two key ways:

1. As a default prefix for the resource's **physical name** in the target cloud provider.
2. To construct the Universal Resource Name (URN) used by Pulumi to track the resource across updates.

Note that the variable name a resource object is assigned to isn't used in any way for either logical or physical naming.

#### Auto-naming {#autonaming}

A resource's logical and physical names may not match. In fact, most physical resource names in Pulumi are "auto-named." As a result, even if you give your IAM role has a logical name of `my-role`, as shown above, the physical name will typically look something like `my-role-d7c2fa0`.

This random suffix is added for two reasons:

- It ensures that two stacks for the same project can be deployed without risk of collisions. This helps you to multi-instance your project more easily, whether that's for many development or testing instances, or even scaling to new regions. Without auto-naming, you would need to manually distinguish these resources with different physical names.

- It allows Pulumi to do zero-downtime resource updates. Certain updates require replacing resources, rather than updating them in place. This is because Pulumi can create replacements first, then update existing references to them, and finally delete the old resources. If it weren't for auto-naming, Pulumi would need to do things in a very different order: namely, it would need to delete resources first, and create new instances afterwards, which is far more impactful and leads to downtime.

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
role, _ := iam.Role(ctx, "my-role", &iam.RoleArgs{
    Name: "my-role-001",
}, pulumi.ResourceOpt{})
```

```csharp
var role = new Aws.Iam.Role("my-role", new Aws.Iam.RoleArgs
{
    Name = "my-role-001",
});
```

> If `name` doesn't work, please consult the documentation for the specific resource you are creating. Some resources use a different property to override the auto-naming. For instance, the `aws.s3.Bucket` type uses the property `bucket` instead of `name`. Other resources, like `aws.kms.Key`, don't even have physical names and instead use other auto-generated IDs to uniquely identify them.

Notice above that the physical and logical names do not need to match. You may even elect to construct the name using the name of your project and/or stack instead. This is often necessary if you are going to create multiple stacks for your project:

{{< langchoose csharp >}}

```javascript
let role = new aws.iam.Role("my-role", {
    name: "my-role-" + pulumi.getProject() + "-" + pulumi.getStack(),
});
```

```typescript
let role = new aws.iam.Role("my-role", {
    name: `my-role-${pulumi.getProject()}-${pulumi.getStack()}`,
});
```

```python
role = iam.Role('my-role', {
    name='my-role-%s-%s'.format(pulumi.get_project(), pulumi.get_stack())
})
```

```go
role, _ := iam.Role(ctx, "my-role", &iam.RoleArgs{
    Name: "my-role-"+pulumi.GetProject()+"-"+pulumi.GetStack(),
}, pulumi.ResourceOpt{})
```

```csharp
var role = new Aws.Iam.Role("my-role", new Aws.Iam.RoleArgs
{
    Name = "my-role-" + Deployment.Instance.ProjectName + "-" + Deployment.Instance.StackName,
});
```

Overriding auto-naming typically opens up your project to naming collisions. As a result, for resources that may need to be replaced, you will also need to specify `deleteBeforeReplace: true` in the resources's `ResourceOptions`. This ensures old resources are deleted before new ones are recreated.

#### URNs {#urns}

The Unique Resource Name (URN) of a resource is automatically constructed from the name provided by the resource, the type of the resource, and the types of all the parent component resources. It also includes information about the project and stack. For example:

```
urn:pulumi:thumbnailer-twitch::video-thumbnailer::cloud:bucket:Bucket$cloud:function:Function::onNewThumbnail
urn:pulumi:    <stackname>   ::  <projectname>  ::    <parenttype>   $     <resourcetype>    ::<resourcename>
```

> Note: It is likely that the format of the URN will be changed in the future to be simpler and more flexible.

Since the URN serves as the unique identity of a resource within a stack, it must be unique for each resource created by a single Pulumi program.  In particular, this requires that the resource name must be unique among resources of the same type with the same type of parent component.

Any change to the URN of a resource will cause the old and new resources to be treated as unrelated---the new one will be created (since it was not in the prior state) and the old one will be deleted (since it is not in the new desired state). This includes changing the `name` used to construct the resource or changing the parent of a resource.  Both of these operations will lead to a different URN, and a `create` and a `delete` operation instead of an `update` or `replace` operation of the resource.  As a result, changes to names must be made with care.

Resources constructed as children of a [component](#components) should make sure that their names will be unique across multiple instances of the component.  In general, the name of the component instance itself (the `name` parameter passed in to the component constructor) shoud be used as part of the name of the child resources.

#### Resource get {#resource-get}

A `get` method is available on any resource, which reads in the current value of an existing resource.  The shape it returns corresponds to the type of the resource.

## Outputs and Inputs {#outputs}

Outputs are a key part of how Pulumi tracks dependencies between resources.  Because the values of Outputs are not available until resources are created, these are represented using the special [`Output`][pulumi.Output] type, which internally represents two things:

1. An eventually available value of the output
2. The dependency on the source(s) of the output value

In fact, `Output`s are similar to promises/futures that you may be familiar with from other programming models. Additionally, they carry along dependency information.

The output properties of all resource objects in Pulumi have type [`Output`][pulumi.Output].

Resource inputs have type [`Input`][pulumi.Input], which accepts either a raw value, a `Promise`, or an output from another resource. This allows dependencies to be inferred, including ensuring that resources are not created or updated until all their dependencies are available and up to date.

### Apply {#apply}

To transform an output into a new value, use the [`apply` method]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#OutputInstance-apply" >}}). For example, use the following to create an HTTPS URL from the DNS name of a virtual machine:

{{< langchoose csharp >}}

```javascript
let url = virtualmachine.dnsName.apply(dnsName => "https://" + dnsName)
```

```typescript
let url = virtualmachine.dnsName.apply(dnsName => "https://" + dnsName)
```

```python
url = virtual_machine.dns_name.apply(
    lambda dns_name: "https://" + dns_name
)
```

```go
url := virtualmachine.DnsName().Apply(func(dnsName string) (interface{}, error) {
    return "https://" + dnsName, nil
})
```

```csharp
var url = virtualmachine.DnsName.Apply(dnsName => "https://" + dnsName);
```

The `apply` method accepts a callback which will be passed the value of the `Output` when it is available, and which returns the new value.  The result of the call to `apply` is a new `Output` whose value is the value returned from the callback, and which includes the dependencies of the original `Output`.  If the callback itself returns an `Output`, the dependencies of that output are unioned into the dependencies of the returned `Output`.

> _Note_: Several common types of transformations can be done more conveniently.  See [Accessing properties of an Output](#lifting) for how to access Output value properties simply.   Also, `Output` itself cannot be used directly in string concatenation as it is not itself the value of the output.  See [Working with Outputs and strings](#outputs-and-strings) for examples of how to use the two together.  In cases where these convenience forms are not sufficient, `.apply` is the most general way to transform one `Output` into another.

#### Accessing properties of an Output {#lifting}

It is common to only need access to some property of the value of an `Output` in order to pass in that property to another `Resource`.  For example, when using ACM certificates, one might write:

{{< langchoose csharp >}}

```javascript
let certCertificate = new aws.acm.Certificate("cert", {
  domainName: "example.com",
  validationMethod: "DNS",
});
let certValidation = new aws.route53.Record("cert_validation", {
  // Need to pass along a deep subproperty of this Output
  records: [certCertificate.domainValidationOptions.apply(domainValidationOptions => domainValidationOptions[0].resourceRecordValue)],
  ...
```

```typescript
let certCertificate = new aws.acm.Certificate("cert", {
  domainName: "example.com",
  validationMethod: "DNS",
});
let certValidation = new aws.route53.Record("cert_validation", {
  // Need to pass along a deep subproperty of this Output
  records: [certCertificate.domainValidationOptions.apply(domainValidationOptions => domainValidationOptions[0].resourceRecordValue)],
  ...
```

```python
certificate = aws.acm.Certificate("cert",
  domain_name="example.com",
  validation_method="DNS",

record = aws.route53.Record("validation",
  # Need to pass along a deep subproperty of this Output
  records=[certificate.domain_validation_options.apply(
      lambda domain_validation_options: domain_validation_options[0].resource_record_value
  )],
  ...
```

```go
// Helpers for accessing properties are not yet available in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
// Helpers for accessing properties are not yet available in .NET.
```

To make this kind of property and array element access more simple, an `Output` _lifts_ the properties of the value that is wrapped, allowing you to access them directly off of the `Output` itself.  This allows the previous example to be written more simply as:

{{< langchoose csharp >}}

```javascript
let certCertificate = new aws.acm.Certificate("cert", {
  domainName: "example.com",
  validationMethod: "DNS",
});
let certValidation = new aws.route53.Record("cert_validation", {
  records: [certCertificate.domainValidationOptions[0].resourceRecordValue],
  ...
```

```typescript
let certCertificate = new aws.acm.Certificate("cert", {
  domainName: "example.com",
  validationMethod: "DNS",
});
let certValidation = new aws.route53.Record("cert_validation", {
  records: [certCertificate.domainValidationOptions[0].resourceRecordValue],
  ...
```

```python
certificate = aws.acm.Certificate("cert",
  domain_name="example.com",
  validation_method="DNS",

record = aws.route53.Record("validation",
  records=[certificate.domain_validation_options[0].resource_record_value],
  ...
```

```go
// Helpers for accessing properties are not yet available in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
// Helpers for accessing properties are not yet available in .NET
```

This helps the clarity of the final code, while not losing any important dependency information that is needed for properly creating and maintaining the stack.

##### Optional chaining off of an Output

In JavaScript and TypeScript, a 'lifted' property access on an `Output<T>` that wraps `undefined` will produce another `Output<T>` with the `undefined` value instead of throwing or producing a 'faulted' `Output<T>`.  In this manner 'lifted' property accesses behave like the [`?.` (optional chaining operator)](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html#optional-chaining) in JavaScript and TypeScript. This makes it much easier to form a chain of property accesses on an `Output<T>`.

{{< langchoose nodeonly >}}

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

##### All {#all}

To combine multiple `Output`s into a transformed value, use [pulumi.all].  This allows a new value to be constructed from several inputs, such as concatenating outputs from two different resources together, or constructing a policy document using information from several other resources.

{{< langchoose csharp >}}

```javascript
let connectionString = pulumi.all([sqlServer.name, database.name])
                             .apply(([server, db]) => `Server=tcp:${server}.database.windows.net;initial catalog=${db}...`);
```

```typescript
let connectionString = pulumi.all([sqlServer.name, database.name])
                             .apply(([server, db]) => `Server=tcp:${server}.database.windows.net;initial catalog=${db}...`);
```

```python
from pulumi import Output

connection_string = Output.all(sql_server.name, database.name) \
    .apply(lambda args: f"Server=tcp:{args[0]}.database.windows.net;initial catalog={args[1]}...")
```

```go
// `all` is not yet available in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
// In .NET 'Output.Tuple' is used so that each unwrapped value will preserve their distinct type.
// 'Output.All' can be used when all input values have the same type (i.e. all are Output<string>)
var connectionString = Output.Tuple(sqlServer.name, database.name)
                             .Apply(t => `Server=tcp:${t.Item1}.database.windows.net;initial catalog=${t.Item2}...`);
```

##### Convert Input to Output {#frominput}

To turn an `Input` into an `Output`, use [pulumi.output].  This can be useful when you want to transform an input value that could either be a raw value or an `Output`:

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
// Helpers for converting Inputs to Outputs are not yet available in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
Output<string[]> Split(Input<string[]> input)
{
    var output = input.ToOutput()
    return output.Apply(v => v.Split(","));
}
```

##### Working with Outputs and strings {#outputs-and-strings}

It's very common to want to build a string out of the values contained in `Outputs`.  Common uses include either providing a custom [stack output](#stack-outputs), or providing a dynamically computed string as an [Input]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Input" >}}) to another Resource.  For example, say you had the following:

{{< langchoose csharp >}}

```javascript
const hostName = // get some Output
const port = // get some Output

// Would like to produce a string equivalent to: http://${hostname}:${port}/
const url = // ?
```

```typescript
const hostName: Output<string> = // get some Output
const port: Output<number> = // get some Output

// Would like to produce a string equivalent to: http://${hostname}:${port}/
const url: Output<string> = // ?
```

```python
hostName: Output[str] = # get some Output
port: Output[int] = # get some Output

# Would like to produce a string equivalent to: http://${hostname}:${port}/
url = # ?
```

```go
// Helpers for combining Outputs into strings are not yet available in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
Output<string> hostName = // get some Output
Output<int> port = // get some Output

// Would like to produce a string equivalent to: http://{hostname}:{port}/
var url = // ?
```

Using [.apply](#apply) and [.all](#all), this could be solved as shown previously like so:

```javascript
const url = pulumi.all([hostname, port]).apply(([hostname, port]) => `http://${hostname}:${port}/`);
```

```typescript
const url: Output<string> = pulumi.all([hostname, port]).apply(([hostname, port]) => `http://${hostname}:${port}/`);
```

```python
url = Output.all([hostname, port]).apply(lambda l: f"http://{l[0]}:{l[1]}/")
```

```go
// Helpers for combining Outputs into strings are not yet available in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
var url = pulumi.Tuple(hostname, port).Apply(t => `http://{t.Item1}:{t.Item2}/`);
```

However, this is quite verbose and unwieldy.  To make this easier, Pulumi exposes helpers like `concat` and `interpolate` to make this more convenient.  They can be used as follows:

```javascript
const url1 = pulumi.concat("http://", hostname, ":", port, "/");
const url2 = pulumi.interpolate `http://${hostname}:${port}/`;
```

```typescript
const url1: Output<string> = pulumi.concat("http://", hostname, ":", port, "/");
const url2: Output<string> = pulumi.interpolate `http://${hostname}:${port}/`;
```

```python
url = Output.concat("http://", hostname, ":", post, "/")
```

```go
// Helpers for combining Outputs into strings are not yet available in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
// In .NET 'Interpolate' is called 'Format'.
var url2 = Output.Format($"http://{hostname}:{port}/");
```

`concat` takes a list of arguments that can be `Inputs`, `Outputs`, `Promises`, and simple values, and creates an `Output` with all their underlying values concatenated together.  `interpolate`---which is JavaScript only---does the same, but allows you to use a JavaScript `template literal` if that is your preferred way of combining values into strings.

## Secrets {#secrets}

Pulumi records all resource inputs and outputs in a [state file]({{< relref "state.md" >}}). This may contain sensitive data, such as database passwords or service tokens. The CLI's `config set` command offers a `--secret` flag to encrypt configuration settings, which is where most sensitive data comes from. However, you may create such data at runtime. In both cases, you can prevent these secrets from appearing as plaintext in your state file by using programmatic functions described below. These use automatic per-stack encryption keys provided by the Pulumi Service by default, but you can use a provider of your own choosing.

> This topic concerns itself with the programming model for secrets. For a more complete overview, including
> how and when to use the CLI commands mentioned above, configuring your own secrets provider, and more, refer to
> [Configuration and Secrets]({{< relref "config#secrets" >}}).

### Programmatically Creating Secrets

There are two ways to programmatically create secret values:

{{< langchoose csharp >}}

<div class="language-prologue-javascript"></div>

- Using [`getSecret(key)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-getSecret" >}}) or [`requireSecret(key)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-requireSecret" >}}) when reading a value from config.
- Calling [`pulumi.secret(value)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#secret" >}}) to construct a secret from an existing value.

<div class="language-prologue-typescript"></div>

- Using [`getSecret(key)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-getSecret" >}}) or [`requireSecret(key)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-requireSecret" >}}) when reading a value from config.
- Calling [`pulumi.secret(value)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#secret" >}}) to construct a secret from an existing value.

<div class="language-prologue-python"></div>

- Using [`get_secret`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Config.get_secret" >}}) or [`require_secret`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Config.require_secret" >}}) when reading a value from config.
- Calling [`Output.secret`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Output.secret" >}} to construct a secret from an existing value.

<div class="language-prologue-go"></div>

Secrets are not yet available in Go. See <https://github.com/pulumi/pulumi/issues/2820>.

<div class="language-prologue-csharp"></div>

- Using `Config.GetSecret(key)` or `Config.RequireSecret(key)` when reading a value from config.
- Calling `Output.CreateSecret(value)` to construct a secret from an existing value.

To illustrate using these functions, this code creates an AWS Parameter Store parameter insecurely:

{{< langchoose csharp >}}

```javascript
const cfg = new pulumi.Config()
const param = new aws.ssm.Parameter("a-secret-param", {
    type: "SecureString",
    value: cfg.require("my-secret-value"),
});
```

```typescript
const cfg = new pulumi.Config()
const param = new aws.ssm.Parameter("a-secret-param", {
    type: "SecureString",
    value: cfg.require("my-secret-value"),
});
```

```python
cfg = pulumi.Config()
param = ssm.Parameter("a-secret-param",
    type="SecureString",
    value=cfg.require("my-secret-value"))
```

```go
// Secrets are not yet available in Go.
//
// See https://github.com/pulumi/pulumi/issues/2820
```

```csharp
var cfg = new Pulumi.Config()
var param = new Aws.Ssm.Parameter("a-secret-param", new Aws.Ssm.ParameterArgs
{
    type = "SecureString",
    value = cfg.Require("my-secret-value"),
});
```

As written, this program's state will include the plaintext value of the `my-secret-value` configuration variable in `a-secret-param`'s input properties.

To fix this, we can use one of the above methods, ensuring the resulting data is encrypted in the state file the same way it was in the configuration that we read it from:

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
// Secrets are not yet avaiaible in Go.
//
// See https://github.com/pulumi/pulumi/issues/2820
```

```csharp
var cfg = new Pulumi.Config()
var param = new Aws.Ssm.Parameter("a-secret-param", new Aws.Ssm.ParameterArgs
{
    type = "SecureString",
    value = cfg.RequireSecret("my-secret-value"),
});
```

After this change, the `Parameter` resource's `value` property will be encrypted in the state file.

> Pulumi tracks the transitive usage of secrets, so that your secret won't end up accidentally leaking into
> the state file. This includes automatically marking data generated from secret inputs itself as secret, as
> well as fully encrypting any resource properties that include secrets in them.

### How Secrets Relate to Outputs

Secrets have the same type `Output` as do other unencrypted resource outputs. The difference is that they are marked internally as needing encryption before persisting in the state file. When you combine an existing output that is marked as a secret using `apply` or `all`, the resulting output is also marked as a secret.

An `apply`'s callback is given the plaintext value of the underlying secret. Although Pulumi ensures that the value returned from an `apply` on a secret is also marked as secret, Pulumi cannot guarantee that the `apply` callback itself will not expose the secret value. For instance, by explicitly printing the value to the console or saving it to a file. Be careful that you do not pass this plaintext value to code that might intentionally or accidentally expose it.

> Unlike regular outputs, secrets cannot be captured by Pulumi closure serialization system for use in serverless code. Attempting to do so will lead to an exception. We do plan to support this once we can ensure that the values will be persisted securely. See [pulumi/pulumi#2718](https://github.com/pulumi/pulumi/issues/2718).

### Explicitly Marking Resource Outputs as Secrets

It is possible to mark resource outputs as containg secrets. In this case, Pulumi will automatically treat those outputs
as secrets and encrypt them in the state file and anywhere they flow to. To do so,
[use the "additional secret outputs" option, as described above]({{< relref "#additionalsecretoutputs" >}}).

## Stack outputs {#stack-outputs}

A [stack output]({{< relref "stack.md#outputs" >}}) is a value exported from a stack. A stack's outputs can be easily retrieved from the Pulumi CLI and are displayed on pulumi.com. To export values from a stack, use the following definition in the top-level of the entrypoint for your project:

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
ctx.Export("url", resource.Url())
```

```csharp
// The dictionary returned by the function passed to Deployment.Run will be used to provide all the exported values.
static Task Main() =>
    Deployment.Run(async () =>
    {
        return new Dictionary<string, object> { { "url", resource.Url } };
    });
```

From the CLI, you can then use `pulumi stack output url` to get the value and incorporate into other scripts or tools.

The right-hand side of a stack export can be a regular JavaScript value, an [Output](#outputs), or a `Promise`. The actual value will be resolved at the end of `pulumi up`.

Stack exports are JSON-serialized, though quotes are removed when exporting a string value. For example:

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
ctx.Export("x", "hello")
ctx.Export("o", map[string]interface{}{
    "num": 42,
})
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

If a stack contains any output values which are marked as secrets, their values will not be shown by default. Instead, they will be displayed as `[secret]` in the CLI.

You may pass `--show-secrets` to `pulumi stack output` to see the plaintext value.

## Stack References {#stack-references}

Stack references provide a way to access the [outputs](#stack-outputs) of one stack from another stack. To reference values from another stack, create an instance of the `StackReference` type using the name of the referenced stack as an input:

{{< langchoose csharp >}}

```javascript
const pulumi = require("@pulumi/pulumi");
const other = new pulumi.StackReference("acmecorp/infra/other");
const otherOutput = other.getOutput("x")
```

```typescript
import * as pulumi from "@pulumi/pulumi";
const other = new pulumi.StackReference("acmecorp/infra/other");
const otherOutput = other.getOutput("x")
```

```python
from pulumi import StackReference

other = StackReference(f"acmecorp/infra/other")
other_output = other.get_output("x")
```

```go
// StackReference is not currently supported in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
// StackReference is not currently supported in .NET.
//
// https://github.com/pulumi/pulumi/issues/3406.
```

Each output of the stack can then be accessed via `getOutput` or `getOutputSync` if the name of the stack is statically known.

## Config {#config}

To access configuration values that have been set with `pulumi config set`, use the following:

{{< langchoose csharp >}}

```javascript
let config = new pulumi.Config();
let name = config.require("name");
console.log(`Hello, ${name}!`);
```

```typescript
let config = new pulumi.Config();
let name = config.require("name");
console.log(`Hello, ${name}!`);
```

```python
config = pulumi.Config("project");
name = config.require("name");
print(f"Hello, {name}!")
```

```go
conf = config.New(ctx, "project");
name = conf.Require("name");
fmt.Printf("Hello, %s!", name);
```

```csharp
var config = new Pulumi.Config();
var name = config.Require("name");
Console.WriteLine($"Hello, {name}!");
```

Configuration values can be retrieved using [config.get] or [config.require].  Using `get` will return `undefined` if the configuration value was not provided, and `require` will raise an exception with a helpful error message to prevent the deployment from continuing.

Configuration values are stored as strings, but can be parsed as richly typed values.  For example, [config.getNumber] will convert the string value to a number and return a `Number` value instead of a string.  It will raise an exception if the value cannot be parsed as a number.

For richer structured data, the [config.getObject] method can be used to parse JSON values which can be set on the command line with `pulumi config set` and the `--path` flag. For example:

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

The `Config` object also provides functions to get the value from configuration and mark it as a secret. See [config.getSecret] or [config.requireSecret]. Unlike [config.get] and [config.require], these methods return an `Output<T>` which holds the underlying value and ensures that it is encrypted when it is being persisted.

For more information on config, see [Configuration and Secrets]({{< relref "/docs/intro/concepts/config" >}}).

## Components {#components}

A Pulumi **component** is a logical group of resources that contains other components and physical cloud resources. A Pulumi stack is itself a component that contains all top-level components and resources in a program.

To create a new component, either in a top-level program or in a library, create a subclass of [pulumi.ComponentResource]. Components provide a way to create reusable abstractions made up of other resources.

Here's a simple component definition:

{{< langchoose csharp >}}

```javascript
class MyResource extends pulumi.ComponentResource {
    constructor(name, opts) {
        super("pkg:MyResource", name, {}, opts);
    }
}
```

```typescript
class MyResource extends pulumi.ComponentResource {
    constructor(name, opts) {
        super("pkg:MyResource", name, {}, opts);
    }
}
```

```python
class MyResource(pulumi.ComponentResource):
    def __init__(self, name, opts = None):
        super().__init__('pkg:MyResource', name, None, opts)
```

```go
// ComponentResources are currently not directly supported in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
class MyResource : Pulumi.ComponentResource
{
    public MyResource(string name, ComponentResourceOptions opts)
        : base("pkg:MyResource", name, opts);
    {
        // initialization logic.

        // Signal to the UI that this resource has completed construction.
        this.RegisterOutputs();
    }
}
```

The call to `super` registers the component instance with the Pulumi engine. This records the resource in the checkpoint and tracks it across program deployments. Since all resources must have a name, a component constructor should accept a name and pass it to `super`.

A component must register a namespace, such as `pkg:MyResource` in the previous example. To reduce the potential of name conflicts, this name should contain the package name and resource type, such as `aws:lambda:Function`. The format `<package>:<module>:<type>` is typically used, though not currently fully enforced.

Components will often contain child resources. To track this relationship, pass the component instance as the parent when constructing a resource:

{{< langchoose csharp >}}

```javascript
let bucket = new aws.s3.Bucket(`${name}-bucket`, {}, { parent: this });
```

```typescript
let bucket = new aws.s3.Bucket(`${name}-bucket`, {}, { parent: this });
```

```python
bucket = s3.Bucket(f"{name}-bucket", opts=pulumi.ResourceOptions(parent=self))
```

```go
bucket := s3.Bucket(ctx, fmt.Sprintf("%s-bucket", name), &s3.BucketArgs{}, pulumi.ResourceOpt{Parent: parent});
```

```csharp
var bucket = new Aws.S3.Bucket($"{name}-bucket", new Aws.S3.BucketArgs(), new ResourceOptions { Parent = this });
```

Components can define their own properties using [registerOutputs]. The Pulumi engine uses this information to display the logical outputs of the component.  The call to `registerOutputs` also tells Pulumi that the resource is done registering children and should be considered fully constructed, so it is recommended that this method be called in all components even if no outputs need to be registered.

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
// ComponentResources are currently not directly supported in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
this.RegisterOutputs(new Dictionary<string, object>
{
    { "bucketDnsName", bucket.BucketDomainName }
});
```

In addition to the usual resource options, components accept a set of [providers](#providers) to use for their child resources. If a component is itself a child of another component, its set of providers is inherited from its parent by default.

{{< langchoose csharp >}}

```javascript
let component = new MyResource("component", { providers: { aws: useast1, kubernetes: myk8s } });
```

```typescript
let component = new MyResource("component", { providers: { aws: useast1, kubernetes: myk8s } });
```

```python
component = MyResource("component", ResourceOptions(providers={
    "aws": useast1,
    "kubernetes": myk8s,
}))
```

```go
// ComponentResources are currently not directly supported in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```csharp
var component = new MyResource("component", new ComponentResourceOptions { Providers = { awsUsEast1, myk8s } });
```

For more information about components, see the [Pulumi Components]({{< relref "/docs/tutorials/aws/s3-folder-component" >}}) tutorial.

## Providers {#providers}

A [CustomResource][pulumi.CustomResource] needs an associated resource provider to manage its Create, Read, Update, and Delete (_CRUD_) operations. This is in contrast to a [ComponentResource][pulumi.ComponentResource], whose logic is authored entirely in a Pulumi program's source language such as Javascript or Python. By default, a provider for a `CustomResource` is determined based on its [package](#packages). This default provider is automatically created by Pulumi, and is configured using the [config values](#config) of the package. For example, the following configuration and program will create a single EC2 instance in the `us-west-2` region.

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
// Providers are currently not supported in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
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

```bash
$ pulumi config set aws:region us-west-2
```

While this works for the majority of Pulumi programs, some programs may have special requirements. For example, it may require the ability to deploy to multiple AWS regions simultaneously, or to deploy to a Kubernetes cluster created earlier in the program that requires explicitly creating, configuring, and referencing providers. This is typically done by instantiating the relevant package's `Provider` type and passing in the options for each `CustomResource` or `ComponentResource` that needs to use it. For example, the following configuration and program will create an ACM certificate in the `us-east-1` region and a load balancer listener in the `us-west-2` region.

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
// Providers are currently not supported in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
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
// Providers are currently not supported in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
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
        var instance = new Aws.Ec2.Instance("instance", new Aws.Ec2.InstanceArgs { ... }, new ResourceOptions { Parent = this });
        var pod = new Kubernetes.Core.V1.Pod("pod", new Kubernetes.Core.V1.PodArgs { ... }, new ResourceOptions { Parent = this });
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

## Dynamic Providers <span class="badge badge-preview">PREVIEW</span> {#dynamicproviders}

Every `CustomResource` has a provider associated with it which knows how to `create`, `read`, `update`, and `delete` instances of the custom resource in the backing cloud provider.  This provider can be defined by implementing the Pulumi Resource Provider gRPC interface.  There are generally two approaches to implementing this provider interface:

1. Create a provider binary with the appropriate name and put it on the path, such that it will be loaded to handle CRUD operations from the Pulumi engine on resources from the package it is defined to handle.  For example, the `pulumi-resource-aws` binary will handle resources from the `aws` package.  This binary can be authored in any language, but must be authored and distributed out of band of a Pulumi program.
2. Define an implementation of the Provider interface directly within your Pulumi program, just for use within that program.

The former is used for most common Pulumi providers like AWS and Kubernetes.  The latter is a concept called _Dynamic Providers_, which provide a flexible approach to defining custom resource types directly within the source code of your Pulumi program.

You should consider implementing a dynamic provider if:

1. You need to manage a cloud resource for which there is not yet a published Pulumi Provider, but you expect to only use it from within one program. If you expect to use it from many programs, and in many languages, implementing a full provider is preferrable.
2. You need to integrate custom logic into the deployment workflow that runs exactly during one or more of the `create`, `read`, `update`, or `delete` steps, instead of running "always" as part of a normal Pulumi program.

Dynamic Providers are defined by first implementing the `pulumi.dynamic.ResourceProvider` interface, including the `create`, `read`, `update` and `delete` operations for your resource, as well as `check` and `diff`.  Default implementations are provided for everything except `create`, so a minimal implementation could look like:

{{< langchoose csharp >}}

```javascript
const myprovider = {
    async create(inputs) {
        return { id: "foo", outs: {}};
    }
}
```

```typescript
const myprovider: pulumi.dynamic.ResourceProvider = {
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

This resource provider is then used to create a new kind of custom resource by inheriting from the `pulumi.dynamic.Resource` base class which is a subclass of `pulumi.CustomResource`.

{{< langchoose csharp >}}

```javascript
class MyResource extends pulumi.dynamic.Resource {
    constructor(name, props, opts) {
        super(myprovider, name, props, opts);
    }
}
```

```typescript
class MyResource extends pulumi.dynamic.Resource {
    constructor(name: string, props: {}, opts?: pulumi.CustomResourceOptions) {
        super(myprovider, name, props, opts);
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

We can now create instances of the new `MyResource` resource kind in our program with `new MyResource("name", args)`.  When doing so, if Pulumi determines the resource has not yet been created, it will call the `create` method on the resource provider interface.  If another Pulumi deployment happens and the resource already exists, Pulumi will call the `diff` method to determine whether a change can be made in place or whether a replacement is needed.  If a replacement is needed, Pulumi will call `create` for the new resource and then `delete` for the old resource.  If no replacement is needed, Pulumi will call `update`.  In all cases, Pulumi first calls the `check` method with the resource arguments to give the provider a chance to validate that the arguments are valid.  And finally, if Pulumi needs to read an existing resource without managing it directly, it will call `read`.

> **Note:** _Dynamic Providers_ are a flexible and low-level mechanism to plug arbitrary code directly into the deployment process.  Whereas most code in a Pulumi program runs as part of constructing the desired state of resources (the "resource graph"), the code inside the dynamic provider resource provider interface implementations, such as `create` or `update`, runs instead during resource provisioning (while the resource graph is being turned into a set of CRUD operations scheduled against the cloud providers).  In fact, these two phases of execution actually run in completely separate processes.  The construction of a `new MyResource` happens inside the JavaScript, Python, or Go process running your Pulumi program.  But your implementations of `create` or `update` are executed by a special resource provider binary called `pulumi-resource-pulumi-nodejs`.  This binary is what actually implements the Pulumi resource provider gRPC interface and speaks directly to the Pulumi engine. Because your implementation of the resource provider interface must be used by a different process, potentially at a different point in time, dynamic providers are built on top of the same [function serialization]({{< relref "/docs/tutorials/aws/serializing-functions" >}}) that is used for turning callbacks into AWS Lambdas or Google Cloud Functions. Because of this serialization, there are some limits on what can be done inside the implementation of the resource provider interface, which you can read more about in the function serialization documentation.

### Dynamic Resource Inputs

A dynamic provider interfaces with other components via subclasses of `pulumi.dynamic.Resource`. The inputs to a dynamic provider's implementation are provided by instantiation of such a subclass. This is the `props` parameter in the constructor in the following example. Any properties you set in the `props` object will be passed to your `pulumi.dynamic.ResourceProvider` functions as the `inputs` where appropriate.

> For statically typed languages, you can get rich type information for the inputs declaring an input type to make it easy to use your custom resource.

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

### Resource Provider Interface

Implementing the `pulumi.dynamic.ResourceProvider` interface requires implementing a subset of the following methods. Each of these methods may be asynchronous, and most implementations of these methods will perform network I/O to provision resources in a backing cloud provider or other resource model. There are several important contracts between a dynamic provider and the Pulumi CLI that inform when these methods are called and with what data.

Though the input properties passed to a `pulumi.dynamic.Resource` instance will usually be of type `pulumi.Input<T>` the dynamic provider's functions are invoked with the fully resolved input values in order to compose well with Pulumi resources. Strong typing for the inputs to your provider's functions can help clarify this. You can achieve this by creating a second interface with the same properties as your resource's inputs, but with fully unwrapped types.

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

```go
// Dynamic Providers are currently not supported in Go.
```

```csharp
// Dynamic Providers are currently not supported in .NET.
```

#### `check(olds, news)`

Check is invoked before any other methods, and is passed the resolved input properties that were originally provided to the resource constructor by the user.  It is passed both the old input properties that were stored in the _state file_ after the previous update to the resource, as well as the new inputs from the current deployment.  It has two jobs: (1) Verify that the inputs (particularly the news) are valid and return useful error messages if they are not, and (2) Return a set of checked inputs.  The inputs returned from the call to `check` will be the inputs that the Pulumi engine uses for all further processing of the resource, including the values that will be passed back in to `diff`, `create`, `update`, or other operations.  In many cases, the `news` can be returned directly as the checked inputs.  But in cases where the provider need to populate defaults, or do some normalization on values, it may want to do that in the `check` method so that this data is complete and normalized prior to being passed in to other methods.

#### `create(inputs)`

Create is invoked when the URN of the resource created by the user is not found in the existing state of the deployment.  The engine passes the provider the checked inputs returned from the call to `check`.  The `create` method is expected to do the work in the backing cloud provider to create the requested resource.  It then returns two pieces of data: (1) an `id` that can uniquely identify the resource in the backing provider for later lookups, and (2) a set of `outputs` from the backing provider that should be returned to the user code as properties on the `CustomResource` object, and stored into the _checkpoint_ file.  If an error occurs, an exception can be thrown from the `create` method to return this error to the user.

#### `diff(id, olds, news)`

Diff is invoked when the URN of the resource created by the user is found in the existing state of the deployment. This means the resource already exists, and will need to be either updated or replaced.  The `diff` method is passed the `id` of the resource---as returned by `create`, as well as the old outputs from the checkpoint file which are values returned from a previous call to either `create` or `update`.  It is also passed the new checked inputs from the current deployment.  It returns four optional values:

- `changes`: `true` if the provider believes there is a difference between the `olds` and `news` and wants to do an `update` or `replace` to affect this change.
- `replaces`: An array of property names that have changed that should force a replacement.  Returning a non-zero length array here will tell the Pulumi engine to schedule a replacement instead of an update, which might involve downtime, so this should only be used when a `diff` requested by the user cannot be implemented as an in-place update on the backing cloud provider.
- `stables`: An array of property names that are known to not change between updates.  Pulumi will use this information to allow some `apply` calls on Outputs to be processed during `previews` because it knows that the values of these will stay the same during an update.
- `deleteBeforeReplace`: `true` if the proposed replacements require deleteing the existing resource before creating the new one.  By default Pulumi will try to create the new resource before deleting the old one to avoid downtime.
If an error occurs, an exception can be thrown from the `diff` method to return this error to the user.

#### `update(id, olds, news)`

Update is invoked if the call to `diff` indicates replacement is not needed.  It is passed the `id` of the resource as returned by `create`, and the old outputs from the checkpoint file which are values returned from a previous call to either `create` or `update`. It is also passed the new checked inputs from the current deployment.  The `update` method is expected to do the work in the backing cloud provider to update an existing resource to the new desired state.  It then returns a new set of `outputs` from the backing provider that should be returned to the user code as properties on the `CustomResource` object, and stored into the checkpoint file.  If an error occurs, an exception can be thrown from the `update` method to return this error to the user.

#### `delete(id, props)`

Delete is invoked if the URN exists in the previous state but not in the new desired state, or if a replacement is needed.  It is passed the `id` of the resource as returned by `create`, and the old outputs from the checkpoint file which are values returned from a previous call to either `create` or `update`.  It is expected to delete the corresponding resource from the backing cloud provider.  Nothing needs to be returned.  If an error occurs, an exception can be thrown from the `delete` method to return this error to the user.

#### `read(id, props)`

Read is invoked when the Pulumi engine needs to get data about a resource that is not managed by Pulumi. It is passed the the `id` of the resource as tracked in the backing cloud provider, and an optional bag of additional properties that can be used to disambiguate the request if needed. The `read` method is expected to look up the requested resource, and return the canonical `id` and output properties of this resource if found.  If an error occurs, an exception can be thrown from the `read` method to return this error to the user.

### Dynamic Resource Outputs

Any outputs can be returned by your `create` function in the `outs` property of `pulumi.dynamic.CreateResult`.

> The following only applies to **statically typed languages**.

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
    public readonly myStringOutput: pulumi.Output<string>;
    public readonly myNumberOutput: pulumi.Output<number>;

    constructor(name: string, props: MyResourceInputs, opts?: pulumi.CustomResourceOptions) {
        super(myprovider, name, { myStringOutput: undefined, myNumberOutput: undefined, ...props }, opts);
    }
}
```

```python
from pulumi import ResourceOptions, Input, Output
from pulumi.dynamic import Resource, ResourceProvider, CreateResult
from typing import Any, Optional

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

### Dynamic Provider Examples

#### Example: Random

This example highlights using dynamic providers to run some code only when a resource is created, and then store the results of that in the _checkpoint_ file so that this value is maintained across deployments of the resource.  In this case, there is no "backing cloud provider", just the _checkpoint_ file serialization that persists data.  The result is a provider similar to the one provided in `@pulumi/random`, although that library has many more flags than the following simple example:

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

#### Example: GitHub Labels REST API

This example highlights making REST API calls to some backing provider---the GitHub API in this case---to perform CRUD operations.  Because the resource provider method implementations will be serialized and used in a different process, we keep all the work to initialize the REST client and make calls to it local to each function.

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

## Packages {#packages}

Pulumi packages are normal NPM or Python packages. They transitively depend on `@pulumi/pulumi` which defines how resources created by a Pulumi program will be communicated to the Pulumi engine.  The ability to register resources with the Pulumi engine is the only difference between a Pulumi package and any other NPM package.

Some Pulumi packages have a dependency on a [Resource Provider plugin]({{< relref "/docs/reference/cli/pulumi_plugin.md" >}}) which contains the implementation for how to `create`, `read`, `update`, and `delete` resources defined by the package.  The [pulumi.CustomResource] base class is used to connect a JavaScript resource class with the resource provider it depends on for resource management.  Packages like [@pulumi/aws] and [@pulumi/kubernetes] define resources, such as `aws.ec2.Instance`, `kubernetes.Pod`, which are managed by the AWS and Kubernetes resource provider plugins. Packages such as [@pulumi/cloud] and [@pulumi/awsx] contain only higher-level component resources, which are not managed by a resource provider plugin.

## Runtime code {#runtime}

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

Libraries which use JavaScript callbacks as inputs to be provided as source text to resource construction---like the Lambda that is created by the `onObjectCreated` function in the previous example---are built on top of the [pulumi.runtime.serializeFunction] API, which takes a JavaScript `Function` object as input, and returns a `Promise` containing the serialized form of that function.

When serializing a function to text, the following steps are taken:

1. Any captured variables referenced by the function are evaluated when the function is serialized.
2. The values of those variables are serialized.
3. When the values are objects, all properties and prototype chains are serialized.  When the values are functions, those functions are serialized by following these same steps.

See [Serializing Functions]({{< relref "/docs/tutorials/aws/serializing-functions" >}}) for more details.

## Design Guidelines {#design-guidelines}

### OutputInstance.apply

It is recommended that the `func` argument of [OutputInstance.apply]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#OutputInstance-apply" >}}) not create any resources. Doing so can lead to the results of `pulumi preview` being wrong, since the `apply` callback will not get run during a preview. This is because the real output values are not yet known until the resources are deployed, so any resources created in the callback will not be seen during the `preview`.

However, you may have a scenario in which the actual value, such as an array of Outputs, is needed to create a resource but is not determined until the time of `pulumi update` and after part of the deployment has already happened. For example, an array of [Nameservers]({{< relref "/docs/reference/pkg/nodejs/pulumi/aws/route53#Zone-nameServers" >}})).  In that case, Pulumi lets you express this within the `apply`, but be cautioned that the preview may not include some changes to resources that are created or later removed from within the `apply`.

<!-- MARKDOWN LINKS -->
[pulumi.Resource]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Resource" >}}
[pulumi.ComponentResource]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#ComponentResource" >}}
[pulumi.CustomResource]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#CustomResource" >}}
[pulumi.Output]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Output" >}}
[pulumi.Input]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Input" >}}
[@pulumi/pulumi]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi" >}}
[@pulumi/aws]: {{< relref "/docs/reference/pkg/nodejs/pulumi/aws" >}}
[@pulumi/kubernetes]: {{< relref "/docs/reference/pkg/nodejs/pulumi/kubernetes" >}}
[@pulumi/cloud]: {{< relref "/docs/reference/pkg/nodejs/pulumi/cloud" >}}
[@pulumi/awsx]: {{< relref "/docs/reference/pkg/nodejs/pulumi/awsx" >}}

[pulumi.getStack]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#getStack" >}}
[pulumi.log]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi/log" >}}
[pulumi.runtime.serializeFunction]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi/runtime#serializeFunction" >}}
[pulumi.output]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#output" >}}
[pulumi.all]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#all" >}}

[config.get]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-get" >}}
[config.require]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-require" >}}
[config.getNumber]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-getNumber" >}}
[config.getObject]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-getObject" >}}
[config.getSecret]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-getSecret" >}}
[config.requireSecret]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-requireSecret" >}}

[registerOutputs]: {{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#ComponentResource-registerOutputs" >}}
<!-- END LINKS -->
