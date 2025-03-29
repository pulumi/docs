---
title: The Easier Way to Create Pulumi Providers in Go
allow_long_title: true
date: 2023-01-19
authors:
  - kyle-dixler
tags:
  - go
  - packages
meta_desc: A major update to the Pulumi Provider Boilerplate simplifies the provider
  development process.
meta_image: meta.png
search:
  keywords:
    - Go
    - Provider
    - Go Provider
    - Provider Boilerplate
---

We are excited to announce that we've updated the Pulumi Provider Boilerplate to make custom provider implementation easier!

This major update brings a wealth of usability improvements to the Pulumi Provider Boilerplate by incorporating our brand
new Pulumi Go Provider SDK.

<!--more-->

**Note:** This update will not have any impact on existing providers that are utilizing an older version of the repository.

## Background

The Pulumi Provider Boilerplate [(view on GitHub)](https://github.com/pulumi/pulumi-provider-boilerplate) is a template repository
that contains a minimal example of a working provider and has served as a starting point for writing your own provider.

For those who may not be familiar with provider authoring, it involves three distinct parts:

1. Package schema definition
2. Provider implementation
3. SDK generation

Providers are implemented as gRPC servers that handle requests to perform CRUD (create, read, update, delete) operations on resources on behalf of the Pulumi engine.
SDK generation, on the other hand, involves generating source code libraries for a Pulumi program to utilize the provided resources.

In the past, implementing a provider using the old provider boilerplate could be difficult because you had to implement:

- the provider's schema
- the CRUD operations on a provider's resources
- the gRPC server
- SDK code generation to consume these resources in a Pulumi program

Now, using our code-first approach, you can implement your provider in Go by defining the provider's metadata, resources, and functions, and then compiling the provider binary.
The library takes care of the provider schema and gRPC server for you and the Pulumi CLI takes care of the SDK code generation with the following command:

```bash
pulumi package gen-sdk <path/to/provider-binary>
```

You can leave the heavy lifting to us and focus on the implementation details that matter to your organization.

## Boilerplate code

**Note:** The completed boilerplate is attached at the bottom of this document and in the pulumi-provider-boilerplate repository [(view on GitHub)](https://github.com/pulumi/pulumi-provider-boilerplate).

### Provider Entrypoint

The pulumi provider boilerplate program is currently quite short and the main entrypoint is as follows.

```go
package main

import (
    p "github.com/pulumi/pulumi-go-provider"
    "github.com/pulumi/pulumi-go-provider/infer"
)

func main() {
    p.RunProvider("xyz", Version,
        // We tell the provider what resources it needs to support.
        // In this case, a single custom resource.
        infer.Provider(infer.Options{
            Resources: []infer.InferredResource{
                infer.Resource[Random, RandomArgs, RandomState](),
            },
        }))
}
```

### Resource Implementation

Resources consist of arguments, state, and CRUD operations to control them.

```go
// Each resource has in input struct, defining what arguments it accepts.
type RandomArgs struct {
    // Fields projected into Pulumi must be public and hava a `pulumi:"..."` tag.
    // The pulumi tag doesn't need to match the field name, but its generally a
    // good idea.
    Length int `pulumi:"length"`
}

// Each resource has a state, describing the fields that exist on the created resource.
type RandomState struct {
    // It is generally a good idea to embed args in outputs, but it isn't strictly necessary.
    RandomArgs
    // Here we define a required output called result.
    Result string `pulumi:"result"`
}

// Each resource has a controlling struct.
type Random struct{}
```

Resource behavior is determined by implementing methods on the controlling struct.

```go
// All resources must implement Create at a minumum.
func (Random) Create(ctx p.Context, name string, input RandomArgs, preview bool) (string, RandomState, error) {
    state := RandomState{RandomArgs: input}
    if preview {
        return name, state, nil
    }
    state.Result = makeRandom(input.Length)
    return name, state, nil
}
```

The `Create` method is mandatory, but other methods are optional.

- `Check`: Remap inputs before they are typed.
- `Diff`: Change how instances of a resource are compared.
- `Update`: Mutate a resource in place.
- `Read`: Get the state of a resource from the backing provider.
- `Delete`: Custom logic when the resource is deleted.
- `Annotate`: Describe fields and set defaults for a resource.
- `WireDependencies`: Control how outputs and secrets flows through values.

## Wrapping up

We encourage everyone to try the new authoring experience, including devs who may have previously found it challenging in comparison to the ease of program authorship.

### Additional Example: Command provider

If you want a more involved example, the command provider [(view on GitHub)](https://github.com/pulumi/pulumi-command/) has been
rewritten to use the Pulumi Go Provider library entirely and is heavily commented. You can actually compare the project before and after using it to see how it has streamlined
provider implementation.

### Completed example

The complete boilerplate provider looks as follows:

```go
package main

import (
    "math/rand"
    "time"

    p "github.com/pulumi/pulumi-go-provider"
    "github.com/pulumi/pulumi-go-provider/infer"
)

// Version is initialized by the Go linker to contain the semver of this build.
var Version string

func main() {
    p.RunProvider("xyz", Version,
        // We tell the provider what resources it needs to support.
        // In this case, a single custom resource.
        infer.Provider(infer.Options{
            Resources: []infer.InferredResource{
                infer.Resource[Random, RandomArgs, RandomState](),
            },
        }))
}

// Each resource has a controlling struct.
// Resource behavior is determined by implementing methods on the controlling struct.
// The `Create` method is mandatory, but other methods are optional.
// - Check: Remap inputs before they are typed.
// - Diff: Change how instances of a resource are compared.
// - Update: Mutate a resource in place.
// - Read: Get the state of a resource from the backing provider.
// - Delete: Custom logic when the resource is deleted.
// - Annotate: Describe fields and set defaults for a resource.
// - WireDependencies: Control how outputs and secrets flows through values.
type Random struct{}

// Each resource has in input struct, defining what arguments it accepts.
type RandomArgs struct {
    // Fields projected into Pulumi must be public and hava a `pulumi:"..."` tag.
    // The pulumi tag doesn't need to match the field name, but its generally a
    // good idea.
    Length int `pulumi:"length"`
}

// Each resource has a state, describing the fields that exist on the created resource.
type RandomState struct {
    // It is generally a good idea to embed args in outputs, but it isn't strictly necessary.
    RandomArgs
    // Here we define a required output called result.
    Result string `pulumi:"result"`
}

// All resources must implement Create at a minumum.
func (Random) Create(ctx p.Context, name string, input RandomArgs, preview bool) (string, RandomState, error) {
    state := RandomState{RandomArgs: input}
    if preview {
        return name, state, nil
    }
    state.Result = makeRandom(input.Length)
    return name, state, nil
}

func makeRandom(length int) string {
    seededRand := rand.New(rand.NewSource(time.Now().UnixNano()))
    charset := []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    result := make([]rune, length)
    for i := range result {
        result[i] = charset[seededRand.Intn(len(charset))]
    }
    return string(result)
}
```
