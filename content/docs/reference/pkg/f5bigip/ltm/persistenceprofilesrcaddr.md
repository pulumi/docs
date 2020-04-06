
---
title: "PersistenceProfileSrcAddr"
block_external_search_index: true
---



Configures a source address persistence profile

## Reference

`name` - (Required) Name of the virtual address

`defaults_from` - (Required) Parent cookie persistence profile

`match_across_pools` (Optional) (enabled or disabled) match across pools with given persistence record

`match_across_services` (Optional) (enabled or disabled) match across services with given persistence record

`match_across_virtuals` (Optional) (enabled or disabled) match across virtual servers with given persistence record

`mirror` (Optional) (enabled or disabled) mirror persistence record

`timeout` (Optional) (enabled or disabled) Timeout for persistence of the session in seconds

`override_conn_limit` (Optional) (enabled or disabled) Enable or dissable pool member connection limits are overridden for persisted clients. Per-virtual connection limits remain hard limits and are not overridden.

`hash_algorithm` (Optional) Specify the hash algorithm

`mask` (Optional) Identify a range of source IP addresses to manage together as a single source address affinity persistent connection when connecting to the pool. Must be a valid IPv4 or IPv6 mask.

`map_proxies` (Optional) (enabled or disabled) Directs all to the same single pool member

> This content is derived from https://github.com/terraform-providers/terraform-provider-bigip/blob/master/website/docs/r/bigip_ltm_persistence_profile_srcaddr.html.markdown.



## Create a PersistenceProfileSrcAddr Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#PersistenceProfileSrcAddr">PersistenceProfileSrcAddr</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#PersistenceProfileSrcAddrArgs">PersistenceProfileSrcAddrArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">PersistenceProfileSrcAddr</span><span class="p">(resource_name, opts=None, </span>app_service=None<span class="p">, </span>defaults_from=None<span class="p">, </span>hash_algorithm=None<span class="p">, </span>map_proxies=None<span class="p">, </span>mask=None<span class="p">, </span>match_across_pools=None<span class="p">, </span>match_across_services=None<span class="p">, </span>match_across_virtuals=None<span class="p">, </span>mirror=None<span class="p">, </span>name=None<span class="p">, </span>override_conn_limit=None<span class="p">, </span>timeout=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewPersistenceProfileSrcAddr<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/go/f5bigip/ltm?tab=doc#PersistenceProfileSrcAddrArgs">PersistenceProfileSrcAddrArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/go/f5bigip/ltm?tab=doc#PersistenceProfileSrcAddr">PersistenceProfileSrcAddr</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5bigip.Ltm.PersistenceProfileSrcAddr.html">PersistenceProfileSrcAddr</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5bigip.Ltm.PersistenceProfileSrcAddrArgs.html">PersistenceProfileSrcAddrArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hash<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specify the hash algorithm
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Map<wbr>Proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable directs all to the same single pool member
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mask</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hash<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specify the hash algorithm
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Map<wbr>Proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable directs all to the same single pool member
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mask</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hash<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specify the hash algorithm
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>map<wbr>Proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable directs all to the same single pool member
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mask</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>defaults_<wbr>from</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hash_<wbr>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specify the hash algorithm
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>map_<wbr>proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable directs all to the same single pool member
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mask</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>across_<wbr>pools</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>across_<wbr>services</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>across_<wbr>virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>override_<wbr>conn_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## PersistenceProfileSrcAddr Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hash<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specify the hash algorithm
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Map<wbr>Proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable directs all to the same single pool member
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Mask</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hash<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specify the hash algorithm
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Map<wbr>Proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable directs all to the same single pool member
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Mask</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>app<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hash<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specify the hash algorithm
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>map<wbr>Proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable directs all to the same single pool member
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>mask</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>app_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>defaults_<wbr>from</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hash_<wbr>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specify the hash algorithm
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>map_<wbr>proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable directs all to the same single pool member
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>mask</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>match_<wbr>across_<wbr>pools</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>match_<wbr>across_<wbr>services</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>match_<wbr>across_<wbr>virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>override_<wbr>conn_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing PersistenceProfileSrcAddr Resource

Get an existing PersistenceProfileSrcAddr resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#PersistenceProfileSrcAddrState">PersistenceProfileSrcAddrState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/f5bigip/ltm/#PersistenceProfileSrcAddr">PersistenceProfileSrcAddr</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>app_service=None<span class="p">, </span>defaults_from=None<span class="p">, </span>hash_algorithm=None<span class="p">, </span>map_proxies=None<span class="p">, </span>mask=None<span class="p">, </span>match_across_pools=None<span class="p">, </span>match_across_services=None<span class="p">, </span>match_across_virtuals=None<span class="p">, </span>mirror=None<span class="p">, </span>name=None<span class="p">, </span>override_conn_limit=None<span class="p">, </span>timeout=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetPersistenceProfileSrcAddr<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/go/f5bigip/ltm?tab=doc#PersistenceProfileSrcAddrState">PersistenceProfileSrcAddrState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-f5bigip/sdk/go/f5bigip/ltm?tab=doc#PersistenceProfileSrcAddr">PersistenceProfileSrcAddr</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5bigip.Ltm.PersistenceProfileSrcAddr.html">PersistenceProfileSrcAddr</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.F5bigip/Pulumi.F5bigip.Ltm.PersistenceProfileSrcAddrState.html">PersistenceProfileSrcAddrState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hash<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specify the hash algorithm
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Map<wbr>Proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable directs all to the same single pool member
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mask</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hash<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specify the hash algorithm
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Map<wbr>Proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable directs all to the same single pool member
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mask</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>defaults<wbr>From</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hash<wbr>Algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specify the hash algorithm
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>map<wbr>Proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable directs all to the same single pool member
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mask</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Across<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Across<wbr>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match<wbr>Across<wbr>Virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>override<wbr>Conn<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>defaults_<wbr>from</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Inherit defaults from parent profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hash_<wbr>algorithm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specify the hash algorithm
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>map_<wbr>proxies</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable directs all to the same single pool member
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mask</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Identify a range of source IP addresses to manage together as a single source address affinity persistent connection
when connecting to the pool. Must be a valid IPv4 or IPv6 mask.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>across_<wbr>pools</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across pools with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>across_<wbr>services</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>match_<wbr>across_<wbr>virtuals</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable match across services with given persistence record
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mirror</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the persistence profile
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>override_<wbr>conn_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}To enable _ disable that pool member connection limits are overridden for persisted clients. Per-virtual connection
limits remain hard limits and are not overridden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Timeout for persistence of the session
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-f5bigip">https://github.com/pulumi/pulumi-f5bigip</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

