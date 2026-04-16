---
title_tag: "Pulumi Go Provider SDK"
meta_desc: "Learn how to use the Pulumi Go Provider SDK to author Pulumi packages in Go."
title: Pulumi Go Provider SDK
h1: Pulumi Go Provider SDK
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Pulumi Go Provider SDK
        parent: iac-guides-packages
        weight: 68
aliases:
- /docs/iac/using-pulumi/extending-pulumi/pulumi-provider-sdk/
- /docs/iac/extending-pulumi/pulumi-provider-sdk/
- /docs/iac/build-with-pulumi/pulumi-provider-sdk/
- /docs/iac/guides/building-extending/providers/pulumi-provider-sdk/
- /docs/iac/guides/building-extending/providers/sdks/
- /docs/iac/guides/building-extending/providers/sdks/pulumi-go-provider-sdk/
---

[pulumi-go-provider](https://github.com/pulumi/pulumi-go-provider/) is a Go library for authoring Pulumi [packages](/docs/iac/concepts/packages/). A package built with pulumi-go-provider can contain any combination of:

- [Custom resources](/docs/iac/concepts/resources/)
- [Components](/docs/iac/concepts/components/), distributed as either a [source-based plugin package](/docs/iac/guides/building-extending/packages/source-based-plugin/) or as a compiled, executable plugin
- [Functions](/docs/iac/concepts/functions/)

The library uses Go reflection to derive the package's [schema](/docs/iac/guides/building-extending/packages/schema/) from your Go types, so multi-language SDKs can be generated without hand-authoring a JSON schema. Pulumi uses pulumi-go-provider internally for several of its own packages, including [`pulumi-eks`](/registry/packages/eks/).

Useful links:

- **Repository**: [pulumi/pulumi-go-provider](https://github.com/pulumi/pulumi-go-provider/) on GitHub
- **Examples**: [example providers](https://github.com/pulumi/pulumi-go-provider/tree/main/examples) in the repository
- **Reference documentation**: [pulumi-go-provider](https://pkg.go.dev/github.com/pulumi/pulumi-go-provider) on pkg.go.dev

## Custom resources

The following example defines a `greetings` package with a single custom resource, `HelloWorld`, that takes a `name` and an optional `loud` flag and stores the resulting greeting in resource state.

```go
func main() {
	provider, err := infer.NewProviderBuilder().
		WithResources(infer.Resource(&HelloWorld{})).
		Build()
	if err != nil {
		log.Fatal(err)
	}
	if err := provider.Run(context.Background(), "greetings", "0.1.0"); err != nil {
		log.Fatal(err)
	}
}

// Each resource has a controlling struct.
type HelloWorld struct{}

// Each resource has an input struct, defining what arguments it accepts.
type HelloWorldArgs struct {
	// Fields projected into Pulumi must be public and have a `pulumi:"..."` tag.
	Name string `pulumi:"name"`
	// Fields marked `optional` are optional, so they should have a pointer ahead of their type.
	Loud *bool `pulumi:"loud,optional"`
}

// Each resource has a state struct, describing the fields that exist on the created resource.
type HelloWorldState struct {
	// It is generally a good idea to embed args in outputs, but it isn't strictly necessary.
	HelloWorldArgs
	// Here we define a required output called message.
	Message string `pulumi:"message"`
}

// All resources must implement Create at a minimum.
func (HelloWorld) Create(
	ctx context.Context, name string, input HelloWorldArgs, preview bool,
) (string, HelloWorldState, error) {
	state := HelloWorldState{HelloWorldArgs: input}
	if preview {
		return name, state, nil
	}
	state.Message = fmt.Sprintf("Hello, %s", input.Name)
	if input.Loud != nil && *input.Loud {
		state.Message = strings.ToUpper(state.Message)
	}
	return name, state, nil
}
```

Sensible defaults are provided for any lifecycle method you don't implement. Because the example above doesn't implement `Diff` or `Update`, any input change replaces the resource. `Check` and `Read` confirm that inputs deserialize into `HelloWorldArgs`. `Delete` is a no-op.

## Functions

Functions are stateless operations that a Pulumi program can call. Define a function by creating a struct with an `Invoke` method and registering it with `infer.Function`.

The following example, adapted from the [`str` example provider](https://github.com/pulumi/pulumi-go-provider/tree/main/examples/str), defines a `replace` function that returns a string with all occurrences of one substring replaced by another.

```go
func main() {
	provider, err := infer.NewProviderBuilder().
		WithFunctions(infer.Function(&Replace{})).
		Build()
	if err != nil {
		log.Fatal(err)
	}
	if err := provider.Run(context.Background(), "str", "0.1.0"); err != nil {
		log.Fatal(err)
	}
}

type Replace struct{}

type ReplaceArgs struct {
	S   string `pulumi:"s"`
	Old string `pulumi:"old"`
	New string `pulumi:"new"`
}

type ReplaceResult struct {
	Out string `pulumi:"out"`
}

func (Replace) Invoke(
	ctx context.Context, req infer.FunctionRequest[ReplaceArgs],
) (infer.FunctionResponse[ReplaceResult], error) {
	return infer.FunctionResponse[ReplaceResult]{
		Output: ReplaceResult{
			Out: strings.ReplaceAll(req.Input.S, req.Input.Old, req.Input.New),
		},
	}, nil
}
```

## Components

Components are defined as Go structs that embed `pulumi.ResourceState` and are registered with `infer.ComponentF` (or `infer.Component`). The constructor receives a `*pulumi.Context` and the component's input struct, and creates child resources in the usual way.

For a complete example, see [`examples/component-provider`](https://github.com/pulumi/pulumi-go-provider/tree/main/examples/component-provider) in the pulumi-go-provider repository. To distribute a component package without compiling a binary plugin for every platform, see the [source-based plugin package guide](/docs/iac/guides/building-extending/packages/source-based-plugin/).

## Architecture

pulumi-go-provider has a few key building blocks:

- **Provider**: the main entry point that the Pulumi engine talks to.
- **Middleware**: handles token dispatch, schema generation, cancellation, and other lifecycle concerns.
- **infer**: a reflection-based framework for declaring resources, components, and functions from Go types.
- **resourcex**: helpers for inspecting and manipulating resource property values.
