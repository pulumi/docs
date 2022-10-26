---
title: Upgrading to Pulumi 3.0
meta_desc: This page provides instructions for upgrading to Pulumi 3.0
no_on_this_page: true
---

Pulumi 3.0 is generally available. It’s simple to upgrade:

1. [Install or upgrade to the 3.0 CLI](/docs/get-started/install/).
2. Review the updated CLI behaviors listed below.
3. Update each of your Pulumi programs to utilize the new version of the SDK.

## Updated CLI behavior in Pulumi 3.0

Previously, when using the `--stack` option on CLI commands, Pulumi would inconsistently set that stack as the current stack. In Pulumi 3.0, this behavior has now standardized and will *NOT* set the stack as the current stack. This affects the following commands:

* `pulumi cancel`
* `pulumi config refresh`
* `pulumi destroy`
* `pulumi import`
* `pulumi logs`
* `pulumi preview`
* `pulumi refresh`
* `pulumi stack *`
* `pulumi state`
* `pulumi up`
* `pulumi watch`

## Required updates to Pulumi programs

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language "javascript,typescript" %}}

### Update to the new SDK version

```bash
npm install @pulumi/pulumi@^3.0.0
```

### Changes to pulumi.runtime.Mocks

The signature of the `setMocks` function has changed with the introduction of the `pulumi.runtime.MockResourceArgs` and `pulumi.runtime.MockCallArgs` types. If you use `setMocks` in your code, you'll need to update to these new types.

```javascript
// before
pulumi.runtime.setMocks({
    newResource: function(type: string, name: string, inputs: any): {id: string, state: any} {
        switch (type) {
            case "aws:ec2/securityGroup:SecurityGroup":
                return {
                    id: "sg-12345678",
                    state: {
                        ...inputs,

                        arn: "arn:aws:ec2:us-west-2:123456789012:security-group/sg-12345678",
                        name: inputs.name || name + "-sg",
                    },
                };
            case "aws:ec2/instance:Instance":
                return {
                    id: "i-1234567890abcdef0",
                    state: {
                        ...inputs,

                        arn: "arn:aws:ec2:us-west-2:123456789012:instance/i-1234567890abcdef0",
                        instanceState: "running",
                        primaryNetworkInterfaceId: "eni-12345678",
                        privateDns: "ip-10-0-1-17.ec2.internal",
                        publicDns: "ec2-203-0-113-12.compute-1.amazonaws.com",
                        publicIp: "203.0.113.12",
                    },
                };
            default:
                return {
                    id: inputs.name + "_id",
                    state: {
                        ...inputs,
                    },
                };
        }
    },
    call: function(token: string, args: any, provider?: string) {
    switch (token) {
        case "aws:ec2/getAmi:getAmi":
            return {
                "architecture": "x86_64",
                "id": "ami-0eb1f3cdeeb8eed2a",
            };
        default:
            return args;
    }
},
});

// after
pulumi.runtime.setMocks({
    newResource: function(args: pulumi.runtime.MockResourceArgs): {id: string, state: any} {
        switch (args.type) {
            case "aws:ec2/securityGroup:SecurityGroup":
                return {
                    id: "sg-12345678",
                    state: {
                        ...args.inputs,

                        arn: "arn:aws:ec2:us-west-2:123456789012:security-group/sg-12345678",
                        name: args.inputs.name || name + "-sg",
                    },
                };
            case "aws:ec2/instance:Instance":
                return {
                    id: "i-1234567890abcdef0",
                    state: {
                        ...args.inputs,

                        arn: "arn:aws:ec2:us-west-2:123456789012:instance/i-1234567890abcdef0",
                        instanceState: "running",
                        primaryNetworkInterfaceId: "eni-12345678",
                        privateDns: "ip-10-0-1-17.ec2.internal",
                        publicDns: "ec2-203-0-113-12.compute-1.amazonaws.com",
                        publicIp: "203.0.113.12",
                    },
                };
            default:
                return {
                    id: args.inputs.name + "_id",
                    state: {
                        ...args.inputs,
                    },
                };
        }
    },
    call: function(args: MockCallArgs) {
        switch (args.token) {
            case "aws:ec2/getAmi:getAmi":
                return {
                    "architecture": "x86_64",
                    "id": "ami-0eb1f3cdeeb8eed2a",
                };
            default:
                return args.inputs;
        }
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

### Update to the new SDK version

Modify your `requirements.txt` file to update the Pulumi SDK and any providers you use, like this:

```
pulumi>=3.0.0,<4.0.0
pulumi-aws>=4.0.0,<5.0.0
```

Then run `pip install`:

```bash
pip install -r requirements.txt
```

### Dictionary snake_case/camelCase Key Translation Fixes in Provider Python SDKs

Prior versions of Pulumi provider Python SDKs would unintentionally translate keys of user-defined `dict` inputs (e.g. AWS `tags`) from snake_case to camelCase (and vice versa for outputs) if the key happened to exist in the provider's internal translation tables. Additionally, some provider SDKs did not consistently translate keys of nested data structures. All 3.0-based Pulumi provider Python SDKs have addressed these issues:

* Dictionary keys in user-defined `dict`s are no longer modified.
* Dictionary keys in nested outputs are now consistently snake_case. If you're accessing camelCase keys from such output classes, you need to update your code to access the values via the class's snake_case property getters. A warning will be logged when accessing values from output classes using camelCase keys.

```python
from pulumi import export
from pulumi_gcp import compute

instance = compute.Instance("instance", ...)

# before
export("ip", instance.network_interfaces[0]["accessConfigs"][0]["natIp"])

# after
export("ip", instance.network_interfaces[0].access_configs[0].nat_ip)
```

### Changes to pulumi.runtime.Mocks

The signatures of the `new_resource` and `call` methods have changed with the introduction of the `pulumi.runtime.MockResourceArgs` and `pulumi.runtime.MockCallArgs` types. If you use `new_resource` and `call` in your code, you'll need to update to these new types.

```python
# before
class MyMocks(pulumi.runtime.Mocks):
    def new_resource(self, token, name, inputs, provider, id_):
        outputs = inputs
        if token == "aws:ec2/instance:Instance":
            outputs = {
                **inputs,
                "publicIp": "203.0.113.12",
                "publicDns": "ec2-203-0-113-12.compute-1.amazonaws.com",
            }
        return [name + '_id', outputs]
    def call(self, token, args, provider):
        if token == "aws:ec2/getAmi:getAmi":
            return {
                "architecture": "x86_64",
                "id": "ami-0eb1f3cdeeb8eed2a",
            }
        return {}

pulumi.runtime.set_mocks(MyMocks())

# after
class MyMocks(pulumi.runtime.Mocks):
    def new_resource(self, args: pulumi.runtime.MockResourceArgs):
        outputs = args.inputs
        if args.token == "aws:ec2/instance:Instance":
            outputs = {
                **args.inputs,
                "publicIp": "203.0.113.12",
                "publicDns": "ec2-203-0-113-12.compute-1.amazonaws.com",
            }
        return [args.name + '_id', args.outputs]
    def call(self, args: pulumi.runtime.MockCallArgs):
        if args.token == "aws:ec2/getAmi:getAmi":
            return {
                "architecture": "x86_64",
                "id": "ami-0eb1f3cdeeb8eed2a",
            }
        return {}

pulumi.runtime.set_mocks(MyMocks())
```

{{% /choosable %}}
{{% choosable language go %}}

### Update to the new SDK version

Modify your `go.mod` file to update the Pulumi SDK and any providers you use, like this:

```
require (
    github.com/pulumi/pulumi/sdk/v3 v3.0.0
    github.com/pulumi/pulumi-aws/sdk/v4 v4.0.0
)
```

Then run `go mod download`

### Remove any `Apply<TypeName>` calls

In order to improve the performance of our Go SDK, we have removed:

* `Apply<TypeName>`
* `Apply`
* `ApplyWithContext`

We now suggest that you use:

* `ApplyT`
* `ApplyTWithContext`

When using ApplyT, remember to cast the result to the Output type.

```go
//before
containerDef := image.ImageName.ApplyString(func(name string) (string, error) {
    return name, nil
})

//after
containerDef := image.ImageName.ApplyT(func(name string) (string, error) {
    return name, nil
}).(pulumi.StringOutput)
```

### Changes to pulumi.runtime.Mocks

The signatures of the `NewResource` and `Call` functions have changed with the introduction of the `pulumi.runtime.MockResourceArgs` and `pulumi.runtime.MockCallArgs` types. If you use `setMocks` in your code, you'll need to update to these new types.

```go
//before
func (mocks) NewResource(token, name string, inputs resource.PropertyMap, provider, id string) (string, resource.PropertyMap, error) {
	outputs := inputs.Mappable()
	if token == "aws:ec2/instance:Instance" {
		outputs["publicIp"] = "203.0.113.12"
		outputs["publicDns"] = "ec2-203-0-113-12.compute-1.amazonaws.com"
	}
	return name + "_id", resource.NewPropertyMapFromMap(outputs), nil
}

func (mocks) Call(token string, args resource.PropertyMap, provider string) (resource.PropertyMap, error) {
	outputs := map[string]interface{}{}
	if token == "aws:ec2/getAmi:getAmi" {
		outputs["architecture"] = "x86_64"
		outputs["id"] = "ami-0eb1f3cdeeb8eed2a"
	}
	return resource.NewPropertyMapFromMap(outputs), nil
}

//after
func (mocks) NewResource(args pulumi.MockResourceArgs) (string, resource.PropertyMap, error) {
	outputs := args.Inputs.Mappable()
	if args.Token == "aws:ec2/instance:Instance" {
		outputs["publicIp"] = "203.0.113.12"
		outputs["publicDns"] = "ec2-203-0-113-12.compute-1.amazonaws.com"
	}
	return args.Name + "_id", resource.NewPropertyMapFromMap(outputs), nil
}

func (mocks) Call(args pulumi.MockCallArgs) (resource.PropertyMap, error) {
	outputs := map[string]interface{}{}
	if args.Token == "aws:ec2/getAmi:getAmi" {
		outputs["architecture"] = "x86_64"
		outputs["id"] = "ami-0eb1f3cdeeb8eed2a"
	}
	return resource.NewPropertyMapFromMap(outputs), nil
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

### Update to the new SDK version

Modify your project file to update the Pulumi SDK and any providers you use, like this:

```csharp
<PackageReference Include="Pulumi" Version="3.0.*" />
```

### Changes to pulumi.runtime.Mocks

The signatures of the `NewResourceAsync` and `CallAsync` methods have changed with the introduction of the `pulumi.runtime.MockResourceArgs` and `pulumi.runtime.MockCallArgs` types. If you use `setMocks` in your code, you'll need to update to these new types.

```csharp
// before
public Task<(string id, object state)> NewResourceAsync(string type, string name, ImmutableDictionary<string, object> inputs, string? provider, string? id)
{
    var outputs = ImmutableDictionary.CreateBuilder<string, object>();

    // Forward all input parameters as resource outputs, so that we could test them.
    outputs.AddRange(inputs);

    if (type == "aws:ec2/instance:Instance")
    {
        outputs.Add("publicIp", "203.0.113.12");
        outputs.Add("publicDns", "ec2-203-0-113-12.compute-1.amazonaws.com");
    }

    // Default the resource ID to `{name}_id`.
    // We could also format it as `/subscription/abc/resourceGroups/xyz/...` if that was important for tests.
    id ??= $"{name}_id";
    return Task.FromResult((id, (object)outputs));
}

public Task<object> CallAsync(string token, ImmutableDictionary<string, object> inputs, string? provider)
{
    var outputs = ImmutableDictionary.CreateBuilder<string, object>();

    if (token == "aws:index/getAmi:getAmi")
    {
        outputs.Add("architecture", "x86_64");
        outputs.Add("id", "ami-0eb1f3cdeeb8eed2a");
    }

    return Task.FromResult((object)outputs);
}

// after
public Task<(string id, object state)> NewResourceAsync(MockResourceArgs args)
{
    var outputs = ImmutableDictionary.CreateBuilder<string, object>();

    // Forward all input parameters as resource outputs, so that we could test them.
    outputs.AddRange(args.Inputs);

    if (args.Type == "aws:ec2/instance:Instance")
    {
        outputs.Add("publicIp", "203.0.113.12");
        outputs.Add("publicDns", "ec2-203-0-113-12.compute-1.amazonaws.com");
    }

    // Default the resource ID to `{name}_id`.
    // We could also format it as `/subscription/abc/resourceGroups/xyz/...` if that was important for tests.
    id ??= $"{args.Name}_id";
    return Task.FromResult((id, (object)outputs));
}

public Task<object> CallAsync(MockCallArgs args)
{
    var outputs = ImmutableDictionary.CreateBuilder<string, object>();

    if (args.Token == "aws:index/getAmi:getAmi")
    {
        outputs.Add("architecture", "x86_64");
        outputs.Add("id", "ami-0eb1f3cdeeb8eed2a");
    }

    return Task.FromResult((object)outputs);
}
```

{{% /choosable %}}

{{< /chooser >}}

## Required updates for automation API users

If you used a pre-GA release of Automation API, you need to update programs that use automation API to use the following namespaces:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language "javascript,typescript" %}}

```javascript
// before
import as automation from "@pulumi/pulumi/x/automation";

//after
import as automation from "@pulumi/pulumi/automation";
```

{{% /choosable %}}

{{% choosable language "python" %}}

```python
#before
from pulumi.x import automation as auto

#after
from pulumi import automation as auto
```

{{% /choosable %}}

{{% choosable language "go" %}}

```go
//before
import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v2/go/x/auto"
	"github.com/pulumi/pulumi/sdk/v2/go/x/auto/optdestroy"
	"github.com/pulumi/pulumi/sdk/v2/go/x/auto/optup"
)

//after
import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/auto"
	"github.com/pulumi/pulumi/sdk/v3/go/auto/optdestroy"
	"github.com/pulumi/pulumi/sdk/v3/go/auto/optup"
)
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

```csharp
using System;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Threading.Tasks;
using Pulumi.Automation;
```

{{% /choosable %}}

{{< /chooser >}}

## Remaining on Pulumi 2.0

We recommend switching to Pulumi 3.0 if possible. We will only push critical security and bug fixes into the 2.x branch.
Other fixes, feature enhancements, and new functionality will not be supported in the 2.x branch. In addition, provider
updates will only be built against Pulumi 3.0.

If you wish to remain on the 2.x CLI, you can continue to download the CLI by referring to the manual installation
instructions and choosing a specific version.

Running `pulumi new` will attempt to use the latest versions of the project templates, which pull in the 3.0 SDK. You can continue to
use the 2.x templates by running `pulumi new https://github.com/pulumi/templates/tree/2.x`.
