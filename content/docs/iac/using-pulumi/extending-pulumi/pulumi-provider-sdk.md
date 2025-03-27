---
title_tag: "Pulumi Provider SDK"
meta_desc: "Learn about the Pulumi Provider SDK for Go to create your own Pulumi providers."
title: Pulumi Provider SDK
h1: Pulumi Provider SDK
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Pulumi Provider SDK
        parent: iac-extending-pulumi
        weight: 9
---

The [Pulumi Provider SDK](https://github.com/pulumi/pulumi-go-provider/) is a high-level library that simplifies the process of writing a Pulumi [provider](https://www.pulumi.com/docs/iac/concepts/resources/providers/) in Go. It abstracts much of the complexity involved in defining custom infrastructure resources, allowing developers to focus on business logic rather than boilerplate code.

Some key advantages of the SDK are:

- **Schema Generation**: Automatically generates provider schemas for seamless multi-language support.
- **Code-First Approach**: Define providers using Go structures and interfaces.
- **Middleware Support**: Enhances providers with layers like token dispatch, schema generation, and cancellation propagation.
- **Simplified Resource Definition**: Use the `infer` and `resourcex` libraries to streamline provider development.

## Using the Pulumi Provider SDK

> - **Repository**: [Pulumi Provider SDK](https://github.com/pulumi/pulumi-go-provider/) on GitHub
> - **Examples**: The repository includes a number of [example providers](https://github.com/pulumi/pulumi-go-provider/tree/main/examples).
> - **Reference Documentation**: [pulumi-go-provider](https://pkg.go.dev/github.com/pulumi/pulumi-go-provider) package on go.dev

Here's a quick example of the minimal code necessary to make a provider that can be used in any language. This example creates a provider called `greetings` that has two parameters (`name` and `loud`), which stores the product of its work (the constructed greeting message) as resource state.

### Example: "Hello, Pulumi" Provider

```go
func main() {
	p.RunProvider("greetings", "0.1.0", provider())
}

// Create the provider using infer
func provider() p.Provider {
    return infer.Provider(infer.Options{
			Resources: []infer.InferredResource{
				infer.Resource[HelloWorld, HelloWorldArgs, HelloWorldState](),
			},
		}))
}

// Each resource has a controlling struct.
type HelloWorld struct{}

// Each resource has in input struct, defining what arguments it accepts.
type HelloWorldArgs struct {
	// Fields projected into Pulumi must be public and hava a `pulumi:"..."` tag.
	// The pulumi tag doesn't need to match the field name, but its generally a
	// good idea.
	Name string `pulumi:"name"`
	// Fields marked `optional` are optional, so they should have a pointer
	// ahead of their type.
	Loud *bool `pulumi:"loud,optional"`
}

// Each resource has a state, describing the fields that exist on the created resource.
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

In this example, notice how the SDK framework has done a lot of work for us. The base implementation uses sensible default behaviours allowing you to implement only the parts that you need to. For example, since we didn't implement `Diff` or `Update`, if any field changes the resource state will just be regenerated and replaced. `Check` and `Read` will confirm that our inputs can be serialized into `HelloWorldArgs`. And `Delete` is a no-op.

## Architecture

The Pulumi Provider SDK follows a modular architecture with key components:

- **Provider**: The main entry point defining how resources are managed.
- **Middleware**: Handles token dispatch, schema generation, and other lifecycle events.
- **Infer**: A reflection-based framework for defining provider resources.
- **ResourceX**: Utilities for enhancing and extending provider capabilities.

## Testing

The SDK includes a built-in testing framework for validating provider behavior. Tests can be written in Go and executed using standard test frameworks.

***Example:** Testing a provider built with the Pulumi Provider SDK*

```go
// TBD need SME to provider HelloWorld provider test example
```

## Comparing to the Traditional Authoring Experience

| Feature                | Traditional SDKs | Pulumi Provider SDK |
|----------------------|----------------|------------------|
| Language Support   | JSON-based Schema & Boilerplate Code | Code-first in Go, automatic multi-language generation |
| Ease of Use        | High setup overhead | Simplified with `infer` |
| Schema Management | Manual JSON schema definitions | Automatic generation |
| Middleware Support | Limited | Built-in middleware system |

## Migration Guide

For users transitioning from traditional Pulumi provider authoring:

1. Convert schema definitions into Go structs.
2. Replace manual CRUD implementations with `infer`.
3. Leverage built-in middleware for authentication and resource handling.
4. Use the testing framework to validate the provider before deployment.

## Gotchas and FAQs

### Handling Default Values

*TODO: need SME to write this up*

### When will I get this in my favorite language?

The Pulumi Go Provider SDK primarily targets Go-based providers, but its schema generation allows multi-language support.

### Why did we build it and how does Pulumi use it?

This SDK simplifies provider development and ensures consistent, maintainable infrastructure definitions across Pulumi’s ecosystem. We use the same SDK to implement providers like `pulumi-eks`.

### Can I expect this library to be maintained?

Yes! This SDK is actively developed and maintained by Pulumi, and since we use it in the providers we author and maintain, it will always get attention from our engineering team.

### Does this entirely replace other SDKs/boilerplates?

No, but it offers a streamlined alternative. Existing SDKs will continue to be supported alongside this new approach.

---
For more details, check out the official [Pulumi Go Provider SDK repository](https://github.com/pulumi/pulumi-go-provider/).
