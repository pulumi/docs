---
title: Module container
title_tag: Module container | Package pulumi_gcp | Python SDK
linktitle: container
notitle: true
---

<div class="section" id="container">
<h1>container<a class="headerlink" href="#container" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.container"></span><dl class="class">
<dt id="pulumi_gcp.container.AwaitableGetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">AwaitableGetClusterResult</code><span class="sig-paren">(</span><em class="sig-param">additional_zones=None</em>, <em class="sig-param">addons_configs=None</em>, <em class="sig-param">authenticator_groups_configs=None</em>, <em class="sig-param">cluster_autoscalings=None</em>, <em class="sig-param">cluster_ipv4_cidr=None</em>, <em class="sig-param">database_encryptions=None</em>, <em class="sig-param">default_max_pods_per_node=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_binary_authorization=None</em>, <em class="sig-param">enable_intranode_visibility=None</em>, <em class="sig-param">enable_kubernetes_alpha=None</em>, <em class="sig-param">enable_legacy_abac=None</em>, <em class="sig-param">enable_shielded_nodes=None</em>, <em class="sig-param">enable_tpu=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">initial_node_count=None</em>, <em class="sig-param">instance_group_urls=None</em>, <em class="sig-param">ip_allocation_policies=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">logging_service=None</em>, <em class="sig-param">maintenance_policies=None</em>, <em class="sig-param">master_auths=None</em>, <em class="sig-param">master_authorized_networks_configs=None</em>, <em class="sig-param">master_version=None</em>, <em class="sig-param">min_master_version=None</em>, <em class="sig-param">monitoring_service=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">network_policies=None</em>, <em class="sig-param">node_configs=None</em>, <em class="sig-param">node_locations=None</em>, <em class="sig-param">node_pools=None</em>, <em class="sig-param">node_version=None</em>, <em class="sig-param">operation=None</em>, <em class="sig-param">pod_security_policy_configs=None</em>, <em class="sig-param">private_cluster_configs=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">release_channels=None</em>, <em class="sig-param">remove_default_node_pool=None</em>, <em class="sig-param">resource_labels=None</em>, <em class="sig-param">resource_usage_export_configs=None</em>, <em class="sig-param">services_ipv4_cidr=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">tpu_ipv4_cidr_block=None</em>, <em class="sig-param">vertical_pod_autoscalings=None</em>, <em class="sig-param">workload_identity_configs=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.AwaitableGetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.AwaitableGetEngineVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">AwaitableGetEngineVersionsResult</code><span class="sig-paren">(</span><em class="sig-param">default_cluster_version=None</em>, <em class="sig-param">latest_master_version=None</em>, <em class="sig-param">latest_node_version=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">valid_master_versions=None</em>, <em class="sig-param">valid_node_versions=None</em>, <em class="sig-param">version_prefix=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.AwaitableGetEngineVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.AwaitableGetRegistryImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">AwaitableGetRegistryImageResult</code><span class="sig-paren">(</span><em class="sig-param">digest=None</em>, <em class="sig-param">image_url=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tag=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.AwaitableGetRegistryImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.AwaitableGetRegistryRepositoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">AwaitableGetRegistryRepositoryResult</code><span class="sig-paren">(</span><em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">repository_url=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.AwaitableGetRegistryRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">addons_config=None</em>, <em class="sig-param">authenticator_groups_config=None</em>, <em class="sig-param">cluster_autoscaling=None</em>, <em class="sig-param">cluster_ipv4_cidr=None</em>, <em class="sig-param">database_encryption=None</em>, <em class="sig-param">default_max_pods_per_node=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_binary_authorization=None</em>, <em class="sig-param">enable_intranode_visibility=None</em>, <em class="sig-param">enable_kubernetes_alpha=None</em>, <em class="sig-param">enable_legacy_abac=None</em>, <em class="sig-param">enable_shielded_nodes=None</em>, <em class="sig-param">enable_tpu=None</em>, <em class="sig-param">initial_node_count=None</em>, <em class="sig-param">ip_allocation_policy=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">logging_service=None</em>, <em class="sig-param">maintenance_policy=None</em>, <em class="sig-param">master_auth=None</em>, <em class="sig-param">master_authorized_networks_config=None</em>, <em class="sig-param">min_master_version=None</em>, <em class="sig-param">monitoring_service=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">network_policy=None</em>, <em class="sig-param">node_config=None</em>, <em class="sig-param">node_locations=None</em>, <em class="sig-param">node_pools=None</em>, <em class="sig-param">node_version=None</em>, <em class="sig-param">pod_security_policy_config=None</em>, <em class="sig-param">private_cluster_config=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">release_channel=None</em>, <em class="sig-param">remove_default_node_pool=None</em>, <em class="sig-param">resource_labels=None</em>, <em class="sig-param">resource_usage_export_config=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">vertical_pod_autoscaling=None</em>, <em class="sig-param">workload_identity_config=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Google Kubernetes Engine (GKE) cluster. For more information see
<a class="reference external" href="https://cloud.google.com/container-engine/docs/clusters">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters">the API reference</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments and attributes, including basic auth username and
passwords as well as certificate outputs will be stored in the raw state as
plaintext. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>addons_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for addons supported by GKE.
Structure is documented below.</p></li>
<li><p><strong>authenticator_groups_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite">Google Groups for GKE</a> feature.
Structure is documented below.</p></li>
<li><p><strong>cluster_autoscaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>)
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster’s workload. See the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning">guide to using Node Auto-Provisioning</a>
for more details. Structure is documented below.</p>
</p></li>
<li><p><strong>cluster_ipv4_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. <code class="docutils literal notranslate"><span class="pre">10.96.0.0/14</span></code>). Leave blank to have one
automatically chosen or specify a <code class="docutils literal notranslate"><span class="pre">/14</span></code> block in <code class="docutils literal notranslate"><span class="pre">10.0.0.0/8</span></code>. This field will
only work for routes-based clusters, where <code class="docutils literal notranslate"><span class="pre">ip_allocation_policy</span></code> is not defined.</p></li>
<li><p><strong>database_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ).
Structure is documented below.</p></li>
<li><p><strong>default_max_pods_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default maximum number of pods
per node in this cluster. This doesn’t work on “routes-based” clusters, clusters
that don’t have IP Aliasing enabled. See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the cluster.</p></li>
<li><p><strong>enable_binary_authorization</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.</p></li>
<li><p><strong>enable_intranode_visibility</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>)
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.</p>
</p></li>
<li><p><strong>enable_kubernetes_alpha</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.</p></li>
<li><p><strong>enable_legacy_abac</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><strong>enable_shielded_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – ) Enable Shielded Nodes features on all nodes in this cluster.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_tpu</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>) Whether to enable Cloud TPU resources in this cluster.
See the <a class="reference external" href="https://cloud.google.com/tpu/docs/kubernetes-engine-setup">official documentation</a>.</p>
</p></li>
<li><p><strong>initial_node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of nodes to create in this
cluster’s default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> is not set. If you’re using
<code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code> objects with no default node pool, you’ll need to
set this to a value of at least <code class="docutils literal notranslate"><span class="pre">1</span></code>, alongside setting
<code class="docutils literal notranslate"><span class="pre">remove_default_node_pool</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>ip_allocation_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases">IP aliasing</a>,
making the cluster VPC-native instead of routes-based. Structure is documented
below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as <code class="docutils literal notranslate"><span class="pre">us-central1-a</span></code>), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as <code class="docutils literal notranslate"><span class="pre">us-west1</span></code>), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well</p></li>
<li><p><strong>logging_service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The logging service that the cluster should
write logs to. Available options include <code class="docutils literal notranslate"><span class="pre">logging.googleapis.com</span></code>(Legacy Stackdriver),
<code class="docutils literal notranslate"><span class="pre">logging.googleapis.com/kubernetes</span></code>(Stackdriver Kubernetes Engine Logging), and <code class="docutils literal notranslate"><span class="pre">none</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">logging.googleapis.com/kubernetes</span></code></p></li>
<li><p><strong>maintenance_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The maintenance policy to use for the cluster. Structure is
documented below.</p></li>
<li><p><strong>master_auth</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the <code class="docutils literal notranslate"><span class="pre">container.clusters.getCredentials</span></code> permission.
Structure is documented below.</p></li>
<li><p><strong>master_authorized_networks_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The desired configuration options
for master authorized networks. Omit the nested <code class="docutils literal notranslate"><span class="pre">cidr_blocks</span></code> attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).</p></li>
<li><p><strong>min_master_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version–use the read-only <code class="docutils literal notranslate"><span class="pre">master_version</span></code> field to obtain that.
If unset, the cluster’s version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions. If you intend to specify versions manually,
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version">the docs</a>
describe the various acceptable formats for this field.</p></li>
<li><p><strong>monitoring_service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
<code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com</span></code>(Legacy Stackdriver), <code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com/kubernetes</span></code>(Stackdriver Kubernetes Engine Monitoring), and <code class="docutils literal notranslate"><span class="pre">none</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com/kubernetes</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cluster, unique within the project and
location.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.</p></li>
<li><p><strong>network_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration options for the
<a class="reference external" href="https://kubernetes.io/docs/concepts/services-networking/networkpolicies/">NetworkPolicy</a>
feature. Structure is documented below.</p></li>
<li><p><strong>node_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
<code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code> or a <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> block; this configuration
manages the default node pool, which isn’t recommended to be used with
this provider. Structure is documented below.</p></li>
<li><p><strong>node_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of zones in which the cluster’s nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster’s zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster’s zone.</p></li>
<li><p><strong>node_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of node pools associated with this cluster.
See container.NodePool for schema.
<strong>Warning:</strong> node pools defined inside a cluster can’t be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say “these are the <em>only</em> node pools associated with this cluster”, use the
container.NodePool resource instead of this property.</p></li>
<li><p><strong>node_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Kubernetes version on the nodes. Must either be unset
or set to the same value as <code class="docutils literal notranslate"><span class="pre">min_master_version</span></code> on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it’s
recommended that you specify explicit versions as this provider will see spurious diffs
when fuzzy versions are used. See the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source’s
<code class="docutils literal notranslate"><span class="pre">version_prefix</span></code> field to approximate fuzzy versions.
To update nodes in other node pools, use the <code class="docutils literal notranslate"><span class="pre">version</span></code> attribute on the node pool.</p></li>
<li><p><strong>pod_security_policy_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ) Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies">PodSecurityPolicy</a> feature.
Structure is documented below.</p></li>
<li><p><strong>private_cluster_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters">private clusters</a>,
clusters with private nodes. Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>release_channel</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ) Configuration options for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels">Release channel</a>
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.</p></li>
<li><p><strong>remove_default_node_pool</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, deletes the default node
pool upon cluster creation. If you’re using <code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code>
resources with no default node pool, this should be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, alongside
setting <code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> to at least <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>resource_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The GCE resource labels (a map of key/value pairs) to be applied to the cluster.</p></li>
<li><p><strong>resource_usage_export_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ) Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering">ResourceUsageExportConfig</a> feature.
Structure is documented below.</p></li>
<li><p><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or self_link of the Google Compute Engine
subnetwork in which the cluster’s instances are launched.</p></li>
<li><p><strong>vertical_pod_autoscaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>)
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.</p>
</p></li>
<li><p><strong>workload_identity_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>)
Workload Identity allows Kubernetes service accounts to act as a user-managed
<a class="reference external" href="https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts">Google IAM Service Account</a>.
Structure is documented below.</p>
</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrunConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">horizontalPodAutoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpLoadBalancing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">istioConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">auth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPolicyConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>authenticator_groups_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>cluster_autoscaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoProvisioningDefaults</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLimits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>database_encryption</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ip_allocation_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clusterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>maintenance_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dailyMaintenanceWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurringWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">endTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>master_auth</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificateConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">issueClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCaCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>master_authorized_networks_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cidrBlocks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>network_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>node_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>node_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of nodes to create in this
cluster’s default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> is not set. If you’re using
<code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code> objects with no default node pool, you’ll need to
set this to a value of at least <code class="docutils literal notranslate"><span class="pre">1</span></code>, alongside setting
<code class="docutils literal notranslate"><span class="pre">remove_default_node_pool</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_group_urls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of instance group URLs which have been assigned
to the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">management</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoRepair</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_pods_per_node</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the cluster, unique within the project and
location.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
<code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code> or a <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> block; this configuration
manages the default node pool, which isn’t recommended to be used with
this provider. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_locations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of zones in which the cluster’s nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster’s zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster’s zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">upgrade_settings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>pod_security_policy_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>private_cluster_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peeringName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>release_channel</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">channel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>resource_usage_export_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bigqueryDestination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableNetworkEgressMetering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>vertical_pod_autoscaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>workload_identity_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityNamespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_cluster.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.addons_config">
<code class="sig-name descname">addons_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.addons_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for addons supported by GKE.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrunConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">horizontalPodAutoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpLoadBalancing</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">istioConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">auth</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPolicyConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.authenticator_groups_config">
<code class="sig-name descname">authenticator_groups_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.authenticator_groups_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite">Google Groups for GKE</a> feature.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.cluster_autoscaling">
<code class="sig-name descname">cluster_autoscaling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.cluster_autoscaling" title="Permalink to this definition">¶</a></dt>
<dd><p>)
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster’s workload. See the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning">guide to using Node Auto-Provisioning</a>
for more details. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoProvisioningDefaults</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLimits</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.cluster_ipv4_cidr">
<code class="sig-name descname">cluster_ipv4_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.cluster_ipv4_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. <code class="docutils literal notranslate"><span class="pre">10.96.0.0/14</span></code>). Leave blank to have one
automatically chosen or specify a <code class="docutils literal notranslate"><span class="pre">/14</span></code> block in <code class="docutils literal notranslate"><span class="pre">10.0.0.0/8</span></code>. This field will
only work for routes-based clusters, where <code class="docutils literal notranslate"><span class="pre">ip_allocation_policy</span></code> is not defined.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.database_encryption">
<code class="sig-name descname">database_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.database_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>).
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keyName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.default_max_pods_per_node">
<code class="sig-name descname">default_max_pods_per_node</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.default_max_pods_per_node" title="Permalink to this definition">¶</a></dt>
<dd><p>The default maximum number of pods
per node in this cluster. This doesn’t work on “routes-based” clusters, clusters
that don’t have IP Aliasing enabled. See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.enable_binary_authorization">
<code class="sig-name descname">enable_binary_authorization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_binary_authorization" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.enable_intranode_visibility">
<code class="sig-name descname">enable_intranode_visibility</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_intranode_visibility" title="Permalink to this definition">¶</a></dt>
<dd><p>)
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.enable_kubernetes_alpha">
<code class="sig-name descname">enable_kubernetes_alpha</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_kubernetes_alpha" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.enable_legacy_abac">
<code class="sig-name descname">enable_legacy_abac</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_legacy_abac" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.enable_shielded_nodes">
<code class="sig-name descname">enable_shielded_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_shielded_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>) Enable Shielded Nodes features on all nodes in this cluster.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.enable_tpu">
<code class="sig-name descname">enable_tpu</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_tpu" title="Permalink to this definition">¶</a></dt>
<dd><p>) Whether to enable Cloud TPU resources in this cluster.
See the <a class="reference external" href="https://cloud.google.com/tpu/docs/kubernetes-engine-setup">official documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of this cluster’s Kubernetes master.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.initial_node_count">
<code class="sig-name descname">initial_node_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.initial_node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of nodes to create in this
cluster’s default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> is not set. If you’re using
<code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code> objects with no default node pool, you’ll need to
set this to a value of at least <code class="docutils literal notranslate"><span class="pre">1</span></code>, alongside setting
<code class="docutils literal notranslate"><span class="pre">remove_default_node_pool</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.instance_group_urls">
<code class="sig-name descname">instance_group_urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.instance_group_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>List of instance group URLs which have been assigned
to the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.ip_allocation_policy">
<code class="sig-name descname">ip_allocation_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.ip_allocation_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases">IP aliasing</a>,
making the cluster VPC-native instead of routes-based. Structure is documented
below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clusterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as <code class="docutils literal notranslate"><span class="pre">us-central1-a</span></code>), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as <code class="docutils literal notranslate"><span class="pre">us-west1</span></code>), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.logging_service">
<code class="sig-name descname">logging_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.logging_service" title="Permalink to this definition">¶</a></dt>
<dd><p>The logging service that the cluster should
write logs to. Available options include <code class="docutils literal notranslate"><span class="pre">logging.googleapis.com</span></code>(Legacy Stackdriver),
<code class="docutils literal notranslate"><span class="pre">logging.googleapis.com/kubernetes</span></code>(Stackdriver Kubernetes Engine Logging), and <code class="docutils literal notranslate"><span class="pre">none</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">logging.googleapis.com/kubernetes</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.maintenance_policy">
<code class="sig-name descname">maintenance_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.maintenance_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The maintenance policy to use for the cluster. Structure is
documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dailyMaintenanceWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurringWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">endTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.master_auth">
<code class="sig-name descname">master_auth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.master_auth" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the <code class="docutils literal notranslate"><span class="pre">container.clusters.getCredentials</span></code> permission.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificateConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">issueClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCaCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.master_authorized_networks_config">
<code class="sig-name descname">master_authorized_networks_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.master_authorized_networks_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired configuration options
for master authorized networks. Omit the nested <code class="docutils literal notranslate"><span class="pre">cidr_blocks</span></code> attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cidrBlocks</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.master_version">
<code class="sig-name descname">master_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.master_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the master in the cluster. This may
be different than the <code class="docutils literal notranslate"><span class="pre">min_master_version</span></code> set in the config if the master
has been updated by GKE.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.min_master_version">
<code class="sig-name descname">min_master_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.min_master_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version–use the read-only <code class="docutils literal notranslate"><span class="pre">master_version</span></code> field to obtain that.
If unset, the cluster’s version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions. If you intend to specify versions manually,
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version">the docs</a>
describe the various acceptable formats for this field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.monitoring_service">
<code class="sig-name descname">monitoring_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.monitoring_service" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
<code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com</span></code>(Legacy Stackdriver), <code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com/kubernetes</span></code>(Stackdriver Kubernetes Engine Monitoring), and <code class="docutils literal notranslate"><span class="pre">none</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com/kubernetes</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the cluster, unique within the project and
location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.network">
<code class="sig-name descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.network" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.network_policy">
<code class="sig-name descname">network_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.network_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration options for the
<a class="reference external" href="https://kubernetes.io/docs/concepts/services-networking/networkpolicies/">NetworkPolicy</a>
feature. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.node_config">
<code class="sig-name descname">node_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.node_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
<code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code> or a <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> block; this configuration
manages the default node pool, which isn’t recommended to be used with
this provider. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.node_locations">
<code class="sig-name descname">node_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.node_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of zones in which the cluster’s nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster’s zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster’s zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.node_pools">
<code class="sig-name descname">node_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.node_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>List of node pools associated with this cluster.
See container.NodePool for schema.
<strong>Warning:</strong> node pools defined inside a cluster can’t be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say “these are the <em>only</em> node pools associated with this cluster”, use the
container.NodePool resource instead of this property.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of nodes to create in this
cluster’s default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> is not set. If you’re using
<code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code> objects with no default node pool, you’ll need to
set this to a value of at least <code class="docutils literal notranslate"><span class="pre">1</span></code>, alongside setting
<code class="docutils literal notranslate"><span class="pre">remove_default_node_pool</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_group_urls</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of instance group URLs which have been assigned
to the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">management</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoRepair</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_pods_per_node</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the cluster, unique within the project and
location.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_config</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
<code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code> or a <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> block; this configuration
manages the default node pool, which isn’t recommended to be used with
this provider. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_locations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The list of zones in which the cluster’s nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster’s zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster’s zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">upgrade_settings</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurge</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailable</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.node_version">
<code class="sig-name descname">node_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.node_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Kubernetes version on the nodes. Must either be unset
or set to the same value as <code class="docutils literal notranslate"><span class="pre">min_master_version</span></code> on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it’s
recommended that you specify explicit versions as this provider will see spurious diffs
when fuzzy versions are used. See the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source’s
<code class="docutils literal notranslate"><span class="pre">version_prefix</span></code> field to approximate fuzzy versions.
To update nodes in other node pools, use the <code class="docutils literal notranslate"><span class="pre">version</span></code> attribute on the node pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.pod_security_policy_config">
<code class="sig-name descname">pod_security_policy_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.pod_security_policy_config" title="Permalink to this definition">¶</a></dt>
<dd><p>) Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies">PodSecurityPolicy</a> feature.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.private_cluster_config">
<code class="sig-name descname">private_cluster_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.private_cluster_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters">private clusters</a>,
clusters with private nodes. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peeringName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.release_channel">
<code class="sig-name descname">release_channel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.release_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>) Configuration options for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels">Release channel</a>
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">channel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.remove_default_node_pool">
<code class="sig-name descname">remove_default_node_pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.remove_default_node_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, deletes the default node
pool upon cluster creation. If you’re using <code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code>
resources with no default node pool, this should be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, alongside
setting <code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> to at least <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.resource_labels">
<code class="sig-name descname">resource_labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.resource_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCE resource labels (a map of key/value pairs) to be applied to the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.resource_usage_export_config">
<code class="sig-name descname">resource_usage_export_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.resource_usage_export_config" title="Permalink to this definition">¶</a></dt>
<dd><p>) Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering">ResourceUsageExportConfig</a> feature.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bigqueryDestination</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableNetworkEgressMetering</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.services_ipv4_cidr">
<code class="sig-name descname">services_ipv4_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.services_ipv4_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address range of the Kubernetes services in this
cluster, in <a class="reference external" href="http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">CIDR</a>
notation (e.g. <code class="docutils literal notranslate"><span class="pre">1.2.3.4/29</span></code>). Service addresses are typically put in the last
<code class="docutils literal notranslate"><span class="pre">/16</span></code> from the container CIDR.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.subnetwork">
<code class="sig-name descname">subnetwork</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or self_link of the Google Compute Engine
subnetwork in which the cluster’s instances are launched.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.vertical_pod_autoscaling">
<code class="sig-name descname">vertical_pod_autoscaling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.vertical_pod_autoscaling" title="Permalink to this definition">¶</a></dt>
<dd><p>)
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.workload_identity_config">
<code class="sig-name descname">workload_identity_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.workload_identity_config" title="Permalink to this definition">¶</a></dt>
<dd><p>)
Workload Identity allows Kubernetes service accounts to act as a user-managed
<a class="reference external" href="https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts">Google IAM Service Account</a>.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityNamespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.container.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">addons_config=None</em>, <em class="sig-param">authenticator_groups_config=None</em>, <em class="sig-param">cluster_autoscaling=None</em>, <em class="sig-param">cluster_ipv4_cidr=None</em>, <em class="sig-param">database_encryption=None</em>, <em class="sig-param">default_max_pods_per_node=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_binary_authorization=None</em>, <em class="sig-param">enable_intranode_visibility=None</em>, <em class="sig-param">enable_kubernetes_alpha=None</em>, <em class="sig-param">enable_legacy_abac=None</em>, <em class="sig-param">enable_shielded_nodes=None</em>, <em class="sig-param">enable_tpu=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">initial_node_count=None</em>, <em class="sig-param">instance_group_urls=None</em>, <em class="sig-param">ip_allocation_policy=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">logging_service=None</em>, <em class="sig-param">maintenance_policy=None</em>, <em class="sig-param">master_auth=None</em>, <em class="sig-param">master_authorized_networks_config=None</em>, <em class="sig-param">master_version=None</em>, <em class="sig-param">min_master_version=None</em>, <em class="sig-param">monitoring_service=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">network_policy=None</em>, <em class="sig-param">node_config=None</em>, <em class="sig-param">node_locations=None</em>, <em class="sig-param">node_pools=None</em>, <em class="sig-param">node_version=None</em>, <em class="sig-param">operation=None</em>, <em class="sig-param">pod_security_policy_config=None</em>, <em class="sig-param">private_cluster_config=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">release_channel=None</em>, <em class="sig-param">remove_default_node_pool=None</em>, <em class="sig-param">resource_labels=None</em>, <em class="sig-param">resource_usage_export_config=None</em>, <em class="sig-param">services_ipv4_cidr=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">tpu_ipv4_cidr_block=None</em>, <em class="sig-param">vertical_pod_autoscaling=None</em>, <em class="sig-param">workload_identity_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>addons_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for addons supported by GKE.
Structure is documented below.</p></li>
<li><p><strong>authenticator_groups_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite">Google Groups for GKE</a> feature.
Structure is documented below.</p>
</p></li>
<li><p><strong>cluster_autoscaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>)
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster’s workload. See the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning">guide to using Node Auto-Provisioning</a>
for more details. Structure is documented below.</p>
</p></li>
<li><p><strong>cluster_ipv4_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. <code class="docutils literal notranslate"><span class="pre">10.96.0.0/14</span></code>). Leave blank to have one
automatically chosen or specify a <code class="docutils literal notranslate"><span class="pre">/14</span></code> block in <code class="docutils literal notranslate"><span class="pre">10.0.0.0/8</span></code>. This field will
only work for routes-based clusters, where <code class="docutils literal notranslate"><span class="pre">ip_allocation_policy</span></code> is not defined.</p></li>
<li><p><strong>database_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ).
Structure is documented below.</p></li>
<li><p><strong>default_max_pods_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The default maximum number of pods
per node in this cluster. This doesn’t work on “routes-based” clusters, clusters
that don’t have IP Aliasing enabled. See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the cluster.</p></li>
<li><p><strong>enable_binary_authorization</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.</p></li>
<li><p><strong>enable_intranode_visibility</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>)
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.</p>
</p></li>
<li><p><strong>enable_kubernetes_alpha</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.</p></li>
<li><p><strong>enable_legacy_abac</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><strong>enable_shielded_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – ) Enable Shielded Nodes features on all nodes in this cluster.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_tpu</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>) Whether to enable Cloud TPU resources in this cluster.
See the <a class="reference external" href="https://cloud.google.com/tpu/docs/kubernetes-engine-setup">official documentation</a>.</p>
</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of this cluster’s Kubernetes master.</p></li>
<li><p><strong>initial_node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of nodes to create in this
cluster’s default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> is not set. If you’re using
<code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code> objects with no default node pool, you’ll need to
set this to a value of at least <code class="docutils literal notranslate"><span class="pre">1</span></code>, alongside setting
<code class="docutils literal notranslate"><span class="pre">remove_default_node_pool</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>instance_group_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of instance group URLs which have been assigned
to the cluster.</p></li>
<li><p><strong>ip_allocation_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases">IP aliasing</a>,
making the cluster VPC-native instead of routes-based. Structure is documented
below.</p>
</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as <code class="docutils literal notranslate"><span class="pre">us-central1-a</span></code>), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as <code class="docutils literal notranslate"><span class="pre">us-west1</span></code>), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well</p></li>
<li><p><strong>logging_service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The logging service that the cluster should
write logs to. Available options include <code class="docutils literal notranslate"><span class="pre">logging.googleapis.com</span></code>(Legacy Stackdriver),
<code class="docutils literal notranslate"><span class="pre">logging.googleapis.com/kubernetes</span></code>(Stackdriver Kubernetes Engine Logging), and <code class="docutils literal notranslate"><span class="pre">none</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">logging.googleapis.com/kubernetes</span></code></p></li>
<li><p><strong>maintenance_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The maintenance policy to use for the cluster. Structure is
documented below.</p></li>
<li><p><strong>master_auth</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the <code class="docutils literal notranslate"><span class="pre">container.clusters.getCredentials</span></code> permission.
Structure is documented below.</p></li>
<li><p><strong>master_authorized_networks_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The desired configuration options
for master authorized networks. Omit the nested <code class="docutils literal notranslate"><span class="pre">cidr_blocks</span></code> attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).</p></li>
<li><p><strong>master_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current version of the master in the cluster. This may
be different than the <code class="docutils literal notranslate"><span class="pre">min_master_version</span></code> set in the config if the master
has been updated by GKE.</p></li>
<li><p><strong>min_master_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version–use the read-only <code class="docutils literal notranslate"><span class="pre">master_version</span></code> field to obtain that.
If unset, the cluster’s version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source useful - it indicates which versions
are available, and can be use to approximate fuzzy versions. If you intend to specify versions manually,
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version">the docs</a>
describe the various acceptable formats for this field.</p>
</p></li>
<li><p><strong>monitoring_service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
<code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com</span></code>(Legacy Stackdriver), <code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com/kubernetes</span></code>(Stackdriver Kubernetes Engine Monitoring), and <code class="docutils literal notranslate"><span class="pre">none</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com/kubernetes</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cluster, unique within the project and
location.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.</p></li>
<li><p><strong>network_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration options for the
<a class="reference external" href="https://kubernetes.io/docs/concepts/services-networking/networkpolicies/">NetworkPolicy</a>
feature. Structure is documented below.</p>
</p></li>
<li><p><strong>node_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
<code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code> or a <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> block; this configuration
manages the default node pool, which isn’t recommended to be used with
this provider. Structure is documented below.</p></li>
<li><p><strong>node_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of zones in which the cluster’s nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster’s zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster’s zone.</p></li>
<li><p><strong>node_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of node pools associated with this cluster.
See container.NodePool for schema.
<strong>Warning:</strong> node pools defined inside a cluster can’t be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say “these are the <em>only</em> node pools associated with this cluster”, use the
container.NodePool resource instead of this property.</p></li>
<li><p><strong>node_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Kubernetes version on the nodes. Must either be unset
or set to the same value as <code class="docutils literal notranslate"><span class="pre">min_master_version</span></code> on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it’s
recommended that you specify explicit versions as this provider will see spurious diffs
when fuzzy versions are used. See the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source’s
<code class="docutils literal notranslate"><span class="pre">version_prefix</span></code> field to approximate fuzzy versions.
To update nodes in other node pools, use the <code class="docutils literal notranslate"><span class="pre">version</span></code> attribute on the node pool.</p></li>
<li><p><strong>pod_security_policy_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies">PodSecurityPolicy</a> feature.
Structure is documented below.</p>
</p></li>
<li><p><strong>private_cluster_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration for <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters">private clusters</a>,
clusters with private nodes. Structure is documented below.</p>
</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>release_channel</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) Configuration options for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels">Release channel</a>
feature, which provide more control over automatic upgrades of your GKE clusters. Structure is documented below.</p>
</p></li>
<li><p><strong>remove_default_node_pool</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, deletes the default node
pool upon cluster creation. If you’re using <code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code>
resources with no default node pool, this should be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, alongside
setting <code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> to at least <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>resource_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The GCE resource labels (a map of key/value pairs) to be applied to the cluster.</p></li>
<li><p><strong>resource_usage_export_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering">ResourceUsageExportConfig</a> feature.
Structure is documented below.</p>
</p></li>
<li><p><strong>services_ipv4_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The IP address range of the Kubernetes services in this
cluster, in <a class="reference external" href="http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">CIDR</a>
notation (e.g. <code class="docutils literal notranslate"><span class="pre">1.2.3.4/29</span></code>). Service addresses are typically put in the last
<code class="docutils literal notranslate"><span class="pre">/16</span></code> from the container CIDR.</p>
</p></li>
<li><p><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or self_link of the Google Compute Engine
subnetwork in which the cluster’s instances are launched.</p></li>
<li><p><strong>vertical_pod_autoscaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>)
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.</p>
</p></li>
<li><p><strong>workload_identity_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>)
Workload Identity allows Kubernetes service accounts to act as a user-managed
<a class="reference external" href="https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts">Google IAM Service Account</a>.
Structure is documented below.</p>
</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrunConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">horizontalPodAutoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpLoadBalancing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">istioConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">auth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPolicyConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>authenticator_groups_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>cluster_autoscaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoProvisioningDefaults</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLimits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>database_encryption</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ip_allocation_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clusterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>maintenance_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dailyMaintenanceWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurringWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">endTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>master_auth</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificateConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">issueClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCaCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>master_authorized_networks_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cidrBlocks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>network_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>node_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>node_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of nodes to create in this
cluster’s default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> is not set. If you’re using
<code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code> objects with no default node pool, you’ll need to
set this to a value of at least <code class="docutils literal notranslate"><span class="pre">1</span></code>, alongside setting
<code class="docutils literal notranslate"><span class="pre">remove_default_node_pool</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_group_urls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of instance group URLs which have been assigned
to the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">management</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoRepair</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_pods_per_node</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the cluster, unique within the project and
location.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
<code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code> or a <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> block; this configuration
manages the default node pool, which isn’t recommended to be used with
this provider. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_locations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of zones in which the cluster’s nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster’s zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster’s zone.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">upgrade_settings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>pod_security_policy_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>private_cluster_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peeringName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>release_channel</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">channel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>resource_usage_export_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bigqueryDestination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableNetworkEgressMetering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>vertical_pod_autoscaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>workload_identity_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityNamespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_cluster.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.container.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.container.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.GetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">GetClusterResult</code><span class="sig-paren">(</span><em class="sig-param">additional_zones=None</em>, <em class="sig-param">addons_configs=None</em>, <em class="sig-param">authenticator_groups_configs=None</em>, <em class="sig-param">cluster_autoscalings=None</em>, <em class="sig-param">cluster_ipv4_cidr=None</em>, <em class="sig-param">database_encryptions=None</em>, <em class="sig-param">default_max_pods_per_node=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enable_binary_authorization=None</em>, <em class="sig-param">enable_intranode_visibility=None</em>, <em class="sig-param">enable_kubernetes_alpha=None</em>, <em class="sig-param">enable_legacy_abac=None</em>, <em class="sig-param">enable_shielded_nodes=None</em>, <em class="sig-param">enable_tpu=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">initial_node_count=None</em>, <em class="sig-param">instance_group_urls=None</em>, <em class="sig-param">ip_allocation_policies=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">logging_service=None</em>, <em class="sig-param">maintenance_policies=None</em>, <em class="sig-param">master_auths=None</em>, <em class="sig-param">master_authorized_networks_configs=None</em>, <em class="sig-param">master_version=None</em>, <em class="sig-param">min_master_version=None</em>, <em class="sig-param">monitoring_service=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">network_policies=None</em>, <em class="sig-param">node_configs=None</em>, <em class="sig-param">node_locations=None</em>, <em class="sig-param">node_pools=None</em>, <em class="sig-param">node_version=None</em>, <em class="sig-param">operation=None</em>, <em class="sig-param">pod_security_policy_configs=None</em>, <em class="sig-param">private_cluster_configs=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">release_channels=None</em>, <em class="sig-param">remove_default_node_pool=None</em>, <em class="sig-param">resource_labels=None</em>, <em class="sig-param">resource_usage_export_configs=None</em>, <em class="sig-param">services_ipv4_cidr=None</em>, <em class="sig-param">subnetwork=None</em>, <em class="sig-param">tpu_ipv4_cidr_block=None</em>, <em class="sig-param">vertical_pod_autoscalings=None</em>, <em class="sig-param">workload_identity_configs=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_gcp.container.GetClusterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.GetEngineVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">GetEngineVersionsResult</code><span class="sig-paren">(</span><em class="sig-param">default_cluster_version=None</em>, <em class="sig-param">latest_master_version=None</em>, <em class="sig-param">latest_node_version=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">valid_master_versions=None</em>, <em class="sig-param">valid_node_versions=None</em>, <em class="sig-param">version_prefix=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEngineVersions.</p>
<dl class="attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.default_cluster_version">
<code class="sig-name descname">default_cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.default_cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of Kubernetes the service deploys by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.latest_master_version">
<code class="sig-name descname">latest_master_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.latest_master_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version available in the given zone for use with master instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.latest_node_version">
<code class="sig-name descname">latest_node_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.latest_node_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version available in the given zone for use with node instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.valid_master_versions">
<code class="sig-name descname">valid_master_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.valid_master_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of versions available in the given zone for use with master instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.valid_node_versions">
<code class="sig-name descname">valid_node_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.valid_node_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of versions available in the given zone for use with node instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.GetRegistryImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">GetRegistryImageResult</code><span class="sig-paren">(</span><em class="sig-param">digest=None</em>, <em class="sig-param">image_url=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tag=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetRegistryImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistryImage.</p>
<dl class="attribute">
<dt id="pulumi_gcp.container.GetRegistryImageResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetRegistryImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.GetRegistryRepositoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">GetRegistryRepositoryResult</code><span class="sig-paren">(</span><em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">repository_url=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetRegistryRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistryRepository.</p>
<dl class="attribute">
<dt id="pulumi_gcp.container.GetRegistryRepositoryResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetRegistryRepositoryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.NodePool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">NodePool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autoscaling=None</em>, <em class="sig-param">cluster=None</em>, <em class="sig-param">initial_node_count=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">management=None</em>, <em class="sig-param">max_pods_per_node=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">node_config=None</em>, <em class="sig-param">node_count=None</em>, <em class="sig-param">node_locations=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">upgrade_settings=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.NodePool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a node pool in a Google Kubernetes Engine (GKE) cluster separately from
the cluster control plane. For more information see <a class="reference external" href="https://cloud.google.com/container-engine/docs/node-pools">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters.nodePools">the API reference</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autoscaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster to create the node pool for. Cluster must be present in <code class="docutils literal notranslate"><span class="pre">location</span></code> provided for zonal clusters.</p></li>
<li><p><strong>initial_node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location (region or zone) of the cluster.</p></li>
<li><p><strong>management</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.</p></li>
<li><p><strong>max_pods_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>) The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are “route-based” - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the node pool. If left blank, this provider will
auto-generate a unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>node_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The node configuration of the pool. See
container.Cluster for schema.</p></li>
<li><p><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside <code class="docutils literal notranslate"><span class="pre">autoscaling</span></code>.</p></li>
<li><p><strong>node_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>)
The list of zones in which the node pool’s nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster’s zone for zonal clusters. If unspecified, the cluster-level
<code class="docutils literal notranslate"><span class="pre">node_locations</span></code> will be used.</p>
</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Kubernetes version for the nodes in this pool. Note that if this field
and <code class="docutils literal notranslate"><span class="pre">auto_upgrade</span></code> are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it’s
recommended that you specify explicit versions as this provider will see spurious diffs
when fuzzy versions are used. See the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source’s
<code class="docutils literal notranslate"><span class="pre">version_prefix</span></code> field to approximate fuzzy versions.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>management</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoRepair</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>node_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>upgrade_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_node_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_node_pool.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.autoscaling">
<code class="sig-name descname">autoscaling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.autoscaling" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.cluster">
<code class="sig-name descname">cluster</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster to create the node pool for. Cluster must be present in <code class="docutils literal notranslate"><span class="pre">location</span></code> provided for zonal clusters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.initial_node_count">
<code class="sig-name descname">initial_node_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.initial_node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.instance_group_urls">
<code class="sig-name descname">instance_group_urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.instance_group_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource URLs of the managed instance groups associated with this node pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location (region or zone) of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.management">
<code class="sig-name descname">management</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.management" title="Permalink to this definition">¶</a></dt>
<dd><p>Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoRepair</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.max_pods_per_node">
<code class="sig-name descname">max_pods_per_node</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.max_pods_per_node" title="Permalink to this definition">¶</a></dt>
<dd><p>) The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are “route-based” - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the node pool. If left blank, this provider will
auto-generate a unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.node_config">
<code class="sig-name descname">node_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.node_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The node configuration of the pool. See
container.Cluster for schema.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.node_count">
<code class="sig-name descname">node_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside <code class="docutils literal notranslate"><span class="pre">autoscaling</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.node_locations">
<code class="sig-name descname">node_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.node_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>)
The list of zones in which the node pool’s nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster’s zone for zonal clusters. If unspecified, the cluster-level
<code class="docutils literal notranslate"><span class="pre">node_locations</span></code> will be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Kubernetes version for the nodes in this pool. Note that if this field
and <code class="docutils literal notranslate"><span class="pre">auto_upgrade</span></code> are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it’s
recommended that you specify explicit versions as this provider will see spurious diffs
when fuzzy versions are used. See the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source’s
<code class="docutils literal notranslate"><span class="pre">version_prefix</span></code> field to approximate fuzzy versions.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.container.NodePool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autoscaling=None</em>, <em class="sig-param">cluster=None</em>, <em class="sig-param">initial_node_count=None</em>, <em class="sig-param">instance_group_urls=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">management=None</em>, <em class="sig-param">max_pods_per_node=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">node_config=None</em>, <em class="sig-param">node_count=None</em>, <em class="sig-param">node_locations=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">upgrade_settings=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.NodePool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NodePool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autoscaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster to create the node pool for. Cluster must be present in <code class="docutils literal notranslate"><span class="pre">location</span></code> provided for zonal clusters.</p></li>
<li><p><strong>initial_node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.</p></li>
<li><p><strong>instance_group_urls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The resource URLs of the managed instance groups associated with this node pool.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location (region or zone) of the cluster.</p></li>
<li><p><strong>management</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.</p></li>
<li><p><strong>max_pods_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>) The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are “route-based” - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the node pool. If left blank, this provider will
auto-generate a unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>node_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The node configuration of the pool. See
container.Cluster for schema.</p></li>
<li><p><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside <code class="docutils literal notranslate"><span class="pre">autoscaling</span></code>.</p></li>
<li><p><strong>node_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>)
The list of zones in which the node pool’s nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster’s zone for zonal clusters. If unspecified, the cluster-level
<code class="docutils literal notranslate"><span class="pre">node_locations</span></code> will be used.</p>
</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Kubernetes version for the nodes in this pool. Note that if this field
and <code class="docutils literal notranslate"><span class="pre">auto_upgrade</span></code> are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it’s
recommended that you specify explicit versions as this provider will see spurious diffs
when fuzzy versions are used. See the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source’s
<code class="docutils literal notranslate"><span class="pre">version_prefix</span></code> field to approximate fuzzy versions.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>management</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoRepair</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>node_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>upgrade_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_node_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_node_pool.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.container.NodePool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.NodePool.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.container.NodePool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.NodePool.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>prop</strong> (<em>str</em>) – A property name.</p>
</dd>
<dt class="field-even">Returns</dt>
<dd class="field-even"><p>A potentially transformed property name.</p>
</dd>
<dt class="field-odd">Return type</dt>
<dd class="field-odd"><p>str</p>
</dd>
</dl>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.container.get_cluster">
<code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">get_cluster</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Get info about a GKE cluster from its name and location.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>location</strong> (<em>str</em>) – The location (zone or region) this cluster has been
created in. One of <code class="docutils literal notranslate"><span class="pre">location</span></code>, <code class="docutils literal notranslate"><span class="pre">region</span></code>, <code class="docutils literal notranslate"><span class="pre">zone</span></code>, or a provider-level <code class="docutils literal notranslate"><span class="pre">zone</span></code> must
be specified.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the cluster.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region this cluster has been created in. Deprecated
in favour of <code class="docutils literal notranslate"><span class="pre">location</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>str</em>) – The zone this cluster has been created in. Deprecated in
favour of <code class="docutils literal notranslate"><span class="pre">location</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_cluster.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.container.get_engine_versions">
<code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">get_engine_versions</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">version_prefix=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_engine_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>subcategory: “Kubernetes (Container) Engine”
layout: “google”
page_title: “Google: container.getEngineVersions”
sidebar_current: “docs-google-datasource-container-versions”
description: <a href="#id32"><span class="problematic" id="id33">|</span></a>-</p>
<blockquote>
<div><p>Provides lists of available Google Kubernetes Engine versions for masters and nodes.</p>
</div></blockquote>
<p>Provides access to available Google Kubernetes Engine versions in a zone or region for a given project.</p>
<blockquote>
<div><p>If you are using the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> datasource with a
regional cluster, ensure that you have provided a region as the <code class="docutils literal notranslate"><span class="pre">location</span></code> to
the datasource. A region can have a different set of supported versions than
its component zones, and not all zones in a region are guaranteed to
support the same version.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>location</strong> (<em>str</em>) – The location (region or zone) to list versions for.
Must exactly match the location the cluster will be deployed in, or listed
versions may not be available. If <code class="docutils literal notranslate"><span class="pre">location</span></code>, <code class="docutils literal notranslate"><span class="pre">region</span></code>, and <code class="docutils literal notranslate"><span class="pre">zone</span></code> are not
specified, the provider-level zone must be set and is used instead.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – ID of the project to list available cluster versions for. Should match the project the cluster will be deployed to.
Defaults to the project that the provider is authenticated with.</p></li>
<li><p><strong>version_prefix</strong> (<em>str</em>) – If provided, this provider will only return versions
that match the string prefix. For example, <code class="docutils literal notranslate"><span class="pre">1.11.</span></code> will match all <code class="docutils literal notranslate"><span class="pre">1.11</span></code> series
releases. Since this is just a string match, it’s recommended that you append a
<code class="docutils literal notranslate"><span class="pre">.</span></code> after minor versions to ensure that prefixes such as <code class="docutils literal notranslate"><span class="pre">1.1</span></code> don’t match
versions like <code class="docutils literal notranslate"><span class="pre">1.12.5-gke.10</span></code> accidentally. See <a class="reference external" href="https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#versioning_scheme">the docs on versioning schema</a>
for full details on how version strings are formatted.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_engine_versions.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_engine_versions.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.container.get_registry_image">
<code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">get_registry_image</code><span class="sig-paren">(</span><em class="sig-param">digest=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tag=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_registry_image" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source fetches the project name, and provides the appropriate URLs to use for container registry for this project.</p>
<p>The URLs are computed entirely offline - as long as the project exists, they will be valid, but this data source does not contact Google Container Registry (GCR) at any point.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_registry_image.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_registry_image.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.container.get_registry_repository">
<code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">get_registry_repository</code><span class="sig-paren">(</span><em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_registry_repository" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source fetches the project name, and provides the appropriate URLs to use for container registry for this project.</p>
<p>The URLs are computed entirely offline - as long as the project exists, they will be valid, but this data source does not contact Google Container Registry (GCR) at any point.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_registry_repository.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_registry_repository.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
