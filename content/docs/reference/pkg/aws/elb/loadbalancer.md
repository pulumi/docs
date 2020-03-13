
---
title: "LoadBalancer"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an Elastic Load Balancer resource, also known as a "Classic
Load Balancer" after the release of
[Application/Network Load Balancers](https://www.terraform.io/docs/providers/aws/r/lb.html).

> **NOTE on ELB Instances and ELB Attachments:** This provider currently
provides both a standalone ELB Attachment resource
(describing an instance attached to an ELB), and an ELB resource with
`instances` defined in-line. At this time you cannot use an ELB with in-line
instances in conjunction with a ELB Attachment resources. Doing so will cause a
conflict and will overwrite attachments.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create a new load balancer
const bar = new aws.elb.LoadBalancer("bar", {
    accessLogs: {
        bucket: "foo",
        bucketPrefix: "bar",
        interval: 60,
    },
    availabilityZones: [
        "us-west-2a",
        "us-west-2b",
        "us-west-2c",
    ],
    connectionDraining: true,
    connectionDrainingTimeout: 400,
    crossZoneLoadBalancing: true,
    healthCheck: {
        healthyThreshold: 2,
        interval: 30,
        target: "HTTP:8000/",
        timeout: 3,
        unhealthyThreshold: 2,
    },
    idleTimeout: 400,
    instances: [aws_instance_foo.id],
    listeners: [
        {
            instancePort: 8000,
            instanceProtocol: "http",
            lbPort: 80,
            lbProtocol: "http",
        },
        {
            instancePort: 8000,
            instanceProtocol: "http",
            lbPort: 443,
            lbProtocol: "https",
            sslCertificateId: "arn:aws:iam::123456789012:server-certificate/certName",
        },
    ],
    tags: {
        Name: "foobar-elb",
    },
});
```

## Note on ECDSA Key Algorithm

If the ARN of the `ssl_certificate_id` that is pointed to references a
certificate that was signed by an ECDSA key, note that ELB only supports the
P256 and P384 curves.  Using a certificate signed by a key using a different
curve could produce the error `ERR_SSL_VERSION_OR_CIPHER_MISMATCH` in your
browser.

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elb.html.markdown.



## Create a LoadBalancer Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elb/#LoadBalancer">LoadBalancer</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elb/#LoadBalancerArgs">LoadBalancerArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">LoadBalancer</span><span class="p">(resource_name, id, opts=None, </span>access_logs=None<span class="p">, </span>availability_zones=None<span class="p">, </span>connection_draining=None<span class="p">, </span>connection_draining_timeout=None<span class="p">, </span>cross_zone_load_balancing=None<span class="p">, </span>health_check=None<span class="p">, </span>idle_timeout=None<span class="p">, </span>instances=None<span class="p">, </span>internal=None<span class="p">, </span>listeners=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>security_groups=None<span class="p">, </span>source_security_group=None<span class="p">, </span>subnets=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewLoadBalancer<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elb?tab=doc#LoadBalancerArgs">LoadBalancerArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elb?tab=doc#LoadBalancer">LoadBalancer</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elb.LoadBalancer.html">LoadBalancer</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elb.LoadBalancerArgs.html">LoadBalancerArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a LoadBalancer resource with the given unique name, arguments, and options.

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
            <td class="align-top">Access<wbr>Logs</td>
            <td class="align-top">
                
                <code><a href="#loadbalanceraccesslogs">Pulumi.<wbr>Aws.<wbr>Elb.<wbr>Load<wbr>Balancer<wbr>Access<wbr>Logs<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Access Logs block. Access Logs documented below.
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
The AZ&#39;s to serve traffic in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Draining</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable connection draining. Default: `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Draining<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds to allow for connections to drain. Default: `300`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cross<wbr>Zone<wbr>Load<wbr>Balancing</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable cross-zone load balancing. Default: `true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerhealthcheck">Pulumi.<wbr>Aws.<wbr>Elb.<wbr>Load<wbr>Balancer<wbr>Health<wbr>Check<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A health_check block. Health Check documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Idle<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds that the connection is allowed to be idle. Default: `60`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instances</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of instance ids to place in the ELB pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Internal</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, ELB will be an internal ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Listeners</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerlistener">List&lt;Pulumi.<wbr>Aws.<wbr>Elb.<wbr>Load<wbr>Balancer<wbr>Listener<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of listener blocks. Listeners documented below.
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
The name of the ELB. By default generated by this provider.
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
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to assign to the ELB.
Only valid if creating an ELB within a VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Security<wbr>Group</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Use this for Classic or Default VPC only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnets</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to attach to the ELB.
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
            <td class="align-top">Access<wbr>Logs</td>
            <td class="align-top">
                
                <code><a href="#loadbalanceraccesslogs">*elb.<wbr>Load<wbr>Balancer<wbr>Access<wbr>Logs</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Access Logs block. Access Logs documented below.
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
The AZ&#39;s to serve traffic in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Draining</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable connection draining. Default: `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Draining<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds to allow for connections to drain. Default: `300`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cross<wbr>Zone<wbr>Load<wbr>Balancing</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable cross-zone load balancing. Default: `true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerhealthcheck">*elb.<wbr>Load<wbr>Balancer<wbr>Health<wbr>Check</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A health_check block. Health Check documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Idle<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds that the connection is allowed to be idle. Default: `60`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instances</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of instance ids to place in the ELB pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Internal</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, ELB will be an internal ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Listeners</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerlistener">[]elb.<wbr>Load<wbr>Balancer<wbr>Listener</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of listener blocks. Listeners documented below.
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
The name of the ELB. By default generated by this provider.
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
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to assign to the ELB.
Only valid if creating an ELB within a VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Security<wbr>Group</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Use this for Classic or Default VPC only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnets</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to attach to the ELB.
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
            <td class="align-top">access<wbr>Logs</td>
            <td class="align-top">
                
                <code><a href="#loadbalanceraccesslogs">elb.<wbr>Load<wbr>Balancer<wbr>Access<wbr>Logs?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Access Logs block. Access Logs documented below.
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
The AZ&#39;s to serve traffic in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection<wbr>Draining</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable connection draining. Default: `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection<wbr>Draining<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds to allow for connections to drain. Default: `300`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cross<wbr>Zone<wbr>Load<wbr>Balancing</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable cross-zone load balancing. Default: `true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerhealthcheck">elb.<wbr>Load<wbr>Balancer<wbr>Health<wbr>Check?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A health_check block. Health Check documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">idle<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds that the connection is allowed to be idle. Default: `60`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instances</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of instance ids to place in the ELB pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">internal</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, ELB will be an internal ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">listeners</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerlistener">elb.<wbr>Load<wbr>Balancer<wbr>Listener[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of listener blocks. Listeners documented below.
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
The name of the ELB. By default generated by this provider.
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
            <td class="align-top">security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to assign to the ELB.
Only valid if creating an ELB within a VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Security<wbr>Group</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Use this for Classic or Default VPC only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnets</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to attach to the ELB.
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
            <td class="align-top">access_<wbr>logs</td>
            <td class="align-top">
                
                <code><a href="#loadbalanceraccesslogs">dict{load_<wbr>balancer_<wbr>access_<wbr>logs}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Access Logs block. Access Logs documented below.
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
The AZ&#39;s to serve traffic in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection_<wbr>draining</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable connection draining. Default: `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection_<wbr>draining_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds to allow for connections to drain. Default: `300`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cross_<wbr>zone_<wbr>load_<wbr>balancing</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable cross-zone load balancing. Default: `true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerhealthcheck">dict{load_<wbr>balancer_<wbr>health_<wbr>check}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A health_check block. Health Check documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">idle_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds that the connection is allowed to be idle. Default: `60`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instances</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of instance ids to place in the ELB pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">internal</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, ELB will be an internal ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">listeners</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerlistener">list[load_<wbr>balancer_<wbr>listener]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of listener blocks. Listeners documented below.
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
The name of the ELB. By default generated by this provider.
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
            <td class="align-top">security_<wbr>groups</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to assign to the ELB.
Only valid if creating an ELB within a VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>security_<wbr>group</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Use this for Classic or Default VPC only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnets</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to attach to the ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## LoadBalancer Output Properties

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
            <td class="align-top">Access<wbr>Logs</td>
            <td class="align-top">
                
                <code><a href="#loadbalanceraccesslogs">Pulumi.<wbr>Aws.<wbr>Elb.<wbr>Load<wbr>Balancer<wbr>Access<wbr>Logs?</a></code>
            </td>
            <td class="align-top">{{% md %}} An Access Logs block. Access Logs documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the ELB
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} The AZ&#39;s to serve traffic in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Draining</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Boolean to enable connection draining. Default: `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Draining<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The time in seconds to allow for connections to drain. Default: `300`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cross<wbr>Zone<wbr>Load<wbr>Balancing</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Enable cross-zone load balancing. Default: `true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS name of the ELB
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerhealthcheck">Pulumi.<wbr>Aws.<wbr>Elb.<wbr>Load<wbr>Balancer<wbr>Health<wbr>Check</a></code>
            </td>
            <td class="align-top">{{% md %}} A health_check block. Health Check documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Idle<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The time in seconds that the connection is allowed to be idle. Default: `60`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instances</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} A list of instance ids to place in the ELB pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Internal</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, ELB will be an internal ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Listeners</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerlistener">List&lt;Pulumi.<wbr>Aws.<wbr>Elb.<wbr>Load<wbr>Balancer<wbr>Listener&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of listener blocks. Listeners documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the ELB. By default generated by this provider.
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
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} A list of security group IDs to assign to the ELB.
Only valid if creating an ELB within a VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Security<wbr>Group</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Use this for Classic or Default VPC only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Only available on ELBs launched in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnets</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} A list of subnet IDs to attach to the ELB.
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
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record)
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
            <td class="align-top">Access<wbr>Logs</td>
            <td class="align-top">
                
                <code><a href="#loadbalanceraccesslogs">*elb.<wbr>Load<wbr>Balancer<wbr>Access<wbr>Logs</a></code>
            </td>
            <td class="align-top">{{% md %}} An Access Logs block. Access Logs documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the ELB
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} The AZ&#39;s to serve traffic in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Draining</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Boolean to enable connection draining. Default: `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Draining<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The time in seconds to allow for connections to drain. Default: `300`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cross<wbr>Zone<wbr>Load<wbr>Balancing</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Enable cross-zone load balancing. Default: `true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS name of the ELB
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerhealthcheck">elb.<wbr>Load<wbr>Balancer<wbr>Health<wbr>Check</a></code>
            </td>
            <td class="align-top">{{% md %}} A health_check block. Health Check documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Idle<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The time in seconds that the connection is allowed to be idle. Default: `60`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instances</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of instance ids to place in the ELB pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Internal</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, ELB will be an internal ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Listeners</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerlistener">[]elb.<wbr>Load<wbr>Balancer<wbr>Listener</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of listener blocks. Listeners documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the ELB. By default generated by this provider.
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
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of security group IDs to assign to the ELB.
Only valid if creating an ELB within a VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Security<wbr>Group</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Use this for Classic or Default VPC only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Only available on ELBs launched in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnets</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of subnet IDs to attach to the ELB.
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
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record)
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
            <td class="align-top">access<wbr>Logs</td>
            <td class="align-top">
                
                <code><a href="#loadbalanceraccesslogs">elb.<wbr>Load<wbr>Balancer<wbr>Access<wbr>Logs?</a></code>
            </td>
            <td class="align-top">{{% md %}} An Access Logs block. Access Logs documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the ELB
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} The AZ&#39;s to serve traffic in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection<wbr>Draining</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Boolean to enable connection draining. Default: `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection<wbr>Draining<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The time in seconds to allow for connections to drain. Default: `300`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cross<wbr>Zone<wbr>Load<wbr>Balancing</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Enable cross-zone load balancing. Default: `true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS name of the ELB
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerhealthcheck">elb.<wbr>Load<wbr>Balancer<wbr>Health<wbr>Check</a></code>
            </td>
            <td class="align-top">{{% md %}} A health_check block. Health Check documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">idle<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The time in seconds that the connection is allowed to be idle. Default: `60`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instances</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} A list of instance ids to place in the ELB pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">internal</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} If true, ELB will be an internal ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">listeners</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerlistener">elb.<wbr>Load<wbr>Balancer<wbr>Listener[]</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of listener blocks. Listeners documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the ELB. By default generated by this provider.
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
            <td class="align-top">security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} A list of security group IDs to assign to the ELB.
Only valid if creating an ELB within a VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Security<wbr>Group</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Use this for Classic or Default VPC only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Only available on ELBs launched in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnets</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} A list of subnet IDs to attach to the ELB.
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
            <td class="align-top">zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record)
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
            <td class="align-top">access_<wbr>logs</td>
            <td class="align-top">
                
                <code><a href="#loadbalanceraccesslogs">dict{load_<wbr>balancer_<wbr>access_<wbr>logs}</a></code>
            </td>
            <td class="align-top">{{% md %}} An Access Logs block. Access Logs documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the ELB
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} The AZ&#39;s to serve traffic in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection_<wbr>draining</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Boolean to enable connection draining. Default: `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection_<wbr>draining_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The time in seconds to allow for connections to drain. Default: `300`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cross_<wbr>zone_<wbr>load_<wbr>balancing</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Enable cross-zone load balancing. Default: `true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The DNS name of the ELB
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerhealthcheck">dict{load_<wbr>balancer_<wbr>health_<wbr>check}</a></code>
            </td>
            <td class="align-top">{{% md %}} A health_check block. Health Check documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">idle_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The time in seconds that the connection is allowed to be idle. Default: `60`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instances</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A list of instance ids to place in the ELB pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">internal</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, ELB will be an internal ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">listeners</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerlistener">list[load_<wbr>balancer_<wbr>listener]</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of listener blocks. Listeners documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the ELB. By default generated by this provider.
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
            <td class="align-top">security_<wbr>groups</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A list of security group IDs to assign to the ELB.
Only valid if creating an ELB within a VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>security_<wbr>group</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Use this for Classic or Default VPC only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>security_<wbr>group_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Only available on ELBs launched in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnets</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} A list of subnet IDs to attach to the ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing LoadBalancer Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LoadBalancerState, opts?: pulumi.CustomResourceOptions): LoadBalancer;
```

```python
def get(resource_name, id, opts=None, access_<wbr>logs=None, arn=None, availability_<wbr>zones=None, connection_<wbr>draining=None, connection_<wbr>draining_<wbr>timeout=None, cross_<wbr>zone_<wbr>load_<wbr>balancing=None, dns_<wbr>name=None, health_<wbr>check=None, idle_<wbr>timeout=None, instances=None, internal=None, listeners=None, name=None, name_<wbr>prefix=None, security_<wbr>groups=None, source_<wbr>security_<wbr>group=None, source_<wbr>security_<wbr>group_<wbr>id=None, subnets=None, tags=None, zone_<wbr>id=None)
```

```go
func GetLoadBalancer(ctx *pulumi.Context, name string, id pulumi.IDInput, state *LoadBalancerState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static LoadBalancer Get(string name, Input<string> id, LoadBalancerState? state = null, CustomResourceOptions? options = null);
```

Get an existing LoadBalancer resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Access<wbr>Logs</td>
            <td class="align-top">
                
                <code><a href="#loadbalanceraccesslogs">Pulumi.<wbr>Aws.<wbr>Elb.<wbr>Load<wbr>Balancer<wbr>Access<wbr>Logs<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Access Logs block. Access Logs documented below.
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
The ARN of the ELB
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
The AZ&#39;s to serve traffic in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Draining</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable connection draining. Default: `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Draining<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds to allow for connections to drain. Default: `300`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cross<wbr>Zone<wbr>Load<wbr>Balancing</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable cross-zone load balancing. Default: `true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS name of the ELB
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerhealthcheck">Pulumi.<wbr>Aws.<wbr>Elb.<wbr>Load<wbr>Balancer<wbr>Health<wbr>Check<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A health_check block. Health Check documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Idle<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds that the connection is allowed to be idle. Default: `60`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instances</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of instance ids to place in the ELB pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Internal</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, ELB will be an internal ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Listeners</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerlistener">List&lt;Pulumi.<wbr>Aws.<wbr>Elb.<wbr>Load<wbr>Balancer<wbr>Listener<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of listener blocks. Listeners documented below.
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
The name of the ELB. By default generated by this provider.
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
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to assign to the ELB.
Only valid if creating an ELB within a VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Security<wbr>Group</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Use this for Classic or Default VPC only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Only available on ELBs launched in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnets</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to attach to the ELB.
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
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record)
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
            <td class="align-top">Access<wbr>Logs</td>
            <td class="align-top">
                
                <code><a href="#loadbalanceraccesslogs">*elb.<wbr>Load<wbr>Balancer<wbr>Access<wbr>Logs</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Access Logs block. Access Logs documented below.
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
The ARN of the ELB
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
The AZ&#39;s to serve traffic in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Draining</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable connection draining. Default: `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Draining<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds to allow for connections to drain. Default: `300`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cross<wbr>Zone<wbr>Load<wbr>Balancing</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable cross-zone load balancing. Default: `true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS name of the ELB
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerhealthcheck">*elb.<wbr>Load<wbr>Balancer<wbr>Health<wbr>Check</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A health_check block. Health Check documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Idle<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds that the connection is allowed to be idle. Default: `60`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instances</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of instance ids to place in the ELB pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Internal</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, ELB will be an internal ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Listeners</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerlistener">[]elb.<wbr>Load<wbr>Balancer<wbr>Listener</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of listener blocks. Listeners documented below.
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
The name of the ELB. By default generated by this provider.
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
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to assign to the ELB.
Only valid if creating an ELB within a VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Security<wbr>Group</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Use this for Classic or Default VPC only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Only available on ELBs launched in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnets</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to attach to the ELB.
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
            <td class="align-top">Zone<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record)
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
            <td class="align-top">access<wbr>Logs</td>
            <td class="align-top">
                
                <code><a href="#loadbalanceraccesslogs">elb.<wbr>Load<wbr>Balancer<wbr>Access<wbr>Logs?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Access Logs block. Access Logs documented below.
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
The ARN of the ELB
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
The AZ&#39;s to serve traffic in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection<wbr>Draining</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable connection draining. Default: `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection<wbr>Draining<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds to allow for connections to drain. Default: `300`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cross<wbr>Zone<wbr>Load<wbr>Balancing</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable cross-zone load balancing. Default: `true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS name of the ELB
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health<wbr>Check</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerhealthcheck">elb.<wbr>Load<wbr>Balancer<wbr>Health<wbr>Check?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A health_check block. Health Check documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">idle<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds that the connection is allowed to be idle. Default: `60`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instances</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of instance ids to place in the ELB pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">internal</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, ELB will be an internal ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">listeners</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerlistener">elb.<wbr>Load<wbr>Balancer<wbr>Listener[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of listener blocks. Listeners documented below.
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
The name of the ELB. By default generated by this provider.
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
            <td class="align-top">security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to assign to the ELB.
Only valid if creating an ELB within a VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Security<wbr>Group</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Use this for Classic or Default VPC only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Only available on ELBs launched in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnets</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to attach to the ELB.
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
            <td class="align-top">zone<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record)
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
            <td class="align-top">access_<wbr>logs</td>
            <td class="align-top">
                
                <code><a href="#loadbalanceraccesslogs">dict{load_<wbr>balancer_<wbr>access_<wbr>logs}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Access Logs block. Access Logs documented below.
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
The ARN of the ELB
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
The AZ&#39;s to serve traffic in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection_<wbr>draining</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable connection draining. Default: `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection_<wbr>draining_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds to allow for connections to drain. Default: `300`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cross_<wbr>zone_<wbr>load_<wbr>balancing</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enable cross-zone load balancing. Default: `true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS name of the ELB
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">health_<wbr>check</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerhealthcheck">dict{load_<wbr>balancer_<wbr>health_<wbr>check}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A health_check block. Health Check documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">idle_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time in seconds that the connection is allowed to be idle. Default: `60`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instances</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of instance ids to place in the ELB pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">internal</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, ELB will be an internal ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">listeners</td>
            <td class="align-top">
                
                <code><a href="#loadbalancerlistener">list[load_<wbr>balancer_<wbr>listener]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of listener blocks. Listeners documented below.
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
The name of the ELB. By default generated by this provider.
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
            <td class="align-top">security_<wbr>groups</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to assign to the ELB.
Only valid if creating an ELB within a VPC
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>security_<wbr>group</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Use this for Classic or Default VPC only.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source_<wbr>security_<wbr>group_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the security group that you can use as
part of your inbound rules for your load balancer&#39;s back-end application
instances. Only available on ELBs launched in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnets</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of subnet IDs to attach to the ELB.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">zone_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The canonical hosted zone ID of the ELB (to be used in a Route 53 Alias record)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### LoadBalancerAccessLogs
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LoadBalancerAccessLogs">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LoadBalancerAccessLogs">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elb?tab=doc#LoadBalancerAccessLogsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elb?tab=doc#LoadBalancerAccessLogsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elb.LoadBalancerAccessLogsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elb.LoadBalancerAccessLogs.html">output</a> API doc for this type.
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
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The S3 bucket name to store the logs in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 bucket prefix. Logs are stored in the root if not configured.
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
Boolean to enable / disable `access_logs`. Default is `true`
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
The interval between checks.
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
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The S3 bucket name to store the logs in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 bucket prefix. Logs are stored in the root if not configured.
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
Boolean to enable / disable `access_logs`. Default is `true`
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
The interval between checks.
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
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The S3 bucket name to store the logs in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 bucket prefix. Logs are stored in the root if not configured.
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
Boolean to enable / disable `access_logs`. Default is `true`
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
The interval between checks.
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
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The S3 bucket name to store the logs in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The S3 bucket prefix. Logs are stored in the root if not configured.
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
Boolean to enable / disable `access_logs`. Default is `true`
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
The interval between checks.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LoadBalancerHealthCheck
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LoadBalancerHealthCheck">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LoadBalancerHealthCheck">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elb?tab=doc#LoadBalancerHealthCheckArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elb?tab=doc#LoadBalancerHealthCheckOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elb.LoadBalancerHealthCheckArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elb.LoadBalancerHealthCheck.html">output</a> API doc for this type.
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
            <td class="align-top">Healthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of checks before the instance is declared healthy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Interval</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The interval between checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The target of the check. Valid pattern is &#34;${PROTOCOL}:${PORT}${PATH}&#34;, where PROTOCOL
values are:
* `HTTP`, `HTTPS` - PORT and PATH are required
* `TCP`, `SSL` - PORT is required, PATH is not supported
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The length of time before the check times out.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Unhealthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of checks before the instance is declared unhealthy.
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
            <td class="align-top">Healthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of checks before the instance is declared healthy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Interval</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The interval between checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The target of the check. Valid pattern is &#34;${PROTOCOL}:${PORT}${PATH}&#34;, where PROTOCOL
values are:
* `HTTP`, `HTTPS` - PORT and PATH are required
* `TCP`, `SSL` - PORT is required, PATH is not supported
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Timeout</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The length of time before the check times out.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Unhealthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of checks before the instance is declared unhealthy.
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
            <td class="align-top">healthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of checks before the instance is declared healthy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">interval</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The interval between checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The target of the check. Valid pattern is &#34;${PROTOCOL}:${PORT}${PATH}&#34;, where PROTOCOL
values are:
* `HTTP`, `HTTPS` - PORT and PATH are required
* `TCP`, `SSL` - PORT is required, PATH is not supported
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The length of time before the check times out.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">unhealthy<wbr>Threshold</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of checks before the instance is declared unhealthy.
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
            <td class="align-top">healthy_<wbr>threshold</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of checks before the instance is declared healthy.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">interval</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The interval between checks.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The target of the check. Valid pattern is &#34;${PROTOCOL}:${PORT}${PATH}&#34;, where PROTOCOL
values are:
* `HTTP`, `HTTPS` - PORT and PATH are required
* `TCP`, `SSL` - PORT is required, PATH is not supported
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The length of time before the check times out.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">unhealthy_<wbr>threshold</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of checks before the instance is declared unhealthy.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LoadBalancerListener
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LoadBalancerListener">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LoadBalancerListener">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elb?tab=doc#LoadBalancerListenerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elb?tab=doc#LoadBalancerListenerOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elb.LoadBalancerListenerArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elb.LoadBalancerListener.html">output</a> API doc for this type.
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
            <td class="align-top">Instance<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The port on the instance to route to
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol to use to the instance. Valid
values are `HTTP`, `HTTPS`, `TCP`, or `SSL`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lb<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The port to listen on for the load balancer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lb<wbr>Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol to listen on. Valid values are `HTTP`,
`HTTPS`, `TCP`, or `SSL`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ssl<wbr>Certificate<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SSL certificate you have
uploaded to AWS IAM. **Note ECDSA-specific restrictions below.  Only valid when `lb_protocol` is either HTTPS or SSL**
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
            <td class="align-top">Instance<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The port on the instance to route to
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol to use to the instance. Valid
values are `HTTP`, `HTTPS`, `TCP`, or `SSL`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lb<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The port to listen on for the load balancer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lb<wbr>Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol to listen on. Valid values are `HTTP`,
`HTTPS`, `TCP`, or `SSL`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ssl<wbr>Certificate<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SSL certificate you have
uploaded to AWS IAM. **Note ECDSA-specific restrictions below.  Only valid when `lb_protocol` is either HTTPS or SSL**
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
            <td class="align-top">instance<wbr>Port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The port on the instance to route to
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol to use to the instance. Valid
values are `HTTP`, `HTTPS`, `TCP`, or `SSL`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lb<wbr>Port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The port to listen on for the load balancer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lb<wbr>Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol to listen on. Valid values are `HTTP`,
`HTTPS`, `TCP`, or `SSL`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ssl<wbr>Certificate<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SSL certificate you have
uploaded to AWS IAM. **Note ECDSA-specific restrictions below.  Only valid when `lb_protocol` is either HTTPS or SSL**
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
            <td class="align-top">instance_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The port on the instance to route to
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol to use to the instance. Valid
values are `HTTP`, `HTTPS`, `TCP`, or `SSL`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lb_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The port to listen on for the load balancer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lb_<wbr>protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The protocol to listen on. Valid values are `HTTP`,
`HTTPS`, `TCP`, or `SSL`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ssl_<wbr>certificate_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an SSL certificate you have
uploaded to AWS IAM. **Note ECDSA-specific restrictions below.  Only valid when `lb_protocol` is either HTTPS or SSL**
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







