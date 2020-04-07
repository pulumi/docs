
---
title: "Router"
block_external_search_index: true
---



Manages a V2 router resource within OpenStack.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as openstack from "@pulumi/openstack";

const router1 = new openstack.networking.Router("router_1", {
    adminStateUp: true,
    externalNetworkId: "f67f0d72-0ddf-11e4-9d95-e1f29f417e2f",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/networking_router_v2.html.markdown.



## Create a Router Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#Router">Router</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#RouterArgs">RouterArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Router</span><span class="p">(resource_name, opts=None, </span>admin_state_up=None<span class="p">, </span>availability_zone_hints=None<span class="p">, </span>description=None<span class="p">, </span>distributed=None<span class="p">, </span>enable_snat=None<span class="p">, </span>external_fixed_ips=None<span class="p">, </span>external_gateway=None<span class="p">, </span>external_network_id=None<span class="p">, </span>name=None<span class="p">, </span>region=None<span class="p">, </span>tags=None<span class="p">, </span>tenant_id=None<span class="p">, </span>value_specs=None<span class="p">, </span>vendor_options=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewRouter<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#RouterArgs">RouterArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#Router">Router</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.Router.html">Router</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.RouterArgs.html">RouterArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Distributed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Snat</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.
Setting this value **requires** an **ext-gw-mode** extension to be enabled
in OpenStack Neutron.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Fixed<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerexternalfixedip">List&lt;Router<wbr>External<wbr>Fixed<wbr>Ip<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>External<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use external_network_id instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for the router. Changing this
updates the `name` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of additional driver-specific options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vendor<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routervendoroptions">Router<wbr>Vendor<wbr>Options<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Map of additional vendor-specific options.
Supported options are described below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Distributed</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Snat</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.
Setting this value **requires** an **ext-gw-mode** extension to be enabled
in OpenStack Neutron.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Fixed<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerexternalfixedip">[]Router<wbr>External<wbr>Fixed<wbr>Ip</a></span>
    </dt>
    <dd>{{% md %}}An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>External<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use external_network_id instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unique name for the router. Changing this
updates the `name` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of additional driver-specific options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vendor<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routervendoroptions">*Router<wbr>Vendor<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Map of additional vendor-specific options.
Supported options are described below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>distributed</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Snat</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.
Setting this value **requires** an **ext-gw-mode** extension to be enabled
in OpenStack Neutron.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external<wbr>Fixed<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerexternalfixedip">Router<wbr>External<wbr>Fixed<wbr>Ip[]?</a></span>
    </dt>
    <dd>{{% md %}}An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>external<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use external_network_id instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>external<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for the router. Changing this
updates the `name` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of additional driver-specific options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vendor<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routervendoroptions">Router<wbr>Vendor<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}Map of additional vendor-specific options.
Supported options are described below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>state_<wbr>up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability_<wbr>zone_<wbr>hints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>distributed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>snat</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.
Setting this value **requires** an **ext-gw-mode** extension to be enabled
in OpenStack Neutron.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external_<wbr>fixed_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerexternalfixedip">List[Router<wbr>External<wbr>Fixed<wbr>Ip]</a></span>
    </dt>
    <dd>{{% md %}}An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>external_<wbr>gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use external_network_id instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>external_<wbr>network_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for the router. Changing this
updates the `name` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value_<wbr>specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of additional driver-specific options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vendor_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routervendoroptions">Dict[Router<wbr>Vendor<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}Map of additional vendor-specific options.
Supported options are described below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Router Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>All<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the router, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Distributed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Snat</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.
Setting this value **requires** an **ext-gw-mode** extension to be enabled
in OpenStack Neutron.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>External<wbr>Fixed<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerexternalfixedip">List&lt;Router<wbr>External<wbr>Fixed<wbr>Ip&gt;</a></span>
    </dt>
    <dd>{{% md %}}An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>External<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use external_network_id instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>External<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the router. Changing this
updates the `name` of an existing router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of additional driver-specific options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vendor<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routervendoroptions">Router<wbr>Vendor<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}Map of additional vendor-specific options.
Supported options are described below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>All<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the router, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Distributed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Snat</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.
Setting this value **requires** an **ext-gw-mode** extension to be enabled
in OpenStack Neutron.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>External<wbr>Fixed<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerexternalfixedip">[]Router<wbr>External<wbr>Fixed<wbr>Ip</a></span>
    </dt>
    <dd>{{% md %}}An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>External<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use external_network_id instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>External<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the router. Changing this
updates the `name` of an existing router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of additional driver-specific options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vendor<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routervendoroptions">*Router<wbr>Vendor<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Map of additional vendor-specific options.
Supported options are described below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>all<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the router, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>distributed</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Snat</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.
Setting this value **requires** an **ext-gw-mode** extension to be enabled
in OpenStack Neutron.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>external<wbr>Fixed<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerexternalfixedip">Router<wbr>External<wbr>Fixed<wbr>Ip[]</a></span>
    </dt>
    <dd>{{% md %}}An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>external<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use external_network_id instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>external<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the router. Changing this
updates the `name` of an existing router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of additional driver-specific options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vendor<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routervendoroptions">Router<wbr>Vendor<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}Map of additional vendor-specific options.
Supported options are described below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>admin_<wbr>state_<wbr>up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>all_<wbr>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the router, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>availability_<wbr>zone_<wbr>hints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>distributed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>snat</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.
Setting this value **requires** an **ext-gw-mode** extension to be enabled
in OpenStack Neutron.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>external_<wbr>fixed_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerexternalfixedip">List[Router<wbr>External<wbr>Fixed<wbr>Ip]</a></span>
    </dt>
    <dd>{{% md %}}An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>external_<wbr>gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use external_network_id instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>external_<wbr>network_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for the router. Changing this
updates the `name` of an existing router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>value_<wbr>specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of additional driver-specific options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vendor_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routervendoroptions">Dict[Router<wbr>Vendor<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}Map of additional vendor-specific options.
Supported options are described below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Router Resource

Get an existing Router resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#RouterState">RouterState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#Router">Router</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>admin_state_up=None<span class="p">, </span>all_tags=None<span class="p">, </span>availability_zone_hints=None<span class="p">, </span>description=None<span class="p">, </span>distributed=None<span class="p">, </span>enable_snat=None<span class="p">, </span>external_fixed_ips=None<span class="p">, </span>external_gateway=None<span class="p">, </span>external_network_id=None<span class="p">, </span>name=None<span class="p">, </span>region=None<span class="p">, </span>tags=None<span class="p">, </span>tenant_id=None<span class="p">, </span>value_specs=None<span class="p">, </span>vendor_options=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetRouter<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#RouterState">RouterState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#Router">Router</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.Router.html">Router</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.RouterState.html">RouterState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>All<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the router, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Distributed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Snat</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.
Setting this value **requires** an **ext-gw-mode** extension to be enabled
in OpenStack Neutron.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Fixed<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerexternalfixedip">List&lt;Router<wbr>External<wbr>Fixed<wbr>Ip<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>External<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use external_network_id instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for the router. Changing this
updates the `name` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of additional driver-specific options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vendor<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routervendoroptions">Router<wbr>Vendor<wbr>Options<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Map of additional vendor-specific options.
Supported options are described below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>All<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the router, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Distributed</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Snat</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.
Setting this value **requires** an **ext-gw-mode** extension to be enabled
in OpenStack Neutron.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Fixed<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerexternalfixedip">[]Router<wbr>External<wbr>Fixed<wbr>Ip</a></span>
    </dt>
    <dd>{{% md %}}An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>External<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use external_network_id instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unique name for the router. Changing this
updates the `name` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of additional driver-specific options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vendor<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routervendoroptions">*Router<wbr>Vendor<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Map of additional vendor-specific options.
Supported options are described below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin<wbr>State<wbr>Up</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>all<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the router, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability<wbr>Zone<wbr>Hints</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>distributed</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Snat</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.
Setting this value **requires** an **ext-gw-mode** extension to be enabled
in OpenStack Neutron.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external<wbr>Fixed<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerexternalfixedip">Router<wbr>External<wbr>Fixed<wbr>Ip[]?</a></span>
    </dt>
    <dd>{{% md %}}An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>external<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use external_network_id instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>external<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for the router. Changing this
updates the `name` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of additional driver-specific options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vendor<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routervendoroptions">Router<wbr>Vendor<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}Map of additional vendor-specific options.
Supported options are described below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>admin_<wbr>state_<wbr>up</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Administrative up/down status for the router
(must be "true" or "false" if provided). Changing this updates the
`admin_state_up` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>all_<wbr>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The collection of tags assigned on the router, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability_<wbr>zone_<wbr>hints</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>distributed</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>snat</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable Source NAT for the router. Valid values are
"true" or "false". An `external_network_id` has to be set in order to
set this property. Changing this updates the `enable_snat` of the router.
Setting this value **requires** an **ext-gw-mode** extension to be enabled
in OpenStack Neutron.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external_<wbr>fixed_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerexternalfixedip">List[Router<wbr>External<wbr>Fixed<wbr>Ip]</a></span>
    </dt>
    <dd>{{% md %}}An external fixed IP for the router. This
can be repeated. The structure is described below. An `external_network_id`
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>external_<wbr>gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use external_network_id instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>external_<wbr>network_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for the router. Changing this
updates the `name` of an existing router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`region` argument of the provider is used. Changing this creates a new
router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value_<wbr>specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of additional driver-specific options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vendor_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routervendoroptions">Dict[Router<wbr>Vendor<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}Map of additional vendor-specific options.
Supported options are described below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Router<wbr>External<wbr>Fixed<wbr>Ip</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/input/#RouterExternalFixedIp">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/output/#RouterExternalFixedIp">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#RouterExternalFixedIpArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#RouterExternalFixedIpOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address to set on the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Subnet in which the fixed IP belongs to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IP address to set on the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Subnet in which the fixed IP belongs to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address to set on the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Subnet in which the fixed IP belongs to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP address to set on the router.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Subnet in which the fixed IP belongs to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Router<wbr>Vendor<wbr>Options</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/input/#RouterVendorOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/output/#RouterVendorOptions">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#RouterVendorOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#RouterVendorOptionsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Set<wbr>Router<wbr>Gateway<wbr>After<wbr>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean to control whether
the Router gateway is assigned during creation or updated after creation.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Set<wbr>Router<wbr>Gateway<wbr>After<wbr>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean to control whether
the Router gateway is assigned during creation or updated after creation.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>set<wbr>Router<wbr>Gateway<wbr>After<wbr>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean to control whether
the Router gateway is assigned during creation or updated after creation.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>set<wbr>Router<wbr>Gateway<wbr>After<wbr>Create</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean to control whether
the Router gateway is assigned during creation or updated after creation.
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

