---
title: "Programming Model"
---

{% include mini-toc.html %}

## Overview {#overview}

In Pulumi, [resources](#resources) are defined by allocating resource objects in a program, such as `new aws.ec2.Instance(...)`.  The first argument passed to the resource constructor is its `name`, which must be unique within the Pulumi program. To create dependencies between resources, just reference the [output properties](#outputs) of a resource. For example, this definition of an EC2 instance creates a dependency on a `SecurityGroup`:

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

Pulumi programs are authored in general purpose programming languages such as [JavaScript](javascript.html) or [Python](python.html). You can use any packages supported by the languages package manager, as well as [Pulumi packages](pkg/). 

When `pulumi update` is run, your Pulumi program is run and the Pulumi CLI determines the desired state of application resources. A Pulumi program can reference artifacts that have already been published (such as S3 objects or pre-built Docker images) or it can define application resources itself so that everything is versioned together. For example, if your program uses `cloud.Service` with a `build` step, or defines a Lambda for an S3 trigger, you're defining application code that is implicitly deployed during the `pulumi update`.

A Pulumi program is contained within a [project](project.html). In JavaScript, the `main` property of `package.json` defines the entry point for the Pulumi program. 

## @pulumi/pulumi Package {#pulumipulumi}

The [@pulumi/pulumi] package is the core library for working with the Pulumi planning engine. This package defines the following:
- Resources ([pulumi.Resource])
- External cloud platform resources ([pulumi.CustomResource])
- Components defined entirely in JavaScript ([pulumi.ComponentResource])

Dependencies between resources are encoded with [pulumi.Output](#outputs).

This package also provides the following helpers:
- [pulumi.getStack] to get information about the current stack 
- [pulumi.log] for logging deployment information
- [pulumi.runtime.serializeFunction] for turning JavaScript callbacks into data which can be [used as application code](#runtime).

## Creating resources {#resources}

A resource is created via `new Resource(name, args)` in JavaScript. All resources must have a name, which must be unique in the Pulumi program.

All resource constructors also accept a third argument which can provide the following additional properties. 
- `dependsOn` - a list of explicit resource dependencies
- `protect` - whether to mark a resource as protected. A protected resource cannot be deleted directly: first you must set `protect: false` and run `pulumi update`. Then, the resource can be deleted, either by removing the line of code or by running `pulumi destroy`.
- `parent` - optional parent for the resource. See [Components](#components).
- `provider` - optional provider for the resource. See [Providers](#providers).

## Resource outputs {#outputs}

Outputs are a key part of how Pulumi tracks dependencies between resources.  Because the values of Outputs are not available until resources are created, these are represented using a special [`Output`][pulumi.Output] type which internally represents two things:
1. An eventually available value of the output
2. The dependency on the source(s) of the output value

In fact, `Output`s are similar to promises/futures that you may be familiar with from other programming models but also carry along dependency information.

The output properties of all resource objects in Pulumi have type [`Output`][pulumi.Output]. Resource inputs have type [`Input`][pulumi.Input], which accepts either a raw value, a `Promise`, or an output from another resource. This allows dependencies to be inferred, including ensuring that resources are not created or updatred until all their dependencies are availabe and up to date.  

#### Apply {#apply}

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

The `apply` method accepts a callback which will be passed the value of the `Output` when it is availabe, and which returns the new value.  The result of the call to `apply` is new `Output` whose value is the value returned from the callback, and which includes the dependencies of the original `Output`.  If the callback itself returns an `Output`, the dependencies of that output are unioned into the dependencies of the returned `Output`.

> Note: The `Output` itself cannot be used directly in string concatenation or other operations, as it is not itself the value of the output.  To transform the value of the output (when it becomes available), the `apply` method should be used instead.

#### All {#all}

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
# `all` is not yet available in Python
#
# See https://github.com/pulumi/pulumi/issues/2284.
```

```go
// `all` is not yet available in Go.
// 
// See https://github.com/pulumi/pulumi/issues/1614.
```

#### Convert Input to Output {#frominput}

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
    output.apply(lambda v: v.split());
}
```

```go
// Helpers for converting Inputs to Outputs are not yet available in Go.
// 
// See https://github.com/pulumi/pulumi/issues/1614.
```

#### Working with Outputs and strings {#ouputs-and-strings}

It's very common want to build a string to use out of the values contained in `Outputs`.  Common uses for this are to either provide a custom [stack output](#stack-outputs), or to provide a dynamically computed string as an [Input](https://pulumi.io/reference/pkg/nodejs/@pulumi/pulumi/#Input) to another Resource.  For example, say you had the following:

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

A [stack output](stack.html#outputs) is a value that can be easily retrieved from the Pulumi CLI and is displayed on pulumi.com. To export values from a stack, use the following definition in the top-level of the entry point for your project:

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

## Using configuration values {#config}

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

Configuration values are always stored as strings, but can be parsed as richly typed values.  For example, [config.getNumer] will convert the string value to a number and return a `Number`value instead of a string.  It will raise an exception if the value cannot be parsed as a number. 

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

A Pulumi **component** is a logical group of resources which contains other components and physical cloud resources. A Pulumi stack is itself a component that contains all top-level components and resources in a program. 

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
# Providers are not supported in Python currently.
#
# See https://github.com/pulumi/pulumi/issues/1535.
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
# Providers are not supported in Python currently.
#
# See https://github.com/pulumi/pulumi/issues/1535.
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
});
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
# Providers are not supported in Python currently.
#
# See https://github.com/pulumi/pulumi/issues/1535.
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
# Providers are not supported in Python currently.
#
# See https://github.com/pulumi/pulumi/issues/1535.
```

```go
// Providers are not supported in Go currently.
// 
// See https://github.com/pulumi/pulumi/issues/1614.
```

## Packages {#packages}

Pulumi packages are normal NPM or Python packages. They transitively depend on `@pulumi/pulumi` which defines how resources created by a Pulumi program will be communicated to the Pulumi engine.  This ability to register resources with the Pulumi engine is the only difference between a Pulumi package and any other NPM package.

Some Pulumi packages have a dependency on a [Resource Provider plugin](/reference/cli/pulumi_plugin.html) which contains the implementation for how to Create, Read, Update and Delete resources defined by the package.  The [pulumi.CustomResource] base class is used to connect a JavaScript resource class with the resource provider it depends on for resource management.  Packages like [@pulumi/aws] and [@pulumi/kubernetes] define resources, such as `aws.ec2.Intance`, `kubernetes.Pod`, which are managed by the AWS and Kubernetes resource provider plugins. Packages such as [@pulumi/cloud] and [@pulumi/aws-infra] contain only higher-level component resources, which are not managed by a resource provider plugin.

## Runtime code {#runtime}

You can create libraries and components that allow the caller to pass in JavaScript callbacks to invoke at runtime. For example, a JavaScript callback could be used as the implementation of an AWS Lambda function. 

{% include langchoose.html %}

```javascript
let bucket = new aws.s3.Bucket("mybucket");
bucket.onObjectCreated("onObject", async (ev) => {
    // This callback will be invoked at runtime any time an object is added to the bucket.
    console.log(JSON.stringify(ev));
});
```

```typescript
let bucket = new aws.s3.Bucket("mybucket");
bucket.onObjectCreated("onObject", async (ev: aws.s3.BucketEvent) => {
    // This callback will be invoked at runtime any time an object is added to the bucket.
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
