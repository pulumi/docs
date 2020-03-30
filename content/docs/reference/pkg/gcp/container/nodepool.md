
---
title: "NodePool"
block_external_search_index: true
---

Manages a node pool in a Google Kubernetes Engine (GKE) cluster separately from
the cluster control plane. For more information see [the official documentation](https://cloud.google.com/container-engine/docs/node-pools)
and [the API reference](https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters.nodePools).

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_node_pool.html.markdown.



## Create a NodePool Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/container/#NodePool">NodePool</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/container/#NodePoolArgs">NodePoolArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">NodePool</span><span class="p">(resource_name, opts=None, </span>autoscaling=None<span class="p">, </span>cluster=None<span class="p">, </span>initial_node_count=None<span class="p">, </span>location=None<span class="p">, </span>management=None<span class="p">, </span>max_pods_per_node=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>node_config=None<span class="p">, </span>node_count=None<span class="p">, </span>node_locations=None<span class="p">, </span>project=None<span class="p">, </span>upgrade_settings=None<span class="p">, </span>version=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewNodePool<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolArgs">NodePoolArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePool">NodePool</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Container.NodePool.html">NodePool</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Container.Inputs.NodePoolArgs.html">NodePoolArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolautoscaling">Node<wbr>Pool<wbr>Autoscaling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The cluster to create the node pool for. Cluster must be present in `location` provided for zonal clusters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolmanagement">Node<wbr>Pool<wbr>Management<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are "route-based" - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the node pool. If left blank, the provider will
auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfig">Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The node configuration of the pool. See
gcp.container.Cluster for schema.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}
The list of zones in which the node pool's nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster's zone for zonal clusters. If unspecified, the cluster-level
`node_locations` will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolupgradesettings">Node<wbr>Pool<wbr>Upgrade<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of `max_surge` and `max_unavailable`.
The maximum number of nodes upgraded simultaneously is limited to 20.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolautoscaling">*Node<wbr>Pool<wbr>Autoscaling</a></span>
    </dt>
    <dd>{{% md %}}Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The cluster to create the node pool for. Cluster must be present in `location` provided for zonal clusters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolmanagement">*Node<wbr>Pool<wbr>Management</a></span>
    </dt>
    <dd>{{% md %}}Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are "route-based" - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the node pool. If left blank, the provider will
auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfig">*Node<wbr>Pool<wbr>Node<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The node configuration of the pool. See
gcp.container.Cluster for schema.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}
The list of zones in which the node pool's nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster's zone for zonal clusters. If unspecified, the cluster-level
`node_locations` will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolupgradesettings">*Node<wbr>Pool<wbr>Upgrade<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of `max_surge` and `max_unavailable`.
The maximum number of nodes upgraded simultaneously is limited to 20.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolautoscaling">Node<wbr>Pool<wbr>Autoscaling?</a></span>
    </dt>
    <dd>{{% md %}}Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The cluster to create the node pool for. Cluster must be present in `location` provided for zonal clusters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolmanagement">Node<wbr>Pool<wbr>Management?</a></span>
    </dt>
    <dd>{{% md %}}Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are "route-based" - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the node pool. If left blank, the provider will
auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfig">Node<wbr>Pool<wbr>Node<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The node configuration of the pool. See
gcp.container.Cluster for schema.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}
The list of zones in which the node pool's nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster's zone for zonal clusters. If unspecified, the cluster-level
`node_locations` will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolupgradesettings">Node<wbr>Pool<wbr>Upgrade<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of `max_surge` and `max_unavailable`.
The maximum number of nodes upgraded simultaneously is limited to 20.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolautoscaling">Dict[Node<wbr>Pool<wbr>Autoscaling]</a></span>
    </dt>
    <dd>{{% md %}}Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The cluster to create the node pool for. Cluster must be present in `location` provided for zonal clusters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial_<wbr>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolmanagement">Dict[Node<wbr>Pool<wbr>Management]</a></span>
    </dt>
    <dd>{{% md %}}Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>pods_<wbr>per_<wbr>node</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are "route-based" - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the node pool. If left blank, the provider will
auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfig">Dict[Node<wbr>Pool<wbr>Node<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The node configuration of the pool. See
gcp.container.Cluster for schema.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}
The list of zones in which the node pool's nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster's zone for zonal clusters. If unspecified, the cluster-level
`node_locations` will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolupgradesettings">Dict[Node<wbr>Pool<wbr>Upgrade<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of `max_surge` and `max_unavailable`.
The maximum number of nodes upgraded simultaneously is limited to 20.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## NodePool Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolautoscaling">Node<wbr>Pool<wbr>Autoscaling?</a></span>
    </dt>
    <dd>{{% md %}}Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The cluster to create the node pool for. Cluster must be present in `location` provided for zonal clusters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The resource URLs of the managed instance groups associated with this node pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolmanagement">Node<wbr>Pool<wbr>Management</a></span>
    </dt>
    <dd>{{% md %}}Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are "route-based" - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the node pool. If left blank, the provider will
auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfig">Node<wbr>Pool<wbr>Node<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The node configuration of the pool. See
gcp.container.Cluster for schema.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}
The list of zones in which the node pool's nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster's zone for zonal clusters. If unspecified, the cluster-level
`node_locations` will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Upgrade<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolupgradesettings">Node<wbr>Pool<wbr>Upgrade<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of `max_surge` and `max_unavailable`.
The maximum number of nodes upgraded simultaneously is limited to 20.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolautoscaling">*Node<wbr>Pool<wbr>Autoscaling</a></span>
    </dt>
    <dd>{{% md %}}Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The cluster to create the node pool for. Cluster must be present in `location` provided for zonal clusters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The resource URLs of the managed instance groups associated with this node pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolmanagement">Node<wbr>Pool<wbr>Management</a></span>
    </dt>
    <dd>{{% md %}}Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are "route-based" - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the node pool. If left blank, the provider will
auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfig">Node<wbr>Pool<wbr>Node<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The node configuration of the pool. See
gcp.container.Cluster for schema.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}
The list of zones in which the node pool's nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster's zone for zonal clusters. If unspecified, the cluster-level
`node_locations` will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Upgrade<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolupgradesettings">Node<wbr>Pool<wbr>Upgrade<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of `max_surge` and `max_unavailable`.
The maximum number of nodes upgraded simultaneously is limited to 20.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolautoscaling">Node<wbr>Pool<wbr>Autoscaling?</a></span>
    </dt>
    <dd>{{% md %}}Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The cluster to create the node pool for. Cluster must be present in `location` provided for zonal clusters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The resource URLs of the managed instance groups associated with this node pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolmanagement">Node<wbr>Pool<wbr>Management</a></span>
    </dt>
    <dd>{{% md %}}Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are "route-based" - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the node pool. If left blank, the provider will
auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfig">Node<wbr>Pool<wbr>Node<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The node configuration of the pool. See
gcp.container.Cluster for schema.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}
The list of zones in which the node pool's nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster's zone for zonal clusters. If unspecified, the cluster-level
`node_locations` will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>upgrade<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolupgradesettings">Node<wbr>Pool<wbr>Upgrade<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of `max_surge` and `max_unavailable`.
The maximum number of nodes upgraded simultaneously is limited to 20.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolautoscaling">Dict[Node<wbr>Pool<wbr>Autoscaling]</a></span>
    </dt>
    <dd>{{% md %}}Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The cluster to create the node pool for. Cluster must be present in `location` provided for zonal clusters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>initial_<wbr>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>group_<wbr>urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The resource URLs of the managed instance groups associated with this node pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolmanagement">Dict[Node<wbr>Pool<wbr>Management]</a></span>
    </dt>
    <dd>{{% md %}}Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max_<wbr>pods_<wbr>per_<wbr>node</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are "route-based" - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the node pool. If left blank, the provider will
auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfig">Dict[Node<wbr>Pool<wbr>Node<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The node configuration of the pool. See
gcp.container.Cluster for schema.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node_<wbr>locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}
The list of zones in which the node pool's nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster's zone for zonal clusters. If unspecified, the cluster-level
`node_locations` will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>upgrade_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolupgradesettings">Dict[Node<wbr>Pool<wbr>Upgrade<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of `max_surge` and `max_unavailable`.
The maximum number of nodes upgraded simultaneously is limited to 20.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing NodePool Resource

Get an existing NodePool resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/container/#NodePoolState">NodePoolState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/container/#NodePool">NodePool</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>autoscaling=None<span class="p">, </span>cluster=None<span class="p">, </span>initial_node_count=None<span class="p">, </span>instance_group_urls=None<span class="p">, </span>location=None<span class="p">, </span>management=None<span class="p">, </span>max_pods_per_node=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>node_config=None<span class="p">, </span>node_count=None<span class="p">, </span>node_locations=None<span class="p">, </span>project=None<span class="p">, </span>upgrade_settings=None<span class="p">, </span>version=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetNodePool<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolState">NodePoolState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePool">NodePool</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Container.NodePool.html">NodePool</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Container.NodePoolState.html">NodePoolState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolautoscaling">Node<wbr>Pool<wbr>Autoscaling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The cluster to create the node pool for. Cluster must be present in `location` provided for zonal clusters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The resource URLs of the managed instance groups associated with this node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolmanagement">Node<wbr>Pool<wbr>Management<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are "route-based" - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the node pool. If left blank, the provider will
auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfig">Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The node configuration of the pool. See
gcp.container.Cluster for schema.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}
The list of zones in which the node pool's nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster's zone for zonal clusters. If unspecified, the cluster-level
`node_locations` will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolupgradesettings">Node<wbr>Pool<wbr>Upgrade<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of `max_surge` and `max_unavailable`.
The maximum number of nodes upgraded simultaneously is limited to 20.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolautoscaling">*Node<wbr>Pool<wbr>Autoscaling</a></span>
    </dt>
    <dd>{{% md %}}Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The cluster to create the node pool for. Cluster must be present in `location` provided for zonal clusters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The resource URLs of the managed instance groups associated with this node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolmanagement">*Node<wbr>Pool<wbr>Management</a></span>
    </dt>
    <dd>{{% md %}}Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are "route-based" - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the node pool. If left blank, the provider will
auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfig">*Node<wbr>Pool<wbr>Node<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The node configuration of the pool. See
gcp.container.Cluster for schema.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}
The list of zones in which the node pool's nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster's zone for zonal clusters. If unspecified, the cluster-level
`node_locations` will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolupgradesettings">*Node<wbr>Pool<wbr>Upgrade<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of `max_surge` and `max_unavailable`.
The maximum number of nodes upgraded simultaneously is limited to 20.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolautoscaling">Node<wbr>Pool<wbr>Autoscaling?</a></span>
    </dt>
    <dd>{{% md %}}Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The cluster to create the node pool for. Cluster must be present in `location` provided for zonal clusters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The resource URLs of the managed instance groups associated with this node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolmanagement">Node<wbr>Pool<wbr>Management?</a></span>
    </dt>
    <dd>{{% md %}}Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are "route-based" - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the node pool. If left blank, the provider will
auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfig">Node<wbr>Pool<wbr>Node<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The node configuration of the pool. See
gcp.container.Cluster for schema.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}
The list of zones in which the node pool's nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster's zone for zonal clusters. If unspecified, the cluster-level
`node_locations` will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolupgradesettings">Node<wbr>Pool<wbr>Upgrade<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of `max_surge` and `max_unavailable`.
The maximum number of nodes upgraded simultaneously is limited to 20.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolautoscaling">Dict[Node<wbr>Pool<wbr>Autoscaling]</a></span>
    </dt>
    <dd>{{% md %}}Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The cluster to create the node pool for. Cluster must be present in `location` provided for zonal clusters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial_<wbr>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>group_<wbr>urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The resource URLs of the managed instance groups associated with this node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolmanagement">Dict[Node<wbr>Pool<wbr>Management]</a></span>
    </dt>
    <dd>{{% md %}}Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>pods_<wbr>per_<wbr>node</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are "route-based" - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the node pool. If left blank, the provider will
auto-generate a unique name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with `name`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfig">Dict[Node<wbr>Pool<wbr>Node<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The node configuration of the pool. See
gcp.container.Cluster for schema.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside `autoscaling`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}
The list of zones in which the node pool's nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster's zone for zonal clusters. If unspecified, the cluster-level
`node_locations` will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolupgradesettings">Dict[Node<wbr>Pool<wbr>Upgrade<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of `max_surge` and `max_unavailable`.
The maximum number of nodes upgraded simultaneously is limited to 20.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version for the nodes in this pool. Note that if this field
and `auto_upgrade` are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Node<wbr>Pool<wbr>Autoscaling</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#NodePoolAutoscaling">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#NodePoolAutoscaling">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolAutoscalingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolAutoscalingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Maximum number of nodes in the NodePool. Must be >= min_node_count.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Min<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Minimum number of nodes in the NodePool. Must be >=0 and
<= `max_node_count`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Maximum number of nodes in the NodePool. Must be >= min_node_count.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Min<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Minimum number of nodes in the NodePool. Must be >=0 and
<= `max_node_count`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Maximum number of nodes in the NodePool. Must be >= min_node_count.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>min<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Minimum number of nodes in the NodePool. Must be >=0 and
<= `max_node_count`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Maximum number of nodes in the NodePool. Must be >= min_node_count.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>min<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Minimum number of nodes in the NodePool. Must be >=0 and
<= `max_node_count`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Node<wbr>Pool<wbr>Management</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#NodePoolManagement">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#NodePoolManagement">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolManagementArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolManagementOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Repair</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether the nodes will be automatically repaired.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Upgrade</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether the nodes will be automatically upgraded.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Repair</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether the nodes will be automatically repaired.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Upgrade</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether the nodes will be automatically upgraded.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Repair</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether the nodes will be automatically repaired.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Upgrade</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether the nodes will be automatically upgraded.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Repair</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the nodes will be automatically repaired.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Upgrade</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the nodes will be automatically upgraded.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Node<wbr>Pool<wbr>Node<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#NodePoolNodeConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#NodePoolNodeConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolNodeConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolNodeConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Kms<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigguestaccelerator">List&lt;Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Ssd<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sandbox<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigsandboxconfig">Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigshieldedinstanceconfig">Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigtaint">List&lt;Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Taint<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Workload<wbr>Metadata<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigworkloadmetadataconfig">Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Kms<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigguestaccelerator">[]Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Ssd<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sandbox<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigsandboxconfig">*Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigshieldedinstanceconfig">*Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigtaint">[]Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Taint</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Workload<wbr>Metadata<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigworkloadmetadataconfig">*Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk<wbr>Kms<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigguestaccelerator">Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local<wbr>Ssd<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sandbox<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigsandboxconfig">Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigshieldedinstanceconfig">Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigtaint">Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Taint[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>workload<wbr>Metadata<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigworkloadmetadataconfig">Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>boot<wbr>Disk<wbr>Kms<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>size_<wbr>gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest_<wbr>accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigguestaccelerator">List[Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local<wbr>Ssd<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>machine_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sandbox<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigsandboxconfig">Dict[Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>account</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shielded_<wbr>instance_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigshieldedinstanceconfig">Dict[Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigtaint">List[Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Taint]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>workload<wbr>Metadata<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#nodepoolnodeconfigworkloadmetadataconfig">Dict[Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#NodePoolNodeConfigGuestAccelerator">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#NodePoolNodeConfigGuestAccelerator">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolNodeConfigGuestAcceleratorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolNodeConfigGuestAcceleratorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
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
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
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
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
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
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#NodePoolNodeConfigSandboxConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#NodePoolNodeConfigSandboxConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolNodeConfigSandboxConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolNodeConfigSandboxConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Sandbox<wbr>Type</span>
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
        <span>Sandbox<wbr>Type</span>
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
        <span>sandbox<wbr>Type</span>
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
        <span>sandbox<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#NodePoolNodeConfigShieldedInstanceConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#NodePoolNodeConfigShieldedInstanceConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolNodeConfigShieldedInstanceConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolNodeConfigShieldedInstanceConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Integrity<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Integrity<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Integrity<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Integrity<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Taint</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#NodePoolNodeConfigTaint">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#NodePoolNodeConfigTaint">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolNodeConfigTaintArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolNodeConfigTaintOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
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
        <span>Effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
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
        <span>effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
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
        <span>effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#NodePoolNodeConfigWorkloadMetadataConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#NodePoolNodeConfigWorkloadMetadataConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolNodeConfigWorkloadMetadataConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolNodeConfigWorkloadMetadataConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Node<wbr>Metadata</span>
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
        <span>Node<wbr>Metadata</span>
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
        <span>node<wbr>Metadata</span>
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
        <span>node<wbr>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Node<wbr>Pool<wbr>Upgrade<wbr>Settings</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#NodePoolUpgradeSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#NodePoolUpgradeSettings">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolUpgradeSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#NodePoolUpgradeSettingsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Surge</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of additional nodes that can be added to the node pool during
an upgrade. Increasing `max_surge` raises the number of nodes that can be upgraded simultaneously.
Can be set to 0 or greater.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Unavailable</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of nodes that can be simultaneously unavailable during
an upgrade. Increasing `max_unavailable` raises the number of nodes that can be upgraded in
parallel. Can be set to 0 or greater.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Surge</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of additional nodes that can be added to the node pool during
an upgrade. Increasing `max_surge` raises the number of nodes that can be upgraded simultaneously.
Can be set to 0 or greater.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Unavailable</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of nodes that can be simultaneously unavailable during
an upgrade. Increasing `max_unavailable` raises the number of nodes that can be upgraded in
parallel. Can be set to 0 or greater.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Surge</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of additional nodes that can be added to the node pool during
an upgrade. Increasing `max_surge` raises the number of nodes that can be upgraded simultaneously.
Can be set to 0 or greater.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Unavailable</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of nodes that can be simultaneously unavailable during
an upgrade. Increasing `max_unavailable` raises the number of nodes that can be upgraded in
parallel. Can be set to 0 or greater.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Surge</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of additional nodes that can be added to the node pool during
an upgrade. Increasing `max_surge` raises the number of nodes that can be upgraded simultaneously.
Can be set to 0 or greater.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Unavailable</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of nodes that can be simultaneously unavailable during
an upgrade. Increasing `max_unavailable` raises the number of nodes that can be upgraded in
parallel. Can be set to 0 or greater.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







