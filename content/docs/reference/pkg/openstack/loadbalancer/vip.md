
---
title: "Vip"
block_external_search_index: true
---



Manages a V1 load balancer vip resource within OpenStack.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as openstack from "@pulumi/openstack";

const vip1 = new openstack.loadbalancer.Vip("vip_1", {
    poolId: "67890",
    port: 80,
    protocol: "HTTP",
    subnetId: "12345",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/lb_vip_v1.html.markdown.



## Create a Vip Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/loadbalancer/#Vip">Vip</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/loadbalancer/#VipArgs">VipArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Vip</span><span class="p">(resource_name, opts=None, </span>address=None<span class="p">, </span>admin_state_up=None<span class="p">, </span>conn_limit=None<span class="p">, </span>description=None<span class="p">, </span>floating_ip=None<span class="p">, </span>name=None<span class="p">, </span>persistence=None<span class="p">, </span>pool_id=None<span class="p">, </span>port=None<span class="p">, </span>protocol=None<span class="p">, </span>region=None<span class="p">, </span>subnet_id=None<span class="p">, </span>tenant_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewVip<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/loadbalancer?tab=doc#VipArgs">VipArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/loadbalancer?tab=doc#Vip">Vip</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Loadbalancer.Vip.html">Vip</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.LoadBalancer.VipArgs.html">VipArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address of the vip. Changing this creates a new
vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the vip. Changing
this updates the description of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Floating<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the vip. Changing this updates the name of
the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Persistence</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic. Changing
this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IP address of the vip. Changing this creates a new
vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the vip. Changing
this updates the description of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Floating<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the vip. Changing this updates the name of
the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Persistence</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic. Changing
this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address of the vip. Changing this creates a new
vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the vip. Changing
this updates the description of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>floating<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the vip. Changing this updates the name of
the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>persistence</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic. Changing
this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP address of the vip. Changing this creates a new
vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>state_<wbr>up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conn_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the vip. Changing
this updates the description of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>floating_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the vip. Changing this updates the name of
the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>persistence</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>pool_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic. Changing
this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Vip Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP address of the vip. Changing this creates a new
vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the vip. Changing
this updates the description of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Floating<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the vip. Changing this updates the name of
the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Persistence</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic. Changing
this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Port UUID for this VIP at associated floating IP (if any).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP address of the vip. Changing this creates a new
vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the vip. Changing
this updates the description of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Floating<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the vip. Changing this updates the name of
the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Persistence</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic. Changing
this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Port UUID for this VIP at associated floating IP (if any).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP address of the vip. Changing this creates a new
vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the vip. Changing
this updates the description of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>floating<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the vip. Changing this updates the name of
the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>persistence</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic. Changing
this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Port UUID for this VIP at associated floating IP (if any).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP address of the vip. Changing this creates a new
vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>admin_<wbr>state_<wbr>up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>conn_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the vip. Changing
this updates the description of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>floating_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the vip. Changing this updates the name of
the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>persistence</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pool_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic. Changing
this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Port UUID for this VIP at associated floating IP (if any).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subnet_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Vip Resource

Get an existing Vip resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/loadbalancer/#VipState">VipState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/loadbalancer/#Vip">Vip</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>address=None<span class="p">, </span>admin_state_up=None<span class="p">, </span>conn_limit=None<span class="p">, </span>description=None<span class="p">, </span>floating_ip=None<span class="p">, </span>name=None<span class="p">, </span>persistence=None<span class="p">, </span>pool_id=None<span class="p">, </span>port=None<span class="p">, </span>port_id=None<span class="p">, </span>protocol=None<span class="p">, </span>region=None<span class="p">, </span>subnet_id=None<span class="p">, </span>tenant_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetVip<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/loadbalancer?tab=doc#VipState">VipState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/loadbalancer?tab=doc#Vip">Vip</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Loadbalancer.Vip.html">Vip</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Loadbalancer.VipState.html">VipState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address of the vip. Changing this creates a new
vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the vip. Changing
this updates the description of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Floating<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the vip. Changing this updates the name of
the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Persistence</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic. Changing
this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Port UUID for this VIP at associated floating IP (if any).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IP address of the vip. Changing this creates a new
vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the vip. Changing
this updates the description of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Floating<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the vip. Changing this updates the name of
the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Persistence</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic. Changing
this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Port UUID for this VIP at associated floating IP (if any).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address of the vip. Changing this creates a new
vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the vip. Changing
this updates the description of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>floating<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the vip. Changing this updates the name of
the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>persistence</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic. Changing
this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Port UUID for this VIP at associated floating IP (if any).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP address of the vip. Changing this creates a new
vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>state_<wbr>up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the vip.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conn_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of connections allowed for the
vip. Default is -1, meaning no limit. Changing this updates the conn_limit
of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the vip. Changing
this updates the description of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>floating_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A *Networking* Floating IP that will be associated
with the vip. The Floating IP must be provisioned already.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the vip. Changing this updates the name of
the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>persistence</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Omit this field to prevent session persistence.
The persistence object structure is documented below. Changing this updates
the persistence of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pool_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the pool with which the vip is associated.
Changing this updates the pool_id of the existing vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The port on which to listen for client traffic. Changing
this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Port UUID for this VIP at associated floating IP (if any).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The protocol - can be either 'TCP, 'HTTP', or
HTTPS'. Changing this creates a new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a VIP. If omitted, the
`region` argument of the provider is used. Changing this creates a new
VIP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The network on which to allocate the vip's address. A
tenant can only create vips on networks authorized by policy (e.g. networks
that belong to them or networks that are shared). Changing this creates a
new vip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the vip. Required if admin wants to
create a vip member for another tenant. Changing this creates a new vip.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-openstack">https://github.com/pulumi/pulumi-openstack</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

