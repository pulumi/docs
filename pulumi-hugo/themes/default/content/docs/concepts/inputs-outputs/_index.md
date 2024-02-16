---
title_tag: "Inputs & Outputs | Pulumi Concepts"
meta_desc: Resource properties are treated specially in Pulumi, both for purposes of input and output. Learn how to work with inputs and outputs in this guide.
title: "Inputs & outputs"
h1: "Inputs & outputs"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    identifier: inputs-outputs
    weight: 5
aliases:
    - /docs/reference/inputs-outputs/
    - /docs/intro/concepts/inputs-outputs/
search:
    boost: true
    keywords:
        - output
        - input
---

## Inputs

All resources in Pulumi accept values that describe the way the resource behaves. We call these values *inputs*.

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

_Inputs_ are generally representations of the parameters to the underlying API call of any resource that Pulumi is managing. The simplest way to create a resource with its required _inputs_ is to use a _plain value_.

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

{{% notes %}}
_Plain value_ in this document is used to describe a standard string, boolean, integer or other typed value or data structure in your language of choice. _Plain value_ is a way of differentiating these language specific values from Pulumi's asynchronous values.
{{% /notes %}}

However, in most Pulumi programs, the inputs to a resource will reference values from another resource:

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

In this case, Pulumi is taking the _output_ from one resource and using it as the _input_ to another resource.

## Outputs

All resources created by Pulumi will have properties which are returned from the cloud provider API. These values are called *outputs*.

Outputs are values of type {{< pulumi-output >}}, which behave very much like [promises](https://en.wikipedia.org/wiki/Futures_and_promises) or [monads](https://en.wikipedia.org/wiki/Monad_(functional_programming)). Simply put, outputs are a way of representing values that are not initially known but will become available once the infrastructure resource has completed provisioning, and this happens *asynchronously*. This is because the provisioning of resources is an asynchronous operation. It takes time for a cloud provider to complete the provisioning process, and Pulumi optimizes the process by [executing operations in parallel rather than sequentially](/docs/concepts/how-pulumi-works/#creation-and-deletion-order).

Because outputs are asynchronous, their actual plain values are not immediately available. If you need to access an output’s plain value, you can do so using one of the following options:

- [Apply](/docs/concepts/inputs-outputs/apply/): a callback that receives the plain value and computes a new output, generally used for accessing single values
- [Lifting](/docs/concepts/inputs-outputs/lifting/): directly read the value of an output, generally used for accessing nested values
- [Interpolation](/docs/concepts/inputs-outputs/outputs-and-strings/): concatenate string outputs with other strings

## Tracking dependencies

Outputs are also how Pulumi tracks dependencies between resources. When an output from one resource has been returned from the cloud provider API, Pulumi can link the two resources together and pass it as the input to another resource.

Pulumi automatically captures dependencies when you pass an output from one resource as an input to another resource. Capturing these dependencies ensures that the physical infrastructure resources are not created or updated until all their dependencies are available and up-to-date.
