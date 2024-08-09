---
title_tag: "Provider Functions"
meta_desc: A provider may make functions ("provider functions") available in its SDK as well as resource types. Learn how these provider functions work in this guide.
title: Provider functions
h1: Provider functions
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    parent: resources
    weight: 7
aliases:
- /docs/intro/concepts/resources/functions/
---

A provider may make **functions** available in its SDK as well as resource types. These "provider functions" are often for calling a platform API to get a value that is not part of a resource. For example, the AWS provider includes the function [`aws.apigateway.getDomainName`](/registry/packages/aws/api-docs/apigateway/getdomainname/):

<div><pulumi-examples>
<div><pulumi-chooser type="language" options="typescript,python,go,csharp,java,yaml"></pulumi-chooser></div>
<div>
<pulumi-choosable type="language" values="csharp">

```csharp
using Pulumi;
using Aws = Pulumi.Aws;

class MyStack : Stack
{
    public MyStack()
    {
        var example = Output.Create(Aws.ApiGateway.GetDomainName.InvokeAsync(new Aws.ApiGateway.GetDomainNameArgs
        {
            DomainName = "api.example.com",
        }));
    }
}
```

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="go">

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/apigateway"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := apigateway.LookupDomainName(ctx, &apigateway.LookupDomainNameArgs{
			DomainName: "api.example.com",
		}, nil)
		if err != nil {
			return err
		}
		return nil
	})
}
```

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="java">

```java
package generated_program;

import java.util.*;
import java.io.*;
import java.nio.*;
import com.pulumi.*;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        final var example = Output.of(ApigatewayFunctions.getDomainName(GetDomainNameArgs.builder()
            .domainName("api.example.com")
            .build()));
    }
}
```

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="python">

```python
import pulumi
import pulumi_aws as aws

example = aws.apigateway.get_domain_name(domain_name="api.example.com")
```

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="typescript">

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = pulumi.output(aws.apigateway.getDomainName({
    domainName: "api.example.com",
}));
```

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="yaml">

```yaml
variables:
  example:
    fn::aws:apigateway:getDomainName:
      domainName: api.example.com
```

</pulumi-choosable>
</div>
</pulumi-examples></div>

Provider functions are exposed in each language as regular functions, in two variations:

 1. A function that accepts plain arguments (strings and so on) and returns an asynchronous value (e.g. a `Promise` in NodeJS, or a `Task` in Python), or blocks until the result is available. This is often referred to as the _direct form_.
 2. A function that accepts `Input` values and returns an [Output](/docs/concepts/inputs-outputs/). This is often referred to as the _output form_.

The documentation for a provider function will tell you the name and signature for each of the variations.

#### Invoke options

Each function and method also accepts "invoke options", either as an object or as varargs depending on the host language. The options are as follows:

- `parent`: Supply a parent resource for this function call. Much like the [parent resource option](/docs/concepts/options/parent/), the parent will be consulted when determining the provider to use.

- `pluginDownloadURL`: Pass a URL from which the provider plugin should be fetched. This may be necessary for third-party packages such as those not hosted at [https://get.pulumi.com](https://get.pulumi.com).

- `provider`: Pass an [explicitly configured provider](/docs/concepts/resources/providers/#explicit-provider-configuration) to use for this function call, instead of using the default provider. This is useful, for example, if you want to invoke a function in each of a set of AWS regions.

- `version`: Pass a provider plugin version that should be used when invoking the function.

- `async`: _This option is deprecated and will be removed in a future release_.

### Dependencies and ordering

While the direct and output forms of a provider function are equivalent in terms of the results they produce when invoked, they differ in how they interact with the rest of the Pulumi program and the order in which they may be executed. Specifically:

- Direct form invocations execute just like any other function call in the language. Since they do not accept Pulumi `Input`s nor return Pulumi `Output`s, they are not tracked by the Pulumi engine and do not participate in the dependency graph.

- Output form invocations, on the other hand, are tracked by the Pulumi engine and participate in the dependency graph. This means, for example, that Pulumi will ensure that input resources are created or updated before an invocation and that the invocation is executed before its dependent resources are created or updated.

If you require that dependent resources are created or updated before an invocation, you must use a provider function's output form. If you need to specify a dependency that can't be captured by passing an appropriate input (that is, if you wish to simulate something like the [`dependsOn` resource option](/docs/concepts/options/dependson/)), you can use Pulumi's [`all`](/docs/concepts/inputs-outputs/all/) function and `Output`'s [`apply`](/docs/concepts/inputs-outputs/apply/) method:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}
{{% choosable language typescript %}}

 ```typescript
import * as pulumi from "@pulumi/pulumi";

const res1 = new MyResource("res1", {});
const res2 = new MyResource("res2", {});

// Assuming `myFunctionOutput` is an output-form invocation of the `myFunction`
// provider function, this use of `all` and `apply` will ensure that it does not
// happen until `res1` and `res2` have been processed. This will work for any
// set of resources, even those with no explicit outputs, since the `.urn`
// output is always available.
pulumi.all([res1.urn, res2.urn]).apply(() => myFunctionOutput());
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using Pulumi;

return await Deployment.RunAsync(() =>
{
    var res1 = new MyResource("res1", new MyResourceArgs());
    var res2 = new MyResource("res2", new MyResourceArgs());

    // Assuming `myFunctionOutput` is an output-form invocation of the `myFunction`
    // provider function, this use of `Tuple` and `Apply` will ensure that it does
    // not happen until `res1` and `res2` have been processed. This will work for
    // any set of resources, even those with no explicit outputs, since the `.Urn`
    // output is always available.
    Output.Tuple(res1.Urn, res2.Urn).Apply(t => myFunctionOutput());
});
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		res1, err := NewMyResource(ctx, "res1", nil)
		if err != nil {
			return err
		}

		res2, err := NewMyResource(ctx, "res2", nil)
		if err != nil {
			return err
		}

		// Assuming `myFunctionOutput` is an output-form invocation of the `myFunction`
		// provider function, this use of `All` and `ApplyT` will ensure that it does not
		// happen until `res1` and `res2` have been processed. This will work for any set
		// of resources, even those with no explicit outputs, since the `.URN` output is
		// always available.
		_, err = pulumi.All(res1.URN, res2.URN).ApplyT(func(args []interface{}) (interface{}, error) {
			return myFunctionOutput()
		})
		if err != nil {
			return err
		}

		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi

res1 = MyResource("res1", {})
res2 = MyResource("res2", {})

# Assuming `my_function_output` is an output-form invocation of the `my_function`
# provider function, this use of `all` and `apply` will ensure that it does not
# happen until `res1` and `res2` have been processed. This will work for any set
# of resources, even those with no explicit outputs, since the `.urn` output is
# always available.
pulumi.all(res1.urn, res2.urn).apply(lambda args: my_function_output())
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Output;
import com.pulumi.Pulumi;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        final var res1 = new MyResource("res1", new MyResourceArgs());
        final var res2 = new MyResource("res2", new MyResourceArgs());

        // Assuming `myFunctionOutput` is an output-form invocation of the `myFunction`
        // provider function, this use of `tuple` and `applyValue` will ensure that it does
        // not happen until `res1` and `res2` have been processed. This will work for
        // any set of resources, even those with no explicit outputs, since the `.urn`
        // output is always available.
        Output.tuple(res1.getUrn(), res2.getUrn()).applyValue(t -> myFunctionOutput());
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

Output form invocations are not yet supported in YAML

{{% /choosable %}}
{{< /chooser >}}

### Provider methods

Provider SDKs may also include _methods_ attached to a resource type. For example, in the [EKS](/registry/packages/eks/api-docs/) SDK, the `Cluster` resource has a [.GetKubeconfig](/registry/packages/eks/api-docs/cluster/#method_GetKubeconfig) method:

<div><pulumi-examples>
<div><pulumi-chooser type="language" options="typescript,python,go,csharp,java,yaml"></pulumi-chooser></div>
<div>
<pulumi-choosable type="language" values="typescript">

```typescript
getKubeconfig(args?: Cluster.GetKubeconfigArgs): Output<Cluster.GetKubeconfigResult>
```

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="csharp">

```csharp
public Output<string> GetKubeconfig(Cluster.GetKubeconfigArgs? args)
```

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="go">

```go
func (r *Cluster) GetKubeconfig(ctx *Context, args *ClusterGetKubeconfigArgs) (pulumi.StringOutput, error)
```

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="python">

```python
def get_kubeconfig(self,
                   profile_name: Optional[pulumi.Input[str]] = None,
                   role_arn: Optional[pulumi.Input[str]] = None) -> Output[str]
```

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="java">

No example available for Java

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="yaml">

No example available for YAML

</pulumi-choosable>
</div>

</pulumi-examples></div>

Unlike provider functions, methods always appear in the _output form_: they take `Input` arguments, and return an `Output`. Moreover, methods do not accept invoke options.
