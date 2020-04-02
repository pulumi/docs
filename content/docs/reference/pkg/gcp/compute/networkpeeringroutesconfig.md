
---
title: "NetworkPeeringRoutesConfig"
block_external_search_index: true
---

Manage a network peering's route settings without managing the peering as
a whole. This resource is primarily intended for use with GCP-generated
peerings that shouldn't otherwise be managed by other tools. Deleting this
resource is a no-op and the peering will not be modified.


To get more information about NetworkPeeringRoutesConfig, see:

* [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/networks/updatePeering)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/vpc/docs/vpc-peering)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_network_peering_routes_config.html.markdown.



## Create a NetworkPeeringRoutesConfig Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#NetworkPeeringRoutesConfig">NetworkPeeringRoutesConfig</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#NetworkPeeringRoutesConfigArgs">NetworkPeeringRoutesConfigArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">NetworkPeeringRoutesConfig</span><span class="p">(resource_name, opts=None, </span>export_custom_routes=None<span class="p">, </span>import_custom_routes=None<span class="p">, </span>network=None<span class="p">, </span>peering=None<span class="p">, </span>project=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewNetworkPeeringRoutesConfig<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#NetworkPeeringRoutesConfigArgs">NetworkPeeringRoutesConfigArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#NetworkPeeringRoutesConfig">NetworkPeeringRoutesConfig</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.NetworkPeeringRoutesConfig.html">NetworkPeeringRoutesConfig</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.NetworkPeeringRoutesConfigArgs.html">NetworkPeeringRoutesConfigArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Export<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to export the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Import<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to import the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the primary network for the peering.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Peering</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the peering.
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

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Export<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to export the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Import<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to import the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the primary network for the peering.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Peering</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the peering.
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

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>export<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether to export the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>import<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether to import the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the primary network for the peering.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>peering</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the peering.
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

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>export_<wbr>custom_<wbr>routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to export the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>import_<wbr>custom_<wbr>routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to import the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the primary network for the peering.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>peering</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the peering.
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

</dl>
{{% /choosable %}}







## NetworkPeeringRoutesConfig Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Export<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to export the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Import<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to import the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the primary network for the peering.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Peering</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the peering.
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

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Export<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to export the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Import<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to import the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the primary network for the peering.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Peering</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the peering.
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

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>export<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether to export the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>import<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether to import the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the primary network for the peering.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>peering</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the peering.
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

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>export_<wbr>custom_<wbr>routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to export the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>import_<wbr>custom_<wbr>routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to import the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the primary network for the peering.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>peering</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the peering.
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

</dl>
{{% /choosable %}}








## Look up an Existing NetworkPeeringRoutesConfig Resource

Get an existing NetworkPeeringRoutesConfig resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#NetworkPeeringRoutesConfigState">NetworkPeeringRoutesConfigState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/compute/#NetworkPeeringRoutesConfig">NetworkPeeringRoutesConfig</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>export_custom_routes=None<span class="p">, </span>import_custom_routes=None<span class="p">, </span>network=None<span class="p">, </span>peering=None<span class="p">, </span>project=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetNetworkPeeringRoutesConfig<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#NetworkPeeringRoutesConfigState">NetworkPeeringRoutesConfigState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/compute?tab=doc#NetworkPeeringRoutesConfig">NetworkPeeringRoutesConfig</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.NetworkPeeringRoutesConfig.html">NetworkPeeringRoutesConfig</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Compute.NetworkPeeringRoutesConfigState.html">NetworkPeeringRoutesConfigState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Export<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to export the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Import<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to import the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the primary network for the peering.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peering</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the peering.
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

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Export<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to export the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Import<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to import the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the primary network for the peering.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peering</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the peering.
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

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>export<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to export the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>import<wbr>Custom<wbr>Routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to import the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the primary network for the peering.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peering</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the peering.
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

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>export_<wbr>custom_<wbr>routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to export the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>import_<wbr>custom_<wbr>routes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to import the custom routes to the peer network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the primary network for the peering.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peering</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the peering.
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

</dl>
{{% /choosable %}}










<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
