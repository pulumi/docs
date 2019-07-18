---
title: "Programming Model"
expanded_url: /docs/reference/concepts/
menu:
  reference:
    parent: concepts
    weight: 1
---

{{< mini-toc >}}

## Overview {#overview}

In Pulumi, [resources](#resources) are defined by allocating resource objects in a program.  For example, your program would contain a statement such as `new aws.ec2.Instance(...)` in order to create a new AWS EC2 instance.  The first argument passed to the resource constructor is its `name`, which must be unique within the Pulumi program.

Dependencies between resources are expressed in Pulumi by using the [output properties](#outputs) of one resource in the construction of another resource.  For example, this definition of an EC2 instance creates a dependency on a `SecurityGroup`:


{{< langchoose >}}

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

To publish values that you wish to access outside your application, create a [stack output](#stack-outputs) via module exports.

In Pulumi, you can group multiple resources in a [component](#components). A component is a logical container for physical cloud resources and affects how resources are grouped in the CLI and the pulumi.com console.

## Programs {#programs}

Pulumi programs are authored in general purpose programming languages such as [JavaScript]({{< relref "javascript.md" >}}) or [Python]({{< relref "python.md" >}}). You can use any packages supported by the language's package manager, as well as [Pulumi packages]({{< relref "pkg" >}}).

When `pulumi up` is run, your Pulumi program is run and the Pulumi CLI determines the desired state of application resources. A Pulumi program can reference artifacts that have already been published (such as S3 objects or pre-built Docker images) or it can define application resources itself so that everything is versioned together. For example, if your program uses `cloud.Service` with a `build` step, or defines a Lambda for an S3 trigger, you're defining application code that is implicitly deployed during the `pulumi up`.

A Pulumi program is contained within a [project]({{< relref "project.md" >}}). In JavaScript, the `main` property of `package.json` defines the entry point for the Pulumi program.

## Pulumi SDK {#pulumipulumi}

The [@pulumi/pulumi] package is the core library for working with the Pulumi engine. This package defines the following kinds of resources which can be deployed with Pulumi:

- Resources ([pulumi.Resource])
- External cloud platform resources ([pulumi.CustomResource])
- Components defined entirely in JavaScript ([pulumi.ComponentResource])

Dependencies between resources are encoded with [pulumi.Output](#outputs).

This package also provides the following helpers:

- [pulumi.getStack] to get information about the current stack
- [pulumi.log] for logging deployment information
- [pulumi.runtime.serializeFunction] for turning JavaScript callbacks into data which can be [used as application code](#runtime).

## Resources {#resources}

A resource is created with the following:

{{< langchoose >}}

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

All resources have a [`name`](#names), which must be unique in the Pulumi program.

The `args` provided to a resource determine what inputs will be used to initialize the resource.  These can typically be either raw values or [outputs from other resources](#outputs).

### Resource options {#resourceoptions}

All resource constructors also accept an `options` argument which can provide the following additional resource options controlling how the resource will be managed by Pulumi.

###### `additionalSecretOutputs`
Provides a list of output properties which should be treated as secrets. This value augments any values that Pulumi detects itself, based on what secret inputs to the resource has. This is typically used to express that for a specific instance of a resource, some of its output properties should be treated as secrets (when they would not normally be).

###### `aliases`
Provides a list of aliases for a resource or component. When making a breaking change to the name or type of a resource or component, you can add the old name to the list of `aliases` for a resource to ensure that existing resources will be migrated to the new name instead of being deleted and replaced with the new named resource. 

For example, a resource can be aliased to a full previous [resource URN](#urns):
 
`aliases: ["urn:pulumi:stackname::projectname::aws:s3/bucket:Bucket::app-function"]`

Or it can be aliased to a relative change to the resource's name, parent, and/or type: 

`aliases: [{ name: "otherchild", parent: this }]`

###### `customTimeouts`
Provides a set of custom timeouts for `create`, `update`, and `delete` operations on a resource. These timeouts can be specified as a string like "5m", "40s", or "1d" (5 minutes, 40 seconds, or 1 day, respectively). For example, `customTimeouts: { create: "1m" }`.

###### `deleteBeforeReplace`
Set this option to `true` to specify that replacements of the resource will delete the existing resource before creating its replacement.  This will lead to downtime during the replacement, but may be necessary for some resources that manage scarce resources behind the scenes.  The default is `false`.

###### `dependsOn`
Provides a list of explicit resource dependencies to add to the resource. Every resource referenced either directly or indirectly by an `Output` that is passed in to the resource constructor will implicitly be included, so this additional information is only needed when the dependency is on something that is not already an input to the resource. The default is `[]`.

###### `ignoreChanges`
Provides a list of properties which will be ignored as part of updates. The value of the property will be used for newly created resources, but will not be used as part of updates. This is typically used to avoid changes in properties leading to diffs or to change defaults for a property without forcing all existing deployed stacks to update or replace the affected resource.

###### `import`
The ID of an existing resource to import for Pulumi to manage. When set, Pulumi will read the current state of the resource with the given ID from the backing provider &ndash; AWS, Azure, GCP, or Kubernetes for example. The inputs to the resource's constructor must not differ from this state or the import will fail. Once a resource has been imported, this property should be unset.

###### `parent`
A parent for the resource. See [Components](#components).  The default is to parent to the implicitly-created `Stack` resource that is a root resource for all Pulumi stacks.

###### `protect`
Marks a resource as protected. A protected resource cannot be deleted directly: First, you must set `protect: false` and run `pulumi up`. Then, you can delete the resource by removing the line of code or by running `pulumi destroy`.  The default is to inherit this value from the parent resource, and `false` for resources without a parent.

###### `provider`
A provider for the resource. See [Providers](#providers).  The default is to inherit this value from the parent resource, and to use the ambient provider specified by Pulumi configuration for resources without a parent.

### Resource names {#names}

Every resource managed by Pulumi has a name.  This name is used to track the identity of a resource across multiple deployments of the same program.  The name specified during resource creation is used in three ways:

1. It is used as part of constructing the Universal Resource Name (URN) used by the Pulumi engine to track the resource across updates.
2. Most resource providers will use it as a default prefix for constructing the cloud-provider name of the resource.
3. Some CLI commands use the URN.

#### URNs {#urns}

The URN of a resource is constructed from the name provided by the resource, the type of the resource, and the types of all the parent component resources.  It also includes information about the project and stack.  For example:

```
urn:pulumi:thumbnailer-twitch::video-thumbnailer::cloud:bucket:Bucket$cloud:function:Function::onNewThumbnail
urn:pulumi:    <stackname>   ::  <projectname>  ::    <parenttype>   $     <resourcetype>    ::<resourcename>
```

> Note: It is likely that the format of the URN will be changed in the future to be simpler and more flexible.

Because it is used as the unique identity of a resource within a stack, this URN must be unique for each resource created by a single Pulumi program.  In particular, this requires that the resource name must be unique among resources of the same type with the same type of parent component.

Any change to the URN of a resource will cause the old and new resources to be treated as unrelated - the new one will be created (since it was not in the prior state) and the old one will be deleted (since it is not in the new desired state). This includes changing the `name` used to construct the resource or changing the parent of a resource.  Both of these operations will lead to a different URN, and thus to a `create` and a `delete` operation instead of an `update` or `replace` operation of the resource.  As a result, changes to names must be made with care.

Resources constructed as children of a [component](#components) should make sure that their names will be unique across multiple instances of the component.  In general, that means that the name of the component instance itself (the `name` parameter passed in to the component constructor) shoud be used as part of the name of the child resources.

#### Auto-naming {#autonaming}

The name of a resource is also used by many providers as a default prefix for constructing the cloud-provider name for the resource.  For example, constructing a `new aws.s3.Bucket("mybucket")` will result in an AWS bucket named something like `mybucket-eb24ea8`.

This random postfix is added by default for two reasons.  First, it ensures that two instances of a program can be deployed to the same environment without risk of name collisions.  Second, it ensures that it will be possible to do zero-downtime replacements when needed, by creating the new resource first, updating any references to point to it, and then deleting the old resource.

In cases where the two proprties above are not required, and where it would be useful to be able to precisely specify the name, it is typically possible to provide a `name: ` argument to the resource inputs to specify an explicit cloud-provider name.  For resources that may need to be replaced, this will often require also specifying `deleteBeforeReplace: true` in the resources's `ResourceOptions`.

#### Resource get (#resource-get)

A `get` method is available on any resource, which reads in the current value of an existing resource.  The shape it returns corresponds to the type of the resource.

## Outputs and Inputs {#outputs}

Outputs are a key part of how Pulumi tracks dependencies between resources.  Because the values of Outputs are not available until resources are created, these are represented using the special [`Output`][pulumi.Output] type, which internally represents two things:

1. An eventually available value of the output
2. The dependency on the source(s) of the output value

In fact, `Output`s are similar to promises/futures that you may be familiar with from other programming models. Additionally, they carry along dependency information.

The output properties of all resource objects in Pulumi have type [`Output`][pulumi.Output].

Resource inputs have type [`Input`][pulumi.Input], which accepts either a raw value, a `Promise`, or an output from another resource. This allows dependencies to be inferred, including ensuring that resources are not created or updated until all their dependencies are available and up to date.

##### Apply {#apply}

To transform an output into a new value, use the [`apply` method]({{< relref "pkg/nodejs/pulumi/pulumi/#OutputInstance-apply" >}}). For example, use the following to create an HTTPS URL from the DNS name of a virtual machine:

{{< langchoose >}}

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

The `apply` method accepts a callback which will be passed the value of the `Output` when it is available, and which returns the new value.  The result of the call to `apply` is a new `Output` whose value is the value returned from the callback, and which includes the dependencies of the original `Output`.  If the callback itself returns an `Output`, the dependencies of that output are unioned into the dependencies of the returned `Output`.

> _Note_: Several common types of transformations can be done more convienently.  See [Accessing properties of an Output](#lifting) for how to access Output value properties simply.   Also, `Output` itself cannot be used directly in string concatenation as it is not itself the value of the output.  See (Working with Outputs and strings)[#ouputs-and-strings] for examples of how to more simply work use the two together.  For cases where these convenience forms are not sufficient, `.apply` is available the most general way to transform one `Output` into another.

##### Accessing properties of an Output {#lifting}

It is common to need to only access some property of the value of an `Output` in order to pass in that property to another `Resource`.  For example, when using ACM certificates one might write:

{{< langchoose >}}

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

To make this kind of property and array-element access more simple, an `Output` 'lifts' the properties of the value that is wrapped, allowing you to access them directly off of the `Output` itself.  This allows the above to be more simply written as:

{{< langchoose >}}

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

This helps the clarity of the final code, while not losing any important dependency information that is needed for properly creating and maintaining the stack.

##### All {#all}

To combine multiple `Output`s into a transformed value, use [pulumi.all].  This allows a new value to be constructed from several inputs, such as concatenating outputs from two different resources together, or constructing a policy document using information from several other resources.

{{< langchoose >}}

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

##### Convert Input to Output {#frominput}

To turn an `Input` into an `Output`, use [pulumi.output].  This can be useful when you want to transform an input value that could either be a raw value or an `Output`:

{{< langchoose >}}

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

##### Working with Outputs and strings {#outputs-and-strings}

It's very common to want to build a string out of the values contained in `Outputs`.  Common uses for this are to either provide a custom [stack output](#stack-outputs), or to provide a dynamically computed string as an [Input]({{< relref "pkg/nodejs/pulumi/pulumi#Input" >}}) to another Resource.  For example, say you had the following:

{{< langchoose >}}

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
# Helpers for combining Outputs into strings are not yet available in Python.
#
# See https://github.com/pulumi/pulumi/issues/2366.
```

```go
// Helpers for combining Outputs into strings are not yet available in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

Using [.apply](#apply) and [.all](#all) this could be solved as shown above like so:

```javascript
const url = pulumi.all([hostname, port]).apply(([hostname, port]) => `http://${hostname}:${port}/`);
```

```typescript
const url: Output<string> = pulumi.all([hostname, port]).apply(([hostname, port]) => `http://${hostname}:${port}/`);
```

```python
# Helpers for combining Outputs into strings are not yet available in Python.
#
# See https://github.com/pulumi/pulumi/issues/2366.
```

```go
// Helpers for combining Outputs into strings are not yet available in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

However, this is quite verbose and unwieldy.  To make this easier, Pulumi exposes two helpers `concat` and `interpolate`  to make this more convenient.  They can be used as follows:

```javascript
const url1 = pulumi.concat("http://", hostname, ":", port, "/");
const url2 = pulumi.interpolate `http://${hostname}:${port}/`;
```

```typescript
const url1: Output<string> = pulumi.concat("http://", hostname, ":", port, "/");
const url2: Output<string> = pulumi.interpolate `http://${hostname}:${port}/`;
```

```python
# Helpers for combining Outputs into strings are not yet available in Python.
#
# See https://github.com/pulumi/pulumi/issues/2366.
```

```go
// Helpers for combining Outputs into strings are not yet available in Go.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

`concat` takes a list of arguments that can be `Inputs`, `Outputs`, `Promises` and simple JavaScript values, and creates an `Output` with all their underlying values concatenated together.  `interpolate` does the same, but allows you to use a JavaScript `template literal` if that's your preferred way of combining values into strings.

## Secrets {#secrets}

When constructing resources, Pulumi will record all inputs and outputs from a resource it is state file.  Some of these properties may contain sensitive data, which should be encrypted before being stored in the state file. For example, consider the following program which creates an AWS Parameter Store parameter.

{{< langchoose >}}

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
// Secrets are not yet avaiaible in Go.
//
// See https://github.com/pulumi/pulumi/issues/2820
```

As written, the state file for this program will show the plaintext value of the "my-secret-value" configuration variable as an input to the `Parameter` resource.  Pulumi provides a way to mark a value as "secret" such that if it stored in the state file, it will be encrypted in the same way secret configuration values are.  There are two ways to create secret values:

1. By calling `requireSecret` or `getSecret` (JavaScript) or `require_secret` or `get_secret` (Python) when reading a value from config.
2. Using `pulumi.secret` (JavaScript) or `Output.secret` (Python) to construct a secret from an existing value.

We can change the above code to look like the following:

{{< langchoose >}}

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

In which case the value property of the `Parameter` resource will now be encrypted in the state file.

Secrets behave just like normal `Output`'s in Pulumi (in fact, their type is simply `Output`), except they are marked internally as needed to be encrypted before being persisted in the state file. When you combine an existing Output that is marked as a secret (either via `apply` or `all`) with out values, the resulting Output is also marked as a secret.

> __Note__: During an `apply` you have access to the raw value of the underlying secret.  While Pulumi ensures that the value returned from an `apply` is marked as secret, it can not enforce that any work done inside the `apply` itself will not leak the secret value.  For example, inside an apply you could explicitly make a call to print the value to the console or save it to a file. Becasue of this, care must be taken inside the apply to ensure your code does not cause the value to be leaked.

Unlike regular Outputs, secret outputs cannot be captured by Pulumi closure serialization system and attempting to do so will lead to an exception. We do plan to support this once we can ensure the values will be persisted securely (see [pulumi/pulumi#2718](https://github.com/pulumi/pulumi/issues/2718)).

While Pulumi ensures that any outputs of a resource which have coresponding secret inputs are marked as secrets, there may be additional outputs that you wish to mark as secrets. In this case, you can pass the `additionalSecretOutputs` (JavaScript) or `additional_secret_outputs` (Python) option when creating a resource to ensure these extra output values are encrypted before being stored in the state file.

## Stack output {#stack-outputs}

A [stack output]({{< relref "stack.md#outputs" >}}) is a value exported from a stack. A stack's outputs can be easily retrieved from the Pulumi CLI and is displayed on pulumi.com. To export values from a stack, use the following definition in the top-level of the entry point for your project:

{{< langchoose >}}

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

From the CLI, you can then use `pulumi stack output url` to get the value and incorporate into other scripts or tools.

The right-hand side of a stack export can be a regular JavaScript value, an [Output](#outputs), or a `Promise`. The actual value will be resolved at the end of `pulumi up`.

Stack exports are JSON serialized, though quotes are removed when exporting just a string value. For example:

{{< langchoose >}}

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

If a stack contains any output values which are marked as secrets, their values will not be shown by default (instead they will be displayed as `[secret]` in the CLI). You may pass `--show-secrets` to `pulumi stack output` to see the plaintext value.

## Config {#config}

To access configuration values that have been set with `pulumi config set`, use the following:

{{< langchoose >}}

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

Config values can be retrieved using [config.get] or [config.require].  Using `get` will return `undefined` if the configuration value was not provided, and `require` will raise an exception with a helpful error message to prevent the deployment from continuing.

Configuration values are always stored as strings, but can be parsed as richly typed values.  For example, [config.getNumber] will convert the string value to a number and return a `Number` value instead of a string.  It will raise an exception if the value cannot be parsed as a number.

For richer structured data, the [config.getObject] method can be used to parse JSON values.  For example, following `pulumi config set data '{"active": true, "nums": [1,2,3]}'`, a program can read the `data` config into a rich object with:

{{< langchoose >}}

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
# JSON parsing helpers for config are not built-in for Python currently.
#
# See https://github.com/pulumi/pulumi/issues/1535.
```

```go
// JSON parsing helpers for config are not built-in for Go currently.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

The `Config` object also provides functions to get the value from configuration and mark it as a secret. See [config.getSecret] or [config.requireSecret].  Unlike the [config.get] and [config.require], these methods return an `Output<T>` which holds the underlying value and ensures that it is encrypted when it is being persisted.

## Components {#components}

A Pulumi **component** is a logical group of resources that contains other components and physical cloud resources. A Pulumi stack is itself a component that contains all top-level components and resources in a program.

To create a new component, either in a top-level program or in a library, create a subclass of [pulumi.ComponentResource]. Components provide a way to create reusable abstractions made up of other resources.

Here's a simple component definition:

{{< langchoose >}}

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
// ComponentResources are not directly supported in Go currently.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

The call to `super` registers the component instance with the Pulumi engine. This records the resource in the checkpoint and tracks it across program deployments. Since all resources must have a name, a component constructor should accept a name and pass it to `super`.

A component must register a namespace, such as `pkg:MyResource` in the example above. To reduce the potential of name conflicts, this name should contain the package name and resource type, such as `aws:lambda:Function`. The format `<package>:<module>:<type>` is typically used, though not currently fully enforced.

Components will often contain child resources. To track this relationship, pass the component instance as the parent when constructing a resource:

{{< langchoose >}}

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

Components can define their own properties using [registerOutputs]. The Pulumi engine uses this information to display the logical outputs of the component.  The call to `registerOutputs` also tells Pulumi that the resource is done registering children and should be considered fully constructed, so it is recommended that this method be called in all components even if no outputs need to be registered.


{{< langchoose >}}

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
// ComponentResources are not directly supported in Go currently.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

In addition to the usual resource options, components accept a set of [providers](#providers) to use for their child resources. If a component is itself a child of another component, its set of providers is inherited from its parent by default.

{{< langchoose >}}

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
// ComponentResources are not directly supported in Go currently.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

For more information about components, see the [Pulumi Components]({{< relref "component-tutorial.md" >}}) tutorial.

## Providers {#providers}

A [CustomResource][pulumi.CustomResource] needs an associated resource provider to manage its Create, Read, Update, and Delete (_CRUD_) operations. This is in contrast to a [ComponentResource][pulumi.ComponentResource], whose logic is authored entirely in a Pulumi program's source language (e.g. Javascript or Python). By default, a `CustomResource`'s provider is determined based on its [package](#packages). This default provider is automatically created by Pulumi, and is configured using its package's [config values](#config). For example, the configuration and program below will create a single EC2 instance in the `us-west-2` region.

{{< langchoose >}}

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
// Providers are not supported in Go currently.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```


```bash
$ pulumi config set aws:region us-west-2
```

While this works for the majority of Pulumi programs, some programs may have special requirements (e.g. the ability to deploy into multiple AWS regions simultaneously or to deploy into a Kubernetes cluster created earlier in the program) that require explicitly creating, configuring, and referencing providers. This is typically done by instantiating the relevant package's `Provider` type and passing it in the options for each `CustomResource` or `ComponentResource` that needs to use it. For example, the configuration and program below will create an ACM certificate in the `us-east-1` region and a load balancer listener in the `us-west-2` region.

{{< langchoose >}}

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
let listener = new aws.elasticloadbalancingv2.Listener("listener", {
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
let listener = new aws.elasticloadbalancingv2.Listener("listener", {
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
listener = aws.elasticloadbalancingv2.Listener("listener",
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
// Providers are not supported in Go currently.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

```bash
$ pulumi config set aws:region us-west-2
```

Component resources also accept a set of providers to use with their child resources. For example, the EC2 instance parented to `myResource` in the program below will be created in `us-east-1`, and the Kubernetes pod parented to `myResource` will be created in the cluster targeted by the "test-ci" context.

{{< langchoose >}}

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
// Providers are not supported in Go currently.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

## Dynamic Providers {#dynamicproviders}

Every `CustomResource` has a provider associated with it which knows how to create/read/update/delete instances of the custom resource in the backing cloud provider.  This provider can be defined by implementing the Pulumi Resource Provider gRPC interface.  There are generally two approaches to implementing this provider interface:

1. Create a provider binary with the appropriate name and put it on the path, such that it will be loaded to handle CRUD operations from the Pulumi engine on resources from the package it is defined to handle.  For example the `pulumi-resource-aws` binary will handle resources from the `aws` package.  This binary can be authored in any language, but must be authored and distributed out of band of a Pulumi program.
2. Define an implementation of the Provider interface directly within your Pulumi program, just for use within that program.

The former is used for most common Pulumi providers like AWS and Kubernetes.  The latter is a concept called Dynamic Providers, which provide a flexible approach to defining custom resource types directly within the source code of your Pulumi program.

You should consider implementing a dynamic provider in a few cases:

1. You need to manage a cloud resource for which there is not yet a published Pulumi Provider, but you expect to only use it from within one program.  (If you expect to use it from many programs, and in many languages, implementing a full provider is preferrable.)
2. You need to integrate custom logic into the deployment workflow that runs exactly during one or more of the create, read, update or delete steps - instead of running "always" as part of a normal Pulumi program.

Dynamic Providers are defined by first implementing the `pulumi.dynamic.ResourceProvider` interface, including the `create`, `read`, `update` and `delete` operations for your resource, as well as `check` and `diff`.  Default implementations are provided for everything except `create`, so a minimal implementation could look like:

{{< langchoose >}}

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
# Dynamic Providers are not supported in Python currently.
```

```go
// Dynamic Providers are not supported in Go currently.
```

This resource provider is then used to create a new kind of custom resource by inheriting from the `pulumi.dynamic.Resource` base class (a subclass of `pulumi.CustomResource`).

{{< langchoose >}}

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
# Dynamic Providers are not supported in Python currently.
```

```go
// Dynamic Providers are not supported in Go currently.
```

We can now create instances of the new `MyResource` resource kind in our program with `new MyRresource("name", args)`.  When we do so, if Pulumi determines the resource has not yet been created, it will call the `create` method on the resource provider interface.  If another Pulumi deployment happens and the resource already exists, Pulumi will call the `diff` method to determine whether a change can be made in place or whether a replacement is needed.  If a replacement is needed, Pulumi will call `create` for the new resource and then `delete` for the old resource.  If no repacement is needed, Pulumi will call `update`.  In all cases, before doing anything else, Pulumi will call the `check` method with the resource arguments to give the provider a chance to validate that the arguments are valid.  And finally, if Pulumi needs to read an existing resource without managing it directly, it will call `read`.

> _Note_: Dynamic Providers are a flexible and low-level mechanism to plug arbitrary code directly into the deployment process.  Whereas most code in a Pulumi program runs as part of constructing the desired state of resources (the "resource graph"), the code inside the dynamic provider resource provider interface implementations (`create`, `update`, etc.) runs instead during resource provisioning (while the resource graph is being turned into a set of CRUD operations scheduled against the cloud providers).  In fact, these two phases of execution actually run in completely seperate processes.  The construction of a `new MyResource` happens inside the JavaScript/Python/Go process that's running your Pulumi program.  But your implementations of `create` or `update` are executed by a special resource provider binary called `pulumi-resource-pulumi-nodejs`.  This binary is what actually implements the Pulumi resource provider gRPC interface and speaks directly to the Pulumi engine. Because your implementation of the resource provider interface must be used by a different process, potentialy at a different point in time, dynamic providers are built on top of the same [function serialization]({{< relref "serializing-functions.md" >}}) that is used for turning callbacks into AWS Lambdas or Google Cloud Functions.  Because of this serialization, there are some limits on what can be done inside the implementation of the resource provider interface, which you can read more about in the function serialization documentation.

### Dynamic Resource Inputs

A dynamic provider interfaces with other components via subclasses of `pulumi.dynamic.Resource`. The inputs to a dynamic provider's implementation are provided via a instantiation of such a subclass; this is the `props` parameter in the constructor in the example below. Any properties you set in the `props` object will be passed to your `pulumi.dynamic.ResourceProvider` functions as the `inputs` where appropriate.

> For statically typed languages, you can get rich type information for the inputs declaring an input type to make it easy to use your custom resource.

{{< langchoose >}}

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
# Dynamic Providers are not supported in Python currently.
```

```go
// Dynamic Providers are not supported in Go currently.
```

### Resource Provider Interface

Implementing the `pulumi.dynamic.ResourceProvider` interface requires implementing a subset of the methods below. Each of these methods may be asynchronous, and most implementations of these methods will perform network I/O to provision resources in a backing cloud provider or other resource model. There are several important contracts between a dynamic provider and the Pulumi CLI that inform when these methods are called and with what data.

Though the input properties passed to a `pulumi.dynamic.Resource` instance will usually be of type `pulumi.Input<T>` in order to compose well with other Pulumi resources, the dynamic provider's functions are invoked with the fully resolved input values. Strong typing for the inputs to your provider's functions can help clarify this; you can achieve this by creating a second interface with the same properties as your resource's inputs, but with fully unwrapped types.

{{< langchoose >}}

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
# Dynamic Providers are not supported in Python currently.
```

```go
// Dynamic Providers are not supported in Go currently.
```

##### `check(olds, news)`
Check is invoked before any other methods, and is passed the resolved input properties that were originally provided to the resource constructor by the user.  It is passed both the old input properties that were stored in the statefile after the previous update to the resource, as well as the new inputs from the current deployment.  It has two jobs: (1) to verify that the inputs (particularly the news) are valid and if not to return useful error messages and (2) to return a set of checked inputs.  The inputs returned from the call to `check` will be the inputs that the Pulumi engine uses for all further processing of the resource, including being the values that will be passed back in to `diff`, `create`, `update`, etc.  In many cases, the `news` can be returned dirctly as the checked inputs.  But in cases where the provider needs to populate defaults, or do some normalization on values, it may want to do that in the `check` method so that this data is complete and normalized prior to being passed into other methods.

##### `create(inputs)`
Create is invoked when the resource name (URN) of the resoruce created by the user is not found in the existing state of the deployment.  The engine passes the provider the checked inputs returned from the call to `check`.  The create method is expected to do the work in the backing cloud provider to create the requested resource.  It then returns two pieces of data: (1) an `id` that can uniquely identify the resource in the backing provider for ater lookups and (2) a set of `outputs` from the backing provider that should be returned to the user code as properties on the `CustomResource` object, and stored into the checkpoint file.  If an error occurs, an exception can be thrown from the `create` method to return this error to the user.

##### `diff(id, olds, news)`
Diff is invoked when the resource name (URN) of the resoruce created by the user is found in the existing state of the deployment. This means the resource already exists, and will need to be either updated or replaced.  The `diff` method is passed the `id` of the resource (as returned by `create`) as well as the old outputs from the checkpoint file (values returned from a previous call to either `create` or `update`).  It is also passed the new checked inputs from the current deployment.  It returns four things (all optional):

* `changes`: `true` if the provider believes there is a difference between the `olds` and `news` and wants to do an `update` or `replace` to affect this change.
* `replaces`: An array of property names that have changed that should force a replacement.  Returning a non-zero length array here will tell the Pulumi engine to scheduled a replacement instead of an update, which might involve downtime, so this should only be used when a diff requested by the user cannot be implemented as an in-place update on the backing cloud provider.
* `stables`: An array of property names that are known to not change between updates.  Pulumi will use this information to allow some `apply` calls on [Outputs]() to be processed during `previews` because it knows that the values of these will stay the same during an update.
* `deleteBeforeReplace`: `true` if the proposed replacements require deleteing the existing resource before creating the new one.  By default Pulumi will try to create the new resource before deleting the old one to avoid downtime.
If an error occurs, an exception can be thrown from the `diff` method to return this error to the user.

##### `update(id, olds, news)`
Update is invoked if the call to `diff` indicates replacement is not needed.  It is passed the the `id` of the resource (as returned by `create`) as well as the old outputs from the checkpoint file (values returned from a previous call to either `create` or `update`). It is also passed the new checked inputs from the current deployment.  The update method is expected to do the work in the backing cloud provider to update an existing resource to the new desired state.  It then returns a new set of `outputs` from the backing provider that should be returned to the user code as properties on the `CustomResource` object, and stored into the checkpoint file.  If an error occurs, an exception can be thrown from the `create` method to return this error to the user.

##### `delete(id, props)`
Delete is invoked if the resource name (URN) exists in the previous state but not in the new desired state, or if a replacement is needed.  It is passed the the `id` of the resource (as returned by `create`) as well as the old outputs from the checkpoint file (values returned from a previous call to either `create` or `update`).  It is expected to delete the corresponding resource from the backing cloud provider.  Nothing needs to be returned.  If an error occurs, an exception can be thrown from the `create` method to return this error to the user.

##### `read(id, props)`
Read is invoked when the Pulumi engine needs to get data about a resource that it is not managed by Pulumi.  It is passed the the `id` of the resource as tracked in the backing cloud provider as well as an optional bag of additional properties to use to disambiguate the request if needed. The `read` method is execpted to lookup the requested resource, and if found return the canonical `id` and output properties of this resource.  If an error occurs, an exception can be thrown from the `create` method to return this error to the user.

### Dynamic Resource Outputs

Any outputs can be returned by your `create` function in the `outs` property of `pulumi.dynamic.CreateResult`.

> The following only applies to **statically typed languages**.

If you need to access the outputs of your custom resource outside it with strong typing support, then declare each output property returned in the `outs` property by your `create` function as a class member of the `pulumi.dynamic.Resource` itself. For example, in TypeScript, these must be declared as `public readonly` class members in your `pulumi.dynamic.Resource` class. These class members must also have the type `pulumi.Output<T>`.

**Note** that the name of the class member must match the names of the output properties as returned by the `create` function.

{{< langchoose >}}

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

    async diff(id: string, oldOutputs: MyResourceProviderOutputs, newInputs: MyResourceProviderInputs): Promise<pulumi.dynamic.DiffResult> {
        ...
    }
    ...
}

export class MyResource extends pulumi.dynamic.Resource {
    public readonly myStringOutput: pulumi.Output<string>;
    public readonly myNumberOutput: pulumi.Output<number>;

    constructor(name: string, props: MyResourceInputs, opts?: pulumi.CustomResourceOptions) {
        super(myprovider, name, props, opts); 
    }
}
```

```python
# Dynamic Providers are not yet supported in Python.
```

```go
// Dynamic Providers are not yet supported in Go.
```

### Dynamic Provider Examples

#### Example: Random

This example highlights using dynamic providers to run some code only when a resource is created, and then to store the results of that in the checkpoint file so that this value is maintained across deployments of the resource.  In this case, there is no "backing cloud provider", just the checkpoint file serialization that persists data.  The result is a provider similar to the one provided in `@pulumi/random` (although that library has many more flags than this simple example):

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
# Dynamic Providers are not supported in Python currently.
```

```go
// Dynamic Providers are not supported in Go currently.
```

#### Example: GitHub Labels REST API

This example highlights making REST API calls to some backing provider (in this case the GitHub API) to perform CRUD operations.  Because the resource provider method implementations will be serialized and used in a different process, we keep all the work to initialize the REST client and make calls to it local to each function.


{{< langchoose >}}

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
# Dynamic Providers are not supported in Python currently.
```

```go
// Dynamic Providers are not supported in Go currently.
```

## Packages {#packages}

Pulumi packages are normal NPM or Python packages. They transitively depend on `@pulumi/pulumi` which defines how resources created by a Pulumi program will be communicated to the Pulumi engine.  This ability to register resources with the Pulumi engine is the only difference between a Pulumi package and any other NPM package.

Some Pulumi packages have a dependency on a [Resource Provider plugin]({{< relref "/docs/reference/cli/pulumi_plugin.md" >}}) which contains the implementation for how to Create, Read, Update and Delete resources defined by the package.  The [pulumi.CustomResource] base class is used to connect a JavaScript resource class with the resource provider it depends on for resource management.  Packages like [@pulumi/aws] and [@pulumi/kubernetes] define resources, such as `aws.ec2.Instance`, `kubernetes.Pod`, which are managed by the AWS and Kubernetes resource provider plugins. Packages such as [@pulumi/cloud] and [@pulumi/awsx] contain only higher-level component resources, which are not managed by a resource provider plugin.

## Runtime code {#runtime}

You can create libraries and components that allow the caller to pass in JavaScript callbacks to invoke at runtime. For example, you can create an AWS Lambda function (or an Azure Function) by providing a JavaScript callback to be used as its implementation.

{{< langchoose >}}

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
# Runtime code provided via callbacks are not supported in Python currently.
#
# See https://github.com/pulumi/pulumi/issues/1535.
```

```go
// Runtime code provided via callbacks are not supported in Go currently.
//
// See https://github.com/pulumi/pulumi/issues/1614.
```

Libraries which use JavaScript callbacks as inputs to be provided as source text to resource construction (like the Lambda that is created by the `onObjectCreated` function in the example above) are built on top of the [pulumi.runtime.serializeFunction] API, which takes as input a JavaScript `Function` object, and returns a `Promise` that contains the serialized form of that function.

When serializing a function to text, the following steps are taken:

1. Any captured variables referenced by the function are evaluated when the function is serialized.
2. The values of those variables are serialized.
3. When the values are objects, all properties and prototype chains are serialized.  When the values are functions, those functions are serialized by following these same steps.

For more details see the docs on [serializing functions]({{< relref "serializing-functions.md" >}}).

## Design Guidelines {#design-guidelines}

### OutputInstance.apply

It is recommended that the `func` argument of [OutputInstance.apply]({{< relref "pkg/nodejs/pulumi/pulumi/#OutputInstance-apply" >}}) not create any resources, as doing so can lead to the results of `pulumi preview` being wrong, as the `apply` callback will not get run during a preview (because the real outputs values aren't yet known until the resources are deployed), and therefore any resources created in the callback will not be seen during the `preview`.

However, you may have a scenario in which the actual value, such as an array of Outputs, is needed to create a resource but is not determined until the time of `pulumi update` and after part of the deployment has already happened (e.g. an array of [Nameservers]({{< relref "pkg/nodejs/pulumi/aws/route53#Zone-nameServers" >}})).  In that case, Pulumi lets you express this within the `apply`, but be cautioned that the preview may not include some changes to resources that are created (or later removed) from within the `apply`.

<!-- MARKDOWN LINKS -->
[pulumi.Resource]: {{< relref "pkg/nodejs/pulumi/pulumi#Resource" >}}
[pulumi.ComponentResource]: {{< relref "pkg/nodejs/pulumi/pulumi#ComponentResource" >}}
[pulumi.CustomResource]: {{< relref "pkg/nodejs/pulumi/pulumi#CustomResource" >}}
[pulumi.Output]: {{< relref "pkg/nodejs/pulumi/pulumi#Output" >}}
[pulumi.Input]: {{< relref "pkg/nodejs/pulumi/pulumi#Input" >}}
[@pulumi/pulumi]: {{< relref "pkg/nodejs/pulumi/pulumi" >}}
[@pulumi/aws]: {{< relref "pkg/nodejs/pulumi/aws" >}}
[@pulumi/kubernetes]: {{< relref "pkg/nodejs/pulumi/kubernetes" >}}
[@pulumi/cloud]: {{< relref "pkg/nodejs/pulumi/cloud" >}}
[@pulumi/awsx]: {{< relref "pkg/nodejs/pulumi/awsx" >}}

[pulumi.getStack]: {{< relref "pkg/nodejs/pulumi/pulumi#getStack" >}}
[pulumi.log]: {{< relref "pkg/nodejs/pulumi/pulumi/log/" >}}
[pulumi.runtime.serializeFunction]: {{< relref "pkg/nodejs/pulumi/pulumi/runtime#serializeFunction" >}}
[pulumi.output]: {{< relref "pkg/nodejs/pulumi/pulumi#output" >}}
[pulumi.all]: {{< relref "pkg/nodejs/pulumi/pulumi#all" >}}

[config.get]: {{< relref "pkg/nodejs/pulumi/pulumi#method-get" >}}
[config.require]: {{< relref "pkg/nodejs/pulumi/pulumi#method-require" >}}
[config.getNumber]: {{< relref "pkg/nodejs/pulumi/pulumi#method-getnumber" >}}
[config.getObject]: {{< relref "pkg/nodejs/pulumi/pulumi#method-getobject" >}}

[registerOutputs]: {{< relref "pkg/nodejs/pulumi/pulumi#method-registeroutputs" >}}
<!-- END LINKS -->
