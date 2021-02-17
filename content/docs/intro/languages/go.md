---
title: "Go"
meta_desc: An overview of how to use the Go language for infrastructure as code
           on any cloud (AWS, Azure, GCP, Kubernetes, etc.).
menu:
  intro:
    parent: languages
    weight: 4
---

<img src="/logos/tech/logo-golang.png" align="right" width="150" style="padding:8px; margin-top: -64px">

Pulumi supports writing your infrastructure as code using the Go language. Go 1.14 or later is required.

<a class="btn" href="https://golang.org/doc/install" target="_blank" title="Install Go">INSTALL GO</a>

## Getting Started

The fastest way to get up and running is to choose from one of the following Getting Started guides:

<div class="tiles my-4">
    <a class="tile flex-1 p-4" href="{{< relref "/docs/get-started/aws" >}}">
        <img class="h-8 mx-auto" src="/logos/tech/aws.svg" alt="AWS">
    </a>
    <a class="tile md:mx-4 flex-1 p-4" href="{{< relref "/docs/get-started/azure" >}}">
        <img class="h-8 mx-auto" src="/logos/tech/azure.svg" alt="Azure">
    </a>
    <a class="tile flex-1 p-4" href="{{< relref "/docs/get-started/gcp" >}}">
        <img class="h-8 mx-auto" src="/logos/tech/gcp.svg" alt="Google Cloud">
    </a>
</div>

## Templates

The fastest way to get started is to use a template. The template will initialize a Pulumi project. The getting started guides shown above will help do this on your cloud of choice, but this section describes doing so independently.

From an empty directory, create a new project:

```bash
$ mkdir myproject && cd myproject
$ pulumi new go
```

This will create a `Pulumi.yaml` [project file]({{< relref "../concepts/project" >}}) containing some minimal metadata about your project (including a name and description which you may wish to change) and a `main.go` file containing your program. The name of the directory is used as the project name in `Pulumi.yaml`. Use your favorite Go dependency manager (such as Go's built-in modules system, by running `go mod init` in your project's directory).

To deploy your infrastructure, first build your Go program: `go build -o $(basename $(pwd))`. Then run `pulumi up` and Pulumi will perform the operations needed to deploy the infrastructure you have declared.

This `go` template is cloud agnostic, and you will need to install additional Go modules for the cloud provider of your choice. Additional templates are available that do this for you:

* `pulumi new aws-go`: creates a starter AWS Go project
* `pulumi new azure-go`: creates a starter Azure Go project
* `pulumi new gcp-go`: creates a starter Google Cloud Go project

## Pulumi Programming Model


The Pulumi programming model includes a core concept of `Input` and `Output` values, which are used to track how outputs of one resource flow in as inputs to another resource.  This concept is important to understand when getting started with Go and Pulumi, and the [Inputs and Outputs]({{< relref "/docs/intro/concepts/inputs-outputs" >}}) documentation is recommended to get a feel for how to work with this core part of Pulumi in common cases.

### Additional Notes on the Pulumi Programming Model in Go

Outputs of Pulumi resources in Go programs are values that implement the `pulumi.Output` interface.  Most outputs are strongly typed to return a specific type of data, such as `pulumi.StringOutput` or `pulumi.IntArrayOutput`. Outputs are values which may not yet be known.  For example during a preview, the outputs of a resource may not be known if the resource has not yet been created or if the resource may need to be replaced.  As a result, you cannot directly access the value of an output.  Instead, to access and transform the value of an output you must use the `.Apply` method on the output, passing it a function which will run if and when the value is known to construct some new value.  See the section on Apply below for more details.

> Note: Because Go does not have generics, there are a large number of these implementations of the `pulumi.Output` interface, for every kind of value, including all nested struct values.

All inputs to Pulumi resources in Go programs are values that implement the `pulumi.Input` interfrace.  Many inputs are strongly typed to expect a specific type of input such as `pulumi.StringInput` or `pulumi.IntArrayInput`.  There are two kinds of values that implement these interfaces:

1. Normal Go values of the underlying type, which can be wrapped in a type alias that implements the specific type of `pulumi.Input` interface, such as `pulumi.String("hello")` for `pulumi.StringInput` or `pulumi.IntArray{pulumi.Int(1), pulumi.Int(2)}` for `pulumi.IntArrayInput`.
2. Output values which implement the `pulumi.Output` interface and are compatible with the input type, such as `pulumi.StringOutput` for `pulumi.StringInput` or `pulumi.IntArrayOutput` for `pulumi.IntArrayInput`.

As a concrete example - this program creates two resources.  The `Bucket` input property on `NewBucketObject` is of type `pulumi.StringInput` and is passed a `pulumi.StringOutput` value.  The `Key` input property is also of type `pulumi.StringInput` but is passed a `pulumi.String`.  During an initial preview, the `bucket.Bucket` output will not be known but the `pulumi.String("index.html)` value will be known.

```go
bucket, _ := s3.NewBucket(ctx, "my-bucket", nil)
obj, _ := s3.NewBucketObject(ctx, "my-object", &s3.BucketObjectArgs{
    Bucket:  bucket.Bucket,
    Key:     pulumi.String("index.html"),
    Content: pulumi.String("<h1>Hello world!</h1>"),
})
```

#### Apply

If you ever need to transform the value of an `Output` to a new value, of the same type or any other type, use one of the `Apply` methods on the output.  These methods are passed a callback function.  If and when the value of the `Output` becomes known, that callback function will be called with the underlying Go value of the output, and must return a new Go value.  The `Apply` method returns a new `Output` which itself will become known once this new Go value is available.

There are three kinds of `Apply` methods available.  They all do the same thing, but provide different static typing options for the inputs and outputs of the function passed to the `Apply` and the type of the `Output` returned from the `Apply`:

* `.ApplyT`: Callback inputs and outputs are strongly typed dynamically, but the return from `ApplyT` is always `pulumi.Output`.
* `.Apply<TypeName>`: Callback inputs and outputs are strongly typed dynamically, and the return from `Apply<TypeName>` is `pulumi.<TypeName>Output`.
* `.Apply`: Callback inputs and outputs are `interface{}`, and the return from `Apply` is always `pulumi.AnyOutput`.

Let's see each of these in action.  First, imagine we have an output value that is a string, and trying to compute it's length to pass as an input to some resource input.  

```go
var out pulumi.StringOutput = pulumi.String("hello").ToStringOutput()
var in pulumi.IntInput
```

We could use `ApplyT` like this: 

```go
in = out.ApplyT(func(s string) int {
    return len(s)
}).(pulumi.IntOutput)
```

The callback function passed to `ApplyT` takes the raw Go type of the output it is applied to as an argument, and returns the raw Go type that it wants to return.  Inside the body of the callback function, it works purely in terms of raw Go values - there are no inputs and outputs inside the callback function body.  That is because the callback function is called only if and when the values are all known.  

The signature of `ApplyT` is `func (Output) ApplyT(applier interface{}) Output`.  Note that the `applier` callback is typed as `interface` instead of a `func` type.  This allows the single `ApplyT` method to be used with *any* input and output types.  In the example here - the input type is `string` and the output type is `int`.  In other cases, we could use the same function, but with different input and output types for the callback.  This means that the callback function type is not statically type checked by Go.  Instead, it is type checked at runtime.  If the output is a `StringOutput`, it will be a runtime panic if the argument type of the callback function is not assignable from `string`.

The return type of `ApplyT` is `Output`, but the actual runtime type of the return value will depend on the return type of the callback passed to `ApplyT`. In the example above, the callback return `int`, and so the returned value from `ApplyT` will be an `IntOutput`.  This means it is safe by construction to type assert the return of the function to `.(pulumi.IntOutput)`.

The callback passed to `ApplyT` could also choose to return an error, in case it might fail.  In this case, the returned `Output` value will be put in to an error state.

```go
in = out.ApplyT(func(s string) (int, error) {
    return len(s), nil
}).(pulumi.IntOutput)
```

Instead of using `ApplyT` with a type assertion, we could use `ApplyInt` like this:

```go
in = out.ApplyInt(func(s string) (int, error) {
    return len(s), nil
})
```

This behaves exactly the same as `ApplyT`, but without the need for the `.(pulumi.IntOutput)` assertion.  

The last option is `Apply`, which works with `interface{}` values, and is thus more work to use in general - but more explicit.

```go
var anyout pulumi.AnyOutput = out.Apply(func(s interface{}) (interface{}, error) {
	return len(s.(string)), nil
})
in = anyout.ApplyInt(func(s interface{}) int { return s.(int) })
```

Note that with `Apply` you get an `AnyOutput`, which is an `Output` that represents a value of type `interface{}` - and in practice to pass that to other code (like an input that accepts an `IntInput`), you must use an `ApplyT` or `Apply<TypeName>` to assert the `interface{}` to the concrete type you need, as shown in the example above.

#### Working with Inputs

If you have an `Input` value and need to transform it, you should first convert it to an `Output`.  This is necesary because the input could be either a plain value or an Output, and both of these can be represented conservatively by an `Output`.  All input types have a `.To<type>Output()` method to convert to the corresponding Output type.  For example:

```go
var s pulumi.StringInput
sout := s.ToStringOutput()
```

#### Type Mapping Table

| Go Type | Pulumi Type |
| ------------ | ---------|
| `interface{}` | `Any` |
| `string` | `String` |
| `int` | `Int` |
| `float64` | `Float64` |
| `bool` | `Bool` |
| `[]interface{}` | `Array` |
| `map[string]interface{}` | `Map` |
| `[][]interface{}` | `ArrayArray` |
| `map[string]map[string]interface{}` | `MapMap` |
| `[]map[string]interface{}` | `MapArray` |
| `map[string][]interface{}` | `ArrayMap` |
| `*string` | `StringPtr` |
| `[]string` | `StringArray` |
| `map[string]string` | `StringMap` |
| `[][]string` | `StringArrayArray` |
| `map[string]map[string]string` | `StringMapMap` |
| `[]map[string]string` | `StringMapArray` |
| `map[string][]string` | `StringArrayMap` |
