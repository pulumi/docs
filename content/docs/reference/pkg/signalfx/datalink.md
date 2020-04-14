
---
title: "DataLink"
block_external_search_index: true
---



Manage SignalFx [Data Links](https://docs.signalfx.com/en/latest/managing/data-links.html).

> This content is derived from https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/data_link.html.markdown.



## Create a DataLink Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#DataLink">DataLink</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#DataLinkArgs">DataLinkArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">DataLink</span><span class="p">(resource_name, opts=None, </span>context_dashboard_id=None<span class="p">, </span>property_name=None<span class="p">, </span>property_value=None<span class="p">, </span>target_external_urls=None<span class="p">, </span>target_signalfx_dashboards=None<span class="p">, </span>target_splunks=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDataLink<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DataLinkArgs">DataLinkArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DataLink">DataLink</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.DataLink.html">DataLink</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.SignalFx.DataLinkArgs.html">DataLinkArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Context<wbr>Dashboard<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Property<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Property<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>External<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetexternalurl">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Data<wbr>Link<wbr>Target<wbr>External<wbr>Url<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Signalfx<wbr>Dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsignalfxdashboard">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Data<wbr>Link<wbr>Target<wbr>Signalfx<wbr>Dashboard<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Link to a SignalFx dashboard
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Splunks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsplunk">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Data<wbr>Link<wbr>Target<wbr>Splunk<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Context<wbr>Dashboard<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Property<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Property<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>External<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetexternalurl">[]Data<wbr>Link<wbr>Target<wbr>External<wbr>Url</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Signalfx<wbr>Dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsignalfxdashboard">[]Data<wbr>Link<wbr>Target<wbr>Signalfx<wbr>Dashboard</a></span>
    </dt>
    <dd>{{% md %}}Link to a SignalFx dashboard
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Splunks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsplunk">[]Data<wbr>Link<wbr>Target<wbr>Splunk</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>context<wbr>Dashboard<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>property<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>property<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>External<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetexternalurl">Data<wbr>Link<wbr>Target<wbr>External<wbr>Url[]</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Signalfx<wbr>Dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsignalfxdashboard">Data<wbr>Link<wbr>Target<wbr>Signalfx<wbr>Dashboard[]</a></span>
    </dt>
    <dd>{{% md %}}Link to a SignalFx dashboard
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Splunks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsplunk">Data<wbr>Link<wbr>Target<wbr>Splunk[]</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>context_<wbr>dashboard_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>property_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>property_<wbr>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target_<wbr>external_<wbr>urls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetexternalurl">List[Data<wbr>Link<wbr>Target<wbr>External<wbr>Url]</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target_<wbr>signalfx_<wbr>dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsignalfxdashboard">List[Data<wbr>Link<wbr>Target<wbr>Signalfx<wbr>Dashboard]</a></span>
    </dt>
    <dd>{{% md %}}Link to a SignalFx dashboard
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target_<wbr>splunks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsplunk">List[Data<wbr>Link<wbr>Target<wbr>Splunk]</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Look up an Existing DataLink Resource

Get an existing DataLink resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#DataLinkState">DataLinkState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#DataLink">DataLink</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>context_dashboard_id=None<span class="p">, </span>property_name=None<span class="p">, </span>property_value=None<span class="p">, </span>target_external_urls=None<span class="p">, </span>target_signalfx_dashboards=None<span class="p">, </span>target_splunks=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDataLink<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DataLinkState">DataLinkState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DataLink">DataLink</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.DataLink.html">DataLink</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx..DataLinkState.html">DataLinkState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Context<wbr>Dashboard<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Property<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Property<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>External<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetexternalurl">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Data<wbr>Link<wbr>Target<wbr>External<wbr>Url<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Signalfx<wbr>Dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsignalfxdashboard">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Data<wbr>Link<wbr>Target<wbr>Signalfx<wbr>Dashboard<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Link to a SignalFx dashboard
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Splunks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsplunk">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Data<wbr>Link<wbr>Target<wbr>Splunk<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Context<wbr>Dashboard<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Property<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Property<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>External<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetexternalurl">[]Data<wbr>Link<wbr>Target<wbr>External<wbr>Url</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Signalfx<wbr>Dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsignalfxdashboard">[]Data<wbr>Link<wbr>Target<wbr>Signalfx<wbr>Dashboard</a></span>
    </dt>
    <dd>{{% md %}}Link to a SignalFx dashboard
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Splunks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsplunk">[]Data<wbr>Link<wbr>Target<wbr>Splunk</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>context<wbr>Dashboard<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>property<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>property<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>External<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetexternalurl">Data<wbr>Link<wbr>Target<wbr>External<wbr>Url[]</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Signalfx<wbr>Dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsignalfxdashboard">Data<wbr>Link<wbr>Target<wbr>Signalfx<wbr>Dashboard[]</a></span>
    </dt>
    <dd>{{% md %}}Link to a SignalFx dashboard
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Splunks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsplunk">Data<wbr>Link<wbr>Target<wbr>Splunk[]</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>context_<wbr>dashboard_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>property_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name (key) of the metadata that's the trigger of a data link. If you specify `property_value`, you must specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>property_<wbr>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Value of the metadata that's the trigger of a data link. If you specify this property, you must also specify `property_name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target_<wbr>external_<wbr>urls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetexternalurl">List[Data<wbr>Link<wbr>Target<wbr>External<wbr>Url]</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target_<wbr>signalfx_<wbr>dashboards</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsignalfxdashboard">List[Data<wbr>Link<wbr>Target<wbr>Signalfx<wbr>Dashboard]</a></span>
    </dt>
    <dd>{{% md %}}Link to a SignalFx dashboard
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target_<wbr>splunks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datalinktargetsplunk">List[Data<wbr>Link<wbr>Target<wbr>Splunk]</a></span>
    </dt>
    <dd>{{% md %}}Link to an external URL
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Data<wbr>Link<wbr>Target<wbr>External<wbr>Url</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#DataLinkTargetExternalUrl">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#DataLinkTargetExternalUrl">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DataLinkTargetExternalUrlArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DataLinkTargetExternalUrlOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}User-assigned target name. Use this value to differentiate between the link targets for a data link object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that designates a target as the default for a data link object. `true` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Minimum<wbr>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The [minimum time window](https://developers.signalfx.com/administration/data_links_overview.html#_minimum_time_window) for a search sent to an external site. Defaults to `6000`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Property<wbr>Key<wbr>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Describes the relationship between SignalFx metadata keys and external system properties when the key names are different.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}[Designates the format](https://developers.signalfx.com/administration/data_links_overview.html#_minimum_time_window) of `minimum_time_window` in the same data link target object. Must be one of `"ISO8601"`, `"EpochSeconds"` or `"Epoch"` (which is milliseconds). Defaults to `"ISO8601"`.
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
    <dd>{{% md %}}User-assigned target name. Use this value to differentiate between the link targets for a data link object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that designates a target as the default for a data link object. `true` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Minimum<wbr>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The [minimum time window](https://developers.signalfx.com/administration/data_links_overview.html#_minimum_time_window) for a search sent to an external site. Defaults to `6000`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Property<wbr>Key<wbr>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Describes the relationship between SignalFx metadata keys and external system properties when the key names are different.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}[Designates the format](https://developers.signalfx.com/administration/data_links_overview.html#_minimum_time_window) of `minimum_time_window` in the same data link target object. Must be one of `"ISO8601"`, `"EpochSeconds"` or `"Epoch"` (which is milliseconds). Defaults to `"ISO8601"`.
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
    <dd>{{% md %}}User-assigned target name. Use this value to differentiate between the link targets for a data link object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Flag that designates a target as the default for a data link object. `true` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>minimum<wbr>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The [minimum time window](https://developers.signalfx.com/administration/data_links_overview.html#_minimum_time_window) for a search sent to an external site. Defaults to `6000`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>property<wbr>Key<wbr>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Describes the relationship between SignalFx metadata keys and external system properties when the key names are different.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}[Designates the format](https://developers.signalfx.com/administration/data_links_overview.html#_minimum_time_window) of `minimum_time_window` in the same data link target object. Must be one of `"ISO8601"`, `"EpochSeconds"` or `"Epoch"` (which is milliseconds). Defaults to `"ISO8601"`.
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
    <dd>{{% md %}}User-assigned target name. Use this value to differentiate between the link targets for a data link object.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that designates a target as the default for a data link object. `true` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>minimum<wbr>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The [minimum time window](https://developers.signalfx.com/administration/data_links_overview.html#_minimum_time_window) for a search sent to an external site. Defaults to `6000`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>property<wbr>Key<wbr>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Describes the relationship between SignalFx metadata keys and external system properties when the key names are different.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}[Designates the format](https://developers.signalfx.com/administration/data_links_overview.html#_minimum_time_window) of `minimum_time_window` in the same data link target object. Must be one of `"ISO8601"`, `"EpochSeconds"` or `"Epoch"` (which is milliseconds). Defaults to `"ISO8601"`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Data<wbr>Link<wbr>Target<wbr>Signalfx<wbr>Dashboard</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#DataLinkTargetSignalfxDashboard">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#DataLinkTargetSignalfxDashboard">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DataLinkTargetSignalfxDashboardArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DataLinkTargetSignalfxDashboardOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dashboard<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SignalFx-assigned ID of the dashboard link target's dashboard group
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Dashboard<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SignalFx-assigned ID of the dashboard link target
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}User-assigned target name. Use this value to differentiate between the link targets for a data link object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that designates a target as the default for a data link object. `true` by default
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dashboard<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SignalFx-assigned ID of the dashboard link target's dashboard group
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Dashboard<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SignalFx-assigned ID of the dashboard link target
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}User-assigned target name. Use this value to differentiate between the link targets for a data link object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that designates a target as the default for a data link object. `true` by default
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dashboard<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SignalFx-assigned ID of the dashboard link target's dashboard group
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>dashboard<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}SignalFx-assigned ID of the dashboard link target
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}User-assigned target name. Use this value to differentiate between the link targets for a data link object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Flag that designates a target as the default for a data link object. `true` by default
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dashboard<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}SignalFx-assigned ID of the dashboard link target's dashboard group
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>dashboard<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}SignalFx-assigned ID of the dashboard link target
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}User-assigned target name. Use this value to differentiate between the link targets for a data link object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that designates a target as the default for a data link object. `true` by default
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Data<wbr>Link<wbr>Target<wbr>Splunk</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#DataLinkTargetSplunk">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#DataLinkTargetSplunk">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DataLinkTargetSplunkArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DataLinkTargetSplunkOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}User-assigned target name. Use this value to differentiate between the link targets for a data link object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that designates a target as the default for a data link object. `true` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Property<wbr>Key<wbr>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Describes the relationship between SignalFx metadata keys and external system properties when the key names are different.
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
    <dd>{{% md %}}User-assigned target name. Use this value to differentiate between the link targets for a data link object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that designates a target as the default for a data link object. `true` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Property<wbr>Key<wbr>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Describes the relationship between SignalFx metadata keys and external system properties when the key names are different.
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
    <dd>{{% md %}}User-assigned target name. Use this value to differentiate between the link targets for a data link object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Flag that designates a target as the default for a data link object. `true` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>property<wbr>Key<wbr>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Describes the relationship between SignalFx metadata keys and external system properties when the key names are different.
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
    <dd>{{% md %}}User-assigned target name. Use this value to differentiate between the link targets for a data link object.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that designates a target as the default for a data link object. `true` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>property<wbr>Key<wbr>Mapping</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Describes the relationship between SignalFx metadata keys and external system properties when the key names are different.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-signalfx">https://github.com/pulumi/pulumi-signalfx</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

