
---
title: "Policy"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an AutoScaling Scaling Policy resource.

> **NOTE:** You may want to omit `desired_capacity` attribute from attached `aws.autoscaling.Group`
when using autoscaling policies. It's good practice to pick either
[manual](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-manual-scaling.html)
or [dynamic](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-scale-based-on-demand.html)
(policy-based) scaling.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bar = new aws.autoscaling.Group("bar", {
    availabilityZones: ["us-east-1a"],
    forceDelete: true,
    healthCheckGracePeriod: 300,
    healthCheckType: "ELB",
    launchConfiguration: aws_launch_configuration_foo.name,
    maxSize: 5,
    minSize: 2,
});
const bat = new aws.autoscaling.Policy("bat", {
    adjustmentType: "ChangeInCapacity",
    autoscalingGroupName: bar.name,
    cooldown: 300,
    scalingAdjustment: 4,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_policy.html.markdown.



## Create a Policy Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/autoscaling/#Policy">Policy</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/autoscaling/#PolicyArgs">PolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Policy</span><span class="p">(resource_name, id, opts=None, </span>adjustment_type=None<span class="p">, </span>autoscaling_group_name=None<span class="p">, </span>cooldown=None<span class="p">, </span>estimated_instance_warmup=None<span class="p">, </span>metric_aggregation_type=None<span class="p">, </span>min_adjustment_magnitude=None<span class="p">, </span>name=None<span class="p">, </span>policy_type=None<span class="p">, </span>scaling_adjustment=None<span class="p">, </span>step_adjustments=None<span class="p">, </span>target_tracking_configuration=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#PolicyArgs">PolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#Policy">Policy</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.Policy.html">Policy</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.PolicyArgs.html">PolicyArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Policy resource with the given unique name, arguments, and options.

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
            <td class="align-top">Adjustment<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the autoscaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cooldown</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Estimated<wbr>Instance<wbr>Warmup</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group&#39;s specified cooldown period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Aggregation<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The aggregation type for the policy&#39;s metrics. Valid values are &#34;Minimum&#34;, &#34;Maximum&#34;, and &#34;Average&#34;. Without a value, AWS will treat the aggregation type as &#34;Average&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Adjustment<wbr>Magnitude</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
The name of the dimension.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The policy type, either &#34;SimpleScaling&#34;, &#34;StepScaling&#34; or &#34;TargetTrackingScaling&#34;. If this value isn&#39;t provided, AWS will default to &#34;SimpleScaling.&#34;
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Adjustment</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Step<wbr>Adjustments</td>
            <td class="align-top">
                
                <code><a href="#policystepadjustment">List&lt;Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Policy<wbr>Step<wbr>Adjustment<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of adjustments that manage
group scaling. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Tracking<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfiguration">Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A target tracking policy. These have the following structure:
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
            <td class="align-top">Adjustment<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the autoscaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cooldown</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Estimated<wbr>Instance<wbr>Warmup</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group&#39;s specified cooldown period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Aggregation<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The aggregation type for the policy&#39;s metrics. Valid values are &#34;Minimum&#34;, &#34;Maximum&#34;, and &#34;Average&#34;. Without a value, AWS will treat the aggregation type as &#34;Average&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Adjustment<wbr>Magnitude</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
The name of the dimension.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The policy type, either &#34;SimpleScaling&#34;, &#34;StepScaling&#34; or &#34;TargetTrackingScaling&#34;. If this value isn&#39;t provided, AWS will default to &#34;SimpleScaling.&#34;
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Adjustment</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Step<wbr>Adjustments</td>
            <td class="align-top">
                
                <code><a href="#policystepadjustment">[]autoscaling.<wbr>Policy<wbr>Step<wbr>Adjustment</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of adjustments that manage
group scaling. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Tracking<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfiguration">*autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A target tracking policy. These have the following structure:
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
            <td class="align-top">adjustment<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the autoscaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cooldown</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">estimated<wbr>Instance<wbr>Warmup</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group&#39;s specified cooldown period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Aggregation<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The aggregation type for the policy&#39;s metrics. Valid values are &#34;Minimum&#34;, &#34;Maximum&#34;, and &#34;Average&#34;. Without a value, AWS will treat the aggregation type as &#34;Average&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Adjustment<wbr>Magnitude</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
The name of the dimension.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The policy type, either &#34;SimpleScaling&#34;, &#34;StepScaling&#34; or &#34;TargetTrackingScaling&#34;. If this value isn&#39;t provided, AWS will default to &#34;SimpleScaling.&#34;
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling<wbr>Adjustment</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">step<wbr>Adjustments</td>
            <td class="align-top">
                
                <code><a href="#policystepadjustment">autoscaling.<wbr>Policy<wbr>Step<wbr>Adjustment[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of adjustments that manage
group scaling. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Tracking<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfiguration">autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A target tracking policy. These have the following structure:
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
            <td class="align-top">adjustment_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the autoscaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cooldown</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">estimated_<wbr>instance_<wbr>warmup</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group&#39;s specified cooldown period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric_<wbr>aggregation_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The aggregation type for the policy&#39;s metrics. Valid values are &#34;Minimum&#34;, &#34;Maximum&#34;, and &#34;Average&#34;. Without a value, AWS will treat the aggregation type as &#34;Average&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>adjustment_<wbr>magnitude</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
The name of the dimension.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The policy type, either &#34;SimpleScaling&#34;, &#34;StepScaling&#34; or &#34;TargetTrackingScaling&#34;. If this value isn&#39;t provided, AWS will default to &#34;SimpleScaling.&#34;
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling_<wbr>adjustment</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">step_<wbr>adjustments</td>
            <td class="align-top">
                
                <code><a href="#policystepadjustment">list[policy_<wbr>step_<wbr>adjustment]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of adjustments that manage
group scaling. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>tracking_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfiguration">dict{policy_<wbr>target_<wbr>tracking_<wbr>configuration}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A target tracking policy. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Policy Output Properties

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
            <td class="align-top">Adjustment<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN assigned by AWS to the scaling policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the autoscaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cooldown</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Estimated<wbr>Instance<wbr>Warmup</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group&#39;s specified cooldown period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Aggregation<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The aggregation type for the policy&#39;s metrics. Valid values are &#34;Minimum&#34;, &#34;Maximum&#34;, and &#34;Average&#34;. Without a value, AWS will treat the aggregation type as &#34;Average&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Adjustment<wbr>Magnitude</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the dimension.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The policy type, either &#34;SimpleScaling&#34;, &#34;StepScaling&#34; or &#34;TargetTrackingScaling&#34;. If this value isn&#39;t provided, AWS will default to &#34;SimpleScaling.&#34;
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Adjustment</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Step<wbr>Adjustments</td>
            <td class="align-top">
                
                <code><a href="#policystepadjustment">List&lt;Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Policy<wbr>Step<wbr>Adjustment&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of adjustments that manage
group scaling. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Tracking<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfiguration">Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} A target tracking policy. These have the following structure:
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
            <td class="align-top">Adjustment<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN assigned by AWS to the scaling policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the autoscaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cooldown</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Estimated<wbr>Instance<wbr>Warmup</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group&#39;s specified cooldown period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Aggregation<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The aggregation type for the policy&#39;s metrics. Valid values are &#34;Minimum&#34;, &#34;Maximum&#34;, and &#34;Average&#34;. Without a value, AWS will treat the aggregation type as &#34;Average&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Adjustment<wbr>Magnitude</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the dimension.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The policy type, either &#34;SimpleScaling&#34;, &#34;StepScaling&#34; or &#34;TargetTrackingScaling&#34;. If this value isn&#39;t provided, AWS will default to &#34;SimpleScaling.&#34;
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Adjustment</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Step<wbr>Adjustments</td>
            <td class="align-top">
                
                <code><a href="#policystepadjustment">[]autoscaling.<wbr>Policy<wbr>Step<wbr>Adjustment</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of adjustments that manage
group scaling. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Tracking<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfiguration">*autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} A target tracking policy. These have the following structure:
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
            <td class="align-top">adjustment<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN assigned by AWS to the scaling policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the autoscaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cooldown</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">estimated<wbr>Instance<wbr>Warmup</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group&#39;s specified cooldown period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Aggregation<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The aggregation type for the policy&#39;s metrics. Valid values are &#34;Minimum&#34;, &#34;Maximum&#34;, and &#34;Average&#34;. Without a value, AWS will treat the aggregation type as &#34;Average&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Adjustment<wbr>Magnitude</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the dimension.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The policy type, either &#34;SimpleScaling&#34;, &#34;StepScaling&#34; or &#34;TargetTrackingScaling&#34;. If this value isn&#39;t provided, AWS will default to &#34;SimpleScaling.&#34;
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling<wbr>Adjustment</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">step<wbr>Adjustments</td>
            <td class="align-top">
                
                <code><a href="#policystepadjustment">autoscaling.<wbr>Policy<wbr>Step<wbr>Adjustment[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of adjustments that manage
group scaling. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Tracking<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfiguration">autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} A target tracking policy. These have the following structure:
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
            <td class="align-top">adjustment_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN assigned by AWS to the scaling policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the autoscaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cooldown</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">estimated_<wbr>instance_<wbr>warmup</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group&#39;s specified cooldown period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric_<wbr>aggregation_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The aggregation type for the policy&#39;s metrics. Valid values are &#34;Minimum&#34;, &#34;Maximum&#34;, and &#34;Average&#34;. Without a value, AWS will treat the aggregation type as &#34;Average&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>adjustment_<wbr>magnitude</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the dimension.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The policy type, either &#34;SimpleScaling&#34;, &#34;StepScaling&#34; or &#34;TargetTrackingScaling&#34;. If this value isn&#39;t provided, AWS will default to &#34;SimpleScaling.&#34;
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling_<wbr>adjustment</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">step_<wbr>adjustments</td>
            <td class="align-top">
                
                <code><a href="#policystepadjustment">list[policy_<wbr>step_<wbr>adjustment]</a></code>
            </td>
            <td class="align-top">{{% md %}} A set of adjustments that manage
group scaling. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>tracking_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfiguration">dict{policy_<wbr>target_<wbr>tracking_<wbr>configuration}</a></code>
            </td>
            <td class="align-top">{{% md %}} A target tracking policy. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Policy Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PolicyState, opts?: pulumi.CustomResourceOptions): Policy;
```

```python
def get(resource_name, id, opts=None, adjustment_<wbr>type=None, arn=None, autoscaling_<wbr>group_<wbr>name=None, cooldown=None, estimated_<wbr>instance_<wbr>warmup=None, metric_<wbr>aggregation_<wbr>type=None, min_<wbr>adjustment_<wbr>magnitude=None, name=None, policy_<wbr>type=None, scaling_<wbr>adjustment=None, step_<wbr>adjustments=None, target_<wbr>tracking_<wbr>configuration=None)
```

```go
func GetPolicy(ctx *pulumi.Context, name string, id pulumi.IDInput, state *PolicyState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static Policy Get(string name, Input<string> id, PolicyState? state = null, CustomResourceOptions? options = null);
```

Get an existing Policy resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Adjustment<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN assigned by AWS to the scaling policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the autoscaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cooldown</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Estimated<wbr>Instance<wbr>Warmup</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group&#39;s specified cooldown period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Aggregation<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The aggregation type for the policy&#39;s metrics. Valid values are &#34;Minimum&#34;, &#34;Maximum&#34;, and &#34;Average&#34;. Without a value, AWS will treat the aggregation type as &#34;Average&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Adjustment<wbr>Magnitude</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
The name of the dimension.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The policy type, either &#34;SimpleScaling&#34;, &#34;StepScaling&#34; or &#34;TargetTrackingScaling&#34;. If this value isn&#39;t provided, AWS will default to &#34;SimpleScaling.&#34;
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Adjustment</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Step<wbr>Adjustments</td>
            <td class="align-top">
                
                <code><a href="#policystepadjustment">List&lt;Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Policy<wbr>Step<wbr>Adjustment<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of adjustments that manage
group scaling. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Tracking<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfiguration">Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A target tracking policy. These have the following structure:
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
            <td class="align-top">Adjustment<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN assigned by AWS to the scaling policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the autoscaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cooldown</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Estimated<wbr>Instance<wbr>Warmup</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group&#39;s specified cooldown period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Aggregation<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The aggregation type for the policy&#39;s metrics. Valid values are &#34;Minimum&#34;, &#34;Maximum&#34;, and &#34;Average&#34;. Without a value, AWS will treat the aggregation type as &#34;Average&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Adjustment<wbr>Magnitude</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
The name of the dimension.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The policy type, either &#34;SimpleScaling&#34;, &#34;StepScaling&#34; or &#34;TargetTrackingScaling&#34;. If this value isn&#39;t provided, AWS will default to &#34;SimpleScaling.&#34;
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Adjustment</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Step<wbr>Adjustments</td>
            <td class="align-top">
                
                <code><a href="#policystepadjustment">[]autoscaling.<wbr>Policy<wbr>Step<wbr>Adjustment</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of adjustments that manage
group scaling. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Tracking<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfiguration">*autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A target tracking policy. These have the following structure:
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
            <td class="align-top">adjustment<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN assigned by AWS to the scaling policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the autoscaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cooldown</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">estimated<wbr>Instance<wbr>Warmup</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group&#39;s specified cooldown period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Aggregation<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The aggregation type for the policy&#39;s metrics. Valid values are &#34;Minimum&#34;, &#34;Maximum&#34;, and &#34;Average&#34;. Without a value, AWS will treat the aggregation type as &#34;Average&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Adjustment<wbr>Magnitude</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
The name of the dimension.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The policy type, either &#34;SimpleScaling&#34;, &#34;StepScaling&#34; or &#34;TargetTrackingScaling&#34;. If this value isn&#39;t provided, AWS will default to &#34;SimpleScaling.&#34;
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling<wbr>Adjustment</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">step<wbr>Adjustments</td>
            <td class="align-top">
                
                <code><a href="#policystepadjustment">autoscaling.<wbr>Policy<wbr>Step<wbr>Adjustment[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of adjustments that manage
group scaling. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Tracking<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfiguration">autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A target tracking policy. These have the following structure:
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
            <td class="align-top">adjustment_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are `ChangeInCapacity`, `ExactCapacity`, and `PercentChangeInCapacity`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN assigned by AWS to the scaling policy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the autoscaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cooldown</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">estimated_<wbr>instance_<wbr>warmup</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group&#39;s specified cooldown period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric_<wbr>aggregation_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The aggregation type for the policy&#39;s metrics. Valid values are &#34;Minimum&#34;, &#34;Maximum&#34;, and &#34;Average&#34;. Without a value, AWS will treat the aggregation type as &#34;Average&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>adjustment_<wbr>magnitude</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
The name of the dimension.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The policy type, either &#34;SimpleScaling&#34;, &#34;StepScaling&#34; or &#34;TargetTrackingScaling&#34;. If this value isn&#39;t provided, AWS will default to &#34;SimpleScaling.&#34;
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling_<wbr>adjustment</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">step_<wbr>adjustments</td>
            <td class="align-top">
                
                <code><a href="#policystepadjustment">list[policy_<wbr>step_<wbr>adjustment]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of adjustments that manage
group scaling. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>tracking_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfiguration">dict{policy_<wbr>target_<wbr>tracking_<wbr>configuration}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A target tracking policy. These have the following structure:
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### PolicyStepAdjustment
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PolicyStepAdjustment">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PolicyStepAdjustment">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#PolicyStepAdjustmentArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#PolicyStepAdjustmentOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.PolicyStepAdjustmentArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.PolicyStepAdjustment.html">output</a> API doc for this type.
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
            <td class="align-top">Metric<wbr>Interval<wbr>Lower<wbr>Bound</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The lower bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Interval<wbr>Upper<wbr>Bound</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The upper bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity. The upper bound
must be greater than the lower bound.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Adjustment</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
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
            <td class="align-top">Metric<wbr>Interval<wbr>Lower<wbr>Bound</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The lower bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Interval<wbr>Upper<wbr>Bound</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The upper bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity. The upper bound
must be greater than the lower bound.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Adjustment</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
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
            <td class="align-top">metric<wbr>Interval<wbr>Lower<wbr>Bound</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The lower bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Interval<wbr>Upper<wbr>Bound</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The upper bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity. The upper bound
must be greater than the lower bound.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling<wbr>Adjustment</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
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
            <td class="align-top">metric_<wbr>interval_<wbr>lower_<wbr>bound</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The lower bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric_<wbr>interval_<wbr>upper_<wbr>bound</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The upper bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity. The upper bound
must be greater than the lower bound.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling_<wbr>adjustment</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### PolicyTargetTrackingConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PolicyTargetTrackingConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PolicyTargetTrackingConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#PolicyTargetTrackingConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#PolicyTargetTrackingConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.PolicyTargetTrackingConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.PolicyTargetTrackingConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Customized<wbr>Metric<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfigurationcustomizedmetricspecification">Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration<wbr>Customized<wbr>Metric<wbr>Specification<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A customized metric. Conflicts with `predefined_metric_specification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disable<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether scale in by the target tracking policy is disabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Predefined<wbr>Metric<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfigurationpredefinedmetricspecification">Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration<wbr>Predefined<wbr>Metric<wbr>Specification<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A predefined metric. Conflicts with `customized_metric_specification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Value</td>
            <td class="align-top">
                
                <code>double</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The target value for the metric.
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
            <td class="align-top">Customized<wbr>Metric<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfigurationcustomizedmetricspecification">*autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration<wbr>Customized<wbr>Metric<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A customized metric. Conflicts with `predefined_metric_specification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disable<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether scale in by the target tracking policy is disabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Predefined<wbr>Metric<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfigurationpredefinedmetricspecification">*autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration<wbr>Predefined<wbr>Metric<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A predefined metric. Conflicts with `customized_metric_specification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Value</td>
            <td class="align-top">
                
                <code>float64</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The target value for the metric.
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
            <td class="align-top">customized<wbr>Metric<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfigurationcustomizedmetricspecification">autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration<wbr>Customized<wbr>Metric<wbr>Specification?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A customized metric. Conflicts with `predefined_metric_specification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disable<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether scale in by the target tracking policy is disabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">predefined<wbr>Metric<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfigurationpredefinedmetricspecification">autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration<wbr>Predefined<wbr>Metric<wbr>Specification?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A predefined metric. Conflicts with `customized_metric_specification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Value</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The target value for the metric.
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
            <td class="align-top">customized_<wbr>metric_<wbr>specification</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfigurationcustomizedmetricspecification">dict{policy_<wbr>target_<wbr>tracking_<wbr>configuration_<wbr>customized_<wbr>metric_<wbr>specification}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A customized metric. Conflicts with `predefined_metric_specification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disable_<wbr>scale_<wbr>in</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether scale in by the target tracking policy is disabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">predefined_<wbr>metric_<wbr>specification</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfigurationpredefinedmetricspecification">dict{policy_<wbr>target_<wbr>tracking_<wbr>configuration_<wbr>predefined_<wbr>metric_<wbr>specification}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A predefined metric. Conflicts with `customized_metric_specification`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>value</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The target value for the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### PolicyTargetTrackingConfigurationCustomizedMetricSpecification
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PolicyTargetTrackingConfigurationCustomizedMetricSpecification">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PolicyTargetTrackingConfigurationCustomizedMetricSpecification">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#PolicyTargetTrackingConfigurationCustomizedMetricSpecificationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#PolicyTargetTrackingConfigurationCustomizedMetricSpecificationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.PolicyTargetTrackingConfigurationCustomizedMetricSpecificationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.PolicyTargetTrackingConfigurationCustomizedMetricSpecification.html">output</a> API doc for this type.
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
            <td class="align-top">Metric<wbr>Dimensions</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfigurationcustomizedmetricspecificationmetricdimension">List&lt;Pulumi.<wbr>Aws.<wbr>Autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration<wbr>Customized<wbr>Metric<wbr>Specification<wbr>Metric<wbr>Dimension<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The dimensions of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The namespace of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Statistic</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The statistic of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Unit</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unit of the metric.
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
            <td class="align-top">Metric<wbr>Dimensions</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfigurationcustomizedmetricspecificationmetricdimension">[]autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration<wbr>Customized<wbr>Metric<wbr>Specification<wbr>Metric<wbr>Dimension</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The dimensions of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The namespace of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Statistic</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The statistic of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Unit</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unit of the metric.
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
            <td class="align-top">metric<wbr>Dimensions</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfigurationcustomizedmetricspecificationmetricdimension">autoscaling.<wbr>Policy<wbr>Target<wbr>Tracking<wbr>Configuration<wbr>Customized<wbr>Metric<wbr>Specification<wbr>Metric<wbr>Dimension[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The dimensions of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The namespace of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">statistic</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The statistic of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">unit</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unit of the metric.
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
            <td class="align-top">metric_<wbr>dimensions</td>
            <td class="align-top">
                
                <code><a href="#policytargettrackingconfigurationcustomizedmetricspecificationmetricdimension">list[policy_<wbr>target_<wbr>tracking_<wbr>configuration_<wbr>customized_<wbr>metric_<wbr>specification_<wbr>metric_<wbr>dimension]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The dimensions of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The namespace of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">statistic</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The statistic of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">unit</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The unit of the metric.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimensionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.PolicyTargetTrackingConfigurationCustomizedMetricSpecificationMetricDimension.html">output</a> API doc for this type.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the dimension.
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
The value of the dimension.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the dimension.
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
The value of the dimension.
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the dimension.
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
The value of the dimension.
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the dimension.
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
The value of the dimension.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### PolicyTargetTrackingConfigurationPredefinedMetricSpecification
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#PolicyTargetTrackingConfigurationPredefinedMetricSpecification">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#PolicyTargetTrackingConfigurationPredefinedMetricSpecification">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#PolicyTargetTrackingConfigurationPredefinedMetricSpecificationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#PolicyTargetTrackingConfigurationPredefinedMetricSpecificationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.PolicyTargetTrackingConfigurationPredefinedMetricSpecificationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.PolicyTargetTrackingConfigurationPredefinedMetricSpecification.html">output</a> API doc for this type.
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
            <td class="align-top">Predefined<wbr>Metric<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The metric type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Label</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifies the resource associated with the metric type.
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
            <td class="align-top">Predefined<wbr>Metric<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The metric type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Label</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifies the resource associated with the metric type.
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
            <td class="align-top">predefined<wbr>Metric<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The metric type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource<wbr>Label</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifies the resource associated with the metric type.
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
            <td class="align-top">predefined_<wbr>metric_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The metric type.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource_<wbr>label</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifies the resource associated with the metric type.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







