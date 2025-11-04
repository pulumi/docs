---
title_tag: "ignoreChanges | Resource Options"
meta_desc: The ignoreChanges resource option declares that changes to certain properties should be ignored during a diff.
title: "ignoreChanges"
h1: "Resource option: ignoreChanges"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    identifier: ignoreChanges
    parent: options-concepts
    weight: 8
aliases:
  - /docs/intro/concepts/resources/options/ignorechanges/
  - /docs/concepts/options/ignorechanges/
  - /docs/iac/concepts/options/ignorechanges/
---

The `ignoreChanges` resource option specifies a list of properties that Pulumi will ignore when it updates existing resources. Pulumi ignores a property by using the old value from the state instead of the value provided by the Pulumi program when determining whether an update or replace is needed. Ignored properties will still be used from the program when there is no previous value in the state, most importantly when creating the resource.

## How ignoreChanges works

After the resource is created, Pulumi relies on the last recorded state for every property named in `ignoreChanges`. During a preview or update, Pulumi:

1. Uses the program value when there is no prior state (typically the initial create).
1. Uses the serialized value from the stack state for any later previews or updates.
1. Does not automatically read the live value for the property unless you run a refresh.

Because Pulumi reuses the value stored in the state, an external system can safely update the live resource as long as you synchronize the stack before the next update. Run `pulumi refresh` (or `pulumi up --refresh`) to pull the latest provider values into the state. Skipping the refresh step leaves stale values in the state, and Pulumi will continue to send those stale values to the provider during subsequent updates, which can overwrite the drift you meant to preserve.

{{% notes type="warning" %}}
When you skip `pulumi refresh` (or `pulumi up --refresh`) after `ignoreChanges` has been set, Pulumi keeps using the previous state value when it performs an update. This can lead to unintentional changes if the cloud state has been changed (either through intentional external management, or unintentional drift). Providers that require full object replacements—such as AWS load balancer listeners where the entire target group array is sent on every update—will receive the potentially stale values from the state and may reset the live configuration.
{{% /notes %}}

For instance, in this example, the resource’s prop property "new-value" will be set when Pulumi initially creates the resource, but from then on, any updates will ignore it:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let res = new MyResource("res",
    { prop: "new-value" }, { ignoreChanges: ["prop"] });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let res = new MyResource("res",
    { prop: "new-value" }, { ignoreChanges: ["prop"] });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
res = MyResource("res",
    prop="new-value",
    opts=ResourceOptions(ignore_changes=["prop"]))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
res, _ := NewMyResource(ctx, "res",
    &MyResourceArgs{Prop: "new-value"},
    pulumi.IgnoreChanges([]string{"prop"}))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var res = new MyResource("res",
    new MyResourceArgs { Prop = "new-value" },
    new CustomResourceOptions { IgnoreChanges = { "prop" } });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var res = new MyResource("res",
    MyResourceArgs.builder()
        .prop("new-value")
        .build(),
    CustomResourceOptions.builder()
        .ignoreChanges("prop")
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  res:
    type: MyResource
    properties:
      prop: new-value
    options:
      ignoreChanges:
        - prop
```

{{% /choosable %}}

{{< /chooser >}}

Some common reasons to use the `ignoreChanges` option are:

- Ignoring changes to properties that lead to diffs.
- Changing the defaults for a property without forcing all existing deployed stacks to update or replace the affected resource. This commonly occurs after importing existing infrastructure provisioned by another method into Pulumi. In these cases, there may be historical drift that you’d prefer to retain, rather than replacing and reconstructing critical parts of your infrastructure.
- Allowing an external system to manage aspects of the resource. In these cases you do not want Pulumi to reset values to their original Pulumi value.

## Example: Preserve externally managed weights

Consider an AWS Application Load Balancer listener whose target group weights are managed by an external traffic controller. You can let Pulumi create the listener and target groups while preventing future updates to the weights by adding the property path to `ignoreChanges`:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const frontEnd = new aws.lb.LoadBalancer("frontEnd", {});
const frontEndBlue = new aws.lb.TargetGroup("frontEndBlue", {});
const frontEndGreen = new aws.lb.TargetGroup("frontEndGreen", {});
const frontEndListener = new aws.lb.Listener("frontEndListener", {
    loadBalancerArn: frontEnd.arn,
    port: 443,
    protocol: "HTTPS",
    sslPolicy: "ELBSecurityPolicy-2016-08",
    certificateArn: "arn:aws:iam::187416307283:server-certificate/test_cert_rab3wuqwgja25ct3n4jdj2tzu4",
    defaultActions: [{
        type: "forward",
        forward: {
            targetGroups: [
                {
                    arn: frontEndBlue.arn,
                    weight: 100,
                },
                {
                    arn: frontEndGreen.arn,
                    weight: 0,
                },
            ],
        },
    }],
}, {
    ignoreChanges: ['defaultActions[*].forward.targetGroups[*].weight']
});

```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

front_end = aws.lb.LoadBalancer("frontEnd")
front_end_blue = aws.lb.TargetGroup("frontEndBlue")
front_end_green = aws.lb.TargetGroup("frontEndGreen")
front_end_listener = aws.lb.Listener("frontEndListener",
    load_balancer_arn=front_end.arn,
    port=443,
    protocol="HTTPS",
    ssl_policy="ELBSecurityPolicy-2016-08",
    certificate_arn="arn:aws:iam::187416307283:server-certificate/test_cert_rab3wuqwgja25ct3n4jdj2tzu4",
    default_actions=[{
        "type": "forward",
        "forward": {
            "target_groups": [
                {
                    "arn": front_end_blue.arn,
                    "weight": 100,
                },
                {
                    "arn": front_end_green.arn,
                    "weight": 0,
                },
            ],
        },
    }],
    opts=ResourceOptions(ignore_changes=["defaultActions[*].forward.targetGroups[*].weight"]))

```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/lb"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		frontEnd, err := lb.NewLoadBalancer(ctx, "frontEnd", nil)
		if err != nil {
			return err
		}
		frontEndBlue, err := lb.NewTargetGroup(ctx, "frontEndBlue", nil)
		if err != nil {
			return err
		}
		frontEndGreen, err := lb.NewTargetGroup(ctx, "frontEndGreen", nil)
		if err != nil {
			return err
		}
		_, err = lb.NewListener(ctx, "frontEndListener", &lb.ListenerArgs{
			LoadBalancerArn: frontEnd.Arn,
			Port:            pulumi.Int(443),
			Protocol:        pulumi.String("HTTPS"),
			SslPolicy:       pulumi.String("ELBSecurityPolicy-2016-08"),
			CertificateArn:  pulumi.String("arn:aws:iam::187416307283:server-certificate/test_cert_rab3wuqwgja25ct3n4jdj2tzu4"),
			DefaultActions: lb.ListenerDefaultActionArray{
				&lb.ListenerDefaultActionArgs{
					Type: pulumi.String("forward"),
					Forward: &lb.ListenerDefaultActionForwardArgs{
						TargetGroups: lb.ListenerDefaultActionForwardTargetGroupArray{
							&lb.ListenerDefaultActionForwardTargetGroupArgs{
								Arn:    frontEndBlue.Arn,
								Weight: pulumi.Int(100),
							},
							&lb.ListenerDefaultActionForwardTargetGroupArgs{
								Arn:    frontEndGreen.Arn,
								Weight: pulumi.Int(0),
							},
						},
					},
				},
			},
		}, pulumi.IgnoreChanges([]string{"defaultActions[*].forward.targetGroups[*].weight"}))
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
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var frontEnd = new Aws.LB.LoadBalancer("frontEnd");

    var frontEndBlue = new Aws.LB.TargetGroup("frontEndBlue");

    var frontEndGreen = new Aws.LB.TargetGroup("frontEndGreen");

    var frontEndListener = new Aws.LB.Listener("frontEndListener", new()
    {
        LoadBalancerArn = frontEnd.Arn,
        Port = 443,
        Protocol = "HTTPS",
        SslPolicy = "ELBSecurityPolicy-2016-08",
        CertificateArn = "arn:aws:iam::187416307283:server-certificate/test_cert_rab3wuqwgja25ct3n4jdj2tzu4",
        DefaultActions = new[]
        {
            new Aws.LB.Inputs.ListenerDefaultActionArgs
            {
                Type = "forward",
                Forward = new Aws.LB.Inputs.ListenerDefaultActionForwardArgs
                {
                    TargetGroups = new[]
                    {
                        new Aws.LB.Inputs.ListenerDefaultActionForwardTargetGroupArgs
                        {
                            Arn = frontEndBlue.Arn,
                            Weight = 100,
                        },
                        new Aws.LB.Inputs.ListenerDefaultActionForwardTargetGroupArgs
                        {
                            Arn = frontEndGreen.Arn,
                            Weight = 0,
                        },
                    },
                },
            },
        },
    },
    new CustomResourceOptions { IgnoreChanges = { "defaultActions[*].forward.targetGroups[*].weight" } });

});


```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.lb.LoadBalancer;
import com.pulumi.aws.lb.TargetGroup;
import com.pulumi.aws.lb.Listener;
import com.pulumi.aws.lb.ListenerArgs;
import com.pulumi.aws.lb.inputs.ListenerDefaultActionArgs;
import com.pulumi.aws.lb.inputs.ListenerDefaultActionForwardArgs;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var frontEnd = new LoadBalancer("frontEnd");

        var frontEndBlue = new TargetGroup("frontEndBlue");

        var frontEndGreen = new TargetGroup("frontEndGreen");

        var frontEndListener = new Listener("frontEndListener", ListenerArgs.builder()
            .loadBalancerArn(frontEnd.arn())
            .port(443)
            .protocol("HTTPS")
            .sslPolicy("ELBSecurityPolicy-2016-08")
            .certificateArn("arn:aws:iam::187416307283:server-certificate/test_cert_rab3wuqwgja25ct3n4jdj2tzu4")
            .defaultActions(ListenerDefaultActionArgs.builder()
                .type("forward")
                .forward(ListenerDefaultActionForwardArgs.builder()
                    .targetGroups(
                        ListenerDefaultActionForwardTargetGroupArgs.builder()
                            .arn(frontEndBlue.arn())
                            .weight(100)
                            .build(),
                        ListenerDefaultActionForwardTargetGroupArgs.builder()
                            .arn(frontEndGreen.arn())
                            .weight(0)
                            .build())
                    .build())
                .build())
            .build(),
            CustomResourceOptions.builder()
                .ignoreChanges("prop")
                .build());

    }
}

```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: example
runtime: yaml
resources:
  frontEnd:
    type: aws:lb:LoadBalancer
    name: front_end
  frontEndBlue:
    type: aws:lb:TargetGroup
    name: front_end_blue
  frontEndGreen:
    type: aws:lb:TargetGroup
    name: front_end_green
  frontEndListener:
    type: aws:lb:Listener
    name: front_end
    properties:
      loadBalancerArn: ${frontEnd.arn}
      port: 443
      protocol: HTTPS
      sslPolicy: ELBSecurityPolicy-2016-08
      certificateArn: arn:aws:iam::187416307283:server-certificate/test_cert_rab3wuqwgja25ct3n4jdj2tzu4
      defaultActions:
        - type: forward
          forward:
            targetGroups:
              - arn: ${frontEndBlue.arn}
                weight: 100
              - arn: ${frontEndGreen.arn}
                weight: 0
```

{{% /choosable %}}

{{< /chooser >}}

After the initial deployment, an external process could change the weights (for example, to a 50/50 split). Before you next run `pulumi up` to add a third target group, run `pulumi refresh` so that the stack captures the live weights. Without the refresh, Pulumi retains the original `100` and `0` values in state and will resend them to the AWS API on the next update, resetting the weights you meant to preserve.

{{% notes type="info" %}}
The `ignoreChanges` option only applies to resource inputs, not outputs.
{{% /notes %}}

{{% notes type="info" %}}
The `ignoreChanges` resource option does not apply to inputs to component resources.  If `ignoreChanges` is passed to a component resource, it is up to that component's implementation to decide what if anything it will do.
{{% /notes %}}

In addition to passing simple property names, nested properties can also be supplied to ignore changes to a more targeted nested part of the resource's inputs. See [property paths](/docs/iac/concepts/inputs-outputs/property-paths/) for examples of legal paths that can be passed to specify nested properties of objects and arrays.

{{% notes type="info" %}}
For arrays with different lengths, only changes for elements that are in both arrays are ignored. If the new input array is longer, additional elements will be taken from the new array. If the new array is shorter, we only take that number of elements from the original array.

For example `ignoreChanges` on an old array `[1, 2]` and a new array `[a, b, c]` results in `[1, 2, c]`, and an old array `[1, 2, 3]` and a new array `[a, b]` results in `[1, 2]`.
{{% /notes %}}
