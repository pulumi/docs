---
title_tag: "Intro to Pulumi: Provider Functions"
title: "Provider Functions"
meta_desc: A provider may make functions ("provider functions") available in its SDK as well as resource types. Learn how these provider functions work in this guide.
menu:
  intro:
    parent: resources
    weight: 7
---

A provider may make **functions** available in its SDK as well as resource types. These "provider functions" are often for calling a platform API to get a value that is not part of a resource. For example, the AWS provider includes the function [`aws.apigateway.getDomainName`](https://www.pulumi.com/registry/packages/aws/api-docs/apigateway/getdomainname/):

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
    Fn::Invoke:
      Function: aws:apigateway:getDomainName
      Arguments:
        domainName: api.example.com
```

</pulumi-choosable>
</div>
</pulumi-examples></div>

Provider functions are exposed in each language as regular functions, in two variations:

 1. a function that accepts plain arguments (strings and so on) and returns a Promise, or blocks until the result is available; and,
 2. a function that accepts `Input` values and returns an [Output](/docs/intro/concepts/inputs-outputs/).

The documentation for a provider function will tell you the name and signature for each of the variations.

#### Invoke options

Each function and method also accepts "invoke options", either as an object or as varargs depending on the host language. The options are as follows:

| Option | Explanation                                                  |
|--------|--------------------------------------------------------------|
| parent | Supply a parent resource, which will be used to determine default providers |
| provider | Supply the provider to use explicitly. |
| version | Use exactly this version of the provider plugin. |
| pluginDownloadURL | Download the provider plugin from this URL. The download URL is otherwise inferred from the provider package. |
| _async_ | _This option is deprecated and will be removed in a future release_ |

The `parent` option has a similar purpose to the [parent option](/docs/intro/concepts/resources/options/parent/) used when creating a resource. The parent is consulted when determining the provider to use.

The `provider` option gives an explicit provider to use when running the invoked function. This is useful, for example, if you want to invoke a function in each of a set of AWS regions.

The `version` option specifies an exact version for the provider plugin. This can be used when you need to pin to a specific version to avoid a backward-incompatible change.

The `pluginDownloadURL` option gives a URL for fetching the provider plugin. It may be necessary to supply this for third-party packages (those not hosted at [https://get.pulumi.com](https://get.pulumi.com)).

### Provider methods

Provider SDKs may also include methods attached to a resource type. For example, in the [EKS](https://www.pulumi.com/registry/packages/eks/api-docs/) SDK, the `Cluster` resource has a method [.GetKubeconfig](https://www.pulumi.com/registry/packages/eks/api-docs/cluster/#method_GetKubeconfig):

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

(no example available for Java)

</pulumi-choosable>
</div>
<div>
<pulumi-choosable type="language" values="yaml">

(no example available for YAML)

</pulumi-choosable>
</div>

</pulumi-examples></div>

Unlike provider functions, methods always take `Input` arguments, and return an `Output`. Methods do not have invoke options.
