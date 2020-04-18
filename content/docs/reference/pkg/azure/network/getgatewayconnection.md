
---
title: "GetGatewayConnection"
block_external_search_index: true
---



Use this data source to access information about an existing Virtual Network Gateway Connection.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/virtual_network_gateway_connection.html.markdown.





## Using GetGatewayConnection

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getGatewayConnection<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#GetGatewayConnectionArgs">GetGatewayConnectionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#GetGatewayConnectionResult">GetGatewayConnectionResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_gateway_connection(</span>name=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupGatewayConnection<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#LookupGatewayConnectionArgs">LookupGatewayConnectionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#LookupGatewayConnectionResult">LookupGatewayConnectionResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetGatewayConnection </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.GetGatewayConnectionResult.html">GetGatewayConnectionResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.GetGatewayConnectionArgs.html">GetGatewayConnectionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Virtual Network Gateway Connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the resource group the Virtual Network Gateway Connection is located in.
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
    <dd>{{% md %}}Specifies the name of the Virtual Network Gateway Connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the resource group the Virtual Network Gateway Connection is located in.
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
    <dd>{{% md %}}Specifies the name of the Virtual Network Gateway Connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the resource group the Virtual Network Gateway Connection is located in.
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
    <dd>{{% md %}}Specifies the name of the Virtual Network Gateway Connection.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the resource group the Virtual Network Gateway Connection is located in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetGatewayConnection Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Authorization<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is present only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connection<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Egress<wbr>Bytes<wbr>Transferred</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Express<wbr>Route<wbr>Circuit<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
(i.e. when `type` is `ExpressRoute`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Express<wbr>Route<wbr>Gateway<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding. This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ingress<wbr>Bytes<wbr>Transferred</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ipsec<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getgatewayconnectionipsecpolicy">List&lt;Get<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when a Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Peer<wbr>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Guid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Routing<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The routing weight.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string></span>
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
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Use<wbr>Policy<wbr>Based<wbr>Traffic<wbr>Selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection is created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Authorization<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is present only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connection<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Egress<wbr>Bytes<wbr>Transferred</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Express<wbr>Route<wbr>Circuit<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
(i.e. when `type` is `ExpressRoute`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Express<wbr>Route<wbr>Gateway<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding. This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ingress<wbr>Bytes<wbr>Transferred</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ipsec<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getgatewayconnectionipsecpolicy">[]Get<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when a Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Peer<wbr>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Guid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Routing<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The routing weight.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. 
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
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Use<wbr>Policy<wbr>Based<wbr>Traffic<wbr>Selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection is created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>authorization<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The authorization key associated with the
Express Route Circuit. This field is present only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connection<wbr>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>egress<wbr>Bytes<wbr>Transferred</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>express<wbr>Route<wbr>Circuit<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
(i.e. when `type` is `ExpressRoute`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>express<wbr>Route<wbr>Gateway<wbr>Bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding. This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ingress<wbr>Bytes<wbr>Transferred</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ipsec<wbr>Policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getgatewayconnectionipsecpolicy">Get<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>local<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when a Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>peer<wbr>Virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Guid</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>routing<wbr>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The routing weight.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
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
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>use<wbr>Policy<wbr>Based<wbr>Traffic<wbr>Selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtual<wbr>Network<wbr>Gateway<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection is created.
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
Express Route Circuit. This field is present only if the type is an
ExpressRoute connection.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connection_<wbr>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>egress_<wbr>bytes_<wbr>transferred</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>bgp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, BGP (Border Gateway Protocol) is enabled
for this connection.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>express_<wbr>route_<wbr>circuit_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Express Route Circuit
(i.e. when `type` is `ExpressRoute`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>express_<wbr>route_<wbr>gateway_<wbr>bypass</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, data packets will bypass ExpressRoute Gateway for data forwarding. This is only valid for ExpressRoute connections.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ingress_<wbr>bytes_<wbr>transferred</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ipsec_<wbr>policies</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getgatewayconnectionipsecpolicy">List[Get<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>local_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the local network gateway
when a Site-to-Site connection (i.e. when `type` is `IPsec`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location/region where the connection is
located.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>peer_<wbr>virtual_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the peer virtual
network gateway when a VNet-to-VNet connection (i.e. when `type`
is `Vnet2Vnet`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>guid</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>routing_<wbr>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The routing weight.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>shared_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The shared IPSec key. 
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
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>use_<wbr>policy_<wbr>based_<wbr>traffic_<wbr>selectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an `ipsec_policy` block.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>virtual_<wbr>network_<wbr>gateway_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network Gateway
in which the connection is created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Gateway<wbr>Connection<wbr>Ipsec<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetGatewayConnectionIpsecPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/network?tab=doc#GetGatewayConnectionIpsecPolicy">output</a> API doc for this type.
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

    <dt class="property-required"
            title="Required">
        <span>Sa<wbr>Datasize</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The IPSec SA payload size in KB. Must be at least
`1024` KB.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sa<wbr>Lifetime</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The IPSec SA lifetime in seconds. Must be at least
`300` seconds.
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

    <dt class="property-required"
            title="Required">
        <span>Sa<wbr>Datasize</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The IPSec SA payload size in KB. Must be at least
`1024` KB.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sa<wbr>Lifetime</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The IPSec SA lifetime in seconds. Must be at least
`300` seconds.
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

    <dt class="property-required"
            title="Required">
        <span>sa<wbr>Datasize</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The IPSec SA payload size in KB. Must be at least
`1024` KB.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sa<wbr>Lifetime</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The IPSec SA lifetime in seconds. Must be at least
`300` seconds.
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

    <dt class="property-required"
            title="Required">
        <span>sa<wbr>Datasize</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The IPSec SA payload size in KB. Must be at least
`1024` KB.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sa<wbr>Lifetime</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The IPSec SA lifetime in seconds. Must be at least
`300` seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







