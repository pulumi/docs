
---
title: "RouterPeer"
block_external_search_index: true
---

BGP information that must be configured into the routing stack to
establish BGP peering. This information must specify the peer ASN
and either the interface name, IP address, or peer IP address.
Please refer to RFC4273.


To get more information about RouterBgpPeer, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/routers)
* How-to Guides
    * [Google Cloud Router](https://cloud.google.com/router/docs/)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_router_bgp_peer.html.markdown.



## Create a RouterPeer Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#RouterPeer">RouterPeer</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#RouterPeerArgs">RouterPeerArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">RouterPeer</span><span class="p">(resource_name, opts=None, </span>advertise_mode=None<span class="p">, </span>advertised_groups=None<span class="p">, </span>advertised_ip_ranges=None<span class="p">, </span>advertised_route_priority=None<span class="p">, </span>interface=None<span class="p">, </span>name=None<span class="p">, </span>peer_asn=None<span class="p">, </span>peer_ip_address=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, </span>router=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewRouterPeer<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#RouterPeerArgs">RouterPeerArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#RouterPeer">RouterPeer</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.RouterPeer.html">RouterPeer</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.RouterPeerArgs.html">RouterPeerArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Advertise<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User-specified flag to indicate which mode to use for advertisement. Valid values of this enum field are: 'DEFAULT',
'CUSTOM'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Advertised<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}User-specified list of prefix groups to advertise in custom mode, which can take one of the following options: *
'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets. * 'ALL_VPC_SUBNETS': Advertises the
router's own VPC subnets. * 'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network. Note that this
field can only be populated if advertiseMode is 'CUSTOM' and overrides the list defined for the router (in the "bgp"
message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no
custom groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Advertised<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerpeeradvertisediprange">List&lt;Router<wbr>Peer<wbr>Advertised<wbr>Ip<wbr>Range<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if
advertiseMode is 'CUSTOM' and is advertised to all peers of the router. These IP ranges will be advertised in addition
to any specified groups. Leave this field blank to advertise no custom IP ranges.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Advertised<wbr>Route<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the
routes with the lowest priority value win.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the interface the BGP peer is associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of this BGP peer. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be
1-63 characters long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must
be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last
character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Peer<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Peer<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Region where the router and BgpPeer reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Router</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this BgpPeer will be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Advertise<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User-specified flag to indicate which mode to use for advertisement. Valid values of this enum field are: 'DEFAULT',
'CUSTOM'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Advertised<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}User-specified list of prefix groups to advertise in custom mode, which can take one of the following options: *
'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets. * 'ALL_VPC_SUBNETS': Advertises the
router's own VPC subnets. * 'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network. Note that this
field can only be populated if advertiseMode is 'CUSTOM' and overrides the list defined for the router (in the "bgp"
message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no
custom groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Advertised<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerpeeradvertisediprange">[]Router<wbr>Peer<wbr>Advertised<wbr>Ip<wbr>Range</a></span>
    </dt>
    <dd>{{% md %}}User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if
advertiseMode is 'CUSTOM' and is advertised to all peers of the router. These IP ranges will be advertised in addition
to any specified groups. Leave this field blank to advertise no custom IP ranges.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Advertised<wbr>Route<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the
routes with the lowest priority value win.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the interface the BGP peer is associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of this BGP peer. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be
1-63 characters long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must
be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last
character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Peer<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Peer<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Region where the router and BgpPeer reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Router</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this BgpPeer will be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>advertise<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User-specified flag to indicate which mode to use for advertisement. Valid values of this enum field are: 'DEFAULT',
'CUSTOM'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>advertised<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}User-specified list of prefix groups to advertise in custom mode, which can take one of the following options: *
'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets. * 'ALL_VPC_SUBNETS': Advertises the
router's own VPC subnets. * 'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network. Note that this
field can only be populated if advertiseMode is 'CUSTOM' and overrides the list defined for the router (in the "bgp"
message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no
custom groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>advertised<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerpeeradvertisediprange">Router<wbr>Peer<wbr>Advertised<wbr>Ip<wbr>Range[]?</a></span>
    </dt>
    <dd>{{% md %}}User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if
advertiseMode is 'CUSTOM' and is advertised to all peers of the router. These IP ranges will be advertised in addition
to any specified groups. Leave this field blank to advertise no custom IP ranges.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>advertised<wbr>Route<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the
routes with the lowest priority value win.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the interface the BGP peer is associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of this BGP peer. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be
1-63 characters long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must
be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last
character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>peer<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>peer<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Region where the router and BgpPeer reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>router</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this BgpPeer will be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>advertise_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User-specified flag to indicate which mode to use for advertisement. Valid values of this enum field are: 'DEFAULT',
'CUSTOM'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>advertised_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}User-specified list of prefix groups to advertise in custom mode, which can take one of the following options: *
'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets. * 'ALL_VPC_SUBNETS': Advertises the
router's own VPC subnets. * 'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network. Note that this
field can only be populated if advertiseMode is 'CUSTOM' and overrides the list defined for the router (in the "bgp"
message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no
custom groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>advertised_<wbr>ip_<wbr>ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerpeeradvertisediprange">List[Router<wbr>Peer<wbr>Advertised<wbr>Ip<wbr>Range]</a></span>
    </dt>
    <dd>{{% md %}}User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if
advertiseMode is 'CUSTOM' and is advertised to all peers of the router. These IP ranges will be advertised in addition
to any specified groups. Leave this field blank to advertise no custom IP ranges.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>advertised_<wbr>route_<wbr>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the
routes with the lowest priority value win.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the interface the BGP peer is associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of this BGP peer. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be
1-63 characters long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must
be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last
character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>peer_<wbr>asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>peer_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Region where the router and BgpPeer reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>router</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this BgpPeer will be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## RouterPeer Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Advertise<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User-specified flag to indicate which mode to use for advertisement. Valid values of this enum field are: 'DEFAULT',
'CUSTOM'
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Advertised<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}User-specified list of prefix groups to advertise in custom mode, which can take one of the following options: *
'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets. * 'ALL_VPC_SUBNETS': Advertises the
router's own VPC subnets. * 'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network. Note that this
field can only be populated if advertiseMode is 'CUSTOM' and overrides the list defined for the router (in the "bgp"
message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no
custom groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Advertised<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerpeeradvertisediprange">List&lt;Router<wbr>Peer<wbr>Advertised<wbr>Ip<wbr>Range&gt;?</a></span>
    </dt>
    <dd>{{% md %}}User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if
advertiseMode is 'CUSTOM' and is advertised to all peers of the router. These IP ranges will be advertised in addition
to any specified groups. Leave this field blank to advertise no custom IP ranges.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Advertised<wbr>Route<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the
routes with the lowest priority value win.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the interface the BGP peer is associated with.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}IP address of the interface inside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The resource that configures and manages this BGP peer. * 'MANAGED_BY_USER' is the default value and can be managed by
you or other users * 'MANAGED_BY_ATTACHMENT' is a BGP peer that is configured and managed by Cloud Interconnect,
specifically by an InterconnectAttachment of type PARTNER. Google automatically creates, updates, and deletes this type
of BGP peer when the PARTNER InterconnectAttachment is created, updated, or deleted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of this BGP peer. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be
1-63 characters long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must
be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last
character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Peer<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Peer<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region where the router and BgpPeer reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Router</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this BgpPeer will be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Advertise<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User-specified flag to indicate which mode to use for advertisement. Valid values of this enum field are: 'DEFAULT',
'CUSTOM'
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Advertised<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}User-specified list of prefix groups to advertise in custom mode, which can take one of the following options: *
'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets. * 'ALL_VPC_SUBNETS': Advertises the
router's own VPC subnets. * 'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network. Note that this
field can only be populated if advertiseMode is 'CUSTOM' and overrides the list defined for the router (in the "bgp"
message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no
custom groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Advertised<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerpeeradvertisediprange">[]Router<wbr>Peer<wbr>Advertised<wbr>Ip<wbr>Range</a></span>
    </dt>
    <dd>{{% md %}}User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if
advertiseMode is 'CUSTOM' and is advertised to all peers of the router. These IP ranges will be advertised in addition
to any specified groups. Leave this field blank to advertise no custom IP ranges.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Advertised<wbr>Route<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the
routes with the lowest priority value win.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the interface the BGP peer is associated with.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}IP address of the interface inside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The resource that configures and manages this BGP peer. * 'MANAGED_BY_USER' is the default value and can be managed by
you or other users * 'MANAGED_BY_ATTACHMENT' is a BGP peer that is configured and managed by Cloud Interconnect,
specifically by an InterconnectAttachment of type PARTNER. Google automatically creates, updates, and deletes this type
of BGP peer when the PARTNER InterconnectAttachment is created, updated, or deleted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of this BGP peer. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be
1-63 characters long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must
be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last
character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Peer<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Peer<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region where the router and BgpPeer reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Router</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this BgpPeer will be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>advertise<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User-specified flag to indicate which mode to use for advertisement. Valid values of this enum field are: 'DEFAULT',
'CUSTOM'
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>advertised<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}User-specified list of prefix groups to advertise in custom mode, which can take one of the following options: *
'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets. * 'ALL_VPC_SUBNETS': Advertises the
router's own VPC subnets. * 'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network. Note that this
field can only be populated if advertiseMode is 'CUSTOM' and overrides the list defined for the router (in the "bgp"
message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no
custom groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>advertised<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerpeeradvertisediprange">Router<wbr>Peer<wbr>Advertised<wbr>Ip<wbr>Range[]?</a></span>
    </dt>
    <dd>{{% md %}}User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if
advertiseMode is 'CUSTOM' and is advertised to all peers of the router. These IP ranges will be advertised in addition
to any specified groups. Leave this field blank to advertise no custom IP ranges.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>advertised<wbr>Route<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the
routes with the lowest priority value win.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the interface the BGP peer is associated with.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}IP address of the interface inside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The resource that configures and manages this BGP peer. * 'MANAGED_BY_USER' is the default value and can be managed by
you or other users * 'MANAGED_BY_ATTACHMENT' is a BGP peer that is configured and managed by Cloud Interconnect,
specifically by an InterconnectAttachment of type PARTNER. Google automatically creates, updates, and deletes this type
of BGP peer when the PARTNER InterconnectAttachment is created, updated, or deleted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of this BGP peer. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be
1-63 characters long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must
be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last
character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>peer<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>peer<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region where the router and BgpPeer reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>router</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this BgpPeer will be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>advertise_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User-specified flag to indicate which mode to use for advertisement. Valid values of this enum field are: 'DEFAULT',
'CUSTOM'
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>advertised_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}User-specified list of prefix groups to advertise in custom mode, which can take one of the following options: *
'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets. * 'ALL_VPC_SUBNETS': Advertises the
router's own VPC subnets. * 'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network. Note that this
field can only be populated if advertiseMode is 'CUSTOM' and overrides the list defined for the router (in the "bgp"
message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no
custom groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>advertised_<wbr>ip_<wbr>ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerpeeradvertisediprange">List[Router<wbr>Peer<wbr>Advertised<wbr>Ip<wbr>Range]</a></span>
    </dt>
    <dd>{{% md %}}User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if
advertiseMode is 'CUSTOM' and is advertised to all peers of the router. These IP ranges will be advertised in addition
to any specified groups. Leave this field blank to advertise no custom IP ranges.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>advertised_<wbr>route_<wbr>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the
routes with the lowest priority value win.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the interface the BGP peer is associated with.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IP address of the interface inside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The resource that configures and manages this BGP peer. * 'MANAGED_BY_USER' is the default value and can be managed by
you or other users * 'MANAGED_BY_ATTACHMENT' is a BGP peer that is configured and managed by Cloud Interconnect,
specifically by an InterconnectAttachment of type PARTNER. Google automatically creates, updates, and deletes this type
of BGP peer when the PARTNER InterconnectAttachment is created, updated, or deleted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of this BGP peer. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be
1-63 characters long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must
be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last
character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>peer_<wbr>asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>peer_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Region where the router and BgpPeer reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>router</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this BgpPeer will be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing RouterPeer Resource

Get an existing RouterPeer resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#RouterPeerState">RouterPeerState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#RouterPeer">RouterPeer</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>advertise_mode=None<span class="p">, </span>advertised_groups=None<span class="p">, </span>advertised_ip_ranges=None<span class="p">, </span>advertised_route_priority=None<span class="p">, </span>interface=None<span class="p">, </span>ip_address=None<span class="p">, </span>management_type=None<span class="p">, </span>name=None<span class="p">, </span>peer_asn=None<span class="p">, </span>peer_ip_address=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, </span>router=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetRouterPeer<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#RouterPeerState">RouterPeerState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#RouterPeer">RouterPeer</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.RouterPeer.html">RouterPeer</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.RouterPeerState.html">RouterPeerState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Advertise<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User-specified flag to indicate which mode to use for advertisement. Valid values of this enum field are: 'DEFAULT',
'CUSTOM'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Advertised<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}User-specified list of prefix groups to advertise in custom mode, which can take one of the following options: *
'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets. * 'ALL_VPC_SUBNETS': Advertises the
router's own VPC subnets. * 'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network. Note that this
field can only be populated if advertiseMode is 'CUSTOM' and overrides the list defined for the router (in the "bgp"
message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no
custom groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Advertised<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerpeeradvertisediprange">List&lt;Router<wbr>Peer<wbr>Advertised<wbr>Ip<wbr>Range<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if
advertiseMode is 'CUSTOM' and is advertised to all peers of the router. These IP ranges will be advertised in addition
to any specified groups. Leave this field blank to advertise no custom IP ranges.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Advertised<wbr>Route<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the
routes with the lowest priority value win.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the interface the BGP peer is associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address of the interface inside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The resource that configures and manages this BGP peer. * 'MANAGED_BY_USER' is the default value and can be managed by
you or other users * 'MANAGED_BY_ATTACHMENT' is a BGP peer that is configured and managed by Cloud Interconnect,
specifically by an InterconnectAttachment of type PARTNER. Google automatically creates, updates, and deletes this type
of BGP peer when the PARTNER InterconnectAttachment is created, updated, or deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of this BGP peer. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be
1-63 characters long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must
be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last
character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peer<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peer<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Region where the router and BgpPeer reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Router</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this BgpPeer will be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Advertise<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}User-specified flag to indicate which mode to use for advertisement. Valid values of this enum field are: 'DEFAULT',
'CUSTOM'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Advertised<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}User-specified list of prefix groups to advertise in custom mode, which can take one of the following options: *
'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets. * 'ALL_VPC_SUBNETS': Advertises the
router's own VPC subnets. * 'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network. Note that this
field can only be populated if advertiseMode is 'CUSTOM' and overrides the list defined for the router (in the "bgp"
message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no
custom groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Advertised<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerpeeradvertisediprange">[]Router<wbr>Peer<wbr>Advertised<wbr>Ip<wbr>Range</a></span>
    </dt>
    <dd>{{% md %}}User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if
advertiseMode is 'CUSTOM' and is advertised to all peers of the router. These IP ranges will be advertised in addition
to any specified groups. Leave this field blank to advertise no custom IP ranges.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Advertised<wbr>Route<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the
routes with the lowest priority value win.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the interface the BGP peer is associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}IP address of the interface inside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The resource that configures and manages this BGP peer. * 'MANAGED_BY_USER' is the default value and can be managed by
you or other users * 'MANAGED_BY_ATTACHMENT' is a BGP peer that is configured and managed by Cloud Interconnect,
specifically by an InterconnectAttachment of type PARTNER. Google automatically creates, updates, and deletes this type
of BGP peer when the PARTNER InterconnectAttachment is created, updated, or deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of this BGP peer. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be
1-63 characters long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must
be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last
character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peer<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peer<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Region where the router and BgpPeer reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Router</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this BgpPeer will be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>advertise<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}User-specified flag to indicate which mode to use for advertisement. Valid values of this enum field are: 'DEFAULT',
'CUSTOM'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>advertised<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}User-specified list of prefix groups to advertise in custom mode, which can take one of the following options: *
'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets. * 'ALL_VPC_SUBNETS': Advertises the
router's own VPC subnets. * 'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network. Note that this
field can only be populated if advertiseMode is 'CUSTOM' and overrides the list defined for the router (in the "bgp"
message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no
custom groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>advertised<wbr>Ip<wbr>Ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerpeeradvertisediprange">Router<wbr>Peer<wbr>Advertised<wbr>Ip<wbr>Range[]?</a></span>
    </dt>
    <dd>{{% md %}}User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if
advertiseMode is 'CUSTOM' and is advertised to all peers of the router. These IP ranges will be advertised in addition
to any specified groups. Leave this field blank to advertise no custom IP ranges.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>advertised<wbr>Route<wbr>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the
routes with the lowest priority value win.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the interface the BGP peer is associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address of the interface inside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The resource that configures and manages this BGP peer. * 'MANAGED_BY_USER' is the default value and can be managed by
you or other users * 'MANAGED_BY_ATTACHMENT' is a BGP peer that is configured and managed by Cloud Interconnect,
specifically by an InterconnectAttachment of type PARTNER. Google automatically creates, updates, and deletes this type
of BGP peer when the PARTNER InterconnectAttachment is created, updated, or deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of this BGP peer. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be
1-63 characters long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must
be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last
character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peer<wbr>Asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peer<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Region where the router and BgpPeer reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>router</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this BgpPeer will be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>advertise_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User-specified flag to indicate which mode to use for advertisement. Valid values of this enum field are: 'DEFAULT',
'CUSTOM'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>advertised_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}User-specified list of prefix groups to advertise in custom mode, which can take one of the following options: *
'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets. * 'ALL_VPC_SUBNETS': Advertises the
router's own VPC subnets. * 'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network. Note that this
field can only be populated if advertiseMode is 'CUSTOM' and overrides the list defined for the router (in the "bgp"
message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no
custom groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>advertised_<wbr>ip_<wbr>ranges</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routerpeeradvertisediprange">List[Router<wbr>Peer<wbr>Advertised<wbr>Ip<wbr>Range]</a></span>
    </dt>
    <dd>{{% md %}}User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if
advertiseMode is 'CUSTOM' and is advertised to all peers of the router. These IP ranges will be advertised in addition
to any specified groups. Leave this field blank to advertise no custom IP ranges.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>advertised_<wbr>route_<wbr>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the
routes with the lowest priority value win.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>interface</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the interface the BGP peer is associated with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IP address of the interface inside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The resource that configures and manages this BGP peer. * 'MANAGED_BY_USER' is the default value and can be managed by
you or other users * 'MANAGED_BY_ATTACHMENT' is a BGP peer that is configured and managed by Cloud Interconnect,
specifically by an InterconnectAttachment of type PARTNER. Google automatically creates, updates, and deletes this type
of BGP peer when the PARTNER InterconnectAttachment is created, updated, or deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of this BGP peer. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be
1-63 characters long and match the regular expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must
be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last
character, which cannot be a dash.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peer_<wbr>asn</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peer_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Region where the router and BgpPeer reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>router</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this BgpPeer will be configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Router<wbr>Peer<wbr>Advertised<wbr>Ip<wbr>Range</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#RouterPeerAdvertisedIpRange">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#RouterPeerAdvertisedIpRange">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#RouterPeerAdvertisedIpRangeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#RouterPeerAdvertisedIpRangeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>range</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
