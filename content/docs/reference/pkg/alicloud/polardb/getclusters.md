
---
title: "GetClusters"
block_external_search_index: true
---



The `alicloud.polardb.getClusters` data source provides a collection of PolarDB clusters available in Alibaba Cloud account.
Filters support regular expression for the cluster description, searches by tags, and other filters which are listed below.

> **NOTE:** Available in v1.66.0+.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/polardb_clusters.html.markdown.





## Using GetClusters

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getClusters<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/polardb/#GetClustersArgs">GetClustersArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/polardb/#GetClustersResult">GetClustersResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_clusters(</span>db_type=None<span class="p">, </span>description_regex=None<span class="p">, </span>ids=None<span class="p">, </span>output_file=None<span class="p">, </span>status=None<span class="p">, </span>tags=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupClusters<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/polardb?tab=doc#LookupClustersArgs">LookupClustersArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/polardb?tab=doc#LookupClustersResult">LookupClustersResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetClusters </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Polardb.GetClustersResult.html">GetClustersResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.PolarDB.GetClustersArgs.html">GetClustersArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by cluster description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of PolarDB cluster IDs. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}status of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by cluster description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of PolarDB cluster IDs. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}status of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>db<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by cluster description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of PolarDB cluster IDs. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}status of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>db_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A regex string to filter results by cluster description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of PolarDB cluster IDs. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}status of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetClusters Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Clusters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getclusterscluster">List&lt;Get<wbr>Clusters<wbr>Cluster&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of PolarDB clusters. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}`Primary` for primary cluster, `ReadOnly` for read-only cluster, `Guard` for disaster recovery cluster, and `Temp` for temporary cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Descriptions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of RDS cluster descriptions. 
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
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of RDS cluster IDs. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Status of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Clusters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getclusterscluster">[]Get<wbr>Clusters<wbr>Cluster</a></span>
    </dt>
    <dd>{{% md %}}A list of PolarDB clusters. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}`Primary` for primary cluster, `ReadOnly` for read-only cluster, `Guard` for disaster recovery cluster, and `Temp` for temporary cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Descriptions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of RDS cluster descriptions. 
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
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of RDS cluster IDs. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Status of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>clusters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getclusterscluster">Get<wbr>Clusters<wbr>Cluster[]</a></span>
    </dt>
    <dd>{{% md %}}A list of PolarDB clusters. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}`Primary` for primary cluster, `ReadOnly` for read-only cluster, `Guard` for disaster recovery cluster, and `Temp` for temporary cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>descriptions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of RDS cluster descriptions. 
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
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of RDS cluster IDs. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Status of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>clusters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getclusterscluster">List[Get<wbr>Clusters<wbr>Cluster]</a></span>
    </dt>
    <dd>{{% md %}}A list of PolarDB clusters. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}`Primary` for primary cluster, `ReadOnly` for read-only cluster, `Guard` for disaster recovery cluster, and `Temp` for temporary cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>descriptions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of RDS cluster descriptions. 
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
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of RDS cluster IDs. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Status of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Clusters<wbr>Cluster</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetClustersCluster">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/polardb?tab=doc#GetClustersCluster">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Billing method. Value options: `PostPaid` for Pay-As-You-Go and `PrePaid` for subscription.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The create_time of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_class of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The DBNodeNumber of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getclustersclusterdbnode">List&lt;Get<wbr>Clusters<wbr>Cluster<wbr>Db<wbr>Node<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The DBNodes of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DBVersion of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Delete<wbr>Lock</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The DeleteLock of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Expire<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Expiration time. Pay-As-You-Go clusters never expire.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Expired</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The expired of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Lock<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The LockMode of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DBClusterNetworkType of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region_id of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}status of the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Used</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The StorageUsed of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the VPC the cluster belongs to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The zone_id of the db_nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Billing method. Value options: `PostPaid` for Pay-As-You-Go and `PrePaid` for subscription.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The create_time of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_class of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The DBNodeNumber of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getclustersclusterdbnode">[]Get<wbr>Clusters<wbr>Cluster<wbr>Db<wbr>Node</a></span>
    </dt>
    <dd>{{% md %}}The DBNodes of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DBVersion of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Delete<wbr>Lock</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The DeleteLock of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Expire<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Expiration time. Pay-As-You-Go clusters never expire.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Expired</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The expired of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Lock<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The LockMode of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DBClusterNetworkType of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region_id of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}status of the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Used</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The StorageUsed of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the VPC the cluster belongs to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The zone_id of the db_nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Billing method. Value options: `PostPaid` for Pay-As-You-Go and `PrePaid` for subscription.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The create_time of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_class of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Node<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The DBNodeNumber of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getclustersclusterdbnode">Get<wbr>Clusters<wbr>Cluster<wbr>Db<wbr>Node[]</a></span>
    </dt>
    <dd>{{% md %}}The DBNodes of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DBVersion of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>delete<wbr>Lock</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The DeleteLock of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>expire<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Expiration time. Pay-As-You-Go clusters never expire.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>expired</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The expired of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>lock<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The LockMode of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The DBClusterNetworkType of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region_id of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}status of the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Used</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The StorageUsed of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the VPC the cluster belongs to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The zone_id of the db_nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>charge_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Billing method. Value options: `PostPaid` for Pay-As-You-Go and `PrePaid` for subscription.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>create_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The create_time of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db_<wbr>node_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The db_node_class of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Node<wbr>Number</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The DBNodeNumber of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getclustersclusterdbnode">List[Get<wbr>Clusters<wbr>Cluster<wbr>Db<wbr>Node]</a></span>
    </dt>
    <dd>{{% md %}}The DBNodes of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The DBVersion of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>delete<wbr>Lock</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The DeleteLock of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Database type. Options are `MySQL`, `Oracle` and `PostgreSQL`. If no value is specified, all types are returned.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>expire<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Expiration time. Pay-As-You-Go clusters never expire.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>expired</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The expired of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>lock<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The LockMode of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The DBClusterNetworkType of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region_id of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}status of the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Used</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The StorageUsed of the PolarDB cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vpc_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the VPC the cluster belongs to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The zone_id of the db_nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Clusters<wbr>Cluster<wbr>Db<wbr>Node</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetClustersClusterDbNode">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/polardb?tab=doc#GetClustersClusterDbNode">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The create_time of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_class of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_id of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_role of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_status of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Connections</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The max_connections of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Iops</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The max_iops of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region_id of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The zone_id of the db_nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The create_time of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_class of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_id of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_role of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Node<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_status of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Connections</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The max_connections of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Iops</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The max_iops of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region_id of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The zone_id of the db_nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The create_time of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Node<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_class of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Node<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_id of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Node<wbr>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_role of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Node<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The db_node_status of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Connections</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The max_connections of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Iops</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The max_iops of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The region_id of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The zone_id of the db_nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>create_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The create_time of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db_<wbr>node_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The db_node_class of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Node<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The db_node_id of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Node<wbr>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The db_node_role of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Node<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The db_node_status of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max_<wbr>connections</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The max_connections of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Iops</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The max_iops of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>region<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region_id of the db_nodes.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The zone_id of the db_nodes.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







