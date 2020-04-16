
---
title: "GetExpressRouteCircuit"
block_external_search_index: true
---



Use this data source to access information about an existing ExpressRoute circuit.

{{% examples %}}
{{% /examples %}}





## Using GetExpressRouteCircuit

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getExpressRouteCircuit<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#GetExpressRouteCircuitArgs">GetExpressRouteCircuitArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/network/#GetExpressRouteCircuitResult">GetExpressRouteCircuitResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_express_route_circuit(</span>name=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupExpressRouteCircuit<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/network?tab=doc#LookupExpressRouteCircuitArgs">LookupExpressRouteCircuitArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/network?tab=doc#LookupExpressRouteCircuitResult">LookupExpressRouteCircuitResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetExpressRouteCircuit </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.GetExpressRouteCircuitResult.html">GetExpressRouteCircuitResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Network.GetExpressRouteCircuitArgs.html">GetExpressRouteCircuitArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the ExpressRoute circuit.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the ExpressRoute circuit exists.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the ExpressRoute circuit.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the ExpressRoute circuit exists.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the ExpressRoute circuit.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the ExpressRoute circuit exists.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the ExpressRoute circuit.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the ExpressRoute circuit exists.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetExpressRouteCircuit Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Azure location where the ExpressRoute circuit exists
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Peerings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getexpressroutecircuitpeering">List&lt;Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Peering&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `peerings` block for the ExpressRoute circuit as documented below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The string needed by the service provider to provision the ExpressRoute circuit.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Provider<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getexpressroutecircuitserviceproviderproperty">List&lt;Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Service<wbr>Provider<wbr>Property&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `service_provider_properties` block for the ExpressRoute circuit as documented below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Provider<wbr>Provisioning<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getexpressroutecircuitsku">Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Sku</a></span>
    </dt>
    <dd>{{% md %}}A `sku` block for the ExpressRoute circuit as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Azure location where the ExpressRoute circuit exists
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Peerings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getexpressroutecircuitpeering">[]Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Peering<wbr>Type</a></span>
    </dt>
    <dd>{{% md %}}A `peerings` block for the ExpressRoute circuit as documented below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The string needed by the service provider to provision the ExpressRoute circuit.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Provider<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getexpressroutecircuitserviceproviderproperty">[]Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Service<wbr>Provider<wbr>Property</a></span>
    </dt>
    <dd>{{% md %}}A `service_provider_properties` block for the ExpressRoute circuit as documented below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Provider<wbr>Provisioning<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sku</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getexpressroutecircuitsku">Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Sku</a></span>
    </dt>
    <dd>{{% md %}}A `sku` block for the ExpressRoute circuit as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Azure location where the ExpressRoute circuit exists
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>peerings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getexpressroutecircuitpeering">Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Peering[]</a></span>
    </dt>
    <dd>{{% md %}}A `peerings` block for the ExpressRoute circuit as documented below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The string needed by the service provider to provision the ExpressRoute circuit.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service<wbr>Provider<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getexpressroutecircuitserviceproviderproperty">Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Service<wbr>Provider<wbr>Property[]</a></span>
    </dt>
    <dd>{{% md %}}A `service_provider_properties` block for the ExpressRoute circuit as documented below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service<wbr>Provider<wbr>Provisioning<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getexpressroutecircuitsku">Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Sku</a></span>
    </dt>
    <dd>{{% md %}}A `sku` block for the ExpressRoute circuit as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Azure location where the ExpressRoute circuit exists
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>peerings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getexpressroutecircuitpeering">List[Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Peering]</a></span>
    </dt>
    <dd>{{% md %}}A `peerings` block for the ExpressRoute circuit as documented below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The string needed by the service provider to provision the ExpressRoute circuit.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service_<wbr>provider_<wbr>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getexpressroutecircuitserviceproviderproperty">List[Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Service<wbr>Provider<wbr>Property]</a></span>
    </dt>
    <dd>{{% md %}}A `service_provider_properties` block for the ExpressRoute circuit as documented below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service_<wbr>provider_<wbr>provisioning_<wbr>state</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are "NotProvisioned", "Provisioning", "Provisioned", and "Deprovisioning".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sku</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getexpressroutecircuitsku">Dict[Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Sku]</a></span>
    </dt>
    <dd>{{% md %}}A `sku` block for the ExpressRoute circuit as documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Peering</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetExpressRouteCircuitPeering">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/network?tab=doc#GetExpressRouteCircuitPeeringType">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Azure<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The Either a 16-bit or a 32-bit ASN for Azure.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Peer<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The Either a 16-bit or a 32-bit ASN. Can either be public or private.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Peering<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Primary<wbr>Peer<wbr>Address<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A `/30` subnet for the primary link.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Secondary<wbr>Peer<wbr>Address<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A `/30` subnet for the secondary link.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The shared key. Can be a maximum of 25 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}A valid VLAN ID to establish this peering on.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Azure<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The Either a 16-bit or a 32-bit ASN for Azure.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Peer<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The Either a 16-bit or a 32-bit ASN. Can either be public or private.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Peering<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Primary<wbr>Peer<wbr>Address<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A `/30` subnet for the primary link.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Secondary<wbr>Peer<wbr>Address<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A `/30` subnet for the secondary link.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The shared key. Can be a maximum of 25 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}A valid VLAN ID to establish this peering on.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>azure<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The Either a 16-bit or a 32-bit ASN for Azure.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>peer<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The Either a 16-bit or a 32-bit ASN. Can either be public or private.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>peering<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>primary<wbr>Peer<wbr>Address<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A `/30` subnet for the primary link.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>secondary<wbr>Peer<wbr>Address<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A `/30` subnet for the secondary link.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>shared<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The shared key. Can be a maximum of 25 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vlan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}A valid VLAN ID to establish this peering on.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>azure_<wbr>asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The Either a 16-bit or a 32-bit ASN for Azure.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>peer_<wbr>asn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The Either a 16-bit or a 32-bit ASN. Can either be public or private.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>peering_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of the ExpressRoute Circuit Peering. Acceptable values include `AzurePrivatePeering`, `AzurePublicPeering` and `MicrosoftPeering`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>primary_<wbr>peer_<wbr>address_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A `/30` subnet for the primary link.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>secondary_<wbr>peer_<wbr>address_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A `/30` subnet for the secondary link.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>shared_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The shared key. Can be a maximum of 25 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vlan_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}A valid VLAN ID to establish this peering on.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Service<wbr>Provider<wbr>Property</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetExpressRouteCircuitServiceProviderProperty">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/network?tab=doc#GetExpressRouteCircuitServiceProviderProperty">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Bandwidth<wbr>In<wbr>Mbps</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The bandwidth in Mbps of the ExpressRoute circuit.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Peering<wbr>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the peering location and **not** the Azure resource location.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service<wbr>Provider<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the ExpressRoute Service Provider.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Bandwidth<wbr>In<wbr>Mbps</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The bandwidth in Mbps of the ExpressRoute circuit.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Peering<wbr>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the peering location and **not** the Azure resource location.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service<wbr>Provider<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the ExpressRoute Service Provider.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>bandwidth<wbr>In<wbr>Mbps</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The bandwidth in Mbps of the ExpressRoute circuit.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>peering<wbr>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the peering location and **not** the Azure resource location.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service<wbr>Provider<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the ExpressRoute Service Provider.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>bandwidth_<wbr>in_<wbr>mbps</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The bandwidth in Mbps of the ExpressRoute circuit.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>peering_<wbr>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the peering location and **not** the Azure resource location.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service_<wbr>provider_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the ExpressRoute Service Provider.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Express<wbr>Route<wbr>Circuit<wbr>Sku</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetExpressRouteCircuitSku">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/network?tab=doc#GetExpressRouteCircuitSku">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Family</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The billing mode for bandwidth. Possible values are `MeteredData` or `UnlimitedData`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The service tier. Possible values are `Basic`, `Local`, `Standard` or `Premium`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Family</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The billing mode for bandwidth. Possible values are `MeteredData` or `UnlimitedData`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The service tier. Possible values are `Basic`, `Local`, `Standard` or `Premium`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>family</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The billing mode for bandwidth. Possible values are `MeteredData` or `UnlimitedData`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The service tier. Possible values are `Basic`, `Local`, `Standard` or `Premium`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>family</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The billing mode for bandwidth. Possible values are `MeteredData` or `UnlimitedData`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The service tier. Possible values are `Basic`, `Local`, `Standard` or `Premium`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







