
---
title: "Network"
block_external_search_index: true
---



Manages a V2 Neutron network resource within OpenStack.

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as openstack from "@pulumi/openstack";

const network1 = new openstack.networking.Network("network_1", {
    adminStateUp: true,
});
const subnet1 = new openstack.networking.Subnet("subnet_1", {
    cidr: "192.168.199.0/24",
    ipVersion: 4,
    networkId: network1.id,
});
const secgroup1 = new openstack.compute.SecGroup("secgroup_1", {
    description: "a security group",
    rules: [{
        cidr: "0.0.0.0/0",
        fromPort: 22,
        ipProtocol: "tcp",
        toPort: 22,
    }],
});
const port1 = new openstack.networking.Port("port_1", {
    adminStateUp: true,
    fixedIps: [{
        ipAddress: "192.168.199.10",
        subnetId: subnet1.id,
    }],
    networkId: network1.id,
    securityGroupIds: [secgroup1.id],
});
const instance1 = new openstack.compute.Instance("instance_1", {
    networks: [{
        port: port1.id,
    }],
    securityGroups: [secgroup1.name],
});
```

{{% /example %}}
{{% /examples %}}



## Create a Network Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#Network">Network</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#NetworkArgs">NetworkArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Network</span><span class="p">(resource_name, opts=None, </span>admin_state_up=None<span class="p">, </span>availability_zone_hints=None<span class="p">, </span>description=None<span class="p">, </span>dns_domain=None<span class="p">, </span>external=None<span class="p">, </span>mtu=None<span class="p">, </span>name=None<span class="p">, </span>port_security_enabled=None<span class="p">, </span>qos_policy_id=None<span class="p">, </span>region=None<span class="p">, </span>segments=None<span class="p">, </span>shared=None<span class="p">, </span>tags=None<span class="p">, </span>tenant_id=None<span class="p">, </span>transparent_vlan=None<span class="p">, </span>value_specs=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewNetwork<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/networking?tab=doc#NetworkArgs">NetworkArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/networking?tab=doc#Network">Network</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.Network.html">Network</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.OpenStack.Networking.NetworkArgs.html">NetworkArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Human-readable description of the network. Changing this
updates the name of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The network DNS domain. Available, when Neutron DNS
extension is enabled. The `dns_domain` of a network in conjunction with the
`dns_name` attribute of its ports will be published in an external DNS
service when Neutron is configured to integrate with such a service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The network MTU. Available for read-only, when Neutron
`net-mtu` extension is enabled. Available for the modification, when
Neutron `net-mtu-writable` extension is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the network. Changing this updates the name of
the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port<wbr>Security<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether to explicitly enable or disable
port security on the network. Port Security is usually enabled by default, so
omitting this argument will usually result in a value of "true". Setting this
explicitly to `false` will disable port security. Valid values are `true` and
`false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Qos<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Reference to the associated QoS policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
`region` argument of the provider is used. Changing this creates a new
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Segments</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#networksegment">List&lt;Pulumi.<wbr>Open<wbr>Stack.<wbr>Networking.<wbr>Inputs.<wbr>Network<wbr>Segment<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}An array of one or more provider segment objects.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabilities of the
existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A set of string tags for the network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Transparent<wbr>Vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
VLAN transparent attribute set. Valid values are true and false. Defaults to
false. Changing this updates the `transparent_vlan` attribute of the existing
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Human-readable description of the network. Changing this
updates the name of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The network DNS domain. Available, when Neutron DNS
extension is enabled. The `dns_domain` of a network in conjunction with the
`dns_name` attribute of its ports will be published in an external DNS
service when Neutron is configured to integrate with such a service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The network MTU. Available for read-only, when Neutron
`net-mtu` extension is enabled. Available for the modification, when
Neutron `net-mtu-writable` extension is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the network. Changing this updates the name of
the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port<wbr>Security<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether to explicitly enable or disable
port security on the network. Port Security is usually enabled by default, so
omitting this argument will usually result in a value of "true". Setting this
explicitly to `false` will disable port security. Valid values are `true` and
`false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Qos<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Reference to the associated QoS policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
`region` argument of the provider is used. Changing this creates a new
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Segments</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#networksegment">[]Network<wbr>Segment</a></span>
    </dt>
    <dd>{{% md %}}An array of one or more provider segment objects.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabilities of the
existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A set of string tags for the network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Transparent<wbr>Vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
VLAN transparent attribute set. Valid values are true and false. Defaults to
false. Changing this updates the `transparent_vlan` attribute of the existing
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Human-readable description of the network. Changing this
updates the name of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The network DNS domain. Available, when Neutron DNS
extension is enabled. The `dns_domain` of a network in conjunction with the
`dns_name` attribute of its ports will be published in an external DNS
service when Neutron is configured to integrate with such a service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The network MTU. Available for read-only, when Neutron
`net-mtu` extension is enabled. Available for the modification, when
Neutron `net-mtu-writable` extension is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the network. Changing this updates the name of
the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port<wbr>Security<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether to explicitly enable or disable
port security on the network. Port Security is usually enabled by default, so
omitting this argument will usually result in a value of "true". Setting this
explicitly to `false` will disable port security. Valid values are `true` and
`false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>qos<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Reference to the associated QoS policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
`region` argument of the provider is used. Changing this creates a new
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>segments</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#networksegment">Network<wbr>Segment[]</a></span>
    </dt>
    <dd>{{% md %}}An array of one or more provider segment objects.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabilities of the
existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A set of string tags for the network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>transparent<wbr>Vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
VLAN transparent attribute set. Valid values are true and false. Defaults to
false. Changing this updates the `transparent_vlan` attribute of the existing
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>state_<wbr>up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability_<wbr>zone_<wbr>hints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Human-readable description of the network. Changing this
updates the name of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns_<wbr>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The network DNS domain. Available, when Neutron DNS
extension is enabled. The `dns_domain` of a network in conjunction with the
`dns_name` attribute of its ports will be published in an external DNS
service when Neutron is configured to integrate with such a service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The network MTU. Available for read-only, when Neutron
`net-mtu` extension is enabled. Available for the modification, when
Neutron `net-mtu-writable` extension is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the network. Changing this updates the name of
the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port_<wbr>security_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether to explicitly enable or disable
port security on the network. Port Security is usually enabled by default, so
omitting this argument will usually result in a value of "true". Setting this
explicitly to `false` will disable port security. Valid values are `true` and
`false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>qos_<wbr>policy_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Reference to the associated QoS policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
`region` argument of the provider is used. Changing this creates a new
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>segments</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#networksegment">List[Network<wbr>Segment]</a></span>
    </dt>
    <dd>{{% md %}}An array of one or more provider segment objects.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabilities of the
existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A set of string tags for the network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>transparent_<wbr>vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
VLAN transparent attribute set. Valid values are true and false. Defaults to
false. Changing this updates the `transparent_vlan` attribute of the existing
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value_<wbr>specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Network Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>All<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the network, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>All<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the network, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>all<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the network, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>all_<wbr>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the network, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Network Resource

Get an existing Network resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#NetworkState">NetworkState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#Network">Network</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>admin_state_up=None<span class="p">, </span>all_tags=None<span class="p">, </span>availability_zone_hints=None<span class="p">, </span>description=None<span class="p">, </span>dns_domain=None<span class="p">, </span>external=None<span class="p">, </span>mtu=None<span class="p">, </span>name=None<span class="p">, </span>port_security_enabled=None<span class="p">, </span>qos_policy_id=None<span class="p">, </span>region=None<span class="p">, </span>segments=None<span class="p">, </span>shared=None<span class="p">, </span>tags=None<span class="p">, </span>tenant_id=None<span class="p">, </span>transparent_vlan=None<span class="p">, </span>value_specs=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetNetwork<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/networking?tab=doc#NetworkState">NetworkState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/networking?tab=doc#Network">Network</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.Network.html">Network</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.NetworkState.html">NetworkState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>All<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the network, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Human-readable description of the network. Changing this
updates the name of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The network DNS domain. Available, when Neutron DNS
extension is enabled. The `dns_domain` of a network in conjunction with the
`dns_name` attribute of its ports will be published in an external DNS
service when Neutron is configured to integrate with such a service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The network MTU. Available for read-only, when Neutron
`net-mtu` extension is enabled. Available for the modification, when
Neutron `net-mtu-writable` extension is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the network. Changing this updates the name of
the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port<wbr>Security<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether to explicitly enable or disable
port security on the network. Port Security is usually enabled by default, so
omitting this argument will usually result in a value of "true". Setting this
explicitly to `false` will disable port security. Valid values are `true` and
`false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Qos<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Reference to the associated QoS policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
`region` argument of the provider is used. Changing this creates a new
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Segments</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#networksegment">List&lt;Pulumi.<wbr>Open<wbr>Stack.<wbr>Networking.<wbr>Inputs.<wbr>Network<wbr>Segment<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}An array of one or more provider segment objects.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabilities of the
existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A set of string tags for the network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Transparent<wbr>Vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
VLAN transparent attribute set. Valid values are true and false. Defaults to
false. Changing this updates the `transparent_vlan` attribute of the existing
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, object&gt;</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>All<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the network, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Human-readable description of the network. Changing this
updates the name of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The network DNS domain. Available, when Neutron DNS
extension is enabled. The `dns_domain` of a network in conjunction with the
`dns_name` attribute of its ports will be published in an external DNS
service when Neutron is configured to integrate with such a service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The network MTU. Available for read-only, when Neutron
`net-mtu` extension is enabled. Available for the modification, when
Neutron `net-mtu-writable` extension is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the network. Changing this updates the name of
the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port<wbr>Security<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether to explicitly enable or disable
port security on the network. Port Security is usually enabled by default, so
omitting this argument will usually result in a value of "true". Setting this
explicitly to `false` will disable port security. Valid values are `true` and
`false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Qos<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Reference to the associated QoS policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
`region` argument of the provider is used. Changing this creates a new
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Segments</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#networksegment">[]Network<wbr>Segment</a></span>
    </dt>
    <dd>{{% md %}}An array of one or more provider segment objects.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabilities of the
existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A set of string tags for the network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Transparent<wbr>Vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
VLAN transparent attribute set. Valid values are true and false. Defaults to
false. Changing this updates the `transparent_vlan` attribute of the existing
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>all<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the network, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Human-readable description of the network. Changing this
updates the name of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The network DNS domain. Available, when Neutron DNS
extension is enabled. The `dns_domain` of a network in conjunction with the
`dns_name` attribute of its ports will be published in an external DNS
service when Neutron is configured to integrate with such a service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The network MTU. Available for read-only, when Neutron
`net-mtu` extension is enabled. Available for the modification, when
Neutron `net-mtu-writable` extension is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the network. Changing this updates the name of
the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port<wbr>Security<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether to explicitly enable or disable
port security on the network. Port Security is usually enabled by default, so
omitting this argument will usually result in a value of "true". Setting this
explicitly to `false` will disable port security. Valid values are `true` and
`false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>qos<wbr>Policy<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Reference to the associated QoS policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
`region` argument of the provider is used. Changing this creates a new
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>segments</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#networksegment">Network<wbr>Segment[]</a></span>
    </dt>
    <dd>{{% md %}}An array of one or more provider segment objects.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabilities of the
existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A set of string tags for the network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>transparent<wbr>Vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
VLAN transparent attribute set. Valid values are true and false. Defaults to
false. Changing this updates the `transparent_vlan` attribute of the existing
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>state_<wbr>up</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value updates the
state of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>all_<wbr>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the network, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability_<wbr>zone_<wbr>hints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Human-readable description of the network. Changing this
updates the name of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns_<wbr>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The network DNS domain. Available, when Neutron DNS
extension is enabled. The `dns_domain` of a network in conjunction with the
`dns_name` attribute of its ports will be published in an external DNS
service when Neutron is configured to integrate with such a service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mtu</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The network MTU. Available for read-only, when Neutron
`net-mtu` extension is enabled. Available for the modification, when
Neutron `net-mtu-writable` extension is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the network. Changing this updates the name of
the existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port_<wbr>security_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether to explicitly enable or disable
port security on the network. Port Security is usually enabled by default, so
omitting this argument will usually result in a value of "true". Setting this
explicitly to `false` will disable port security. Valid values are `true` and
`false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>qos_<wbr>policy_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Reference to the associated QoS policy.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
`region` argument of the provider is used. Changing this creates a new
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>segments</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#networksegment">List[Network<wbr>Segment]</a></span>
    </dt>
    <dd>{{% md %}}An array of one or more provider segment objects.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabilities of the
existing network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A set of string tags for the network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>transparent_<wbr>vlan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether the network resource has the
VLAN transparent attribute set. Valid values are true and false. Defaults to
false. Changing this updates the `transparent_vlan` attribute of the existing
network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value_<wbr>specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Network<wbr>Segment</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/input/#NetworkSegment">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/output/#NetworkSegment">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/networking?tab=doc#NetworkSegmentArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/networking?tab=doc#NetworkSegmentOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of physical network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Physical<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The physical network where this network is implemented.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Segmentation<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}An isolated segment on the physical network.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of physical network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Physical<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The physical network where this network is implemented.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Segmentation<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}An isolated segment on the physical network.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of physical network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>physical<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The physical network where this network is implemented.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>segmentation<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}An isolated segment on the physical network.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of physical network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>physical<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The physical network where this network is implemented.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>segmentation_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}An isolated segment on the physical network.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-openstack">https://github.com/pulumi/pulumi-openstack</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`openstack` Terraform Provider](https://github.com/terraform-providers/terraform-provider-openstack).</dd>
</dl>

