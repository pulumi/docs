---
title_tag: "Provider Functions"
meta_desc: A provider may make functions ("provider functions") available in its SDK as well as resource types. Learn how these provider functions work in this guide.
title: Provider functions
h1: Provider functions
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Provider functions
        parent: iac-concepts-functions
        weight: 1
    concepts:
        parent: functions
        weight: 1
aliases:
- /docs/iac/concepts/resources/functions/
- /docs/intro/concepts/resources/functions/
- /docs/concepts/resources/functions/
---

A provider may make **functions** available in its SDK as well as resource types. These "provider functions" are often for calling a platform API to get a value that is not part of a resource.

For example, the AWS provider includes the function [`aws.ec2.getAmi`](/registry/packages/aws/api-docs/ec2/getami/):

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
  latestAmi:
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
      ami: ${latestAmi.imageId}
      instanceType: "t3.micro"
```

{{% /choosable %}}

{{< /chooser >}}

{{% notes type="info" %}}
Bridged providers, which take a Terraform provider as an underlying dependency, expose Terraform data sources in the upstream Terraform provider as provider functions in the corresponding Pulumi provider.
{{% /notes %}}

## Direct form and output form

Provider functions are exposed in each language as regular functions, in two variations.

In most languages, the two variations take the form of **two separately named functions** rather than overloads of a single function. For example, the AWS function `aws.ec2.getAmi` has a corresponding output form named `aws.ec2.getAmiOutput`. Java's naming convention is inverted: `Ec2Functions.getAmi()` is the _output_ form, while `Ec2Functions.getAmiPlain()` is the direct form. In YAML, both forms are invoked using `fn::invoke`, and the runtime handles the distinction transparently.

### Direct form

The **direct form** accepts plain arguments (e.g., `string`, as opposed to `pulumi.Input<string>`):

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

The direct form returns a `Promise<T>`. These functions are typically named `getX()`.

{{% /choosable %}}

{{% choosable language python %}}

The direct form returns the result synchronously. These functions are typically named `get_x()`.

{{% /choosable %}}

{{% choosable language go %}}

The direct form returns `(T, error)` synchronously. These functions are typically named `LookupX()` or `GetX()`.

{{% /choosable %}}

{{% choosable language csharp %}}

The direct form returns a `Task<T>`. These functions are typically named `GetX.InvokeAsync()`.

{{% /choosable %}}

{{% choosable language java %}}

The direct form returns a `CompletableFuture<T>`. These functions are typically named `ModuleFunctions.getXPlain()`.

{{% /choosable %}}

{{% choosable language yaml %}}

The direct form is invoked using `fn::invoke`. The result is resolved synchronously.

{{% /choosable %}}

{{< /chooser >}}

### Output form

The **output form** accepts Pulumi Inputs (or plain values) as arguments and returns a Pulumi Output as a result. For more information on these types, see [Inputs and Outputs](/docs/concepts/inputs-outputs/).

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

The output form returns an `Output<T>`. These functions are typically named `getXOutput()`.

{{% /choosable %}}

{{% choosable language python %}}

The output form returns an `Output[T]`. These functions are typically named `get_x_output()`.

{{% /choosable %}}

{{% choosable language go %}}

The output form returns a `LookupXResultOutput` or `GetXResultOutput`. These functions are typically named `LookupXOutput()` or `GetXOutput()`.

{{% /choosable %}}

{{% choosable language csharp %}}

The output form returns an `Output<T>`. These functions are typically named `GetX.Invoke()`.

{{% /choosable %}}

{{% choosable language java %}}

The output form returns an `Output<T>`. These functions are typically named `ModuleFunctions.getX()`.

{{% /choosable %}}

{{% choosable language yaml %}}

YAML does not distinguish between direct and output forms; both are invoked using `fn::invoke`.

{{% /choosable %}}

{{< /chooser >}}

The [Pulumi Registry](/registry) contains authoritative documentation for all provider functions.

## Invoke options

In addition to function arguments, provider functions also accept "invoke options", similar to the way Pulumi resources accept [resource options](/docs/concepts/options/). Invoke options may be specified either as an object or as a list of arguments depending on the language you're writing your Pulumi program in. The available options are:

* `dependsOn`: An array of resources that this function depends on. This option is only available in the Output form of a provider function. See [Choosing between direct form and output form](#choosing-between-direct-form-and-output-form) for a full explanation.
* `parent`: Supply a parent resource for this function call. Much like the [parent resource option](/docs/concepts/options/parent/), the parent will be consulted when determining the provider to use.
* `provider`: Pass an [explicitly configured provider](/docs/concepts/resources/providers/#explicit-provider-configuration) to use for this function call, instead of using the default provider. This is useful, for example, if you want to invoke a function in each of a set of AWS regions.

The following options are also available, but are deprecated and should not be used in modern Pulumi programs as the functionality they control are commonly handled when you install a provider package:

* `pluginDownloadURL`: Pass a URL from which the provider plugin should be fetched. This may be necessary for third-party packages such as those not hosted at [https://get.pulumi.com](https://get.pulumi.com).
* `version`: Pass a provider plugin version that should be used when invoking the function.
* `async`: _This option is deprecated and will be removed in a future release_.

## When your function will execute

While the direct and output forms of a provider function will both return the same data when they are invoked, the two forms differ in when they are executed when running your Pulumi program:

* Direct form functions execute just like any other function call in your Pulumi program's language. Since direct form functions do not accept Pulumi Inputs and Outputs, they are not tracked by the Pulumi engine the way resources are, and do not participate in the dependency graph.
* Output form functions are tracked by the Pulumi engine because they take Inputs as arguments and return Outputs as return values and therefore participate in the dependency graph. This means that Pulumi will ensure that all input values to the function are resolved before the function is invoked. (This is why `dependsOn` is only an option for the output form of a function.)

## Choosing between direct form and output form

There are several common scenarios where either direct form or output form must or should be used:

* **If you need a provider function's result to determine whether a resource should be created at all, you must use the direct form.** The direct form of a function executes _while_ the Pulumi engine is formulating the dependency graph (that is, determining what resources need to be created, updated, or deleted), so in order to figure out whether a resource belongs in the graph at all, that decision has to always be calculated up front.
* **If you need resources to be created or updated before the function is invoked, you should use the output form.** (It is _possible_ to use the direct form in this case, but it requires wrapping the call in an `apply`, which can be awkward from a readability standpoint.) Dependencies in the output form of a function are tracked identically to resources: all inputs to the function must be resolved before the function executes. If you need to specify a dependency that isn't already implied by an input to the function's arguments, you can use the `dependsOn` function option to specify additional dependencies (just like you can with resources).

The following examples illustrate both scenarios. The first uses the direct form so that the lookup result can gate whether the instance resource is added to the stack at all. The second uses the output form to pass a secret config value directly into the lookup's filter — no apply call required to pass the secret into the filter.

**Using the direct form:**

{{% notes type="info" %}}
YAML does not distinguish between direct and output forms at the language level — both use `fn::invoke`. The output-form example below applies equally to YAML.
{{% /notes %}}

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

// getAmiIds returns a Promise<GetAmiIdsResult>; await it to get a plain value.
const candidates = await aws.ec2.getAmiIds({
    owners: ["amazon"],
    filters: [{ name: "name", values: ["amzn2-ami-hvm-*-x86_64-gp3"] }],
});

// Because candidates.ids is a plain string[], we can branch on it freely.
// The instance is only added to the stack if a matching AMI was found.
if (candidates.ids.length > 0) {
    new aws.ec2.Instance("web", {
        ami: candidates.ids[0],
        instanceType: "t3.micro",
    });
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_aws as aws

# get_ami_ids returns a plain GetAmiIdsResult.
candidates = aws.ec2.get_ami_ids(
    owners=["amazon"],
    filters=[aws.ec2.GetAmiIdsFilterArgs(name="name", values=["amzn2-ami-hvm-*-x86_64-gp3"])],
)

# Because candidates.ids is a plain list, we can branch on it freely.
# The instance is only added to the stack if a matching AMI was found.
if candidates.ids:
    aws.ec2.Instance(
        "web",
        ami=candidates.ids[0],
        instance_type="t3.micro",
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
		// GetAmiIds returns plain results synchronously.
		candidates, err := ec2.GetAmiIds(ctx, &ec2.GetAmiIdsArgs{
			Owners: []string{"amazon"},
			Filters: []ec2.GetAmiIdsFilter{
				{Name: "name", Values: []string{"amzn2-ami-hvm-*-x86_64-gp3"}},
			},
		}, nil)
		if err != nil {
			return err
		}

		// Because candidates.Ids is a plain []string, we can branch on it freely.
		// The instance is only added to the stack if a matching AMI was found.
		if len(candidates.Ids) > 0 {
			if _, err = ec2.NewInstance(ctx, "web", &ec2.InstanceArgs{
				Ami:          pulumi.String(candidates.Ids[0]),
				InstanceType: pulumi.String("t3.micro"),
			}); err != nil {
				return err
			}
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

// The async lambda allows us to await the direct form function.
return await Deployment.RunAsync(async () =>
{
    // GetAmiIds.InvokeAsync returns a Task<GetAmiIdsResult>; await it for a plain value.
    var candidates = await Aws.Ec2.GetAmiIds.InvokeAsync(new Aws.Ec2.GetAmiIdsInvokeArgs
    {
        Owners = { "amazon" },
        Filters =
        {
            new Aws.Ec2.Inputs.GetAmiIdsFilterInputArgs
            {
                Name = "name",
                Values = { "amzn2-ami-hvm-*-x86_64-gp3" },
            },
        },
    });

    // Because candidates.Ids is a plain ImmutableArray<string>, we can branch on it freely.
    // The instance is only added to the stack if a matching AMI was found.
    if (candidates.Ids.Count > 0)
    {
        _ = new Aws.Ec2.Instance("web", new Aws.Ec2.InstanceArgs
        {
            Ami = candidates.Ids[0],
            InstanceType = "t3.micro",
        });
    }
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.ec2.Ec2Functions;
import com.pulumi.aws.ec2.Instance;
import com.pulumi.aws.ec2.InstanceArgs;
import com.pulumi.aws.ec2.inputs.GetAmiIdsArgs;
import com.pulumi.aws.ec2.inputs.GetAmiIdsFilterArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        // getAmiIdsPlain returns a CompletableFuture<GetAmiIdsResult>; join() for a plain value.
        var candidates = Ec2Functions.getAmiIdsPlain(GetAmiIdsArgs.builder()
                .owners("amazon")
                .filters(GetAmiIdsFilterArgs.builder()
                        .name("name")
                        .values("amzn2-ami-hvm-*-x86_64-gp3")
                        .build())
                .build()).join();

        // Because candidates.ids() is a plain List<String>, we can branch on it freely.
        // The instance is only added to the stack if a matching AMI was found.
        if (!candidates.ids().isEmpty()) {
            new Instance("web", InstanceArgs.builder()
                    .ami(candidates.ids().get(0))
                    .instanceType("t3.micro")
                    .build());
        }
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

**Using the output form:**

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();

// config.requireSecret returns an Output<string>.  The output form of the
// function accepts Pulumi Inputs, so we can pass this value directly without
// an apply() wrapper.
const amiNameFilter = config.requireSecret("amiNameFilter");

const latestAmi = aws.ec2.getAmiOutput({
    owners: ["amazon"],
    mostRecent: true,
    filters: [{ name: "name", values: [amiNameFilter] }],
});

new aws.ec2.Instance("web", {
    ami: latestAmi.imageId,
    instanceType: "t3.micro",
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

config = pulumi.Config()

# config.require_secret returns an Output[str].  The output form of the
# function accepts Pulumi Inputs, so we can pass this value directly without
# an apply() wrapper.
ami_name_filter = config.require_secret("amiNameFilter")

latest_ami = aws.ec2.get_ami_output(
    owners=["amazon"],
    most_recent=True,
    filters=[aws.ec2.GetAmiFilterArgs(name="name", values=[ami_name_filter])],
)

aws.ec2.Instance(
    "web",
    ami=latest_ami.image_id,
    instance_type="t3.micro",
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		cfg := config.New(ctx, "")

		// cfg.RequireSecret returns a pulumi.StringOutput.  The output form
		// of the function accepts Pulumi Inputs, so we can pass this value
		// directly without an Apply() wrapper.
		amiNameFilter := cfg.RequireSecret("amiNameFilter")

		latestAmi := ec2.LookupAmiOutput(ctx, ec2.LookupAmiOutputArgs{
			Owners:     pulumi.StringArray{pulumi.String("amazon")},
			MostRecent: pulumi.BoolPtr(true),
			Filters: ec2.GetAmiFilterArray{
				ec2.GetAmiFilterArgs{
					Name:   pulumi.String("name"),
					Values: pulumi.StringArray{amiNameFilter},
				},
			},
		}, nil)

		_, err := ec2.NewInstance(ctx, "web", &ec2.InstanceArgs{
			Ami:          latestAmi.ImageId(),
			InstanceType: pulumi.String("t3.micro"),
		})
		return err
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
    var config = new Config();

    // config.RequireSecret returns an Output<string>.  The output form of the
    // function accepts Pulumi Inputs, so we can pass this value directly without
    // an Apply() wrapper.
    var amiNameFilter = config.RequireSecret("amiNameFilter");

    var latestAmi = Aws.Ec2.GetAmi.Invoke(new Aws.Ec2.GetAmiInvokeArgs
    {
        Owners = { "amazon" },
        MostRecent = true,
        Filters =
        {
            new Aws.Ec2.Inputs.GetAmiFilterInputArgs
            {
                Name = "name",
                Values = { amiNameFilter },
            },
        },
    });

    _ = new Aws.Ec2.Instance("web", new Aws.Ec2.InstanceArgs
    {
        Ami = latestAmi.Apply(a => a.ImageId),
        InstanceType = "t3.micro",
    });
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
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
        var amiNameFilter = ctx.config().requireSecret("amiNameFilter");

        // Ec2Functions.getAmi() is the output form (returns Output<GetAmiResult>).
        // It accepts Pulumi Inputs, so we can pass the secret Output directly.
        var latestAmi = Ec2Functions.getAmi(GetAmiArgs.builder()
                .owners("amazon")
                .mostRecent(true)
                .filters(GetAmiFilterArgs.builder()
                        .name("name")
                        .values(amiNameFilter)
                        .build())
                .build());

        new Instance("web", InstanceArgs.builder()
                .ami(latestAmi.applyValue(ami -> ami.imageId()))
                .instanceType("t3.micro")
                .build());
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: provider
runtime: yaml

config:
  amiNameFilter:
    type: string
    secret: true

# In YAML, fn::invoke naturally accepts config variable references.
# There is no distinction between the direct and output forms; the
# runtime resolves all variable references before invoking the function.
variables:
  latestAmi:
    fn::invoke:
      function: aws:ec2/getAmi:getAmi
      arguments:
        owners: ["amazon"]
        mostRecent: true
        filters:
          - name: name
            values: ["${amiNameFilter}"]

resources:
  web:
    type: aws:ec2:Instance
    properties:
      ami: ${latestAmi.imageId}
      instanceType: t3.micro
```

{{% /choosable %}}

{{< /chooser >}}

{{% notes type="info" %}}
Pulumi recommends you choose the output form of a function unless you have a specific need for the direct form. We make this recommendation because:

1. The output form reduces mental overhead in that it allows your program to stick with a single programming model (Pulumi Inputs and Outputs) as opposed to also having to manage language-specific return types (e.g., `Promise` in TypeScript, `Task` in .NET, `CompletableFuture` in Java, or synchronous returns in Python and Go).
1. Syntactically, it's slightly more terse.

Assuming there is no specific reason to choose one or the other, the choice between the two forms is ultimately a preference: there is no significant difference in either performance or code maintainability between the two forms.
{{% /notes %}}
