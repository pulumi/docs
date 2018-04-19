---
title: "Programming Model"
---

🚧 WORK IN PROGRESS 🚧

## Programs {#programs}
* Written in Node.js or Python
* Can use any pacakges, but also can use Pulumi packages (e.g. @pulumi/aws)
* Run during `pulumi preview` and `pulumi update` to determine the desired state of the application's resources
* Application logic can be included int Pulumi programs via references to published artifacts (S3 buckets, existing
  docker images, etc.), or artifacts that version with the Pulumi program (strings or files in the Pulumi program
  folder, docker images built during the program execution, or code compiled form Pulumi program callbacks into AWS
  Lambdas or Azure Functions).
* A `Pulumi.yaml` file in a folder indicates that it is a Pulumi program.  The `runtime` field of the `Pulumi.yaml`
  indicates which runtime will be used to run the program.  When the `runtime` is `nodejs`, the user-installed Node.js runtime
  will be used to run the program.  The `package.json` file next to `Pulumi.yaml` (or in the folder
  referred to by the `main` property of `Pulumi.yaml`) is used to identify which JavaScript code will be used as the
  entry point for the Pulumi program.

## `@pulumi/pulumi` Package {#pulumipulumi}
* The core library for working with the Pulumi planning engine from a Pulumi program or library.
* Defines how resources are created (`pulumi.Resource`), and how resources can be defined in external cloud platforms
  (`pulumi.CustomResource`) or as components in pure code (`pulumi.ComponentResource`).
* Defines how dependencies between resources are represented, as `pulumi.Output<T>` values.
* Provides helpers for getting stack information (`pulumi.getStack`), logging deployment information (`pulumi.log`), and
  for turning JavaScript callbacks into data which can be [used as application code](#runtime)
  (`pulumi.runtime.serializeFunctionAsync`).
* Full API documentation available at [@pulumi/pulumi API docs](../packages/pulumi)

## Creating Resources {#resources}
* `new Resource()`
* Name
* Custom Resource, ComponentResource, DynamicResource
* Dependencies
* Additional options
   * `dependencies`
   * `protect`
   * `parent`

## Outputs {#outputs}
* Outputs of resource objects are of type `Ouput<T>`
* Inputs are of type `Input<T> == T | Output<T>`, allowing either a raw value or an output from another resource to be
  used as input.
* Inputs 
* `apply` can be used to transform an output into a new value - for example: `virtualmachine.dnsName.apply(dnsName =>
  "https://" + dnsName)` to create an HTTPS url from a DNS name of a virtual machine running a web server.

## Stack Exports {#exports}
* Use `export let url = ...` at top level in your stack entry point to export a value from a stack
* Most useful as a way to export an output from one or more resources created by the program
* Can be discovered from the CLI with `pulumi stack output url` - easy to chain into other scripts or tooling.
* Any `Input<T>` value can be assigned to an export (a value, an `Ouput<T>` or a `Promise<T>`, and will be resolved to a
  final value before being returned to the `pulumi` CLI
* Stack exports are JSON serialized, but top-level string values are not quoted.  So `export let x = "hello"` results in
  `hello`, and `export let o = {num: 42}` results in `{"num": 42}`.

## Using Config {#config}
* Programs can access config through `let config = new pulumi.Config("package-name"); let value =
  config.get("mySetting");`.
* Config is always defined as string values in the CLI (`pulumi config set pkg:name value`), but can be extracted in a
  more strongly typed form with `config.getNumber`, `config.getBoolean`, etc.

## Components {#components}
* A Pulumi **component** is a logical group of resources which contains other components and physical cloud resources. A Pulumi stack is itself a component that contains all top-level components and resources in a program.
* Programs and libraries can define new Components by defining classes derived from `pulumi.ComponentResource`.
* These components provide a way of creating reusable abstractions made up of other resources.
* A simple components looks like:

  ```typescript
  class MyResource extends pulumi.ComponentResource {
      constructor(name: string, opts?: pulumi.ResourceOptions) {
          super("pkg:MyResource", name, {}, opts);
      }
  }
  ```

* The call to `super` will cause an instance of the component to be registered with Pulumi.  This will allow it to be
  recorded in the checkpoint and tracked across deployments of the program.
* The component must register a Type (e.g. `pkg:MyResource`).  This is used to identify resources that are managed by
  this component.  The name should include the package name and resource type, along with any static namespacing (e.g.
  `aws:lambda:Function`).  In general, it should be the same as the way users will refer to the resource in code, but
  with `:` in place of `.`.
* Since resources must have a name, a component constructor should accept a name and pass it to `super`.

* Components can register other resources as children by passing themselves as the `parent` of the resource when it in
  constructed.  This allows the component to logically group all of the resources that it is composed out of.
* Components can also define their own exported properties using `registerOutputs`.

  ```typescript
  class MyResource extends pulumi.ComponentResource {
      constructor(name: string, opts?: pulumi.ResourceOptions) {
          super("pkg:MyResource", name, {}, opts);
          let bucket = new aws.s3.Bucket(`${name}-bucket`, {}, { parent: this });
          this.registerOutputs({
              bucketDnsName: bucket.bucketDomainName,
          })
      }
  }
  ```

## Runtime Code {#runtime}
* Pulumi programs and libraries can choose to allow using JavaScript functions as runtime code which gets passed in as
  the application code that will run in infrastructure resources.  For example, a JavaScript callback could be used as
  an AWS Lambda implementation, or a long running function could be used as a container implementation on Kubernetes or
  ECS.
* This is enabled by the `pulumi.runtime.serializeFunctionAsync` API, which takes a JavaScript `Function` object as
  input, and returns a `Promise<string>` that contains the serialized form of that function.
* The serialized form is a module with a single exported function named `handler` which is a function with the same
  signature as the inputs.
* When serializing a function to text, the following steps are taken:
  1. Any captured variables referenced by the function are evaluated when the function is serialized.
  2. The values of those variables are serialized.
  3. When the values are objects, all properties and prototype chains are serialized.  When the values are functions,
     those functions are serialized by following these same steps.

## Packages {#packages}
* Pulumi packages are normal NPM or Python packages
* Pulumi packages transitively depend on `@pulumi/pulumi` which defines how resources created by a Pulumi program will
  be communicated to the Pulumi engine.  This ability to register resources with the Pulumi engine is the only
  difference between a Pulumi package and any other NPM package.
* Some Pulumi packages have a dependency on a Resource Provider plugin which knows how to Create, Read, Update and
  Delete resources defined by the package.  The `pulumi.CustomResource` base class is used to connect a JavaScript
  resource class with the resource provider it depends on for resource management.  Packages like `@pulumi/aws` and
  `@pulumi/kubernetes` define resources (like `aws.ec2.Intance`, `kubernetes.Pod`), which are managed by the AWS and
  Kubernetes ressource providers.
* A `CustomResource` needs an associated CRUD provider, whereas a `ComponentResource` does not (its logic is entirely in JS/TS/Py).
* Other Pulumi packages define components purely in JavaScript (or Python) which are built out of these raw provider
  resource building blocks.  This includes packages like `@pulumi/cloud` or `@pulumi/aws-infrastructure` which provide
  higher-level components..
