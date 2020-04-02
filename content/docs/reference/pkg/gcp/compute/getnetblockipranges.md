
---
title: "GetNetblockIPRanges"
block_external_search_index: true
---

Use this data source to get the IP addresses from different special IP ranges on Google Cloud Platform.

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_google_netblock_ip_ranges.html.markdown.





## Using GetNetblockIPRanges

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getNetblockIPRanges<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#GetNetblockIPRangesArgs">GetNetblockIPRangesArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#GetNetblockIPRangesResult">GetNetblockIPRangesResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_netblock_ip_ranges(</span>range_type=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupNetblockIPRanges<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#LookupNetblockIPRangesArgs">LookupNetblockIPRangesArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#LookupNetblockIPRangesResult">LookupNetblockIPRangesResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetNetblockIPRanges </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.GetNetblockIPRangesResult.html">GetNetblockIPRangesResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.GetNetblockIPRangesArgs.html">GetNetblockIPRangesArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Range<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of range for which to provide results.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Range<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of range for which to provide results.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>range<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of range for which to provide results.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>range_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of range for which to provide results.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetNetblockIPRanges Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cidr<wbr>Blocks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Retrieve list of all CIDR blocks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cidr<wbr>Blocks<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Retrieve list of the IPv4 CIDR blocks
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cidr<wbr>Blocks<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Retrieve list of the IPv6 CIDR blocks, if available.
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
        <span>Range<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cidr<wbr>Blocks</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Retrieve list of all CIDR blocks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cidr<wbr>Blocks<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Retrieve list of the IPv4 CIDR blocks
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cidr<wbr>Blocks<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Retrieve list of the IPv6 CIDR blocks, if available.
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
        <span>Range<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>cidr<wbr>Blocks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Retrieve list of all CIDR blocks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cidr<wbr>Blocks<wbr>Ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Retrieve list of the IPv4 CIDR blocks
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cidr<wbr>Blocks<wbr>Ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Retrieve list of the IPv6 CIDR blocks, if available.
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
        <span>range<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>cidr_<wbr>blocks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Retrieve list of all CIDR blocks.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cidr_<wbr>blocks_<wbr>ipv4s</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Retrieve list of the IPv4 CIDR blocks
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cidr_<wbr>blocks_<wbr>ipv6s</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Retrieve list of the IPv6 CIDR blocks, if available.
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
        <span>range_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







