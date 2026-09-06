---
title_tag: "Loops & Iteration | Language Essentials"
meta_desc: Learn how for loops and comprehensions replace count and for_each when writing Pulumi programs in a general-purpose language.
title: Loops
h1: Loops and Iteration
menu:
    iac:
        name: Loops
        parent: iac-guides-language-essentials
        weight: 30
aliases:
    - /docs/iac/guides/language-essentials/loops/
---

A loop repeats an action once for each item in a collection. This is the
construct behind `count` and `for_each` in HCL: a way to create a resource
multiple times, once per item in a list or map, without writing the resource
block out by hand for each one. A general-purpose language gives you an
ordinary loop, and it applies to resources exactly the way it applies to any
other value.

## Where you have seen this before

Pulumi YAML has no native looping construct, so a fixed-size resource
collection is usually spelled out explicitly. Terraform HCL's `for_each` is
the direct analogue of the loops in this guide:

```hcl
variable "availability_zones" {
  default = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

resource "aws_subnet" "app" {
  for_each          = toset(var.availability_zones)
  availability_zone = each.value
  cidr_block        = "10.0.${index(var.availability_zones, each.value)}.0/24"
}
```

## The syntax

Each language has an idiomatic way to iterate a list: `for...of` in
TypeScript, a `for` loop in Python, `for ... range` in Go, `foreach` in C#,
and an enhanced `for` loop in Java.

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
const zones = ["us-east-1a", "us-east-1b", "us-east-1c"];

for (const zone of zones) {
  console.log(zone);
}
```

TypeScript also has `.map()`, which builds a new array by applying a function
to every element, and reads well when the loop's whole purpose is to produce
a value per item, which is exactly the shape of most resource loops:

```typescript
const upper = zones.map((zone) => zone.toUpperCase());
```

{{% /choosable %}}
{{% choosable language python %}}

```python
zones = ["us-east-1a", "us-east-1b", "us-east-1c"]

for zone in zones:
    print(zone)
```

A list comprehension is Python's equivalent of `.map()`, building a new list
from an existing one in a single expression:

```python
upper = [zone.upper() for zone in zones]
```

{{% /choosable %}}
{{% choosable language go %}}

```go
zones := []string{"us-east-1a", "us-east-1b", "us-east-1c"}

for _, zone := range zones {
	fmt.Println(zone)
}
```

Go has no built-in `map`-style function; a `for ... range` loop that appends
to a new slice is the idiomatic way to transform a list.

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var zones = new[] { "us-east-1a", "us-east-1b", "us-east-1c" };

foreach (var zone in zones)
{
    Console.WriteLine(zone);
}
```

LINQ's `.Select()` is C#'s equivalent of `.map()`, useful when the loop's job
is to produce a new sequence rather than perform a side effect:

```csharp
var upper = zones.Select(zone => zone.ToUpper());
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var zones = List.of("us-east-1a", "us-east-1b", "us-east-1c");

for (var zone : zones) {
    System.out.println(zone);
}
```

The `Stream` API's `.map()` is Java's equivalent, useful when you're
transforming a list into another list rather than iterating for a side
effect:

```java
var upper = zones.stream().map(String::toUpperCase).toList();
```

{{% /choosable %}}
{{% choosable language yaml %}}

Pulumi YAML has no looping construct of any kind, functional or otherwise.
Every resource in the file has to be written out explicitly.

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
variable "availability_zones" {
  default = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

resource "aws_subnet" "app" {
  for_each          = toset(var.availability_zones)
  availability_zone = each.value
}
```

{{% /choosable %}}

{{< /chooser >}}

## In a Pulumi program

Creating one subnet per availability zone is the same loop, with a resource
declaration as the body. The index or the zone name becomes part of the
resource's logical name, so each iteration produces a distinct resource
instead of overwriting the same one:

{{< chooser language "typescript,python,go,csharp,java,yaml,hcl" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

const zones = ["us-east-1a", "us-east-1b", "us-east-1c"];

const subnets = zones.map(
  (zone, index) =>
    new aws.ec2.Subnet(`app-subnet-${zone}`, {
      availabilityZone: zone,
      cidrBlock: `10.0.${index}.0/24`,
    }),
);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi_aws as aws

zones = ["us-east-1a", "us-east-1b", "us-east-1c"]

subnets = [
    aws.ec2.Subnet(
        f"app-subnet-{zone}",
        availability_zone=zone,
        cidr_block=f"10.0.{index}.0/24",
    )
    for index, zone in enumerate(zones)
]
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"fmt"

	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		zones := []string{"us-east-1a", "us-east-1b", "us-east-1c"}

		for index, zone := range zones {
			_, err := ec2.NewSubnet(ctx, fmt.Sprintf("app-subnet-%s", zone), &ec2.SubnetArgs{
				AvailabilityZone: pulumi.String(zone),
				CidrBlock:        pulumi.String(fmt.Sprintf("10.0.%d.0/24", index)),
			})
			if err != nil {
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
using Pulumi.Aws.Ec2;

return await Deployment.RunAsync(() =>
{
    var zones = new[] { "us-east-1a", "us-east-1b", "us-east-1c" };

    var subnets = zones.Select((zone, index) => new Subnet($"app-subnet-{zone}", new SubnetArgs
    {
        AvailabilityZone = zone,
        CidrBlock = $"10.0.{index}.0/24",
    })).ToList();
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
import com.pulumi.Pulumi;
import com.pulumi.aws.ec2.Subnet;
import com.pulumi.aws.ec2.SubnetArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var zones = List.of("us-east-1a", "us-east-1b", "us-east-1c");

            for (var i = 0; i < zones.size(); i++) {
                var zone = zones.get(i);
                var subnet = new Subnet("app-subnet-" + zone, SubnetArgs.builder()
                    .availabilityZone(zone)
                    .cidrBlock("10.0." + i + ".0/24")
                    .build());
            }
        });
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

Pulumi YAML can't create a resource per item in a list. Each subnet has to be
declared as its own resource, so a fixed, small set of zones is written out
by hand:

```yaml
resources:
  appSubnetA:
    type: aws:ec2:Subnet
    properties:
      availabilityZone: us-east-1a
      cidrBlock: 10.0.0.0/24
  appSubnetB:
    type: aws:ec2:Subnet
    properties:
      availabilityZone: us-east-1b
      cidrBlock: 10.0.1.0/24
```

{{% /choosable %}}
{{% choosable language hcl %}}

```hcl
variable "availability_zones" {
  default = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

resource "aws_subnet" "app" {
  for_each          = toset(var.availability_zones)
  availability_zone = each.value
  cidr_block        = "10.0.${index(var.availability_zones, each.value)}.0/24"
}
```

{{% /choosable %}}

{{< /chooser >}}

## What to watch out for

Every resource needs a unique logical name, the first argument to its
constructor, and that name is part of the resource's identity in Pulumi's
state. When you loop, build the name from something stable, such as the zone
or a fixed index, rather than an order that could shift between updates;
changing the name replaces the resource. See
[resource names](/docs/iac/concepts/resources/names/) for how logical names,
URNs, and physical IDs relate.

Don't iterate an output directly the way you'd iterate a plain list. A list of
resource outputs isn't resolved until each resource exists, so looping over it
with a plain `for` won't see real values yet. Call `.apply()` on a single
output, or `pulumi.all([...])` to wait on several at once, and iterate inside
the callback instead, where the values are resolved:

```typescript
pulumi.all(subnets.map((subnet) => subnet.id)).apply((ids) =>
  ids.forEach((id) => console.log(id)));
```

See [working with outputs](/docs/iac/concepts/inputs-outputs/apply/) and
[combining outputs](/docs/iac/concepts/inputs-outputs/all/) for the full
picture in every language.

## Frequently asked questions

### How do I replace `for_each` when I move from Terraform to Pulumi?

With a normal loop or comprehension over a list or map in your programming language. There's no separate meta-argument to learn: you iterate over the same data structure you'd use anywhere else in your code, and each iteration declares one resource.

### How do I keep resource names stable when I create resources in a loop?

Build each resource's logical name from a stable key drawn from your data, such as an item's identifier, rather than from the loop's iteration order or index. Pulumi tracks resources by their [logical name](/docs/iac/concepts/resources/names/), so changing that name causes Pulumi to replace the resource, and a name derived from iteration order shifts whenever the underlying list is reordered or resized.

### Can I loop over a resource output?

Not directly, since an [output](/docs/iac/concepts/inputs-outputs/) isn't a concrete value while your program runs. Call [`.apply()`](/docs/iac/concepts/inputs-outputs/apply/) on a single output, or [`pulumi.all([...])`](/docs/iac/concepts/inputs-outputs/all/) to combine several, and do the iteration inside the callback once the values are resolved.

## Next steps

Continue to [functions](/docs/iac/guides/basics/language-essentials/functions/) to
see how to package a repeated set of resources behind a single call.
