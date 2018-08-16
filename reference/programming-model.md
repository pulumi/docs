---
title: "Programming Model"
---

In Pulumi, [resources](programming-model.html#resources) are defined by allocating resource objects in a program, such as `new aws.ec2.Instance(...)`.  The first argument passed to the resource constructor is its `name`, which must be unique within the Pulumi program. To create dependencies between resources, just reference the [output properties](#outputs) of a resource. For example, this definition of an EC2 instance creates a dependency on a `SecurityGroup`:


```js
let group = new aws.ec2.SecurityGroup(...);

let server = new aws.ec2.Instance("webserver-www", {
    ...
    securityGroups: [ group.name ], // reference the security group resource above
});
```

To publish values that you wish to access outside your application, create a [stack output](#stack-outputs) via module exports. 

In Pulumi, you can group multiple resources in a [component](#components). A component is a logical container for physical cloud resources and affects how resources are grouped in the CLI and the pulumi.com console. 

## Programs {#programs}

Pulumi programs are authored in JavaScript or Python. You can use any packages supported by the languages package manager, as well as [Pulumi packages](pkg/). 

When `pulumi update` is run, your Pulumi program is run in either Node.js or Python and the Pulumi CLI determines the desired state of application resources. A Pulumi program can reference artifacts that have already been published (such as S3 objects or pre-built Docker images) or it can define application resources itself so that everything is versioned together. For example, if your program uses `cloud.Service` with a `build` step, or defines a Lambda for an S3 trigger, you're defining application code that is implicitly deployed during the `pulumi update`.

A Pulumi program is contained within a [project](project.html). In JavaScript, the `main` property of `package.json` defines the entry point for the Pulumi program. 

## @pulumi/pulumi Package {#pulumipulumi}

The [@pulumi/pulumi] package is the core library for working with the Pulumi planning engine. This package defines the following:
- Resources ([pulumi.Resource])
- External cloud platform resources ([pulumi.CustomResource])
- Components defined entirely in JavaScript ([pulumi.ComponentResource])

Dependencies between resources are encoded with [pulumi.Output].

This package also provides the following helpers:
- [pulumi.getStack] to get information about the current stack 
- [pulumi.log] for logging deployment information
- [pulumi.runtime.serializeFunctionAsync] for turning JavaScript callbacks into data which can be [used as application code](#runtime).

## Creating resources {#resources}

A resource is created via `new Resource(name)` in JavaScript. All resources must have a name, which must be unique in the Pulumi program.

All resource constructors take the following additional properties. 
- `dependencies` - a list of explicit resource dependencies
- `protect` - whether to mark a resource as protected. A protected resource cannot be deleted directly: first you must set `protect: false` and run `pulumi update`. Then, the resource can be deleted, either by removing the line of code or by running `pulumi destroy`.
- `parent` - optional parent for the resource. See [Components](#components).
- `provider` - optional provider for the resource. See [Providers](#providers).

## Resource outputs {#outputs}

<!-- TODO: add direct anchor link to `apply` once #333 is fixed -->

The outputs of resource objects have type [Output][pulumi.Output]. Resource inputs take either a raw value or an output from another resource. To transform an output into a new value, use the [`apply` method](pkg/nodejs/@pulumi/pulumi/#Output). 

For example, use the following to create an HTTPS URL from the DNS name of a virtual machine: 

```js
virtualmachine.dnsName.apply(dnsName => "https://" + dnsName)
```

## Stack output {#stack-outputs}

A [stack output](stack.html#outputs) is a value that can be easily retrieved from the Pulumi CLI and is displayed on pulumi.com. To export value from a stack, use the following definition in the top-level of the entry point for your project:

**JavaScript**
```js
exports.url = ...
```

**TypeScript**
```ts
export let url = ...
```

**Python**
```python
pulumi.output(url, ...)
```

From the CLI, you can then use `pulumi stack output url` to get the value and incorporate into other scripts or tools. 

The right-hand side of a stack export can be a regular JavaScript value, an [Output], or a `Promise`. The actual value will be resolved at the end of `pulumi update`.

Stack exports are JSON serialized, though quotes are removed when exporting just a string value. For example:

```js
exports.x = "hello" 
// result of `pulumi stack output x`:
// hello

exports.o = {num: 42}
// result of `pulumi stack output o`:
// {"num": 42}
```

## Using configuration values {#config}

To access configuration values that have been set with `pulumi config set`, use the following:

```js
let config = new pulumi.Config("broome-proj"); // broome-proj is name defined in Pulumi.yaml
console.log(`Hello, ${config.require("name")}!`);        // prints "BroomeLLC"
```

In the Pulumi CLI, configuration values are always created as string values. But, you can extract a strongly-typed form with methods such as `config.getNumber`, `config.getBoolean`, and so on.

## Components {#components}

A Pulumi **component** is a logical group of resources which contains other components and physical cloud resources. A Pulumi stack is itself a component that contains all top-level components and resources in a program. 

To create a new component, either in a top-level program or in a library, create a subclass of [pulumi.ComponentResource]. Components provide a way to create reusable abstractions made up of other resources.

Here's a simple component definition:

```js
class MyResource extends pulumi.ComponentResource {
    constructor(name, opts) {
        super("pkg:MyResource", name, {}, opts);
    }
}
```

The call to `super` registers the component instance with the Pulumi engine. This records the resource in the checkpoint and tracks it across program deployments. Since all resources must have a name, a component constructor should accept a name and pass it to `super`.

<!-- TODO: What names are allowed for the component namespace? -->

A component must register a namespace, such as `pkg:MyResource` in the example above. To reduce the potential of name conflicts, this name should contain the package name and resource type, such as `aws:lambda:Function`. 

Components will often contain child resources. To track this relationship, pass the component instance as the parent when constructing a resource:

```js
let bucket = new aws.s3.Bucket(`${name}-bucket`, {}, { parent: this });
```

Components can define their own properties using `registerOutputs`. The Pulumi engine uses this information to track dependencies between resources. 

```js
this.registerOutputs({
    bucketDnsName: bucket.bucketDomainName,
})
```

In addition to the usual resource options, components accept a set of [providers](#providers) to use for their child resources. If a component is itself a child of another component, its set of providers is inherited from its parent by default.

```js
let component = new MyResource("component", { providers: { aws: useast1, kubernetes: myk8s } });
```

For more information about components, see the [Pulumi Components](component-tutorial.html) tutorial.

## Providers {#providers}

A [CustomResource][pulumi.CustomResource] needs an associated resource provider to manage its Create, Read, Update, and Delete (_CRUD_) operations. This is in contrast to a [ComponentResource][pulumi.ComponentResource], whose logic is authored entirely in a Pulumi program's source language (e.g. Javascript or Python). By default, a `CustomResource`'s provider is determined based on its [package](#packages). This default provider is automatically created by Pulumi, and is configured using its package's [config values](#config). For example, the configuration and program below will create a single EC2 instance in the `us-west-2` region.

```js
let aws = require("@pulumi/aws");

let instance = new aws.ec2.Instance("myInstance", {
    instanceType: "t2.micro",
    ami: "myAMI",
});
```

```bash
$ pulumi config set aws:region us-west-2
```

While this works for the majority of Pulumi programs, some programs may have special requirements (e.g. the ability to deploy into multiple AWS regions simultaneously or to deploy into a Kubernetes cluster created earlier in the program) that require explicitly creating, configuring, and referencing providers. This is typically done by instantiating the relevant package's `Provider` type and passing it in the options for each `CustomResource` or `ComponentResource` that needs to use it. For example, the configuration and program below will create an ACM certificate in the `us-east-1` region and a load balancer listener in the `us-west-2` region.

```js
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

```
$ pulumi config set aws:region us-west-2
```

Component resources also accept a set of providers to use with their child resources. For example, the EC2 instance parented to `myResource` in the program below will be created in `us-east-1`, and the Kubernetes pod parented to `myResource` will be created in the cluster targeted by the "test-ci" context.

```js
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

## Packages {#packages}

Pulumi packages are normal NPM or Python packages. They transitively depend on `@pulumi/pulumi` which defines how resources created by a Pulumi program will be communicated to the Pulumi engine.  This ability to register resources with the Pulumi engine is the only difference between a Pulumi package and any other NPM package.

Some Pulumi packages have a dependency on a Resource Provider plugin which contains the implementation for how to Create, Read, Update and Delete resources defined by the package.  The [pulumi.CustomResource] base class is used to connect a JavaScript resource class with the resource provider it depends on for resource management.  Packages like [@pulumi/aws] and [@pulumi/kubernetes] define resources, such as `aws.ec2.Intance`, `kubernetes.Pod`, which are managed by the AWS and Kubernetes resource providers. Packages such as [@pulumi/cloud] and [@pulumi/aws-infra] contain only higher-level component resources, which are not managed by a resource provider.

## Runtime code {#runtime}

You can create a component that allows the caller to pass in runtime JavaScript functions. For example, a JavaScript callback could be used as the implementation of an AWS Lambda function. This is enabled by the [pulumi.runtime.serializeFunctionAsync] API, which takes as input a JavaScript `Function` object, and returns a `Promise<string>` that contains the serialized form of that function. 

The serialized form is a module with a single exported function named `handler` which is a function with the same signature as the inputs.

When serializing a function to text, the following steps are taken:

1. Any captured variables referenced by the function are evaluated when the function is serialized.
2. The values of those variables are serialized.
3. When the values are objects, all properties and prototype chains are serialized.  When the values are functions, those functions are serialized by following these same steps.

<!-- MARKDOWN LINKS -->
[pulumi.Resource]: pkg/nodejs/@pulumi/pulumi/#Resource
[pulumi.ComponentResource]: pkg/nodejs/@pulumi/pulumi/#ComponentResource
[pulumi.CustomResource]: pkg/nodejs/@pulumi/pulumi/#CustomResource
[pulumi.Output]: pkg/nodejs/@pulumi/pulumi/#Output
[@pulumi/pulumi]: pkg/nodejs/@pulumi/pulumi
[@pulumi/aws]: pkg/nodejs/@pulumi/aws
[@pulumi/kubernetes]: pkg/nodejs/@pulumi/kubernetes/
[@pulumi/cloud]: pkg/nodejs/@pulumi/cloud
[@pulumi/aws-infra]: pkg/nodejs/@pulumi/aws-infra

[pulumi.getStack]: pkg/nodejs/@pulumi/pulumi/#getStack
[pulumi.log]: pkg/nodejs/@pulumi/pulumi/log/
[pulumi.runtime.serializeFunctionAsync]: pkg/nodejs/@pulumi/pulumi/runtime/#serializeFunctionAsync
<!-- END LINKS -->
