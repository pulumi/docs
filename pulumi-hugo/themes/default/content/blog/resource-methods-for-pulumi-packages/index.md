---
title: "Introducing Resource Methods for Pulumi Packages"
date: 2021-10-11T08:00:00-07:00
draft: false
meta_desc: It's now possible to provide resource methods from Pulumi Packages
meta_image: pulumi-mlc-packages.png
authors:
    - justin-vanpatten
tags:
    - packages
---

It's now possible to provide resource methods from Pulumi Packages. Resource methods are similar to functions, but instead of being exposed as top-level functions in a module, methods are exposed as methods on a resource class. This allows for a more object-oriented approach to exposing functionality&mdash;operations performed by a resource (that potentially use the resource's state) can now be exposed as methods on the resource. Resource methods can be implemented once, in your language of choice, and made available to users in all Pulumi languages.

<!--more-->

When authoring component resources, it's often useful to provide additional functionality through methods on the component. For example, the `Cluster` component in the [`eks`]({{< relref "/docs/reference/pkg/eks" >}}) package has a [`getKubeconfig`](https://github.com/pulumi/pulumi-eks/blob/700d73e961976e58762cb9c723ad2fa838052f46/nodejs/eks/cluster.ts#L1482) method that can be used to generate a kubeconfig for authentication with the cluster that does not use the default AWS credential provider chain, but is instead scoped based on the passed-in arguments. Until now, that method has only been available from JavaScript/TypeScript (the language the `Cluster` component was written in). With the new support for resource methods for Pulumi Packages, we can make this method available to all the Pulumi languages, which is exactly what we've done in pulumi-eks [v0.34.0](https://github.com/pulumi/pulumi-eks/releases/tag/v0.34.0).

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```typescript
const cluster = new eks.Cluster("mycluster");
const kubeconfig = cluster.getKubeconfig(...);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
cluster = eks.Cluster("mycluster")
kubeconfig = cluster.get_kubeconfig(...)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var cluster = new Cluster("mycluster");
var kubeconfig = cluster.GetKubeconfig(...);
```

{{% /choosable %}}

{{% choosable language go %}}

```go
cluster, err := eks.NewCluster(ctx, "mycluster", nil)
if err != nil {
    return err
}
kubeconfig, err := cluster.GetKubeconfig(ctx, &eks.ClusterGetKubeconfigArgs{...})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% /chooser %}}

This post will show how you can provide resource methods from your [component packages]({{< relref "/docs/guides/pulumi-packages" >}}).

## Authoring Methods

It's always been possible to provide module-level functions from Pulumi Packages. For example, the [`aws`]({{< relref "/docs/reference/pkg/aws" >}}) package provides many module-level functions, such as the [`getAmi`]({{< relref "/docs/reference/pkg/aws/ec2/getami" >}}) function, which can be used to get the ID of an existing Amazon Machine Image (AMI). Functions are declared in the package's [schema]({{< relref "/docs/guides/pulumi-packages/schema" >}}), and their functionality is implemented in the provider through the `Invoke` remote procedure call (RPC).

Methods are authored in a similar manner to functions. Methods are declared in the schema and implemented in the provider's `Call` RPC (similar to `Invoke`).

Let's walk through an example. We'll author a `Message` component that accepts a message as input. The component then provides a `getMessage` method that accepts a recipient name and returns the message customized for the recipient. To get started authoring a component package, refer to the [package]({{< relref "/docs/guides/pulumi-packages" >}}) documentation.

### Schema

We'll start with declaring the method and component in the [Pulumi schema]({{< relref "/docs/guides/pulumi-packages/schema" >}}). First, define the function representing the method:

```json
  "functions": {
    "example:index:Message/getMessage": {
      "inputs": {
        "properties": {
          "__self__": {
            "$ref": "#/resources/example:index:Message"
          },
          "recipient": {
            "type": "string"
          }
        },
        "required": ["__self__", "recipient"]
      },
      "outputs": {
        "properties": {
          "result": {
            "type": "string"
          }
        },
        "required": ["result"]
      }
    }
  },
```

Our method has two required arguments: `__self__` and `recipient`. `__self__` is a special input required by all methods that represents the component resource and is typed as such. The method has one result named `result`.

Next, define our `Message` component:

```json
  "resources": {
    "example:index:Message": {
      "isComponent": true,
      "inputProperties": {
        "message": {
          "type": "string"
        },
      },
      "requiredInputs": ["message"],
      "properties": {
        "message": {
          "type": "string"
        },
      },
      "required": ["message"],
      "methods": {
        "getMessage": "example:index:Message/getMessage"
      }
    }
  },
```

Our component has a single required input/output property: `message`. The method is specified in the `methods` property, which references the method's function definition: `"getMessage": "example:index:Message/getMessage"`.

Here's our schema all together:

```json
{
  "version": "0.0.1",
  "name": "example",
  "functions": {
    "example:index:Message/getMessage": {
      "inputs": {
        "properties": {
          "__self__": {
            "$ref": "#/resources/example:index:Message"
          },
          "recipient": {
            "type": "string"
          }
        },
        "required": ["__self__", "recipient"]
      },
      "outputs": {
        "properties": {
          "result": {
            "type": "string"
          }
        },
        "required": ["result"]
      }
    }
  },
  "resources": {
    "example:index:Message": {
      "isComponent": true,
      "inputProperties": {
        "message": {
          "type": "string"
        },
      },
      "requiredInputs": ["message"],
      "properties": {
        "message": {
          "type": "string"
        },
      },
      "required": ["message"],
      "methods": {
        "getMessage": "example:index:Message/getMessage"
      }
    }
  },
  "language": {
    "csharp": {
      "packageReferences": {
        "Pulumi": "3.12"
      },
      "liftSingleValueMethodReturns": true
    },
    "go": {
      "liftSingleValueMethodReturns": true
    },
    "nodejs": {
      "devDependencies": {
        "@types/node": "latest"
      },
      "liftSingleValueMethodReturns": true
    },
    "python": {
      "liftSingleValueMethodReturns": true
    }
  }
}
```

To make it easier for users of our method, we also set `"liftSingleValueMethodReturns": true` for each language, which makes single-value methods return the single value directly, rather than wrapping the results in a `Result` type.

### Component Implementation

We can implement the component and make it available to any Pulumi language. We're going to show some implementation examples in TypeScript/JavaScript, Python, and Go.

Here's the implementation of the `Message` component:

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

interface MessageArgs {
    message: pulumi.Input<string>;
}

class Message extends pulumi.ComponentResource {
    public readonly message!: pulumi.Output<string>;

    constructor(name: string, args: MessageArgs, opts?: pulumi.ComponentResourceOptions) {
        const props = { message: args?.message }
        super("example:index:Message", name, props, opts);

        if (opts?.urn) {
            // Skip further initialization when being constructed from a resource reference.
            return;
        }

        this.registerOutputs(props);
    }

    getMessage(recipient: pulumi.Input<string>): pulumi.Output<string> {
        return pulumi.iterpolate `${recipient}, ${this.message}!`;
    }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from typing import Optional

import pulumi

class Message(pulumi.ComponentResource):
    @property
    @pulumi.getter
    def message(self) -> pulumi.Output[str]:
        return pulumi.get(self, "message")

    def __init__(self,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 message: Optional[pulumi.Input[str]] = None) -> None:

        args = {"message": message}
        super().__init__("example:index:Message", resource_name, args, opts)

        if opts and opts.urn:
            # Skip further initialization when being constructed from a resource reference.
            return

        self.register_outputs(args)

    def get_message(self, recipient: pulumi.Input[str]) -> pulumi.Output[str]:
        return pulumi.Output.concat(recipient, ", ", self.message, "!")
```

{{% /choosable %}}
{{% choosable language csharp %}}

[Authoring multi-language components in .NET](https://github.com/pulumi/pulumi/issues/5488) is not yet supported.

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"errors"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Message struct {
	pulumi.ResourceState
	Message  pulumi.StringOutput `pulumi:"message"`
}

type MessageArgs struct {
	Message  pulumi.StringInput `pulumi:"message"`
}

func NewMessage(ctx *pulumi.Context, name string, args *MessageArgs, opts ...pulumi.ResourceOption) (*Message, error) {
	if args == nil {
		return nil, errors.New("args is required")
	}

	message := &Message{}
	err := ctx.RegisterComponentResource("example:index:Message", name, message, opts...)
	if err != nil {
		return nil, err
	}

	message.Message = args.Message.ToStringOutput()
	if err := ctx.RegisterResourceOutputs(message, pulumi.Map{
		"message":  args.Message,
	}); err != nil {
		return nil, err
	}

	return message, nil
}

type GetMessageArgs struct {
	Recipient pulumi.StringInput `pulumi:"recipient"`
}

func (c *Message) GetMessage(args *GetMessageArgs) StringOutput {
	return pulumi.Sprintf("%s, %s!", args.Recipient, c.Message)
}
```

{{% /choosable %}}

{{% /chooser %}}

### Provider RPCs

Next, wire up the provider RPCs with the component implementation:

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as provider from "@pulumi/pulumi/provider";

class Provider implements provider.Provider {
    public readonly version = "0.0.1";

    constructor() {
        // Register any resources that can come back as resource references that need to be rehydrated.
        pulumi.runtime.registerResourceModule("example", "index", {
            version: this.version,
            construct: (name, type, urn) => {
                switch (type) {
                    case "example:index:Message":
                        return new Component(name, <any>undefined, { urn });
                    default:
                        throw new Error(`unknown resource type ${type}`);
                }
            },
        });
    }

    async construct(name: string, type: string, inputs: pulumi.Inputs,
              options: pulumi.ComponentResourceOptions): Promise<provider.ConstructResult> {
        if (type != "example:index:Message") {
            throw new Error(`unknown resource type ${type}`);
        }

        const message = new Message(name, <MessageArgs>inputs, options);
        return {
            urn: message.urn,
            state: inputs,
        };
    }

    async call(token: string, inputs: pulumi.Inputs): Promise<provider.InvokeResult> {
        switch (token) {
            case "example:index:Message/getMessage":
                const self: Component = inputs.__self__;
                return {
                    outputs: {
                        result: self.getMessage(inputs.recipient),
                    },
                };

            default:
                throw new Error(`unknown method ${token}`);
        }
    }
}

export function main(args: string[]) {
    return provider.main(new Provider(), args);
}

main(process.argv.slice(2));
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from typing import Optional
import sys

import pulumi
import pulumi.provider as provider


class Provider(provider.Provider):
    VERSION = "0.0.1"

    class Module(pulumi.runtime.ResourceModule):
        def version(self):
            return Provider.VERSION

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "example:index:Message":
                return Component(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")

    def __init__(self):
        super().__init__(Provider.VERSION)
        pulumi.runtime.register_resource_module("example", "index", Provider.Module())

    def construct(self, name: str, resource_type: str, inputs: pulumi.Inputs,
                  options: Optional[pulumi.ResourceOptions] = None) -> provider.ConstructResult:

        if resource_type != "example:index:Message":
            raise Exception(f"unknown resource type {resource_type}")

        message = Message(name, opts=options, message=inputs["message"])

        return provider.ConstructResult(
            urn=component.urn,
            state=inputs)

    def call(self, token: str, args: pulumi.Inputs) -> provider.CallResult:
        if token != "example:index:Message/getMessage":
            raise Exception(f'unknown method {token}')

        message: Message = args["__self__"]
        outputs = {
            "result": message.get_message(args["recipient"])
        }
        return provider.CallResult(outputs=outputs)


if __name__ == "__main__":
    provider.main(Provider(), sys.argv[1:])
```

{{% /choosable %}}
{{% choosable language csharp %}}

[Authoring multi-language components in .NET](https://github.com/pulumi/pulumi/issues/5488) is not yet supported.

{{% /choosable %}}
{{% choosable language go %}}

```go
import (
	"errors"
	"fmt"

	"github.com/blang/semver"

	"github.com/pulumi/pulumi/pkg/v3/resource/provider"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/cmdutil"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	pulumiprovider "github.com/pulumi/pulumi/sdk/v3/go/pulumi/provider"
)

const providerName = "example"
const version = "0.0.1"

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	if typ != "example:index:Message" {
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}
	r = &Component{}
	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type GetMessageResult struct {
	Result pulumi.StringOutput `pulumi:"result"`
}

func main() {
	pulumi.RegisterResourceModule("example", "index", &module{semver.MustParse(version)})

	if err := provider.MainWithOptions(provider.Options{
		Name:    providerName,
		Version: version,
		Construct: func(ctx *pulumi.Context, typ, name string, inputs pulumiprovider.ConstructInputs,
			options pulumi.ResourceOption) (*pulumiprovider.ConstructResult, error) {

			if typ != "example:index:Message" {
				return nil, fmt.Errorf("unknown resource type %s", typ)
			}

			args := &MessageArgs{}
			if err := inputs.CopyTo(args); err != nil {
				return nil, fmt.Errorf("setting args: %w", err)
			}

			message, err := NewMessage(ctx, name, args, options)
			if err != nil {
				return nil, fmt.Errorf("creating component: %w", err)
			}

			return pulumiprovider.NewConstructResult(message)
		},
		Call: func(ctx *pulumi.Context, tok string, args pulumiprovider.CallArgs) (*pulumiprovider.CallResult, error) {
			if tok != "example:index:Message/getMessage" {
				return nil, fmt.Errorf("unknown method %s", tok)
			}

			methodArgs := &GetMessageArgs{}
			res, err := args.CopyTo(methodArgs)
			if err != nil {
				return nil, fmt.Errorf("setting args: %w", err)
			}
			message := res.(*Message)

			result, message.GetMessage(methodArgs)
			return pulumiprovider.NewCallResult(&GetMessageResult{
                Result: result
            })
		},
	}); err != nil {
		cmdutil.ExitError(err.Error())
	}
}
```

{{% /choosable %}}

{{% /chooser %}}

The `Construct` RPC is called when creating an instance of the component. The `Call` RPC is called when a method is called.

### Using the Component

Now we can build and try out using the component and its method from any Pulumi language:

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```typescript
const component = new example.Message("mycomponent", {
    message: "hello world",
});
export const message = component.getMessage({ recipient: "Alice" }); // Exports "Alice, hello world!"
```

{{% /choosable %}}
{{% choosable language python %}}

```python
component = example.Message("mycomponent", message="hello world")
message = component.get_message(recipient="Alice")
pulumi.export("message", message) # Exports "Alice, hello world!"
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var component = new Message("mycomponent", new MessageArgs
{
    Message = "hello world",
});
// Exports "Alice, hello world!"
this.Message = component.GetMessage(new MessageGetMessageArgs
{
    Recipient = "Alice",
});
```

{{% /choosable %}}

{{% choosable language go %}}

```go
component, err := example.NewMessage(ctx, "mycomponent", &example.MessageArgs{
	Message: "hello world",
})
if err != nil {
	return err
}
message, err := component.GetMessage(ctx, &example.MessageGetMessageArgs{Recipient: "Alice"})
if err != nil {
	return err
}
pulumi.Export("message", message) // Exports "Alice, hello world!"
```

{{% /choosable %}}

{{% /chooser %}}

## Wrapping Up

With support for resource methods for Pulumi Packages, you can now create component resources with methods and make them available to use from any Pulumi language. We look forward to seeing the components you create!

👉 [Author your first Pulumi Package]({{< relref "/docs/guides/pulumi-packages" >}})
