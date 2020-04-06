
---
title: "Cluster"
block_external_search_index: true
---



Manages a Cloud Dataproc cluster resource within GCP. For more information see
[the official dataproc documentation](https://cloud.google.com/dataproc/).


!> **Warning:** Due to limitations of the API, all arguments except
`labels`,`cluster_config.worker_config.num_instances` and `cluster_config.preemptible_worker_config.num_instances` are non-updatable. Changing others will cause recreation of the
whole cluster!

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dataproc_cluster.html.markdown.



## Create a Cluster Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/dataproc/#Cluster">Cluster</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/dataproc/#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Cluster</span><span class="p">(resource_name, opts=None, </span>cluster_config=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Dataproc.Cluster.html">Cluster</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Dataproc.ClusterArgs.html">ClusterArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Allows you to configure various aspects of the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which the cluster and associated nodes will be created in.
Defaults to `global`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfig">*Cluster<wbr>Cluster<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Allows you to configure various aspects of the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which the cluster and associated nodes will be created in.
Defaults to `global`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfig">Cluster<wbr>Cluster<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Allows you to configure various aspects of the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which the cluster and associated nodes will be created in.
Defaults to `global`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfig">Dict[Cluster<wbr>Cluster<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Allows you to configure various aspects of the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which the cluster and associated nodes will be created in.
Defaults to `global`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Cluster Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfig">Cluster<wbr>Cluster<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Allows you to configure various aspects of the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string></span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which the cluster and associated nodes will be created in.
Defaults to `global`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfig">Cluster<wbr>Cluster<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Allows you to configure various aspects of the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which the cluster and associated nodes will be created in.
Defaults to `global`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfig">Cluster<wbr>Cluster<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Allows you to configure various aspects of the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which the cluster and associated nodes will be created in.
Defaults to `global`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>cluster_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfig">Dict[Cluster<wbr>Cluster<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Allows you to configure various aspects of the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which the cluster and associated nodes will be created in.
Defaults to `global`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Cluster Resource

Get an existing Cluster resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/dataproc/#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/dataproc/#Cluster">Cluster</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>cluster_config=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Dataproc.Cluster.html">Cluster</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Dataproc.ClusterState.html">ClusterState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Allows you to configure various aspects of the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which the cluster and associated nodes will be created in.
Defaults to `global`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfig">*Cluster<wbr>Cluster<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Allows you to configure various aspects of the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region in which the cluster and associated nodes will be created in.
Defaults to `global`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfig">Cluster<wbr>Cluster<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Allows you to configure various aspects of the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region in which the cluster and associated nodes will be created in.
Defaults to `global`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfig">Dict[Cluster<wbr>Cluster<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Allows you to configure various aspects of the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region in which the cluster and associated nodes will be created in.
Defaults to `global`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Cluster<wbr>Cluster<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Autoscaling<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigautoscalingconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Autoscaling<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The autoscaling policy config associated with the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encryption<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigencryptionconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Encryption<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The Customer managed encryption keys settings for the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gce<wbr>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfiggceclusterconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Gce<wbr>Cluster<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Common config settings for resources of Google Compute Engine cluster
instances, applicable to all instances in the cluster. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initialization<wbr>Actions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfiginitializationaction">List&lt;Cluster<wbr>Cluster<wbr>Config<wbr>Initialization<wbr>Action<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Commands to execute on each node after config is completed.
You can specify multiple versions of these. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lifecycle<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfiglifecycleconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Lifecycle<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigmasterconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The Google Compute Engine config settings for the master instances
in a cluster.. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preemptible<wbr>Worker<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigpreemptibleworkerconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Preemptible<wbr>Worker<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The Google Compute Engine config settings for the additional (aka
preemptible) instances in a cluster. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigsecurityconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Security<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Security related configuration. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Software<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigsoftwareconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Software<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The config settings for software inside the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Staging<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage staging bucket used to stage files,
such as Hadoop jars, between client machines and the cluster.
Note: If you don't explicitly specify a `staging_bucket`
then GCP will auto create / assign one for you. However, you are not guaranteed
an auto generated bucket which is solely dedicated to your cluster; it may be shared
with other clusters in the same region/zone also choosing to use the auto generation
option.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Worker<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigworkerconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The Google Compute Engine config settings for the worker instances
in a cluster.. Structure defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Autoscaling<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigautoscalingconfig">*Cluster<wbr>Cluster<wbr>Config<wbr>Autoscaling<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The autoscaling policy config associated with the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encryption<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigencryptionconfig">*Cluster<wbr>Cluster<wbr>Config<wbr>Encryption<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The Customer managed encryption keys settings for the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gce<wbr>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfiggceclusterconfig">*Cluster<wbr>Cluster<wbr>Config<wbr>Gce<wbr>Cluster<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Common config settings for resources of Google Compute Engine cluster
instances, applicable to all instances in the cluster. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initialization<wbr>Actions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfiginitializationaction">[]Cluster<wbr>Cluster<wbr>Config<wbr>Initialization<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}Commands to execute on each node after config is completed.
You can specify multiple versions of these. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lifecycle<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfiglifecycleconfig">*Cluster<wbr>Cluster<wbr>Config<wbr>Lifecycle<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigmasterconfig">*Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The Google Compute Engine config settings for the master instances
in a cluster.. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preemptible<wbr>Worker<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigpreemptibleworkerconfig">*Cluster<wbr>Cluster<wbr>Config<wbr>Preemptible<wbr>Worker<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The Google Compute Engine config settings for the additional (aka
preemptible) instances in a cluster. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigsecurityconfig">*Cluster<wbr>Cluster<wbr>Config<wbr>Security<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Security related configuration. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Software<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigsoftwareconfig">*Cluster<wbr>Cluster<wbr>Config<wbr>Software<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The config settings for software inside the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Staging<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage staging bucket used to stage files,
such as Hadoop jars, between client machines and the cluster.
Note: If you don't explicitly specify a `staging_bucket`
then GCP will auto create / assign one for you. However, you are not guaranteed
an auto generated bucket which is solely dedicated to your cluster; it may be shared
with other clusters in the same region/zone also choosing to use the auto generation
option.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Worker<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigworkerconfig">*Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The Google Compute Engine config settings for the worker instances
in a cluster.. Structure defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>autoscaling<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigautoscalingconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Autoscaling<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The autoscaling policy config associated with the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encryption<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigencryptionconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Encryption<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The Customer managed encryption keys settings for the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gce<wbr>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfiggceclusterconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Gce<wbr>Cluster<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Common config settings for resources of Google Compute Engine cluster
instances, applicable to all instances in the cluster. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initialization<wbr>Actions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfiginitializationaction">Cluster<wbr>Cluster<wbr>Config<wbr>Initialization<wbr>Action[]?</a></span>
    </dt>
    <dd>{{% md %}}Commands to execute on each node after config is completed.
You can specify multiple versions of these. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lifecycle<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfiglifecycleconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Lifecycle<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigmasterconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The Google Compute Engine config settings for the master instances
in a cluster.. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preemptible<wbr>Worker<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigpreemptibleworkerconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Preemptible<wbr>Worker<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The Google Compute Engine config settings for the additional (aka
preemptible) instances in a cluster. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigsecurityconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Security<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Security related configuration. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>software<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigsoftwareconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Software<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The config settings for software inside the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>staging<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage staging bucket used to stage files,
such as Hadoop jars, between client machines and the cluster.
Note: If you don't explicitly specify a `staging_bucket`
then GCP will auto create / assign one for you. However, you are not guaranteed
an auto generated bucket which is solely dedicated to your cluster; it may be shared
with other clusters in the same region/zone also choosing to use the auto generation
option.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>worker<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigworkerconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The Google Compute Engine config settings for the worker instances
in a cluster.. Structure defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>autoscaling<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigautoscalingconfig">Dict[Cluster<wbr>Cluster<wbr>Config<wbr>Autoscaling<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The autoscaling policy config associated with the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encryption<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigencryptionconfig">Dict[Cluster<wbr>Cluster<wbr>Config<wbr>Encryption<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The Customer managed encryption keys settings for the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gce<wbr>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfiggceclusterconfig">Dict[Cluster<wbr>Cluster<wbr>Config<wbr>Gce<wbr>Cluster<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Common config settings for resources of Google Compute Engine cluster
instances, applicable to all instances in the cluster. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initialization<wbr>Actions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfiginitializationaction">List[Cluster<wbr>Cluster<wbr>Config<wbr>Initialization<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}Commands to execute on each node after config is completed.
You can specify multiple versions of these. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lifecycle<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfiglifecycleconfig">Dict[Cluster<wbr>Cluster<wbr>Config<wbr>Lifecycle<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigmasterconfig">Dict[Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The Google Compute Engine config settings for the master instances
in a cluster.. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preemptible<wbr>Worker<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigpreemptibleworkerconfig">Dict[Cluster<wbr>Cluster<wbr>Config<wbr>Preemptible<wbr>Worker<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The Google Compute Engine config settings for the additional (aka
preemptible) instances in a cluster. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigsecurityconfig">Dict[Cluster<wbr>Cluster<wbr>Config<wbr>Security<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Security related configuration. Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>software<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigsoftwareconfig">Dict[Cluster<wbr>Cluster<wbr>Config<wbr>Software<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The config settings for software inside the cluster.
Structure defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>staging<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage staging bucket used to stage files,
such as Hadoop jars, between client machines and the cluster.
Note: If you don't explicitly specify a `staging_bucket`
then GCP will auto create / assign one for you. However, you are not guaranteed
an auto generated bucket which is solely dedicated to your cluster; it may be shared
with other clusters in the same region/zone also choosing to use the auto generation
option.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>worker_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigworkerconfig">Dict[Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The Google Compute Engine config settings for the worker instances
in a cluster.. Structure defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Autoscaling<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigAutoscalingConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigAutoscalingConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigAutoscalingConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigAutoscalingConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Policy<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The autoscaling policy used by the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Policy<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The autoscaling policy used by the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>policy<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The autoscaling policy used by the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>policy<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The autoscaling policy used by the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Encryption<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigEncryptionConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigEncryptionConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigEncryptionConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigEncryptionConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cloud KMS key name to use for PD disk encryption for
all instances in the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cloud KMS key name to use for PD disk encryption for
all instances in the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>kms<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cloud KMS key name to use for PD disk encryption for
all instances in the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>kms_<wbr>key_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cloud KMS key name to use for PD disk encryption for
all instances in the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Gce<wbr>Cluster<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigGceClusterConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigGceClusterConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigGceClusterConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigGceClusterConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Internal<wbr>Ip<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}By default, clusters are not restricted to internal IP addresses, 
and will have ephemeral external IP addresses assigned to each instance. If set to true, all
instances in the cluster will only have internal IP addresses. Note: Private Google Access
(also known as `privateIpGoogleAccess`) must be enabled on the subnetwork that the cluster
will be launched in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A map of the Compute Engine metadata entries to add to all instances
(see [Project and instance metadata](https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata)).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to the cluster will be part of. Conflicts with `subnetwork`.
If neither is specified, this defaults to the "default" network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes
to be made available on all of the node VMs under the `service_account`
specified. These can be	either FQDNs, or scope aliases. The following scopes
must be set if any other scopes are set. They're necessary to ensure the
correct functioning ofthe cluster, and are set automatically by the API:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork the cluster will be part of. Conflicts with `network`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of instance tags applied to instances in the cluster.
Tags are used to identify valid sources or targets for network firewalls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The GCP zone where your data is stored and used (i.e. where
the master and the worker nodes will be created in). If `region` is set to 'global' (default)
then `zone` is mandatory, otherwise GCP is able to make use of [Auto Zone Placement](https://cloud.google.com/dataproc/docs/concepts/auto-zone)
to determine this automatically for you.
Note: This setting additionally determines and restricts
which computing resources are available for use with other configs such as
`cluster_config.master_config.machine_type` and `cluster_config.worker_config.machine_type`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Internal<wbr>Ip<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}By default, clusters are not restricted to internal IP addresses, 
and will have ephemeral external IP addresses assigned to each instance. If set to true, all
instances in the cluster will only have internal IP addresses. Note: Private Google Access
(also known as `privateIpGoogleAccess`) must be enabled on the subnetwork that the cluster
will be launched in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A map of the Compute Engine metadata entries to add to all instances
(see [Project and instance metadata](https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata)).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to the cluster will be part of. Conflicts with `subnetwork`.
If neither is specified, this defaults to the "default" network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes
to be made available on all of the node VMs under the `service_account`
specified. These can be	either FQDNs, or scope aliases. The following scopes
must be set if any other scopes are set. They're necessary to ensure the
correct functioning ofthe cluster, and are set automatically by the API:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork the cluster will be part of. Conflicts with `network`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of instance tags applied to instances in the cluster.
Tags are used to identify valid sources or targets for network firewalls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The GCP zone where your data is stored and used (i.e. where
the master and the worker nodes will be created in). If `region` is set to 'global' (default)
then `zone` is mandatory, otherwise GCP is able to make use of [Auto Zone Placement](https://cloud.google.com/dataproc/docs/concepts/auto-zone)
to determine this automatically for you.
Note: This setting additionally determines and restricts
which computing resources are available for use with other configs such as
`cluster_config.master_config.machine_type` and `cluster_config.worker_config.machine_type`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>internal<wbr>Ip<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}By default, clusters are not restricted to internal IP addresses, 
and will have ephemeral external IP addresses assigned to each instance. If set to true, all
instances in the cluster will only have internal IP addresses. Note: Private Google Access
(also known as `privateIpGoogleAccess`) must be enabled on the subnetwork that the cluster
will be launched in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A map of the Compute Engine metadata entries to add to all instances
(see [Project and instance metadata](https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata)).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to the cluster will be part of. Conflicts with `subnetwork`.
If neither is specified, this defaults to the "default" network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes
to be made available on all of the node VMs under the `service_account`
specified. These can be	either FQDNs, or scope aliases. The following scopes
must be set if any other scopes are set. They're necessary to ensure the
correct functioning ofthe cluster, and are set automatically by the API:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork the cluster will be part of. Conflicts with `network`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of instance tags applied to instances in the cluster.
Tags are used to identify valid sources or targets for network firewalls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The GCP zone where your data is stored and used (i.e. where
the master and the worker nodes will be created in). If `region` is set to 'global' (default)
then `zone` is mandatory, otherwise GCP is able to make use of [Auto Zone Placement](https://cloud.google.com/dataproc/docs/concepts/auto-zone)
to determine this automatically for you.
Note: This setting additionally determines and restricts
which computing resources are available for use with other configs such as
`cluster_config.master_config.machine_type` and `cluster_config.worker_config.machine_type`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>internal<wbr>Ip<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}By default, clusters are not restricted to internal IP addresses, 
and will have ephemeral external IP addresses assigned to each instance. If set to true, all
instances in the cluster will only have internal IP addresses. Note: Private Google Access
(also known as `privateIpGoogleAccess`) must be enabled on the subnetwork that the cluster
will be launched in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A map of the Compute Engine metadata entries to add to all instances
(see [Project and instance metadata](https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata)).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to the cluster will be part of. Conflicts with `subnetwork`.
If neither is specified, this defaults to the "default" network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>account</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes
to be made available on all of the node VMs under the `service_account`
specified. These can be	either FQDNs, or scope aliases. The following scopes
must be set if any other scopes are set. They're necessary to ensure the
correct functioning ofthe cluster, and are set automatically by the API:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork the cluster will be part of. Conflicts with `network`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of instance tags applied to instances in the cluster.
Tags are used to identify valid sources or targets for network firewalls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The GCP zone where your data is stored and used (i.e. where
the master and the worker nodes will be created in). If `region` is set to 'global' (default)
then `zone` is mandatory, otherwise GCP is able to make use of [Auto Zone Placement](https://cloud.google.com/dataproc/docs/concepts/auto-zone)
to determine this automatically for you.
Note: This setting additionally determines and restricts
which computing resources are available for use with other configs such as
`cluster_config.master_config.machine_type` and `cluster_config.worker_config.machine_type`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Initialization<wbr>Action</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigInitializationAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigInitializationAction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigInitializationActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigInitializationActionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum duration (in seconds) which `script` is
allowed to take to execute its action. GCP will default to a predetermined
computed value if not set (currently 300).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum duration (in seconds) which `script` is
allowed to take to execute its action. GCP will default to a predetermined
computed value if not set (currently 300).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>script</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout<wbr>Sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum duration (in seconds) which `script` is
allowed to take to execute its action. GCP will default to a predetermined
computed value if not set (currently 300).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>script</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout_<wbr>sec</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum duration (in seconds) which `script` is
allowed to take to execute its action. GCP will default to a predetermined
computed value if not set (currently 300).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Lifecycle<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigLifecycleConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigLifecycleConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigLifecycleConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigLifecycleConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Delete<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The time when cluster will be auto-deleted.
A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
Example: "2014-10-02T15:01:23.045123456Z".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Idle<wbr>Delete<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The duration to keep the cluster alive while idling
(no jobs running). After this TTL, the cluster will be deleted. Valid range: [10m, 14d].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Idle<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Delete<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The time when cluster will be auto-deleted.
A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
Example: "2014-10-02T15:01:23.045123456Z".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Idle<wbr>Delete<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The duration to keep the cluster alive while idling
(no jobs running). After this TTL, the cluster will be deleted. Valid range: [10m, 14d].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Idle<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Delete<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The time when cluster will be auto-deleted.
A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
Example: "2014-10-02T15:01:23.045123456Z".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>idle<wbr>Delete<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The duration to keep the cluster alive while idling
(no jobs running). After this TTL, the cluster will be deleted. Valid range: [10m, 14d].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>idle<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Delete<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time when cluster will be auto-deleted.
A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
Example: "2014-10-02T15:01:23.045123456Z".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>idle<wbr>Delete<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The duration to keep the cluster alive while idling
(no jobs running). After this TTL, the cluster will be deleted. Valid range: [10m, 14d].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>idle<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigMasterConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigMasterConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigMasterConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigMasterConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigmasterconfigaccelerator">List&lt;Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config<wbr>Accelerator<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The Compute Engine accelerator configuration for these instances. Can be specified multiple times.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigmasterconfigdiskconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config<wbr>Disk<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Disk Config
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URI for the image to use for this worker.  See [the guide](https://cloud.google.com/dataproc/docs/guides/dataproc-images)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently `n1-standard-4`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a minimum generation of CPU family
for the master. If not specified, GCP will default to a predetermined computed value
for each zone. See [the guide](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for details about which CPU families are available (and defaulted) for each zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigmasterconfigaccelerator">[]Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config<wbr>Accelerator</a></span>
    </dt>
    <dd>{{% md %}}The Compute Engine accelerator configuration for these instances. Can be specified multiple times.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigmasterconfigdiskconfig">*Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config<wbr>Disk<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Disk Config
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The URI for the image to use for this worker.  See [the guide](https://cloud.google.com/dataproc/docs/guides/dataproc-images)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently `n1-standard-4`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of a minimum generation of CPU family
for the master. If not specified, GCP will default to a predetermined computed value
for each zone. See [the guide](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for details about which CPU families are available (and defaulted) for each zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigmasterconfigaccelerator">Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config<wbr>Accelerator[]?</a></span>
    </dt>
    <dd>{{% md %}}The Compute Engine accelerator configuration for these instances. Can be specified multiple times.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigmasterconfigdiskconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config<wbr>Disk<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Disk Config
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URI for the image to use for this worker.  See [the guide](https://cloud.google.com/dataproc/docs/guides/dataproc-images)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently `n1-standard-4`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a minimum generation of CPU family
for the master. If not specified, GCP will default to a predetermined computed value
for each zone. See [the guide](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for details about which CPU families are available (and defaulted) for each zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigmasterconfigaccelerator">List[Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config<wbr>Accelerator]</a></span>
    </dt>
    <dd>{{% md %}}The Compute Engine accelerator configuration for these instances. Can be specified multiple times.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigmasterconfigdiskconfig">Dict[Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config<wbr>Disk<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Disk Config
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URI for the image to use for this worker.  See [the guide](https://cloud.google.com/dataproc/docs/guides/dataproc-images)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>machine_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently `n1-standard-4`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of a minimum generation of CPU family
for the master. If not specified, GCP will default to a predetermined computed value
for each zone. See [the guide](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for details about which CPU families are available (and defaulted) for each zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config<wbr>Accelerator</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigMasterConfigAccelerator">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigMasterConfigAccelerator">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigMasterConfigAcceleratorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigMasterConfigAcceleratorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Accelerator<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of the accelerator cards of this type exposed to this instance. Often restricted to one of `1`, `2`, `4`, or `8`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The short name of the accelerator type to expose to this instance. For example, `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Accelerator<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of the accelerator cards of this type exposed to this instance. Often restricted to one of `1`, `2`, `4`, or `8`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The short name of the accelerator type to expose to this instance. For example, `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>accelerator<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of the accelerator cards of this type exposed to this instance. Often restricted to one of `1`, `2`, `4`, or `8`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The short name of the accelerator type to expose to this instance. For example, `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>accelerator<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of the accelerator cards of this type exposed to this instance. Often restricted to one of `1`, `2`, `4`, or `8`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>accelerator_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The short name of the accelerator type to expose to this instance. For example, `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Master<wbr>Config<wbr>Disk<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigMasterConfigDiskConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigMasterConfigDiskConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigMasterConfigDiskConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigMasterConfigDiskConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The disk type of the primary disk attached to each preemptible worker node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Local<wbr>Ssds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The disk type of the primary disk attached to each preemptible worker node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Local<wbr>Ssds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The disk type of the primary disk attached to each preemptible worker node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Local<wbr>Ssds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The disk type of the primary disk attached to each preemptible worker node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Local<wbr>Ssds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Preemptible<wbr>Worker<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigPreemptibleWorkerConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigPreemptibleWorkerConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigPreemptibleWorkerConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigPreemptibleWorkerConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigpreemptibleworkerconfigdiskconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Preemptible<wbr>Worker<wbr>Config<wbr>Disk<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Disk Config
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigpreemptibleworkerconfigdiskconfig">*Cluster<wbr>Cluster<wbr>Config<wbr>Preemptible<wbr>Worker<wbr>Config<wbr>Disk<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Disk Config
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigpreemptibleworkerconfigdiskconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Preemptible<wbr>Worker<wbr>Config<wbr>Disk<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Disk Config
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigpreemptibleworkerconfigdiskconfig">Dict[Cluster<wbr>Cluster<wbr>Config<wbr>Preemptible<wbr>Worker<wbr>Config<wbr>Disk<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Disk Config
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Preemptible<wbr>Worker<wbr>Config<wbr>Disk<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigPreemptibleWorkerConfigDiskConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigPreemptibleWorkerConfigDiskConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigPreemptibleWorkerConfigDiskConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigPreemptibleWorkerConfigDiskConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The disk type of the primary disk attached to each preemptible worker node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Local<wbr>Ssds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The disk type of the primary disk attached to each preemptible worker node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Local<wbr>Ssds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The disk type of the primary disk attached to each preemptible worker node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Local<wbr>Ssds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The disk type of the primary disk attached to each preemptible worker node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Local<wbr>Ssds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Security<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigSecurityConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigSecurityConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigSecurityConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigSecurityConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Kerberos<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigsecurityconfigkerberosconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Security<wbr>Config<wbr>Kerberos<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Kerberos Configuration
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Kerberos<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigsecurityconfigkerberosconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Security<wbr>Config<wbr>Kerberos<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Kerberos Configuration
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>kerberos<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigsecurityconfigkerberosconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Security<wbr>Config<wbr>Kerberos<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Kerberos Configuration
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>kerberos<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigsecurityconfigkerberosconfig">Dict[Cluster<wbr>Cluster<wbr>Config<wbr>Security<wbr>Config<wbr>Kerberos<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Kerberos Configuration
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Security<wbr>Config<wbr>Kerberos<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigSecurityConfigKerberosConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigSecurityConfigKerberosConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigSecurityConfigKerberosConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigSecurityConfigKerberosConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cross<wbr>Realm<wbr>Trust<wbr>Admin<wbr>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The admin server (IP or hostname) for the
remote trusted realm in a cross realm trust relationship.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cross<wbr>Realm<wbr>Trust<wbr>Kdc</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The KDC (IP or hostname) for the
remote trusted realm in a cross realm trust relationship.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cross<wbr>Realm<wbr>Trust<wbr>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The remote realm the Dataproc on-cluster KDC will
trust, should the user enable cross realm trust.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cross<wbr>Realm<wbr>Trust<wbr>Shared<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS
encrypted file containing the shared password between the on-cluster Kerberos realm
and the remote trusted realm, in a cross realm trust relationship.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Kerberos</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag to indicate whether to Kerberize the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kdc<wbr>Db<wbr>Key<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file containing
the master key of the KDC database.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file containing
the password to the user provided key. For the self-signed certificate, this password
is generated by Dataproc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Keystore<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file containing
the password to the user provided keystore. For the self-signed certificated, the password
is generated by Dataproc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Keystore<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of the keystore file used for SSL encryption.
If not provided, Dataproc will provide a self-signed certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the KMS key used to encrypt various sensitive files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the on-cluster Kerberos realm. If not specified, the
uppercased domain of hostnames will be the realm.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Root<wbr>Principal<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file
containing the root principal password.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tgt<wbr>Lifetime<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The lifetime of the ticket granting ticket, in hours.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Truststore<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file
containing the password to the user provided truststore. For the self-signed
certificate, this password is generated by Dataproc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Truststore<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of the truststore file used for
SSL encryption. If not provided, Dataproc will provide a self-signed certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cross<wbr>Realm<wbr>Trust<wbr>Admin<wbr>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The admin server (IP or hostname) for the
remote trusted realm in a cross realm trust relationship.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cross<wbr>Realm<wbr>Trust<wbr>Kdc</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The KDC (IP or hostname) for the
remote trusted realm in a cross realm trust relationship.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cross<wbr>Realm<wbr>Trust<wbr>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The remote realm the Dataproc on-cluster KDC will
trust, should the user enable cross realm trust.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cross<wbr>Realm<wbr>Trust<wbr>Shared<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS
encrypted file containing the shared password between the on-cluster Kerberos realm
and the remote trusted realm, in a cross realm trust relationship.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Kerberos</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag to indicate whether to Kerberize the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kdc<wbr>Db<wbr>Key<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file containing
the master key of the KDC database.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file containing
the password to the user provided key. For the self-signed certificate, this password
is generated by Dataproc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Keystore<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file containing
the password to the user provided keystore. For the self-signed certificated, the password
is generated by Dataproc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Keystore<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of the keystore file used for SSL encryption.
If not provided, Dataproc will provide a self-signed certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the KMS key used to encrypt various sensitive files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the on-cluster Kerberos realm. If not specified, the
uppercased domain of hostnames will be the realm.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Root<wbr>Principal<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file
containing the root principal password.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tgt<wbr>Lifetime<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The lifetime of the ticket granting ticket, in hours.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Truststore<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file
containing the password to the user provided truststore. For the self-signed
certificate, this password is generated by Dataproc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Truststore<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of the truststore file used for
SSL encryption. If not provided, Dataproc will provide a self-signed certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cross<wbr>Realm<wbr>Trust<wbr>Admin<wbr>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The admin server (IP or hostname) for the
remote trusted realm in a cross realm trust relationship.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cross<wbr>Realm<wbr>Trust<wbr>Kdc</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The KDC (IP or hostname) for the
remote trusted realm in a cross realm trust relationship.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cross<wbr>Realm<wbr>Trust<wbr>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The remote realm the Dataproc on-cluster KDC will
trust, should the user enable cross realm trust.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cross<wbr>Realm<wbr>Trust<wbr>Shared<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS
encrypted file containing the shared password between the on-cluster Kerberos realm
and the remote trusted realm, in a cross realm trust relationship.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Kerberos</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag to indicate whether to Kerberize the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kdc<wbr>Db<wbr>Key<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file containing
the master key of the KDC database.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file containing
the password to the user provided key. For the self-signed certificate, this password
is generated by Dataproc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>keystore<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file containing
the password to the user provided keystore. For the self-signed certificated, the password
is generated by Dataproc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>keystore<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of the keystore file used for SSL encryption.
If not provided, Dataproc will provide a self-signed certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>kms<wbr>Key<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the KMS key used to encrypt various sensitive files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the on-cluster Kerberos realm. If not specified, the
uppercased domain of hostnames will be the realm.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>root<wbr>Principal<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file
containing the root principal password.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tgt<wbr>Lifetime<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The lifetime of the ticket granting ticket, in hours.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>truststore<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file
containing the password to the user provided truststore. For the self-signed
certificate, this password is generated by Dataproc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>truststore<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of the truststore file used for
SSL encryption. If not provided, Dataproc will provide a self-signed certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cross<wbr>Realm<wbr>Trust<wbr>Admin<wbr>Server</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The admin server (IP or hostname) for the
remote trusted realm in a cross realm trust relationship.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cross<wbr>Realm<wbr>Trust<wbr>Kdc</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The KDC (IP or hostname) for the
remote trusted realm in a cross realm trust relationship.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cross<wbr>Realm<wbr>Trust<wbr>Realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The remote realm the Dataproc on-cluster KDC will
trust, should the user enable cross realm trust.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cross<wbr>Realm<wbr>Trust<wbr>Shared<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS
encrypted file containing the shared password between the on-cluster Kerberos realm
and the remote trusted realm, in a cross realm trust relationship.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Kerberos</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag to indicate whether to Kerberize the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kdc<wbr>Db<wbr>Key<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file containing
the master key of the KDC database.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file containing
the password to the user provided key. For the self-signed certificate, this password
is generated by Dataproc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>keystore<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file containing
the password to the user provided keystore. For the self-signed certificated, the password
is generated by Dataproc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>keystore<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of the keystore file used for SSL encryption.
If not provided, Dataproc will provide a self-signed certificate.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>kms<wbr>Key<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URI of the KMS key used to encrypt various sensitive files.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>realm</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the on-cluster Kerberos realm. If not specified, the
uppercased domain of hostnames will be the realm.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>root<wbr>Principal<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file
containing the root principal password.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tgt<wbr>Lifetime<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The lifetime of the ticket granting ticket, in hours.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>truststore<wbr>Password<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of a KMS encrypted file
containing the password to the user provided truststore. For the self-signed
certificate, this password is generated by Dataproc.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>truststore<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cloud Storage URI of the truststore file used for
SSL encryption. If not provided, Dataproc will provide a self-signed certificate.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Software<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigSoftwareConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigSoftwareConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigSoftwareConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigSoftwareConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Dataproc image version to use
for the cluster - this controls the sets of software versions
installed onto the nodes when you create clusters. If not specified, defaults to the
latest version. For a list of valid versions see
[Cloud Dataproc versions](https://cloud.google.com/dataproc/docs/concepts/dataproc-versions)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional<wbr>Components</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Override<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A list of override and additional properties (key/value pairs)
used to modify various aspects of the common configuration files used when creating
a cluster. For a list of valid properties please see
[Cluster properties](https://cloud.google.com/dataproc/docs/concepts/cluster-properties)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Cloud Dataproc image version to use
for the cluster - this controls the sets of software versions
installed onto the nodes when you create clusters. If not specified, defaults to the
latest version. For a list of valid versions see
[Cloud Dataproc versions](https://cloud.google.com/dataproc/docs/concepts/dataproc-versions)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Optional<wbr>Components</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Override<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A list of override and additional properties (key/value pairs)
used to modify various aspects of the common configuration files used when creating
a cluster. For a list of valid properties please see
[Cluster properties](https://cloud.google.com/dataproc/docs/concepts/cluster-properties)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud Dataproc image version to use
for the cluster - this controls the sets of software versions
installed onto the nodes when you create clusters. If not specified, defaults to the
latest version. For a list of valid versions see
[Cloud Dataproc versions](https://cloud.google.com/dataproc/docs/concepts/dataproc-versions)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional<wbr>Components</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>override<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A list of override and additional properties (key/value pairs)
used to modify various aspects of the common configuration files used when creating
a cluster. For a list of valid properties please see
[Cluster properties](https://cloud.google.com/dataproc/docs/concepts/cluster-properties)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cloud Dataproc image version to use
for the cluster - this controls the sets of software versions
installed onto the nodes when you create clusters. If not specified, defaults to the
latest version. For a list of valid versions see
[Cloud Dataproc versions](https://cloud.google.com/dataproc/docs/concepts/dataproc-versions)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>optional<wbr>Components</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>override<wbr>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A list of override and additional properties (key/value pairs)
used to modify various aspects of the common configuration files used when creating
a cluster. For a list of valid properties please see
[Cluster properties](https://cloud.google.com/dataproc/docs/concepts/cluster-properties)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigWorkerConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigWorkerConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigWorkerConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigWorkerConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigworkerconfigaccelerator">List&lt;Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config<wbr>Accelerator<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The Compute Engine accelerator configuration for these instances. Can be specified multiple times.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigworkerconfigdiskconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config<wbr>Disk<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Disk Config
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URI for the image to use for this worker.  See [the guide](https://cloud.google.com/dataproc/docs/guides/dataproc-images)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently `n1-standard-4`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a minimum generation of CPU family
for the master. If not specified, GCP will default to a predetermined computed value
for each zone. See [the guide](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for details about which CPU families are available (and defaulted) for each zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigworkerconfigaccelerator">[]Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config<wbr>Accelerator</a></span>
    </dt>
    <dd>{{% md %}}The Compute Engine accelerator configuration for these instances. Can be specified multiple times.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigworkerconfigdiskconfig">*Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config<wbr>Disk<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Disk Config
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The URI for the image to use for this worker.  See [the guide](https://cloud.google.com/dataproc/docs/guides/dataproc-images)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently `n1-standard-4`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of a minimum generation of CPU family
for the master. If not specified, GCP will default to a predetermined computed value
for each zone. See [the guide](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for details about which CPU families are available (and defaulted) for each zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigworkerconfigaccelerator">Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config<wbr>Accelerator[]?</a></span>
    </dt>
    <dd>{{% md %}}The Compute Engine accelerator configuration for these instances. Can be specified multiple times.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigworkerconfigdiskconfig">Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config<wbr>Disk<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Disk Config
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URI for the image to use for this worker.  See [the guide](https://cloud.google.com/dataproc/docs/guides/dataproc-images)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently `n1-standard-4`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a minimum generation of CPU family
for the master. If not specified, GCP will default to a predetermined computed value
for each zone. See [the guide](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for details about which CPU families are available (and defaulted) for each zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigworkerconfigaccelerator">List[Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config<wbr>Accelerator]</a></span>
    </dt>
    <dd>{{% md %}}The Compute Engine accelerator configuration for these instances. Can be specified multiple times.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterconfigworkerconfigdiskconfig">Dict[Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config<wbr>Disk<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Disk Config
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URI for the image to use for this worker.  See [the guide](https://cloud.google.com/dataproc/docs/guides/dataproc-images)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>machine_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type
to create for the worker nodes. If not specified, GCP will default to a predetermined
computed value (currently `n1-standard-4`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of a minimum generation of CPU family
for the master. If not specified, GCP will default to a predetermined computed value
for each zone. See [the guide](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for details about which CPU families are available (and defaulted) for each zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config<wbr>Accelerator</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigWorkerConfigAccelerator">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigWorkerConfigAccelerator">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigWorkerConfigAcceleratorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigWorkerConfigAcceleratorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Accelerator<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of the accelerator cards of this type exposed to this instance. Often restricted to one of `1`, `2`, `4`, or `8`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The short name of the accelerator type to expose to this instance. For example, `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Accelerator<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of the accelerator cards of this type exposed to this instance. Often restricted to one of `1`, `2`, `4`, or `8`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The short name of the accelerator type to expose to this instance. For example, `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>accelerator<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of the accelerator cards of this type exposed to this instance. Often restricted to one of `1`, `2`, `4`, or `8`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>accelerator<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The short name of the accelerator type to expose to this instance. For example, `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>accelerator<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of the accelerator cards of this type exposed to this instance. Often restricted to one of `1`, `2`, `4`, or `8`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>accelerator_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The short name of the accelerator type to expose to this instance. For example, `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Config<wbr>Worker<wbr>Config<wbr>Disk<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterConfigWorkerConfigDiskConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterConfigWorkerConfigDiskConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigWorkerConfigDiskConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/dataproc?tab=doc#ClusterClusterConfigWorkerConfigDiskConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The disk type of the primary disk attached to each preemptible worker node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Local<wbr>Ssds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The disk type of the primary disk attached to each preemptible worker node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Local<wbr>Ssds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The disk type of the primary disk attached to each preemptible worker node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Local<wbr>Ssds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Size of the primary disk attached to each preemptible worker node, specified
in GB. The smallest allowed disk size is 10GB. GCP will default to a predetermined
computed value if not set (currently 500GB). Note: If SSDs are not
attached, it also contains the HDFS data blocks and Hadoop working directories.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The disk type of the primary disk attached to each preemptible worker node.
One of `"pd-ssd"` or `"pd-standard"`. Defaults to `"pd-standard"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Local<wbr>Ssds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each preemptible worker node. Defaults to 0.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

