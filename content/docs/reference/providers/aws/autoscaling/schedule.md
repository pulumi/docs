
---
title: "Schedule"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an AutoScaling Schedule resource.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const foobarGroup = new aws.autoscaling.Group("foobar", {
    availabilityZones: ["us-west-2a"],
    forceDelete: true,
    healthCheckGracePeriod: 300,
    healthCheckType: "ELB",
    maxSize: 1,
    minSize: 1,
    terminationPolicies: ["OldestInstance"],
});
const foobarSchedule = new aws.autoscaling.Schedule("foobar", {
    autoscalingGroupName: foobarGroup.name,
    desiredCapacity: 0,
    endTime: "2016-12-12T06:00:00Z",
    maxSize: 1,
    minSize: 0,
    scheduledActionName: "foobar",
    startTime: "2016-12-11T18:00:00Z",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_schedule.html.markdown.



## Create a Schedule Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/autoscaling/#Schedule">Schedule</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/autoscaling/#ScheduleArgs">ScheduleArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Schedule</span><span class="p">(resource_name, id, opts=None, </span>autoscaling_group_name=None<span class="p">, </span>desired_capacity=None<span class="p">, </span>end_time=None<span class="p">, </span>max_size=None<span class="p">, </span>min_size=None<span class="p">, </span>recurrence=None<span class="p">, </span>scheduled_action_name=None<span class="p">, </span>start_time=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewSchedule<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#ScheduleArgs">ScheduleArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#Schedule">Schedule</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.Schedule.html">Schedule</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.ScheduleArgs.html">ScheduleArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Schedule resource with the given unique name, arguments, and options.

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
            <td class="align-top">Autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name or Amazon Resource Name (ARN) of the Auto Scaling group.
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
The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don&#39;t want to change the desired capacity at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">End<wbr>Time</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to end, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the maximum size at the scheduled time.
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
The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the minimum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Recurrence</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scheduled<wbr>Action<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of this scaling action.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Start<wbr>Time</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to start, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
            <td class="align-top">Autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name or Amazon Resource Name (ARN) of the Auto Scaling group.
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
The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don&#39;t want to change the desired capacity at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">End<wbr>Time</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to end, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the maximum size at the scheduled time.
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
The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the minimum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Recurrence</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scheduled<wbr>Action<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of this scaling action.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Start<wbr>Time</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to start, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
            <td class="align-top">autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name or Amazon Resource Name (ARN) of the Auto Scaling group.
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
The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don&#39;t want to change the desired capacity at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">end<wbr>Time</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to end, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the maximum size at the scheduled time.
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
The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the minimum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">recurrence</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scheduled<wbr>Action<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of this scaling action.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">start<wbr>Time</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to start, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
            <td class="align-top">autoscaling_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name or Amazon Resource Name (ARN) of the Auto Scaling group.
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
The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don&#39;t want to change the desired capacity at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">end_<wbr>time</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to end, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the maximum size at the scheduled time.
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
The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the minimum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">recurrence</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scheduled_<wbr>action_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of this scaling action.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">start_<wbr>time</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to start, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Schedule Output Properties

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
            <td class="align-top">{{% md %}} The ARN assigned by AWS to the autoscaling schedule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name or Amazon Resource Name (ARN) of the Auto Scaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don&#39;t want to change the desired capacity at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">End<wbr>Time</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The time for this action to end, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the maximum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the minimum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Recurrence</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scheduled<wbr>Action<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of this scaling action.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Start<wbr>Time</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The time for this action to start, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
            <td class="align-top">{{% md %}} The ARN assigned by AWS to the autoscaling schedule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name or Amazon Resource Name (ARN) of the Auto Scaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don&#39;t want to change the desired capacity at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">End<wbr>Time</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The time for this action to end, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the maximum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the minimum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Recurrence</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scheduled<wbr>Action<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of this scaling action.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Start<wbr>Time</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The time for this action to start, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
            <td class="align-top">{{% md %}} The ARN assigned by AWS to the autoscaling schedule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name or Amazon Resource Name (ARN) of the Auto Scaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don&#39;t want to change the desired capacity at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">end<wbr>Time</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The time for this action to end, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the maximum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the minimum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">recurrence</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scheduled<wbr>Action<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of this scaling action.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">start<wbr>Time</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The time for this action to start, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
            <td class="align-top">{{% md %}} The ARN assigned by AWS to the autoscaling schedule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name or Amazon Resource Name (ARN) of the Auto Scaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">desired_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don&#39;t want to change the desired capacity at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">end_<wbr>time</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The time for this action to end, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the maximum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the minimum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">recurrence</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scheduled_<wbr>action_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of this scaling action.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">start_<wbr>time</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The time for this action to start, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Schedule Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ScheduleState, opts?: pulumi.CustomResourceOptions): Schedule;
```

```python
def get(resource_name, id, opts=None, arn=None, autoscaling_<wbr>group_<wbr>name=None, desired_<wbr>capacity=None, end_<wbr>time=None, max_<wbr>size=None, min_<wbr>size=None, recurrence=None, scheduled_<wbr>action_<wbr>name=None, start_<wbr>time=None)
```

```go
func GetSchedule(ctx *pulumi.Context, name string, id pulumi.IDInput, state *ScheduleState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static Schedule Get(string name, Input<string> id, ScheduleState? state = null, CustomResourceOptions? options = null);
```

Get an existing Schedule resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The ARN assigned by AWS to the autoscaling schedule.
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
The name or Amazon Resource Name (ARN) of the Auto Scaling group.
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
The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don&#39;t want to change the desired capacity at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">End<wbr>Time</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to end, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the maximum size at the scheduled time.
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
The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the minimum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Recurrence</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scheduled<wbr>Action<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of this scaling action.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Start<wbr>Time</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to start, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
The ARN assigned by AWS to the autoscaling schedule.
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
The name or Amazon Resource Name (ARN) of the Auto Scaling group.
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
The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don&#39;t want to change the desired capacity at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">End<wbr>Time</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to end, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the maximum size at the scheduled time.
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
The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the minimum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Recurrence</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scheduled<wbr>Action<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of this scaling action.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Start<wbr>Time</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to start, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
The ARN assigned by AWS to the autoscaling schedule.
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
The name or Amazon Resource Name (ARN) of the Auto Scaling group.
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
The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don&#39;t want to change the desired capacity at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">end<wbr>Time</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to end, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the maximum size at the scheduled time.
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
The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the minimum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">recurrence</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scheduled<wbr>Action<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of this scaling action.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">start<wbr>Time</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to start, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
The ARN assigned by AWS to the autoscaling schedule.
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
The name or Amazon Resource Name (ARN) of the Auto Scaling group.
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
The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don&#39;t want to change the desired capacity at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">end_<wbr>time</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to end, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
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
The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the maximum size at the scheduled time.
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
The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don&#39;t want to change the minimum size at the scheduled time.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">recurrence</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scheduled_<wbr>action_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of this scaling action.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">start_<wbr>time</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time for this action to start, in &#34;YYYY-MM-DDThh:mm:ssZ&#34; format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









