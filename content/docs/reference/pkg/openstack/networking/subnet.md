
---
title: "Subnet"
block_external_search_index: true
---



Manages a V2 Neutron subnet resource within OpenStack.

> This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/networking_subnet_v2.html.markdown.



## Create a Subnet Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#Subnet">Subnet</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#SubnetArgs">SubnetArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Subnet</span><span class="p">(resource_name, opts=None, </span>allocation_pools=None<span class="p">, </span>allocation_pools_collection=None<span class="p">, </span>cidr=None<span class="p">, </span>description=None<span class="p">, </span>dns_nameservers=None<span class="p">, </span>enable_dhcp=None<span class="p">, </span>gateway_ip=None<span class="p">, </span>host_routes=None<span class="p">, </span>ip_version=None<span class="p">, </span>ipv6_address_mode=None<span class="p">, </span>ipv6_ra_mode=None<span class="p">, </span>name=None<span class="p">, </span>network_id=None<span class="p">, </span>no_gateway=None<span class="p">, </span>prefix_length=None<span class="p">, </span>region=None<span class="p">, </span>subnetpool_id=None<span class="p">, </span>tags=None<span class="p">, </span>tenant_id=None<span class="p">, </span>value_specs=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewSubnet<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#SubnetArgs">SubnetArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#Subnet">Subnet</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.Subnet.html">Subnet</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.SubnetArgs.html">SubnetArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Allocation<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpool">List&lt;Subnet<wbr>Allocation<wbr>Pool<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
`allocation_pool` blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The `allocation_pool` block is documented below.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Allocation<wbr>Pools<wbr>Collection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpoolscollection">List&lt;Subnet<wbr>Allocation<wbr>Pools<wbr>Collection<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}
A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The `allocation_pools` block is documented below.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use allocation_pool instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the subnet. Changing this
updates the name of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gateway<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Host<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnethostroute">List&lt;Subnet<wbr>Host<wbr>Route<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}(**Deprecated** - use `openstack.networking.SubnetRoute`
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use openstack_networking_subnet_route_v2 instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this creates a
new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Address<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Ra<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the subnet. Changing this updates the name of
the existing subnet.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of the parent network. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Prefix<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetpool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the subnetpool associated with the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allocation<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpool">[]Subnet<wbr>Allocation<wbr>Pool</a></span>
    </dt>
    <dd>{{% md %}}A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
`allocation_pool` blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The `allocation_pool` block is documented below.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Allocation<wbr>Pools<wbr>Collection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpoolscollection">[]Subnet<wbr>Allocation<wbr>Pools<wbr>Collection</a></span>
    </dt>
    <dd>{{% md %}}
A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The `allocation_pools` block is documented below.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use allocation_pool instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the subnet. Changing this
updates the name of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gateway<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Host<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnethostroute">[]Subnet<wbr>Host<wbr>Route</a></span>
    </dt>
    <dd>{{% md %}}(**Deprecated** - use `openstack.networking.SubnetRoute`
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use openstack_networking_subnet_route_v2 instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this creates a
new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Address<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Ra<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the subnet. Changing this updates the name of
the existing subnet.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of the parent network. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Prefix<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetpool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the subnetpool associated with the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.
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
        <span>allocation<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpool">Subnet<wbr>Allocation<wbr>Pool[]?</a></span>
    </dt>
    <dd>{{% md %}}A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
`allocation_pool` blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The `allocation_pool` block is documented below.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>allocation<wbr>Pools<wbr>Collection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpoolscollection">Subnet<wbr>Allocation<wbr>Pools<wbr>Collection[]?</a></span>
    </dt>
    <dd>{{% md %}}
A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The `allocation_pools` block is documented below.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use allocation_pool instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the subnet. Changing this
updates the name of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gateway<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>host<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnethostroute">Subnet<wbr>Host<wbr>Route[]?</a></span>
    </dt>
    <dd>{{% md %}}(**Deprecated** - use `openstack.networking.SubnetRoute`
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use openstack_networking_subnet_route_v2 instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this creates a
new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6Address<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6Ra<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the subnet. Changing this updates the name of
the existing subnet.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of the parent network. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>prefix<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetpool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the subnetpool associated with the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allocation_<wbr>pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpool">List[Subnet<wbr>Allocation<wbr>Pool]</a></span>
    </dt>
    <dd>{{% md %}}A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
`allocation_pool` blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The `allocation_pool` block is documented below.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>allocation_<wbr>pools_<wbr>collection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpoolscollection">List[Subnet<wbr>Allocation<wbr>Pools<wbr>Collection]</a></span>
    </dt>
    <dd>{{% md %}}
A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The `allocation_pools` block is documented below.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use allocation_pool instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the subnet. Changing this
updates the name of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns_<wbr>nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gateway_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>host_<wbr>routes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnethostroute">List[Subnet<wbr>Host<wbr>Route]</a></span>
    </dt>
    <dd>{{% md %}}(**Deprecated** - use `openstack.networking.SubnetRoute`
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use openstack_networking_subnet_route_v2 instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this creates a
new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6_<wbr>address_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6_<wbr>ra_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the subnet. Changing this updates the name of
the existing subnet.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UUID of the parent network. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no_<wbr>gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>prefix_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetpool_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the subnetpool associated with the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.
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







## Subnet Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>All<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The collection of ags assigned on the subnet, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allocation<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpool">List&lt;Subnet<wbr>Allocation<wbr>Pool&gt;</a></span>
    </dt>
    <dd>{{% md %}}A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
`allocation_pool` blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The `allocation_pool` block is documented below.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Allocation<wbr>Pools<wbr>Collection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpoolscollection">List&lt;Subnet<wbr>Allocation<wbr>Pools<wbr>Collection&gt;</a></span>
    </dt>
    <dd>{{% md %}}
A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The `allocation_pools` block is documented below.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use allocation_pool instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the subnet. Changing this
updates the name of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dns<wbr>Nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Gateway<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Host<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnethostroute">List&lt;Subnet<wbr>Host<wbr>Route&gt;?</a></span>
    </dt>
    <dd>{{% md %}}(**Deprecated** - use `openstack.networking.SubnetRoute`
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use openstack_networking_subnet_route_v2 instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this creates a
new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ipv6Address<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ipv6Ra<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the subnet. Changing this updates the name of
the existing subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of the parent network. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>No<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Prefix<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subnetpool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the subnetpool associated with the subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>All<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The collection of ags assigned on the subnet, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allocation<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpool">[]Subnet<wbr>Allocation<wbr>Pool</a></span>
    </dt>
    <dd>{{% md %}}A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
`allocation_pool` blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The `allocation_pool` block is documented below.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Allocation<wbr>Pools<wbr>Collection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpoolscollection">[]Subnet<wbr>Allocation<wbr>Pools<wbr>Collection</a></span>
    </dt>
    <dd>{{% md %}}
A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The `allocation_pools` block is documented below.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use allocation_pool instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the subnet. Changing this
updates the name of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dns<wbr>Nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Gateway<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Host<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnethostroute">[]Subnet<wbr>Host<wbr>Route</a></span>
    </dt>
    <dd>{{% md %}}(**Deprecated** - use `openstack.networking.SubnetRoute`
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use openstack_networking_subnet_route_v2 instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this creates a
new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ipv6Address<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ipv6Ra<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the subnet. Changing this updates the name of
the existing subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of the parent network. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>No<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Prefix<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subnetpool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the subnetpool associated with the subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
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

    <dt class="property-"
            title="">
        <span>all<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The collection of ags assigned on the subnet, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allocation<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpool">Subnet<wbr>Allocation<wbr>Pool[]</a></span>
    </dt>
    <dd>{{% md %}}A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
`allocation_pool` blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The `allocation_pool` block is documented below.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>allocation<wbr>Pools<wbr>Collection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpoolscollection">Subnet<wbr>Allocation<wbr>Pools<wbr>Collection[]</a></span>
    </dt>
    <dd>{{% md %}}
A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The `allocation_pools` block is documented below.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use allocation_pool instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the subnet. Changing this
updates the name of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dns<wbr>Nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>gateway<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>host<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnethostroute">Subnet<wbr>Host<wbr>Route[]?</a></span>
    </dt>
    <dd>{{% md %}}(**Deprecated** - use `openstack.networking.SubnetRoute`
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use openstack_networking_subnet_route_v2 instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this creates a
new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ipv6Address<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ipv6Ra<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the subnet. Changing this updates the name of
the existing subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The UUID of the parent network. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>no<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>prefix<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subnetpool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the subnetpool associated with the subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>all_<wbr>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The collection of ags assigned on the subnet, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allocation_<wbr>pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpool">List[Subnet<wbr>Allocation<wbr>Pool]</a></span>
    </dt>
    <dd>{{% md %}}A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
`allocation_pool` blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The `allocation_pool` block is documented below.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>allocation_<wbr>pools_<wbr>collection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpoolscollection">List[Subnet<wbr>Allocation<wbr>Pools<wbr>Collection]</a></span>
    </dt>
    <dd>{{% md %}}
A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The `allocation_pools` block is documented below.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use allocation_pool instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the subnet. Changing this
updates the name of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dns_<wbr>nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>gateway_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>host_<wbr>routes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnethostroute">List[Subnet<wbr>Host<wbr>Route]</a></span>
    </dt>
    <dd>{{% md %}}(**Deprecated** - use `openstack.networking.SubnetRoute`
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use openstack_networking_subnet_route_v2 instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>ip_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this creates a
new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ipv6_<wbr>address_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ipv6_<wbr>ra_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the subnet. Changing this updates the name of
the existing subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UUID of the parent network. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>no_<wbr>gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>prefix_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subnetpool_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the subnetpool associated with the subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>value_<wbr>specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Subnet Resource

Get an existing Subnet resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#SubnetState">SubnetState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/openstack/networking/#Subnet">Subnet</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>all_tags=None<span class="p">, </span>allocation_pools=None<span class="p">, </span>allocation_pools_collection=None<span class="p">, </span>cidr=None<span class="p">, </span>description=None<span class="p">, </span>dns_nameservers=None<span class="p">, </span>enable_dhcp=None<span class="p">, </span>gateway_ip=None<span class="p">, </span>host_routes=None<span class="p">, </span>ip_version=None<span class="p">, </span>ipv6_address_mode=None<span class="p">, </span>ipv6_ra_mode=None<span class="p">, </span>name=None<span class="p">, </span>network_id=None<span class="p">, </span>no_gateway=None<span class="p">, </span>prefix_length=None<span class="p">, </span>region=None<span class="p">, </span>subnetpool_id=None<span class="p">, </span>tags=None<span class="p">, </span>tenant_id=None<span class="p">, </span>value_specs=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetSubnet<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#SubnetState">SubnetState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#Subnet">Subnet</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.Subnet.html">Subnet</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Openstack/Pulumi.Openstack.Networking.SubnetState.html">SubnetState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>All<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The collection of ags assigned on the subnet, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allocation<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpool">List&lt;Subnet<wbr>Allocation<wbr>Pool<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
`allocation_pool` blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The `allocation_pool` block is documented below.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Allocation<wbr>Pools<wbr>Collection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpoolscollection">List&lt;Subnet<wbr>Allocation<wbr>Pools<wbr>Collection<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}
A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The `allocation_pools` block is documented below.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use allocation_pool instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the subnet. Changing this
updates the name of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gateway<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Host<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnethostroute">List&lt;Subnet<wbr>Host<wbr>Route<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}(**Deprecated** - use `openstack.networking.SubnetRoute`
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use openstack_networking_subnet_route_v2 instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this creates a
new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Address<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Ra<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the subnet. Changing this updates the name of
the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID of the parent network. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Prefix<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetpool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the subnetpool associated with the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>All<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The collection of ags assigned on the subnet, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allocation<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpool">[]Subnet<wbr>Allocation<wbr>Pool</a></span>
    </dt>
    <dd>{{% md %}}A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
`allocation_pool` blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The `allocation_pool` block is documented below.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Allocation<wbr>Pools<wbr>Collection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpoolscollection">[]Subnet<wbr>Allocation<wbr>Pools<wbr>Collection</a></span>
    </dt>
    <dd>{{% md %}}
A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The `allocation_pools` block is documented below.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use allocation_pool instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the subnet. Changing this
updates the name of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gateway<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Host<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnethostroute">[]Subnet<wbr>Host<wbr>Route</a></span>
    </dt>
    <dd>{{% md %}}(**Deprecated** - use `openstack.networking.SubnetRoute`
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use openstack_networking_subnet_route_v2 instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this creates a
new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Address<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv6Ra<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the subnet. Changing this updates the name of
the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The UUID of the parent network. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>No<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Prefix<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetpool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the subnetpool associated with the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.
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
        <span>all<wbr>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The collection of ags assigned on the subnet, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allocation<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpool">Subnet<wbr>Allocation<wbr>Pool[]?</a></span>
    </dt>
    <dd>{{% md %}}A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
`allocation_pool` blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The `allocation_pool` block is documented below.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>allocation<wbr>Pools<wbr>Collection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpoolscollection">Subnet<wbr>Allocation<wbr>Pools<wbr>Collection[]?</a></span>
    </dt>
    <dd>{{% md %}}
A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The `allocation_pools` block is documented below.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use allocation_pool instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the subnet. Changing this
updates the name of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gateway<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>host<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnethostroute">Subnet<wbr>Host<wbr>Route[]?</a></span>
    </dt>
    <dd>{{% md %}}(**Deprecated** - use `openstack.networking.SubnetRoute`
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use openstack_networking_subnet_route_v2 instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this creates a
new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6Address<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6Ra<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the subnet. Changing this updates the name of
the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The UUID of the parent network. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no<wbr>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>prefix<wbr>Length</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetpool<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the subnetpool associated with the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Specs</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of additional options.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>all_<wbr>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The collection of ags assigned on the subnet, which have been
explicitly and implicitly added.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allocation_<wbr>pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpool">List[Subnet<wbr>Allocation<wbr>Pool]</a></span>
    </dt>
    <dd>{{% md %}}A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
`allocation_pool` blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The `allocation_pool` block is documented below.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>allocation_<wbr>pools_<wbr>collection</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnetallocationpoolscollection">List[Subnet<wbr>Allocation<wbr>Pools<wbr>Collection]</a></span>
    </dt>
    <dd>{{% md %}}
A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The `allocation_pools` block is documented below.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}use allocation_pool instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the subnet. Changing this
updates the name of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns_<wbr>nameservers</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>dhcp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gateway_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Default gateway used by devices in this subnet.
Leaving this blank and not setting `no_gateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>host_<wbr>routes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subnethostroute">List[Subnet<wbr>Host<wbr>Route]</a></span>
    </dt>
    <dd>{{% md %}}(**Deprecated** - use `openstack.networking.SubnetRoute`
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Use openstack_networking_subnet_route_v2 instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}IP version, either 4 (default) or 6. Changing this creates a
new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6_<wbr>address_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IPv6 address mode. Valid values are
`dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv6_<wbr>ra_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IPv6 Router Advertisement mode. Valid values
are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the subnet. Changing this updates the name of
the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The UUID of the parent network. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>no_<wbr>gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>prefix_<wbr>length</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetpool_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the subnetpool associated with the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A set of string tags for the subnet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.
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

<h4>Subnet<wbr>Allocation<wbr>Pool</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/input/#SubnetAllocationPool">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/output/#SubnetAllocationPool">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#SubnetAllocationPoolArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#SubnetAllocationPoolOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>End</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ending address.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The starting address.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>End</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ending address.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The starting address.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>end</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ending address.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The starting address.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>end</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ending address.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The starting address.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Subnet<wbr>Allocation<wbr>Pools<wbr>Collection</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/input/#SubnetAllocationPoolsCollection">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/output/#SubnetAllocationPoolsCollection">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#SubnetAllocationPoolsCollectionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#SubnetAllocationPoolsCollectionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>End</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ending address.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The starting address.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>End</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ending address.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The starting address.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>end</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ending address.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The starting address.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>end</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ending address.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The starting address.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Subnet<wbr>Host<wbr>Route</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/input/#SubnetHostRoute">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/openstack/types/output/#SubnetHostRoute">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#SubnetHostRouteArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-openstack/sdk/go/openstack/networking?tab=doc#SubnetHostRouteOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Destination<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The destination CIDR.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Next<wbr>Hop</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The next hop in the route.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Destination<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The destination CIDR.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Next<wbr>Hop</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The next hop in the route.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>destination<wbr>Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The destination CIDR.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>next<wbr>Hop</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The next hop in the route.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>destination_<wbr>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The destination CIDR.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>next_<wbr>hop</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The next hop in the route.
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

