
---
title: "RouterNat"
block_external_search_index: true
---



A NAT service created in a router.


To get more information about RouterNat, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/routers)
* How-to Guides
    * [Google Cloud Router](https://cloud.google.com/router/docs/)



## Create a RouterNat Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#RouterNat">RouterNat</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#RouterNatArgs">RouterNatArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">RouterNat</span><span class="p">(resource_name, opts=None, </span>drain_nat_ips=None<span class="p">, </span>icmp_idle_timeout_sec=None<span class="p">, </span>log_config=None<span class="p">, </span>min_ports_per_vm=None<span class="p">, </span>name=None<span class="p">, </span>nat_ip_allocate_option=None<span class="p">, </span>nat_ips=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, </span>router=None<span class="p">, </span>source_subnetwork_ip_ranges_to_nat=None<span class="p">, </span>subnetworks=None<span class="p">, </span>tcp_established_idle_timeout_sec=None<span class="p">, </span>tcp_transitory_idle_timeout_sec=None<span class="p">, </span>udp_idle_timeout_sec=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewRouterNat<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#RouterNatArgs">RouterNatArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#RouterNat">RouterNat</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.RouterNat.html">RouterNat</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.RouterNatArgs.html">RouterNatArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-required"
            title="Required">
        <span>Nat<wbr>Ip<wbr>Allocate<wbr>Option</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}How external IPs should be allocated for this NAT. Valid values are 'AUTO_ONLY' for only allowing NAT IPs allocated by
Google Cloud Platform, or 'MANUAL_ONLY' for only user-allocated NAT IP addresses.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this NAT will be configured.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Subnetwork<wbr>Ip<wbr>Ranges<wbr>To<wbr>Nat</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}How NAT should be configured per Subnetwork. If 'ALL_SUBNETWORKS_ALL_IP_RANGES', all of the IP ranges in every
Subnetwork are allowed to Nat. If 'ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES', all of the primary IP ranges in every
Subnetwork are allowed to Nat. 'LIST_OF_SUBNETWORKS': A list of Subnetworks are allowed to Nat (specified in the field
subnetwork below). Note that if this field contains ALL_SUBNETWORKS_ALL_IP_RANGES or
ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES, then there should not be any other RouterNat section in any Router for this
network in this region.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Drain<wbr>Nat<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of URLs of the IP resources to be drained. These IPs must be valid static external IPs that have been assigned to
the NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Icmp<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for ICMP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatlogconfig">Router<wbr>Nat<wbr>Log<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Configuration for logging on NAT
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Ports<wbr>Per<wbr>Vm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Minimum number of ports allocated to a VM from this NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the NAT service. The name must be 1-63 characters long and comply with RFC1035.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nat<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Self-links of NAT IPs. Only valid if natIpAllocateOption is set to MANUAL_ONLY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Region where the router and NAT reside.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetworks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatsubnetwork">List&lt;Router<wbr>Nat<wbr>Subnetwork<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more subnetwork NAT configurations. Only used if 'source_subnetwork_ip_ranges_to_nat' is set to
'LIST_OF_SUBNETWORKS'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Established<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP established connections. Defaults to 1200s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Transitory<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP transitory connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Udp<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for UDP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Nat<wbr>Ip<wbr>Allocate<wbr>Option</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}How external IPs should be allocated for this NAT. Valid values are 'AUTO_ONLY' for only allowing NAT IPs allocated by
Google Cloud Platform, or 'MANUAL_ONLY' for only user-allocated NAT IP addresses.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this NAT will be configured.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Subnetwork<wbr>Ip<wbr>Ranges<wbr>To<wbr>Nat</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}How NAT should be configured per Subnetwork. If 'ALL_SUBNETWORKS_ALL_IP_RANGES', all of the IP ranges in every
Subnetwork are allowed to Nat. If 'ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES', all of the primary IP ranges in every
Subnetwork are allowed to Nat. 'LIST_OF_SUBNETWORKS': A list of Subnetworks are allowed to Nat (specified in the field
subnetwork below). Note that if this field contains ALL_SUBNETWORKS_ALL_IP_RANGES or
ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES, then there should not be any other RouterNat section in any Router for this
network in this region.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Drain<wbr>Nat<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A list of URLs of the IP resources to be drained. These IPs must be valid static external IPs that have been assigned to
the NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Icmp<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for ICMP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatlogconfig">Router<wbr>Nat<wbr>Log<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for logging on NAT
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Ports<wbr>Per<wbr>Vm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Minimum number of ports allocated to a VM from this NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the NAT service. The name must be 1-63 characters long and comply with RFC1035.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nat<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Self-links of NAT IPs. Only valid if natIpAllocateOption is set to MANUAL_ONLY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Region where the router and NAT reside.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetworks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatsubnetwork">[]Router<wbr>Nat<wbr>Subnetwork</a></span>
    </dt>
    <dd>{{% md %}}One or more subnetwork NAT configurations. Only used if 'source_subnetwork_ip_ranges_to_nat' is set to
'LIST_OF_SUBNETWORKS'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Established<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP established connections. Defaults to 1200s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Transitory<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP transitory connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Udp<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for UDP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>nat<wbr>Ip<wbr>Allocate<wbr>Option</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}How external IPs should be allocated for this NAT. Valid values are 'AUTO_ONLY' for only allowing NAT IPs allocated by
Google Cloud Platform, or 'MANUAL_ONLY' for only user-allocated NAT IP addresses.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this NAT will be configured.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source<wbr>Subnetwork<wbr>Ip<wbr>Ranges<wbr>To<wbr>Nat</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}How NAT should be configured per Subnetwork. If 'ALL_SUBNETWORKS_ALL_IP_RANGES', all of the IP ranges in every
Subnetwork are allowed to Nat. If 'ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES', all of the primary IP ranges in every
Subnetwork are allowed to Nat. 'LIST_OF_SUBNETWORKS': A list of Subnetworks are allowed to Nat (specified in the field
subnetwork below). Note that if this field contains ALL_SUBNETWORKS_ALL_IP_RANGES or
ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES, then there should not be any other RouterNat section in any Router for this
network in this region.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>drain<wbr>Nat<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A list of URLs of the IP resources to be drained. These IPs must be valid static external IPs that have been assigned to
the NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>icmp<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for ICMP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatlogconfig">Router<wbr>Nat<wbr>Log<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for logging on NAT
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Ports<wbr>Per<wbr>Vm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Minimum number of ports allocated to a VM from this NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the NAT service. The name must be 1-63 characters long and comply with RFC1035.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nat<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Self-links of NAT IPs. Only valid if natIpAllocateOption is set to MANUAL_ONLY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Region where the router and NAT reside.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetworks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatsubnetwork">Router<wbr>Nat<wbr>Subnetwork[]</a></span>
    </dt>
    <dd>{{% md %}}One or more subnetwork NAT configurations. Only used if 'source_subnetwork_ip_ranges_to_nat' is set to
'LIST_OF_SUBNETWORKS'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp<wbr>Established<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP established connections. Defaults to 1200s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp<wbr>Transitory<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP transitory connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>udp<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for UDP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>nat_<wbr>ip_<wbr>allocate_<wbr>option</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}How external IPs should be allocated for this NAT. Valid values are 'AUTO_ONLY' for only allowing NAT IPs allocated by
Google Cloud Platform, or 'MANUAL_ONLY' for only user-allocated NAT IP addresses.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this NAT will be configured.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source_<wbr>subnetwork_<wbr>ip_<wbr>ranges_<wbr>to_<wbr>nat</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}How NAT should be configured per Subnetwork. If 'ALL_SUBNETWORKS_ALL_IP_RANGES', all of the IP ranges in every
Subnetwork are allowed to Nat. If 'ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES', all of the primary IP ranges in every
Subnetwork are allowed to Nat. 'LIST_OF_SUBNETWORKS': A list of Subnetworks are allowed to Nat (specified in the field
subnetwork below). Note that if this field contains ALL_SUBNETWORKS_ALL_IP_RANGES or
ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES, then there should not be any other RouterNat section in any Router for this
network in this region.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>drain_<wbr>nat_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A list of URLs of the IP resources to be drained. These IPs must be valid static external IPs that have been assigned to
the NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>icmp_<wbr>idle_<wbr>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for ICMP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatlogconfig">Dict[Router<wbr>Nat<wbr>Log<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration for logging on NAT
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>ports_<wbr>per_<wbr>vm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Minimum number of ports allocated to a VM from this NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Name of the NAT service. The name must be 1-63 characters long and comply with RFC1035.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nat_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Self-links of NAT IPs. Only valid if natIpAllocateOption is set to MANUAL_ONLY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Region where the router and NAT reside.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetworks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatsubnetwork">List[Router<wbr>Nat<wbr>Subnetwork]</a></span>
    </dt>
    <dd>{{% md %}}One or more subnetwork NAT configurations. Only used if 'source_subnetwork_ip_ranges_to_nat' is set to
'LIST_OF_SUBNETWORKS'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp_<wbr>established_<wbr>idle_<wbr>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP established connections. Defaults to 1200s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp_<wbr>transitory_<wbr>idle_<wbr>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP transitory connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>udp_<wbr>idle_<wbr>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for UDP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Look up an Existing RouterNat Resource

Get an existing RouterNat resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#RouterNatState">RouterNatState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#RouterNat">RouterNat</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>drain_nat_ips=None<span class="p">, </span>icmp_idle_timeout_sec=None<span class="p">, </span>log_config=None<span class="p">, </span>min_ports_per_vm=None<span class="p">, </span>name=None<span class="p">, </span>nat_ip_allocate_option=None<span class="p">, </span>nat_ips=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, </span>router=None<span class="p">, </span>source_subnetwork_ip_ranges_to_nat=None<span class="p">, </span>subnetworks=None<span class="p">, </span>tcp_established_idle_timeout_sec=None<span class="p">, </span>tcp_transitory_idle_timeout_sec=None<span class="p">, </span>udp_idle_timeout_sec=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetRouterNat<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#RouterNatState">RouterNatState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#RouterNat">RouterNat</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.RouterNat.html">RouterNat</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.RouterNatState.html">RouterNatState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Drain<wbr>Nat<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of URLs of the IP resources to be drained. These IPs must be valid static external IPs that have been assigned to
the NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Icmp<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for ICMP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatlogconfig">Router<wbr>Nat<wbr>Log<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Configuration for logging on NAT
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Ports<wbr>Per<wbr>Vm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Minimum number of ports allocated to a VM from this NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the NAT service. The name must be 1-63 characters long and comply with RFC1035.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nat<wbr>Ip<wbr>Allocate<wbr>Option</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}How external IPs should be allocated for this NAT. Valid values are 'AUTO_ONLY' for only allowing NAT IPs allocated by
Google Cloud Platform, or 'MANUAL_ONLY' for only user-allocated NAT IP addresses.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nat<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Self-links of NAT IPs. Only valid if natIpAllocateOption is set to MANUAL_ONLY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Region where the router and NAT reside.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this NAT will be configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Subnetwork<wbr>Ip<wbr>Ranges<wbr>To<wbr>Nat</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}How NAT should be configured per Subnetwork. If 'ALL_SUBNETWORKS_ALL_IP_RANGES', all of the IP ranges in every
Subnetwork are allowed to Nat. If 'ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES', all of the primary IP ranges in every
Subnetwork are allowed to Nat. 'LIST_OF_SUBNETWORKS': A list of Subnetworks are allowed to Nat (specified in the field
subnetwork below). Note that if this field contains ALL_SUBNETWORKS_ALL_IP_RANGES or
ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES, then there should not be any other RouterNat section in any Router for this
network in this region.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetworks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatsubnetwork">List&lt;Router<wbr>Nat<wbr>Subnetwork<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more subnetwork NAT configurations. Only used if 'source_subnetwork_ip_ranges_to_nat' is set to
'LIST_OF_SUBNETWORKS'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Established<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP established connections. Defaults to 1200s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Transitory<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP transitory connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Udp<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for UDP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Drain<wbr>Nat<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A list of URLs of the IP resources to be drained. These IPs must be valid static external IPs that have been assigned to
the NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Icmp<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for ICMP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatlogconfig">Router<wbr>Nat<wbr>Log<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for logging on NAT
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Ports<wbr>Per<wbr>Vm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Minimum number of ports allocated to a VM from this NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the NAT service. The name must be 1-63 characters long and comply with RFC1035.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nat<wbr>Ip<wbr>Allocate<wbr>Option</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}How external IPs should be allocated for this NAT. Valid values are 'AUTO_ONLY' for only allowing NAT IPs allocated by
Google Cloud Platform, or 'MANUAL_ONLY' for only user-allocated NAT IP addresses.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Nat<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Self-links of NAT IPs. Only valid if natIpAllocateOption is set to MANUAL_ONLY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Region where the router and NAT reside.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this NAT will be configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Subnetwork<wbr>Ip<wbr>Ranges<wbr>To<wbr>Nat</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}How NAT should be configured per Subnetwork. If 'ALL_SUBNETWORKS_ALL_IP_RANGES', all of the IP ranges in every
Subnetwork are allowed to Nat. If 'ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES', all of the primary IP ranges in every
Subnetwork are allowed to Nat. 'LIST_OF_SUBNETWORKS': A list of Subnetworks are allowed to Nat (specified in the field
subnetwork below). Note that if this field contains ALL_SUBNETWORKS_ALL_IP_RANGES or
ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES, then there should not be any other RouterNat section in any Router for this
network in this region.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetworks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatsubnetwork">[]Router<wbr>Nat<wbr>Subnetwork</a></span>
    </dt>
    <dd>{{% md %}}One or more subnetwork NAT configurations. Only used if 'source_subnetwork_ip_ranges_to_nat' is set to
'LIST_OF_SUBNETWORKS'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Established<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP established connections. Defaults to 1200s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Transitory<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP transitory connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Udp<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for UDP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>drain<wbr>Nat<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A list of URLs of the IP resources to be drained. These IPs must be valid static external IPs that have been assigned to
the NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>icmp<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for ICMP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatlogconfig">Router<wbr>Nat<wbr>Log<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for logging on NAT
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Ports<wbr>Per<wbr>Vm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Minimum number of ports allocated to a VM from this NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Name of the NAT service. The name must be 1-63 characters long and comply with RFC1035.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nat<wbr>Ip<wbr>Allocate<wbr>Option</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}How external IPs should be allocated for this NAT. Valid values are 'AUTO_ONLY' for only allowing NAT IPs allocated by
Google Cloud Platform, or 'MANUAL_ONLY' for only user-allocated NAT IP addresses.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nat<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Self-links of NAT IPs. Only valid if natIpAllocateOption is set to MANUAL_ONLY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Region where the router and NAT reside.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this NAT will be configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Subnetwork<wbr>Ip<wbr>Ranges<wbr>To<wbr>Nat</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}How NAT should be configured per Subnetwork. If 'ALL_SUBNETWORKS_ALL_IP_RANGES', all of the IP ranges in every
Subnetwork are allowed to Nat. If 'ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES', all of the primary IP ranges in every
Subnetwork are allowed to Nat. 'LIST_OF_SUBNETWORKS': A list of Subnetworks are allowed to Nat (specified in the field
subnetwork below). Note that if this field contains ALL_SUBNETWORKS_ALL_IP_RANGES or
ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES, then there should not be any other RouterNat section in any Router for this
network in this region.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetworks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatsubnetwork">Router<wbr>Nat<wbr>Subnetwork[]</a></span>
    </dt>
    <dd>{{% md %}}One or more subnetwork NAT configurations. Only used if 'source_subnetwork_ip_ranges_to_nat' is set to
'LIST_OF_SUBNETWORKS'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp<wbr>Established<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP established connections. Defaults to 1200s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp<wbr>Transitory<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP transitory connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>udp<wbr>Idle<wbr>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for UDP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>drain_<wbr>nat_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A list of URLs of the IP resources to be drained. These IPs must be valid static external IPs that have been assigned to
the NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>icmp_<wbr>idle_<wbr>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for ICMP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatlogconfig">Dict[Router<wbr>Nat<wbr>Log<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration for logging on NAT
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>ports_<wbr>per_<wbr>vm</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Minimum number of ports allocated to a VM from this NAT.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Name of the NAT service. The name must be 1-63 characters long and comply with RFC1035.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nat_<wbr>ip_<wbr>allocate_<wbr>option</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}How external IPs should be allocated for this NAT. Valid values are 'AUTO_ONLY' for only allowing NAT IPs allocated by
Google Cloud Platform, or 'MANUAL_ONLY' for only user-allocated NAT IP addresses.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>nat_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Self-links of NAT IPs. Only valid if natIpAllocateOption is set to MANUAL_ONLY.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Region where the router and NAT reside.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>router</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Router in which this NAT will be configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>subnetwork_<wbr>ip_<wbr>ranges_<wbr>to_<wbr>nat</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}How NAT should be configured per Subnetwork. If 'ALL_SUBNETWORKS_ALL_IP_RANGES', all of the IP ranges in every
Subnetwork are allowed to Nat. If 'ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES', all of the primary IP ranges in every
Subnetwork are allowed to Nat. 'LIST_OF_SUBNETWORKS': A list of Subnetworks are allowed to Nat (specified in the field
subnetwork below). Note that if this field contains ALL_SUBNETWORKS_ALL_IP_RANGES or
ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES, then there should not be any other RouterNat section in any Router for this
network in this region.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetworks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#routernatsubnetwork">List[Router<wbr>Nat<wbr>Subnetwork]</a></span>
    </dt>
    <dd>{{% md %}}One or more subnetwork NAT configurations. Only used if 'source_subnetwork_ip_ranges_to_nat' is set to
'LIST_OF_SUBNETWORKS'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp_<wbr>established_<wbr>idle_<wbr>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP established connections. Defaults to 1200s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp_<wbr>transitory_<wbr>idle_<wbr>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for TCP transitory connections. Defaults to 30s if not set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>udp_<wbr>idle_<wbr>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for UDP connections. Defaults to 30s if not set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Router<wbr>Nat<wbr>Log<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#RouterNatLogConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#RouterNatLogConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#RouterNatLogConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#RouterNatLogConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enable</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enable</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enable</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Router<wbr>Nat<wbr>Subnetwork</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#RouterNatSubnetwork">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#RouterNatSubnetwork">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#RouterNatSubnetworkArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/compute?tab=doc#RouterNatSubnetworkOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Ip<wbr>Ranges<wbr>To<wbr>Nats</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secondary<wbr>Ip<wbr>Range<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
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
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Ip<wbr>Ranges<wbr>To<wbr>Nats</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secondary<wbr>Ip<wbr>Range<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
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
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source<wbr>Ip<wbr>Ranges<wbr>To<wbr>Nats</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secondary<wbr>Ip<wbr>Range<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
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
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source<wbr>Ip<wbr>Ranges<wbr>To<wbr>Nats</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secondary<wbr>Ip<wbr>Range<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`google-beta` Terraform Provider](https://github.com/terraform-providers/terraform-provider-google-beta).</dd>
</dl>

