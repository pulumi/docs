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

A provider may make **functions** available in its SDK as well as resource types. These "provider functions" are often for calling a platform API to get a value that is not part of a resource.

For example, the AWS provider includes the function [`aws.ecs.getAmi`](/registry/packages/aws/api-docs/ec2/getami/):

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

{{% notes type="info" %}}
Bridged providers, which take a Terraform provider as an underlying dependency, expose Terraform data sources in the upstream Terraform provider as provider functions in the corresponding Pulumi provider.
{{% / notes %}}

## Direct form and output form

Provider functions are exposed in each language as regular functions, in two variations:

 1. The **direct form** accepts plain arguments (e.g. `string`, as opposed to `pulumi.Input<string>`) and returns an asynchronous value or blocks until the result is available.
 1. The **output form** accepts Pulumi Inputs as arguments and returns a Pulumi Output as a result. For more information on these types, see [Inputs and Outputs](/docs/concepts/inputs-outputs/).

The [Pulumi Registry](/registry) contains authoritative documentation for all provider functions.

## Invoke options

In addition to function arguments, provider functions also accept "invoke options", similar to the way Pulumi resources accept [resource options](/docs/concepts/options/). Invoke options may be specified either as an object or as a list of arguments depending on the language you're writing your Pulumi program in. The available options are:

* `dependsOn`: An array of resources that this function depends on. This option is only available in the Output form of a provider function. See [Dependencies and ordering](#dependencies-and-ordering) for a full explanation.
* `parent`: Supply a parent resource for this function call. Much like the [parent resource option](/docs/concepts/options/parent/), the parent will be consulted when determining the provider to use.
* `pluginDownloadURL`: Pass a URL from which the provider plugin should be fetched. This may be necessary for third-party packages such as those not hosted at [https://get.pulumi.com](https://get.pulumi.com).
* `provider`: Pass an [explicitly configured provider](/docs/concepts/resources/providers/#explicit-provider-configuration) to use for this function call, instead of using the default provider. This is useful, for example, if you want to invoke a function in each of a set of AWS regions.
* `version`: Pass a provider plugin version that should be used when invoking the function.
* `async`: _This option is deprecated and will be removed in a future release_.

## When your function will execute

While the direct and output forms of a provider function will both return the same data when they are invoked, the two forms differ in when they are executed when running your Pulumi program:

* Direct form functions execute just like any other function call in your Pulumi program's language. Since direct form functions do not accept Pulumi Inputs and Outputs, they are not tracked by the Pulumi engine the way resources are, and do not participate in the dependency graph.
* Output form functions are tracked by the Pulumi engine because they take Inputs as arguments and return Outputs as return values and therefore participate in the dependency graph. This means that Pulumi will ensure that all input values to the function are resolved before the function is invoked. (This is why `dependsOn` is only an option for the output form of a function.)

## Choosing between the direct form and the output form

There are several common scenarios where one form or the other _must_ be used:

* **If you need a provider function's result to determine whether a resource should be created at all**, you must use the provider function's the direct form. The direct form of a function executes _while_ the Pulumi engine is formulating the dependency graph (that is, determining what resources need to be created, updated, or deleted), so in order to figure out whether a resource belongs in the graph at all, that decision has to always be calculated up front.
* **If you need resources to be created or updated before the function is invoked**, you must use the provider function's output form. Dependencies in the output form of a function are tracked identically to resources: all inputs to the function must be resolved before the function executes. If you need to specify a dependency that isn't already implied by an input to the function's arguments, you can use the `dependsOn` function option to specify additional dependencies (just like you can with resources).

{{% notes type="info" %}}
Pulumi recommends you choose the output form of a function unless you have a specific need for the direct form. We make this recommendation because:

1. The output form reduces mental overhead in that it allows your program to stick with a single asynchronous programming mental model (Pulumi inputs and outputs) as opposed to also having to worry about Promises (TypeScript), TaskResults (.NET), etc.
1. Syntactically, it's slightly more terse.

Assuming there is no specific reason to choose one or the other, the choice between the two forms is ultimately a preference: there is no significant difference in either performance or code maintainability between the two forms.
{{% / notes %}}

## Resource methods

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

Unlike provider functions, methods always appear in the _output form_: they take `Input` arguments, and return an `Output` (because they cannot execute until after the resources has been created). Moreover, methods do not accept invoke options.
