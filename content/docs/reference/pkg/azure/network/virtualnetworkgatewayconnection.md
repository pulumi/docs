
---
title: "VirtualNetworkGatewayConnection"
block_external_search_index: true
---

Manages a connection in an existing Virtual Network Gateway.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_network_gateway_connection.html.markdown.



## Create a VirtualNetworkGatewayConnection Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#VirtualNetworkGatewayConnection">VirtualNetworkGatewayConnection</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#VirtualNetworkGatewayConnectionArgs">VirtualNetworkGatewayConnectionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">VirtualNetworkGatewayConnection</span><span class="p">(resource_name, opts=None, </span>authorization_key=None<span class="p">, </span>connection_protocol=None<span class="p">, </span>enable_bgp=None<span class="p">, </span>express_route_circuit_id=None<span class="p">, </span>express_route_gateway_bypass=None<span class="p">, </span>ipsec_policy=None<span class="p">, </span>local_network_gateway_id=None<span class="p">, </span>location=None<span class="p">, </span>name=None<span class="p">, </span>peer_virtual_network_gateway_id=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>routing_weight=None<span class="p">, </span>shared_key=None<span class="p">, </span>tags=None<span class="p">, </span>type=None<span class="p">, </span>use_policy_based_traffic_selectors=None<span class="p">, </span>virtual_network_gateway_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewVirtualNetworkGatewayConnection<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayConnectionArgs">VirtualNetworkGatewayConnectionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayConnection">VirtualNetworkGatewayConnection</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.VirtualNetworkGatewayConnection.html">VirtualNetworkGatewayConnection</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.Inputs.VirtualNetworkGatewayConnectionArgs.html">VirtualNetworkGatewayConnectionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Authorization<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE protocol version to use. Possible
values are `IKEv1` and `IKEv2`. Defaults to `IKEv2`.
Changing this value will force a resource to be created.
> **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Express<wbr>Route<wbr>Circuit<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Express<wbr>Route<wbr>Gateway<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayconnectionipsecpolicy">Virtual<wbr>Network<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the connection. Changing the name forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peer<wbr>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Routing<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The routing weight. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Policy<wbr>Based<wbr>Traffic<wbr>Selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Authorization<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IKE protocol version to use. Possible
values are `IKEv1` and `IKEv2`. Defaults to `IKEv2`.
Changing this value will force a resource to be created.
> **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Express<wbr>Route<wbr>Circuit<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Express<wbr>Route<wbr>Gateway<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayconnectionipsecpolicy">*Virtual<wbr>Network<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the connection. Changing the name forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peer<wbr>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Routing<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The routing weight. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Policy<wbr>Based<wbr>Traffic<wbr>Selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>authorization<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE protocol version to use. Possible
values are `IKEv1` and `IKEv2`. Defaults to `IKEv2`.
Changing this value will force a resource to be created.
> **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>express<wbr>Route<wbr>Circuit<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>express<wbr>Route<wbr>Gateway<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayconnectionipsecpolicy">Virtual<wbr>Network<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the connection. Changing the name forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peer<wbr>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>routing<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The routing weight. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Policy<wbr>Based<wbr>Traffic<wbr>Selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>authorization_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection_<wbr>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IKE protocol version to use. Possible
values are `IKEv1` and `IKEv2`. Defaults to `IKEv2`.
Changing this value will force a resource to be created.
> **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>express_<wbr>route_<wbr>circuit_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>express_<wbr>route_<wbr>gateway_<wbr>bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipsec_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayconnectionipsecpolicy">Dict[Virtual<wbr>Network<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the connection. Changing the name forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peer_<wbr>virtual_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>routing_<wbr>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The routing weight. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use_<wbr>policy_<wbr>based_<wbr>traffic_<wbr>selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>virtual_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## VirtualNetworkGatewayConnection Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Authorization<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connection<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE protocol version to use. Possible
values are `IKEv1` and `IKEv2`. Defaults to `IKEv2`.
Changing this value will force a resource to be created.
> **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Express<wbr>Route<wbr>Circuit<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Express<wbr>Route<wbr>Gateway<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayconnectionipsecpolicy">Virtual<wbr>Network<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the connection. Changing the name forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Peer<wbr>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Routing<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The routing weight. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Use<wbr>Policy<wbr>Based<wbr>Traffic<wbr>Selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Authorization<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connection<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE protocol version to use. Possible
values are `IKEv1` and `IKEv2`. Defaults to `IKEv2`.
Changing this value will force a resource to be created.
> **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Express<wbr>Route<wbr>Circuit<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Express<wbr>Route<wbr>Gateway<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayconnectionipsecpolicy">*Virtual<wbr>Network<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the connection. Changing the name forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Peer<wbr>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Routing<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The routing weight. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Use<wbr>Policy<wbr>Based<wbr>Traffic<wbr>Selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>authorization<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connection<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE protocol version to use. Possible
values are `IKEv1` and `IKEv2`. Defaults to `IKEv2`.
Changing this value will force a resource to be created.
> **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>express<wbr>Route<wbr>Circuit<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>express<wbr>Route<wbr>Gateway<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayconnectionipsecpolicy">Virtual<wbr>Network<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the connection. Changing the name forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>peer<wbr>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>routing<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The routing weight. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>use<wbr>Policy<wbr>Based<wbr>Traffic<wbr>Selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>authorization_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connection_<wbr>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IKE protocol version to use. Possible
values are `IKEv1` and `IKEv2`. Defaults to `IKEv2`.
Changing this value will force a resource to be created.
> **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>express_<wbr>route_<wbr>circuit_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>express_<wbr>route_<wbr>gateway_<wbr>bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ipsec_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayconnectionipsecpolicy">Dict[Virtual<wbr>Network<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>local_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the connection. Changing the name forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>peer_<wbr>virtual_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>routing_<wbr>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The routing weight. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shared_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>use_<wbr>policy_<wbr>based_<wbr>traffic_<wbr>selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtual_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing VirtualNetworkGatewayConnection Resource

Get an existing VirtualNetworkGatewayConnection resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#VirtualNetworkGatewayConnectionState">VirtualNetworkGatewayConnectionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#VirtualNetworkGatewayConnection">VirtualNetworkGatewayConnection</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>authorization_key=None<span class="p">, </span>connection_protocol=None<span class="p">, </span>enable_bgp=None<span class="p">, </span>express_route_circuit_id=None<span class="p">, </span>express_route_gateway_bypass=None<span class="p">, </span>ipsec_policy=None<span class="p">, </span>local_network_gateway_id=None<span class="p">, </span>location=None<span class="p">, </span>name=None<span class="p">, </span>peer_virtual_network_gateway_id=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>routing_weight=None<span class="p">, </span>shared_key=None<span class="p">, </span>tags=None<span class="p">, </span>type=None<span class="p">, </span>use_policy_based_traffic_selectors=None<span class="p">, </span>virtual_network_gateway_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetVirtualNetworkGatewayConnection<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayConnectionState">VirtualNetworkGatewayConnectionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayConnection">VirtualNetworkGatewayConnection</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.VirtualNetworkGatewayConnection.html">VirtualNetworkGatewayConnection</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.VirtualNetworkGatewayConnectionState.html">VirtualNetworkGatewayConnectionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Authorization<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE protocol version to use. Possible
values are `IKEv1` and `IKEv2`. Defaults to `IKEv2`.
Changing this value will force a resource to be created.
> **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Express<wbr>Route<wbr>Circuit<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Express<wbr>Route<wbr>Gateway<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayconnectionipsecpolicy">Virtual<wbr>Network<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the connection. Changing the name forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peer<wbr>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Routing<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The routing weight. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Policy<wbr>Based<wbr>Traffic<wbr>Selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Authorization<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IKE protocol version to use. Possible
values are `IKEv1` and `IKEv2`. Defaults to `IKEv2`.
Changing this value will force a resource to be created.
> **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Express<wbr>Route<wbr>Circuit<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Express<wbr>Route<wbr>Gateway<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayconnectionipsecpolicy">*Virtual<wbr>Network<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the connection. Changing the name forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peer<wbr>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Routing<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The routing weight. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Policy<wbr>Based<wbr>Traffic<wbr>Selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>authorization<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IKE protocol version to use. Possible
values are `IKEv1` and `IKEv2`. Defaults to `IKEv2`.
Changing this value will force a resource to be created.
> **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>express<wbr>Route<wbr>Circuit<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>express<wbr>Route<wbr>Gateway<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipsec<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayconnectionipsecpolicy">Virtual<wbr>Network<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the connection. Changing the name forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peer<wbr>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>routing<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The routing weight. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Policy<wbr>Based<wbr>Traffic<wbr>Selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>authorization_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection_<wbr>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IKE protocol version to use. Possible
values are `IKEv1` and `IKEv2`. Defaults to `IKEv2`.
Changing this value will force a resource to be created.
> **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>express_<wbr>route_<wbr>circuit_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when `type` is `ExpressRoute`).
The Express Route Circuit can be in the same or in a different subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>express_<wbr>route_<wbr>gateway_<wbr>bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipsec_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayconnectionipsecpolicy">Dict[Virtual<wbr>Network<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `ipsec_policy` block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when creating Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the connection. Changing the name forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peer_<wbr>virtual_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`). The peer Virtual Network Gateway can be in the same or
in a different subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>routing_<wbr>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The routing weight. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shared_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of connection. Valid options are `IPsec`
(Site-to-Site), `ExpressRoute` (ExpressRoute), and `Vnet2Vnet` (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use_<wbr>policy_<wbr>based_<wbr>traffic_<wbr>selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Virtual<wbr>Network<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#VirtualNetworkGatewayConnectionIpsecPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#VirtualNetworkGatewayConnectionIpsecPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayConnectionIpsecPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayConnectionIpsecPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dh<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DH group used in IKE phase 1 for initial SA. Valid
options are `DHGroup1`, `DHGroup14`, `DHGroup2`, `DHGroup2048`, `DHGroup24`,
`ECP256`, `ECP384`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ike<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE encryption algorithm. Valid
options are `AES128`, `AES192`, `AES256`, `DES`, or `DES3`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ike<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE integrity algorithm. Valid
options are `MD5`, `SHA1`, `SHA256`, or `SHA384`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipsec<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPSec encryption algorithm. Valid
options are `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128`, `GCMAES192`, `GCMAES256`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipsec<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPSec integrity algorithm. Valid
options are `GCMAES128`, `GCMAES192`, `GCMAES256`, `MD5`, `SHA1`, or `SHA256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Pfs<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DH group used in IKE phase 2 for new child SA.
Valid options are `ECP256`, `ECP384`, `PFS1`, `PFS2`, `PFS2048`, `PFS24`,
or `None`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sa<wbr>Datasize</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The IPSec SA payload size in KB. Must be at least
`1024` KB. Defaults to `102400000` KB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sa<wbr>Lifetime</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The IPSec SA lifetime in seconds. Must be at least
`300` seconds. Defaults to `27000` seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dh<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DH group used in IKE phase 1 for initial SA. Valid
options are `DHGroup1`, `DHGroup14`, `DHGroup2`, `DHGroup2048`, `DHGroup24`,
`ECP256`, `ECP384`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ike<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE encryption algorithm. Valid
options are `AES128`, `AES192`, `AES256`, `DES`, or `DES3`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ike<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE integrity algorithm. Valid
options are `MD5`, `SHA1`, `SHA256`, or `SHA384`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipsec<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPSec encryption algorithm. Valid
options are `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128`, `GCMAES192`, `GCMAES256`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipsec<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPSec integrity algorithm. Valid
options are `GCMAES128`, `GCMAES192`, `GCMAES256`, `MD5`, `SHA1`, or `SHA256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Pfs<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DH group used in IKE phase 2 for new child SA.
Valid options are `ECP256`, `ECP384`, `PFS1`, `PFS2`, `PFS2048`, `PFS24`,
or `None`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sa<wbr>Datasize</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The IPSec SA payload size in KB. Must be at least
`1024` KB. Defaults to `102400000` KB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sa<wbr>Lifetime</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The IPSec SA lifetime in seconds. Must be at least
`300` seconds. Defaults to `27000` seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dh<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DH group used in IKE phase 1 for initial SA. Valid
options are `DHGroup1`, `DHGroup14`, `DHGroup2`, `DHGroup2048`, `DHGroup24`,
`ECP256`, `ECP384`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ike<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE encryption algorithm. Valid
options are `AES128`, `AES192`, `AES256`, `DES`, or `DES3`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ike<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IKE integrity algorithm. Valid
options are `MD5`, `SHA1`, `SHA256`, or `SHA384`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipsec<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPSec encryption algorithm. Valid
options are `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128`, `GCMAES192`, `GCMAES256`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipsec<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPSec integrity algorithm. Valid
options are `GCMAES128`, `GCMAES192`, `GCMAES256`, `MD5`, `SHA1`, or `SHA256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>pfs<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DH group used in IKE phase 2 for new child SA.
Valid options are `ECP256`, `ECP384`, `PFS1`, `PFS2`, `PFS2048`, `PFS24`,
or `None`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sa<wbr>Datasize</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The IPSec SA payload size in KB. Must be at least
`1024` KB. Defaults to `102400000` KB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sa<wbr>Lifetime</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The IPSec SA lifetime in seconds. Must be at least
`300` seconds. Defaults to `27000` seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dh<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The DH group used in IKE phase 1 for initial SA. Valid
options are `DHGroup1`, `DHGroup14`, `DHGroup2`, `DHGroup2048`, `DHGroup24`,
`ECP256`, `ECP384`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ike<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IKE encryption algorithm. Valid
options are `AES128`, `AES192`, `AES256`, `DES`, or `DES3`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ike<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IKE integrity algorithm. Valid
options are `MD5`, `SHA1`, `SHA256`, or `SHA384`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipsec<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IPSec encryption algorithm. Valid
options are `AES128`, `AES192`, `AES256`, `DES`, `DES3`, `GCMAES128`, `GCMAES192`, `GCMAES256`, or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipsec<wbr>Integrity</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IPSec integrity algorithm. Valid
options are `GCMAES128`, `GCMAES192`, `GCMAES256`, `MD5`, `SHA1`, or `SHA256`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>pfs<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The DH group used in IKE phase 2 for new child SA.
Valid options are `ECP256`, `ECP384`, `PFS1`, `PFS2`, `PFS2048`, `PFS24`,
or `None`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sa<wbr>Datasize</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The IPSec SA payload size in KB. Must be at least
`1024` KB. Defaults to `102400000` KB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sa<wbr>Lifetime</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The IPSec SA lifetime in seconds. Must be at least
`300` seconds. Defaults to `27000` seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







