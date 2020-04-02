
---
title: "Cluster"
block_external_search_index: true
---

Manages a Google Kubernetes Engine (GKE) cluster. For more information see
[the official documentation](https://cloud.google.com/container-engine/docs/clusters)
and [the API reference](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters).

> **Note:** All arguments and attributes, including basic auth username and
passwords as well as certificate outputs will be stored in the raw state as
plaintext. [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_cluster.html.markdown.



## Create a Cluster Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/container/#Cluster">Cluster</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/container/#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Cluster</span><span class="p">(resource_name, opts=None, </span>addons_config=None<span class="p">, </span>authenticator_groups_config=None<span class="p">, </span>cluster_autoscaling=None<span class="p">, </span>cluster_ipv4_cidr=None<span class="p">, </span>database_encryption=None<span class="p">, </span>default_max_pods_per_node=None<span class="p">, </span>description=None<span class="p">, </span>enable_binary_authorization=None<span class="p">, </span>enable_intranode_visibility=None<span class="p">, </span>enable_kubernetes_alpha=None<span class="p">, </span>enable_legacy_abac=None<span class="p">, </span>enable_shielded_nodes=None<span class="p">, </span>enable_tpu=None<span class="p">, </span>initial_node_count=None<span class="p">, </span>ip_allocation_policy=None<span class="p">, </span>location=None<span class="p">, </span>logging_service=None<span class="p">, </span>maintenance_policy=None<span class="p">, </span>master_auth=None<span class="p">, </span>master_authorized_networks_config=None<span class="p">, </span>min_master_version=None<span class="p">, </span>monitoring_service=None<span class="p">, </span>name=None<span class="p">, </span>network=None<span class="p">, </span>network_policy=None<span class="p">, </span>node_config=None<span class="p">, </span>node_locations=None<span class="p">, </span>node_pools=None<span class="p">, </span>node_version=None<span class="p">, </span>pod_security_policy_config=None<span class="p">, </span>private_cluster_config=None<span class="p">, </span>project=None<span class="p">, </span>release_channel=None<span class="p">, </span>remove_default_node_pool=None<span class="p">, </span>resource_labels=None<span class="p">, </span>resource_usage_export_config=None<span class="p">, </span>subnetwork=None<span class="p">, </span>vertical_pod_autoscaling=None<span class="p">, </span>workload_identity_config=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Container.Cluster.html">Cluster</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Container.ClusterArgs.html">ClusterArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Addons<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfig">Cluster<wbr>Addons<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The configuration for addons supported by GKE.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticator<wbr>Groups<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterauthenticatorgroupsconfig">Cluster<wbr>Authenticator<wbr>Groups<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[Google Groups for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscaling">Cluster<wbr>Cluster<wbr>Autoscaling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster's workload. See the
[guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for more details. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. `10.96.0.0/14`). Leave blank to have one
automatically chosen or specify a `/14` block in `10.0.0.0/8`. This field will
only work for routes-based clusters, where `ip_allocation_policy` is not defined.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Database<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdatabaseencryption">Cluster<wbr>Database<wbr>Encryption<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The default maximum number of pods
per node in this cluster. This doesn't work on "routes-based" clusters, clusters
that don't have IP Aliasing enabled. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Binary<wbr>Authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Intranode<wbr>Visibility</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Kubernetes<wbr>Alpha</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Legacy<wbr>Abac</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Shielded<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable Shielded Nodes features on all nodes in this cluster.  Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Tpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](https://cloud.google.com/tpu/docs/kubernetes-engine-setup).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Allocation<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteripallocationpolicy">Cluster<wbr>Ip<wbr>Allocation<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables [IP aliasing](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases),
making the cluster VPC-native instead of routes-based. Structure is documented
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as `us-central1-a`), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as `us-west1`), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`(Legacy Stackdriver),
`logging.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Logging), and `none`. Defaults to `logging.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintenance<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicy">Cluster<wbr>Maintenance<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The maintenance policy to use for the cluster. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Auth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauth">Cluster<wbr>Master<wbr>Auth<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the `container.clusters.getCredentials` permission.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Authorized<wbr>Networks<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfig">Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the `gcp.container.getEngineVersions` data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions in a
provider-compatible way. If you intend to specify versions manually,
[the docs](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version)
describe the various acceptable formats for this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitoring<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`(Legacy Stackdriver), `monitoring.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Monitoring), and `none`.
Defaults to `monitoring.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternetworkpolicy">Cluster<wbr>Network<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfig">Cluster<wbr>Node<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepool">List&lt;Cluster<wbr>Node<wbr>Pool<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of node pools associated with this cluster.
See gcp.container.NodePool for schema.
**Warning:** node pools defined inside a cluster can't be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say "these are the _only_ node pools associated with this cluster", use the
gcp.container.NodePool resource instead of this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
To update nodes in other node pools, use the `version` attribute on the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pod<wbr>Security<wbr>Policy<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterpodsecuritypolicyconfig">Cluster<wbr>Pod<wbr>Security<wbr>Policy<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterprivateclusterconfig">Cluster<wbr>Private<wbr>Cluster<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for [private clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters),
clusters with private nodes. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Release<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreleasechannel">Cluster<wbr>Release<wbr>Channel<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[Release channel](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remove<wbr>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, deletes the default node
pool upon cluster creation. If you're using `gcp.container.NodePool`
resources with no default node pool, this should be set to `true`, alongside
setting `initial_node_count` to at least `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}The GCE resource labels (a map of key/value pairs) to be applied to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Usage<wbr>Export<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfig">Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[ResourceUsageExportConfig](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork in which the cluster's instances are launched.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vertical<wbr>Pod<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterverticalpodautoscaling">Cluster<wbr>Vertical<wbr>Pod<wbr>Autoscaling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Workload<wbr>Identity<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterworkloadidentityconfig">Cluster<wbr>Workload<wbr>Identity<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}
Workload Identity allows Kubernetes service accounts to act as a user-managed
[Google IAM Service Account](https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts).
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Addons<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfig">*Cluster<wbr>Addons<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The configuration for addons supported by GKE.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticator<wbr>Groups<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterauthenticatorgroupsconfig">*Cluster<wbr>Authenticator<wbr>Groups<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[Google Groups for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscaling">*Cluster<wbr>Cluster<wbr>Autoscaling</a></span>
    </dt>
    <dd>{{% md %}}
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster's workload. See the
[guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for more details. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. `10.96.0.0/14`). Leave blank to have one
automatically chosen or specify a `/14` block in `10.0.0.0/8`. This field will
only work for routes-based clusters, where `ip_allocation_policy` is not defined.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Database<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdatabaseencryption">*Cluster<wbr>Database<wbr>Encryption</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The default maximum number of pods
per node in this cluster. This doesn't work on "routes-based" clusters, clusters
that don't have IP Aliasing enabled. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Binary<wbr>Authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Intranode<wbr>Visibility</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Kubernetes<wbr>Alpha</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Legacy<wbr>Abac</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Shielded<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable Shielded Nodes features on all nodes in this cluster.  Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Tpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](https://cloud.google.com/tpu/docs/kubernetes-engine-setup).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Allocation<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteripallocationpolicy">*Cluster<wbr>Ip<wbr>Allocation<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables [IP aliasing](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases),
making the cluster VPC-native instead of routes-based. Structure is documented
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as `us-central1-a`), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as `us-west1`), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`(Legacy Stackdriver),
`logging.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Logging), and `none`. Defaults to `logging.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintenance<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicy">*Cluster<wbr>Maintenance<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}The maintenance policy to use for the cluster. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Auth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauth">*Cluster<wbr>Master<wbr>Auth</a></span>
    </dt>
    <dd>{{% md %}}The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the `container.clusters.getCredentials` permission.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Authorized<wbr>Networks<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfig">*Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the `gcp.container.getEngineVersions` data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions in a
provider-compatible way. If you intend to specify versions manually,
[the docs](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version)
describe the various acceptable formats for this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitoring<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`(Legacy Stackdriver), `monitoring.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Monitoring), and `none`.
Defaults to `monitoring.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternetworkpolicy">*Cluster<wbr>Network<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfig">*Cluster<wbr>Node<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepool">[]Cluster<wbr>Node<wbr>Pool</a></span>
    </dt>
    <dd>{{% md %}}List of node pools associated with this cluster.
See gcp.container.NodePool for schema.
**Warning:** node pools defined inside a cluster can't be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say "these are the _only_ node pools associated with this cluster", use the
gcp.container.NodePool resource instead of this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
To update nodes in other node pools, use the `version` attribute on the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pod<wbr>Security<wbr>Policy<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterpodsecuritypolicyconfig">*Cluster<wbr>Pod<wbr>Security<wbr>Policy<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterprivateclusterconfig">*Cluster<wbr>Private<wbr>Cluster<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for [private clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters),
clusters with private nodes. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Release<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreleasechannel">*Cluster<wbr>Release<wbr>Channel</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[Release channel](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remove<wbr>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, deletes the default node
pool upon cluster creation. If you're using `gcp.container.NodePool`
resources with no default node pool, this should be set to `true`, alongside
setting `initial_node_count` to at least `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The GCE resource labels (a map of key/value pairs) to be applied to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Usage<wbr>Export<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfig">*Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[ResourceUsageExportConfig](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork in which the cluster's instances are launched.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vertical<wbr>Pod<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterverticalpodautoscaling">*Cluster<wbr>Vertical<wbr>Pod<wbr>Autoscaling</a></span>
    </dt>
    <dd>{{% md %}}
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Workload<wbr>Identity<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterworkloadidentityconfig">*Cluster<wbr>Workload<wbr>Identity<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}
Workload Identity allows Kubernetes service accounts to act as a user-managed
[Google IAM Service Account](https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts).
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>addons<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfig">Cluster<wbr>Addons<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The configuration for addons supported by GKE.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticator<wbr>Groups<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterauthenticatorgroupsconfig">Cluster<wbr>Authenticator<wbr>Groups<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[Google Groups for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscaling">Cluster<wbr>Cluster<wbr>Autoscaling?</a></span>
    </dt>
    <dd>{{% md %}}
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster's workload. See the
[guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for more details. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. `10.96.0.0/14`). Leave blank to have one
automatically chosen or specify a `/14` block in `10.0.0.0/8`. This field will
only work for routes-based clusters, where `ip_allocation_policy` is not defined.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>database<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdatabaseencryption">Cluster<wbr>Database<wbr>Encryption?</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The default maximum number of pods
per node in this cluster. This doesn't work on "routes-based" clusters, clusters
that don't have IP Aliasing enabled. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Binary<wbr>Authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Intranode<wbr>Visibility</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Kubernetes<wbr>Alpha</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Legacy<wbr>Abac</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Shielded<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable Shielded Nodes features on all nodes in this cluster.  Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Tpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](https://cloud.google.com/tpu/docs/kubernetes-engine-setup).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Allocation<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteripallocationpolicy">Cluster<wbr>Ip<wbr>Allocation<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables [IP aliasing](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases),
making the cluster VPC-native instead of routes-based. Structure is documented
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as `us-central1-a`), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as `us-west1`), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`(Legacy Stackdriver),
`logging.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Logging), and `none`. Defaults to `logging.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintenance<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicy">Cluster<wbr>Maintenance<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}The maintenance policy to use for the cluster. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Auth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauth">Cluster<wbr>Master<wbr>Auth?</a></span>
    </dt>
    <dd>{{% md %}}The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the `container.clusters.getCredentials` permission.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Authorized<wbr>Networks<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfig">Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the `gcp.container.getEngineVersions` data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions in a
provider-compatible way. If you intend to specify versions manually,
[the docs](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version)
describe the various acceptable formats for this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitoring<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`(Legacy Stackdriver), `monitoring.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Monitoring), and `none`.
Defaults to `monitoring.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternetworkpolicy">Cluster<wbr>Network<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfig">Cluster<wbr>Node<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepool">Cluster<wbr>Node<wbr>Pool[]?</a></span>
    </dt>
    <dd>{{% md %}}List of node pools associated with this cluster.
See gcp.container.NodePool for schema.
**Warning:** node pools defined inside a cluster can't be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say "these are the _only_ node pools associated with this cluster", use the
gcp.container.NodePool resource instead of this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
To update nodes in other node pools, use the `version` attribute on the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pod<wbr>Security<wbr>Policy<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterpodsecuritypolicyconfig">Cluster<wbr>Pod<wbr>Security<wbr>Policy<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterprivateclusterconfig">Cluster<wbr>Private<wbr>Cluster<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for [private clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters),
clusters with private nodes. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>release<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreleasechannel">Cluster<wbr>Release<wbr>Channel?</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[Release channel](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remove<wbr>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, deletes the default node
pool upon cluster creation. If you're using `gcp.container.NodePool`
resources with no default node pool, this should be set to `true`, alongside
setting `initial_node_count` to at least `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}The GCE resource labels (a map of key/value pairs) to be applied to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Usage<wbr>Export<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfig">Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[ResourceUsageExportConfig](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork in which the cluster's instances are launched.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vertical<wbr>Pod<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterverticalpodautoscaling">Cluster<wbr>Vertical<wbr>Pod<wbr>Autoscaling?</a></span>
    </dt>
    <dd>{{% md %}}
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>workload<wbr>Identity<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterworkloadidentityconfig">Cluster<wbr>Workload<wbr>Identity<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}
Workload Identity allows Kubernetes service accounts to act as a user-managed
[Google IAM Service Account](https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts).
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>addons_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfig">Dict[Cluster<wbr>Addons<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The configuration for addons supported by GKE.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticator_<wbr>groups_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterauthenticatorgroupsconfig">Dict[Cluster<wbr>Authenticator<wbr>Groups<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[Google Groups for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscaling">Dict[Cluster<wbr>Cluster<wbr>Autoscaling]</a></span>
    </dt>
    <dd>{{% md %}}
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster's workload. See the
[guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for more details. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>ipv4_<wbr>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. `10.96.0.0/14`). Leave blank to have one
automatically chosen or specify a `/14` block in `10.0.0.0/8`. This field will
only work for routes-based clusters, where `ip_allocation_policy` is not defined.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>database_<wbr>encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdatabaseencryption">Dict[Cluster<wbr>Database<wbr>Encryption]</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>max_<wbr>pods_<wbr>per_<wbr>node</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The default maximum number of pods
per node in this cluster. This doesn't work on "routes-based" clusters, clusters
that don't have IP Aliasing enabled. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>binary_<wbr>authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>intranode_<wbr>visibility</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>kubernetes_<wbr>alpha</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>legacy_<wbr>abac</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>shielded_<wbr>nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable Shielded Nodes features on all nodes in this cluster.  Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>tpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](https://cloud.google.com/tpu/docs/kubernetes-engine-setup).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial_<wbr>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>allocation_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteripallocationpolicy">Dict[Cluster<wbr>Ip<wbr>Allocation<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables [IP aliasing](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases),
making the cluster VPC-native instead of routes-based. Structure is documented
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as `us-central1-a`), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as `us-west1`), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`(Legacy Stackdriver),
`logging.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Logging), and `none`. Defaults to `logging.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintenance_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicy">Dict[Cluster<wbr>Maintenance<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}The maintenance policy to use for the cluster. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master_<wbr>auth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauth">Dict[Cluster<wbr>Master<wbr>Auth]</a></span>
    </dt>
    <dd>{{% md %}}The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the `container.clusters.getCredentials` permission.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master_<wbr>authorized_<wbr>networks_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfig">Dict[Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>master_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the `gcp.container.getEngineVersions` data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions in a
provider-compatible way. If you intend to specify versions manually,
[the docs](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version)
describe the various acceptable formats for this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitoring_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`(Legacy Stackdriver), `monitoring.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Monitoring), and `none`.
Defaults to `monitoring.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternetworkpolicy">Dict[Cluster<wbr>Network<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfig">Dict[Cluster<wbr>Node<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepool">List[Cluster<wbr>Node<wbr>Pool]</a></span>
    </dt>
    <dd>{{% md %}}List of node pools associated with this cluster.
See gcp.container.NodePool for schema.
**Warning:** node pools defined inside a cluster can't be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say "these are the _only_ node pools associated with this cluster", use the
gcp.container.NodePool resource instead of this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
To update nodes in other node pools, use the `version` attribute on the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pod_<wbr>security_<wbr>policy_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterpodsecuritypolicyconfig">Dict[Cluster<wbr>Pod<wbr>Security<wbr>Policy<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private_<wbr>cluster_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterprivateclusterconfig">Dict[Cluster<wbr>Private<wbr>Cluster<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration for [private clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters),
clusters with private nodes. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>release_<wbr>channel</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreleasechannel">Dict[Cluster<wbr>Release<wbr>Channel]</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[Release channel](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remove_<wbr>default_<wbr>node_<wbr>pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, deletes the default node
pool upon cluster creation. If you're using `gcp.container.NodePool`
resources with no default node pool, this should be set to `true`, alongside
setting `initial_node_count` to at least `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The GCE resource labels (a map of key/value pairs) to be applied to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>usage_<wbr>export_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfig">Dict[Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[ResourceUsageExportConfig](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork in which the cluster's instances are launched.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vertical_<wbr>pod_<wbr>autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterverticalpodautoscaling">Dict[Cluster<wbr>Vertical<wbr>Pod<wbr>Autoscaling]</a></span>
    </dt>
    <dd>{{% md %}}
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>workload_<wbr>identity_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterworkloadidentityconfig">Dict[Cluster<wbr>Workload<wbr>Identity<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}
Workload Identity allows Kubernetes service accounts to act as a user-managed
[Google IAM Service Account](https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts).
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Cluster Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Addons<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfig">Cluster<wbr>Addons<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The configuration for addons supported by GKE.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Authenticator<wbr>Groups<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterauthenticatorgroupsconfig">Cluster<wbr>Authenticator<wbr>Groups<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[Google Groups for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscaling">Cluster<wbr>Cluster<wbr>Autoscaling</a></span>
    </dt>
    <dd>{{% md %}}
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster's workload. See the
[guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for more details. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. `10.96.0.0/14`). Leave blank to have one
automatically chosen or specify a `/14` block in `10.0.0.0/8`. This field will
only work for routes-based clusters, where `ip_allocation_policy` is not defined.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Database<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdatabaseencryption">Cluster<wbr>Database<wbr>Encryption</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The default maximum number of pods
per node in this cluster. This doesn't work on "routes-based" clusters, clusters
that don't have IP Aliasing enabled. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Binary<wbr>Authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Intranode<wbr>Visibility</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Kubernetes<wbr>Alpha</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Legacy<wbr>Abac</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Shielded<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable Shielded Nodes features on all nodes in this cluster.  Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Tpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](https://cloud.google.com/tpu/docs/kubernetes-engine-setup).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP address of this cluster's Kubernetes master.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}List of instance group URLs which have been assigned
to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ip<wbr>Allocation<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteripallocationpolicy">Cluster<wbr>Ip<wbr>Allocation<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables [IP aliasing](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases),
making the cluster VPC-native instead of routes-based. Structure is documented
below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fingerprint of the set of labels for this cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as `us-central1-a`), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as `us-west1`), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Logging<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`(Legacy Stackdriver),
`logging.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Logging), and `none`. Defaults to `logging.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Maintenance<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicy">Cluster<wbr>Maintenance<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}The maintenance policy to use for the cluster. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Master<wbr>Auth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauth">Cluster<wbr>Master<wbr>Auth</a></span>
    </dt>
    <dd>{{% md %}}The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the `container.clusters.getCredentials` permission.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Master<wbr>Authorized<wbr>Networks<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfig">Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current version of the master in the cluster. This may
be different than the `min_master_version` set in the config if the master
has been updated by GKE.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Min<wbr>Master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the `gcp.container.getEngineVersions` data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions in a
provider-compatible way. If you intend to specify versions manually,
[the docs](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version)
describe the various acceptable formats for this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Monitoring<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`(Legacy Stackdriver), `monitoring.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Monitoring), and `none`.
Defaults to `monitoring.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternetworkpolicy">Cluster<wbr>Network<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfig">Cluster<wbr>Node<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepool">List&lt;Cluster<wbr>Node<wbr>Pool&gt;</a></span>
    </dt>
    <dd>{{% md %}}List of node pools associated with this cluster.
See gcp.container.NodePool for schema.
**Warning:** node pools defined inside a cluster can't be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say "these are the _only_ node pools associated with this cluster", use the
gcp.container.NodePool resource instead of this property.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
To update nodes in other node pools, use the `version` attribute on the node pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pod<wbr>Security<wbr>Policy<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterpodsecuritypolicyconfig">Cluster<wbr>Pod<wbr>Security<wbr>Policy<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterprivateclusterconfig">Cluster<wbr>Private<wbr>Cluster<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for [private clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters),
clusters with private nodes. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Release<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreleasechannel">Cluster<wbr>Release<wbr>Channel</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[Release channel](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Remove<wbr>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, deletes the default node
pool upon cluster creation. If you're using `gcp.container.NodePool`
resources with no default node pool, this should be set to `true`, alongside
setting `initial_node_count` to at least `1`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}The GCE resource labels (a map of key/value pairs) to be applied to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Usage<wbr>Export<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfig">Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[ResourceUsageExportConfig](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Services<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes services in this
cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`). Service addresses are typically put in the last
`/16` from the container CIDR.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork in which the cluster's instances are launched.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tpu<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Optional) The IP address range of the Cloud TPUs in this cluster, in
[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vertical<wbr>Pod<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterverticalpodautoscaling">Cluster<wbr>Vertical<wbr>Pod<wbr>Autoscaling?</a></span>
    </dt>
    <dd>{{% md %}}
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Workload<wbr>Identity<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterworkloadidentityconfig">Cluster<wbr>Workload<wbr>Identity<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}
Workload Identity allows Kubernetes service accounts to act as a user-managed
[Google IAM Service Account](https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts).
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Addons<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfig">Cluster<wbr>Addons<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The configuration for addons supported by GKE.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Authenticator<wbr>Groups<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterauthenticatorgroupsconfig">Cluster<wbr>Authenticator<wbr>Groups<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[Google Groups for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscaling">Cluster<wbr>Cluster<wbr>Autoscaling</a></span>
    </dt>
    <dd>{{% md %}}
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster's workload. See the
[guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for more details. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Cluster<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. `10.96.0.0/14`). Leave blank to have one
automatically chosen or specify a `/14` block in `10.0.0.0/8`. This field will
only work for routes-based clusters, where `ip_allocation_policy` is not defined.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Database<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdatabaseencryption">Cluster<wbr>Database<wbr>Encryption</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The default maximum number of pods
per node in this cluster. This doesn't work on "routes-based" clusters, clusters
that don't have IP Aliasing enabled. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Binary<wbr>Authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Intranode<wbr>Visibility</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Kubernetes<wbr>Alpha</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Legacy<wbr>Abac</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Shielded<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable Shielded Nodes features on all nodes in this cluster.  Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Tpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](https://cloud.google.com/tpu/docs/kubernetes-engine-setup).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP address of this cluster's Kubernetes master.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of instance group URLs which have been assigned
to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ip<wbr>Allocation<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteripallocationpolicy">*Cluster<wbr>Ip<wbr>Allocation<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables [IP aliasing](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases),
making the cluster VPC-native instead of routes-based. Structure is documented
below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fingerprint of the set of labels for this cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as `us-central1-a`), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as `us-west1`), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Logging<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`(Legacy Stackdriver),
`logging.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Logging), and `none`. Defaults to `logging.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Maintenance<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicy">*Cluster<wbr>Maintenance<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}The maintenance policy to use for the cluster. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Master<wbr>Auth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauth">Cluster<wbr>Master<wbr>Auth</a></span>
    </dt>
    <dd>{{% md %}}The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the `container.clusters.getCredentials` permission.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Master<wbr>Authorized<wbr>Networks<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfig">*Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current version of the master in the cluster. This may
be different than the `min_master_version` set in the config if the master
has been updated by GKE.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Min<wbr>Master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the `gcp.container.getEngineVersions` data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions in a
provider-compatible way. If you intend to specify versions manually,
[the docs](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version)
describe the various acceptable formats for this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Monitoring<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`(Legacy Stackdriver), `monitoring.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Monitoring), and `none`.
Defaults to `monitoring.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternetworkpolicy">Cluster<wbr>Network<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfig">Cluster<wbr>Node<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepool">[]Cluster<wbr>Node<wbr>Pool</a></span>
    </dt>
    <dd>{{% md %}}List of node pools associated with this cluster.
See gcp.container.NodePool for schema.
**Warning:** node pools defined inside a cluster can't be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say "these are the _only_ node pools associated with this cluster", use the
gcp.container.NodePool resource instead of this property.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Node<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
To update nodes in other node pools, use the `version` attribute on the node pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pod<wbr>Security<wbr>Policy<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterpodsecuritypolicyconfig">*Cluster<wbr>Pod<wbr>Security<wbr>Policy<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterprivateclusterconfig">Cluster<wbr>Private<wbr>Cluster<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for [private clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters),
clusters with private nodes. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Release<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreleasechannel">Cluster<wbr>Release<wbr>Channel</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[Release channel](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Remove<wbr>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, deletes the default node
pool upon cluster creation. If you're using `gcp.container.NodePool`
resources with no default node pool, this should be set to `true`, alongside
setting `initial_node_count` to at least `1`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The GCE resource labels (a map of key/value pairs) to be applied to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Usage<wbr>Export<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfig">*Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[ResourceUsageExportConfig](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Services<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes services in this
cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`). Service addresses are typically put in the last
`/16` from the container CIDR.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork in which the cluster's instances are launched.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tpu<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Optional) The IP address range of the Cloud TPUs in this cluster, in
[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vertical<wbr>Pod<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterverticalpodautoscaling">*Cluster<wbr>Vertical<wbr>Pod<wbr>Autoscaling</a></span>
    </dt>
    <dd>{{% md %}}
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Workload<wbr>Identity<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterworkloadidentityconfig">*Cluster<wbr>Workload<wbr>Identity<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}
Workload Identity allows Kubernetes service accounts to act as a user-managed
[Google IAM Service Account](https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts).
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>addons<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfig">Cluster<wbr>Addons<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The configuration for addons supported by GKE.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>authenticator<wbr>Groups<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterauthenticatorgroupsconfig">Cluster<wbr>Authenticator<wbr>Groups<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[Google Groups for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscaling">Cluster<wbr>Cluster<wbr>Autoscaling</a></span>
    </dt>
    <dd>{{% md %}}
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster's workload. See the
[guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for more details. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. `10.96.0.0/14`). Leave blank to have one
automatically chosen or specify a `/14` block in `10.0.0.0/8`. This field will
only work for routes-based clusters, where `ip_allocation_policy` is not defined.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>database<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdatabaseencryption">Cluster<wbr>Database<wbr>Encryption</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The default maximum number of pods
per node in this cluster. This doesn't work on "routes-based" clusters, clusters
that don't have IP Aliasing enabled. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Binary<wbr>Authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Intranode<wbr>Visibility</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Kubernetes<wbr>Alpha</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Legacy<wbr>Abac</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Shielded<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable Shielded Nodes features on all nodes in this cluster.  Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Tpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](https://cloud.google.com/tpu/docs/kubernetes-engine-setup).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP address of this cluster's Kubernetes master.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of instance group URLs which have been assigned
to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ip<wbr>Allocation<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteripallocationpolicy">Cluster<wbr>Ip<wbr>Allocation<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables [IP aliasing](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases),
making the cluster VPC-native instead of routes-based. Structure is documented
below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fingerprint of the set of labels for this cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as `us-central1-a`), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as `us-west1`), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>logging<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`(Legacy Stackdriver),
`logging.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Logging), and `none`. Defaults to `logging.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>maintenance<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicy">Cluster<wbr>Maintenance<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}The maintenance policy to use for the cluster. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>master<wbr>Auth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauth">Cluster<wbr>Master<wbr>Auth</a></span>
    </dt>
    <dd>{{% md %}}The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the `container.clusters.getCredentials` permission.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>master<wbr>Authorized<wbr>Networks<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfig">Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The current version of the master in the cluster. This may
be different than the `min_master_version` set in the config if the master
has been updated by GKE.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>min<wbr>Master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the `gcp.container.getEngineVersions` data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions in a
provider-compatible way. If you intend to specify versions manually,
[the docs](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version)
describe the various acceptable formats for this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>monitoring<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`(Legacy Stackdriver), `monitoring.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Monitoring), and `none`.
Defaults to `monitoring.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternetworkpolicy">Cluster<wbr>Network<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfig">Cluster<wbr>Node<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepool">Cluster<wbr>Node<wbr>Pool[]</a></span>
    </dt>
    <dd>{{% md %}}List of node pools associated with this cluster.
See gcp.container.NodePool for schema.
**Warning:** node pools defined inside a cluster can't be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say "these are the _only_ node pools associated with this cluster", use the
gcp.container.NodePool resource instead of this property.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
To update nodes in other node pools, use the `version` attribute on the node pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pod<wbr>Security<wbr>Policy<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterpodsecuritypolicyconfig">Cluster<wbr>Pod<wbr>Security<wbr>Policy<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private<wbr>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterprivateclusterconfig">Cluster<wbr>Private<wbr>Cluster<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for [private clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters),
clusters with private nodes. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>release<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreleasechannel">Cluster<wbr>Release<wbr>Channel</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[Release channel](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>remove<wbr>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, deletes the default node
pool upon cluster creation. If you're using `gcp.container.NodePool`
resources with no default node pool, this should be set to `true`, alongside
setting `initial_node_count` to at least `1`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}The GCE resource labels (a map of key/value pairs) to be applied to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Usage<wbr>Export<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfig">Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[ResourceUsageExportConfig](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>services<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes services in this
cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`). Service addresses are typically put in the last
`/16` from the container CIDR.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork in which the cluster's instances are launched.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tpu<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Optional) The IP address range of the Cloud TPUs in this cluster, in
[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vertical<wbr>Pod<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterverticalpodautoscaling">Cluster<wbr>Vertical<wbr>Pod<wbr>Autoscaling?</a></span>
    </dt>
    <dd>{{% md %}}
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>workload<wbr>Identity<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterworkloadidentityconfig">Cluster<wbr>Workload<wbr>Identity<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}
Workload Identity allows Kubernetes service accounts to act as a user-managed
[Google IAM Service Account](https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts).
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>addons_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfig">Dict[Cluster<wbr>Addons<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The configuration for addons supported by GKE.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>authenticator_<wbr>groups_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterauthenticatorgroupsconfig">Dict[Cluster<wbr>Authenticator<wbr>Groups<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[Google Groups for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster_<wbr>autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscaling">Dict[Cluster<wbr>Cluster<wbr>Autoscaling]</a></span>
    </dt>
    <dd>{{% md %}}
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster's workload. See the
[guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for more details. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>cluster_<wbr>ipv4_<wbr>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. `10.96.0.0/14`). Leave blank to have one
automatically chosen or specify a `/14` block in `10.0.0.0/8`. This field will
only work for routes-based clusters, where `ip_allocation_policy` is not defined.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>database_<wbr>encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdatabaseencryption">Dict[Cluster<wbr>Database<wbr>Encryption]</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>max_<wbr>pods_<wbr>per_<wbr>node</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The default maximum number of pods
per node in this cluster. This doesn't work on "routes-based" clusters, clusters
that don't have IP Aliasing enabled. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>binary_<wbr>authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>intranode_<wbr>visibility</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>kubernetes_<wbr>alpha</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>legacy_<wbr>abac</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>shielded_<wbr>nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable Shielded Nodes features on all nodes in this cluster.  Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>tpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](https://cloud.google.com/tpu/docs/kubernetes-engine-setup).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP address of this cluster's Kubernetes master.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>initial_<wbr>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>group_<wbr>urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of instance group URLs which have been assigned
to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ip_<wbr>allocation_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteripallocationpolicy">Dict[Cluster<wbr>Ip<wbr>Allocation<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables [IP aliasing](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases),
making the cluster VPC-native instead of routes-based. Structure is documented
below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>label_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The fingerprint of the set of labels for this cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as `us-central1-a`), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as `us-west1`), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>logging_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`(Legacy Stackdriver),
`logging.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Logging), and `none`. Defaults to `logging.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>maintenance_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicy">Dict[Cluster<wbr>Maintenance<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}The maintenance policy to use for the cluster. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>master_<wbr>auth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauth">Dict[Cluster<wbr>Master<wbr>Auth]</a></span>
    </dt>
    <dd>{{% md %}}The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the `container.clusters.getCredentials` permission.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>master_<wbr>authorized_<wbr>networks_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfig">Dict[Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>master_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The current version of the master in the cluster. This may
be different than the `min_master_version` set in the config if the master
has been updated by GKE.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>min_<wbr>master_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the `gcp.container.getEngineVersions` data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions in a
provider-compatible way. If you intend to specify versions manually,
[the docs](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version)
describe the various acceptable formats for this field.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>monitoring_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`(Legacy Stackdriver), `monitoring.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Monitoring), and `none`.
Defaults to `monitoring.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternetworkpolicy">Dict[Cluster<wbr>Network<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfig">Dict[Cluster<wbr>Node<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node_<wbr>locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node_<wbr>pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepool">List[Cluster<wbr>Node<wbr>Pool]</a></span>
    </dt>
    <dd>{{% md %}}List of node pools associated with this cluster.
See gcp.container.NodePool for schema.
**Warning:** node pools defined inside a cluster can't be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say "these are the _only_ node pools associated with this cluster", use the
gcp.container.NodePool resource instead of this property.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>node_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
To update nodes in other node pools, use the `version` attribute on the node pool.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pod_<wbr>security_<wbr>policy_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterpodsecuritypolicyconfig">Dict[Cluster<wbr>Pod<wbr>Security<wbr>Policy<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private_<wbr>cluster_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterprivateclusterconfig">Dict[Cluster<wbr>Private<wbr>Cluster<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration for [private clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters),
clusters with private nodes. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>release_<wbr>channel</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreleasechannel">Dict[Cluster<wbr>Release<wbr>Channel]</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[Release channel](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>remove_<wbr>default_<wbr>node_<wbr>pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, deletes the default node
pool upon cluster creation. If you're using `gcp.container.NodePool`
resources with no default node pool, this should be set to `true`, alongside
setting `initial_node_count` to at least `1`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The GCE resource labels (a map of key/value pairs) to be applied to the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>usage_<wbr>export_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfig">Dict[Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[ResourceUsageExportConfig](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>services_<wbr>ipv4_<wbr>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes services in this
cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`). Service addresses are typically put in the last
`/16` from the container CIDR.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork in which the cluster's instances are launched.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tpu_<wbr>ipv4_<wbr>cidr_<wbr>block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(Optional) The IP address range of the Cloud TPUs in this cluster, in
[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vertical_<wbr>pod_<wbr>autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterverticalpodautoscaling">Dict[Cluster<wbr>Vertical<wbr>Pod<wbr>Autoscaling]</a></span>
    </dt>
    <dd>{{% md %}}
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>workload_<wbr>identity_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterworkloadidentityconfig">Dict[Cluster<wbr>Workload<wbr>Identity<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}
Workload Identity allows Kubernetes service accounts to act as a user-managed
[Google IAM Service Account](https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts).
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Cluster Resource

Get an existing Cluster resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/container/#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/container/#Cluster">Cluster</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>addons_config=None<span class="p">, </span>authenticator_groups_config=None<span class="p">, </span>cluster_autoscaling=None<span class="p">, </span>cluster_ipv4_cidr=None<span class="p">, </span>database_encryption=None<span class="p">, </span>default_max_pods_per_node=None<span class="p">, </span>description=None<span class="p">, </span>enable_binary_authorization=None<span class="p">, </span>enable_intranode_visibility=None<span class="p">, </span>enable_kubernetes_alpha=None<span class="p">, </span>enable_legacy_abac=None<span class="p">, </span>enable_shielded_nodes=None<span class="p">, </span>enable_tpu=None<span class="p">, </span>endpoint=None<span class="p">, </span>initial_node_count=None<span class="p">, </span>instance_group_urls=None<span class="p">, </span>ip_allocation_policy=None<span class="p">, </span>label_fingerprint=None<span class="p">, </span>location=None<span class="p">, </span>logging_service=None<span class="p">, </span>maintenance_policy=None<span class="p">, </span>master_auth=None<span class="p">, </span>master_authorized_networks_config=None<span class="p">, </span>master_version=None<span class="p">, </span>min_master_version=None<span class="p">, </span>monitoring_service=None<span class="p">, </span>name=None<span class="p">, </span>network=None<span class="p">, </span>network_policy=None<span class="p">, </span>node_config=None<span class="p">, </span>node_locations=None<span class="p">, </span>node_pools=None<span class="p">, </span>node_version=None<span class="p">, </span>operation=None<span class="p">, </span>pod_security_policy_config=None<span class="p">, </span>private_cluster_config=None<span class="p">, </span>project=None<span class="p">, </span>release_channel=None<span class="p">, </span>remove_default_node_pool=None<span class="p">, </span>resource_labels=None<span class="p">, </span>resource_usage_export_config=None<span class="p">, </span>services_ipv4_cidr=None<span class="p">, </span>subnetwork=None<span class="p">, </span>tpu_ipv4_cidr_block=None<span class="p">, </span>vertical_pod_autoscaling=None<span class="p">, </span>workload_identity_config=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Container.Cluster.html">Cluster</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Container.ClusterState.html">ClusterState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Addons<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfig">Cluster<wbr>Addons<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The configuration for addons supported by GKE.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticator<wbr>Groups<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterauthenticatorgroupsconfig">Cluster<wbr>Authenticator<wbr>Groups<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[Google Groups for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscaling">Cluster<wbr>Cluster<wbr>Autoscaling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster's workload. See the
[guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for more details. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. `10.96.0.0/14`). Leave blank to have one
automatically chosen or specify a `/14` block in `10.0.0.0/8`. This field will
only work for routes-based clusters, where `ip_allocation_policy` is not defined.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Database<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdatabaseencryption">Cluster<wbr>Database<wbr>Encryption<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The default maximum number of pods
per node in this cluster. This doesn't work on "routes-based" clusters, clusters
that don't have IP Aliasing enabled. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Binary<wbr>Authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Intranode<wbr>Visibility</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Kubernetes<wbr>Alpha</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Legacy<wbr>Abac</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Shielded<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable Shielded Nodes features on all nodes in this cluster.  Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Tpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](https://cloud.google.com/tpu/docs/kubernetes-engine-setup).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address of this cluster's Kubernetes master.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of instance group URLs which have been assigned
to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Allocation<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteripallocationpolicy">Cluster<wbr>Ip<wbr>Allocation<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables [IP aliasing](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases),
making the cluster VPC-native instead of routes-based. Structure is documented
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The fingerprint of the set of labels for this cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as `us-central1-a`), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as `us-west1`), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`(Legacy Stackdriver),
`logging.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Logging), and `none`. Defaults to `logging.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintenance<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicy">Cluster<wbr>Maintenance<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The maintenance policy to use for the cluster. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Auth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauth">Cluster<wbr>Master<wbr>Auth<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the `container.clusters.getCredentials` permission.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Authorized<wbr>Networks<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfig">Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The current version of the master in the cluster. This may
be different than the `min_master_version` set in the config if the master
has been updated by GKE.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the `gcp.container.getEngineVersions` data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions in a
provider-compatible way. If you intend to specify versions manually,
[the docs](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version)
describe the various acceptable formats for this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitoring<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`(Legacy Stackdriver), `monitoring.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Monitoring), and `none`.
Defaults to `monitoring.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternetworkpolicy">Cluster<wbr>Network<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfig">Cluster<wbr>Node<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepool">List&lt;Cluster<wbr>Node<wbr>Pool<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of node pools associated with this cluster.
See gcp.container.NodePool for schema.
**Warning:** node pools defined inside a cluster can't be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say "these are the _only_ node pools associated with this cluster", use the
gcp.container.NodePool resource instead of this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
To update nodes in other node pools, use the `version` attribute on the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pod<wbr>Security<wbr>Policy<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterpodsecuritypolicyconfig">Cluster<wbr>Pod<wbr>Security<wbr>Policy<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterprivateclusterconfig">Cluster<wbr>Private<wbr>Cluster<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for [private clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters),
clusters with private nodes. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Release<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreleasechannel">Cluster<wbr>Release<wbr>Channel<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[Release channel](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remove<wbr>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `true`, deletes the default node
pool upon cluster creation. If you're using `gcp.container.NodePool`
resources with no default node pool, this should be set to `true`, alongside
setting `initial_node_count` to at least `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}The GCE resource labels (a map of key/value pairs) to be applied to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Usage<wbr>Export<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfig">Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[ResourceUsageExportConfig](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Services<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes services in this
cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`). Service addresses are typically put in the last
`/16` from the container CIDR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork in which the cluster's instances are launched.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tpu<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(Optional) The IP address range of the Cloud TPUs in this cluster, in
[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vertical<wbr>Pod<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterverticalpodautoscaling">Cluster<wbr>Vertical<wbr>Pod<wbr>Autoscaling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Workload<wbr>Identity<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterworkloadidentityconfig">Cluster<wbr>Workload<wbr>Identity<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}
Workload Identity allows Kubernetes service accounts to act as a user-managed
[Google IAM Service Account](https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts).
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Addons<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfig">*Cluster<wbr>Addons<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The configuration for addons supported by GKE.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authenticator<wbr>Groups<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterauthenticatorgroupsconfig">*Cluster<wbr>Authenticator<wbr>Groups<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[Google Groups for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscaling">*Cluster<wbr>Cluster<wbr>Autoscaling</a></span>
    </dt>
    <dd>{{% md %}}
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster's workload. See the
[guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for more details. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. `10.96.0.0/14`). Leave blank to have one
automatically chosen or specify a `/14` block in `10.0.0.0/8`. This field will
only work for routes-based clusters, where `ip_allocation_policy` is not defined.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Database<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdatabaseencryption">*Cluster<wbr>Database<wbr>Encryption</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The default maximum number of pods
per node in this cluster. This doesn't work on "routes-based" clusters, clusters
that don't have IP Aliasing enabled. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Binary<wbr>Authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Intranode<wbr>Visibility</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Kubernetes<wbr>Alpha</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Legacy<wbr>Abac</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Shielded<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable Shielded Nodes features on all nodes in this cluster.  Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Tpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](https://cloud.google.com/tpu/docs/kubernetes-engine-setup).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IP address of this cluster's Kubernetes master.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of instance group URLs which have been assigned
to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Allocation<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteripallocationpolicy">*Cluster<wbr>Ip<wbr>Allocation<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables [IP aliasing](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases),
making the cluster VPC-native instead of routes-based. Structure is documented
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The fingerprint of the set of labels for this cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as `us-central1-a`), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as `us-west1`), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logging<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`(Legacy Stackdriver),
`logging.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Logging), and `none`. Defaults to `logging.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintenance<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicy">*Cluster<wbr>Maintenance<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}The maintenance policy to use for the cluster. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Auth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauth">*Cluster<wbr>Master<wbr>Auth</a></span>
    </dt>
    <dd>{{% md %}}The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the `container.clusters.getCredentials` permission.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Authorized<wbr>Networks<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfig">*Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The current version of the master in the cluster. This may
be different than the `min_master_version` set in the config if the master
has been updated by GKE.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the `gcp.container.getEngineVersions` data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions in a
provider-compatible way. If you intend to specify versions manually,
[the docs](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version)
describe the various acceptable formats for this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitoring<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`(Legacy Stackdriver), `monitoring.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Monitoring), and `none`.
Defaults to `monitoring.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternetworkpolicy">*Cluster<wbr>Network<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfig">*Cluster<wbr>Node<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepool">[]Cluster<wbr>Node<wbr>Pool</a></span>
    </dt>
    <dd>{{% md %}}List of node pools associated with this cluster.
See gcp.container.NodePool for schema.
**Warning:** node pools defined inside a cluster can't be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say "these are the _only_ node pools associated with this cluster", use the
gcp.container.NodePool resource instead of this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
To update nodes in other node pools, use the `version` attribute on the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pod<wbr>Security<wbr>Policy<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterpodsecuritypolicyconfig">*Cluster<wbr>Pod<wbr>Security<wbr>Policy<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterprivateclusterconfig">*Cluster<wbr>Private<wbr>Cluster<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for [private clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters),
clusters with private nodes. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Release<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreleasechannel">*Cluster<wbr>Release<wbr>Channel</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[Release channel](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remove<wbr>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `true`, deletes the default node
pool upon cluster creation. If you're using `gcp.container.NodePool`
resources with no default node pool, this should be set to `true`, alongside
setting `initial_node_count` to at least `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The GCE resource labels (a map of key/value pairs) to be applied to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Usage<wbr>Export<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfig">*Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[ResourceUsageExportConfig](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Services<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes services in this
cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`). Service addresses are typically put in the last
`/16` from the container CIDR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork in which the cluster's instances are launched.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tpu<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}(Optional) The IP address range of the Cloud TPUs in this cluster, in
[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vertical<wbr>Pod<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterverticalpodautoscaling">*Cluster<wbr>Vertical<wbr>Pod<wbr>Autoscaling</a></span>
    </dt>
    <dd>{{% md %}}
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Workload<wbr>Identity<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterworkloadidentityconfig">*Cluster<wbr>Workload<wbr>Identity<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}
Workload Identity allows Kubernetes service accounts to act as a user-managed
[Google IAM Service Account](https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts).
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>addons<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfig">Cluster<wbr>Addons<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The configuration for addons supported by GKE.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticator<wbr>Groups<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterauthenticatorgroupsconfig">Cluster<wbr>Authenticator<wbr>Groups<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[Google Groups for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscaling">Cluster<wbr>Cluster<wbr>Autoscaling?</a></span>
    </dt>
    <dd>{{% md %}}
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster's workload. See the
[guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for more details. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. `10.96.0.0/14`). Leave blank to have one
automatically chosen or specify a `/14` block in `10.0.0.0/8`. This field will
only work for routes-based clusters, where `ip_allocation_policy` is not defined.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>database<wbr>Encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdatabaseencryption">Cluster<wbr>Database<wbr>Encryption?</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The default maximum number of pods
per node in this cluster. This doesn't work on "routes-based" clusters, clusters
that don't have IP Aliasing enabled. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Binary<wbr>Authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Intranode<wbr>Visibility</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Kubernetes<wbr>Alpha</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Legacy<wbr>Abac</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Shielded<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable Shielded Nodes features on all nodes in this cluster.  Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Tpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](https://cloud.google.com/tpu/docs/kubernetes-engine-setup).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address of this cluster's Kubernetes master.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of instance group URLs which have been assigned
to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Allocation<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteripallocationpolicy">Cluster<wbr>Ip<wbr>Allocation<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables [IP aliasing](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases),
making the cluster VPC-native instead of routes-based. Structure is documented
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label<wbr>Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The fingerprint of the set of labels for this cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as `us-central1-a`), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as `us-west1`), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`(Legacy Stackdriver),
`logging.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Logging), and `none`. Defaults to `logging.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintenance<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicy">Cluster<wbr>Maintenance<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}The maintenance policy to use for the cluster. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Auth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauth">Cluster<wbr>Master<wbr>Auth?</a></span>
    </dt>
    <dd>{{% md %}}The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the `container.clusters.getCredentials` permission.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Authorized<wbr>Networks<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfig">Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The current version of the master in the cluster. This may
be different than the `min_master_version` set in the config if the master
has been updated by GKE.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Master<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the `gcp.container.getEngineVersions` data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions in a
provider-compatible way. If you intend to specify versions manually,
[the docs](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version)
describe the various acceptable formats for this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitoring<wbr>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`(Legacy Stackdriver), `monitoring.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Monitoring), and `none`.
Defaults to `monitoring.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternetworkpolicy">Cluster<wbr>Network<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfig">Cluster<wbr>Node<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepool">Cluster<wbr>Node<wbr>Pool[]?</a></span>
    </dt>
    <dd>{{% md %}}List of node pools associated with this cluster.
See gcp.container.NodePool for schema.
**Warning:** node pools defined inside a cluster can't be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say "these are the _only_ node pools associated with this cluster", use the
gcp.container.NodePool resource instead of this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
To update nodes in other node pools, use the `version` attribute on the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pod<wbr>Security<wbr>Policy<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterpodsecuritypolicyconfig">Cluster<wbr>Pod<wbr>Security<wbr>Policy<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Cluster<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterprivateclusterconfig">Cluster<wbr>Private<wbr>Cluster<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for [private clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters),
clusters with private nodes. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>release<wbr>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreleasechannel">Cluster<wbr>Release<wbr>Channel?</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[Release channel](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remove<wbr>Default<wbr>Node<wbr>Pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `true`, deletes the default node
pool upon cluster creation. If you're using `gcp.container.NodePool`
resources with no default node pool, this should be set to `true`, alongside
setting `initial_node_count` to at least `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}The GCE resource labels (a map of key/value pairs) to be applied to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Usage<wbr>Export<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfig">Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[ResourceUsageExportConfig](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>services<wbr>Ipv4Cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes services in this
cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`). Service addresses are typically put in the last
`/16` from the container CIDR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork in which the cluster's instances are launched.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tpu<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(Optional) The IP address range of the Cloud TPUs in this cluster, in
[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vertical<wbr>Pod<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterverticalpodautoscaling">Cluster<wbr>Vertical<wbr>Pod<wbr>Autoscaling?</a></span>
    </dt>
    <dd>{{% md %}}
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>workload<wbr>Identity<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterworkloadidentityconfig">Cluster<wbr>Workload<wbr>Identity<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}
Workload Identity allows Kubernetes service accounts to act as a user-managed
[Google IAM Service Account](https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts).
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>addons_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfig">Dict[Cluster<wbr>Addons<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The configuration for addons supported by GKE.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authenticator_<wbr>groups_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterauthenticatorgroupsconfig">Dict[Cluster<wbr>Authenticator<wbr>Groups<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[Google Groups for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscaling">Dict[Cluster<wbr>Cluster<wbr>Autoscaling]</a></span>
    </dt>
    <dd>{{% md %}}
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster's workload. See the
[guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for more details. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster_<wbr>ipv4_<wbr>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. `10.96.0.0/14`). Leave blank to have one
automatically chosen or specify a `/14` block in `10.0.0.0/8`. This field will
only work for routes-based clusters, where `ip_allocation_policy` is not defined.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>database_<wbr>encryption</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterdatabaseencryption">Dict[Cluster<wbr>Database<wbr>Encryption]</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>max_<wbr>pods_<wbr>per_<wbr>node</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The default maximum number of pods
per node in this cluster. This doesn't work on "routes-based" clusters, clusters
that don't have IP Aliasing enabled. See the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>binary_<wbr>authorization</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>intranode_<wbr>visibility</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>kubernetes_<wbr>alpha</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>legacy_<wbr>abac</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to `false`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>shielded_<wbr>nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable Shielded Nodes features on all nodes in this cluster.  Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>tpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](https://cloud.google.com/tpu/docs/kubernetes-engine-setup).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP address of this cluster's Kubernetes master.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial_<wbr>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>group_<wbr>urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of instance group URLs which have been assigned
to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>allocation_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteripallocationpolicy">Dict[Cluster<wbr>Ip<wbr>Allocation<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables [IP aliasing](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases),
making the cluster VPC-native instead of routes-based. Structure is documented
below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The fingerprint of the set of labels for this cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as `us-central1-a`), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as `us-west1`), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logging_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The logging service that the cluster should
write logs to. Available options include `logging.googleapis.com`(Legacy Stackdriver),
`logging.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Logging), and `none`. Defaults to `logging.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintenance_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicy">Dict[Cluster<wbr>Maintenance<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}The maintenance policy to use for the cluster. Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master_<wbr>auth</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauth">Dict[Cluster<wbr>Master<wbr>Auth]</a></span>
    </dt>
    <dd>{{% md %}}The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the `container.clusters.getCredentials` permission.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master_<wbr>authorized_<wbr>networks_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfig">Dict[Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The desired configuration options
for master authorized networks. Omit the nested `cidr_blocks` attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The current version of the master in the cluster. This may
be different than the `min_master_version` set in the config if the master
has been updated by GKE.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>master_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version--use the read-only `master_version` field to obtain that.
If unset, the cluster's version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the `gcp.container.getEngineVersions` data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions in a
provider-compatible way. If you intend to specify versions manually,
[the docs](https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version)
describe the various acceptable formats for this field.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitoring_<wbr>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
`monitoring.googleapis.com`(Legacy Stackdriver), `monitoring.googleapis.com/kubernetes`(Stackdriver Kubernetes Engine Monitoring), and `none`.
Defaults to `monitoring.googleapis.com/kubernetes`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternetworkpolicy">Dict[Cluster<wbr>Network<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
feature. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfig">Dict[Cluster<wbr>Node<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>pools</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepool">List[Cluster<wbr>Node<wbr>Pool]</a></span>
    </dt>
    <dd>{{% md %}}List of node pools associated with this cluster.
See gcp.container.NodePool for schema.
**Warning:** node pools defined inside a cluster can't be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say "these are the _only_ node pools associated with this cluster", use the
gcp.container.NodePool resource instead of this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Kubernetes version on the nodes. Must either be unset
or set to the same value as `min_master_version` on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it's
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the `gcp.container.getEngineVersions` data source's
`version_prefix` field to approximate fuzzy versions in a provider-compatible way.
To update nodes in other node pools, use the `version` attribute on the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pod_<wbr>security_<wbr>policy_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterpodsecuritypolicyconfig">Dict[Cluster<wbr>Pod<wbr>Security<wbr>Policy<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private_<wbr>cluster_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterprivateclusterconfig">Dict[Cluster<wbr>Private<wbr>Cluster<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration for [private clusters](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters),
clusters with private nodes. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>release_<wbr>channel</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterreleasechannel">Dict[Cluster<wbr>Release<wbr>Channel]</a></span>
    </dt>
    <dd>{{% md %}}Configuration options for the
[Release channel](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remove_<wbr>default_<wbr>node_<wbr>pool</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, deletes the default node
pool upon cluster creation. If you're using `gcp.container.NodePool`
resources with no default node pool, this should be set to `true`, alongside
setting `initial_node_count` to at least `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The GCE resource labels (a map of key/value pairs) to be applied to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>usage_<wbr>export_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfig">Dict[Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Configuration for the
[ResourceUsageExportConfig](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) feature.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>services_<wbr>ipv4_<wbr>cidr</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP address range of the Kubernetes services in this
cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`). Service addresses are typically put in the last
`/16` from the container CIDR.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnetwork</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name or self_link of the Google Compute Engine
subnetwork in which the cluster's instances are launched.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tpu_<wbr>ipv4_<wbr>cidr_<wbr>block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(Optional) The IP address range of the Cloud TPUs in this cluster, in
[CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
notation (e.g. `1.2.3.4/29`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vertical_<wbr>pod_<wbr>autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterverticalpodautoscaling">Dict[Cluster<wbr>Vertical<wbr>Pod<wbr>Autoscaling]</a></span>
    </dt>
    <dd>{{% md %}}
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>workload_<wbr>identity_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterworkloadidentityconfig">Dict[Cluster<wbr>Workload<wbr>Identity<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}
Workload Identity allows Kubernetes service accounts to act as a user-managed
[Google IAM Service Account](https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts).
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Cluster<wbr>Addons<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterAddonsConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterAddonsConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAddonsConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAddonsConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cloudrun<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfigcloudrunconfig">Cluster<wbr>Addons<wbr>Config<wbr>Cloudrun<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}.
The status of the CloudRun addon. It requires `istio_config` enabled. It is disabled by default.
Set `disabled = false` to enable. This addon can only be enabled at cluster creation time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Cache<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfigdnscacheconfig">Cluster<wbr>Addons<wbr>Config<wbr>Dns<wbr>Cache<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}.
The status of the NodeLocal DNSCache addon. It is disabled by default.
Set `enabled = true` to enable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Horizontal<wbr>Pod<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfighorizontalpodautoscaling">Cluster<wbr>Addons<wbr>Config<wbr>Horizontal<wbr>Pod<wbr>Autoscaling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The status of the Horizontal Pod Autoscaling
addon, which increases or decreases the number of replica pods a replication controller
has based on the resource usage of the existing pods.
It ensures that a Heapster pod is running in the cluster, which is also used by the Cloud Monitoring service.
It is enabled by default;
set `disabled = true` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Load<wbr>Balancing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfighttploadbalancing">Cluster<wbr>Addons<wbr>Config<wbr>Http<wbr>Load<wbr>Balancing<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The status of the HTTP (L7) load balancing
controller addon, which makes it easy to set up HTTP load balancers for services in a
cluster. It is enabled by default; set `disabled = true` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Istio<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfigistioconfig">Cluster<wbr>Addons<wbr>Config<wbr>Istio<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Policy<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfignetworkpolicyconfig">Cluster<wbr>Addons<wbr>Config<wbr>Network<wbr>Policy<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Whether we should enable the network policy addon
for the master.  This must be enabled in order to enable network policy for the nodes.
To enable this, you must also define a `network_policy` block,
otherwise nothing will happen.
It can only be disabled if the nodes already do not have network policies enabled.
Defaults to disabled; set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cloudrun<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfigcloudrunconfig">*Cluster<wbr>Addons<wbr>Config<wbr>Cloudrun<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}.
The status of the CloudRun addon. It requires `istio_config` enabled. It is disabled by default.
Set `disabled = false` to enable. This addon can only be enabled at cluster creation time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Cache<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfigdnscacheconfig">*Cluster<wbr>Addons<wbr>Config<wbr>Dns<wbr>Cache<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}.
The status of the NodeLocal DNSCache addon. It is disabled by default.
Set `enabled = true` to enable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Horizontal<wbr>Pod<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfighorizontalpodautoscaling">*Cluster<wbr>Addons<wbr>Config<wbr>Horizontal<wbr>Pod<wbr>Autoscaling</a></span>
    </dt>
    <dd>{{% md %}}The status of the Horizontal Pod Autoscaling
addon, which increases or decreases the number of replica pods a replication controller
has based on the resource usage of the existing pods.
It ensures that a Heapster pod is running in the cluster, which is also used by the Cloud Monitoring service.
It is enabled by default;
set `disabled = true` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Load<wbr>Balancing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfighttploadbalancing">*Cluster<wbr>Addons<wbr>Config<wbr>Http<wbr>Load<wbr>Balancing</a></span>
    </dt>
    <dd>{{% md %}}The status of the HTTP (L7) load balancing
controller addon, which makes it easy to set up HTTP load balancers for services in a
cluster. It is enabled by default; set `disabled = true` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Istio<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfigistioconfig">*Cluster<wbr>Addons<wbr>Config<wbr>Istio<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Policy<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfignetworkpolicyconfig">*Cluster<wbr>Addons<wbr>Config<wbr>Network<wbr>Policy<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Whether we should enable the network policy addon
for the master.  This must be enabled in order to enable network policy for the nodes.
To enable this, you must also define a `network_policy` block,
otherwise nothing will happen.
It can only be disabled if the nodes already do not have network policies enabled.
Defaults to disabled; set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cloudrun<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfigcloudrunconfig">Cluster<wbr>Addons<wbr>Config<wbr>Cloudrun<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}.
The status of the CloudRun addon. It requires `istio_config` enabled. It is disabled by default.
Set `disabled = false` to enable. This addon can only be enabled at cluster creation time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Cache<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfigdnscacheconfig">Cluster<wbr>Addons<wbr>Config<wbr>Dns<wbr>Cache<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}.
The status of the NodeLocal DNSCache addon. It is disabled by default.
Set `enabled = true` to enable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>horizontal<wbr>Pod<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfighorizontalpodautoscaling">Cluster<wbr>Addons<wbr>Config<wbr>Horizontal<wbr>Pod<wbr>Autoscaling?</a></span>
    </dt>
    <dd>{{% md %}}The status of the Horizontal Pod Autoscaling
addon, which increases or decreases the number of replica pods a replication controller
has based on the resource usage of the existing pods.
It ensures that a Heapster pod is running in the cluster, which is also used by the Cloud Monitoring service.
It is enabled by default;
set `disabled = true` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Load<wbr>Balancing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfighttploadbalancing">Cluster<wbr>Addons<wbr>Config<wbr>Http<wbr>Load<wbr>Balancing?</a></span>
    </dt>
    <dd>{{% md %}}The status of the HTTP (L7) load balancing
controller addon, which makes it easy to set up HTTP load balancers for services in a
cluster. It is enabled by default; set `disabled = true` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>istio<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfigistioconfig">Cluster<wbr>Addons<wbr>Config<wbr>Istio<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Policy<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfignetworkpolicyconfig">Cluster<wbr>Addons<wbr>Config<wbr>Network<wbr>Policy<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Whether we should enable the network policy addon
for the master.  This must be enabled in order to enable network policy for the nodes.
To enable this, you must also define a `network_policy` block,
otherwise nothing will happen.
It can only be disabled if the nodes already do not have network policies enabled.
Defaults to disabled; set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cloudrun<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfigcloudrunconfig">Dict[Cluster<wbr>Addons<wbr>Config<wbr>Cloudrun<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}.
The status of the CloudRun addon. It requires `istio_config` enabled. It is disabled by default.
Set `disabled = false` to enable. This addon can only be enabled at cluster creation time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Cache<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfigdnscacheconfig">Dict[Cluster<wbr>Addons<wbr>Config<wbr>Dns<wbr>Cache<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}.
The status of the NodeLocal DNSCache addon. It is disabled by default.
Set `enabled = true` to enable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>horizontal<wbr>Pod<wbr>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfighorizontalpodautoscaling">Dict[Cluster<wbr>Addons<wbr>Config<wbr>Horizontal<wbr>Pod<wbr>Autoscaling]</a></span>
    </dt>
    <dd>{{% md %}}The status of the Horizontal Pod Autoscaling
addon, which increases or decreases the number of replica pods a replication controller
has based on the resource usage of the existing pods.
It ensures that a Heapster pod is running in the cluster, which is also used by the Cloud Monitoring service.
It is enabled by default;
set `disabled = true` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Load<wbr>Balancing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfighttploadbalancing">Dict[Cluster<wbr>Addons<wbr>Config<wbr>Http<wbr>Load<wbr>Balancing]</a></span>
    </dt>
    <dd>{{% md %}}The status of the HTTP (L7) load balancing
controller addon, which makes it easy to set up HTTP load balancers for services in a
cluster. It is enabled by default; set `disabled = true` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>istio<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfigistioconfig">Dict[Cluster<wbr>Addons<wbr>Config<wbr>Istio<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Policy<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusteraddonsconfignetworkpolicyconfig">Dict[Cluster<wbr>Addons<wbr>Config<wbr>Network<wbr>Policy<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Whether we should enable the network policy addon
for the master.  This must be enabled in order to enable network policy for the nodes.
To enable this, you must also define a `network_policy` block,
otherwise nothing will happen.
It can only be disabled if the nodes already do not have network policies enabled.
Defaults to disabled; set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Addons<wbr>Config<wbr>Cloudrun<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterAddonsConfigCloudrunConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterAddonsConfigCloudrunConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAddonsConfigCloudrunConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAddonsConfigCloudrunConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Addons<wbr>Config<wbr>Dns<wbr>Cache<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterAddonsConfigDnsCacheConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterAddonsConfigDnsCacheConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAddonsConfigDnsCacheConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAddonsConfigDnsCacheConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
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
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
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
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
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
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Addons<wbr>Config<wbr>Horizontal<wbr>Pod<wbr>Autoscaling</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterAddonsConfigHorizontalPodAutoscaling">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterAddonsConfigHorizontalPodAutoscaling">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAddonsConfigHorizontalPodAutoscalingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAddonsConfigHorizontalPodAutoscalingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Addons<wbr>Config<wbr>Http<wbr>Load<wbr>Balancing</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterAddonsConfigHttpLoadBalancing">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterAddonsConfigHttpLoadBalancing">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAddonsConfigHttpLoadBalancingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAddonsConfigHttpLoadBalancingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Addons<wbr>Config<wbr>Istio<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterAddonsConfigIstioConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterAddonsConfigIstioConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAddonsConfigIstioConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAddonsConfigIstioConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auth</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authentication type between services in Istio. Available options include `AUTH_MUTUAL_TLS`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auth</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The authentication type between services in Istio. Available options include `AUTH_MUTUAL_TLS`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auth</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The authentication type between services in Istio. Available options include `AUTH_MUTUAL_TLS`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auth</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The authentication type between services in Istio. Available options include `AUTH_MUTUAL_TLS`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Addons<wbr>Config<wbr>Network<wbr>Policy<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterAddonsConfigNetworkPolicyConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterAddonsConfigNetworkPolicyConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAddonsConfigNetworkPolicyConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAddonsConfigNetworkPolicyConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set `disabled = false` to enable.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Authenticator<wbr>Groups<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterAuthenticatorGroupsConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterAuthenticatorGroupsConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAuthenticatorGroupsConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterAuthenticatorGroupsConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the RBAC security group for use with Google security groups in Kubernetes RBAC. Group name must be in format `gke-security-groups@yourdomain.com`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the RBAC security group for use with Google security groups in Kubernetes RBAC. Group name must be in format `gke-security-groups@yourdomain.com`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>security<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the RBAC security group for use with Google security groups in Kubernetes RBAC. Group name must be in format `gke-security-groups@yourdomain.com`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>security<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the RBAC security group for use with Google security groups in Kubernetes RBAC. Group name must be in format `gke-security-groups@yourdomain.com`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Autoscaling</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterAutoscaling">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterAutoscaling">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterClusterAutoscalingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterClusterAutoscalingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Provisioning<wbr>Defaults</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscalingautoprovisioningdefaults">Cluster<wbr>Cluster<wbr>Autoscaling<wbr>Auto<wbr>Provisioning<wbr>Defaults<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Contains defaults for a node pool created by NAP.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscaling<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Configuration
options for the [Autoscaling profile](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles)
feature, which lets you choose whether the cluster autoscaler should optimize for resource utilization or resource availability
when deciding to remove nodes from a cluster. Can be `BALANCED` or `OPTIMIZE_UTILIZATION`. Defaults to `BALANCED`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscalingresourcelimit">List&lt;Cluster<wbr>Cluster<wbr>Autoscaling<wbr>Resource<wbr>Limit<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Global constraints for machine resources in the
cluster. Configuring the `cpu` and `memory` types is required if node
auto-provisioning is enabled. These limits will apply to node pool autoscaling
in addition to node auto-provisioning. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Provisioning<wbr>Defaults</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscalingautoprovisioningdefaults">*Cluster<wbr>Cluster<wbr>Autoscaling<wbr>Auto<wbr>Provisioning<wbr>Defaults</a></span>
    </dt>
    <dd>{{% md %}}Contains defaults for a node pool created by NAP.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscaling<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Configuration
options for the [Autoscaling profile](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles)
feature, which lets you choose whether the cluster autoscaler should optimize for resource utilization or resource availability
when deciding to remove nodes from a cluster. Can be `BALANCED` or `OPTIMIZE_UTILIZATION`. Defaults to `BALANCED`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscalingresourcelimit">[]Cluster<wbr>Cluster<wbr>Autoscaling<wbr>Resource<wbr>Limit</a></span>
    </dt>
    <dd>{{% md %}}Global constraints for machine resources in the
cluster. Configuring the `cpu` and `memory` types is required if node
auto-provisioning is enabled. These limits will apply to node pool autoscaling
in addition to node auto-provisioning. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Provisioning<wbr>Defaults</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscalingautoprovisioningdefaults">Cluster<wbr>Cluster<wbr>Autoscaling<wbr>Auto<wbr>Provisioning<wbr>Defaults?</a></span>
    </dt>
    <dd>{{% md %}}Contains defaults for a node pool created by NAP.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscaling<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Configuration
options for the [Autoscaling profile](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles)
feature, which lets you choose whether the cluster autoscaler should optimize for resource utilization or resource availability
when deciding to remove nodes from a cluster. Can be `BALANCED` or `OPTIMIZE_UTILIZATION`. Defaults to `BALANCED`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscalingresourcelimit">Cluster<wbr>Cluster<wbr>Autoscaling<wbr>Resource<wbr>Limit[]?</a></span>
    </dt>
    <dd>{{% md %}}Global constraints for machine resources in the
cluster. Configuring the `cpu` and `memory` types is required if node
auto-provisioning is enabled. These limits will apply to node pool autoscaling
in addition to node auto-provisioning. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Provisioning<wbr>Defaults</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscalingautoprovisioningdefaults">Dict[Cluster<wbr>Cluster<wbr>Autoscaling<wbr>Auto<wbr>Provisioning<wbr>Defaults]</a></span>
    </dt>
    <dd>{{% md %}}Contains defaults for a node pool created by NAP.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscaling<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Configuration
options for the [Autoscaling profile](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles)
feature, which lets you choose whether the cluster autoscaler should optimize for resource utilization or resource availability
when deciding to remove nodes from a cluster. Can be `BALANCED` or `OPTIMIZE_UTILIZATION`. Defaults to `BALANCED`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterclusterautoscalingresourcelimit">List[Cluster<wbr>Cluster<wbr>Autoscaling<wbr>Resource<wbr>Limit]</a></span>
    </dt>
    <dd>{{% md %}}Global constraints for machine resources in the
cluster. Configuring the `cpu` and `memory` types is required if node
auto-provisioning is enabled. These limits will apply to node pool autoscaling
in addition to node auto-provisioning. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Autoscaling<wbr>Auto<wbr>Provisioning<wbr>Defaults</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterAutoscalingAutoProvisioningDefaults">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterAutoscalingAutoProvisioningDefaults">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterClusterAutoscalingAutoProvisioningDefaultsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterClusterAutoscalingAutoProvisioningDefaultsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes to be made available
on all of the node VMs under the "default" service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
In order to use the configured `oauth_scopes` for logging and monitoring, the service account being used needs the
[roles/logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles) and
[roles/monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles) roles.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes to be made available
on all of the node VMs under the "default" service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
In order to use the configured `oauth_scopes` for logging and monitoring, the service account being used needs the
[roles/logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles) and
[roles/monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles) roles.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes to be made available
on all of the node VMs under the "default" service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
In order to use the configured `oauth_scopes` for logging and monitoring, the service account being used needs the
[roles/logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles) and
[roles/monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles) roles.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes to be made available
on all of the node VMs under the "default" service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>account</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
In order to use the configured `oauth_scopes` for logging and monitoring, the service account being used needs the
[roles/logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles) and
[roles/monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles) roles.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Cluster<wbr>Autoscaling<wbr>Resource<wbr>Limit</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterClusterAutoscalingResourceLimit">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterClusterAutoscalingResourceLimit">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterClusterAutoscalingResourceLimitArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterClusterAutoscalingResourceLimitOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Maximum</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Maximum amount of the resource in the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Minimum</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Minimum amount of the resource in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the resource. For example, `cpu` and
`memory`.  See the [guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for a list of types.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Maximum</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Maximum amount of the resource in the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Minimum</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Minimum amount of the resource in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the resource. For example, `cpu` and
`memory`.  See the [guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for a list of types.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>maximum</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Maximum amount of the resource in the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>minimum</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Minimum amount of the resource in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the resource. For example, `cpu` and
`memory`.  See the [guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for a list of types.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>maximum</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Maximum amount of the resource in the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>minimum</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Minimum amount of the resource in the cluster.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of the resource. For example, `cpu` and
`memory`.  See the [guide to using Node Auto-Provisioning](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
for a list of types.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Database<wbr>Encryption</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterDatabaseEncryption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterDatabaseEncryption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterDatabaseEncryptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterDatabaseEncryptionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the key to use to encrypt/decrypt secrets.  See the [DatabaseEncryption definition](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#Cluster.DatabaseEncryption) for more information.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`ENCRYPTED` or `DECRYPTED`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}the key to use to encrypt/decrypt secrets.  See the [DatabaseEncryption definition](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#Cluster.DatabaseEncryption) for more information.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`ENCRYPTED` or `DECRYPTED`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}the key to use to encrypt/decrypt secrets.  See the [DatabaseEncryption definition](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#Cluster.DatabaseEncryption) for more information.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}`ENCRYPTED` or `DECRYPTED`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}the key to use to encrypt/decrypt secrets.  See the [DatabaseEncryption definition](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#Cluster.DatabaseEncryption) for more information.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}`ENCRYPTED` or `DECRYPTED`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Ip<wbr>Allocation<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterIpAllocationPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterIpAllocationPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterIpAllocationPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterIpAllocationPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address range for the cluster pod IPs.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Secondary<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the existing secondary
range in the cluster's subnetwork to use for pod IP addresses. Alternatively,
`cluster_ipv4_cidr_block` can be used to automatically create a GKE-managed one.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Services<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address range of the services IPs in this cluster.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Services<wbr>Secondary<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the existing
secondary range in the cluster's subnetwork to use for service `ClusterIP`s.
Alternatively, `services_ipv4_cidr_block` can be used to automatically create a
GKE-managed one.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IP address range for the cluster pod IPs.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Secondary<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the existing secondary
range in the cluster's subnetwork to use for pod IP addresses. Alternatively,
`cluster_ipv4_cidr_block` can be used to automatically create a GKE-managed one.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Services<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IP address range of the services IPs in this cluster.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Services<wbr>Secondary<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the existing
secondary range in the cluster's subnetwork to use for service `ClusterIP`s.
Alternatively, `services_ipv4_cidr_block` can be used to automatically create a
GKE-managed one.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address range for the cluster pod IPs.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Secondary<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the existing secondary
range in the cluster's subnetwork to use for pod IP addresses. Alternatively,
`cluster_ipv4_cidr_block` can be used to automatically create a GKE-managed one.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>services<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP address range of the services IPs in this cluster.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>services<wbr>Secondary<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the existing
secondary range in the cluster's subnetwork to use for service `ClusterIP`s.
Alternatively, `services_ipv4_cidr_block` can be used to automatically create a
GKE-managed one.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP address range for the cluster pod IPs.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Secondary<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the existing secondary
range in the cluster's subnetwork to use for pod IP addresses. Alternatively,
`cluster_ipv4_cidr_block` can be used to automatically create a GKE-managed one.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>services<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP address range of the services IPs in this cluster.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>services<wbr>Secondary<wbr>Range<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the existing
secondary range in the cluster's subnetwork to use for service `ClusterIP`s.
Alternatively, `services_ipv4_cidr_block` can be used to automatically create a
GKE-managed one.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Maintenance<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterMaintenancePolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterMaintenancePolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterMaintenancePolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterMaintenancePolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Daily<wbr>Maintenance<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicydailymaintenancewindow">Cluster<wbr>Maintenance<wbr>Policy<wbr>Daily<wbr>Maintenance<wbr>Window<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Time window specified for daily maintenance operations.
Specify `start_time` in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) format "HH:MM”,
where HH : \[00-23\] and MM : \[00-59\] GMT. For example:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurring<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicyrecurringwindow">Cluster<wbr>Maintenance<wbr>Policy<wbr>Recurring<wbr>Window<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Time window for
recurring maintenance operations.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Daily<wbr>Maintenance<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicydailymaintenancewindow">*Cluster<wbr>Maintenance<wbr>Policy<wbr>Daily<wbr>Maintenance<wbr>Window</a></span>
    </dt>
    <dd>{{% md %}}Time window specified for daily maintenance operations.
Specify `start_time` in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) format "HH:MM”,
where HH : \[00-23\] and MM : \[00-59\] GMT. For example:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurring<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicyrecurringwindow">*Cluster<wbr>Maintenance<wbr>Policy<wbr>Recurring<wbr>Window</a></span>
    </dt>
    <dd>{{% md %}}Time window for
recurring maintenance operations.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>daily<wbr>Maintenance<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicydailymaintenancewindow">Cluster<wbr>Maintenance<wbr>Policy<wbr>Daily<wbr>Maintenance<wbr>Window?</a></span>
    </dt>
    <dd>{{% md %}}Time window specified for daily maintenance operations.
Specify `start_time` in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) format "HH:MM”,
where HH : \[00-23\] and MM : \[00-59\] GMT. For example:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurring<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicyrecurringwindow">Cluster<wbr>Maintenance<wbr>Policy<wbr>Recurring<wbr>Window?</a></span>
    </dt>
    <dd>{{% md %}}Time window for
recurring maintenance operations.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>daily<wbr>Maintenance<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicydailymaintenancewindow">Dict[Cluster<wbr>Maintenance<wbr>Policy<wbr>Daily<wbr>Maintenance<wbr>Window]</a></span>
    </dt>
    <dd>{{% md %}}Time window specified for daily maintenance operations.
Specify `start_time` in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) format "HH:MM”,
where HH : \[00-23\] and MM : \[00-59\] GMT. For example:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurring<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermaintenancepolicyrecurringwindow">Dict[Cluster<wbr>Maintenance<wbr>Policy<wbr>Recurring<wbr>Window]</a></span>
    </dt>
    <dd>{{% md %}}Time window for
recurring maintenance operations.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Maintenance<wbr>Policy<wbr>Daily<wbr>Maintenance<wbr>Window</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterMaintenancePolicyDailyMaintenanceWindow">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterMaintenancePolicyDailyMaintenanceWindow">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterMaintenancePolicyDailyMaintenanceWindowArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterMaintenancePolicyDailyMaintenanceWindowOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Maintenance<wbr>Policy<wbr>Recurring<wbr>Window</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterMaintenancePolicyRecurringWindow">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterMaintenancePolicyRecurringWindow">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterMaintenancePolicyRecurringWindowArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterMaintenancePolicyRecurringWindowOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Recurrence</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start<wbr>Time</span>
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
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Recurrence</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start<wbr>Time</span>
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
        <span>end<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>recurrence</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start<wbr>Time</span>
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
        <span>end<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>recurrence</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Master<wbr>Auth</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterMasterAuth">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterMasterAuth">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterMasterAuthArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterMasterAuthOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthclientcertificateconfig">Cluster<wbr>Master<wbr>Auth<wbr>Client<wbr>Certificate<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Whether client certificate authorization is enabled for this cluster.  For example:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The password to use for HTTP basic authentication when accessing
the Kubernetes master endpoint.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The username to use for HTTP basic authentication when accessing
the Kubernetes master endpoint. If not present basic auth will be disabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthclientcertificateconfig">*Cluster<wbr>Master<wbr>Auth<wbr>Client<wbr>Certificate<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Whether client certificate authorization is enabled for this cluster.  For example:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The password to use for HTTP basic authentication when accessing
the Kubernetes master endpoint.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The username to use for HTTP basic authentication when accessing
the Kubernetes master endpoint. If not present basic auth will be disabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthclientcertificateconfig">Cluster<wbr>Master<wbr>Auth<wbr>Client<wbr>Certificate<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Whether client certificate authorization is enabled for this cluster.  For example:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The password to use for HTTP basic authentication when accessing
the Kubernetes master endpoint.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The username to use for HTTP basic authentication when accessing
the Kubernetes master endpoint. If not present basic auth will be disabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Certificate<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthclientcertificateconfig">Dict[Cluster<wbr>Master<wbr>Auth<wbr>Client<wbr>Certificate<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Whether client certificate authorization is enabled for this cluster.  For example:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cluster<wbr>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The password to use for HTTP basic authentication when accessing
the Kubernetes master endpoint.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The username to use for HTTP basic authentication when accessing
the Kubernetes master endpoint. If not present basic auth will be disabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Master<wbr>Auth<wbr>Client<wbr>Certificate<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterMasterAuthClientCertificateConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterMasterAuthClientCertificateConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterMasterAuthClientCertificateConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterMasterAuthClientCertificateConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Issue<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Issue<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>issue<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>issue<wbr>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterMasterAuthorizedNetworksConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterMasterAuthorizedNetworksConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterMasterAuthorizedNetworksConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterMasterAuthorizedNetworksConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cidr<wbr>Blocks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfigcidrblock">List&lt;Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config<wbr>Cidr<wbr>Block<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}External networks that can access the
Kubernetes cluster master through HTTPS.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cidr<wbr>Blocks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfigcidrblock">[]Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config<wbr>Cidr<wbr>Block</a></span>
    </dt>
    <dd>{{% md %}}External networks that can access the
Kubernetes cluster master through HTTPS.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cidr<wbr>Blocks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfigcidrblock">Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config<wbr>Cidr<wbr>Block[]?</a></span>
    </dt>
    <dd>{{% md %}}External networks that can access the
Kubernetes cluster master through HTTPS.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cidr<wbr>Blocks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clustermasterauthorizednetworksconfigcidrblock">List[Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config<wbr>Cidr<wbr>Block]</a></span>
    </dt>
    <dd>{{% md %}}External networks that can access the
Kubernetes cluster master through HTTPS.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Master<wbr>Authorized<wbr>Networks<wbr>Config<wbr>Cidr<wbr>Block</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterMasterAuthorizedNetworksConfigCidrBlock">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterMasterAuthorizedNetworksConfigCidrBlock">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterMasterAuthorizedNetworksConfigCidrBlockArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterMasterAuthorizedNetworksConfigCidrBlockOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}External network that can access Kubernetes master through HTTPS.
Must be specified in CIDR notation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Field for users to identify CIDR blocks.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}External network that can access Kubernetes master through HTTPS.
Must be specified in CIDR notation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Field for users to identify CIDR blocks.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}External network that can access Kubernetes master through HTTPS.
Must be specified in CIDR notation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Field for users to identify CIDR blocks.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cidr_<wbr>block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}External network that can access Kubernetes master through HTTPS.
Must be specified in CIDR notation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Field for users to identify CIDR blocks.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Network<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNetworkPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNetworkPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNetworkPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNetworkPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The selected network policy provider. Defaults to PROVIDER_UNSPECIFIED.
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
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The selected network policy provider. Defaults to PROVIDER_UNSPECIFIED.
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
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The selected network policy provider. Defaults to PROVIDER_UNSPECIFIED.
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
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>provider</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The selected network policy provider. Defaults to PROVIDER_UNSPECIFIED.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodeConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodeConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodeConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodeConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Kms<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: https://cloud.google.com/compute/docs/disks/customer-managed-encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of the disk attached to each node
(e.g. 'pd-standard' or 'pd-ssd'). If unspecified, the default disk type is 'pd-standard'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigguestaccelerator">List&lt;Cluster<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance.
Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes labels (key/value pairs) to be applied to each node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Ssd<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type.
Defaults to `n1-standard-1`. To create a custom machine type, value should be set as specified
[here](https://cloud.google.com/compute/docs/reference/latest/instances#machineType).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}The metadata key/value pairs assigned to instances in
the cluster. From GKE `1.12` onwards, `disable-legacy-endpoints` is set to
`true` by the API; if `metadata` is set but that default value is not
included, the provider will attempt to unset the value. To avoid this, set the
value in your config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as `Intel Haswell`. See the
[official documentation](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes to be made available
on all of the node VMs under the "default" service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}A boolean that represents whether or not the underlying node VMs
are preemptible. See the [official documentation](https://cloud.google.com/container-engine/docs/preemptible-vm)
for more information. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sandbox<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigsandboxconfig">Cluster<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}[GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) configuration. When enabling this feature you must specify `image_type = "COS_CONTAINERD"` and `node_version = "1.12.7-gke.17"` or later to use it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
In order to use the configured `oauth_scopes` for logging and monitoring, the service account being used needs the
[roles/logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles) and
[roles/monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles) roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigshieldedinstanceconfig">Cluster<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Shielded Instance options. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigtaint">List&lt;Cluster<wbr>Node<wbr>Config<wbr>Taint<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of [Kubernetes taints](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)
to apply to nodes. GKE's API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause the provider to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through `kubectl`), and it's recommended that you do not use
this field to manage taints. If you do, `lifecycle.ignore_changes` is
recommended. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Workload<wbr>Metadata<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigworkloadmetadataconfig">Cluster<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Metadata configuration to expose to workloads on the node pool.
Structure is documented below.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: https://cloud.google.com/compute/docs/disks/customer-managed-encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Type of the disk attached to each node
(e.g. 'pd-standard' or 'pd-ssd'). If unspecified, the default disk type is 'pd-standard'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigguestaccelerator">[]Cluster<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance.
Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The Kubernetes labels (key/value pairs) to be applied to each node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Ssd<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type.
Defaults to `n1-standard-1`. To create a custom machine type, value should be set as specified
[here](https://cloud.google.com/compute/docs/reference/latest/instances#machineType).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The metadata key/value pairs assigned to instances in
the cluster. From GKE `1.12` onwards, `disable-legacy-endpoints` is set to
`true` by the API; if `metadata` is set but that default value is not
included, the provider will attempt to unset the value. To avoid this, set the
value in your config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as `Intel Haswell`. See the
[official documentation](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes to be made available
on all of the node VMs under the "default" service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}A boolean that represents whether or not the underlying node VMs
are preemptible. See the [official documentation](https://cloud.google.com/container-engine/docs/preemptible-vm)
for more information. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sandbox<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigsandboxconfig">*Cluster<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}[GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) configuration. When enabling this feature you must specify `image_type = "COS_CONTAINERD"` and `node_version = "1.12.7-gke.17"` or later to use it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
In order to use the configured `oauth_scopes` for logging and monitoring, the service account being used needs the
[roles/logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles) and
[roles/monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles) roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigshieldedinstanceconfig">*Cluster<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Shielded Instance options. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigtaint">[]Cluster<wbr>Node<wbr>Config<wbr>Taint</a></span>
    </dt>
    <dd>{{% md %}}A list of [Kubernetes taints](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)
to apply to nodes. GKE's API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause the provider to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through `kubectl`), and it's recommended that you do not use
this field to manage taints. If you do, `lifecycle.ignore_changes` is
recommended. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Workload<wbr>Metadata<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigworkloadmetadataconfig">*Cluster<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Metadata configuration to expose to workloads on the node pool.
Structure is documented below.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: https://cloud.google.com/compute/docs/disks/customer-managed-encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of the disk attached to each node
(e.g. 'pd-standard' or 'pd-ssd'). If unspecified, the default disk type is 'pd-standard'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigguestaccelerator">Cluster<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator[]?</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance.
Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes labels (key/value pairs) to be applied to each node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local<wbr>Ssd<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type.
Defaults to `n1-standard-1`. To create a custom machine type, value should be set as specified
[here](https://cloud.google.com/compute/docs/reference/latest/instances#machineType).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}The metadata key/value pairs assigned to instances in
the cluster. From GKE `1.12` onwards, `disable-legacy-endpoints` is set to
`true` by the API; if `metadata` is set but that default value is not
included, the provider will attempt to unset the value. To avoid this, set the
value in your config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as `Intel Haswell`. See the
[official documentation](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes to be made available
on all of the node VMs under the "default" service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}A boolean that represents whether or not the underlying node VMs
are preemptible. See the [official documentation](https://cloud.google.com/container-engine/docs/preemptible-vm)
for more information. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sandbox<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigsandboxconfig">Cluster<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}[GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) configuration. When enabling this feature you must specify `image_type = "COS_CONTAINERD"` and `node_version = "1.12.7-gke.17"` or later to use it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
In order to use the configured `oauth_scopes` for logging and monitoring, the service account being used needs the
[roles/logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles) and
[roles/monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles) roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigshieldedinstanceconfig">Cluster<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Shielded Instance options. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigtaint">Cluster<wbr>Node<wbr>Config<wbr>Taint[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of [Kubernetes taints](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)
to apply to nodes. GKE's API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause the provider to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through `kubectl`), and it's recommended that you do not use
this field to manage taints. If you do, `lifecycle.ignore_changes` is
recommended. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>workload<wbr>Metadata<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigworkloadmetadataconfig">Cluster<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Metadata configuration to expose to workloads on the node pool.
Structure is documented below.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: https://cloud.google.com/compute/docs/disks/customer-managed-encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>size_<wbr>gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type of the disk attached to each node
(e.g. 'pd-standard' or 'pd-ssd'). If unspecified, the default disk type is 'pd-standard'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest_<wbr>accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigguestaccelerator">List[Cluster<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator]</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance.
Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The Kubernetes labels (key/value pairs) to be applied to each node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local<wbr>Ssd<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>machine_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type.
Defaults to `n1-standard-1`. To create a custom machine type, value should be set as specified
[here](https://cloud.google.com/compute/docs/reference/latest/instances#machineType).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The metadata key/value pairs assigned to instances in
the cluster. From GKE `1.12` onwards, `disable-legacy-endpoints` is set to
`true` by the API; if `metadata` is set but that default value is not
included, the provider will attempt to unset the value. To avoid this, set the
value in your config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as `Intel Haswell`. See the
[official documentation](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes to be made available
on all of the node VMs under the "default" service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}A boolean that represents whether or not the underlying node VMs
are preemptible. See the [official documentation](https://cloud.google.com/container-engine/docs/preemptible-vm)
for more information. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sandbox<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigsandboxconfig">Dict[Cluster<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}[GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) configuration. When enabling this feature you must specify `image_type = "COS_CONTAINERD"` and `node_version = "1.12.7-gke.17"` or later to use it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>account</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
In order to use the configured `oauth_scopes` for logging and monitoring, the service account being used needs the
[roles/logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles) and
[roles/monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles) roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shielded_<wbr>instance_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigshieldedinstanceconfig">Dict[Cluster<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Shielded Instance options. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigtaint">List[Cluster<wbr>Node<wbr>Config<wbr>Taint]</a></span>
    </dt>
    <dd>{{% md %}}A list of [Kubernetes taints](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)
to apply to nodes. GKE's API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause the provider to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through `kubectl`), and it's recommended that you do not use
this field to manage taints. If you do, `lifecycle.ignore_changes` is
recommended. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>workload<wbr>Metadata<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodeconfigworkloadmetadataconfig">Dict[Cluster<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Metadata configuration to expose to workloads on the node pool.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodeConfigGuestAccelerator">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodeConfigGuestAccelerator">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodeConfigGuestAcceleratorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodeConfigGuestAcceleratorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodeConfigSandboxConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodeConfigSandboxConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodeConfigSandboxConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodeConfigSandboxConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Sandbox<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Which sandbox to use for pods in the node pool.
Accepted values are:
{{% /md %}}</dd>

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
    <dd>{{% md %}}Which sandbox to use for pods in the node pool.
Accepted values are:
{{% /md %}}</dd>

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
    <dd>{{% md %}}Which sandbox to use for pods in the node pool.
Accepted values are:
{{% /md %}}</dd>

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
    <dd>{{% md %}}Which sandbox to use for pods in the node pool.
Accepted values are:
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodeConfigShieldedInstanceConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodeConfigShieldedInstanceConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodeConfigShieldedInstanceConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodeConfigShieldedInstanceConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Integrity<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Defines if the instance has integrity monitoring enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Defines if the instance has Secure Boot enabled.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Defines if the instance has integrity monitoring enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Defines if the instance has Secure Boot enabled.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Defines if the instance has integrity monitoring enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Defines if the instance has Secure Boot enabled.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Defines if the instance has integrity monitoring enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Defines if the instance has Secure Boot enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Config<wbr>Taint</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodeConfigTaint">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodeConfigTaint">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodeConfigTaintArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodeConfigTaintOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Effect for taint. Accepted values are `NO_SCHEDULE`, `PREFER_NO_SCHEDULE`, and `NO_EXECUTE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Key for taint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value for taint.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Effect for taint. Accepted values are `NO_SCHEDULE`, `PREFER_NO_SCHEDULE`, and `NO_EXECUTE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Key for taint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value for taint.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Effect for taint. Accepted values are `NO_SCHEDULE`, `PREFER_NO_SCHEDULE`, and `NO_EXECUTE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Key for taint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value for taint.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Effect for taint. Accepted values are `NO_SCHEDULE`, `PREFER_NO_SCHEDULE`, and `NO_EXECUTE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Key for taint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Value for taint.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodeConfigWorkloadMetadataConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodeConfigWorkloadMetadataConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodeConfigWorkloadMetadataConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodeConfigWorkloadMetadataConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Node<wbr>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}How to expose the node metadata to the workload running on the node.
Accepted values are:
* UNSPECIFIED: Not Set
* SECURE: Prevent workloads not in hostNetwork from accessing certain VM metadata, specifically kube-env, which contains Kubelet credentials, and the instance identity token. See [Metadata Concealment](https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy) documentation.
* EXPOSE: Expose all VM metadata to pods.
* GKE_METADATA_SERVER: Enables [workload identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) on the node.
{{% /md %}}</dd>

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
    <dd>{{% md %}}How to expose the node metadata to the workload running on the node.
Accepted values are:
* UNSPECIFIED: Not Set
* SECURE: Prevent workloads not in hostNetwork from accessing certain VM metadata, specifically kube-env, which contains Kubelet credentials, and the instance identity token. See [Metadata Concealment](https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy) documentation.
* EXPOSE: Expose all VM metadata to pods.
* GKE_METADATA_SERVER: Enables [workload identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) on the node.
{{% /md %}}</dd>

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
    <dd>{{% md %}}How to expose the node metadata to the workload running on the node.
Accepted values are:
* UNSPECIFIED: Not Set
* SECURE: Prevent workloads not in hostNetwork from accessing certain VM metadata, specifically kube-env, which contains Kubelet credentials, and the instance identity token. See [Metadata Concealment](https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy) documentation.
* EXPOSE: Expose all VM metadata to pods.
* GKE_METADATA_SERVER: Enables [workload identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) on the node.
{{% /md %}}</dd>

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
    <dd>{{% md %}}How to expose the node metadata to the workload running on the node.
Accepted values are:
* UNSPECIFIED: Not Set
* SECURE: Prevent workloads not in hostNetwork from accessing certain VM metadata, specifically kube-env, which contains Kubelet credentials, and the instance identity token. See [Metadata Concealment](https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy) documentation.
* EXPOSE: Expose all VM metadata to pods.
* GKE_METADATA_SERVER: Enables [workload identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) on the node.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Pool</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodePool">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodePool">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolautoscaling">Cluster<wbr>Node<wbr>Pool<wbr>Autoscaling<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of instance group URLs which have been assigned
to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolmanagement">Cluster<wbr>Node<wbr>Pool<wbr>Management<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfig">Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolupgradesettings">Cluster<wbr>Node<wbr>Pool<wbr>Upgrade<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
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
        <span>Autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolautoscaling">*Cluster<wbr>Node<wbr>Pool<wbr>Autoscaling</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of instance group URLs which have been assigned
to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolmanagement">*Cluster<wbr>Node<wbr>Pool<wbr>Management</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfig">*Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Upgrade<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolupgradesettings">*Cluster<wbr>Node<wbr>Pool<wbr>Upgrade<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
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
        <span>autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolautoscaling">Cluster<wbr>Node<wbr>Pool<wbr>Autoscaling?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Group<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of instance group URLs which have been assigned
to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolmanagement">Cluster<wbr>Node<wbr>Pool<wbr>Management?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Pods<wbr>Per<wbr>Node</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfig">Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node<wbr>Locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolupgradesettings">Cluster<wbr>Node<wbr>Pool<wbr>Upgrade<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
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
        <span>autoscaling</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolautoscaling">Dict[Cluster<wbr>Node<wbr>Pool<wbr>Autoscaling]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>initial_<wbr>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of nodes to create in this
cluster's default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if `node_pool` is not set. If you're using
`gcp.container.NodePool` objects with no default node pool, you'll need to
set this to a value of at least `1`, alongside setting
`remove_default_node_pool` to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>group_<wbr>urls</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of instance group URLs which have been assigned
to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>management</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolmanagement">Dict[Cluster<wbr>Node<wbr>Pool<wbr>Management]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>pods_<wbr>per_<wbr>node</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the cluster, unique within the project and
location.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfig">Dict[Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
`gcp.container.NodePool` or a `node_pool` block; this configuration
manages the default node pool, which isn't recommended to be used with
this provider. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>node_<wbr>locations</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of zones in which the cluster's nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster's zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster's zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>upgrade_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolupgradesettings">Dict[Cluster<wbr>Node<wbr>Pool<wbr>Upgrade<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Pool<wbr>Autoscaling</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodePoolAutoscaling">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodePoolAutoscaling">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolAutoscalingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolAutoscalingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Min<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Min<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>min<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>min<wbr>Node<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Pool<wbr>Management</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodePoolManagement">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodePoolManagement">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolManagementArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolManagementOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Repair</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Upgrade</span>
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
        <span>Auto<wbr>Repair</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Upgrade</span>
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
        <span>auto<wbr>Repair</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Upgrade</span>
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
        <span>auto<wbr>Repair</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Upgrade</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodePoolNodeConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodePoolNodeConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolNodeConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolNodeConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Boot<wbr>Disk<wbr>Kms<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: https://cloud.google.com/compute/docs/disks/customer-managed-encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of the disk attached to each node
(e.g. 'pd-standard' or 'pd-ssd'). If unspecified, the default disk type is 'pd-standard'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigguestaccelerator">List&lt;Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance.
Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes labels (key/value pairs) to be applied to each node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Ssd<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type.
Defaults to `n1-standard-1`. To create a custom machine type, value should be set as specified
[here](https://cloud.google.com/compute/docs/reference/latest/instances#machineType).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}The metadata key/value pairs assigned to instances in
the cluster. From GKE `1.12` onwards, `disable-legacy-endpoints` is set to
`true` by the API; if `metadata` is set but that default value is not
included, the provider will attempt to unset the value. To avoid this, set the
value in your config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as `Intel Haswell`. See the
[official documentation](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes to be made available
on all of the node VMs under the "default" service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}A boolean that represents whether or not the underlying node VMs
are preemptible. See the [official documentation](https://cloud.google.com/container-engine/docs/preemptible-vm)
for more information. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sandbox<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigsandboxconfig">Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}[GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) configuration. When enabling this feature you must specify `image_type = "COS_CONTAINERD"` and `node_version = "1.12.7-gke.17"` or later to use it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
In order to use the configured `oauth_scopes` for logging and monitoring, the service account being used needs the
[roles/logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles) and
[roles/monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles) roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigshieldedinstanceconfig">Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Shielded Instance options. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigtaint">List&lt;Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Taint<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of [Kubernetes taints](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)
to apply to nodes. GKE's API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause the provider to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through `kubectl`), and it's recommended that you do not use
this field to manage taints. If you do, `lifecycle.ignore_changes` is
recommended. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Workload<wbr>Metadata<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigworkloadmetadataconfig">Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Metadata configuration to expose to workloads on the node pool.
Structure is documented below.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: https://cloud.google.com/compute/docs/disks/customer-managed-encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Type of the disk attached to each node
(e.g. 'pd-standard' or 'pd-ssd'). If unspecified, the default disk type is 'pd-standard'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigguestaccelerator">[]Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance.
Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The Kubernetes labels (key/value pairs) to be applied to each node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Ssd<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type.
Defaults to `n1-standard-1`. To create a custom machine type, value should be set as specified
[here](https://cloud.google.com/compute/docs/reference/latest/instances#machineType).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The metadata key/value pairs assigned to instances in
the cluster. From GKE `1.12` onwards, `disable-legacy-endpoints` is set to
`true` by the API; if `metadata` is set but that default value is not
included, the provider will attempt to unset the value. To avoid this, set the
value in your config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as `Intel Haswell`. See the
[official documentation](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes to be made available
on all of the node VMs under the "default" service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}A boolean that represents whether or not the underlying node VMs
are preemptible. See the [official documentation](https://cloud.google.com/container-engine/docs/preemptible-vm)
for more information. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sandbox<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigsandboxconfig">*Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}[GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) configuration. When enabling this feature you must specify `image_type = "COS_CONTAINERD"` and `node_version = "1.12.7-gke.17"` or later to use it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
In order to use the configured `oauth_scopes` for logging and monitoring, the service account being used needs the
[roles/logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles) and
[roles/monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles) roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigshieldedinstanceconfig">*Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Shielded Instance options. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigtaint">[]Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Taint</a></span>
    </dt>
    <dd>{{% md %}}A list of [Kubernetes taints](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)
to apply to nodes. GKE's API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause the provider to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through `kubectl`), and it's recommended that you do not use
this field to manage taints. If you do, `lifecycle.ignore_changes` is
recommended. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Workload<wbr>Metadata<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigworkloadmetadataconfig">*Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Metadata configuration to expose to workloads on the node pool.
Structure is documented below.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: https://cloud.google.com/compute/docs/disks/customer-managed-encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Size<wbr>Gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of the disk attached to each node
(e.g. 'pd-standard' or 'pd-ssd'). If unspecified, the default disk type is 'pd-standard'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest<wbr>Accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigguestaccelerator">Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator[]?</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance.
Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}The Kubernetes labels (key/value pairs) to be applied to each node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local<wbr>Ssd<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>machine<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type.
Defaults to `n1-standard-1`. To create a custom machine type, value should be set as specified
[here](https://cloud.google.com/compute/docs/reference/latest/instances#machineType).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}The metadata key/value pairs assigned to instances in
the cluster. From GKE `1.12` onwards, `disable-legacy-endpoints` is set to
`true` by the API; if `metadata` is set but that default value is not
included, the provider will attempt to unset the value. To avoid this, set the
value in your config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Cpu<wbr>Platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as `Intel Haswell`. See the
[official documentation](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes to be made available
on all of the node VMs under the "default" service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}A boolean that represents whether or not the underlying node VMs
are preemptible. See the [official documentation](https://cloud.google.com/container-engine/docs/preemptible-vm)
for more information. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sandbox<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigsandboxconfig">Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}[GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) configuration. When enabling this feature you must specify `image_type = "COS_CONTAINERD"` and `node_version = "1.12.7-gke.17"` or later to use it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
In order to use the configured `oauth_scopes` for logging and monitoring, the service account being used needs the
[roles/logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles) and
[roles/monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles) roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shielded<wbr>Instance<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigshieldedinstanceconfig">Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Shielded Instance options. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigtaint">Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Taint[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of [Kubernetes taints](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)
to apply to nodes. GKE's API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause the provider to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through `kubectl`), and it's recommended that you do not use
this field to manage taints. If you do, `lifecycle.ignore_changes` is
recommended. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>workload<wbr>Metadata<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigworkloadmetadataconfig">Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Metadata configuration to expose to workloads on the node pool.
Structure is documented below.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: https://cloud.google.com/compute/docs/disks/customer-managed-encryption
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk_<wbr>size_<wbr>gb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type of the disk attached to each node
(e.g. 'pd-standard' or 'pd-ssd'). If unspecified, the default disk type is 'pd-standard'
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>guest_<wbr>accelerators</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigguestaccelerator">List[Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator]</a></span>
    </dt>
    <dd>{{% md %}}List of the type and count of accelerator cards attached to the instance.
Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The Kubernetes labels (key/value pairs) to be applied to each node.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local<wbr>Ssd<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>machine_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of a Google Compute Engine machine type.
Defaults to `n1-standard-1`. To create a custom machine type, value should be set as specified
[here](https://cloud.google.com/compute/docs/reference/latest/instances#machineType).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The metadata key/value pairs assigned to instances in
the cluster. From GKE `1.12` onwards, `disable-legacy-endpoints` is set to
`true` by the API; if `metadata` is set but that default value is not
included, the provider will attempt to unset the value. To avoid this, set the
value in your config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>cpu_<wbr>platform</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as `Intel Haswell`. See the
[official documentation](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)
for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The set of Google API scopes to be made available
on all of the node VMs under the "default" service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preemptible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}A boolean that represents whether or not the underlying node VMs
are preemptible. See the [official documentation](https://cloud.google.com/container-engine/docs/preemptible-vm)
for more information. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sandbox<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigsandboxconfig">Dict[Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}[GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) configuration. When enabling this feature you must specify `image_type = "COS_CONTAINERD"` and `node_version = "1.12.7-gke.17"` or later to use it.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>account</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The service account to be used by the Node VMs.
If not specified, the "default" service account is used.
In order to use the configured `oauth_scopes` for logging and monitoring, the service account being used needs the
[roles/logging.logWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles) and
[roles/monitoring.metricWriter](https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles) roles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>shielded_<wbr>instance_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigshieldedinstanceconfig">Dict[Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Shielded Instance options. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>taints</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigtaint">List[Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Taint]</a></span>
    </dt>
    <dd>{{% md %}}A list of [Kubernetes taints](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)
to apply to nodes. GKE's API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause the provider to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through `kubectl`), and it's recommended that you do not use
this field to manage taints. If you do, `lifecycle.ignore_changes` is
recommended. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>workload<wbr>Metadata<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusternodepoolnodeconfigworkloadmetadataconfig">Dict[Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Metadata configuration to expose to workloads on the node pool.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Guest<wbr>Accelerator</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodePoolNodeConfigGuestAccelerator">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodePoolNodeConfigGuestAccelerator">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolNodeConfigGuestAcceleratorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolNodeConfigGuestAcceleratorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

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
    <dd>{{% md %}}The number of the guest accelerator cards exposed to this instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Sandbox<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodePoolNodeConfigSandboxConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodePoolNodeConfigSandboxConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolNodeConfigSandboxConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolNodeConfigSandboxConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Sandbox<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Which sandbox to use for pods in the node pool.
Accepted values are:
{{% /md %}}</dd>

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
    <dd>{{% md %}}Which sandbox to use for pods in the node pool.
Accepted values are:
{{% /md %}}</dd>

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
    <dd>{{% md %}}Which sandbox to use for pods in the node pool.
Accepted values are:
{{% /md %}}</dd>

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
    <dd>{{% md %}}Which sandbox to use for pods in the node pool.
Accepted values are:
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Shielded<wbr>Instance<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodePoolNodeConfigShieldedInstanceConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodePoolNodeConfigShieldedInstanceConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolNodeConfigShieldedInstanceConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolNodeConfigShieldedInstanceConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Integrity<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Defines if the instance has integrity monitoring enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Defines if the instance has Secure Boot enabled.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Defines if the instance has integrity monitoring enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Defines if the instance has Secure Boot enabled.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Defines if the instance has integrity monitoring enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Defines if the instance has Secure Boot enabled.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Defines if the instance has integrity monitoring enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Secure<wbr>Boot</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Defines if the instance has Secure Boot enabled.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Taint</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodePoolNodeConfigTaint">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodePoolNodeConfigTaint">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolNodeConfigTaintArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolNodeConfigTaintOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Effect</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Effect for taint. Accepted values are `NO_SCHEDULE`, `PREFER_NO_SCHEDULE`, and `NO_EXECUTE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Key for taint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value for taint.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Effect for taint. Accepted values are `NO_SCHEDULE`, `PREFER_NO_SCHEDULE`, and `NO_EXECUTE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Key for taint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value for taint.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Effect for taint. Accepted values are `NO_SCHEDULE`, `PREFER_NO_SCHEDULE`, and `NO_EXECUTE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Key for taint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Value for taint.
{{% /md %}}</dd>

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
    <dd>{{% md %}}Effect for taint. Accepted values are `NO_SCHEDULE`, `PREFER_NO_SCHEDULE`, and `NO_EXECUTE`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Key for taint.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Value for taint.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Pool<wbr>Node<wbr>Config<wbr>Workload<wbr>Metadata<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodePoolNodeConfigWorkloadMetadataConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodePoolNodeConfigWorkloadMetadataConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolNodeConfigWorkloadMetadataConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolNodeConfigWorkloadMetadataConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Node<wbr>Metadata</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}How to expose the node metadata to the workload running on the node.
Accepted values are:
* UNSPECIFIED: Not Set
* SECURE: Prevent workloads not in hostNetwork from accessing certain VM metadata, specifically kube-env, which contains Kubelet credentials, and the instance identity token. See [Metadata Concealment](https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy) documentation.
* EXPOSE: Expose all VM metadata to pods.
* GKE_METADATA_SERVER: Enables [workload identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) on the node.
{{% /md %}}</dd>

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
    <dd>{{% md %}}How to expose the node metadata to the workload running on the node.
Accepted values are:
* UNSPECIFIED: Not Set
* SECURE: Prevent workloads not in hostNetwork from accessing certain VM metadata, specifically kube-env, which contains Kubelet credentials, and the instance identity token. See [Metadata Concealment](https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy) documentation.
* EXPOSE: Expose all VM metadata to pods.
* GKE_METADATA_SERVER: Enables [workload identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) on the node.
{{% /md %}}</dd>

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
    <dd>{{% md %}}How to expose the node metadata to the workload running on the node.
Accepted values are:
* UNSPECIFIED: Not Set
* SECURE: Prevent workloads not in hostNetwork from accessing certain VM metadata, specifically kube-env, which contains Kubelet credentials, and the instance identity token. See [Metadata Concealment](https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy) documentation.
* EXPOSE: Expose all VM metadata to pods.
* GKE_METADATA_SERVER: Enables [workload identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) on the node.
{{% /md %}}</dd>

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
    <dd>{{% md %}}How to expose the node metadata to the workload running on the node.
Accepted values are:
* UNSPECIFIED: Not Set
* SECURE: Prevent workloads not in hostNetwork from accessing certain VM metadata, specifically kube-env, which contains Kubelet credentials, and the instance identity token. See [Metadata Concealment](https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy) documentation.
* EXPOSE: Expose all VM metadata to pods.
* GKE_METADATA_SERVER: Enables [workload identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) on the node.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Node<wbr>Pool<wbr>Upgrade<wbr>Settings</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterNodePoolUpgradeSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterNodePoolUpgradeSettings">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolUpgradeSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterNodePoolUpgradeSettingsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Surge</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Unavailable</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Unavailable</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Unavailable</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Unavailable</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Pod<wbr>Security<wbr>Policy<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterPodSecurityPolicyConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterPodSecurityPolicyConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterPodSecurityPolicyConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterPodSecurityPolicyConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
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
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
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
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
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
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Private<wbr>Cluster<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterPrivateClusterConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterPrivateClusterConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterPrivateClusterConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterPrivateClusterConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Private<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, the cluster's private
endpoint is used as the cluster endpoint and access through the public endpoint
is disabled. When `false`, either endpoint can be used. This field only applies
to private clusters, when `enable_private_nodes` is `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Private<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enables the private cluster feature,
creating a private endpoint on the cluster. In a private cluster, nodes only
have RFC 1918 private addresses and communicate with the master's private
endpoint via private networking.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP range in CIDR notation to use for
the hosted master network. This range will be used for assigning private IP
addresses to the cluster master(s) and the ILB VIP. This range must not overlap
with any other ranges in use within the cluster's network, and it must be a /28
subnet. See [Private Cluster Limitations](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#limitations)
for more details. This field only applies to private clusters, when
`enable_private_nodes` is `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peering<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the peering between this cluster and the Google owned VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The internal IP address of this cluster's master endpoint.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The external IP address of this cluster's master endpoint.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enable<wbr>Private<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, the cluster's private
endpoint is used as the cluster endpoint and access through the public endpoint
is disabled. When `false`, either endpoint can be used. This field only applies
to private clusters, when `enable_private_nodes` is `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Private<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enables the private cluster feature,
creating a private endpoint on the cluster. In a private cluster, nodes only
have RFC 1918 private addresses and communicate with the master's private
endpoint via private networking.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IP range in CIDR notation to use for
the hosted master network. This range will be used for assigning private IP
addresses to the cluster master(s) and the ILB VIP. This range must not overlap
with any other ranges in use within the cluster's network, and it must be a /28
subnet. See [Private Cluster Limitations](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#limitations)
for more details. This field only applies to private clusters, when
`enable_private_nodes` is `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Peering<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the peering between this cluster and the Google owned VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The internal IP address of this cluster's master endpoint.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The external IP address of this cluster's master endpoint.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enable<wbr>Private<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}When `true`, the cluster's private
endpoint is used as the cluster endpoint and access through the public endpoint
is disabled. When `false`, either endpoint can be used. This field only applies
to private clusters, when `enable_private_nodes` is `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Private<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enables the private cluster feature,
creating a private endpoint on the cluster. In a private cluster, nodes only
have RFC 1918 private addresses and communicate with the master's private
endpoint via private networking.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IP range in CIDR notation to use for
the hosted master network. This range will be used for assigning private IP
addresses to the cluster master(s) and the ILB VIP. This range must not overlap
with any other ranges in use within the cluster's network, and it must be a /28
subnet. See [Private Cluster Limitations](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#limitations)
for more details. This field only applies to private clusters, when
`enable_private_nodes` is `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peering<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the peering between this cluster and the Google owned VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The internal IP address of this cluster's master endpoint.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The external IP address of this cluster's master endpoint.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enable<wbr>Private<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, the cluster's private
endpoint is used as the cluster endpoint and access through the public endpoint
is disabled. When `false`, either endpoint can be used. This field only applies
to private clusters, when `enable_private_nodes` is `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Private<wbr>Nodes</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enables the private cluster feature,
creating a private endpoint on the cluster. In a private cluster, nodes only
have RFC 1918 private addresses and communicate with the master's private
endpoint via private networking.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Ipv4Cidr<wbr>Block</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IP range in CIDR notation to use for
the hosted master network. This range will be used for assigning private IP
addresses to the cluster master(s) and the ILB VIP. This range must not overlap
with any other ranges in use within the cluster's network, and it must be a /28
subnet. See [Private Cluster Limitations](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#limitations)
for more details. This field only applies to private clusters, when
`enable_private_nodes` is `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>peering<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the peering between this cluster and the Google owned VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The internal IP address of this cluster's master endpoint.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The external IP address of this cluster's master endpoint.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Release<wbr>Channel</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterReleaseChannel">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterReleaseChannel">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterReleaseChannelArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterReleaseChannelOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The selected release channel.
Accepted values are:
* UNSPECIFIED: Not set.
* RAPID: Weekly upgrade cadence; Early testers and developers who requires new features.
* REGULAR: Multiple per month upgrade cadence; Production users who need features not yet offered in the Stable channel.
* STABLE: Every few months upgrade cadence; Production users who need stability above all else, and for whom frequent upgrades are too risky.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The selected release channel.
Accepted values are:
* UNSPECIFIED: Not set.
* RAPID: Weekly upgrade cadence; Early testers and developers who requires new features.
* REGULAR: Multiple per month upgrade cadence; Production users who need features not yet offered in the Stable channel.
* STABLE: Every few months upgrade cadence; Production users who need stability above all else, and for whom frequent upgrades are too risky.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The selected release channel.
Accepted values are:
* UNSPECIFIED: Not set.
* RAPID: Weekly upgrade cadence; Early testers and developers who requires new features.
* REGULAR: Multiple per month upgrade cadence; Production users who need features not yet offered in the Stable channel.
* STABLE: Every few months upgrade cadence; Production users who need stability above all else, and for whom frequent upgrades are too risky.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>channel</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The selected release channel.
Accepted values are:
* UNSPECIFIED: Not set.
* RAPID: Weekly upgrade cadence; Early testers and developers who requires new features.
* REGULAR: Multiple per month upgrade cadence; Production users who need features not yet offered in the Stable channel.
* STABLE: Every few months upgrade cadence; Production users who need stability above all else, and for whom frequent upgrades are too risky.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterResourceUsageExportConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterResourceUsageExportConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterResourceUsageExportConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterResourceUsageExportConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Bigquery<wbr>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfigbigquerydestination">Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config<wbr>Bigquery<wbr>Destination<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Parameters for using BigQuery as the destination of resource usage export.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Network<wbr>Egress<wbr>Metering</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to enable network egress metering for this cluster. If enabled, a daemonset will be created
in the cluster to meter network egress traffic.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Bigquery<wbr>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfigbigquerydestination">Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config<wbr>Bigquery<wbr>Destination</a></span>
    </dt>
    <dd>{{% md %}}Parameters for using BigQuery as the destination of resource usage export.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Network<wbr>Egress<wbr>Metering</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable network egress metering for this cluster. If enabled, a daemonset will be created
in the cluster to meter network egress traffic.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>bigquery<wbr>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfigbigquerydestination">Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config<wbr>Bigquery<wbr>Destination</a></span>
    </dt>
    <dd>{{% md %}}Parameters for using BigQuery as the destination of resource usage export.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Network<wbr>Egress<wbr>Metering</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to enable network egress metering for this cluster. If enabled, a daemonset will be created
in the cluster to meter network egress traffic.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>bigquery<wbr>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#clusterresourceusageexportconfigbigquerydestination">Dict[Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config<wbr>Bigquery<wbr>Destination]</a></span>
    </dt>
    <dd>{{% md %}}Parameters for using BigQuery as the destination of resource usage export.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Network<wbr>Egress<wbr>Metering</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable network egress metering for this cluster. If enabled, a daemonset will be created
in the cluster to meter network egress traffic.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Resource<wbr>Usage<wbr>Export<wbr>Config<wbr>Bigquery<wbr>Destination</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterResourceUsageExportConfigBigqueryDestination">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterResourceUsageExportConfigBigqueryDestination">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterResourceUsageExportConfigBigqueryDestinationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterResourceUsageExportConfigBigqueryDestinationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dataset<wbr>Id</span>
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
        <span>Dataset<wbr>Id</span>
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
        <span>dataset<wbr>Id</span>
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
        <span>dataset_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Vertical<wbr>Pod<wbr>Autoscaling</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterVerticalPodAutoscaling">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterVerticalPodAutoscaling">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterVerticalPodAutoscalingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterVerticalPodAutoscalingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
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
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
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
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
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
    <dd>{{% md %}}Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cluster<wbr>Workload<wbr>Identity<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#ClusterWorkloadIdentityConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#ClusterWorkloadIdentityConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterWorkloadIdentityConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/container?tab=doc#ClusterWorkloadIdentityConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Identity<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Currently, the only supported identity namespace is the project's default.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Identity<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Currently, the only supported identity namespace is the project's default.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>identity<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Currently, the only supported identity namespace is the project's default.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>identity<wbr>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Currently, the only supported identity namespace is the project's default.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
