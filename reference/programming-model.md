---
title: "Programming Model"
---

{% include mini-toc.html %}

## Overview {#overview}

In Pulumi, [resources](#resources) are defined by allocating resource objects in a [program](#programs), such as `new aws.ec2.Instance(...)`.  The first argument passed to the resource constructor is its `name`, which must be unique within the Pulumi program. To create dependencies between resources, just reference the [output properties](#outputs) of a resource. For example, this definition of an EC2 instance creates a dependency on a `SecurityGroup`:

{% include langchoose.html %}

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

Pulumi programs are authored in general purpose programming languages such as [JavaScript](javascript.html) or [Python](python.html). You can use any packages supported by the language's package manager, as well as [Pulumi packages](pkg/). 

When `pulumi update` is run, your Pulumi program is run and the Pulumi CLI determines the desired state of application resources. A Pulumi program can reference artifacts that have already been published (such as S3 objects or pre-built Docker images) or it can define application resources itself so that everything is versioned together. For example, if your program uses `cloud.Service` with a `build` step, or defines a Lambda for an S3 trigger, you're defining application code that is implicitly deployed during the `pulumi update`.

A Pulumi program is contained within a [project](project.html). In JavaScript, the `main` property of `package.json` defines the entry point for the Pulumi program. 

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

{% include langchoose.html %}

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

###### `dependsOn`
Optionally provides a list of explicit resource dependencies to add to the implicit dependencies from inputs to the resource.  Every resource referenced directly or indirectly by an `Output` passed in to the resource constructor will implicitly be included, so this is only needed when the dependency is on something that is not already an input to the resource.  The default is `[]`.

###### `protect`
Optionally marks a resource as protected. A protected resource cannot be deleted directly: first you must set `protect: false` and run `pulumi update`. Then, the resource can be deleted, either by removing the line of code or by running `pulumi destroy`.  The default is to inherit this value from the parent resource, and `false` for resources without a parent.

###### `parent`
Optional parent for the resource. See [Components](#components).  The default is to parent to the implicitly-created `Stack` resource that is a root resource for all Pulumi stacks.

###### `provider`
Optional provider for the resource. See [Providers](#providers).  The default is to inherit this value from the parent resource, and to use the ambient provider specified by Pulumi configuration for resources without a parent.

###### `deleteBeforeReplace`
Optionally specify that replacements of the resource will delete the existing resource before creating it's replacement.  This will lead to downtime during the replacement, but may be necessary for some resources that manage scarce resources behind the scenes.  The default is `false`.

### Resource names {#names}

Every resource managed by Pulumi has a name.  This name is used to track the identity of a resource across multiple deployments of the same program.  The name that is specified when a resource is created is used in two ways:
1. It is used as part of constructing the Universal Resource Name (URN) used by the Pulumi engine to track the resource across updates.
2. Most resource providers will use it as a default prefix for constructing the cloud-provider name of the resource.

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

## Outputs {#outputs}

Outputs are a key part of how Pulumi tracks dependencies between resources.  Because the values of Outputs are not available until resources are created, they are represented using a special [`Output`][pulumi.Output] type which internally represents two things:
1. An eventually available value of the output
2. The dependency on the source(s) of the output value

In fact, `Output`s are similar to promises/futures that you may be familiar with from other programming models but also carry along dependency information.

The output properties of all resource objects in Pulumi have type [`Output`][pulumi.Output]. Resource inputs have type [`Input`][pulumi.Input], which accepts either a raw value, a `Promise`, or an output from another resource. This allows dependencies to be inferred, including ensuring that resources are not created or updated until all their dependencies are available and up to date.

##### Apply {#apply}

To transform an output into a new value, use the [`apply` method](pkg/nodejs/@pulumi/pulumi/#property-apply). For example, use the following to create an HTTPS URL from the DNS name of a virtual machine: 

{% include langchoose.html %}

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

> Note: Several common types of transformations can be done more convienently.  See (Accessing properties of an Output)[#lifting] for how to access Output value properties simply.   Also, `Output` itself cannot be used directly in string concatenation as it is not itself the value of the output.  See (Working with Outputs and strings)[#ouputs-and-strings] for examples of how to more simply work use the two together.  For cases where these convenience forms are not sufficient, `.apply` is available the most general way to transform one `Output` into another.  


##### Accessing properties of an Output {#lifting}

It is common to need to only access some property of the value of an `Output` in order to pass in that property to another `Resource`.  For example, when using ACM certificates one might write:

{% include langchoose.html %}

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

{% include langchoose.html %}

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

{% include langchoose.html %}

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

{% include langchoose.html %}

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

##### Working with Outputs and strings {#ouputs-and-strings}

It's very common to want to build a string out of the values contained in `Outputs`.  Common uses for this are to either provide a custom [stack output](#stack-outputs), or to provide a dynamically computed string as an [Input](https://pulumi.io/reference/pkg/nodejs/@pulumi/pulumi/#Input) to another Resource.  For example, say you had the following:

{% include langchoose.html %}

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

## Stack output {#stack-outputs}

A [stack output](stack.html#outputs) is a value exported from a stack. A stack's outputs can be easily retrieved from the Pulumi CLI and is displayed on pulumi.com. To export values from a stack, use the following definition in the top-level of the entry point for your project:

{% include langchoose.html %}

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

The right-hand side of a stack export can be a regular JavaScript value, an [Output](#outputs), or a `Promise`. The actual value will be resolved at the end of `pulumi update`.

Stack exports are JSON serialized, though quotes are removed when exporting just a string value. For example:

{% include langchoose.html %}

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

## Config {#config}

To access configuration values that have been set with `pulumi config set`, use the following:

{% include langchoose.html %}

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

{% include langchoose.html %}

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

## Components {#components}

A Pulumi **component** is a logical group of resources that contains other components and physical cloud resources. A Pulumi stack is itself a component that contains all top-level components and resources in a program. 

To create a new component, either in a top-level program or in a library, create a subclass of [pulumi.ComponentResource]. Components provide a way to create reusable abstractions made up of other resources.

Here's a simple component definition:

{% include langchoose.html %}

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
class MyResource(ComponentResource):
    def __init__(self, name, opts = None):
        super(MyResource, self).__init__('pkg:MyResource', name, None, opts)
```

```go
// ComponentResources are not directly supported in Go currently.
// 
// See https://github.com/pulumi/pulumi/issues/1614.
```

The call to `super` registers the component instance with the Pulumi engine. This records the resource in the checkpoint and tracks it across program deployments. Since all resources must have a name, a component constructor should accept a name and pass it to `super`.

A component must register a namespace, such as `pkg:MyResource` in the example above. To reduce the potential of name conflicts, this name should contain the package name and resource type, such as `aws:lambda:Function`. The format `<package>:<module>:<type>` is typically used, though not currently fully enforced.

Components will often contain child resources. To track this relationship, pass the component instance as the parent when constructing a resource:

{% include langchoose.html %}

```javascript
let bucket = new aws.s3.Bucket(`${name}-bucket`, {}, { parent: this });
```

```typescript
let bucket = new aws.s3.Bucket(`${name}-bucket`, {}, { parent: this });
```

```python
bucket = s3.Bucket(f"{name}-bucket", __opts__=ResourceOptions(parent=self))
```

```go
bucket := s3.Bucket(ctx, fmt.Sprintf("%s-bucket", name), &s3.BucketArgs{}, pulumi.ResourceOpt{Parent: parent});
```

Components can define their own properties using [registerOutputs]. The Pulumi engine uses this information to display the logical outputs of the component.  The call to `registerOutputs` also tells Pulumi that the resource is done registering children and should be considered fully constructed, so it is recommended that this method be called in all components even if no outputs need to be registered.


{% include langchoose.html %}

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

{% include langchoose.html %}

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

For more information about components, see the [Pulumi Components](component-tutorial.html) tutorial.

## Providers {#providers}

A [CustomResource][pulumi.CustomResource] needs an associated resource provider to manage its Create, Read, Update, and Delete (_CRUD_) operations. This is in contrast to a [ComponentResource][pulumi.ComponentResource], whose logic is authored entirely in a Pulumi program's source language (e.g. Javascript or Python). By default, a `CustomResource`'s provider is determined based on its [package](#packages). This default provider is automatically created by Pulumi, and is configured using its package's [config values](#config). For example, the configuration and program below will create a single EC2 instance in the `us-west-2` region.

{% include langchoose.html %}

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

{% include langchoose.html %}

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

{% include langchoose.html %}

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

## Packages {#packages}

Pulumi packages are normal NPM or Python packages. They transitively depend on `@pulumi/pulumi` which defines how resources created by a Pulumi program will be communicated to the Pulumi engine.  This ability to register resources with the Pulumi engine is the only difference between a Pulumi package and any other NPM package.

Some Pulumi packages have a dependency on a [Resource Provider plugin](/reference/cli/pulumi_plugin.html) which contains the implementation for how to Create, Read, Update and Delete resources defined by the package.  The [pulumi.CustomResource] base class is used to connect a JavaScript resource class with the resource provider it depends on for resource management.  Packages like [@pulumi/aws] and [@pulumi/kubernetes] define resources, such as `aws.ec2.Instance`, `kubernetes.Pod`, which are managed by the AWS and Kubernetes resource provider plugins. Packages such as [@pulumi/cloud] and [@pulumi/aws-infra] contain only higher-level component resources, which are not managed by a resource provider plugin.

## Runtime code {#runtime}

You can create libraries and components that allow the caller to pass in JavaScript callbacks to invoke at runtime. For example, you can create an AWS Lambda function (or an Azure Function) by providing a JavaScript callback to be used as its implementation. 

{% include langchoose.html %}

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

For more details see the docs on [serializing functions](serializing-functions.html).

<!-- MARKDOWN LINKS -->
[pulumi.Resource]: pkg/nodejs/@pulumi/pulumi/#Resource
[pulumi.ComponentResource]: pkg/nodejs/@pulumi/pulumi/#ComponentResource
[pulumi.CustomResource]: pkg/nodejs/@pulumi/pulumi/#CustomResource
[pulumi.Output]: pkg/nodejs/@pulumi/pulumi/#Output
[pulumi.Input]: pkg/nodejs/@pulumi/pulumi/#Input
[@pulumi/pulumi]: pkg/nodejs/@pulumi/pulumi
[@pulumi/aws]: pkg/nodejs/@pulumi/aws
[@pulumi/kubernetes]: pkg/nodejs/@pulumi/kubernetes/
[@pulumi/cloud]: pkg/nodejs/@pulumi/cloud
[@pulumi/aws-infra]: pkg/nodejs/@pulumi/aws-infra

[pulumi.getStack]: pkg/nodejs/@pulumi/pulumi/#getStack
[pulumi.log]: pkg/nodejs/@pulumi/pulumi/log/
[pulumi.runtime.serializeFunction]: pkg/nodejs/@pulumi/pulumi/runtime/#serializeFunction
[pulumi.output]: pkg/nodejs/@pulumi/pulumi/#output
[pulumi.all]: pkg/nodejs/@pulumi/pulumi/#all

[config.get]: pkg/nodejs/@pulumi/pulumi/#method-get
[config.require]: pkg/nodejs/@pulumi/pulumi/#method-require
[config.getNumber]: pkg/nodejs/@pulumi/pulumi/#method-getnumber
[config.getObject]: pkg/nodejs/@pulumi/pulumi/#method-getobject

[registerOutputs]: pkg/nodejs/@pulumi/pulumi/#method-registeroutputs
<!-- END LINKS -->
