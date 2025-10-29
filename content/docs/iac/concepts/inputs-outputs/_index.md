---
title_tag: "Inputs & Outputs | Pulumi Concepts"
meta_desc: Resource properties are treated specially in Pulumi, both for purposes of input and output. Learn how to work with inputs and outputs in this guide.
title: "Inputs & outputs"
h1: "Inputs & outputs"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Inputs & Outputs
        parent: iac-concepts
        weight: 60
        identifier: iac-concepts-inputs-outputs
    concepts:
        identifier: inputs-outputs
        weight: 5
aliases:
    - /docs/reference/inputs-outputs/
    - /docs/intro/concepts/inputs-outputs/
    - /docs/concepts/inputs-outputs/
search:
    boost: true
    keywords:
        - output
        - input
---

Pulumi [resources](/docs/iac/concepts/resources) use special types to define their properties, called Inputs and Outputs. These special Pulumi types wrap "plain" values like strings or integers, and are what allow Pulumi to declaratively manage your infrastructure resources.

## What are inputs and outputs?

Pulumi IaC programs use special types called inputs and outputs to keep track of the dependencies between resources. Inputs and outputs, combined with your Pulumi stack's state file, are what allow Pulumi IaC programs to be _declarative_. In other words, you only need to tell Pulumi the desired state of your resources, and Pulumi will figure out what needs to be changed, and in what order those operations need to happen, to turn your declared desired state into the actual state of your resources.

Inputs are values that you _can_ supply to a resource. Inputs may be required or optional: For example, the `vpcId` input is required on the `aws.ec2.Subnet` resource because a subnet must belong to a particular VPC. On the other hand, the `forceDestroy` attribute on an `aws.s3.Bucket` resource (which allows you to delete a bucket that has objects in it) is optional and defaults to `false`.

When specifying inputs to a Pulumi resource, you can always use the plain version of the type. For example, any input that is defined as `pulumi.Input<string>` will accept a plain `string` value.

Outputs are values that are only known after a resource is created. For example, if you are creating an `aws.ec2.Vpc` resource, the VPC ID is an output - you cannot choose this value, and it is only known after the VPC is created in AWS.

When authoring Pulumi IaC programs, you will frequently use one resource's output as another resource's input. For example, you might create an `aws.ec2.Vpc` resource and pass its `vpcId` property (an output) to create several `aws.ec2.Subnet` resources (where `vpcId` is a required input). Pulumi uses inputs and outputs to automatically keep track of the dependencies between your resources. Using our example using Pulumi IaC to manage a VPC and its subnets, Pulumi will manage your resources in the following ways:

- When running `pulumi up`, Pulumi will ensure that no subnets are created until the VPC has been created and its VPC ID is known. If you are running your Pulumi program for the first time, this means Pulumi will wait until the VPC is created. If you ran your program before and are now adding an additional subnet, that subnet will be created immediately because the VPC ID is already known. (The value is stored in your Pulumi state file.)
- If you were running a `pulumi destroy` command to delete all the resources in your program, Pulumi would ensure that the VPC is not deleted until _all_ subnets in your Pulumi program have been deleted.

{{% notes type="info" %}}
Most dependencies between resources are automatically tracked by virtue of one resource's output being another resource's input. However, there may be other dependencies between resources that are not defined by this output-to-input relationship. For these cases, you can use the [`dependsOn`](/docs/iac/concepts/resources/options/dependson) resource option to explicitly define a dependency between resources.
{{% /notes %}}

Input and Output types are defined for each supported Pulumi language in the corresponding Pulumi SDK for that language. For example, in TypeScript, the Pulumi Node SDK has definitions for the types `pulumi.Input<T>` and `pulumi.Output<T>`. The Pulumi SDK is typically imported by default whenever you create a new Pulumi program, e.g. with `pulumi new typescript`, `pulumi new python`, etc.

## Why are inputs and outputs necessary?

Pulumi inputs and outputs are what allow Pulumi IaC programs to manage your resources declaratively despite being written in imperative general purpose programming languages.

In imperative programming, you write step-by-step instructions telling the computer exactly how to perform a task, in the exact order those steps must occur. For example, in a traditional imperative program, you might write code that says "first create a VPC, wait for it to be created, get its ID, then create a subnet using that ID."

In declarative programming, you describe the desired end state you want to achieve, and the system figures out how to reach that state. For example, in a declarative infrastructure program, you would describe "I want a VPC and a subnet in that VPC," and the system automatically determines that the VPC must be created first, waits for it to be ready, and then creates the subnet.

Pulumi's input and output system enables this declarative approach by automatically tracking dependencies between resources. When you pass an output from one resource as an input to another, Pulumi records that dependency and ensures the resources are created, updated, or destroyed in the correct order—without you needing to write explicit sequencing logic.

## Working with inputs

All resources in Pulumi accept values that describe the way the resource behaves. These values are called inputs.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
const myId = new random.RandomId("mine", {
    byteLength: 8, // byteLength is an input
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const myId = new random.RandomId("mine", {
    byteLength: 8, // byteLength is an input
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
my_id = random.RandomId("mine",
    byte_length=8 # byte_length is an input
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go

myId, err := random.NewRandomId(ctx, "mine", &random.RandomIdArgs{
	ByteLength: pulumi.Int(8), // ByteLength is an input
})
if err != nil {
	return err
}

```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var myId = new Random.RandomId("mine", new()
{
    ByteLength = 8, // ByteLength is an input
});

```

{{% /choosable %}}
{{% choosable language java %}}

```java
var myId = new RandomId("mine", RandomIdArgs.builder()
    .byteLength(8) // byteLength is an input
    .build());

```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  myId:
    type: random:randomId
    properties:
      byteLength: 8 # byteLength is an input
```

{{% /choosable %}}
{{< /chooser >}}

Inputs are generally representations of the parameters to the underlying API call of any resource that Pulumi is managing. The simplest way to create a resource with its required inputs is to use a plain value, like a string:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
const key = new tls.PrivateKey("my-private-key", {
    algorithm: "ECDSA", // ECDSA is a plain value
});

```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const key = new tls.PrivateKey("my-private-key", {
    algorithm: "ECDSA", // ECDSA is a plain value
});

```

{{% /choosable %}}
{{% choosable language python %}}

```python
key = tls.PrivateKey("my-private-key",
  algorithm="ECDSA", # ECDSA is a plain value
)

```

{{% /choosable %}}
{{% choosable language go %}}

```go

key, err := tls.NewPrivateKey(ctx, "my-private-key", &tls.PrivateKeyArgs{
	Algorithm:  pulumi.String("ECDSA"), // ECDSA is a plain value
})
if err != nil {
	return err
}


```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var key = new PrivateKey("my-private-key", new PrivateKeyArgs{
    Algorithm = "ECDSA", // ECDSA is a plain value
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var key = new PrivateKey("my-private-key", PrivateKeyArgs.builder()
    .algorithm("ECDSA") // ECDSA is a plain value
    .build()
)
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  key:
    type: tls:PrivateKey
    properties:
      algorithm: "ECDSA" # ECDSA is a plain value
```

{{% /choosable %}}
{{< /chooser >}}

## Working with outputs

All resources created by Pulumi will have properties which are returned from the cloud provider API. These values are called outputs.

{{% notes type="info" %}}
This section is about resource outputs, which are related to, but not the same as [stack outputs](/docs/iac/concepts/stacks/#outputs). A stack output is a value that is exported at the end of a successful update, usually intended for use outside of the Pulumi program context: either from the command line via the `pulumi stack output` command or in another Pulumi program by using a [stack reference](/docs/iac/concepts/stacks/#stackreferences).
{{% /notes %}}

Outputs are similar to [promises or futures](https://en.wikipedia.org/wiki/Futures_and_promises): They represent values that are not initially known but will become known once an infrastructure resource has completed provisioning. In other words, outputs represent asynchronous values. Outputs are necessary in Pulumi because provisioning resources is an asynchronous operation: It takes time for a cloud provider to finish provisioning a resource (several minutes in some cases).

Because outputs represent asynchronous values, they must be handled differently than plain types like `string`. For example, you cannot directly print the value of an output using your language's string printing function (e.g. `console.log()` in TypeScript, `print` in Python, etc.). Instead, you must use methods supplied in the Pulumi SDK to access the value once it is known.

The Pulumi SDK provides several basic methods for accessing the plain values of outputs once they are known:

- [Apply](/docs/concepts/inputs-outputs/apply/) allows you to access a single output's plain value
- [All](/docs/concepts/inputs-outputs/all/) allows you to access multiple outputs' plain values

Both `apply` and `all` allow you to return a value, which itself is also a Pulumi output. Transforming output values into other outputs is often useful. For example, you may want to take a DNS name that is the output of a load balancer and transform it into a full URL by appending `https://`. You can do this using `apply`.

In addition to the basic methods `apply` and `all`, each Pulumi language's SDK may also provide helper methods that allow you to work with Outputs similarly to plain types. For example:

- The Pulumi Node SDK contains a method [`pulumi.jsonStringify()`](/docs/reference/pkg/nodejs/pulumi/pulumi/functions/jsonStringify.html) which mirrors Node's `JSON.stringify()` function.
- The Pulumi Python SDK contains a method [`pulumi.Output.json_dumps()`](/docs/reference/pkg/python/pulumi/#pulumi.Output.json_dumps) which mirrors the function `dumps()` in the standard Python `json` library.

Check your language's Pulumi SDK documentation for a complete listing:

- [TypeScript (Node.js)](/docs/reference/pkg/nodejs/pulumi/pulumi/)
- [Python](/docs/reference/pkg/python/pulumi/)
- [Go](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi)
- [.NET](/docs/reference/pkg/dotnet/Pulumi/Pulumi.html)
- [Java](/docs/reference/pkg/java/)
- [YAML](/docs/iac/languages-sdks/yaml/yaml-language-reference/#expressions)

## Using inputs and outputs together

In Pulumi programs, you will often use one resource's output as another resource's input. Pulumi will keep track of this dependency behind the scenes to ensure that your resources are changed in the necessary order:

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language javascript %}}

```javascript
let password = new random.RandomPassword("password", {
    length: 16,
    special: true,
    overrideSpecial: "!#$%&*()-_=+[]{}<>:?",
});
let example = new aws.rds.Instance("example", {
    instanceClass: "db.t3.micro",
    allocatedStorage: 64,
    engine: "mysql",
    username: "someone",
    password: password.result, // We pass the output from password as an input
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const password = new random.RandomPassword("password", {
    length: 16,
    special: true,
    overrideSpecial: "!#$%&*()-_=+[]{}<>:?",
});
const example = new aws.rds.Instance("example", {
    instanceClass: "db.t3.micro",
    allocatedStorage: 64,
    engine: "mysql",
    username: "someone",
    password: password.result, // We pass the output from password as an input
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
password = random.RandomPassword(
    "password",
    length=16,
    special=True,
    override_special="!#$%&*()-_=+[]{}<>:?"
)
example = aws.rds.Instance(
    "example",
    instance_class="db.t3.micro",
    allocated_storage=64,
    engine="mysql",
    username="someone",
    password=password.result, # We pass the output from password as an input
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
password, err := random.NewRandomPassword(ctx, "password", &random.RandomPasswordArgs{
	Length:          pulumi.Int(16),
	Special:         pulumi.Bool(true),
	OverrideSpecial: pulumi.String("!#$%&*()-_=+[]{}<>:?"),
})
if err != nil {
	return err
}
_, err = rds.NewInstance(ctx, "example", &rds.InstanceArgs{
	InstanceClass:    pulumi.String("db.t3.micro"),
	AllocatedStorage: pulumi.Int(64),
	Engine:           pulumi.String("mysql"),
	Username:         pulumi.String("someone"),
	Password:         password.Result, // We pass the output from password as an input
})
if err != nil {
	return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var password = new Random.RandomPassword("password", new()
{
    Length = 16,
    Special = true,
    OverrideSpecial = "!#$%&*()-_=+[]{}<>:?",
});

var example = new Aws.Rds.Instance("example", new()
{
    InstanceClass = "db.t3.micro",
    AllocatedStorage = 64,
    Engine = "mysql",
    Username = "someone",
    Password = password.Result, // We pass the output from password as an input
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var password = new RandomPassword("password", RandomPasswordArgs.builder()
    .length(16)
    .special(true)
    .overrideSpecial("!#$%&*()-_=+[]{}<>:?")
    .build());

var example = new Instance("example", InstanceArgs.builder()
    .instanceClass("db.t3.micro")
    .allocatedStorage(64)
    .engine("mysql")
    .username("someone")
    .password(password.result()) // We pass the output from password as an input
    .build());
```

{{% /choosable %}}
{{< /chooser >}}
