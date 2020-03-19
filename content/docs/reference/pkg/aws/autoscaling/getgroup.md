
---
title: "GetGroup"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Use this data source to get information on an existing autoscaling group.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const foo = aws.autoscaling.getGroup({
    name: "foo",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/autoscaling_group.html.markdown.





## Using GetGroup

{{< langchoose csharp nojavascript >}}


<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getGroup<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/autoscaling/#GetGroupArgs">GetGroupArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/autoscaling/#GetGroupResult">GetGroupResult</a></span>></span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_group(</span>name=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupGroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#LookupGroupArgs">LookupGroupArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/autoscaling?tab=doc#LookupGroupResult">LookupGroupResult</a></span>, error)</span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GetGroupResult.html">Pulumi.Aws.Autoscaling.GetGroupResult</a></span>> <span class="p">GetGroup(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Autoscaling.GetGroupArgs.html">GetGroupArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>



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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specify the exact name of the desired autoscaling group.
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
Specify the exact name of the desired autoscaling group.
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
Specify the exact name of the desired autoscaling group.
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
Specify the exact name of the desired autoscaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## GetGroup Result

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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the Auto Scaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} One or more Availability Zones for the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Cooldown</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The desired size of the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Grace<wbr>Period</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The service to use for the health checks. The valid values are EC2 and ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the associated launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} One or more load balancers associated with the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The maximum size of the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The minimum size of the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Auto Scaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">New<wbr>Instances<wbr>Protected<wbr>From<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Group</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the placement group into which to launch your instances, if any. For more information, see Placement Groups (http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the Amazon Elastic Compute Cloud User Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Linked<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The current state of the group when DeleteAutoScalingGroup is in progress.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Group<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Names (ARN) of the target groups for your load balancer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Termination<wbr>Policies</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} The termination policies for the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Zone<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} VPC ID for the group.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the Auto Scaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} One or more Availability Zones for the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Cooldown</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The desired size of the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Grace<wbr>Period</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The service to use for the health checks. The valid values are EC2 and ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the associated launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} One or more load balancers associated with the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The maximum size of the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The minimum size of the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Auto Scaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">New<wbr>Instances<wbr>Protected<wbr>From<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Group</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the placement group into which to launch your instances, if any. For more information, see Placement Groups (http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the Amazon Elastic Compute Cloud User Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Linked<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The current state of the group when DeleteAutoScalingGroup is in progress.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Group<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Names (ARN) of the target groups for your load balancer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Termination<wbr>Policies</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} The termination policies for the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Zone<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} VPC ID for the group.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the Auto Scaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} One or more Availability Zones for the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Cooldown</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">desired<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The desired size of the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Grace<wbr>Period</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The service to use for the health checks. The valid values are EC2 and ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch<wbr>Configuration</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the associated launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} One or more load balancers associated with the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The maximum size of the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The minimum size of the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Auto Scaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">new<wbr>Instances<wbr>Protected<wbr>From<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement<wbr>Group</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the placement group into which to launch your instances, if any. For more information, see Placement Groups (http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the Amazon Elastic Compute Cloud User Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Linked<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The current state of the group when DeleteAutoScalingGroup is in progress.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Group<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Names (ARN) of the target groups for your load balancer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">termination<wbr>Policies</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} The termination policies for the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Zone<wbr>Identifier</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} VPC ID for the group.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the Auto Scaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} One or more Availability Zones for the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>cooldown</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">desired_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The desired size of the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>grace_<wbr>period</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The service to use for the health checks. The valid values are EC2 and ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch_<wbr>configuration</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the associated launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load_<wbr>balancers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} One or more load balancers associated with the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The maximum size of the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The minimum size of the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Auto Scaling group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">new<wbr>Instances<wbr>Protected<wbr>From<wbr>Scale<wbr>In</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement_<wbr>group</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the placement group into which to launch your instances, if any. For more information, see Placement Groups (http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) in the Amazon Elastic Compute Cloud User Guide.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>linked_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The current state of the group when DeleteAutoScalingGroup is in progress.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>group_<wbr>arns</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} The Amazon Resource Names (ARN) of the target groups for your load balancer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">termination_<wbr>policies</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} The termination policies for the group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Zone<wbr>Identifier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} VPC ID for the group.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







