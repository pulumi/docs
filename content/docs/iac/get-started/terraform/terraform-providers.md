---
title_tag: Use Terraform Providers | Pulumi for Terraform Users
title: Use Terraform Providers
h1: "Use Terraform Providers"
meta_desc: Learn how to use any Terraform provider in Pulumi programs for accessing the full ecosystem of 3000+ providers.
weight: 6
menu:
    iac:
        name: Use Terraform Providers
        parent: terraform-get-started
        weight: 6

aliases:
- /docs/iac/get-started/terraform/terraform-providers/
---

## Access the provider ecosystem

Pulumi provides access to thousands of Terraform providers through the Terraform bridge. This means you can use any Terraform provider in your Pulumi programs, including community providers and custom providers that aren't available as native Pulumi providers.

## Add a Terraform provider

Use the `pulumi package add` command to add Terraform providers to your project:

```bash
$ pulumi package add terraform-provider hashicorp/random
```

This command automatically:

* Downloads the Terraform provider binary
* Generates Pulumi bindings for the provider
* Creates an SDK in your preferred language
* Adds the provider to your project dependencies

## Example: Random Pet Names

Let's see how this works first-hand, using the `random` Terraform provider. We'll import the Terraform provider then use it to put a load balander in a random availability zone.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-provider-test && cd pulumi-terraform-provider-test
$ pulumi new aws-typescript --yes
```

Next, add the `hashicorp/random` Terraform provider:

```bash
$ pulumi package add terraform-provider hashicorp/random
```

Then use it in your Pulumi program:

```typescript
import * as aws from "@pulumi/aws";
import * as random from "@pulumi/random";

const az = new random.Shuffle("availability-zones-randomizer", {
    inputs: [
        "us-west-2a",
        "us-west-2b",
        "us-west-2c",
        "us-west-2d",
    ],
    resultCount: 2,
});

// Place the ELB in any two of the given availability zones, selected at random.
const example = new aws.elb.LoadBalancer("random-load-balancer", {
    availabilityZones: az.results,
     listeners: [
        {
            instancePort: 8000,
            instanceProtocol: "http",
            lbPort: 80,
            lbProtocol: "http",
        },
    ],
});

// Export the zones we picked for reference.
export const availabilityZones = az.results;
```

{{% /choosable %}}

{{% choosable language "python" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-provider-test && cd pulumi-terraform-provider-test
$ pulumi new aws-python --yes
```

Next, add the `hashicorp/random` Terraform provider:

```bash
$ pulumi package add terraform-provider hashicorp/random
```

Then use it in your Pulumi program:

```python
import pulumi as pulumi
import pulumi_aws as aws
import pulumi_random as random

az = random.Shuffle("availability-zones-randomizer",
    inputs=[
        "us-west-2a",
        "us-west-2b",
        "us-west-2c",
        "us-west-2d",
    ],
    result_count=2)


aws.elb.LoadBalancer("random-load-balancer",
    availability_zones=az.results,
    listeners=[
        {
            "instance_port": 8000,
            "instance_protocol": "http",
            "lb_port": 80,
            "lb_protocol": "http",
        }])

pulumi.export('availability_zones', az.results)
```

{{% /choosable %}}

{{% choosable language "go" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-provider-test && cd pulumi-terraform-provider-test
$ pulumi new aws-go --yes
```

Next, add the `hashicorp/random` Terraform provider:

```bash
$ pulumi package add terraform-provider hashicorp/random
```

Then use it in your Pulumi program:

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/elb"
	"github.com/pulumi/pulumi-terraform-provider/sdks/go/random/v3/random"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		az, err := random.NewShuffle(ctx, "availability-zones-randomizer", &random.ShuffleArgs{
			Inputs: pulumi.StringArray{
				pulumi.String("us-west-2a"),
				pulumi.String("us-west-2b"),
				pulumi.String("us-west-2c"),
				pulumi.String("us-west-2d"),
			},
			ResultCount: pulumi.Float64(2),
		})
		if err != nil {
			return err
		}
		_, err = elb.NewLoadBalancer(ctx, "random-load-balancer", &elb.LoadBalancerArgs{
			AvailabilityZones: az.Results,
			Listeners: elb.LoadBalancerListenerArray{
				&elb.LoadBalancerListenerArgs{
					InstancePort:     pulumi.Int(8000),
					InstanceProtocol: pulumi.String("http"),
					LbPort:           pulumi.Int(80),
					LbProtocol:       pulumi.String("http"),
				},
			},
		})
		if err != nil {
			return err
		}
		ctx.Export("availability_zones", az.Results)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language "csharp" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-provider-test && cd pulumi-terraform-provider-test
$ pulumi new aws-csharp --yes
```

Next, add the `hashicorp/random` Terraform provider:

```bash
$ pulumi package add terraform-provider hashicorp/random
```

Then use it in your Pulumi program:

```csharp
using System.Collections.Generic;
using Pulumi;
using Pulumi.Random;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var az = new Shuffle("availability-zones-randomizer", new()
    {
        Inputs = new[]
        {
            "us-west-2a",
            "us-west-2b",
            "us-west-2c",
            "us-west-2d",
        },
        ResultCount = 2,
    });

    // Create a new load balancer
    var bar = new Aws.Elb.LoadBalancer("random-load-balancer", new()
    {
        AvailabilityZones = az.Results,
        Listeners = new[]
        {
            new Aws.Elb.Inputs.LoadBalancerListenerArgs
            {
                InstancePort = 8000,
                InstanceProtocol = "http",
                LbPort = 80,
                LbProtocol = "http",
            },
        },
    });

    return new Dictionary<string, object?>
    {
        ["availability_zones"] = az.Results
    };
});
```

{{% /choosable %}}

{{% choosable language "java" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-provider-test && cd pulumi-terraform-provider-test
$ pulumi new aws-java --yes
```

Next, add the `hashicorp/random` Terraform provider:

```bash
$ pulumi package add terraform-provider hashicorp/random
```

Then use it in your Pulumi program:

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.random.Shuffle;
import com.pulumi.random.ShuffleArgs;
import com.pulumi.aws.elb.LoadBalancer;
import com.pulumi.aws.elb.LoadBalancerArgs;
import com.pulumi.aws.elb.inputs.LoadBalancerListenerArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var az = new Shuffle("availability-zones-randomizer", ShuffleArgs.builder()
            .inputs(
                "us-west-2a",
                "us-west-2b",
                "us-west-2c",
                "us-west-2d")
            .resultCount(2d)
            .build());

        var bar = new LoadBalancer("random-load-balancer", LoadBalancerArgs.builder()
            .availabilityZones(az.results())
            .listeners(
                LoadBalancerListenerArgs.builder()
                    .instancePort(8000)
                    .instanceProtocol("http")
                    .lbPort(80)
                    .lbProtocol("http")
                    .build())
            .build());

        ctx.export("availability_zones", az.results());
    }
}
```

{{% /choosable %}}

{{% choosable language "yaml" %}}

First, create a new Pulumi program:

```bash
$ mkdir pulumi-terraform-provider-test && cd pulumi-terraform-provider-test
$ pulumi new aws-yaml --yes
```

Next, add the `hashicorp/random` Terraform provider:

```bash
$ pulumi package add terraform-provider hashicorp/random
```

Then use it in your Pulumi program:

```yaml
name: terraform-provider-example
runtime: yaml
description: Use Terraform providers in Pulumi
resources:
  az:
    type: random:Shuffle
    properties:
      inputs:
        - us-west-2a
        - us-west-2b
        - us-west-2c
        - us-west-2d
      resultCount: 2
  random-load-balancer:
    type: aws:elb:LoadBalancer
    properties:
      availabilityZones: ${az.results}
      listeners:
        - instancePort: 8000
          instanceProtocol: http
          lbPort: 80
          lbProtocol: http
outputs:
  availability_zones: ${az.results}
packages:
  random:
    source: terraform-provider
    version: 0.12.0
    parameters:
      - hashicorp/random
```

{{% /choosable %}}

## Compare with Terraform

The same functionality in Terraform would look like:

```hcl
# Terraform equivalent
resource "random_shuffle" "az" {
  input        = ["us-west-2a", "us-west-2b", "us-west-2c", "us-west-2d"]
  result_count = 2
}

resource "aws_elb" "random-load-balancer" {
  # Place the ELB in any two of the given availability zones, selected at random.
  availability_zones = random_shuffle.az.result

  listener {
    instance_port     = 8000
    instance_protocol = "http"
    lb_port           = 80
    lb_protocol       = "http"
  }
}
output "availability_zones" {
  value = random_shuffle.az.results
}
```

## Best practices

1. **Use native providers when available**: Prefer native Pulumi providers over Terraform providers for better performance and type safety
2. **Document provider usage**: Document which Terraform providers your team uses and why
3. **Monitor provider updates**: Keep track of provider updates and breaking changes

{{< get-started-stepper >}}
