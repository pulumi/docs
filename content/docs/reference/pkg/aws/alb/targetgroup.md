
---
title: "TargetGroup"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a Target Group resource for use with Load Balancer resources.

> **Note:** `aws.alb.TargetGroup` is known as `aws.lb.TargetGroup`. The functionality is identical.

## Example Usage

### Instance Target Group

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const main = new aws.ec2.Vpc("main", {
    cidrBlock: "10.0.0.0/16",
});
const test = new aws.lb.TargetGroup("test", {
    port: 80,
    protocol: "HTTP",
    vpcId: main.id,
});
```

### IP Target Group

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const main = new aws.ec2.Vpc("main", {
    cidrBlock: "10.0.0.0/16",
});
const ip_example = new aws.lb.TargetGroup("ip-example", {
    port: 80,
    protocol: "HTTP",
    targetType: "ip",
    vpcId: main.id,
});
```

### Lambda Target Group

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const lambda_example = new aws.lb.TargetGroup("lambda-example", {
    targetType: "lambda",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lb_target_group.html.markdown.



## Create a TargetGroup Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/alb/#TargetGroup">TargetGroup</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/alb/#TargetGroupArgs">TargetGroupArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">TargetGroup</span><span class="p">(resource_name, opts=None, </span>deregistration_delay=None<span class="p">, </span>health_check=None<span class="p">, </span>lambda_multi_value_headers_enabled=None<span class="p">, </span>load_balancing_algorithm_type=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>port=None<span class="p">, </span>protocol=None<span class="p">, </span>proxy_protocol_v2=None<span class="p">, </span>slow_start=None<span class="p">, </span>stickiness=None<span class="p">, </span>tags=None<span class="p">, </span>target_type=None<span class="p">, </span>vpc_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewTargetGroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#TargetGroupArgs">TargetGroupArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#TargetGroup">TargetGroup</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.TargetGroup.html">TargetGroup</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.TargetGroupArgs.html">TargetGroupArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a TargetGroup resource with the given unique name, arguments, and options.

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
            <td class="align-top">Deregistration<wbr>Delay</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#targetgrouphealthcheck">Pulumi.<wbr>Aws.<wbr>Alb.<wbr>Target<wbr>Group<wbr>Health<wbr>Check<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Health Check block. Health Check blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Multi<wbr>Value<wbr>Headers<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancing<wbr>Algorithm<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `round_robin` or `least_outstanding_requests`. The default is `round_robin`.
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
The name of the target group. If omitted, this provider will assign a random, unique name.
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
Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proxy<wbr>Protocol<wbr>V2</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Slow<wbr>Start</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stickiness</td>
            <td class="align-top">
                
                <code><a href="#targetgroupstickiness">Pulumi.<wbr>Aws.<wbr>Alb.<wbr>Target<wbr>Group<wbr>Stickiness<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of target that you must specify when registering targets with this target group.
The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
The default is `instance`. Note that you can&#39;t specify targets for a target group using both instance IDs and IP addresses.
If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can&#39;t specify publicly routable IP addresses.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the VPC in which to create the target group. Required when `target_type` is `instance` or `ip`. Does not apply when `target_type` is `lambda`.
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
            <td class="align-top">Deregistration<wbr>Delay</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#targetgrouphealthcheck">*alb.<wbr>Target<wbr>Group<wbr>Health<wbr>Check</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Health Check block. Health Check blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Multi<wbr>Value<wbr>Headers<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancing<wbr>Algorithm<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `round_robin` or `least_outstanding_requests`. The default is `round_robin`.
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
The name of the target group. If omitted, this provider will assign a random, unique name.
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
Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proxy<wbr>Protocol<wbr>V2</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Slow<wbr>Start</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stickiness</td>
            <td class="align-top">
                
                <code><a href="#targetgroupstickiness">*alb.<wbr>Target<wbr>Group<wbr>Stickiness</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of target that you must specify when registering targets with this target group.
The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
The default is `instance`. Note that you can&#39;t specify targets for a target group using both instance IDs and IP addresses.
If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can&#39;t specify publicly routable IP addresses.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the VPC in which to create the target group. Required when `target_type` is `instance` or `ip`. Does not apply when `target_type` is `lambda`.
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
            <td class="align-top">deregistration<wbr>Delay</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#targetgrouphealthcheck">alb.<wbr>Target<wbr>Group<wbr>Health<wbr>Check?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Health Check block. Health Check blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Multi<wbr>Value<wbr>Headers<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load<wbr>Balancing<wbr>Algorithm<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `round_robin` or `least_outstanding_requests`. The default is `round_robin`.
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
The name of the target group. If omitted, this provider will assign a random, unique name.
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
Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proxy<wbr>Protocol<wbr>V2</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">slow<wbr>Start</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stickiness</td>
            <td class="align-top">
                
                <code><a href="#targetgroupstickiness">alb.<wbr>Target<wbr>Group<wbr>Stickiness?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of target that you must specify when registering targets with this target group.
The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
The default is `instance`. Note that you can&#39;t specify targets for a target group using both instance IDs and IP addresses.
If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can&#39;t specify publicly routable IP addresses.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the VPC in which to create the target group. Required when `target_type` is `instance` or `ip`. Does not apply when `target_type` is `lambda`.
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
            <td class="align-top">deregistration_<wbr>delay</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check</td>
            <td class="align-top">
                
                <code><a href="#targetgrouphealthcheck">Dict[Target<wbr>Group<wbr>Health<wbr>Check]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Health Check block. Health Check blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>multi_<wbr>value_<wbr>headers_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load_<wbr>balancing_<wbr>algorithm_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `round_robin` or `least_outstanding_requests`. The default is `round_robin`.
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
The name of the target group. If omitted, this provider will assign a random, unique name.
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
Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proxy_<wbr>protocol_<wbr>v2</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">slow_<wbr>start</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stickiness</td>
            <td class="align-top">
                
                <code><a href="#targetgroupstickiness">Dict[Target<wbr>Group<wbr>Stickiness]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of target that you must specify when registering targets with this target group.
The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
The default is `instance`. Note that you can&#39;t specify targets for a target group using both instance IDs and IP addresses.
If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can&#39;t specify publicly routable IP addresses.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the VPC in which to create the target group. Required when `target_type` is `instance` or `ip`. Does not apply when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## TargetGroup Output Properties

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
            <td class="align-top">{{% md %}} The ARN of the Target Group (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn<wbr>Suffix</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN suffix for use with CloudWatch Metrics.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deregistration<wbr>Delay</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#targetgrouphealthcheck">Pulumi.<wbr>Aws.<wbr>Alb.<wbr>Target<wbr>Group<wbr>Health<wbr>Check</a></code>
            </td>
            <td class="align-top">{{% md %}} A Health Check block. Health Check blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Multi<wbr>Value<wbr>Headers<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancing<wbr>Algorithm<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `round_robin` or `least_outstanding_requests`. The default is `round_robin`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the target group. If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proxy<wbr>Protocol<wbr>V2</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Slow<wbr>Start</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stickiness</td>
            <td class="align-top">
                
                <code><a href="#targetgroupstickiness">Pulumi.<wbr>Aws.<wbr>Alb.<wbr>Target<wbr>Group<wbr>Stickiness</a></code>
            </td>
            <td class="align-top">{{% md %}} A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The type of target that you must specify when registering targets with this target group.
The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
The default is `instance`. Note that you can&#39;t specify targets for a target group using both instance IDs and IP addresses.
If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can&#39;t specify publicly routable IP addresses.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The identifier of the VPC in which to create the target group. Required when `target_type` is `instance` or `ip`. Does not apply when `target_type` is `lambda`.
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
            <td class="align-top">{{% md %}} The ARN of the Target Group (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn<wbr>Suffix</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN suffix for use with CloudWatch Metrics.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deregistration<wbr>Delay</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#targetgrouphealthcheck">alb.<wbr>Target<wbr>Group<wbr>Health<wbr>Check</a></code>
            </td>
            <td class="align-top">{{% md %}} A Health Check block. Health Check blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Multi<wbr>Value<wbr>Headers<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancing<wbr>Algorithm<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `round_robin` or `least_outstanding_requests`. The default is `round_robin`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the target group. If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proxy<wbr>Protocol<wbr>V2</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Slow<wbr>Start</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stickiness</td>
            <td class="align-top">
                
                <code><a href="#targetgroupstickiness">alb.<wbr>Target<wbr>Group<wbr>Stickiness</a></code>
            </td>
            <td class="align-top">{{% md %}} A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The type of target that you must specify when registering targets with this target group.
The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
The default is `instance`. Note that you can&#39;t specify targets for a target group using both instance IDs and IP addresses.
If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can&#39;t specify publicly routable IP addresses.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The identifier of the VPC in which to create the target group. Required when `target_type` is `instance` or `ip`. Does not apply when `target_type` is `lambda`.
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
            <td class="align-top">{{% md %}} The ARN of the Target Group (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn<wbr>Suffix</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN suffix for use with CloudWatch Metrics.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deregistration<wbr>Delay</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#targetgrouphealthcheck">alb.<wbr>Target<wbr>Group<wbr>Health<wbr>Check</a></code>
            </td>
            <td class="align-top">{{% md %}} A Health Check block. Health Check blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Multi<wbr>Value<wbr>Headers<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load<wbr>Balancing<wbr>Algorithm<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `round_robin` or `least_outstanding_requests`. The default is `round_robin`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the target group. If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proxy<wbr>Protocol<wbr>V2</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">slow<wbr>Start</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stickiness</td>
            <td class="align-top">
                
                <code><a href="#targetgroupstickiness">alb.<wbr>Target<wbr>Group<wbr>Stickiness</a></code>
            </td>
            <td class="align-top">{{% md %}} A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The type of target that you must specify when registering targets with this target group.
The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
The default is `instance`. Note that you can&#39;t specify targets for a target group using both instance IDs and IP addresses.
If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can&#39;t specify publicly routable IP addresses.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The identifier of the VPC in which to create the target group. Required when `target_type` is `instance` or `ip`. Does not apply when `target_type` is `lambda`.
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
            <td class="align-top">{{% md %}} The ARN of the Target Group (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn_<wbr>suffix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN suffix for use with CloudWatch Metrics.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deregistration_<wbr>delay</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check</td>
            <td class="align-top">
                
                <code><a href="#targetgrouphealthcheck">Dict[Target<wbr>Group<wbr>Health<wbr>Check]</a></code>
            </td>
            <td class="align-top">{{% md %}} A Health Check block. Health Check blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>multi_<wbr>value_<wbr>headers_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load_<wbr>balancing_<wbr>algorithm_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `round_robin` or `least_outstanding_requests`. The default is `round_robin`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the target group. If omitted, this provider will assign a random, unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proxy_<wbr>protocol_<wbr>v2</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">slow_<wbr>start</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stickiness</td>
            <td class="align-top">
                
                <code><a href="#targetgroupstickiness">Dict[Target<wbr>Group<wbr>Stickiness]</a></code>
            </td>
            <td class="align-top">{{% md %}} A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of target that you must specify when registering targets with this target group.
The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
The default is `instance`. Note that you can&#39;t specify targets for a target group using both instance IDs and IP addresses.
If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can&#39;t specify publicly routable IP addresses.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The identifier of the VPC in which to create the target group. Required when `target_type` is `instance` or `ip`. Does not apply when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing TargetGroup Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/alb/#TargetGroupState">TargetGroupState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/alb/#TargetGroup">TargetGroup</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>arn_suffix=None<span class="p">, </span>deregistration_delay=None<span class="p">, </span>health_check=None<span class="p">, </span>lambda_multi_value_headers_enabled=None<span class="p">, </span>load_balancing_algorithm_type=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>port=None<span class="p">, </span>protocol=None<span class="p">, </span>proxy_protocol_v2=None<span class="p">, </span>slow_start=None<span class="p">, </span>stickiness=None<span class="p">, </span>tags=None<span class="p">, </span>target_type=None<span class="p">, </span>vpc_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetTargetGroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#TargetGroupState">TargetGroupState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#TargetGroup">TargetGroup</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.TargetGroup.html">TargetGroup</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.TargetGroupState.html">TargetGroupState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing TargetGroup resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The ARN of the Target Group (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn<wbr>Suffix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN suffix for use with CloudWatch Metrics.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deregistration<wbr>Delay</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#targetgrouphealthcheck">Pulumi.<wbr>Aws.<wbr>Alb.<wbr>Target<wbr>Group<wbr>Health<wbr>Check<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Health Check block. Health Check blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Multi<wbr>Value<wbr>Headers<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancing<wbr>Algorithm<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `round_robin` or `least_outstanding_requests`. The default is `round_robin`.
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
The name of the target group. If omitted, this provider will assign a random, unique name.
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
Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proxy<wbr>Protocol<wbr>V2</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Slow<wbr>Start</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stickiness</td>
            <td class="align-top">
                
                <code><a href="#targetgroupstickiness">Pulumi.<wbr>Aws.<wbr>Alb.<wbr>Target<wbr>Group<wbr>Stickiness<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of target that you must specify when registering targets with this target group.
The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
The default is `instance`. Note that you can&#39;t specify targets for a target group using both instance IDs and IP addresses.
If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can&#39;t specify publicly routable IP addresses.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the VPC in which to create the target group. Required when `target_type` is `instance` or `ip`. Does not apply when `target_type` is `lambda`.
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
The ARN of the Target Group (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn<wbr>Suffix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN suffix for use with CloudWatch Metrics.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deregistration<wbr>Delay</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#targetgrouphealthcheck">*alb.<wbr>Target<wbr>Group<wbr>Health<wbr>Check</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Health Check block. Health Check blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Multi<wbr>Value<wbr>Headers<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancing<wbr>Algorithm<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `round_robin` or `least_outstanding_requests`. The default is `round_robin`.
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
The name of the target group. If omitted, this provider will assign a random, unique name.
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
Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Proxy<wbr>Protocol<wbr>V2</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Slow<wbr>Start</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stickiness</td>
            <td class="align-top">
                
                <code><a href="#targetgroupstickiness">*alb.<wbr>Target<wbr>Group<wbr>Stickiness</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of target that you must specify when registering targets with this target group.
The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
The default is `instance`. Note that you can&#39;t specify targets for a target group using both instance IDs and IP addresses.
If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can&#39;t specify publicly routable IP addresses.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the VPC in which to create the target group. Required when `target_type` is `instance` or `ip`. Does not apply when `target_type` is `lambda`.
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
The ARN of the Target Group (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn<wbr>Suffix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN suffix for use with CloudWatch Metrics.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deregistration<wbr>Delay</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#targetgrouphealthcheck">alb.<wbr>Target<wbr>Group<wbr>Health<wbr>Check?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Health Check block. Health Check blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Multi<wbr>Value<wbr>Headers<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load<wbr>Balancing<wbr>Algorithm<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `round_robin` or `least_outstanding_requests`. The default is `round_robin`.
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
The name of the target group. If omitted, this provider will assign a random, unique name.
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
Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proxy<wbr>Protocol<wbr>V2</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">slow<wbr>Start</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stickiness</td>
            <td class="align-top">
                
                <code><a href="#targetgroupstickiness">alb.<wbr>Target<wbr>Group<wbr>Stickiness?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of target that you must specify when registering targets with this target group.
The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
The default is `instance`. Note that you can&#39;t specify targets for a target group using both instance IDs and IP addresses.
If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can&#39;t specify publicly routable IP addresses.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the VPC in which to create the target group. Required when `target_type` is `instance` or `ip`. Does not apply when `target_type` is `lambda`.
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
The ARN of the Target Group (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn_<wbr>suffix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN suffix for use with CloudWatch Metrics.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deregistration_<wbr>delay</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. The default value is 300 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check</td>
            <td class="align-top">
                
                <code><a href="#targetgrouphealthcheck">Dict[Target<wbr>Group<wbr>Health<wbr>Check]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Health Check block. Health Check blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>multi_<wbr>value_<wbr>headers_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean whether the request and response headers exchanged between the load balancer and the Lambda function include arrays of values or strings. Only applies when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load_<wbr>balancing_<wbr>algorithm_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Determines how the load balancer selects targets when routing requests. Only applicable for Application Load Balancer Target Groups. The value is `round_robin` or `least_outstanding_requests`. The default is `round_robin`.
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
The name of the target group. If omitted, this provider will assign a random, unique name.
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
Creates a unique name beginning with the specified prefix. Conflicts with `name`. Cannot be longer than 6 characters.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">proxy_<wbr>protocol_<wbr>v2</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable / disable support for proxy protocol v2 on Network Load Balancers. See [doc](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">slow_<wbr>start</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount time for targets to warm up before the load balancer sends them a full share of requests. The range is 30-900 seconds or 0 to disable. The default value is 0 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stickiness</td>
            <td class="align-top">
                
                <code><a href="#targetgroupstickiness">Dict[Target<wbr>Group<wbr>Stickiness]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Stickiness block. Stickiness blocks are documented below. `stickiness` is only valid if used with Load Balancers of type `Application`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of target that you must specify when registering targets with this target group.
The possible values are `instance` (targets are specified by instance ID) or `ip` (targets are specified by IP address) or `lambda` (targets are specified by lambda arn).
The default is `instance`. Note that you can&#39;t specify targets for a target group using both instance IDs and IP addresses.
If the target type is `ip`, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group,
the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10).
You can&#39;t specify publicly routable IP addresses.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The identifier of the VPC in which to create the target group. Required when `target_type` is `instance` or `ip`. Does not apply when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### TargetGroupHealthCheck
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TargetGroupHealthCheck">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TargetGroupHealthCheck">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#TargetGroupHealthCheckArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#TargetGroupHealthCheckOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.TargetGroupHealthCheckArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.TargetGroupHealthCheck.html">output</a> API doc for this type.
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
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether  health checks are enabled. Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Healthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of consecutive health checks successes required before considering an unhealthy target healthy. Defaults to 3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Interval</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The approximate amount of time, in seconds, between health checks of an individual target. Minimum value 5 seconds, Maximum value 300 seconds. For `lambda` target groups, it needs to be greater as the `timeout` of the underlying `lambda`. Default 30 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Matcher</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The destination for the health check request. Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, during which no response means a failed health check. For Application Load Balancers, the range is 2 to 120 seconds, and the default is 5 seconds for the `instance` target type and 30 seconds for the `lambda` target type. For Network Load Balancers, you cannot set a custom value, and the default is 10 seconds for TCP and HTTPS health checks and 6 seconds for HTTP health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Unhealthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of consecutive health check failures required before considering the target unhealthy . For Network Load Balancers, this value must be the same as the `healthy_threshold`. Defaults to 3.
* `matcher` (Required for HTTP/HTTPS ALB) The HTTP codes to use when checking for a successful response from a target. You can specify multiple values (for example, &#34;200,202&#34;) or a range of values (for example, &#34;200-299&#34;). Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).
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
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether  health checks are enabled. Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Healthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of consecutive health checks successes required before considering an unhealthy target healthy. Defaults to 3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Interval</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The approximate amount of time, in seconds, between health checks of an individual target. Minimum value 5 seconds, Maximum value 300 seconds. For `lambda` target groups, it needs to be greater as the `timeout` of the underlying `lambda`. Default 30 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Matcher</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Path</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The destination for the health check request. Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, during which no response means a failed health check. For Application Load Balancers, the range is 2 to 120 seconds, and the default is 5 seconds for the `instance` target type and 30 seconds for the `lambda` target type. For Network Load Balancers, you cannot set a custom value, and the default is 10 seconds for TCP and HTTPS health checks and 6 seconds for HTTP health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Unhealthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of consecutive health check failures required before considering the target unhealthy . For Network Load Balancers, this value must be the same as the `healthy_threshold`. Defaults to 3.
* `matcher` (Required for HTTP/HTTPS ALB) The HTTP codes to use when checking for a successful response from a target. You can specify multiple values (for example, &#34;200,202&#34;) or a range of values (for example, &#34;200-299&#34;). Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).
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
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether  health checks are enabled. Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">healthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of consecutive health checks successes required before considering an unhealthy target healthy. Defaults to 3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">interval</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The approximate amount of time, in seconds, between health checks of an individual target. Minimum value 5 seconds, Maximum value 300 seconds. For `lambda` target groups, it needs to be greater as the `timeout` of the underlying `lambda`. Default 30 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">matcher</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The destination for the health check request. Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, during which no response means a failed health check. For Application Load Balancers, the range is 2 to 120 seconds, and the default is 5 seconds for the `instance` target type and 30 seconds for the `lambda` target type. For Network Load Balancers, you cannot set a custom value, and the default is 10 seconds for TCP and HTTPS health checks and 6 seconds for HTTP health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">unhealthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of consecutive health check failures required before considering the target unhealthy . For Network Load Balancers, this value must be the same as the `healthy_threshold`. Defaults to 3.
* `matcher` (Required for HTTP/HTTPS ALB) The HTTP codes to use when checking for a successful response from a target. You can specify multiple values (for example, &#34;200,202&#34;) or a range of values (for example, &#34;200-299&#34;). Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).
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
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether  health checks are enabled. Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">healthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of consecutive health checks successes required before considering an unhealthy target healthy. Defaults to 3.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">interval</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The approximate amount of time, in seconds, between health checks of an individual target. Minimum value 5 seconds, Maximum value 300 seconds. For `lambda` target groups, it needs to be greater as the `timeout` of the underlying `lambda`. Default 30 seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">matcher</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The destination for the health check request. Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port to use to connect with the target. Valid values are either ports 1-65535, or `traffic-port`. Defaults to `traffic-port`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol to use to connect with the target. Defaults to `HTTP`. Not applicable when `target_type` is `lambda`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The amount of time, in seconds, during which no response means a failed health check. For Application Load Balancers, the range is 2 to 120 seconds, and the default is 5 seconds for the `instance` target type and 30 seconds for the `lambda` target type. For Network Load Balancers, you cannot set a custom value, and the default is 10 seconds for TCP and HTTPS health checks and 6 seconds for HTTP health checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">unhealthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of consecutive health check failures required before considering the target unhealthy . For Network Load Balancers, this value must be the same as the `healthy_threshold`. Defaults to 3.
* `matcher` (Required for HTTP/HTTPS ALB) The HTTP codes to use when checking for a successful response from a target. You can specify multiple values (for example, &#34;200,202&#34;) or a range of values (for example, &#34;200-299&#34;). Applies to Application Load Balancers only (HTTP/HTTPS), not Network Load Balancers (TCP).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TargetGroupStickiness
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TargetGroupStickiness">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TargetGroupStickiness">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#TargetGroupStickinessArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#TargetGroupStickinessOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.TargetGroupStickinessArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.TargetGroupStickiness.html">output</a> API doc for this type.
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
            <td class="align-top">Cookie<wbr>Duration</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether  health checks are enabled. Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of sticky sessions. The only current possible value is `lb_cookie`.
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
            <td class="align-top">Cookie<wbr>Duration</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether  health checks are enabled. Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of sticky sessions. The only current possible value is `lb_cookie`.
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
            <td class="align-top">cookie<wbr>Duration</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether  health checks are enabled. Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of sticky sessions. The only current possible value is `lb_cookie`.
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
            <td class="align-top">cookie<wbr>Duration</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether  health checks are enabled. Defaults to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of sticky sessions. The only current possible value is `lb_cookie`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







