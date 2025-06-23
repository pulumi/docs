---
title_tag: "Provider Functions"
meta_desc: A provider may make functions ("provider functions") available in its SDK as well as resource types. Learn how these provider functions work in this guide.
title: Provider functions
h1: Provider functions
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Provider functions
        parent: iac-concepts-resources
        weight: 7
    concepts:
        parent: resources
        weight: 7
aliases:
- /docs/intro/concepts/resources/functions/
- /docs/concepts/resources/functions/
---

A provider may make **functions** available in its SDK as well as resource types. These "provider functions" are often for calling a platform API to get a value that is not part of a resource. For example, the AWS provider includes the function [`aws.ecs.getAmi`](/registry/packages/aws/api-docs/ec2/getami/):

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

// Wrapping our program in an immediately invoked async function allows us to
// use the "async" keyword.
(async () => {
  const latestAmi = await aws.ec2.getAmi({
    owners: ["amazon"],
    mostRecent: true,
    filters: [
      { name: "name", values: ["amzn2-ami-hvm-*"] },
      { name: "architecture", values: ["x86_64"] }
    ]
  });

  new aws.ec2.Instance("web-server", {
    ami: latestAmi.imageId,
    instanceType: "t3.micro",
  });
})();
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_aws as aws

latest_ami = aws.ec2.get_ami(
    owners=["amazon"],
    most_recent=True,
    filters=[
        {"name": "name", "values": ["amzn2-ami-hvm-*"]},
        {"name": "architecture", "values": ["x86_64"]}
    ]
)

instance = aws.ec2.Instance(
    "web-server",
    ami=latest_ami.image_id,
    instance_type="t3.micro"
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		latestAmi, err := ec2.LookupAmi(ctx, &ec2.LookupAmiArgs{
			Owners:     []string{"amazon"},
			MostRecent: pulumi.BoolRef(true),
			Filters: []ec2.GetAmiFilter{
				{
					Name:   "name",
					Values: []string{"amzn2-ami-hvm-*"},
				},
				{
					Name:   "architecture",
					Values: []string{"x86_64"},
				},
			},
		}, nil)
		if err != nil {
			return err
		}

		_, err = ec2.NewInstance(ctx, "web-server", &ec2.InstanceArgs{
			Ami:          pulumi.String(latestAmi.ImageId),
			InstanceType: pulumi.String("t3.micro"),
		})
		if err != nil {
			return err
		}

		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var latestAmi = Aws.Ec2.GetAmi.Invoke(new Aws.Ec2.GetAmiInvokeArgs
    {
        Owners = { "amazon" },
        MostRecent = true,
        Filters =
              {
                  new Aws.Ec2.Inputs.GetAmiFilterInputArgs
                  {
                      Name = "name",
                      Values = { "amzn2-ami-hvm-*" }
                  },
                  new Aws.Ec2.Inputs.GetAmiFilterInputArgs
                  {
                      Name = "architecture",
                      Values = { "x86_64" }
                  }
              }
    });

    var instance = new Aws.Ec2.Instance("web-server", new Aws.Ec2.InstanceArgs
    {
        Ami = latestAmi.Apply(ami => ami.ImageId),
        InstanceType = "t3.micro"
    });
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.*;
import com.pulumi.aws.ec2.Ec2Functions;
import com.pulumi.aws.ec2.Instance;
import com.pulumi.aws.ec2.InstanceArgs;
import com.pulumi.aws.ec2.inputs.GetAmiArgs;
import com.pulumi.aws.ec2.inputs.GetAmiFilterArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var latestAmi = Ec2Functions.getAmi(GetAmiArgs.builder()
                .owners("amazon")
                .mostRecent(true)
                .filters(
                        GetAmiFilterArgs.builder()
                                .name("name")
                                .values("amzn2-ami-hvm-*")
                                .build(),
                        GetAmiFilterArgs.builder()
                                .name("architecture")
                                .values("x86_64")
                                .build())
                .build());

        new Instance("web-server", InstanceArgs.builder()
                .ami(latestAmi.applyValue(ami -> ami.imageId()))
                .instanceType("t3.micro")
                .build());
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: provider-functions
runtime: yaml

variables:
  lastestAmi:
    fn::invoke:
      function: aws:ec2/getAmi:getAmi
      arguments:
        filters:
          - name: name
            values: ["amzn2-ami-hvm-*"]
          - name: architecture
            values: ["x86_64"]
        owners: ["amazon"]
        mostRecent: true

resources:
  myInstance:
    type: aws:ec2:Instance
    properties:
      ami: ${lastestAmi.imageId}
      instanceType: "t3.micro"
```

{{% /choosable %}}

{{% /chooser %}}

Provider functions are exposed in each language as regular functions, in two variations:

 1. The **direct form** accepts plain arguments (e.g. `string`, as opposed to `pulumi.Input<string>`) and returns an asynchronous value (e.g. a `Promise` in NodeJS, or a `Task` in Python), or blocks until the result is available. These functions are typically named, e.g., `getFoo()`.
 2. The **output form** accepts `Input` values (or plain values) and returns an [Output](/docs/concepts/inputs-outputs/). These functions are typically named, e.g., `getFooOutput()`.

The [Pulumi Registry](/registry) contains authoritative documentation for all provider functions.

#### Invoke options

Functions also accept "invoke options", similar to the way Pulumi resources accept [resource options](/docs/concepts/options/). Invoke options may be specified either as an object or as a list of arguments depending on the language you're writing your Pulumi program in. The options are as follows:

- `dependsOn`: An array of resources that this function depends on, see [Dependencies and ordering](#dependencies-and-ordering). This option is only available on Output form invocations.

- `parent`: Supply a parent resource for this function call. Much like the [parent resource option](/docs/concepts/options/parent/), the parent will be consulted when determining the provider to use.

- `pluginDownloadURL`: Pass a URL from which the provider plugin should be fetched. This may be necessary for third-party packages such as those not hosted at [https://get.pulumi.com](https://get.pulumi.com).

- `provider`: Pass an [explicitly configured provider](/docs/concepts/resources/providers/#explicit-provider-configuration) to use for this function call, instead of using the default provider. This is useful, for example, if you want to invoke a function in each of a set of AWS regions.

- `version`: Pass a provider plugin version that should be used when invoking the function.

- `async`: _This option is deprecated and will be removed in a future release_.

### Dependencies and ordering

While the direct and output forms of a provider function are equivalent in terms of the results they produce when invoked, they differ in how they interact with the rest of the Pulumi program and the order in which they may be executed. Specifically:

- Direct form invocations execute just like any other function call in the language. Since they do not accept Pulumi `Input`s nor return Pulumi `Output`s, they are not tracked by the Pulumi engine and do not participate in the dependency graph.

- Output form invocations, on the other hand, are tracked by the Pulumi engine and participate in the dependency graph. This means, for example, that Pulumi will ensure that input resources are created or updated before an invocation and that the invocation is executed before its dependent resources are created or updated.

If you require that dependent resources are created or updated before an invocation, you must use a provider function's output form. If you need to specify a dependency that can't be captured by passing an appropriate input, you can use the `dependsOn` option to specify additional dependencies.

### Resource methods

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
