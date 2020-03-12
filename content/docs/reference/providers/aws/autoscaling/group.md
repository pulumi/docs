
---
title: "Group"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an AutoScaling Group resource.

> **Note:** You must specify either `launch_configuration`, `launch_template`, or `mixed_instances_policy`.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const test = new aws.ec2.PlacementGroup("test", {
    strategy: "cluster",
});
const bar = new aws.autoscaling.Group("bar", {
    desiredCapacity: 4,
    forceDelete: true,
    healthCheckGracePeriod: 300,
    healthCheckType: "ELB",
    initialLifecycleHooks: [{
        defaultResult: "CONTINUE",
        heartbeatTimeout: 2000,
        lifecycleTransition: "autoscaling:EC2_INSTANCE_LAUNCHING",
        name: "foobar",
        notificationMetadata: `{
  "foo": "bar"
}
`,
        notificationTargetArn: "arn:aws:sqs:us-east-1:444455556666:queue1*",
        roleArn: "arn:aws:iam::123456789012:role/S3Access",
    }],
    launchConfiguration: aws_launch_configuration_foobar.name,
    maxSize: 5,
    minSize: 2,
    placementGroup: test.id,
    tags: [
        {
            key: "foo",
            propagateAtLaunch: true,
            value: "bar",
        },
        {
            key: "lorem",
            propagateAtLaunch: false,
            value: "ipsum",
        },
    ],
    timeouts: [{
        delete: "15m",
    }],
    vpcZoneIdentifiers: [
        aws_subnet_example1.id,
        aws_subnet_example2.id,
    ],
});
```

### With Latest Version Of Launch Template

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const foobar = new aws.ec2.LaunchTemplate("foobar", {
    imageId: "ami-1a2b3c",
    instanceType: "t2.micro",
    namePrefix: "foobar",
});
const bar = new aws.autoscaling.Group("bar", {
    availabilityZones: ["us-east-1a"],
    desiredCapacity: 1,
    launchTemplate: {
        id: foobar.id,
        version: "$Latest",
    },
    maxSize: 1,
    minSize: 1,
});
```

### Mixed Instances Policy

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleLaunchTemplate = new aws.ec2.LaunchTemplate("example", {
    imageId: aws_ami_example.id,
    instanceType: "c5.large",
    namePrefix: "example",
});
const exampleGroup = new aws.autoscaling.Group("example", {
    availabilityZones: ["us-east-1a"],
    desiredCapacity: 1,
    maxSize: 1,
    minSize: 1,
    mixedInstancesPolicy: {
        launchTemplate: {
            launchTemplateSpecification: {
                launchTemplateId: exampleLaunchTemplate.id,
            },
            overrides: [
                {
                    instanceType: "c4.large",
                    weightedCapacity: "3",
                },
                {
                    instanceType: "c3.large",
                    weightedCapacity: "2",
                },
            ],
        },
    },
});
```

## Interpolated tags

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const config = new pulumi.Config();
const extraTags = config.get("extraTags") || [
    {
        key: "Foo",
        propagateAtLaunch: true,
        value: "Bar",
    },
    {
        key: "Baz",
        propagateAtLaunch: true,
        value: "Bam",
    },
];

const bar = new aws.autoscaling.Group("bar", {
    launchConfiguration: aws_launch_configuration_foobar.name,
    maxSize: 5,
    minSize: 2,
    tagsCollection: [{"key": "interpolation1", "value": "value3", "propagate_at_launch": true}, {"key": "interpolation2", "value": "value4", "propagate_at_launch": true}].concat(extraTags),
    vpcZoneIdentifiers: [
        aws_subnet_example1.id,
        aws_subnet_example2.id,
    ],
});
```

## Waiting for Capacity

A newly-created ASG is initially empty and begins to scale to `min_size` (or
`desired_capacity`, if specified) by launching instances using the provided
Launch Configuration. These instances take time to launch and boot.

On ASG Update, changes to these values also take time to result in the target
number of instances providing service.

This provider provides two mechanisms to help consistently manage ASG scale up
time across dependent resources.

#### Waiting for ASG Capacity

The first is default behavior. This provider waits after ASG creation for
`min_size` (or `desired_capacity`, if specified) healthy instances to show up
in the ASG before continuing.

If `min_size` or `desired_capacity` are changed in a subsequent update,
this provider will also wait for the correct number of healthy instances before
continuing.

This provider considers an instance "healthy" when the ASG reports `HealthStatus:
"Healthy"` and `LifecycleState: "InService"`. See the [AWS AutoScaling
Docs](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/AutoScalingGroupLifecycle.html)
for more information on an ASG's lifecycle.

This provider will wait for healthy instances for up to
`wait_for_capacity_timeout`. If ASG creation is taking more than a few minutes,
it's worth investigating for scaling activity errors, which can be caused by
problems with the selected Launch Configuration.

Setting `wait_for_capacity_timeout` to `"0"` disables ASG Capacity waiting.

#### Waiting for ELB Capacity

The second mechanism is optional, and affects ASGs with attached ELBs specified
via the `load_balancers` attribute or with ALBs specified with `target_group_arns`.

The `min_elb_capacity` parameter causes this provider to wait for at least the
requested number of instances to show up `"InService"` in all attached ELBs
during ASG creation.  It has no effect on ASG updates.

If `wait_for_elb_capacity` is set, this provider will wait for exactly that number
of Instances to be `"InService"` in all attached ELBs on both creation and
updates.

These parameters can be used to ensure that service is being provided before
this provider moves on. If new instances don't pass the ELB's health checks for any
reason, the deployment will time out, and the ASG will be marked as
tainted (i.e. marked to be destroyed in a follow up run).

As with ASG Capacity, this provider will wait for up to `wait_for_capacity_timeout`
for the proper number of instances to be healthy.

#### Troubleshooting Capacity Waiting Timeouts

If ASG creation takes more than a few minutes, this could indicate one of a
number of configuration problems. See the [AWS Docs on Load Balancer
Troubleshooting](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-troubleshooting.html)
for more information.

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_group.html.markdown.



## Create a Group Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/autoscaling/#Group">Group</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/autoscaling/#GroupArgs">GroupArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

```python
def Group(resource_name, id, opts=None, availability_<wbr>zones=None, default_<wbr>cooldown=None, desired_<wbr>capacity=None, enabled_<wbr>metrics=None, force_<wbr>delete=None, health_<wbr>check_<wbr>grace_<wbr>period=None, health_<wbr>check_<wbr>type=None, initial_<wbr>lifecycle_<wbr>hooks=None, launch_<wbr>configuration=None, launch_<wbr>template=None, load_<wbr>balancers=None, max_<wbr>instance_<wbr>lifetime=None, max_<wbr>size=None, metrics_<wbr>granularity=None, min_<wbr>elb_<wbr>capacity=None, min_<wbr>size=None, mixed_<wbr>instances_<wbr>policy=None, name=None, name_<wbr>prefix=None, placement_<wbr>group=None, protect_<wbr>from_<wbr>scale_<wbr>in=None, service_<wbr>linked_<wbr>role_<wbr>arn=None, suspended_<wbr>processes=None, tags=None, tags_<wbr>collection=None, target_<wbr>group_<wbr>arns=None, termination_<wbr>policies=None, vpc_<wbr>zone_<wbr>identifiers=None, wait_<wbr>for_<wbr>capacity_<wbr>timeout=None, wait_<wbr>for_<wbr>elb_<wbr>capacity=None, __props__=None)
```

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewGroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupArgs">GroupArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#Group">Group</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.Group.html">Group</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupArgs.html">GroupArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Group resource with the given unique name, arguments, and options.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Cooldown</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Metrics</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of metrics to collect. The allowed values are `GroupDesiredCapacity`, `GroupInServiceCapacity`, `GroupPendingCapacity`, `GroupMinSize`, `GroupMaxSize`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupStandbyCapacity`, `GroupTerminatingCapacity`, `GroupTerminatingInstances`, `GroupTotalCapacity`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: &#34;10m&#34;) A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to &#34;0&#34; causes
this provider to skip all Capacity Waiting behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Delete</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it&#39;s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Grace<wbr>Period</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time (in seconds) after instance comes into service before checking health.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
&#34;EC2&#34; or &#34;ELB&#34;. Controls how health checking is done.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Initial<wbr>Lifecycle<wbr>Hooks</td>
            <td class="align-top">
                
                <code><a href="#groupinitiallifecyclehook">List&lt;Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Initial<wbr>Lifecycle<wbr>Hook<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws.autoscaling.LifecycleHook`](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws.autoscaling.LifecycleHook` resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch configuration to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#grouplaunchtemplate">Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Launch<wbr>Template<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Instance<wbr>Lifetime</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time, in seconds, that an instance can be in service, values must be either equal to 0 or between 604800 and 31536000 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum size of the auto scale group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metrics<wbr>Granularity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The minimum size of the auto scale group.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mixed<wbr>Instances<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicy">Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Group</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the placement group into which you&#39;ll launch your instances, if any.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protect<wbr>From<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Linked<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the service-linked role that the ASG will use to call other AWS services
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Suspended<wbr>Processes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code><a href="#grouptag">List&lt;Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Tag<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks. Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags<wbr>Collection</td>
            <td class="align-top">
                
                <code>List&lt;Immutable<wbr>Dictionary&lt;string, object&gt;&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks (maps). Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Group<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of `aws.alb.TargetGroup` ARNs, for use with Application or Network Load Balancing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Termination<wbr>Policies</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `OldestLaunchTemplate`, `AllocationStrategy`, `Default`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Zone<wbr>Identifiers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to launch resources in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Capacity<wbr>Timeout</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over `min_elb_capacity` behavior.)
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Cooldown</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Metrics</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of metrics to collect. The allowed values are `GroupDesiredCapacity`, `GroupInServiceCapacity`, `GroupPendingCapacity`, `GroupMinSize`, `GroupMaxSize`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupStandbyCapacity`, `GroupTerminatingCapacity`, `GroupTerminatingInstances`, `GroupTotalCapacity`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: &#34;10m&#34;) A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to &#34;0&#34; causes
this provider to skip all Capacity Waiting behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Delete</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it&#39;s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Grace<wbr>Period</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time (in seconds) after instance comes into service before checking health.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
&#34;EC2&#34; or &#34;ELB&#34;. Controls how health checking is done.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Initial<wbr>Lifecycle<wbr>Hooks</td>
            <td class="align-top">
                
                <code><a href="#groupinitiallifecyclehook">[]autoscaling.<wbr>Group<wbr>Initial<wbr>Lifecycle<wbr>Hook</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws.autoscaling.LifecycleHook`](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws.autoscaling.LifecycleHook` resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Configuration</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch configuration to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#grouplaunchtemplate">*autoscaling.<wbr>Group<wbr>Launch<wbr>Template</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Instance<wbr>Lifetime</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time, in seconds, that an instance can be in service, values must be either equal to 0 or between 604800 and 31536000 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum size of the auto scale group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metrics<wbr>Granularity</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The minimum size of the auto scale group.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mixed<wbr>Instances<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicy">*autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Group</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the placement group into which you&#39;ll launch your instances, if any.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protect<wbr>From<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Linked<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the service-linked role that the ASG will use to call other AWS services
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Suspended<wbr>Processes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code><a href="#grouptag">[]autoscaling.<wbr>Group<wbr>Tag</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks. Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags<wbr>Collection</td>
            <td class="align-top">
                
                <code>[]map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks (maps). Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Group<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of `aws.alb.TargetGroup` ARNs, for use with Application or Network Load Balancing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Termination<wbr>Policies</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `OldestLaunchTemplate`, `AllocationStrategy`, `Default`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Zone<wbr>Identifiers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to launch resources in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Capacity<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over `min_elb_capacity` behavior.)
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Cooldown</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled<wbr>Metrics</td>
            <td class="align-top">
                
                <code>Metric[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of metrics to collect. The allowed values are `GroupDesiredCapacity`, `GroupInServiceCapacity`, `GroupPendingCapacity`, `GroupMinSize`, `GroupMaxSize`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupStandbyCapacity`, `GroupTerminatingCapacity`, `GroupTerminatingInstances`, `GroupTotalCapacity`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: &#34;10m&#34;) A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to &#34;0&#34; causes
this provider to skip all Capacity Waiting behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force<wbr>Delete</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it&#39;s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Grace<wbr>Period</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time (in seconds) after instance comes into service before checking health.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
&#34;EC2&#34; or &#34;ELB&#34;. Controls how health checking is done.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">initial<wbr>Lifecycle<wbr>Hooks</td>
            <td class="align-top">
                
                <code><a href="#groupinitiallifecyclehook">autoscaling.<wbr>Group<wbr>Initial<wbr>Lifecycle<wbr>Hook[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws.autoscaling.LifecycleHook`](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws.autoscaling.LifecycleHook` resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string | Launch<wbr>Configuration</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch configuration to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#grouplaunchtemplate">autoscaling.<wbr>Group<wbr>Launch<wbr>Template?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Instance<wbr>Lifetime</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time, in seconds, that an instance can be in service, values must be either equal to 0 or between 604800 and 31536000 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum size of the auto scale group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metrics<wbr>Granularity</td>
            <td class="align-top">
                
                <code>string | Metrics<wbr>Granularity</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The minimum size of the auto scale group.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mixed<wbr>Instances<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicy">autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement<wbr>Group</td>
            <td class="align-top">
                
                <code>string | Placement<wbr>Group</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the placement group into which you&#39;ll launch your instances, if any.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protect<wbr>From<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Linked<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the service-linked role that the ASG will use to call other AWS services
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">suspended<wbr>Processes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code><a href="#grouptag">autoscaling.<wbr>Group<wbr>Tag[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks. Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags<wbr>Collection</td>
            <td class="align-top">
                
                <code>{[key: string]: any}[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks (maps). Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Group<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of `aws.alb.TargetGroup` ARNs, for use with Application or Network Load Balancing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">termination<wbr>Policies</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `OldestLaunchTemplate`, `AllocationStrategy`, `Default`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Zone<wbr>Identifiers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to launch resources in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait<wbr>For<wbr>Capacity<wbr>Timeout</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait<wbr>For<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over `min_elb_capacity` behavior.)
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>cooldown</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">desired_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled_<wbr>metrics</td>
            <td class="align-top">
                
                <code>list[metric]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of metrics to collect. The allowed values are `GroupDesiredCapacity`, `GroupInServiceCapacity`, `GroupPendingCapacity`, `GroupMinSize`, `GroupMaxSize`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupStandbyCapacity`, `GroupTerminatingCapacity`, `GroupTerminatingInstances`, `GroupTotalCapacity`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: &#34;10m&#34;) A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to &#34;0&#34; causes
this provider to skip all Capacity Waiting behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force_<wbr>delete</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it&#39;s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>grace_<wbr>period</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time (in seconds) after instance comes into service before checking health.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
&#34;EC2&#34; or &#34;ELB&#34;. Controls how health checking is done.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">initial_<wbr>lifecycle_<wbr>hooks</td>
            <td class="align-top">
                
                <code><a href="#groupinitiallifecyclehook">list[group_<wbr>initial_<wbr>lifecycle_<wbr>hook]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws.autoscaling.LifecycleHook`](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws.autoscaling.LifecycleHook` resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch_<wbr>configuration</td>
            <td class="align-top">
                
                <code>dict</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch configuration to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch_<wbr>template</td>
            <td class="align-top">
                
                <code><a href="#grouplaunchtemplate">dict{group_<wbr>launch_<wbr>template}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load_<wbr>balancers</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>instance_<wbr>lifetime</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time, in seconds, that an instance can be in service, values must be either equal to 0 or between 604800 and 31536000 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum size of the auto scale group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metrics_<wbr>granularity</td>
            <td class="align-top">
                
                <code>dict</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>elb_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The minimum size of the auto scale group.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mixed_<wbr>instances_<wbr>policy</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicy">dict{group_<wbr>mixed_<wbr>instances_<wbr>policy}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement_<wbr>group</td>
            <td class="align-top">
                
                <code>dict</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the placement group into which you&#39;ll launch your instances, if any.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protect_<wbr>from_<wbr>scale_<wbr>in</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>linked_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the service-linked role that the ASG will use to call other AWS services
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">suspended_<wbr>processes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code><a href="#grouptag">list[group_<wbr>tag]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks. Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags_<wbr>collection</td>
            <td class="align-top">
                
                <code>list[any>]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks (maps). Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>group_<wbr>arns</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of `aws.alb.TargetGroup` ARNs, for use with Application or Network Load Balancing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">termination_<wbr>policies</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `OldestLaunchTemplate`, `AllocationStrategy`, `Default`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>zone_<wbr>identifiers</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to launch resources in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait_<wbr>for_<wbr>capacity_<wbr>timeout</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait_<wbr>for_<wbr>elb_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over `min_elb_capacity` behavior.)
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Group Output Properties

The following output properties are available:



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for this AutoScaling Group
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Cooldown</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Metrics</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A list of metrics to collect. The allowed values are `GroupDesiredCapacity`, `GroupInServiceCapacity`, `GroupPendingCapacity`, `GroupMinSize`, `GroupMaxSize`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupStandbyCapacity`, `GroupTerminatingCapacity`, `GroupTerminatingInstances`, `GroupTotalCapacity`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: &#34;10m&#34;) A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to &#34;0&#34; causes
this provider to skip all Capacity Waiting behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Delete</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it&#39;s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Grace<wbr>Period</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} Time (in seconds) after instance comes into service before checking health.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} &#34;EC2&#34; or &#34;ELB&#34;. Controls how health checking is done.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Initial<wbr>Lifecycle<wbr>Hooks</td>
            <td class="align-top">
                
                <code><a href="#groupinitiallifecyclehook">List&lt;Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Initial<wbr>Lifecycle<wbr>Hook&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws.autoscaling.LifecycleHook`](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws.autoscaling.LifecycleHook` resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the launch configuration to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#grouplaunchtemplate">Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Launch<wbr>Template?</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Instance<wbr>Lifetime</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The maximum amount of time, in seconds, that an instance can be in service, values must be either equal to 0 or between 604800 and 31536000 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The maximum size of the auto scale group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metrics<wbr>Granularity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The minimum size of the auto scale group.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mixed<wbr>Instances<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicy">Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Group</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the placement group into which you&#39;ll launch your instances, if any.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protect<wbr>From<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Linked<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the service-linked role that the ASG will use to call other AWS services
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Suspended<wbr>Processes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code><a href="#grouptag">List&lt;Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Tag&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of tag blocks. Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags<wbr>Collection</td>
            <td class="align-top">
                
                <code>List&lt;Immutable<wbr>Dictionary&lt;string, object&gt;&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A list of tag blocks (maps). Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Group<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} A list of `aws.alb.TargetGroup` ARNs, for use with Application or Network Load Balancing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Termination<wbr>Policies</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `OldestLaunchTemplate`, `AllocationStrategy`, `Default`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Zone<wbr>Identifiers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} A list of subnet IDs to launch resources in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Capacity<wbr>Timeout</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over `min_elb_capacity` behavior.)
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for this AutoScaling Group
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Cooldown</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Metrics</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of metrics to collect. The allowed values are `GroupDesiredCapacity`, `GroupInServiceCapacity`, `GroupPendingCapacity`, `GroupMinSize`, `GroupMaxSize`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupStandbyCapacity`, `GroupTerminatingCapacity`, `GroupTerminatingInstances`, `GroupTotalCapacity`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: &#34;10m&#34;) A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to &#34;0&#34; causes
this provider to skip all Capacity Waiting behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Delete</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it&#39;s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Grace<wbr>Period</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} Time (in seconds) after instance comes into service before checking health.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} &#34;EC2&#34; or &#34;ELB&#34;. Controls how health checking is done.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Initial<wbr>Lifecycle<wbr>Hooks</td>
            <td class="align-top">
                
                <code><a href="#groupinitiallifecyclehook">[]autoscaling.<wbr>Group<wbr>Initial<wbr>Lifecycle<wbr>Hook</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws.autoscaling.LifecycleHook`](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws.autoscaling.LifecycleHook` resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Configuration</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the launch configuration to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#grouplaunchtemplate">*autoscaling.<wbr>Group<wbr>Launch<wbr>Template</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Instance<wbr>Lifetime</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The maximum amount of time, in seconds, that an instance can be in service, values must be either equal to 0 or between 604800 and 31536000 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The maximum size of the auto scale group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metrics<wbr>Granularity</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The minimum size of the auto scale group.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mixed<wbr>Instances<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicy">*autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Group</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the placement group into which you&#39;ll launch your instances, if any.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protect<wbr>From<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Linked<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the service-linked role that the ASG will use to call other AWS services
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Suspended<wbr>Processes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code><a href="#grouptag">[]autoscaling.<wbr>Group<wbr>Tag</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of tag blocks. Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags<wbr>Collection</td>
            <td class="align-top">
                
                <code>[]map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A list of tag blocks (maps). Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Group<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of `aws.alb.TargetGroup` ARNs, for use with Application or Network Load Balancing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Termination<wbr>Policies</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `OldestLaunchTemplate`, `AllocationStrategy`, `Default`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Zone<wbr>Identifiers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of subnet IDs to launch resources in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Capacity<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over `min_elb_capacity` behavior.)
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for this AutoScaling Group
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Cooldown</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled<wbr>Metrics</td>
            <td class="align-top">
                
                <code>Metric[]?</code>
            </td>
            <td class="align-top">{{% md %}} A list of metrics to collect. The allowed values are `GroupDesiredCapacity`, `GroupInServiceCapacity`, `GroupPendingCapacity`, `GroupMinSize`, `GroupMaxSize`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupStandbyCapacity`, `GroupTerminatingCapacity`, `GroupTerminatingInstances`, `GroupTotalCapacity`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: &#34;10m&#34;) A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to &#34;0&#34; causes
this provider to skip all Capacity Waiting behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force<wbr>Delete</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it&#39;s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Grace<wbr>Period</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} Time (in seconds) after instance comes into service before checking health.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} &#34;EC2&#34; or &#34;ELB&#34;. Controls how health checking is done.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">initial<wbr>Lifecycle<wbr>Hooks</td>
            <td class="align-top">
                
                <code><a href="#groupinitiallifecyclehook">autoscaling.<wbr>Group<wbr>Initial<wbr>Lifecycle<wbr>Hook[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws.autoscaling.LifecycleHook`](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws.autoscaling.LifecycleHook` resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the launch configuration to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#grouplaunchtemplate">autoscaling.<wbr>Group<wbr>Launch<wbr>Template?</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Instance<wbr>Lifetime</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The maximum amount of time, in seconds, that an instance can be in service, values must be either equal to 0 or between 604800 and 31536000 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The maximum size of the auto scale group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metrics<wbr>Granularity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The minimum size of the auto scale group.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mixed<wbr>Instances<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicy">autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement<wbr>Group</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the placement group into which you&#39;ll launch your instances, if any.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protect<wbr>From<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Linked<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the service-linked role that the ASG will use to call other AWS services
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">suspended<wbr>Processes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code><a href="#grouptag">autoscaling.<wbr>Group<wbr>Tag[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of tag blocks. Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags<wbr>Collection</td>
            <td class="align-top">
                
                <code>{[key: string]: any}[]?</code>
            </td>
            <td class="align-top">{{% md %}} A list of tag blocks (maps). Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Group<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} A list of `aws.alb.TargetGroup` ARNs, for use with Application or Network Load Balancing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">termination<wbr>Policies</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `OldestLaunchTemplate`, `AllocationStrategy`, `Default`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Zone<wbr>Identifiers</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} A list of subnet IDs to launch resources in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait<wbr>For<wbr>Capacity<wbr>Timeout</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait<wbr>For<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over `min_elb_capacity` behavior.)
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for this AutoScaling Group
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>cooldown</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">desired_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled_<wbr>metrics</td>
            <td class="align-top">
                
                <code>list[metric]</code>
            </td>
            <td class="align-top">{{% md %}} A list of metrics to collect. The allowed values are `GroupDesiredCapacity`, `GroupInServiceCapacity`, `GroupPendingCapacity`, `GroupMinSize`, `GroupMaxSize`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupStandbyCapacity`, `GroupTerminatingCapacity`, `GroupTerminatingInstances`, `GroupTotalCapacity`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: &#34;10m&#34;) A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to &#34;0&#34; causes
this provider to skip all Capacity Waiting behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force_<wbr>delete</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it&#39;s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>grace_<wbr>period</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} Time (in seconds) after instance comes into service before checking health.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} &#34;EC2&#34; or &#34;ELB&#34;. Controls how health checking is done.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">initial_<wbr>lifecycle_<wbr>hooks</td>
            <td class="align-top">
                
                <code><a href="#groupinitiallifecyclehook">list[group_<wbr>initial_<wbr>lifecycle_<wbr>hook]</a></code>
            </td>
            <td class="align-top">{{% md %}} One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws.autoscaling.LifecycleHook`](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws.autoscaling.LifecycleHook` resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch_<wbr>configuration</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the launch configuration to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch_<wbr>template</td>
            <td class="align-top">
                
                <code><a href="#grouplaunchtemplate">dict{group_<wbr>launch_<wbr>template}</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load_<wbr>balancers</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>instance_<wbr>lifetime</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The maximum amount of time, in seconds, that an instance can be in service, values must be either equal to 0 or between 604800 and 31536000 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The maximum size of the auto scale group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metrics_<wbr>granularity</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>elb_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The minimum size of the auto scale group.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mixed_<wbr>instances_<wbr>policy</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicy">dict{group_<wbr>mixed_<wbr>instances_<wbr>policy}</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement_<wbr>group</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the placement group into which you&#39;ll launch your instances, if any.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protect_<wbr>from_<wbr>scale_<wbr>in</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>linked_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the service-linked role that the ASG will use to call other AWS services
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">suspended_<wbr>processes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code><a href="#grouptag">list[group_<wbr>tag]</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of tag blocks. Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags_<wbr>collection</td>
            <td class="align-top">
                
                <code>list[any>]</code>
            </td>
            <td class="align-top">{{% md %}} A list of tag blocks (maps). Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>group_<wbr>arns</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A list of `aws.alb.TargetGroup` ARNs, for use with Application or Network Load Balancing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">termination_<wbr>policies</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `OldestLaunchTemplate`, `AllocationStrategy`, `Default`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>zone_<wbr>identifiers</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A list of subnet IDs to launch resources in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait_<wbr>for_<wbr>capacity_<wbr>timeout</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait_<wbr>for_<wbr>elb_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over `min_elb_capacity` behavior.)
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Group Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupState, opts?: pulumi.CustomResourceOptions): Group;
```

```python
def get(resource_name, id, opts=None, arn=None, availability_<wbr>zones=None, default_<wbr>cooldown=None, desired_<wbr>capacity=None, enabled_<wbr>metrics=None, force_<wbr>delete=None, health_<wbr>check_<wbr>grace_<wbr>period=None, health_<wbr>check_<wbr>type=None, initial_<wbr>lifecycle_<wbr>hooks=None, launch_<wbr>configuration=None, launch_<wbr>template=None, load_<wbr>balancers=None, max_<wbr>instance_<wbr>lifetime=None, max_<wbr>size=None, metrics_<wbr>granularity=None, min_<wbr>elb_<wbr>capacity=None, min_<wbr>size=None, mixed_<wbr>instances_<wbr>policy=None, name=None, name_<wbr>prefix=None, placement_<wbr>group=None, protect_<wbr>from_<wbr>scale_<wbr>in=None, service_<wbr>linked_<wbr>role_<wbr>arn=None, suspended_<wbr>processes=None, tags=None, tags_<wbr>collection=None, target_<wbr>group_<wbr>arns=None, termination_<wbr>policies=None, vpc_<wbr>zone_<wbr>identifiers=None, wait_<wbr>for_<wbr>capacity_<wbr>timeout=None, wait_<wbr>for_<wbr>elb_<wbr>capacity=None)
```

```go
func GetGroup(ctx *pulumi.Context, name string, id pulumi.IDInput, state *GroupState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static Group Get(string name, Input<string> id, GroupState? state = null, CustomResourceOptions? options = null);
```

Get an existing Group resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following state arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for this AutoScaling Group
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Cooldown</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Metrics</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of metrics to collect. The allowed values are `GroupDesiredCapacity`, `GroupInServiceCapacity`, `GroupPendingCapacity`, `GroupMinSize`, `GroupMaxSize`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupStandbyCapacity`, `GroupTerminatingCapacity`, `GroupTerminatingInstances`, `GroupTotalCapacity`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: &#34;10m&#34;) A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to &#34;0&#34; causes
this provider to skip all Capacity Waiting behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Delete</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it&#39;s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Grace<wbr>Period</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time (in seconds) after instance comes into service before checking health.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
&#34;EC2&#34; or &#34;ELB&#34;. Controls how health checking is done.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Initial<wbr>Lifecycle<wbr>Hooks</td>
            <td class="align-top">
                
                <code><a href="#groupinitiallifecyclehook">List&lt;Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Initial<wbr>Lifecycle<wbr>Hook<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws.autoscaling.LifecycleHook`](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws.autoscaling.LifecycleHook` resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch configuration to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#grouplaunchtemplate">Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Launch<wbr>Template<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Instance<wbr>Lifetime</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time, in seconds, that an instance can be in service, values must be either equal to 0 or between 604800 and 31536000 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum size of the auto scale group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metrics<wbr>Granularity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum size of the auto scale group.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mixed<wbr>Instances<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicy">Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Group</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the placement group into which you&#39;ll launch your instances, if any.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protect<wbr>From<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Linked<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the service-linked role that the ASG will use to call other AWS services
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Suspended<wbr>Processes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code><a href="#grouptag">List&lt;Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Tag<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks. Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags<wbr>Collection</td>
            <td class="align-top">
                
                <code>List&lt;Immutable<wbr>Dictionary&lt;string, object&gt;&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks (maps). Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Group<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of `aws.alb.TargetGroup` ARNs, for use with Application or Network Load Balancing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Termination<wbr>Policies</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `OldestLaunchTemplate`, `AllocationStrategy`, `Default`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Zone<wbr>Identifiers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to launch resources in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Capacity<wbr>Timeout</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over `min_elb_capacity` behavior.)
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for this AutoScaling Group
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Cooldown</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled<wbr>Metrics</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of metrics to collect. The allowed values are `GroupDesiredCapacity`, `GroupInServiceCapacity`, `GroupPendingCapacity`, `GroupMinSize`, `GroupMaxSize`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupStandbyCapacity`, `GroupTerminatingCapacity`, `GroupTerminatingInstances`, `GroupTotalCapacity`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: &#34;10m&#34;) A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to &#34;0&#34; causes
this provider to skip all Capacity Waiting behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Force<wbr>Delete</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it&#39;s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Grace<wbr>Period</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time (in seconds) after instance comes into service before checking health.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
&#34;EC2&#34; or &#34;ELB&#34;. Controls how health checking is done.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Initial<wbr>Lifecycle<wbr>Hooks</td>
            <td class="align-top">
                
                <code><a href="#groupinitiallifecyclehook">[]autoscaling.<wbr>Group<wbr>Initial<wbr>Lifecycle<wbr>Hook</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws.autoscaling.LifecycleHook`](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws.autoscaling.LifecycleHook` resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Configuration</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch configuration to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#grouplaunchtemplate">*autoscaling.<wbr>Group<wbr>Launch<wbr>Template</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Instance<wbr>Lifetime</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time, in seconds, that an instance can be in service, values must be either equal to 0 or between 604800 and 31536000 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum size of the auto scale group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metrics<wbr>Granularity</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum size of the auto scale group.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Mixed<wbr>Instances<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicy">*autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Group</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the placement group into which you&#39;ll launch your instances, if any.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protect<wbr>From<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Linked<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the service-linked role that the ASG will use to call other AWS services
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Suspended<wbr>Processes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code><a href="#grouptag">[]autoscaling.<wbr>Group<wbr>Tag</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks. Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags<wbr>Collection</td>
            <td class="align-top">
                
                <code>[]map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks (maps). Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Group<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of `aws.alb.TargetGroup` ARNs, for use with Application or Network Load Balancing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Termination<wbr>Policies</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `OldestLaunchTemplate`, `AllocationStrategy`, `Default`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Zone<wbr>Identifiers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to launch resources in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Capacity<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over `min_elb_capacity` behavior.)
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for this AutoScaling Group
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Cooldown</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled<wbr>Metrics</td>
            <td class="align-top">
                
                <code>Metric[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of metrics to collect. The allowed values are `GroupDesiredCapacity`, `GroupInServiceCapacity`, `GroupPendingCapacity`, `GroupMinSize`, `GroupMaxSize`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupStandbyCapacity`, `GroupTerminatingCapacity`, `GroupTerminatingInstances`, `GroupTotalCapacity`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: &#34;10m&#34;) A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to &#34;0&#34; causes
this provider to skip all Capacity Waiting behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force<wbr>Delete</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it&#39;s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Grace<wbr>Period</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time (in seconds) after instance comes into service before checking health.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
&#34;EC2&#34; or &#34;ELB&#34;. Controls how health checking is done.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">initial<wbr>Lifecycle<wbr>Hooks</td>
            <td class="align-top">
                
                <code><a href="#groupinitiallifecyclehook">autoscaling.<wbr>Group<wbr>Initial<wbr>Lifecycle<wbr>Hook[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws.autoscaling.LifecycleHook`](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws.autoscaling.LifecycleHook` resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string | Launch<wbr>Configuration</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch configuration to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#grouplaunchtemplate">autoscaling.<wbr>Group<wbr>Launch<wbr>Template?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Instance<wbr>Lifetime</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time, in seconds, that an instance can be in service, values must be either equal to 0 or between 604800 and 31536000 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum size of the auto scale group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metrics<wbr>Granularity</td>
            <td class="align-top">
                
                <code>string | Metrics<wbr>Granularity</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum size of the auto scale group.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mixed<wbr>Instances<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicy">autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement<wbr>Group</td>
            <td class="align-top">
                
                <code>string | Placement<wbr>Group</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the placement group into which you&#39;ll launch your instances, if any.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protect<wbr>From<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Linked<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the service-linked role that the ASG will use to call other AWS services
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">suspended<wbr>Processes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code><a href="#grouptag">autoscaling.<wbr>Group<wbr>Tag[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks. Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags<wbr>Collection</td>
            <td class="align-top">
                
                <code>{[key: string]: any}[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks (maps). Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Group<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of `aws.alb.TargetGroup` ARNs, for use with Application or Network Load Balancing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">termination<wbr>Policies</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `OldestLaunchTemplate`, `AllocationStrategy`, `Default`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Zone<wbr>Identifiers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to launch resources in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait<wbr>For<wbr>Capacity<wbr>Timeout</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait<wbr>For<wbr>Elb<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over `min_elb_capacity` behavior.)
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for this AutoScaling Group
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of one or more availability zones for the group. This parameter should not be specified when using `vpc_zone_identifier`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>cooldown</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">desired_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled_<wbr>metrics</td>
            <td class="align-top">
                
                <code>list[metric]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of metrics to collect. The allowed values are `GroupDesiredCapacity`, `GroupInServiceCapacity`, `GroupPendingCapacity`, `GroupMinSize`, `GroupMaxSize`, `GroupInServiceInstances`, `GroupPendingInstances`, `GroupStandbyInstances`, `GroupStandbyCapacity`, `GroupTerminatingCapacity`, `GroupTerminatingInstances`, `GroupTotalCapacity`, `GroupTotalInstances`.
* `wait_for_capacity_timeout` (Default: &#34;10m&#34;) A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to &#34;0&#34; causes
this provider to skip all Capacity Waiting behavior.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">force_<wbr>delete</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it&#39;s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>grace_<wbr>period</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Time (in seconds) after instance comes into service before checking health.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
&#34;EC2&#34; or &#34;ELB&#34;. Controls how health checking is done.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">initial_<wbr>lifecycle_<wbr>hooks</td>
            <td class="align-top">
                
                <code><a href="#groupinitiallifecyclehook">list[group_<wbr>initial_<wbr>lifecycle_<wbr>hook]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more
[Lifecycle Hooks](http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html)
to attach to the autoscaling group **before** instances are launched. The
syntax is exactly the same as the separate
[`aws.autoscaling.LifecycleHook`](https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hook.html)
resource, without the `autoscaling_group_name` attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use `aws.autoscaling.LifecycleHook` resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch_<wbr>configuration</td>
            <td class="align-top">
                
                <code>dict</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch configuration to use.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch_<wbr>template</td>
            <td class="align-top">
                
                <code><a href="#grouplaunchtemplate">dict{group_<wbr>launch_<wbr>template}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load_<wbr>balancers</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use `target_group_arns` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>instance_<wbr>lifetime</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum amount of time, in seconds, that an instance can be in service, values must be either equal to 0 or between 604800 and 31536000 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum size of the auto scale group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metrics_<wbr>granularity</td>
            <td class="align-top">
                
                <code>dict</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The granularity to associate with the metrics to collect. The only valid value is `1Minute`. Default is `1Minute`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>elb_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The minimum size of the auto scale group.
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">mixed_<wbr>instances_<wbr>policy</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicy">dict{group_<wbr>mixed_<wbr>instances_<wbr>policy}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement_<wbr>group</td>
            <td class="align-top">
                
                <code>dict</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the placement group into which you&#39;ll launch your instances, if any.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protect_<wbr>from_<wbr>scale_<wbr>in</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>linked_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the service-linked role that the ASG will use to call other AWS services
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">suspended_<wbr>processes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of processes to suspend for the AutoScaling Group. The allowed values are `Launch`, `Terminate`, `HealthCheck`, `ReplaceUnhealthy`, `AZRebalance`, `AlarmNotification`, `ScheduledActions`, `AddToLoadBalancer`.
Note that if you suspend either the `Launch` or `Terminate` process types, it can prevent your autoscaling group from functioning properly.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code><a href="#grouptag">list[group_<wbr>tag]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks. Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags_<wbr>collection</td>
            <td class="align-top">
                
                <code>list[any>]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of tag blocks (maps). Tags documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>group_<wbr>arns</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of `aws.alb.TargetGroup` ARNs, for use with Application or Network Load Balancing.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">termination_<wbr>policies</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are `OldestInstance`, `NewestInstance`, `OldestLaunchConfiguration`, `ClosestToNextInstanceHour`, `OldestLaunchTemplate`, `AllocationStrategy`, `Default`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>zone_<wbr>identifiers</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to launch resources in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait_<wbr>for_<wbr>capacity_<wbr>timeout</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait_<wbr>for_<wbr>elb_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over `min_elb_capacity` behavior.)
(See also Waiting for Capacity below.)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### GroupInitialLifecycleHook
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GroupInitialLifecycleHook">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GroupInitialLifecycleHook">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupInitialLifecycleHookArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupInitialLifecycleHookOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupInitialLifecycleHookArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupInitialLifecycleHook.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Default<wbr>Result</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Heartbeat<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lifecycle<wbr>Transition</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Metadata</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Target<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Default<wbr>Result</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Heartbeat<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lifecycle<wbr>Transition</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Metadata</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Target<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">default<wbr>Result</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">heartbeat<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lifecycle<wbr>Transition</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification<wbr>Metadata</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification<wbr>Target<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">default_<wbr>result</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">heartbeat_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lifecycle_<wbr>transition</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification_<wbr>metadata</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification_<wbr>target_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GroupLaunchTemplate
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GroupLaunchTemplate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GroupLaunchTemplate">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupLaunchTemplateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupLaunchTemplateOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupLaunchTemplateArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupLaunchTemplate.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The autoscaling group id.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Template version. Can be version number, `$Latest`, or `$Default`. (Default: `$Default`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The autoscaling group id.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Template version. Can be version number, `$Latest`, or `$Default`. (Default: `$Default`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The autoscaling group id.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Template version. Can be version number, `$Latest`, or `$Default`. (Default: `$Default`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The autoscaling group id.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the auto scaling group. By default generated by this provider.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Template version. Can be version number, `$Latest`, or `$Default`. (Default: `$Default`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GroupMixedInstancesPolicy
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GroupMixedInstancesPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GroupMixedInstancesPolicy">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupMixedInstancesPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupMixedInstancesPolicyOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupMixedInstancesPolicyArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupMixedInstancesPolicy.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Instances<wbr>Distribution</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicyinstancesdistribution">Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy<wbr>Instances<wbr>Distribution<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing settings on how to mix on-demand and Spot instances in the Auto Scaling group. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicylaunchtemplate">Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy<wbr>Launch<wbr>Template<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Instances<wbr>Distribution</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicyinstancesdistribution">*autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy<wbr>Instances<wbr>Distribution</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing settings on how to mix on-demand and Spot instances in the Auto Scaling group. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicylaunchtemplate">autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy<wbr>Launch<wbr>Template</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">instances<wbr>Distribution</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicyinstancesdistribution">autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy<wbr>Instances<wbr>Distribution?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing settings on how to mix on-demand and Spot instances in the Auto Scaling group. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch<wbr>Template</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicylaunchtemplate">autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy<wbr>Launch<wbr>Template</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">instances_<wbr>distribution</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicyinstancesdistribution">dict{group_<wbr>mixed_<wbr>instances_<wbr>policy_<wbr>instances_<wbr>distribution}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument containing settings on how to mix on-demand and Spot instances in the Auto Scaling group. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch_<wbr>template</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicylaunchtemplate">dict{group_<wbr>mixed_<wbr>instances_<wbr>policy_<wbr>launch_<wbr>template}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GroupMixedInstancesPolicyInstancesDistribution
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GroupMixedInstancesPolicyInstancesDistribution">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GroupMixedInstancesPolicyInstancesDistribution">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupMixedInstancesPolicyInstancesDistributionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupMixedInstancesPolicyInstancesDistributionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupMixedInstancesPolicyInstancesDistributionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupMixedInstancesPolicyInstancesDistribution.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">On<wbr>Demand<wbr>Allocation<wbr>Strategy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Strategy to use when launching on-demand instances. Valid values: `prioritized`. Default: `prioritized`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Demand<wbr>Base<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Absolute minimum amount of desired capacity that must be fulfilled by on-demand instances. Default: `0`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Demand<wbr>Percentage<wbr>Above<wbr>Base<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Percentage split between on-demand and Spot instances above the base on-demand capacity. Default: `100`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Allocation<wbr>Strategy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How to allocate capacity across the Spot pools. Valid values: `lowest-price`, `capacity-optimized`. Default: `lowest-price`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Instance<wbr>Pools</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of Spot pools per availability zone to allocate capacity. EC2 Auto Scaling selects the cheapest Spot pools and evenly allocates Spot capacity across the number of Spot pools that you specify. Default: `2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Max<wbr>Price</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum price per unit hour that the user is willing to pay for the Spot instances. Default: an empty string which means the on-demand price.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">On<wbr>Demand<wbr>Allocation<wbr>Strategy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Strategy to use when launching on-demand instances. Valid values: `prioritized`. Default: `prioritized`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Demand<wbr>Base<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Absolute minimum amount of desired capacity that must be fulfilled by on-demand instances. Default: `0`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Demand<wbr>Percentage<wbr>Above<wbr>Base<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Percentage split between on-demand and Spot instances above the base on-demand capacity. Default: `100`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Allocation<wbr>Strategy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How to allocate capacity across the Spot pools. Valid values: `lowest-price`, `capacity-optimized`. Default: `lowest-price`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Instance<wbr>Pools</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of Spot pools per availability zone to allocate capacity. EC2 Auto Scaling selects the cheapest Spot pools and evenly allocates Spot capacity across the number of Spot pools that you specify. Default: `2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Max<wbr>Price</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum price per unit hour that the user is willing to pay for the Spot instances. Default: an empty string which means the on-demand price.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">on<wbr>Demand<wbr>Allocation<wbr>Strategy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Strategy to use when launching on-demand instances. Valid values: `prioritized`. Default: `prioritized`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on<wbr>Demand<wbr>Base<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Absolute minimum amount of desired capacity that must be fulfilled by on-demand instances. Default: `0`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on<wbr>Demand<wbr>Percentage<wbr>Above<wbr>Base<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Percentage split between on-demand and Spot instances above the base on-demand capacity. Default: `100`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot<wbr>Allocation<wbr>Strategy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How to allocate capacity across the Spot pools. Valid values: `lowest-price`, `capacity-optimized`. Default: `lowest-price`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot<wbr>Instance<wbr>Pools</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of Spot pools per availability zone to allocate capacity. EC2 Auto Scaling selects the cheapest Spot pools and evenly allocates Spot capacity across the number of Spot pools that you specify. Default: `2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot<wbr>Max<wbr>Price</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum price per unit hour that the user is willing to pay for the Spot instances. Default: an empty string which means the on-demand price.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">on_<wbr>demand_<wbr>allocation_<wbr>strategy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Strategy to use when launching on-demand instances. Valid values: `prioritized`. Default: `prioritized`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on_<wbr>demand_<wbr>base_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Absolute minimum amount of desired capacity that must be fulfilled by on-demand instances. Default: `0`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on_<wbr>demand_<wbr>percentage_<wbr>above_<wbr>base_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Percentage split between on-demand and Spot instances above the base on-demand capacity. Default: `100`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot_<wbr>allocation_<wbr>strategy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
How to allocate capacity across the Spot pools. Valid values: `lowest-price`, `capacity-optimized`. Default: `lowest-price`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot_<wbr>instance_<wbr>pools</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Number of Spot pools per availability zone to allocate capacity. EC2 Auto Scaling selects the cheapest Spot pools and evenly allocates Spot capacity across the number of Spot pools that you specify. Default: `2`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot_<wbr>max_<wbr>price</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maximum price per unit hour that the user is willing to pay for the Spot instances. Default: an empty string which means the on-demand price.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GroupMixedInstancesPolicyLaunchTemplate
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GroupMixedInstancesPolicyLaunchTemplate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GroupMixedInstancesPolicyLaunchTemplate">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupMixedInstancesPolicyLaunchTemplateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupMixedInstancesPolicyLaunchTemplateOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupMixedInstancesPolicyLaunchTemplateArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupMixedInstancesPolicyLaunchTemplate.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Launch<wbr>Template<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicylaunchtemplatelaunchtemplatespecification">Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy<wbr>Launch<wbr>Template<wbr>Launch<wbr>Template<wbr>Specification<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument defines the Launch Template. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Overrides</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicylaunchtemplateoverride">List&lt;Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy<wbr>Launch<wbr>Template<wbr>Override<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of nested arguments provides the ability to specify multiple instance types. This will override the same parameter in the launch template. For on-demand instances, Auto Scaling considers the order of preference of instance types to launch based on the order specified in the overrides list. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Launch<wbr>Template<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicylaunchtemplatelaunchtemplatespecification">autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy<wbr>Launch<wbr>Template<wbr>Launch<wbr>Template<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument defines the Launch Template. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Overrides</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicylaunchtemplateoverride">[]autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy<wbr>Launch<wbr>Template<wbr>Override</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of nested arguments provides the ability to specify multiple instance types. This will override the same parameter in the launch template. For on-demand instances, Auto Scaling considers the order of preference of instance types to launch based on the order specified in the overrides list. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">launch<wbr>Template<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicylaunchtemplatelaunchtemplatespecification">autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy<wbr>Launch<wbr>Template<wbr>Launch<wbr>Template<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument defines the Launch Template. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">overrides</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicylaunchtemplateoverride">autoscaling.<wbr>Group<wbr>Mixed<wbr>Instances<wbr>Policy<wbr>Launch<wbr>Template<wbr>Override[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of nested arguments provides the ability to specify multiple instance types. This will override the same parameter in the launch template. For on-demand instances, Auto Scaling considers the order of preference of instance types to launch based on the order specified in the overrides list. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">launch_<wbr>template_<wbr>specification</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicylaunchtemplatelaunchtemplatespecification">dict{group_<wbr>mixed_<wbr>instances_<wbr>policy_<wbr>launch_<wbr>template_<wbr>launch_<wbr>template_<wbr>specification}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Nested argument defines the Launch Template. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">overrides</td>
            <td class="align-top">
                
                <code><a href="#groupmixedinstancespolicylaunchtemplateoverride">list[group_<wbr>mixed_<wbr>instances_<wbr>policy_<wbr>launch_<wbr>template_<wbr>override]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of nested arguments provides the ability to specify multiple instance types. This will override the same parameter in the launch template. For on-demand instances, Auto Scaling considers the order of preference of instance types to launch based on the order specified in the overrides list. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Launch<wbr>Template<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the launch template. Conflicts with `launch_template_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Template<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. Conflicts with `launch_template_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Template version. Can be version number, `$Latest`, or `$Default`. (Default: `$Default`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Launch<wbr>Template<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the launch template. Conflicts with `launch_template_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Template<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. Conflicts with `launch_template_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Template version. Can be version number, `$Latest`, or `$Default`. (Default: `$Default`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">launch<wbr>Template<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the launch template. Conflicts with `launch_template_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch<wbr>Template<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. Conflicts with `launch_template_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Template version. Can be version number, `$Latest`, or `$Default`. (Default: `$Default`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">launch_<wbr>template_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the launch template. Conflicts with `launch_template_name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch_<wbr>template_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. Conflicts with `launch_template_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Template version. Can be version number, `$Latest`, or `$Default`. (Default: `$Default`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GroupMixedInstancesPolicyLaunchTemplateOverride
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GroupMixedInstancesPolicyLaunchTemplateOverride">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GroupMixedInstancesPolicyLaunchTemplateOverride">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupMixedInstancesPolicyLaunchTemplateOverrideArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupMixedInstancesPolicyLaunchTemplateOverrideOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupMixedInstancesPolicyLaunchTemplateOverrideArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupMixedInstancesPolicyLaunchTemplateOverride.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Override the instance type in the Launch Template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Weighted<wbr>Capacity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of capacity units, which gives the instance type a proportional weight to other instance types.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Override the instance type in the Launch Template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Weighted<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of capacity units, which gives the instance type a proportional weight to other instance types.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Override the instance type in the Launch Template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">weighted<wbr>Capacity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of capacity units, which gives the instance type a proportional weight to other instance types.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">instance_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Override the instance type in the Launch Template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">weighted_<wbr>capacity</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of capacity units, which gives the instance type a proportional weight to other instance types.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GroupTag
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GroupTag">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GroupTag">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupTagArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#GroupTagOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupTagArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GroupTag.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Key
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Propagate<wbr>At<wbr>Launch</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Enables propagation of the tag to
Amazon EC2 instances launched via this ASG
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Value
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Key
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Propagate<wbr>At<wbr>Launch</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Enables propagation of the tag to
Amazon EC2 instances launched via this ASG
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Value
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Key
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">propagate<wbr>At<wbr>Launch</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Enables propagation of the tag to
Amazon EC2 instances launched via this ASG
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Value
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Key
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">propagate_<wbr>at_<wbr>launch</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Enables propagation of the tag to
Amazon EC2 instances launched via this ASG
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Value
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







