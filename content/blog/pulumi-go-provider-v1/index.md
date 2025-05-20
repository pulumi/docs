---
title: "The Pulumi Go Provider SDK is Now Generally Available"
date: 2025-05-20
draft: false
allow_long_title: true

meta_desc: "Pulumi Go Provider SDK is now v1.0: Build custom infrastructure providers in hours, not weeks, while unlocking cross-team collaboration and standardization"
meta_image: meta.png
authors:
    - eron-wright
tags:
    - releases 
    - platform-teams
    - features
    - iac
    - components
---

At Pulumi, we are committed to accelerating your cloud infrastructure journey by eliminating barriers between your teams and the tools they need. Today, we're thrilled to announce a game-changing milestone that puts unprecedented power in your hands: the **v1.0.0 release of the Pulumi Go Provider SDK**!

<!--more-->

## Unlock the Full Potential of Your Cloud Ecosystem

The Pulumi Go Provider SDK is a transformative framework that enables you to integrate **any** service, tool, or API into your infrastructure as code workflows. After extensive development and testing with customers, this framework is now **stable and production-ready** for your most critical infrastructure needs.

Pulumi has worked diligently to bring this SDK to maturity, incorporating feedback from enterprise users and leveraging it internally to build production providers like the [Docker Build Provider](/registry/packages/docker-build). With v1.0.0, building robust, multi-language Pulumi providers is more accessible than ever.


## Key Enhancements for Your Team

The Pulumi Go Provider SDK delivers capabilities that benefit everyone from platform engineers to DevOps professionals:

- **Go 1.24 Support**: Utilize the latest language features and performance improvements
- **Intuitive Provider Builder API**: A fluent, developer-friendly API that eliminates boilerplate and accelerates provider development
- **Functional-Style Components**: Create reusable infrastructure building blocks with a natural, functional programming style
- **Enterprise-Grade Testing Framework**: Ensure reliability with comprehensive testing capabilities for both resources and components

For a complete technical overview, see our comprehensive [Pulumi Go Provider SDK documentation](/docs/iac/using-pulumi/extending-pulumi/pulumi-provider-sdk/).

## Defining and Testing a Custom Resource

## Creating a Custom Resource in Minutes, Not Days

Let's see how the SDK transforms the provider development experience. Using the `infer` package, you define your resource types using straightforward Go structs:

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

You then implement the necessary methods for the resource's lifecycle with surprising simplicity: 

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

This minimal code creates a fully-functional resource that your teams can use in their infrastructure code! The SDK handles all the complex gRPC communication with the Pulumi engine and automatically generates the necessary schema for multi-language support.

For detailed step-by-step instructions on building your own provider, check out our [Build a Provider guide](/docs/iac/using-pulumi/extending-pulumi/build-a-provider/).

## Confidence Through Comprehensive Testing

One of the biggest challenges with custom infrastructure providers is ensuring they're reliable. The SDK's built-in testing framework solves this with targeted capabilities:

- **Lifecycle Testing**: Verify your resources' CRUD operations function correctly
- **Component Testing**: Validate complex resource compositions with mock capabilities
- **Integration Testing**: Ensure your provider works seamlessly with the Pulumi ecosystem

Here's how easy it is to test your custom resource:

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

For more information, see ["Pulumi Go Provider SDK"](/docs/iac/using-pulumi/extending-pulumi/pulumi-provider-sdk/).

## Standardize Infrastructure with Powerful Component Resources

Beyond simple resources, providers can also define **Component Resources**. Components are higher-level abstractions that encapsulate multiple child resources working together to implement a specific capability. They are perfect for codifying organizational standards and best practices into reusable (cross-language!) building blocks.

The Pulumi Go Provider SDK v1.0.0 introduces support for defining components using a **functional style**, similar to how you might define a local component within a single program. This provides a streamlined way to build components. Here's an example using the functional style:

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

For a deep dive into creating component resources, see our comprehensive [Build a Component guide](/docs/iac/using-pulumi/extending-pulumi/build-a-component/).

And testing components is equally straightforward:

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

A major advantage of using the Pulumi Go Provider SDK is that your provider, once written in Go, can be used in **any Pulumi program**, in **any supported language** (TypeScript, Python, Go, .NET, Java, or YAML). The SDK's automatic schema generation takes care of creating the necessary language-specific SDKs, enabling **cross-language consumption** without manual effort.

Packaging and publishing your provider for others to use, whether within your organization or publicly, is a key step. Follow our [Publishing Packages guide](/docs/iac/using-pulumi/extending-pulumi/publishing-packages/) for detailed instructions on distributing your custom provider.

## Understanding Provider Schema

The SDK automatically generates a schema for your provider based on the Go types and annotations you define. This schema describes the resources, their inputs and outputs, and documentation. For more details on how schema generation works and how to customize it, check out our [Schema documentation](/docs/iac/using-pulumi/extending-pulumi/schema/).

## Get Started Today!

The v1.0.0 release of the Pulumi Go Provider SDK represents a significant step forward in simplifying and accelerating the development of Pulumi providers. By focusing on a code-first approach, automatic schema generation, and providing a robust testing framework, we are empowering engineers to integrate Pulumi with virtually any service or tool.

We encourage you to explore the Pulumi Go Provider SDK, build your own integrations, and contribute to the growing ecosystem of Pulumi providers.
Start with our [Extending Pulumi overview documentation](/docs/iac/using-pulumi/extending-pulumi/) to get a complete picture of the possibilities.

1. **Explore our documentation** on [Extending Pulumi](/docs/iac/using-pulumi/extending-pulumi/)
2. **Review examples** in the [GitHub repository](https://github.com/pulumi/pulumi-go-provider)
3. **Learn how to build a provider** with our [step-by-step guide](/docs/iac/using-pulumi/extending-pulumi/build-a-provider/)
4. **Identify your first integration** - what custom service would provide the most value to your team?
5. **Join our community** in the [Pulumi Community Slack](https://slack.pulumi.com/) to learn from others building custom providers
6. Share your feedback with us on the in Slack or by opening an issue in the [pulumi/pulumi-go-provider GitHub repository](https://github.com/pulumi/pulumi-go-provider).

Happy building!
