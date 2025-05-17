---
title: "Announcing Pulumi Go Provider SDK v1.0"
date: 2025-05-16
updated: 2025-05-16
draft: false
allow_long_title: true

meta_desc: Pulumi Components enable you to create, share, and consume reusable infrastructure building blocks across your organization and the broader community.
meta_image: meta.png
authors:
    - eron-wright
    - meagan-cojocar
tags:
    - releases 
    - platform-teams
    - features
    - iac
    - components
social:
    twitter: "(todo)"
    linkedin: "(todo)"
---

At Pulumi, we are constantly striving to enhance the developer experience and boost productivity for engineers managing cloud infrastructure. A key part of this is enabling integrations with the vast ecosystem of cloud services and tools. Pulumi Providers are the mechanism that allow you to define and manage resources from virtually any service or tool. Today, we are thrilled to announce a significant milestone: the **v1.0.0 release of the Pulumi Provider SDK** for Go!

<!--more-->

This framework has been under active development since 2022 and is now considered **stable and production-ready**. The Pulumi Provider SDK is a high-level library specifically designed to simplify the process of writing Pulumi providers in Go. It abstracts away much of the complexity involved in defining custom infrastructure resources, allowing developers to **focus on business logic rather than boilerplate code**. This focus on streamlining the development process is directly in line with our commitment to **developer productivity and velocity**.

Pulumi has worked diligently to bring this SDK to maturity, incorporating feedback and leveraging it internally to build providers like the ["Docker Build Provider"][pulumi-docker-build]. With v1.0.0, building robust, multi-language Pulumi providers is more accessible than ever.

[pulumi-docker-build]: https://www.pulumi.com/registry/packages/docker-build/

## Summary of Changes

Key changes and new features include:
- **Go 1.24**
- **New Provider Builder API**: A convenient builder API to define providers.
- **Functional-Style Components**: It is now possible to define components using a functional style, similar to local components.
- **Integrated Testing Framework**: The SDK includes a built-in testing framework for validating your provider implementation code. Much-improved support for testing of component resources with mocks.

## Defining and Testing a Custom Resource

Let's look at how easy it is to define a custom resource. Using the `infer` package, you define your resource types using Go structs. For example, a simple "Hello World" resource might look like this:


```go
func main() {
	p.RunProvider("greetings", "0.1.0", provider())
}

func provider() p.Provider {
	p, _ := infer.NewProviderBuilder().
		WithResources(
			infer.Resource(&HelloWorld{}),
		).
		Build()
	return p
}

// Each resource has a controlling struct.
type HelloWorld struct{}

// Each resource has in input struct, defining what arguments it accepts.
type HelloWorldArgs struct {
	Name string `pulumi:"name"`
	Loud *bool `pulumi:"loud,optional"`
}

// Each resource has a state, describing the fields that exist on the created resource.
type HelloWorldState struct {
	HelloWorldArgs
	Message string `pulumi:"message"`
}

func (l *HelloWorldState) Annotate(a infer.Annotator) {
    a.Describe(&l, "A Hello World resource")
	a.Describe(&l.Name, "Who to say hello to.")
	a.SetDefault(&l.Name, "user-")
	a.Describe(&l.Loud, "Indicates whether to give a LOUD greeting.")
	a.Describe(&l.Message, "The greeting message.")
}
```

You then implement the necessary methods for the resource's lifecycle. At a minimum, you need to implement Create. 

```go
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

This minimal code defines a fully-functional resource! The SDK handles the gRPC server communication with the Pulumi engine and automatically generates the necessary schema for multi-language support.

Testing your custom resource is also made easier with the SDK's **built-in testing framework**. This framework includes **Lifecycle testing**, specifically designed to exercise the CRUD methods of your custom resources. You can use the `integration` package and its `integration.Server` test harness to simulate Pulumi engine interactions.

To test a custom resource, you typically:
1. Create an instance of your provider.
2. Set up an `integration.Server` instance, passing your provider to it.
3. Use the server methods to simulate the Pulumi engine interacting with your resource.

```go
func TestHelloWorldLifecycle(t *testing.T) {
	server, err := integration.NewServer(t.Context(), "greetings", semver.Version{Minor: 1},
		integration.WithProvider(provider()),
	)
	require.NoError(t, err)

	// Test the lifecycle methods of the HelloWorld resource.
	integration.LifeCycleTest{
		Resource: "pkg:index:HelloWorld",
		Create: integration.Operation{
			Inputs: property.NewMap(map[string]property.Value{
				"name": property.New("tester"),
				"loud", property.New(true),
			}),
			Hook: func(inputs, output property.Map) {
				message := output.Get("message").AsString()
				assert.Equal(t, "Hello, tester", message)
			},
		},
	}.Run(t, server)
}
```

This approach allows you to fully test the business logic within your resource's CRUD methods by providing simulated inputs and checking the resulting resource state.

For more information, see ["Pulumi Provider SDK"](/docs/iac/using-pulumi/extending-pulumi/pulumi-provider-sdk/).

## Defining and Testing a Component Resource

Beyond simple resources, providers can also define **Component Resources**. Components are higher-level abstractions that encapsulate multiple child resources working together to implement a specific capability. They are perfect for codifying organizational standards and best practices into reusable (cross-language!) building blocks.

The Pulumi Provider SDK v1.0.0 introduces support for defining components using a **functional style**, similar to how you might define a local component within a single program. This provides a streamlined way to build components. Here's an example using the functional style:

```go
func provider() p.Provider {
	p, _ := infer.NewProviderBuilder().
		WithComponents(
			infer.ComponentF(NewRandomLogin),
		).
		Build()
	return p
}

type RandomLoginArgs struct {
	Prefix pulumi.StringInput `pulumi:"prefix"`
}

type RandomLogin struct {
	pulumi.ResourceState
	RandomLoginArgs

	Username pulumi.StringOutput `pulumi:"username"`
	Password pulumi.StringOutput `pulumi:"password"`
}

func NewRandomLogin(ctx *pulumi.Context, name string, args RandomLoginArgs, opts ...pulumi.ResourceOption) (*RandomLogin, error) {
	comp := &RandomLogin{}
	err := ctx.RegisterComponentResource(p.GetTypeToken(ctx), name, comp, opts...)
	if err != nil {
		return nil, err
	}

	username, err := random.NewRandomPet(ctx, name+"-username", &random.RandomPetArgs{
		Prefix: args.Prefix,
	}, pulumi.Parent(comp))
	if err != nil {
		return nil, err
	}
	comp.Username = username.ID().ToStringOutput()

	password, err := random.NewRandomPassword(ctx, name+"-password", &random.RandomPasswordArgs{
		Length: pulumi.Int(12),
	}, pulumi.Parent(comp))
	if err != nil {
		return nil, err
	}
	comp.Password = password.Result

	return comp, nil
}

func (l *RandomLogin) Annotate(a infer.Annotator) {
	a.Describe(&l, "Generate a random login credential (a username and password).")
	a.Describe(&l.Prefix, "An optional prefix for the generated username.")
	a.SetDefault(&l.Prefix, "user-")
}
```

Testing component resources is also fully supported with the integration framework. You can write tests to exercise your component function and **simulate the interactions between your component and its child resources** using **component testing with mocks**. This helps ensure your components correctly wire up child resources and produce the expected outputs.

```go
func TestRandomLogin(t *testing.T) {
	provider, err := provider()
	require.NoError(t, err)
	server, err := integration.NewServer(t.Context(),
		"random-login",
		semver.Version{Minor: 1},
		integration.WithProvider(provider),
		integration.WithMocks(&integration.MockResourceMonitor{
			NewResourceF: func(args integration.MockResourceArgs) (string, property.Map, error) {
				switch {
				case args.TypeToken == "random:index/randomPet:RandomPet" && args.Name == "login-username":
					assert.Equal(t, "foo", args.Inputs.Get("prefix").AsString())
					return "user", property.Map{}, nil

				case args.TypeToken == "random:index/randomPassword:RandomPassword" && args.Name == "login-password":
					assert.Equal(t, 12.0, args.Inputs.Get("length").AsNumber())
					return args.Name, property.NewMap(map[string]property.Value{
						"result": property.New("12345").WithSecret(true),
					}), nil

				return "", property.Map{}, nil
			},
		}),
	)
	require.NoError(t, err)

	// test the "random-login:RandomLogin" component
	resp, err := server.Construct(p.ConstructRequest{
		Urn: "urn:pulumi:stack::project::random-login:index:RandomLogin::login",
		Inputs: property.NewMap(map[string]property.Value{
			"prefix": property.New("foo"),
		}),
	})
	require.NoError(t, err)

	require.Equal(t, property.NewMap(map[string]property.Value{
		"username": property.New("user"),
		"password": property.New("12345").WithSecret(true),
	}), resp.State)
}
```

For more information about component resources, see the blog post ["Announcing the Next-Generation of Pulumi Components: Enabling Infrastructure Abstractions"](../pulumi-components/index.md).

## Seamless Multi-Language Support and Sharing

A major advantage of using the Pulumi Provider SDK is that your provider, once written in Go, can be used in **any Pulumi program**, in **any supported language** (TypeScript, Python, Go, .NET, Java, or YAML). The SDK's automatic schema generation takes care of creating the necessary language-specific SDKs, enabling **cross-language consumption** without manual effort.

Packaging and publishing your provider for others to use, whether within your organization or publicly, is a key step. The Pulumi documentation provides detailed guides on how to package and share your custom providers. For more information, see ["Publishing packages"](/docs/iac/using-pulumi/extending-pulumi/publishing-packages/).

## Get Started Today!

The v1.0.0 release of the Pulumi Provider SDK represents a significant step forward in simplifying and accelerating the development of Pulumi providers. By focusing on a code-first approach, automatic schema generation, and providing a robust testing framework, we are empowering engineers to integrate Pulumi with virtually any service or tool.

We encourage you to explore the Pulumi Provider SDK, build your own integrations, and contribute to the growing ecosystem of Pulumi providers.
Check out our documentation on ["Extending Pulumi"][ext]. Also, check out the examples in the repository and dive into the package-level documentation.

**Explore the Pulumi Provider SDK on GitHub:** https://github.com/pulumi/pulumi-go-provider

We're excited to see what you build! Share your feedback with us on the [Pulumi Community Slack] or open an issue in the [pulumi/pulumi-go-provider GitHub repository][pgp].

[Pulumi Community Slack]: https://slack.pulumi.com/
[pgp]: https://github.com/pulumi/pulumi-go-provider
[ext]: /docs/iac/using-pulumi/extending-pulumi/