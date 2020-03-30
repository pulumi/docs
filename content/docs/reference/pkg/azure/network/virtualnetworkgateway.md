
---
title: "VirtualNetworkGateway"
block_external_search_index: true
---

Manages a Virtual Network Gateway to establish secure, cross-premises connectivity.

> **Note:** Please be aware that provisioning a Virtual Network Gateway takes a long time (between 30 minutes and 1 hour)

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_network_gateway.html.markdown.



## Create a VirtualNetworkGateway Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#VirtualNetworkGateway">VirtualNetworkGateway</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#VirtualNetworkGatewayArgs">VirtualNetworkGatewayArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">VirtualNetworkGateway</span><span class="p">(resource_name, opts=None, </span>active_active=None<span class="p">, </span>bgp_settings=None<span class="p">, </span>default_local_network_gateway_id=None<span class="p">, </span>enable_bgp=None<span class="p">, </span>generation=None<span class="p">, </span>ip_configurations=None<span class="p">, </span>location=None<span class="p">, </span>name=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>sku=None<span class="p">, </span>tags=None<span class="p">, </span>type=None<span class="p">, </span>vpn_client_configuration=None<span class="p">, </span>vpn_type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewVirtualNetworkGateway<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayArgs">VirtualNetworkGatewayArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGateway">VirtualNetworkGateway</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.VirtualNetworkGateway.html">VirtualNetworkGateway</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.Inputs.VirtualNetworkGatewayArgs.html">VirtualNetworkGatewayArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Active<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bgp<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewaybgpsettings">Virtual<wbr>Network<wbr>Gateway<wbr>Bgp<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Generation of the Virtual Network gateway. Possible values include `Generation1`, `Generation2` or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayipconfiguration">List&lt;Virtual<wbr>Network<wbr>Gateway<wbr>Ip<wbr>Configuration<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw4`,`VpnGw5`, `VpnGw1AZ`,
`VpnGw2AZ`, `VpnGw3AZ`,`VpnGw4AZ` and `VpnGw5AZ` and depend on the `type`, `vpn_type` and
`generation` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.
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
    <dd>{{% md %}}The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Client<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfiguration">Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Active<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bgp<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewaybgpsettings">*Virtual<wbr>Network<wbr>Gateway<wbr>Bgp<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Generation of the Virtual Network gateway. Possible values include `Generation1`, `Generation2` or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayipconfiguration">[]Virtual<wbr>Network<wbr>Gateway<wbr>Ip<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw4`,`VpnGw5`, `VpnGw1AZ`,
`VpnGw2AZ`, `VpnGw3AZ`,`VpnGw4AZ` and `VpnGw5AZ` and depend on the `type`, `vpn_type` and
`generation` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.
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
    <dd>{{% md %}}The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Client<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfiguration">*Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bgp<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewaybgpsettings">Virtual<wbr>Network<wbr>Gateway<wbr>Bgp<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Generation of the Virtual Network gateway. Possible values include `Generation1`, `Generation2` or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ip<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayipconfiguration">Virtual<wbr>Network<wbr>Gateway<wbr>Ip<wbr>Configuration[]</a></span>
    </dt>
    <dd>{{% md %}}One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw4`,`VpnGw5`, `VpnGw1AZ`,
`VpnGw2AZ`, `VpnGw3AZ`,`VpnGw4AZ` and `VpnGw5AZ` and depend on the `type`, `vpn_type` and
`generation` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.
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
    <dd>{{% md %}}The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn<wbr>Client<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfiguration">Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration?</a></span>
    </dt>
    <dd>{{% md %}}A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active_<wbr>active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bgp_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewaybgpsettings">Dict[Virtual<wbr>Network<wbr>Gateway<wbr>Bgp<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>local_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Generation of the Virtual Network gateway. Possible values include `Generation1`, `Generation2` or `None`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ip_<wbr>configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayipconfiguration">List[Virtual<wbr>Network<wbr>Gateway<wbr>Ip<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw4`,`VpnGw5`, `VpnGw1AZ`,
`VpnGw2AZ`, `VpnGw3AZ`,`VpnGw4AZ` and `VpnGw5AZ` and depend on the `type`, `vpn_type` and
`generation` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.
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
    <dd>{{% md %}}The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn_<wbr>client_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfiguration">Dict[Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## VirtualNetworkGateway Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Active<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bgp<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewaybgpsettings">Virtual<wbr>Network<wbr>Gateway<wbr>Bgp<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Generation of the Virtual Network gateway. Possible values include `Generation1`, `Generation2` or `None`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ip<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayipconfiguration">List&lt;Virtual<wbr>Network<wbr>Gateway<wbr>Ip<wbr>Configuration&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw4`,`VpnGw5`, `VpnGw1AZ`,
`VpnGw2AZ`, `VpnGw3AZ`,`VpnGw4AZ` and `VpnGw5AZ` and depend on the `type`, `vpn_type` and
`generation` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.
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
    <dd>{{% md %}}The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpn<wbr>Client<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfiguration">Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration?</a></span>
    </dt>
    <dd>{{% md %}}A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Active<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Bgp<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewaybgpsettings">Virtual<wbr>Network<wbr>Gateway<wbr>Bgp<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Generation of the Virtual Network gateway. Possible values include `Generation1`, `Generation2` or `None`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ip<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayipconfiguration">[]Virtual<wbr>Network<wbr>Gateway<wbr>Ip<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw4`,`VpnGw5`, `VpnGw1AZ`,
`VpnGw2AZ`, `VpnGw3AZ`,`VpnGw4AZ` and `VpnGw5AZ` and depend on the `type`, `vpn_type` and
`generation` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.
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
    <dd>{{% md %}}The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpn<wbr>Client<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfiguration">*Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>active<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bgp<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewaybgpsettings">Virtual<wbr>Network<wbr>Gateway<wbr>Bgp<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Generation of the Virtual Network gateway. Possible values include `Generation1`, `Generation2` or `None`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ip<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayipconfiguration">Virtual<wbr>Network<wbr>Gateway<wbr>Ip<wbr>Configuration[]</a></span>
    </dt>
    <dd>{{% md %}}One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw4`,`VpnGw5`, `VpnGw1AZ`,
`VpnGw2AZ`, `VpnGw3AZ`,`VpnGw4AZ` and `VpnGw5AZ` and depend on the `type`, `vpn_type` and
`generation` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.
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
    <dd>{{% md %}}The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpn<wbr>Client<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfiguration">Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration?</a></span>
    </dt>
    <dd>{{% md %}}A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>active_<wbr>active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>bgp_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewaybgpsettings">Dict[Virtual<wbr>Network<wbr>Gateway<wbr>Bgp<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>local_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Generation of the Virtual Network gateway. Possible values include `Generation1`, `Generation2` or `None`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ip_<wbr>configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayipconfiguration">List[Virtual<wbr>Network<wbr>Gateway<wbr>Ip<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw4`,`VpnGw5`, `VpnGw1AZ`,
`VpnGw2AZ`, `VpnGw3AZ`,`VpnGw4AZ` and `VpnGw5AZ` and depend on the `type`, `vpn_type` and
`generation` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.
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
    <dd>{{% md %}}The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpn_<wbr>client_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfiguration">Dict[Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpn_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing VirtualNetworkGateway Resource

Get an existing VirtualNetworkGateway resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#VirtualNetworkGatewayState">VirtualNetworkGatewayState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#VirtualNetworkGateway">VirtualNetworkGateway</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>active_active=None<span class="p">, </span>bgp_settings=None<span class="p">, </span>default_local_network_gateway_id=None<span class="p">, </span>enable_bgp=None<span class="p">, </span>generation=None<span class="p">, </span>ip_configurations=None<span class="p">, </span>location=None<span class="p">, </span>name=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>sku=None<span class="p">, </span>tags=None<span class="p">, </span>type=None<span class="p">, </span>vpn_client_configuration=None<span class="p">, </span>vpn_type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetVirtualNetworkGateway<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayState">VirtualNetworkGatewayState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGateway">VirtualNetworkGateway</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.VirtualNetworkGateway.html">VirtualNetworkGateway</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.VirtualNetworkGatewayState.html">VirtualNetworkGatewayState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Active<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bgp<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewaybgpsettings">Virtual<wbr>Network<wbr>Gateway<wbr>Bgp<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Generation of the Virtual Network gateway. Possible values include `Generation1`, `Generation2` or `None`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayipconfiguration">List&lt;Virtual<wbr>Network<wbr>Gateway<wbr>Ip<wbr>Configuration<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw4`,`VpnGw5`, `VpnGw1AZ`,
`VpnGw2AZ`, `VpnGw3AZ`,`VpnGw4AZ` and `VpnGw5AZ` and depend on the `type`, `vpn_type` and
`generation` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.
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
    <dd>{{% md %}}The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Client<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfiguration">Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Active<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bgp<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewaybgpsettings">*Virtual<wbr>Network<wbr>Gateway<wbr>Bgp<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Generation of the Virtual Network gateway. Possible values include `Generation1`, `Generation2` or `None`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayipconfiguration">[]Virtual<wbr>Network<wbr>Gateway<wbr>Ip<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw4`,`VpnGw5`, `VpnGw1AZ`,
`VpnGw2AZ`, `VpnGw3AZ`,`VpnGw4AZ` and `VpnGw5AZ` and depend on the `type`, `vpn_type` and
`generation` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.
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
    <dd>{{% md %}}The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Client<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfiguration">*Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active<wbr>Active</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bgp<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewaybgpsettings">Virtual<wbr>Network<wbr>Gateway<wbr>Bgp<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Generation of the Virtual Network gateway. Possible values include `Generation1`, `Generation2` or `None`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayipconfiguration">Virtual<wbr>Network<wbr>Gateway<wbr>Ip<wbr>Configuration[]?</a></span>
    </dt>
    <dd>{{% md %}}One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw4`,`VpnGw5`, `VpnGw1AZ`,
`VpnGw2AZ`, `VpnGw3AZ`,`VpnGw4AZ` and `VpnGw5AZ` and depend on the `type`, `vpn_type` and
`generation` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.
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
    <dd>{{% md %}}The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn<wbr>Client<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfiguration">Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration?</a></span>
    </dt>
    <dd>{{% md %}}A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active_<wbr>active</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a `HighPerformance` or an
`UltraPerformance` sku. If `false`, an active-standby gateway will be created.
Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bgp_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewaybgpsettings">Dict[Virtual<wbr>Network<wbr>Gateway<wbr>Bgp<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>local_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (*forced tunneling*). Refer to the
[Azure documentation on forced tunneling](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm).
If not specified, forced tunneling is disabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>generation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Generation of the Virtual Network gateway. Possible values include `Generation1`, `Generation2` or `None`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>configurations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayipconfiguration">List[Virtual<wbr>Network<wbr>Gateway<wbr>Ip<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}One or two `ip_configuration` blocks documented below.
An active-standby gateway requires exactly one `ip_configuration` block whereas
an active-active gateway requires exactly two `ip_configuration` blocks.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Configuration of the size and capacity of the virtual network
gateway. Valid options are `Basic`, `Standard`, `HighPerformance`, `UltraPerformance`,
`ErGw1AZ`, `ErGw2AZ`, `ErGw3AZ`, `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw4`,`VpnGw5`, `VpnGw1AZ`,
`VpnGw2AZ`, `VpnGw3AZ`,`VpnGw4AZ` and `VpnGw5AZ` and depend on the `type`, `vpn_type` and
`generation` arguments.
A `PolicyBased` gateway only supports the `Basic` sku. Further, the `UltraPerformance`
sku is only supported by an `ExpressRoute` gateway.
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
    <dd>{{% md %}}The type of the Virtual Network Gateway. Valid options are
`Vpn` or `ExpressRoute`. Changing the type forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn_<wbr>client_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfiguration">Dict[Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}A `vpn_client_configuration` block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The routing type of the Virtual Network Gateway. Valid
options are `RouteBased` or `PolicyBased`. Defaults to `RouteBased`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Virtual<wbr>Network<wbr>Gateway<wbr>Bgp<wbr>Settings</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#VirtualNetworkGatewayBgpSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#VirtualNetworkGatewayBgpSettings">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayBgpSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayBgpSettingsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The Autonomous System Number (ASN) to use as part of the BGP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peer<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The weight added to routes which have been learned
through BGP peering. Valid values can be between `0` and `100`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peering<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The BGP peer IP address of the virtual network
gateway. This address is needed to configure the created gateway as a BGP Peer
on the on-premises VPN devices. The IP address must be part of the subnet of
the Virtual Network Gateway. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The Autonomous System Number (ASN) to use as part of the BGP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peer<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The weight added to routes which have been learned
through BGP peering. Valid values can be between `0` and `100`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peering<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The BGP peer IP address of the virtual network
gateway. This address is needed to configure the created gateway as a BGP Peer
on the on-premises VPN devices. The IP address must be part of the subnet of
the Virtual Network Gateway. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The Autonomous System Number (ASN) to use as part of the BGP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peer<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The weight added to routes which have been learned
through BGP peering. Valid values can be between `0` and `100`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peering<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The BGP peer IP address of the virtual network
gateway. This address is needed to configure the created gateway as a BGP Peer
on the on-premises VPN devices. The IP address must be part of the subnet of
the Virtual Network Gateway. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Autonomous System Number (ASN) to use as part of the BGP.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peer<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The weight added to routes which have been learned
through BGP peering. Valid values can be between `0` and `100`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peering<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The BGP peer IP address of the virtual network
gateway. This address is needed to configure the created gateway as a BGP Peer
on the on-premises VPN devices. The IP address must be part of the subnet of
the Virtual Network Gateway. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Virtual<wbr>Network<wbr>Gateway<wbr>Ip<wbr>Configuration</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#VirtualNetworkGatewayIpConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#VirtualNetworkGatewayIpConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayIpConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayIpConfigurationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Ip<wbr>Address<wbr>Allocation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Defines how the private IP address
of the gateways virtual interface is assigned. Valid options are `Static` or
`Dynamic`. Defaults to `Dynamic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ip<wbr>Address<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the public ip address to associate
with the Virtual Network Gateway.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the gateway subnet of a virtual network in
which the virtual network gateway will be created. It is mandatory that
the associated subnet is named `GatewaySubnet`. Therefore, each virtual
network can contain at most a single Virtual Network Gateway.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Ip<wbr>Address<wbr>Allocation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Defines how the private IP address
of the gateways virtual interface is assigned. Valid options are `Static` or
`Dynamic`. Defaults to `Dynamic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ip<wbr>Address<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the public ip address to associate
with the Virtual Network Gateway.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the gateway subnet of a virtual network in
which the virtual network gateway will be created. It is mandatory that
the associated subnet is named `GatewaySubnet`. Therefore, each virtual
network can contain at most a single Virtual Network Gateway.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Ip<wbr>Address<wbr>Allocation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Defines how the private IP address
of the gateways virtual interface is assigned. Valid options are `Static` or
`Dynamic`. Defaults to `Dynamic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Ip<wbr>Address<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the public ip address to associate
with the Virtual Network Gateway.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the gateway subnet of a virtual network in
which the virtual network gateway will be created. It is mandatory that
the associated subnet is named `GatewaySubnet`. Therefore, each virtual
network can contain at most a single Virtual Network Gateway.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Ip<wbr>Address<wbr>Allocation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Defines how the private IP address
of the gateways virtual interface is assigned. Valid options are `Static` or
`Dynamic`. Defaults to `Dynamic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Ip<wbr>Address<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the public ip address to associate
with the Virtual Network Gateway.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the gateway subnet of a virtual network in
which the virtual network gateway will be created. It is mandatory that
the associated subnet is named `GatewaySubnet`. Therefore, each virtual
network can contain at most a single Virtual Network Gateway.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#VirtualNetworkGatewayVpnClientConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#VirtualNetworkGatewayVpnClientConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayVpnClientConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayVpnClientConfigurationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Address<wbr>Spaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The address space out of which ip addresses for
vpn clients will be taken. You can provide more than one address space, e.g.
in CIDR notation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Radius<wbr>Server<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The address of the Radius server.
This setting is incompatible with the use of `root_certificate` and `revoked_certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Radius<wbr>Server<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The secret used by the Radius server.
This setting is incompatible with the use of `root_certificate` and `revoked_certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revoked<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfigurationrevokedcertificate">List&lt;Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration<wbr>Revoked<wbr>Certificate<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `revoked_certificate` blocks which
are defined below.
This setting is incompatible with the use of `radius_server_address` and `radius_server_secret`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfigurationrootcertificate">List&lt;Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration<wbr>Root<wbr>Certificate<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `root_certificate` blocks which are
defined below. These root certificates are used to sign the client certificate
used by the VPN clients to connect to the gateway.
This setting is incompatible with the use of `radius_server_address` and `radius_server_secret`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Client<wbr>Protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of the protocols supported by the vpn client.
The supported values are `SSTP`, `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Address<wbr>Spaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The address space out of which ip addresses for
vpn clients will be taken. You can provide more than one address space, e.g.
in CIDR notation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Radius<wbr>Server<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The address of the Radius server.
This setting is incompatible with the use of `root_certificate` and `revoked_certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Radius<wbr>Server<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The secret used by the Radius server.
This setting is incompatible with the use of `root_certificate` and `revoked_certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Revoked<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfigurationrevokedcertificate">[]Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration<wbr>Revoked<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}One or more `revoked_certificate` blocks which
are defined below.
This setting is incompatible with the use of `radius_server_address` and `radius_server_secret`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfigurationrootcertificate">[]Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration<wbr>Root<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}One or more `root_certificate` blocks which are
defined below. These root certificates are used to sign the client certificate
used by the VPN clients to connect to the gateway.
This setting is incompatible with the use of `radius_server_address` and `radius_server_secret`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpn<wbr>Client<wbr>Protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of the protocols supported by the vpn client.
The supported values are `SSTP`, `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>address<wbr>Spaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The address space out of which ip addresses for
vpn clients will be taken. You can provide more than one address space, e.g.
in CIDR notation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>radius<wbr>Server<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The address of the Radius server.
This setting is incompatible with the use of `root_certificate` and `revoked_certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>radius<wbr>Server<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The secret used by the Radius server.
This setting is incompatible with the use of `root_certificate` and `revoked_certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revoked<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfigurationrevokedcertificate">Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration<wbr>Revoked<wbr>Certificate[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `revoked_certificate` blocks which
are defined below.
This setting is incompatible with the use of `radius_server_address` and `radius_server_secret`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfigurationrootcertificate">Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration<wbr>Root<wbr>Certificate[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `root_certificate` blocks which are
defined below. These root certificates are used to sign the client certificate
used by the VPN clients to connect to the gateway.
This setting is incompatible with the use of `radius_server_address` and `radius_server_secret`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn<wbr>Client<wbr>Protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of the protocols supported by the vpn client.
The supported values are `SSTP`, `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>address_<wbr>spaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The address space out of which ip addresses for
vpn clients will be taken. You can provide more than one address space, e.g.
in CIDR notation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>radius<wbr>Server<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The address of the Radius server.
This setting is incompatible with the use of `root_certificate` and `revoked_certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>radius<wbr>Server<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The secret used by the Radius server.
This setting is incompatible with the use of `root_certificate` and `revoked_certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>revoked<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfigurationrevokedcertificate">List[Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration<wbr>Revoked<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}One or more `revoked_certificate` blocks which
are defined below.
This setting is incompatible with the use of `radius_server_address` and `radius_server_secret`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>root<wbr>Certificates</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#virtualnetworkgatewayvpnclientconfigurationrootcertificate">List[Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration<wbr>Root<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}One or more `root_certificate` blocks which are
defined below. These root certificates are used to sign the client certificate
used by the VPN clients to connect to the gateway.
This setting is incompatible with the use of `radius_server_address` and `radius_server_secret`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpn<wbr>Client<wbr>Protocols</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of the protocols supported by the vpn client.
The supported values are `SSTP`, `IkeV2` and `OpenVPN`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration<wbr>Revoked<wbr>Certificate</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>thumbprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Virtual<wbr>Network<wbr>Gateway<wbr>Vpn<wbr>Client<wbr>Configuration<wbr>Root<wbr>Certificate</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#VirtualNetworkGatewayVpnClientConfigurationRootCertificate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#VirtualNetworkGatewayVpnClientConfigurationRootCertificate">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayVpnClientConfigurationRootCertificateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Cert<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SHA1 thumbprint of the certificate to be
revoked.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Cert<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SHA1 thumbprint of the certificate to be
revoked.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Cert<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SHA1 thumbprint of the certificate to be
revoked.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the revoked certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Cert<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SHA1 thumbprint of the certificate to be
revoked.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







