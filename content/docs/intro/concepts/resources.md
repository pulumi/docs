---
title: "Resources"
meta_desc: An in depth look at Pulumi resources and their usage.
menu:
  intro:
    parent: concepts
    weight: 4
---

Resources represent the fundamental components that make up your infrastructure, such as a compute instance, storage bucket, or database instance.

All infrastructure resources are described by one of two subclasses of the `Resource` class. These two subclasses are:

- `CustomResource`: A resource managed by a [resource providers]({{< relref "#resource-providers" >}}), such as AWS, Microsoft Azure, Google Cloud, Kubernetes, and so on.
- `ComponentResource`: A component resource is a logical grouping of other resources that creates a larger, higher-level abstraction that encapsulates its implementation details.

## Custom Resources

The Pulumi SDK has libraries for AWS, Google, Azure, with Kubernetes, as well as other providers. These libraries describe the custom resources that each cloud provider currently offers and are updated frequently to match changes to underlying services.

To use a provider library, import or reference the relevant library package when writing a program, as you would with any other shared library. For more information on the resources for each provider, see [Resource Documentation]({{< relref "/docs/reference/pkg#resource-documentation">}}).

A custom resource’s desired state is declared by constructing an instance of the resource:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let res = new Resource(name, args, options);
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let res = new Resource(name, args, options);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
res = Resource(name, args, options)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
res, err := NewResource(ctx, name, args, opt1, opt2)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var res = new Resource(name, args, options);
```

{{% /choosable %}}

{{< /chooser >}}

All resources have a required [`name`]({{< relref "#names" >}}) argument, which must be unique across resources of the same kind in a [`stack`]({{< relref "/docs/intro/concepts/stack" >}}). This *logical name* influences the *physical name* assigned by your infrastructure’s cloud provider. Pulumi [auto-names]({{< relref "#autonaming" >}}) physical resources by default, so the physical name and the logical name may differ. This auto-naming behavior can be overridden, if required.

The [`args`]({{< relref "#args" >}}) argument is an object with a set of named property input values that are used to initialize the resource. These can be normal raw values—such as strings, integers, lists, and maps—or outputs from other resources. For more information, see [Inputs and Outputs]({{< relref "docs/intro/concepts/inputs-outputs" >}}).

The [`options`]({{< relref "#options" >}}) argument is optional, but lets you control certain aspects of the resource. For example, you can show explicit dependencies, use a custom provider configuration, or import an existing infrastructure.

### Resource Names {#names}

Every resource managed by Pulumi has a logical name that you specify as an argument to its constructor. For instance, the logical name of this IAM role is `my-role`:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let role = new aws.iam.Role("my-role");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let role = new aws.iam.Role("my-role");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
role = iam.Role("my-role")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
role, err := iam.NewRole(ctx, "my-role", &iam.RoleArgs{})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var role = new Aws.Iam.Role("my-role");
```

{{% /choosable %}}

{{< /chooser >}}

The logical name you specify during resource creation is used in two ways:

- As a default prefix for the resource’s physical name, assigned by the cloud provider.
- To construct the [Universal Resource Name (URN)]({{< relref "#urns" >}}) used to track the resource across updates.

Pulumi uses the logical name to track the identity of a resource through multiple deployments of the same program and uses it to choose between creating new resources or updating existing ones.

The variable names assigned to resource objects are not used for either logical or physical resource naming. The variable only refers to that resource in the program. For example, in this code:

```typescript
var foo = new aws.Thing("my-thing");
```

The variable name `foo` has no bearing at all on the resulting infrastructure. You could change it to another name, run `pulumi up`, and the result would be no changes. The only exception is if you export that variable, in which case the name of the export would change to the new name.

#### Physical Names and Auto-Naming {#autonaming}

A resource’s logical and physical names may not match. In fact, most physical resource names in Pulumi are, by default, auto-named. As a result, even if your IAM role has a logical name of `my-role`, the physical name will typically look something like `my-role-d7c2fa0`. The suffix appended to the end of the name is random.

This random suffix serves two purposes:

- It ensures that two stacks for the same project can be deployed without their resources colliding. The suffix helps you to create multiple instances of your project more easily, whether because you want, for example, many development or testing stacks, or to scale to new regions.
- It allows Pulumi to do zero-downtime resource updates. Due to the way some cloud providers work, certain updates require replacing resources rather than updating them in place. By default, Pulumi creates replacements first, then updates the existing references to them, and finally deletes the old resources.

For cases that require specific names, you can override auto-naming by specifying a physical name. Most resources have a `name` property that you can use to name the resource yourself. Specify your name in the argument object to the constructor. Here’s an example.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let role = new aws.iam.Role("my-role", {
    name: "my-role-001",
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let role = new aws.iam.Role("my-role", {
    name: "my-role-001",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
role = iam.Role('my-role', {
    name='my-role-001'
})
```

{{% /choosable %}}
{{% choosable language go %}}

```go
role, err := iam.NewRole(ctx, "my-role", &iam.RoleArgs{
    Name: pulumi.String("my-role-001"),
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var role = new Aws.Iam.Role("my-role", new Aws.Iam.RoleArgs
{
    Name = "my-role-001",
});
```

{{% /choosable %}}

{{< /chooser >}}

If the `name` property is not available on a resource, consult the [API Reference]({{< relref "/docs/reference/pkg" >}}) for the specific resource you are creating. Some resources use a different property to override auto-naming. For instance, the `aws.s3.Bucket` type uses the property `bucket` instead of name. Other resources, such as `aws.kms.Key`, do not have physical names and use other auto-generated IDs to uniquely identify them.

Overriding auto-naming makes your project susceptible to naming collisions. As a result, for resources that may need to be replaced, you should specify `deleteBeforeReplace: true` in the resource’s options. This option ensures that old resources are deleted before new ones are created, which will prevent those collisions.

Because physical and logical names do not need to match, you can construct the physical name by using your project and stack names. Similarly to auto-naming, this approach protects you from naming collisions while still having meaningful names. Note that `deleteBeforeReplace` is still necessary:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let role = new aws.iam.Role("my-role", {
    name: "my-role-" + pulumi.getProject() + "-" + pulumi.getStack(),
}, { deleteBeforeReplace: true });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let role = new aws.iam.Role("my-role", {
    name: `my-role-${pulumi.getProject()}-${pulumi.getStack()}`,
}, { deleteBeforeReplace: true });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
role = iam.Role('my-role', {
    name='my-role-{}-{}'.format(pulumi.get_project(), pulumi.get_stack())
}, opts=ResourceOptions(delete_before_replace=True))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
role, _ := iam.NewRole(ctx, "my-role", &iam.RoleArgs{
    Name: fmt.Sprintf("my-role-%s-%s", ctx.Project(), ctx.Stack()),
}, pulumi.DeleteBeforeReplace(true))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var role = new Aws.Iam.Role("my-role", new Aws.Iam.RoleArgs
    {
        Name = string.Format($"my-role-{Deployment.Instance.ProjectName}-{Deployment.Instance.StackName}"),
    },
    new CustomResourceOptions { DeleteBeforeReplace = true }
);
```

{{% /choosable %}}

{{< /chooser >}}

#### Resource URNs {#urns}

Each resource is assigned a [Uniform Resource Name (URN)](https://en.wikipedia.org/wiki/Uniform_Resource_Name) that uniquely identifies that resource globally. Unless you are writing a tool, you will seldom need to interact with an URN directly, but it is fundamental to how Pulumi works so it’s good to have a general understanding of it.

The URN is automatically constructed from the project name, stack name, resource name, resource type, and the types of all the parent resources (in the case of [component resources]({{< relref "#components" >}})).

The following is an example of a URN:

```text
urn:pulumi:production::acmecorp-website::custom:resources:Resource$aws:s3/bucket:Bucket::my-bucket
        ^^^^^^^^^^  ^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^
        <stack-name>  <project-name>        <parent-type>          <resource-type>  <resource-name>
```

The URN must be globally unique. This means all of the components that go into a URN must be unique within your program. If you create two resources with the same name, type, and parent path, for instance, you will see an error:

```bash
error: Duplicate resource URN 'urn:pulumi:production::acmecorp-website::custom:resources:Resource$aws:s3/bucket:Bucket::my-bucket'; try giving it a unique name
```

Any change to the URN of a resource causes the old and new resources to be treated as unrelated—the new one will be created (since it was not in the prior state) and the old one will be deleted (since it is not in the new desired state). This behavior happens when you change the `name` used to construct the resource or the structure of a resource’s parent hierarchy.

Both of these operations will lead to a different URN, and thus require the `create` and `delete` operations instead of an `update` or `replace` operation that you would use for an existing resource. In other words, be careful when you change a resource’s name.

{{% notes "info" %}}
If you’d like to rename a resource without destroying the old one, refer to the [aliases]({{< relref "#aliases" >}}) resource option.
{{% /notes %}}

Resources constructed as children of a component resource should ensure their names are unique across multiple instances of the component resource. In general, the name of the component resource instance itself (the `name` parameter passed into the component resource constructor) should be used as part of the name of the child resources.

### Resource Arguments {#args}

A resource’s argument parameters differ by resource type. Each resource has a number of named input properties that control the behavior of the resulting infrastructure. To determine what arguments a resource supports, refer to that resource’s [API documentation]({{< relref "/docs/reference/pkg" >}}).

### Resource Options {#options}

All resource constructors accept an options argument that provide the following resource options:

- [additionalSecretOutputs]({{< relref "#additionalsecretoutputs" >}}): specify properties that must be encrypted as secrets.
- [aliases]({{< relref "#aliases" >}}): specify aliases for this resource, so that renaming or refactoring doesn’t replace it.
- [customTimeouts]({{< relref "#customtimeouts" >}}): override the default retry/timeout behavior for resource provisioning. The default value varies by resource.
- [deleteBeforeReplace]({{< relref "#deletebeforereplace" >}}): override the default create-before-delete behavior when replacing a resource.
- [dependsOn]({{< relref "#dependson" >}}): specify additional explicit dependencies in addition to the ones in the dependency graph.
- [ignoreChanges]({{< relref "#ignorechanges" >}}): declare that changes to certain properties should be ignored during a diff.
- [import]({{< relref "#import" >}}): bring an existing cloud resource into Pulumi.
- [parent]({{< relref "#parent" >}}): establish a parent/child relationship between resources.
- [protect]({{< relref "#protect" >}}): prevent accidental deletion of a resource by marking it as protected.
- [provider]({{< relref "#provider" >}}): pass an [explicitly configured provider]({{< relref "#explicit-provider-configuration" >}}), instead of using the default global provider.
- [transformations]({{< relref "#transformations" >}}): dynamically transform a resource’s properties on the fly.
- [version]({{< relref "#version" >}}): pass a provider plugin version that should be used when operating on a resource.

#### additionalSecretOutputs

This option specifies a list of named output properties that should be treated as [secrets]({{< relref "/docs/intro/concepts/secrets" >}}), which means they will be encrypted. It augments the list of values that Pulumi detects, based on secret inputs to the resource.

This example ensures that the password generated for a database resource is an encrypted secret:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let db = new Database("new-name-for-db", { /*...*/ },
    { additionalSecretOutputs: ["password"] });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let db = new Database("new-name-for-db", { /*...*/ },
    { additionalSecretOutputs: ["password"] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database('db',
    opts=ResourceOptions(additional_secret_outputs=['password']))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.AdditionalSecretOutputs([]string{"password"}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("new-name-for-db", new DatabaseArgs(),
    new CustomResourceOptions { AdditionalSecretOutputs = { "password" } });
```

{{% /choosable %}}

{{< /chooser >}}

Only top-level resource properties can be designated secret. If sensitive data is nested inside of a property, you must mark the entire top-level output property as secret.

#### aliases

This option provides a list of aliases for a resource or component resource. If you’re changing the name, type, or parent path of a resource or component resource, you can add the old name to the list of aliases for a resource to ensure that existing resources will be migrated to the new name instead of being deleted and replaced with the new named resource.

For example, imagine we change a database resource’s name from `old-name-for-db` to `new-name-for-db`. By default, when we run pulumi up, we see that the old resource is deleted and the new one created. If we annotate that resource with the aliases option, however, the resource is updated in-place:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let db = new Database("new-name-for-db", {/*...*/},
    { aliases: [{ name: "old-name-for-db" }] });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let db = new Database("new-name-for-db", {/*...*/},
    { aliases: [{ name: "old-name-for-db" }] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database('db',
    opts=ResourceOptions(aliases=[Alias(name='old-name-for-db')]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.Aliases(pulumi.Alias{Name: pulumi.String("old-name-for-db")}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("new-name-for-db", new DatabaseArgs(),
    new CustomResourceOptions { Aliases = { new Alias { Name = "old-name-for-db"} } });
```

{{% /choosable %}}

{{< /chooser >}}

The aliases option accepts a list of old identifiers. If a resource has been renamed multiple times, it can have many aliases. The list of aliases may contain old `Alias` objects and/or old resource URNs.

The above example used objects of type `Alias` with the old resource names. These values may specify any combination of the old name, type, parent, stack, and/or project values. Alternatively, you can just specify the URN directly:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let db = new Database("new-name-for-db", {/*...*/},
    { aliases: [ "urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db" ] });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let db = new Database("new-name-for-db", {/*...*/},
    { aliases: [ "urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db" ] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database('db',
    opts=ResourceOptions(aliases=['urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db']))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.Aliases([]pulumi.Alias{pulumi.Alias{
        URN: pulumi.URN("urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db"),
    }})
)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("new-name-for-db", new DatabaseArgs(),
    new CustomResourceOptions { Aliases = { new Alias {
        Urn = "urn:pulumi:stackname::projectname::aws:rds/database:Database::old-name-for-db" } } });
```

{{% /choosable %}}

{{< /chooser >}}

#### customTimeouts

This option provides a set of custom timeouts for `create`, `update`, and `delete` operations on a resource. These timeouts are specified using a duration string such as "5m" (5 minutes), "40s" (40 seconds), or "1d" (1 day). Supported duration units are "ns", "us" (or "µs"), "ms", "s", "m", and "h" (nanoseconds, microseconds, milliseconds, seconds, minutes, and hours, respectively).

For the most part, Pulumi automatically waits for operations to complete and times out appropriately. In some circumstances, such as working around bugs in the infrastructure provider, custom timeouts may be necessary.

This example specifies that the create operation should wait up to 30 minutes to complete before timing out:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let db = new Database("db", {/*...*/},
    { customTimeouts: { create: "30m" } });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let db = new Database("db", {/*...*/},
    { customTimeouts: { create: "30m" } });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database('db',
    opts=ResourceOptions(custom_timeouts=CustomTimeouts(create='30m')))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.Timeouts(&pulumi.CustomTimeouts{Create: "30m"}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("db", new DatabaseArgs(),
    new CustomResourceOptions {
        CustomTimeouts = new CustomTimeouts { Create = TimeSpan.FromMinutes(30) }
    });
```

{{% /choosable %}}

{{< /chooser >}}

#### deleteBeforeReplace

A resource may need to be replaced if an immutable property changes. In these cases, cloud providers do not support updating an existing resource so a new instance will be created and the old one deleted. By default, to minimize downtime, Pulumi creates new instances of resources before deleting old ones.

Setting the `deleteBeforeReplace` option to true means that Pulumi will delete the existing resource before creating its replacement. Be aware that this behavior has a cascading impact on dependencies so more resources may be replaced, which can lead to downtime. However, this option may be necessary for some resources that manage scarce resources behind the scenes, and/or resources that cannot exist side-by-side.

This example deletes a database entirely before its replacement is created:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let db = new Database("db", {/*...*/},
    { deleteBeforeReplace: true});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let db = new Database("db", {/*...*/},
    { deleteBeforeReplace: true});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database("db",
    opts=ResourceOptions(delete_before_replace=True))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, err := NewDatabase(ctx, "db", &DatabaseArgs{ /*...*/ },
    pulumi.DeleteBeforeReplace(true))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// The resource will be deleted before it's replacement is created
var db = new Database("db", new DatabaseArgs(),
    new CustomResourceOptions { DeleteBeforeReplace = true });
```

{{% /choosable %}}

{{< /chooser >}}

#### dependsOn

The `dependsOn` option creates a list of explicit dependencies between resources.

Pulumi automatically tracks dependencies between resources when you supply an input argument that came from another resource’s output properties. In some cases, however, you may need to explicitly specify additional dependencies that Pulumi doesn’t know about but must still respect. This might happen if a dependency is external to the infrastructure itself—such as an application dependency—or is implied due to an ordering or eventual consistency requirement. The `dependsOn` option ensures that resource creation, update, and deletion operations are done in the correct order.

This example demonstrates how to make res2 dependent on res1, even if there is no property-level dependency:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let res1 = new MyResource("res1", {/*...*/});
let res2 = new MyResource("res2", {/*...*/}, { dependsOn: [res1] });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let res1 = new MyResource("res1", {/*...*/});
let res2 = new MyResource("res2", {/*...*/}, { dependsOn: [res1] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
res1 = MyResource("res1");
res2 = MyResource("res2", opts=ResourceOptions(depends_on=[res1]));
```

{{% /choosable %}}
{{% choosable language go %}}

```go
res1, _ := NewMyResource(ctx, "res1", &MyResourceArgs{/*...*/})
res2, _ := NewMyResource(ctx, "res2", &MyResourceArgs{/*...*/}, pulumi.DependsOn([]Resource{res1}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var res1 = new MyResource("res1", new MyResourceArgs());
var res2 = new MyResource("res2", new MyResourceArgs(),
    new CustomResourceOptions { DependsOn = { res1 } });
```

{{% /choosable %}}

{{< /chooser >}}

#### ignoreChanges

This option specifies a list of properties that Pulumi will ignore when it updates existing resources. Any properties specified in this list that are also specified in the resource’s arguments will only be used when creating the resource.

For instance, in this example, the resource’s prop property "new-value" will be set when Pulumi initially creates the resource, but from then on, any updates will ignore it:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let res = new MyResource("res",
    { prop: "new-value" }, { ignoreChanges: ["prop"] });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let res = new MyResource("res",
    { prop: "new-value" }, { ignoreChanges: ["prop"] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
res = MyResource("res",
    prop="new-value",
    opts=ResourceOptions(ignore_changes=["prop"]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
res, _ := NewMyResource(ctx, "res",
    &MyResourceArgs{Prop: "new-value"},
    pulumi.IgnoreChanges([]string{"prop"}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var res = new MyResource("res",
    new MyResourceArgs { Prop = "new-value" },
    new CustomResourceOptions { IgnoreChanges = { "prop" } });
```

{{% /choosable %}}

{{< /chooser >}}

One reason you would use the `ignoreChanges` option is to ignore changes in properties that lead to diffs. Another reason is to change the defaults for a property without forcing all existing deployed stacks to update or replace the affected resource. This is common after you’ve imported existing infrastructure provisioned by another method into Pulumi. In these cases, there may be historical drift that you’d prefer to retain, rather than replacing and reconstructing critical parts of your infrastructure.

In addition to passing simple property names, nested properties can also be supplied to ignore changes to a more targeted nested part of the resource's inputs. Here are examples of legal paths that can be passed to specify nested properties of objects and arrays, as well as to escape object keys that contain special characters:

- `root`
- `root.nested`
- `root["nested"]`
- `root.double.nest`
- `root["double"].nest`
- `root["double"]["nest"]`
- `root.array[0]`
- `root.array[100]`
- `root.array[0].nested`
- `root.array[0][1].nested`
- `root.nested.array[0].double[1]`
- `root["key with \"escaped\" quotes"]`
- `root["key with a ."]`
- `["root key with \"escaped\" quotes"].nested`
- `["root key with a ."][100]`

{{% notes "info" %}}
The property names passed to `ignoreChanges` should always be the “camelCase” version of the property name, as used in the core Pulumi resource model.
{{% /notes %}}

#### import

This option imports an existing cloud resource so that Pulumi can manage it. Imported resources can have been provisioned by any other method, including manually in the cloud console or with the cloud CLI.

To import a resource, first specify the `import` option with the resource’s ID. This ID is the same as would be returned by the id property for any resource created by Pulumi; the ID is resource-specific. Pulumi reads the current state of the resource with the given ID from the cloud provider. Next, you must specify all required arguments to the resource constructor so that it exactly matches the state to import. By doing this, you end up with a Pulumi program that will accurately generate a matching desired state.

This example imports an existing EC2 security group with ID sg-04aeda9a214730248 and an EC2 instance with ID `i-06a1073de86f4adef`:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

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

{{% /choosable %}}
{{% choosable language typescript %}}

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

{{% /choosable %}}
{{% choosable language python %}}

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

{{% /choosable %}}
{{% choosable language csharp %}}

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

{{% /choosable %}}

{{< /chooser >}}

For this to work, your Pulumi stack must be configured correctly. In this example, it’s important that the AWS region is correct.

If the resource’s arguments differ from the imported state, the import will fail. You will receive this message: `warning: inputs to import do not match the existing resource; importing this resource will fail`. Select “details” in the `pulumi up` preview to learn what the differences are. If you try to proceed without correcting the inconsistencies, you will see this message: `error: inputs to import do not match the existing resource`. To fix these errors, make sure that your program computes a state that completely matches the resource to be imported.

Because of auto-naming, it is common to run into this error when you import a resource’s name property. Unless you explicitly specify a name, Pulumi will auto-generate one, which is guaranteed not to match, because it will have a random hex suffix. To fix this problem, explicitly specify the resource’s name [as described here]({{< relref "#autonaming" >}}). Note that, in the example for the EC2 security group, the name was specified by passing `web-sg-62a569b` as the resource’s name property.

Once a resource is successfully imported, remove the `import` option because Pulumi is now managing the resource.

#### parent

This option specifies a parent for a resource. It is used to associate children with the parents that encapsulate or are responsible for them. Good examples of this are [component resources]({{< relref "#components" >}}). The default behavior is to parent each resource to the implicitly-created `pulumi:pulumi:Stack` component resource that is a root resource for all Pulumi stacks.

For example, this code creates two resources, a parent and child, the latter of which is a child to the former:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let parent = new MyResource("parent", {/*...*/});
let child = new MyResource("child", {/*...*/}, { parent: parent });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let parent = new MyResource("parent", {/*...*/});
let child = new MyResource("child", {/*...*/}, { parent: parent });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
parent = MyResource("parent");
child = MyResource("child", opts=ResourceOptions(parent=parent));
```

{{% /choosable %}}
{{% choosable language go %}}

```go
parent, _ := NewMyResource(ctx, "parent", &MyResourceArgs{/*...*/})
child, _ := NewMyResource(ctx, "child", &MyResourceArgs{/*...*/}, pulumi.Parent(parent))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var parent = new MyResource("parent", new MyResourceArgs());
var child = new MyResource("child", new MyResourceArgs(),
    new CustomResourceOptions { Parent = parent });
```

{{% /choosable %}}

{{< /chooser >}}

Using parents can clarify causality or why a given resource was created in the first place. For example, this pulumi up output shows an AWS Virtual Private Cloud (VPC) with two subnets attached to it, and also shows that the VPC directly belongs to the implicit pulumi:pulumi:Stack resource:

```bash
Previewing update (dev):

    Type                       Name                             Plan
    pulumi:pulumi:Stack        parent-demo-dev
+   ├─ awsx:x:ec2:Vpc          default-vpc-866580ff             create
+   │  ├─ awsx:x:ec2:Subnet    default-vpc-866580ff-public-1    create
+   │  └─ awsx:x:ec2:Subnet    default-vpc-866580ff-public-0    create
```

#### protect

The `protect` option marks a resource as protected. A protected resource cannot be deleted directly. Instead, you must first set `protect: false` and run `pulumi up`. Then you can delete the resource by removing the line of code or by running `pulumi destroy`. The default is to inherit this value from the parent resource, and `false` for resources without a parent.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let db = new Database("db", {}, { protect: true});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let db = new Database("db", {}, { protect: true});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
db = Database("db", opts=ResourceOptions(protect=True))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
db, _ := NewDatabase(ctx, "db", &DatabaseArgs{}, pulumi.Protect(true));
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var db = new Database("db", new DatabaseArgs(),
    new CustomResourceOptions { Protect = true });
```

{{% /choosable %}}

{{< /chooser >}}

#### provider

The `provider` option sets a provider for the resource. For more information, see [Providers]){{< relref "#providers" >}}. The default is to inherit this value from the parent resource, and to use the ambient provider specified by Pulumi configuration for resources without a parent.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let provider = new aws.Provider("provider", { region: "us-west-2" });
let vpc = new aws.ec2.Vpc("vpc", {}, { provider: provider });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let provider = new aws.Provider("provider", { region: "us-west-2" });
let vpc = new aws.ec2.Vpc("vpc", {}, { provider: provider });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
provider = Provider("provider", region="us-west-2")
vpc = ec2.Vpc("vpc", opts=ResourceOptions(provider=provider))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
provider, _ := aws.NewProvider(ctx, "provider", &aws.ProviderArgs{Region: pulumi.StringPtr("us-west-2")})
vpc, _ := ec2.NewVpc(ctx, "vpc", &ec2.VpcArgs{}, pulumi.Provider(provider))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var provider = new Aws.Provider("provider", new Aws.ProviderArgs { Region = "us-west-2" });
var vpc = new Aws.Ec2.Vpc("vpc", new Aws.Ec2.VpcArgs(),
    new CustomResourceOptions { Provider = provider });
```

{{% /choosable %}}

{{< /chooser >}}

#### transformations

The `transformations` option provides a list of transformations to apply to a resource and all of its children. This option is used to override or modify the inputs to the child resources of a component resource. One example is to use the option to add other resource options (such as `ignoreChanges` or `protect`). Another example is to modify an input property (such as adding to tags or changing a property that is not directly configurable).

Each transformation is a callback that gets invoked by the Pulumi runtime. It receives the resource type, name, input properties, resource options, and the resource instance object itself. The callback returns a new set of resource input properties and resource options that will be used to construct the resource instead of the original values.

This example looks for all VPC and Subnet resources inside of a component’s child hierarchy and adds an option to ignore any changes for tags properties (perhaps because we manage all VPC and Subnet tags outside of Pulumi):

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

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

{{% /choosable %}}
{{% choosable language typescript %}}

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

{{% /choosable %}}
{{% choosable language python %}}

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

{{% /choosable %}}
{{% choosable language go %}}

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

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var vpc = new MyVpcComponent("vpc", new ComponentResourceOptions
{
    ResourceTransformations =
    {
        args =>
        {
            if (args.Resource.GetResourceType() == "aws:ec2/vpc:Vpc" ||
                args.Resource.GetResourceType() == "aws:ec2/subnet:Subnet")
            {
                var options = CustomResourceOptions.Merge(
                    (CustomResourceOptions) args.Options,
                    new CustomResourceOptions { IgnoreChanges = {"tags"} });
                return new ResourceTransformationResult(args.Args, options);
            }

            return null;
        }
    }
});
```

{{% /choosable %}}

{{< /chooser >}}

{{% choosable language "typescript,javascript,python,go" %}}
Transformations can also be applied in bulk to many resources in a stack by using the `registerStackTransformation` function.
{{% /choosable %}}

{{% choosable language "csharp" %}}
Transformations can also be applied in bulk to many resources in a stack by using the `Stack` constructor's `StackOptions.ResourceTransformations` property:

```csharp
public class MyStack : Stack
{
    public MyStack() : base(new StackOptions { ResourceTransformations = ... })
    {
        ...
    }
}
```

{{% /choosable %}}

#### version

The `version` option specifies a provider version to use when operating on a resource. This version overrides the version information inferred from the current package. This option should be used rarely.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let vpc = new aws.ec2.Vpc("vpc", {}, { version: "2.10.0" });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let vpc = new aws.ec2.Vpc("vpc", {}, { version: "2.10.0" });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
vpc = ec2.Vpc("vpc", opts=ResourceOptions(version="2.10.0"))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
vpc, _ := ec2.NewVpc(ctx, "vpc", &ec2.VpcArgs{}, pulumi.Version("2.10.0"))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var vpc = new Aws.Ec2.Vpc("vpc", new Aws.Ec2.VpcArgs(),
    new CustomResourceOptions { Version = "2.10.0" });
```

{{% /choosable %}}

{{< /chooser >}}

### Resource Getter Functions {#resource-get}

You can use the static `get` function, which is available on all resource types, to look up an existing resource’s ID. The `get` function is different from the `import` function. The difference is that, although the resulting resource object’s state will match the live state from an existing environment, the resource will not be managed by Pulumi. A resource read with the `get` function will never be updated or deleted by Pulumi during an update.

You can use the `get` function to consume properties from a resource that was provisioned elsewhere. For example, this program reads an existing EC2 Security Group whose ID is `sg-0dfd33cdac25b1ec9` and uses the result as input to create an EC2 Instance that Pulumi will manage:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let aws = require("@pulumi/aws");

let group = aws.ec2.SecurityGroup.get("group", "sg-0dfd33cdac25b1ec9");

let server = new aws.ec2.Instance("web-server", {
    ami: "ami-6869aa05",
    instanceType: "t2.micro",
    securityGroups: [ group.name ], // reference the security group resource above
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

let group = aws.ec2.SecurityGroup.get("group", "sg-0dfd33cdac25b1ec9");

let server = new aws.ec2.Instance("web-server", {
    ami: "ami-6869aa05",
    instanceType: "t2.micro",
    securityGroups: [ group.name ], // reference the security group resource above
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_aws as aws

group = aws.ec2.SecurityGroup.get('group', 'sg-0dfd33cdac25b1ec9')

server = aws.ec2.Instance('web-server',
    ami='ami-6869aa05',
    instance_type='t2.micro',
    security_groups=[group.name]) # reference the security group resource above
```

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
    "github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ec2"
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

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Aws.Ec2.Inputs;

class MyStack : Stack
{
    public MyStack()
    {
        var group = SecurityGroup.Get("group", "sg-0dfd33cdac25b1ec9");

        var server = new Instance("web-server", new InstanceArgs {
            Ami = "ami-6869aa05",
            InstanceType = "t2.micro",
            SecurityGroups = { group.Name }
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

Two values are passed to the `get` function - the logical name Pulumi will use to refer to the resource, and the physical ID that the resource has in the target cloud.

Importantly, Pulumi will never attempt to modify the security group in this example. It simply reads back the state from your currently configured cloud account and then uses it as input for the new EC2 Instance.

## Component Resources {#components}

A component resource is a logical grouping of resources. Components resources usually instantiate a set of related resources in their constructor, aggregate them as children, and create a larger, useful abstraction that encapsulates their implementation details.

Here are a few examples of component resources:

- A `Vpc` that automatically comes with built-in best practices.
- An `AcmeCorpVirtualMachine` that adheres to your company’s requirements, such as tagging.
- A `KubernetesCluster` that can create EKS, AKS, and GKE clusters, depending on the target.

The implicit `pulumi:pulumi:Stack` resource is itself a component resource that contains all top-level resources in a program.

### Authoring a New Component Resource

To author a new component, either in a program or for a reusable library, create a subclass of [`ComponentResource`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.ComponentResource" >}}). Inside of its constructor, chain to the base constructor, passing its type string, name, arguments, and options. Also inside of its constructor, allocate any child resources, passing the [`parent`]({{< relref "#parent" >}}) option as appropriate to ensure component resource children are parented correctly.

Here’s a simple component example:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
class MyComponent extends pulumi.ComponentResource {
    constructor(name, opts) {
        super("pkg:index:MyComponent", name, {}, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
class MyComponent extends pulumi.ComponentResource {
    constructor(name, opts) {
        super("pkg:index:MyComponent", name, {}, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
class MyComponent(pulumi.ComponentResource):
    def __init__(self, name, opts = None):
        super().__init__('pkg:index:MyComponent', name, None, opts)
```

{{% /choosable %}}
{{% choosable language go %}}

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

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
class MyComponent : Pulumi.ComponentResource
{
    public MyComponent(string name, ComponentResourceOptions opts)
        : base("pkg:index:MyComponent", name, opts)
    {
        // initialization logic.

        // Signal to the UI that this resource has completed construction.
        this.RegisterOutputs();
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

Upon creating a new instance of MyComponent, the call to the base constructor (using `super/base`) registers the component resource instance with the Pulumi engine. This records the resource’s state and tracks it across program deployments so that you see diffs during updates just like with a regular resource (even though component resources have no provider logic associated with them). Since all resources must have a name, a component resource constructor should accept a name and pass it to super.

If you wish to have full control over one of the custom resource’s lifecycle in your component resource—including running specific code when a resource has been updated or deleted—you should look into [`dynamic providers`]({{< relref "#dynamicproviders" >}}). These let you create full-blown resource abstractions in your language of choice.

A component resource must register a unique type name with the base constructor. In the example, the registration is `pkg:index:MyComponent`. To reduce the potential of other type name conflicts, this name contains the package and module name, in addition to the type: `<package>:<module>:<type>`. These names are namespaced alongside non-component resources, such as aws:lambda:Function.

For more information about component resources, see the [Pulumi Components tutorial]({{< relref "/docs/tutorials/aws/s3-folder-component" >}}).

### Creating Child Resources

Component resources often contain child resources. The names of child resources are often derived from the component resources’s name to ensure uniqueness. For example, you might use the component resource’s name as a prefix. Also, when constructing a resource, children must be registered as such. To do this, pass the component resource itself as the `parent` option.

This example demonstrates both the naming convention and how to designate the component resource as the parent:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let bucket = new aws.s3.Bucket(`${name}-bucket`,
    {/*...*/}, { parent: this });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let bucket = new aws.s3.Bucket(`${name}-bucket`,
    {/*...*/}, { parent: this });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
bucket = s3.Bucket(f"{name}-bucket",
    opts=pulumi.ResourceOptions(parent=self))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
bucket, err := s3.NewBucket(ctx, fmt.Sprintf("%s-bucket", name),
    &s3.BucketArgs{ /*...*/ }, pulumi.Parent(myComponent))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var bucket = new Aws.S3.Bucket($"{name}-bucket",
    new Aws.S3.BucketArgs(/*...*/), new CustomResourceOptions { Parent = this });
```

{{% /choosable %}}

{{< /chooser >}}

### Registering Component Outputs

Component resources can define their own output properties by using register_outputs . The Pulumi engine uses this information to display the logical outputs of the component resource and any changes to those outputs will be shown during an update.

For example, this code registers an S3 bucket’s computed domain name, which won’t be known until the bucket is created:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
this.registerOutputs({
    bucketDnsName: bucket.bucketDomainName,
})
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
this.registerOutputs({
    bucketDnsName: bucket.bucketDomainName,
})
```

{{% /choosable %}}
{{% choosable language python %}}

```python
self.register_outputs({
    bucketDnsName: bucket.bucketDomainName
})
```

{{% /choosable %}}
{{% choosable language go %}}

```go
ctx.RegisterResourceOutputs(myComponent, pulumi.Map{
    "bucketDnsName": bucket.BucketDomainName,
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
this.RegisterOutputs(new Dictionary<string, object>
{
    { "bucketDnsName", bucket.BucketDomainName }
});
```

{{% /choosable %}}

{{< /chooser >}}

The call to `registerOutputs` typically happens at the very end of the component resource’s constructor.

The call to `registerOutputs` also tells Pulumi that the resource is done registering children and should be considered fully constructed, so—although it’s not enforced—the best practice is to call it in all components even if no outputs need to be registered.

### Inheriting Resource Providers

One option all resources have is the ability to pass an [explicit resource provider]({{< relref "#providers">}}) to supply explicit configuration settings. For instance, you may want to ensure that all AWS resources are created in a different region than the globally configured region. In the case of component resources, the challenge is that these providers must flow from parent to children.

To allow this, component resources accept a `providers` option that custom resources don’t have. This value contains a map from the provider name to the explicit provider instance to use for the component resource. The map is used by a component resource to fetch the proper `provider` object to use for any child resources. This example overrides the globally configured AWS region and sets it to us-east-1. Note that `myk8s` is the name of the Kubernetes provider.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let component = new MyComponent("...", {
    providers: {
        aws: useast1,
        kubernetes: myk8s,
    },
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let component = new MyComponent("...", {
    providers: {
        aws: useast1,
        kubernetes: myk8s,
    },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
component = MyComponent('...', ResourceOptions(providers={
    'aws': useast1,
    'kubernetes': myk8s,
}))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
component, err := NewMyResource(ctx, "...", nil, pulumi.ProviderMap(
    map[string]pulumi.ProviderResource{
        "aws":        awsUsEast1,
        "kubernetes": myk8s,
    },
))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var component = new MyResource("...", new ComponentResourceOptions {
    Providers = {
        { "aws", awsUsEast1 },
        { "kubernetes", myk8s }
    }
});
```

{{% /choosable %}}

{{< /chooser >}}

If a component resource is itself a child of another component resource, its set of providers is inherited from its parent by default.

## Resource Providers {#providers}

A resource provider handles communications with a cloud service to create, read, update, and delete the resources you define in your Pulumi programs. Pulumi passes your code to a language host such as Node.js, waits to be notified of resource registrations, assembles a model of your desired state, and calls on the resource provider to produce that state. The resource provider translates those requests into API calls to the cloud service.

A resource provider is tied to the language that you use to write your programs. For example, if your cloud provider is AWS, the following providers are available:

- JavaScript/TypeScript: `@pulumi/aws`
- Python: `pulumi-aws`
- Go: `github.com/pulumi/pulumi-aws/sdk/go/aws`
- .NET: `Pulumi.Aws`

Normally, since you declare the language and cloud provider you intend to use when you write a program, Pulumi installs the provider for you as a plugin, using the appropriate package manager, such as NPM for Typescript.

The resource provider for custom resources is determined based on its package name. For example, the `aws` package loads a plugin named `pulumi-resource-aws`, and the `kubernetes` package loads a plugin named `pulumi-resource-kubernetes`.

### Default Provider Configuration

By default, each provider uses its package’s global configuration settings, which are controlled by your stack’s configuration. You can set information such as your cloud provider credentials with environment variables and configuration files. If you store this data in standard locations, Pulumi knows how to retrieve them.

For example, suppose you run this CLI command:

```bash
$ pulumi config set aws:region us-west-2
```

Then, suppose you deploy the following Pulumi program:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let aws = require("@pulumi/aws");

let instance = new aws.ec2.Instance("myInstance", {
    instanceType: "t2.micro",
    ami: "myAMI",
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let aws = require("@pulumi/aws");

let instance = new aws.ec2.Instance("myInstance", {
    instanceType: "t2.micro",
    ami: "myAMI",
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi_aws import ec2

instance = ec2.Instance("myInstance", instance_type="t2.micro", ami="myAMI")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
vpc, err := ec2.NewInstance(ctx, "myInstance", &ec2.InstanceArgs{
    InstanceType: pulumi.String("t2.micro"),
    Ami:          pulumi.String("myAMI"),
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var instance = new Aws.Ec2.Instance("myInstance", new Aws.Ec2.InstanceArgs
{
    InstanceType = "t2.micro",
    Ami = "myAMI",
});
```

{{% /choosable %}}

{{< /chooser >}}

It creates a single EC2 instance in the us-west-2 region.

### Explicit Provider Configuration

While the default provider configuration may be appropriate for the majority of Pulumi programs, some programs may have special requirements. One example is a program that needs to deploy to multiple AWS regions simultaneously. Another example is a program that needs to deploy to a Kubernetes cluster, created earlier in the program, which requires explicitly creating, configuring, and referencing providers. This is typically done by instantiating the relevant package’s `Provider` type and passing in the options for each [CustomResource]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.CustomResource" >}}) or [ComponentResource]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.ComponentResource" >}}) that needs to use it. For example, the following configuration and program creates an ACM certificate in the `us-east-1` region and a load balancer listener in the `us-west-2` region.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

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

{{% /choosable %}}
{{% choosable language typescript %}}

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

{{% /choosable %}}
{{% choosable language python %}}

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

{{% /choosable %}}
{{% choosable language go %}}

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

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
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
```

{{% /choosable %}}

{{< /chooser >}}

```bash
$ pulumi config set aws:region us-west-2
```

Component resources also accept a set of providers to use with their child resources. For example, the EC2 instance parented to `myResource` in the program below is created in `us-east-1`, and the Kubernetes pod parented to myResource is created in the cluster targeted by the `test-ci` context.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

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

{{% /choosable %}}
{{% choosable language typescript %}}

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

{{% /choosable %}}
{{% choosable language python %}}

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

{{% /choosable %}}
{{% choosable language go %}}

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

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Aws = Pulumi.Aws;
using Kubernetes = Pulumi.Kubernetes;

class MyResource : ComponentResource
{
    public MyResource(string name, ComponentResourceOptions opts)
        : base(name, opts)
    {
        var instance = new Aws.Ec2.Instance("instance", new Aws.Ec2.InstanceArgs { ... }, new CustomResourceOptions { Parent = this });
        var pod = new Kubernetes.Core.V1.Pod("pod", new Kubernetes.Core.V1.PodArgs { ... }, new CustomResourceOptions { Parent = this });
    }
}

class MyStack
{
    public MyStack()
    {
        var useast1 = new Aws.Provider("useast1",
            new Aws.ProviderArgs { Region = "us-east-1" });
        var myk8s = new Kubernetes.Provider("myk8s",
            new Kubernetes.ProviderArgs { Context = "test-ci" });
        var myResource = new MyResource("myResource",
            new ComponentResourceOptions { Providers = { useast1, myk8s } });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

### Dynamic Providers {#dynamicproviders}

There are three types of resource providers. The first are the standard resource providers. These resource providers are built and maintained by Pulumi. There is a second kind, called a dynamic resource provider, which we will discuss here. These resource providers run only in the context of your program. They are not shareable. The third type of resource provider is shareable. You write it yourself and then you can distribute it so that others can use it.

Dynamic resource providers can be written in any language you choose. Because they are not shareable, dynamic resource providers do not need a plugin.

There are several reasons why you might want to write a dynamic resource provider. Here are some of them:

- You want to create some new custom resource types.
- You want to use a cloud provider that Pulumi doesn’t support. For example, you might want to write a dynamic resource provider for WordPress.

All dynamic providers must conform to certain interface requirements. You must at least implement the `create` function but, in practice, you will probably also want to implement the `read`, `update`, and `delete` functions as well.

To continue with our WordPress example, you would probably want to create new blogs, update existing blogs, and destroy them. The mechanics of how these operations happen would be essentially the same as if you used one of the standard resource providers. The difference is that the calls that would've been made on the standard resource provider by the Pulumi engine would now be made on your dynamic resource provider and it, in turn, would make the API calls to WordPress.

Dynamic providers are defined by first implementing the `pulumi.dynamic.ResourceProvider` interface. This interface supports all CRUD operations, but only the create function is required. A minimal implementation might look like this:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const myProvider = {
    async create(inputs) {
        return { id: "foo", outs: {}};
    }
}
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const myProvider: pulumi.dynamic.ResourceProvider = {
    async create(inputs) {
        return { id: "foo", outs: {}};
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi.dynamic import ResourceProvider, CreateResult

class MyProvider(ResourceProvider):
    def create(self, inputs):
        return CreateResult(id_="foo", outs={})
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are currently not supported in Go.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}

{{< /chooser >}}

This dynamic resource provider is then used to create a new kind of custom resource by inheriting from the `pulumi.dynamic.Resource` base class, which is a subclass of `pulumi.CustomResource`:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
class MyResource extends pulumi.dynamic.Resource {
    constructor(name, props, opts) {
        super(myProvider, name, props, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
class MyResource extends pulumi.dynamic.Resource {
    constructor(name: string, props: {}, opts?: pulumi.CustomResourceOptions) {
        super(myProvider, name, props, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi import ResourceOptions
from pulumi.dynamic import Resource
from typing import Any, Optional

class MyResource(Resource):
    def __init__(self, name: str, props: Any, opts: Optional[ResourceOptions] = None):
         super().__init__(MyProvider(), name, props, opts)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are currently not supported in Go.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}

{{< /chooser >}}

We can now create instances of the new `MyResource` resource type in our program with `new MyResource("name", args)`, just like we would any custom resource. Pulumi understands how to use the custom provider logic appropriately.

Specifically:

1. If Pulumi determines the resource has not yet been created, it will call the create method on the resource provider interface.
1. If another Pulumi deployment happens and the resource already exists, Pulumi will call the diff method to determine whether a change can be made in place or whether a replacement is needed.
1. If a replacement is needed, Pulumi will call create for the new resource and then call delete for the old resource.
1. If no replacement is needed, Pulumi will call update.
1. In all cases, Pulumi first calls the check method with the resource arguments to give the provider a chance to verify that the arguments are valid.
1. If Pulumi needs to read an existing resource without managing it directly, it will call read.

See below for details on each of these functions.

#### How Dynamic Providers Work

Dynamic providers are a flexible and low-level mechanism that allow you to include arbitrary code directly into the deployment process. While most code in a Pulumi program runs while the desired state of the resources is constructed (in other words, as the resource graph is built), the code inside a dynamic provider’s implementation, such as `create` or `update`, runs during resource provisioning, while the resource graph is being turned into a set of CRUD operations scheduled against the cloud provider.

In fact, these two phases of execution actually run in completely separate processes. The construction of a `new MyResource` happens inside the JavaScript, Python, or Go process running in your Pulumi program. In contrast, your implementations of create or update are executed by a special resource provider binary called `pulumi-resource-pulumi-nodejs`. This binary is what actually implements the Pulumi resource provider gRPC interface and it speaks directly to the Pulumi engine.

Because your implementation of the resource provider interface must be used by a different process, potentially at a different point in time, dynamic providers are built on top of the same [function serialization]({{< relref "/docs/tutorials/aws/serializing-functions" >}}) that is used for turning callbacks into AWS Lambdas or Google Cloud Functions. Because of this serialization, there are some limits on what can be done inside the implementation of the resource provider interface. You can read more about these limitations in the function serialization documentation.

#### The Resource Provider Interface

Implementing the `pulumi.dynamic.ResourceProvider` interface requires implementing a subset of the methods listed further down in this section. Each of these methods can be asynchronous, and most implementations of these methods will perform network I/O to provision resources in a backing cloud provider or other resource model. There are several important contracts between a dynamic provider and the Pulumi CLI that inform when these methods are called and with what data.

Though the input properties passed to a `pulumi.dynamic.Resource` instance will usually be [Input values]({{< relref "/docs/intro/concepts/inputs-outputs" >}}), the dynamic provider’s functions are invoked with the fully resolved input values in order to compose well with Pulumi resources. Strong typing for the inputs to your provider’s functions can help clarify this. You can achieve this by creating a second interface with the same properties as your resource’s inputs, but with fully unwrapped types.

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

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

class MyResourceProvider implements pulumi.dynamic.ResourceProvider {
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

{{% /choosable %}}
{{% choosable language python %}}

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

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are currently not supported in Go.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}
{{< /chooser >}}

##### check(olds, news)

The `check` method is invoked before any other methods. The resolved input properties that were originally provided to the resource constructor by the user are passed to it. The operation is passed both the old input properties that were stored in the *state file* after the previous update to the resource, as well as the new inputs from the current deployment. It has two jobs:

1. Verify that the inputs (particularly the news) are valid or return useful error messages if they are not.
1. Return a set of checked inputs.

The inputs returned from the call to `check` will be the inputs that the Pulumi engine uses for all further processing of the resource, including the values that will be passed back in to `diff`, `create`, `update`, or other operations. In many cases, the news can be returned directly as the checked inputs. But in cases where the provider needs to populate defaults, or do some normalization on values, it may want to do that in the `check` method so that this data is complete and normalized prior to being passed in to other methods.

##### create(inputs)

The `create` method is invoked when the URN of the resource created by the user is not found in the existing state of the deployment. The engine passes the provider the checked inputs returned from the call to `check`. The `create` method creates the resource in the cloud provider. It then returns two pieces of data:

1. An id that can uniquely identify the resource in the backing provider for later lookups, and
1. A set of outputs from the backing provider that should be returned to the user code as properties on the CustomResource object. These outputs are stored in the checkpoint file. If an error occurs, an exception can be thrown from the create method that should be returned to the user.

##### diff(id, olds, news)

The `diff` method is invoked when the URN of the resource created by the user already exists. Because the resource already exists it will need to be either updated or replaced. The `diff` method is passed the `id` of the resource, as returned by `create`, as well as the old outputs from the checkpoint file, which are values returned from a previous call to either `create` or `update`. The checked inputs from the current deployment are passed to the diff method.

It returns four optional values:

- `changes: true` if the provider believes there is a difference between the olds and news and wants to do an update or replace to affect this change.
- `replaces`: An array of property names that have changed that should force a replacement. Returning a non-zero length array tells the Pulumi engine to schedule a replacement instead of an update. Replacements might involve downtime, so this value should only be used when a diff requested by the user cannot be implemented as an in-place update on the cloud provider.
- `stables`: An array of property names that are known not to change between updates. Pulumi will use this information to allow some [`apply`]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) calls on [`Output[T]`]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) to be processed during `previews` because it knows that the values of these property names will stay the same during an update.
- `deleteBeforeReplace`: true if the proposed replacements require that the existing resource be deleted before creating the new one. By default, Pulumi will try to create the new resource before deleting the old one to avoid downtime. If an error occurs, an exception can be thrown from the diff method to return this error to the user.

##### update(id, olds, news)

The `update` method is invoked if the call to diff indicates that a replacement is unnecessary. The method is passed the `id` of the resource as returned by `create`, and the old outputs from the checkpoint file, which are values returned from a previous call to either `create` or `update`. The new checked inputs are also passed from the current deployment. The `update` method is expected to do the work in the cloud provider to update an existing resource to the new desired state. It then returns a new set of `outputs` from the cloud provider that should be returned to the user code as properties on the [`CustomResource`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.CustomResource" >}}) object, and stored into the checkpoint file. If an error occurs, an exception can be thrown from the `update` method to return this error to the user.

##### delete(id, props)

The `delete` operation is invoked if the URN exists in the previous state but not in the new desired state, or if a replacement is needed. The method is passed the `id` of the resource as returned by `create`, and the old outputs from the checkpoint file, which are values returned from a previous call to either `create` or `update`. The method deletes the corresponding resource from the cloud provider. Nothing needs to be returned. If an error occurs, an exception can be thrown from the `delete` method to return this error to the user.

##### read(id, props)

The `read` method is invoked when the Pulumi engine needs to get data about a resource that is not managed by Pulumi. The method is passed the `id` of the resource, as tracked in the cloud provider, and an optional bag of additional properties that can be used to disambiguate the request, if needed. The `read` method looks up the requested resource, and returns the canonical `id` and output properties of this resource if found. If an error occurs, an exception can be thrown from the `read` method to return this error to the user.

#### Dynamic Resource Inputs

The inputs to your `pulumi.dynamic.ResourceProvider`’s functions come from subclasses of `pulumi.dynamic.Resource`. These inputs include any values in the input arguments passed to the `pulumi.dynamic.Resource` constructor. This is just a map of key/value pairs however, in statically typed languages, you can declare types for these input shapes.

For example, `props`, in the `MyResource` class shown below, defines the inputs to the resource provider functions:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
class MyResource extends pulumi.dynamic.Resource {
    constructor(name, props, opts) {
        super(myprovider, name, props, opts);
    }
}
```

{{% /choosable %}}
{{% choosable language typescript %}}

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

{{% /choosable %}}
{{% choosable language python %}}

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

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are currently not supported in Go.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}

{{< /chooser >}}

#### Dynamic Resource Outputs

Any outputs can be returned by your create function in the outs property of `pulumi.dynamic.CreateResult`.

{{% notes "info" %}}
The following only applies to statically typed languages.
{{% /notes %}}

If you need to access the outputs of your custom resource outside it with strong typing support, declare each output property returned in the `outs` property by your `create` function as a class member of the `pulumi.dynamic.Resource` itself. For example, in TypeScript, these outputs must be declared as `public readonly` class members in your `pulumi.dynamic.Resource` class. These class members must also have the type `pulumi.Output<T>`.

The name of the class member must match the names of the output properties as returned by the `create` function.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
JavaScript does not support types.
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
...

interface MyResourceProviderOutputs {
    myNumberOutput: number;
    myStringOutput: string;
}

class MyResourceProvider implements pulumi.dynamic.ResourceProvider {
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

{{% /choosable %}}
{{% choosable language python %}}

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

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are not yet supported in Go.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}

{{< /chooser >}}

#### Dynamic Provider Examples

##### Example: Random

This example generates a random number using a dynamic provider. It highlights using dynamic providers to run some code only when a resource is created, and then store the results of that in the state file so that this value is maintained across deployments of the resource. Because we want our random number to be created once, and then remain stable for subsequent updates, we cannot simply use a random number generator in our program; we need dynamic providers. The result is a provider similar to the one provided in `@pulumi/random`, just specific to our program and language.

Implementing this example requires that we have a provider and resource type:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

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

{{% /choosable %}}
{{% choosable language typescript %}}

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

{{% /choosable %}}
{{% choosable language python %}}

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

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are currently not supported in Go.
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}

{{< /chooser >}}

Now, with this, we can construct new `Random` resource instances, and Pulumi will drive the right calls at the right time.

##### Example: GitHub Labels REST API

This example highlights how to make REST API calls to a backing provider to perform CRUD operations. In this case, the backing provider is the GitHub API in this case. Because the resource provider method implementations will be serialized and used in a different process, we keep all the work to initialize the REST client and to make calls to it, local to each function.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

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

{{% /choosable %}}
{{% choosable language typescript %}}

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

{{% /choosable %}}
{{% choosable language python %}}

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

{{% /choosable %}}
{{% choosable language go %}}

```go
// Dynamic Providers are not currently supported in Go.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Dynamic Providers are currently not supported in .NET.
```

{{% /choosable %}}

{{< /chooser >}}

##### Additional Examples

- [Add a Custom Domain to an Azure CDN endpoint](https://github.com/pulumi/examples/tree/master/azure-ts-dynamicresource)
    Similar to the previous example, this is another example of a shortcoming of the regular Azure resource provider available in Pulumi. However, due to the availability of a REST API, we can easily add a custom domain to an Azure CDN resource using a dynamic provider.
- [Dynamic Providers as Provisioners](https://github.com/pulumi/examples/tree/master/aws-ts-ec2-provisioners)
    Provisioning a VM after it is created is a common problem. Developers have the option to run user-supplied scripts while creating the VM itself. For example, the AWS EC2 resource has a userData parameter, that allows you to specify an inline script, which EC2 will run at instance startup. However, this example of dynamic providers as provisioners allows you to copy/execute scripts on the target instance without replacing the instance itself.
