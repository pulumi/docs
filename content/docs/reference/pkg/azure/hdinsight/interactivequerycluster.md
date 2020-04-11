
---
title: "InteractiveQueryCluster"
block_external_search_index: true
---



Manages a HDInsight Interactive Query Cluster.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_interactive_query_cluster.html.markdown.



## Create a InteractiveQueryCluster Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/hdinsight/#InteractiveQueryCluster">InteractiveQueryCluster</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/hdinsight/#InteractiveQueryClusterArgs">InteractiveQueryClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">InteractiveQueryCluster</span><span class="p">(resource_name, opts=None, </span>cluster_version=None<span class="p">, </span>component_version=None<span class="p">, </span>gateway=None<span class="p">, </span>location=None<span class="p">, </span>name=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>roles=None<span class="p">, </span>storage_account_gen2=None<span class="p">, </span>storage_accounts=None<span class="p">, </span>tags=None<span class="p">, </span>tier=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewInteractiveQueryCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterArgs">InteractiveQueryClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryCluster">InteractiveQueryCluster</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Hdinsight.InteractiveQueryCluster.html">InteractiveQueryCluster</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.HDInsight.InteractiveQueryClusterArgs.html">InteractiveQueryClusterArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Component<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustercomponentversion">Interactive<wbr>Query<wbr>Cluster<wbr>Component<wbr>Version<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `component_version` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustergateway">Interactive<wbr>Query<wbr>Cluster<wbr>Gateway<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `gateway` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroles">Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `roles` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Account<wbr>Gen2</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccountgen2">Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Gen2Args?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_account_gen2` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccount">List&lt;Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Component<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustercomponentversion">Interactive<wbr>Query<wbr>Cluster<wbr>Component<wbr>Version</a></span>
    </dt>
    <dd>{{% md %}}A `component_version` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustergateway">Interactive<wbr>Query<wbr>Cluster<wbr>Gateway</a></span>
    </dt>
    <dd>{{% md %}}A `gateway` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroles">Interactive<wbr>Query<wbr>Cluster<wbr>Roles</a></span>
    </dt>
    <dd>{{% md %}}A `roles` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Account<wbr>Gen2</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccountgen2">*Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Gen2</a></span>
    </dt>
    <dd>{{% md %}}A `storage_account_gen2` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccount">[]Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>component<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustercomponentversion">Interactive<wbr>Query<wbr>Cluster<wbr>Component<wbr>Version</a></span>
    </dt>
    <dd>{{% md %}}A `component_version` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustergateway">Interactive<wbr>Query<wbr>Cluster<wbr>Gateway</a></span>
    </dt>
    <dd>{{% md %}}A `gateway` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroles">Interactive<wbr>Query<wbr>Cluster<wbr>Roles</a></span>
    </dt>
    <dd>{{% md %}}A `roles` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Account<wbr>Gen2</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccountgen2">Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Gen2?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_account_gen2` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccount">Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cluster_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>component_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustercomponentversion">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Component<wbr>Version]</a></span>
    </dt>
    <dd>{{% md %}}A `component_version` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustergateway">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Gateway]</a></span>
    </dt>
    <dd>{{% md %}}A `gateway` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroles">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Roles]</a></span>
    </dt>
    <dd>{{% md %}}A `roles` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>account_<wbr>gen2</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccountgen2">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Gen2]</a></span>
    </dt>
    <dd>{{% md %}}A `storage_account_gen2` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccount">List[Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account]</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## InteractiveQueryCluster Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Component<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustercomponentversion">Interactive<wbr>Query<wbr>Cluster<wbr>Component<wbr>Version</a></span>
    </dt>
    <dd>{{% md %}}A `component_version` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustergateway">Interactive<wbr>Query<wbr>Cluster<wbr>Gateway</a></span>
    </dt>
    <dd>{{% md %}}A `gateway` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Https<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The HTTPS Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroles">Interactive<wbr>Query<wbr>Cluster<wbr>Roles</a></span>
    </dt>
    <dd>{{% md %}}A `roles` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ssh<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SSH Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Account<wbr>Gen2</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccountgen2">Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Gen2?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_account_gen2` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccount">List&lt;Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Component<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustercomponentversion">Interactive<wbr>Query<wbr>Cluster<wbr>Component<wbr>Version</a></span>
    </dt>
    <dd>{{% md %}}A `component_version` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustergateway">Interactive<wbr>Query<wbr>Cluster<wbr>Gateway</a></span>
    </dt>
    <dd>{{% md %}}A `gateway` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Https<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The HTTPS Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroles">Interactive<wbr>Query<wbr>Cluster<wbr>Roles</a></span>
    </dt>
    <dd>{{% md %}}A `roles` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ssh<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SSH Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Account<wbr>Gen2</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccountgen2">*Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Gen2</a></span>
    </dt>
    <dd>{{% md %}}A `storage_account_gen2` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccount">[]Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>component<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustercomponentversion">Interactive<wbr>Query<wbr>Cluster<wbr>Component<wbr>Version</a></span>
    </dt>
    <dd>{{% md %}}A `component_version` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustergateway">Interactive<wbr>Query<wbr>Cluster<wbr>Gateway</a></span>
    </dt>
    <dd>{{% md %}}A `gateway` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>https<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The HTTPS Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroles">Interactive<wbr>Query<wbr>Cluster<wbr>Roles</a></span>
    </dt>
    <dd>{{% md %}}A `roles` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ssh<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The SSH Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage<wbr>Account<wbr>Gen2</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccountgen2">Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Gen2?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_account_gen2` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccount">Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>cluster_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>component_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustercomponentversion">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Component<wbr>Version]</a></span>
    </dt>
    <dd>{{% md %}}A `component_version` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustergateway">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Gateway]</a></span>
    </dt>
    <dd>{{% md %}}A `gateway` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>https_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The HTTPS Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroles">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Roles]</a></span>
    </dt>
    <dd>{{% md %}}A `roles` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ssh_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SSH Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage_<wbr>account_<wbr>gen2</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccountgen2">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Gen2]</a></span>
    </dt>
    <dd>{{% md %}}A `storage_account_gen2` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage_<wbr>accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccount">List[Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account]</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing InteractiveQueryCluster Resource

Get an existing InteractiveQueryCluster resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/hdinsight/#InteractiveQueryClusterState">InteractiveQueryClusterState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/hdinsight/#InteractiveQueryCluster">InteractiveQueryCluster</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>cluster_version=None<span class="p">, </span>component_version=None<span class="p">, </span>gateway=None<span class="p">, </span>https_endpoint=None<span class="p">, </span>location=None<span class="p">, </span>name=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>roles=None<span class="p">, </span>ssh_endpoint=None<span class="p">, </span>storage_account_gen2=None<span class="p">, </span>storage_accounts=None<span class="p">, </span>tags=None<span class="p">, </span>tier=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetInteractiveQueryCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterState">InteractiveQueryClusterState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryCluster">InteractiveQueryCluster</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Hdinsight.InteractiveQueryCluster.html">InteractiveQueryCluster</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Hdinsight.InteractiveQueryClusterState.html">InteractiveQueryClusterState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Component<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustercomponentversion">Interactive<wbr>Query<wbr>Cluster<wbr>Component<wbr>Version<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `component_version` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustergateway">Interactive<wbr>Query<wbr>Cluster<wbr>Gateway<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `gateway` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The HTTPS Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroles">Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `roles` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssh<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The SSH Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Account<wbr>Gen2</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccountgen2">Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Gen2Args?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_account_gen2` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccount">List&lt;Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Component<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustercomponentversion">*Interactive<wbr>Query<wbr>Cluster<wbr>Component<wbr>Version</a></span>
    </dt>
    <dd>{{% md %}}A `component_version` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustergateway">*Interactive<wbr>Query<wbr>Cluster<wbr>Gateway</a></span>
    </dt>
    <dd>{{% md %}}A `gateway` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The HTTPS Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Roles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroles">*Interactive<wbr>Query<wbr>Cluster<wbr>Roles</a></span>
    </dt>
    <dd>{{% md %}}A `roles` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssh<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The SSH Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Account<wbr>Gen2</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccountgen2">*Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Gen2</a></span>
    </dt>
    <dd>{{% md %}}A `storage_account_gen2` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccount">[]Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>component<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustercomponentversion">Interactive<wbr>Query<wbr>Cluster<wbr>Component<wbr>Version?</a></span>
    </dt>
    <dd>{{% md %}}A `component_version` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustergateway">Interactive<wbr>Query<wbr>Cluster<wbr>Gateway?</a></span>
    </dt>
    <dd>{{% md %}}A `gateway` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The HTTPS Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroles">Interactive<wbr>Query<wbr>Cluster<wbr>Roles?</a></span>
    </dt>
    <dd>{{% md %}}A `roles` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssh<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The SSH Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Account<wbr>Gen2</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccountgen2">Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Gen2?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_account_gen2` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccount">Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>component_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustercomponentversion">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Component<wbr>Version]</a></span>
    </dt>
    <dd>{{% md %}}A `component_version` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gateway</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclustergateway">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Gateway]</a></span>
    </dt>
    <dd>{{% md %}}A `gateway` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The HTTPS Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Azure Region which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name for this HDInsight Interactive Query Cluster. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Resource Group in which this HDInsight Interactive Query Cluster should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>roles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroles">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Roles]</a></span>
    </dt>
    <dd>{{% md %}}A `roles` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssh_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The SSH Connectivity Endpoint for this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>account_<wbr>gen2</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccountgen2">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Gen2]</a></span>
    </dt>
    <dd>{{% md %}}A `storage_account_gen2` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterstorageaccount">List[Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account]</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A map of Tags which should be assigned to this HDInsight Interactive Query Cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the Tier which should be used for this HDInsight Interactive Query Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Interactive<wbr>Query<wbr>Cluster<wbr>Component<wbr>Version</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#InteractiveQueryClusterComponentVersion">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#InteractiveQueryClusterComponentVersion">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterComponentVersionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterComponentVersionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Interactive<wbr>Hive</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Interactive<wbr>Hive</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>interactive<wbr>Hive</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>interactive<wbr>Hive</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Interactive<wbr>Query<wbr>Cluster<wbr>Gateway</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#InteractiveQueryClusterGateway">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#InteractiveQueryClusterGateway">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterGatewayArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterGatewayOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the Ambari portal enabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The password used for the Ambari Portal. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username used for the Ambari Portal. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the Ambari portal enabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The password used for the Ambari Portal. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username used for the Ambari Portal. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is the Ambari portal enabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The password used for the Ambari Portal. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username used for the Ambari Portal. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is the Ambari portal enabled? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The password used for the Ambari Portal. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The username used for the Ambari Portal. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Interactive<wbr>Query<wbr>Cluster<wbr>Roles</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#InteractiveQueryClusterRoles">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#InteractiveQueryClusterRoles">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterRolesArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterRolesOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Head<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterrolesheadnode">Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Head<wbr>Node<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `head_node` block as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Worker<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterrolesworkernode">Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Worker<wbr>Node<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `worker_node` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zookeeper<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroleszookeepernode">Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Zookeeper<wbr>Node<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `zookeeper_node` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Head<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterrolesheadnode">Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Head<wbr>Node</a></span>
    </dt>
    <dd>{{% md %}}A `head_node` block as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Worker<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterrolesworkernode">Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Worker<wbr>Node</a></span>
    </dt>
    <dd>{{% md %}}A `worker_node` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zookeeper<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroleszookeepernode">Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Zookeeper<wbr>Node</a></span>
    </dt>
    <dd>{{% md %}}A `zookeeper_node` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>head<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterrolesheadnode">Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Head<wbr>Node</a></span>
    </dt>
    <dd>{{% md %}}A `head_node` block as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>worker<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterrolesworkernode">Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Worker<wbr>Node</a></span>
    </dt>
    <dd>{{% md %}}A `worker_node` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zookeeper<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroleszookeepernode">Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Zookeeper<wbr>Node</a></span>
    </dt>
    <dd>{{% md %}}A `zookeeper_node` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>head<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterrolesheadnode">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Head<wbr>Node]</a></span>
    </dt>
    <dd>{{% md %}}A `head_node` block as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>worker<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterrolesworkernode">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Worker<wbr>Node]</a></span>
    </dt>
    <dd>{{% md %}}A `worker_node` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zookeeper<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#interactivequeryclusterroleszookeepernode">Dict[Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Zookeeper<wbr>Node]</a></span>
    </dt>
    <dd>{{% md %}}A `zookeeper_node` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Head<wbr>Node</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#InteractiveQueryClusterRolesHeadNode">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#InteractiveQueryClusterRolesHeadNode">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterRolesHeadNodeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterRolesHeadNodeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Password associated with the local administrator for the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of SSH Keys which should be used for the local administrator on the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet within the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Username of the local administrator for the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual_<wbr>network_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network where the Head Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vm_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Size of the Virtual Machine which should be used as the Head Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Worker<wbr>Node</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#InteractiveQueryClusterRolesWorkerNode">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#InteractiveQueryClusterRolesWorkerNode">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterRolesWorkerNodeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterRolesWorkerNodeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of instances which should be run for the Worker Nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of instances which should be run for the Worker Nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of instances which should be run for the Worker Nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The minimum number of instances which should be run for the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Password associated with the local administrator for the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of SSH Keys which should be used for the local administrator on the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet within the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Instance<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of instances which should be run for the Worker Nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Username of the local administrator for the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual_<wbr>network_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network where the Worker Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vm_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Size of the Virtual Machine which should be used as the Worker Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Interactive<wbr>Query<wbr>Cluster<wbr>Roles<wbr>Zookeeper<wbr>Node</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#InteractiveQueryClusterRolesZookeeperNode">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#InteractiveQueryClusterRolesZookeeperNode">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterRolesZookeeperNodeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterRolesZookeeperNodeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual<wbr>Network<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vm<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Password associated with the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssh<wbr>Keys</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of SSH Keys which should be used for the local administrator on the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Subnet within the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Username of the local administrator for the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual_<wbr>network_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Virtual Network where the Zookeeper Nodes should be provisioned within. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vm_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Size of the Virtual Machine which should be used as the Zookeeper Nodes. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#InteractiveQueryClusterStorageAccount">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#InteractiveQueryClusterStorageAccount">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterStorageAccountArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterStorageAccountOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Container<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Storage Container. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Container<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Storage Container. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Account<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Container<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Storage Container. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage_<wbr>account_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Access Key which should be used to connect to the Storage Account. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage_<wbr>container_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Storage Container. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Interactive<wbr>Query<wbr>Cluster<wbr>Storage<wbr>Account<wbr>Gen2</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#InteractiveQueryClusterStorageAccountGen2">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#InteractiveQueryClusterStorageAccountGen2">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterStorageAccountGen2Args">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/hdinsight?tab=doc#InteractiveQueryClusterStorageAccountGen2Output">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Filesystem<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Managed<wbr>Identity<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Storage Account. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Filesystem<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Managed<wbr>Identity<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Storage Account. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>filesystem<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>managed<wbr>Identity<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Storage Account. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>filesystem<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Gen2 Filesystem. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Is this the Default Storage Account for the HDInsight Hadoop Cluster? Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>managed<wbr>Identity<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of Managed Identity to use for accessing the Gen2 filesystem. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Storage Account. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-azure">https://github.com/pulumi/pulumi-azure</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

