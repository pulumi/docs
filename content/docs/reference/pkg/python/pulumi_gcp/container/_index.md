---
---

<div class="section" id="module-pulumi_gcp.container">
<span id="container"></span><h1>container<a class="headerlink" href="#module-pulumi_gcp.container" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.container.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_gcp.container.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>additional_zones=None</em>, <em>addons_config=None</em>, <em>authenticator_groups_config=None</em>, <em>cluster_autoscaling=None</em>, <em>cluster_ipv4_cidr=None</em>, <em>database_encryption=None</em>, <em>default_max_pods_per_node=None</em>, <em>description=None</em>, <em>enable_binary_authorization=None</em>, <em>enable_intranode_visibility=None</em>, <em>enable_kubernetes_alpha=None</em>, <em>enable_legacy_abac=None</em>, <em>enable_tpu=None</em>, <em>initial_node_count=None</em>, <em>ip_allocation_policy=None</em>, <em>location=None</em>, <em>logging_service=None</em>, <em>maintenance_policy=None</em>, <em>master_auth=None</em>, <em>master_authorized_networks_config=None</em>, <em>min_master_version=None</em>, <em>monitoring_service=None</em>, <em>name=None</em>, <em>network=None</em>, <em>network_policy=None</em>, <em>node_config=None</em>, <em>node_locations=None</em>, <em>node_pools=None</em>, <em>node_version=None</em>, <em>pod_security_policy_config=None</em>, <em>private_cluster_config=None</em>, <em>project=None</em>, <em>region=None</em>, <em>remove_default_node_pool=None</em>, <em>resource_labels=None</em>, <em>resource_usage_export_config=None</em>, <em>subnetwork=None</em>, <em>vertical_pod_autoscaling=None</em>, <em>workload_identity_config=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Google Kubernetes Engine (GKE) cluster. For more information see
<a class="reference external" href="https://cloud.google.com/container-engine/docs/clusters">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters">the API reference</a>.</p>
<blockquote>
<div><strong>Note:</strong> All arguments and attributes, including basic auth username and
passwords as well as certificate outputs will be stored in the raw state as
plaintext. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>additional_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of zones in which the cluster’s nodes
should be located. These must be in the same region as the cluster zone for
zonal clusters, or in the region of a regional cluster. In a multi-zonal cluster,
the number of nodes specified in <code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> is created in
all specified zones as well as the primary zone. If specified for a regional
cluster, nodes will only be created in these zones. <code class="docutils literal notranslate"><span class="pre">additional_zones</span></code> has been
deprecated in favour of <code class="docutils literal notranslate"><span class="pre">node_locations</span></code>.</li>
<li><strong>addons_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for addons supported by GKE.
Structure is documented below.</li>
<li><strong>authenticator_groups_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ) Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite">Google Groups for GKE</a> feature.
Structure is documented below.</li>
<li><strong>cluster_autoscaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>)
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster’s workload. See the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning">guide to using Node Auto-Provisioning</a>
for more details. Structure is documented below.</p>
</li>
<li><strong>cluster_ipv4_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address range of the kubernetes pods in
this cluster. Default is an automatically assigned CIDR.</li>
<li><strong>database_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ).
Structure is documented below.</li>
<li><strong>default_max_pods_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ) The default maximum number of pods per node in this cluster.
Note that this does not work on node pools which are “route-based” - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the cluster.</li>
<li><strong>enable_binary_authorization</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – ) Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.</li>
<li><strong>enable_intranode_visibility</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>)
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.</p>
</li>
<li><strong>enable_kubernetes_alpha</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.</li>
<li><strong>enable_legacy_abac</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></li>
<li><strong>enable_tpu</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>) Whether to enable Cloud TPU resources in this cluster.
See the <a class="reference external" href="https://cloud.google.com/tpu/docs/kubernetes-engine-setup">official documentation</a>.</p>
</li>
<li><strong>initial_node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of nodes to create in this
cluster’s default node pool. Must be set if <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> is not set. If
you’re using <code class="docutils literal notranslate"><span class="pre">google_container_node_pool</span></code> objects with no default node pool,
you’ll need to set this to a value of at least <code class="docutils literal notranslate"><span class="pre">1</span></code>, alongside setting
<code class="docutils literal notranslate"><span class="pre">remove_default_node_pool</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>ip_allocation_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration for cluster IP allocation. As of now, only pre-allocated subnetworks (custom type with secondary ranges) are supported.
This will activate IP aliases. See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases">official documentation</a>
Structure is documented below. This field is marked to use <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">Attribute as Block</a>
in order to support explicit removal with <code class="docutils literal notranslate"><span class="pre">ip_allocation_policy</span> <span class="pre">=</span> <span class="pre">[]</span></code>.</p>
</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as <code class="docutils literal notranslate"><span class="pre">us-central1-a</span></code>), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as <code class="docutils literal notranslate"><span class="pre">us-west1</span></code>), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well.</li>
<li><strong>logging_service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The logging service that the cluster should
write logs to. Available options include <code class="docutils literal notranslate"><span class="pre">logging.googleapis.com</span></code>,
<code class="docutils literal notranslate"><span class="pre">logging.googleapis.com/kubernetes</span></code>, and <code class="docutils literal notranslate"><span class="pre">none</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">logging.googleapis.com</span></code></li>
<li><strong>maintenance_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The maintenance policy to use for the cluster. Structure is
documented below.</li>
<li><strong>master_auth</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the <code class="docutils literal notranslate"><span class="pre">container.clusters.getCredentials</span></code> permission.
Structure is documented below.</li>
<li><strong>master_authorized_networks_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The desired configuration options
for master authorized networks. Omit the nested <code class="docutils literal notranslate"><span class="pre">cidr_blocks</span></code> attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).</li>
<li><strong>monitoring_service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
<code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com</span></code>, <code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com/kubernetes</span></code>, and <code class="docutils literal notranslate"><span class="pre">none</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com</span></code></li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cluster, unique within the project and
location.</li>
<li><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.</li>
<li><strong>network_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration options for the
<a class="reference external" href="https://kubernetes.io/docs/concepts/services-networking/networkpolicies/">NetworkPolicy</a>
feature. Structure is documented below.</li>
<li><strong>node_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of zones in which the cluster’s nodes
should be located. These must be in the same region as the cluster zone for
zonal clusters, or in the region of a regional cluster. In a multi-zonal cluster,
the number of nodes specified in <code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> is created in
all specified zones as well as the primary zone. If specified for a regional
cluster, nodes will be created in only these zones.</li>
<li><strong>node_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of node pools associated with this cluster.
See google_container_node_pool for schema.
<strong>Warning:</strong> node pools defined inside a cluster can’t be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say “these are the <em>only</em> node pools associated with this cluster”, use the
google_container_node_pool resource instead of this property.</li>
<li><strong>pod_security_policy_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ) Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies">PodSecurityPolicy</a> feature.
Structure is documented below.</li>
<li><strong>private_cluster_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of options for creating
a private cluster. Structure is documented below.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>remove_default_node_pool</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, deletes the default node
pool upon cluster creation. If you’re using <code class="docutils literal notranslate"><span class="pre">google_container_node_pool</span></code>
resources with no default node pool, this should be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, alongside
setting <code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> to at least <code class="docutils literal notranslate"><span class="pre">1</span></code>.</li>
<li><strong>resource_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The GCE resource labels (a map of key/value pairs) to be applied to the cluster.</li>
<li><strong>resource_usage_export_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ) Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering">ResourceUsageExportConfig</a> feature.
Structure is documented below.</li>
<li><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or self_link of the Google Compute Engine subnetwork in
which the cluster’s instances are launched.</li>
<li><strong>vertical_pod_autoscaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>)
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.</p>
</li>
<li><strong>workload_identity_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>)
Workload Identity allows Kubernetes service accounts to act as a user-managed
<a class="reference external" href="https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts">Google IAM Service Account</a>.</p>
</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone that the cluster master and nodes
should be created in. If specified, this cluster will be a zonal cluster. <code class="docutils literal notranslate"><span class="pre">zone</span></code>
has been deprecated in favour of <code class="docutils literal notranslate"><span class="pre">location</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.additional_zones">
<code class="descname">additional_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.additional_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of zones in which the cluster’s nodes
should be located. These must be in the same region as the cluster zone for
zonal clusters, or in the region of a regional cluster. In a multi-zonal cluster,
the number of nodes specified in <code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> is created in
all specified zones as well as the primary zone. If specified for a regional
cluster, nodes will only be created in these zones. <code class="docutils literal notranslate"><span class="pre">additional_zones</span></code> has been
deprecated in favour of <code class="docutils literal notranslate"><span class="pre">node_locations</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.addons_config">
<code class="descname">addons_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.addons_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for addons supported by GKE.
Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.authenticator_groups_config">
<code class="descname">authenticator_groups_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.authenticator_groups_config" title="Permalink to this definition">¶</a></dt>
<dd><p>) Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite">Google Groups for GKE</a> feature.
Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.cluster_autoscaling">
<code class="descname">cluster_autoscaling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.cluster_autoscaling" title="Permalink to this definition">¶</a></dt>
<dd><p>)
Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster’s workload. See the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning">guide to using Node Auto-Provisioning</a>
for more details. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.cluster_ipv4_cidr">
<code class="descname">cluster_ipv4_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.cluster_ipv4_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address range of the kubernetes pods in
this cluster. Default is an automatically assigned CIDR.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.database_encryption">
<code class="descname">database_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.database_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>).
Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.default_max_pods_per_node">
<code class="descname">default_max_pods_per_node</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.default_max_pods_per_node" title="Permalink to this definition">¶</a></dt>
<dd><p>) The default maximum number of pods per node in this cluster.
Note that this does not work on node pools which are “route-based” - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.enable_binary_authorization">
<code class="descname">enable_binary_authorization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_binary_authorization" title="Permalink to this definition">¶</a></dt>
<dd><p>) Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.enable_intranode_visibility">
<code class="descname">enable_intranode_visibility</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_intranode_visibility" title="Permalink to this definition">¶</a></dt>
<dd><p>)
Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.enable_kubernetes_alpha">
<code class="descname">enable_kubernetes_alpha</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_kubernetes_alpha" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.enable_legacy_abac">
<code class="descname">enable_legacy_abac</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_legacy_abac" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.enable_tpu">
<code class="descname">enable_tpu</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_tpu" title="Permalink to this definition">¶</a></dt>
<dd><p>) Whether to enable Cloud TPU resources in this cluster.
See the <a class="reference external" href="https://cloud.google.com/tpu/docs/kubernetes-engine-setup">official documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of this cluster’s Kubernetes master.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.initial_node_count">
<code class="descname">initial_node_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.initial_node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of nodes to create in this
cluster’s default node pool. Must be set if <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> is not set. If
you’re using <code class="docutils literal notranslate"><span class="pre">google_container_node_pool</span></code> objects with no default node pool,
you’ll need to set this to a value of at least <code class="docutils literal notranslate"><span class="pre">1</span></code>, alongside setting
<code class="docutils literal notranslate"><span class="pre">remove_default_node_pool</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.instance_group_urls">
<code class="descname">instance_group_urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.instance_group_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>List of instance group URLs which have been assigned
to the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.ip_allocation_policy">
<code class="descname">ip_allocation_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.ip_allocation_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for cluster IP allocation. As of now, only pre-allocated subnetworks (custom type with secondary ranges) are supported.
This will activate IP aliases. See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases">official documentation</a>
Structure is documented below. This field is marked to use <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">Attribute as Block</a>
in order to support explicit removal with <code class="docutils literal notranslate"><span class="pre">ip_allocation_policy</span> <span class="pre">=</span> <span class="pre">[]</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as <code class="docutils literal notranslate"><span class="pre">us-central1-a</span></code>), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as <code class="docutils literal notranslate"><span class="pre">us-west1</span></code>), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.logging_service">
<code class="descname">logging_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.logging_service" title="Permalink to this definition">¶</a></dt>
<dd><p>The logging service that the cluster should
write logs to. Available options include <code class="docutils literal notranslate"><span class="pre">logging.googleapis.com</span></code>,
<code class="docutils literal notranslate"><span class="pre">logging.googleapis.com/kubernetes</span></code>, and <code class="docutils literal notranslate"><span class="pre">none</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">logging.googleapis.com</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.maintenance_policy">
<code class="descname">maintenance_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.maintenance_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The maintenance policy to use for the cluster. Structure is
documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.master_auth">
<code class="descname">master_auth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.master_auth" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the <code class="docutils literal notranslate"><span class="pre">container.clusters.getCredentials</span></code> permission.
Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.master_authorized_networks_config">
<code class="descname">master_authorized_networks_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.master_authorized_networks_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired configuration options
for master authorized networks. Omit the nested <code class="docutils literal notranslate"><span class="pre">cidr_blocks</span></code> attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.master_version">
<code class="descname">master_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.master_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the master in the cluster. This may
be different than the <code class="docutils literal notranslate"><span class="pre">min_master_version</span></code> set in the config if the master
has been updated by GKE.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.monitoring_service">
<code class="descname">monitoring_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.monitoring_service" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
<code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com</span></code>, <code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com/kubernetes</span></code>, and <code class="docutils literal notranslate"><span class="pre">none</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the cluster, unique within the project and
location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.network">
<code class="descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.network" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.network_policy">
<code class="descname">network_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.network_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration options for the
<a class="reference external" href="https://kubernetes.io/docs/concepts/services-networking/networkpolicies/">NetworkPolicy</a>
feature. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.node_locations">
<code class="descname">node_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.node_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of zones in which the cluster’s nodes
should be located. These must be in the same region as the cluster zone for
zonal clusters, or in the region of a regional cluster. In a multi-zonal cluster,
the number of nodes specified in <code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> is created in
all specified zones as well as the primary zone. If specified for a regional
cluster, nodes will be created in only these zones.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.node_pools">
<code class="descname">node_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.node_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>List of node pools associated with this cluster.
See google_container_node_pool for schema.
<strong>Warning:</strong> node pools defined inside a cluster can’t be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say “these are the <em>only</em> node pools associated with this cluster”, use the
google_container_node_pool resource instead of this property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.pod_security_policy_config">
<code class="descname">pod_security_policy_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.pod_security_policy_config" title="Permalink to this definition">¶</a></dt>
<dd><p>) Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies">PodSecurityPolicy</a> feature.
Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.private_cluster_config">
<code class="descname">private_cluster_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.private_cluster_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of options for creating
a private cluster. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.remove_default_node_pool">
<code class="descname">remove_default_node_pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.remove_default_node_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, deletes the default node
pool upon cluster creation. If you’re using <code class="docutils literal notranslate"><span class="pre">google_container_node_pool</span></code>
resources with no default node pool, this should be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, alongside
setting <code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> to at least <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.resource_labels">
<code class="descname">resource_labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.resource_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCE resource labels (a map of key/value pairs) to be applied to the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.resource_usage_export_config">
<code class="descname">resource_usage_export_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.resource_usage_export_config" title="Permalink to this definition">¶</a></dt>
<dd><p>) Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering">ResourceUsageExportConfig</a> feature.
Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.services_ipv4_cidr">
<code class="descname">services_ipv4_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.services_ipv4_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address range of the Kubernetes services in this
cluster, in <a class="reference external" href="http:en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">CIDR</a>
notation (e.g. <code class="docutils literal notranslate"><span class="pre">1.2.3.4/29</span></code>). Service addresses are typically put in the last
<code class="docutils literal notranslate"><span class="pre">/16</span></code> from the container CIDR.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.subnetwork">
<code class="descname">subnetwork</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or self_link of the Google Compute Engine subnetwork in
which the cluster’s instances are launched.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.vertical_pod_autoscaling">
<code class="descname">vertical_pod_autoscaling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.vertical_pod_autoscaling" title="Permalink to this definition">¶</a></dt>
<dd><p>)
Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.workload_identity_config">
<code class="descname">workload_identity_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.workload_identity_config" title="Permalink to this definition">¶</a></dt>
<dd><p>)
Workload Identity allows Kubernetes service accounts to act as a user-managed
<a class="reference external" href="https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts">Google IAM Service Account</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone that the cluster master and nodes
should be created in. If specified, this cluster will be a zonal cluster. <code class="docutils literal notranslate"><span class="pre">zone</span></code>
has been deprecated in favour of <code class="docutils literal notranslate"><span class="pre">location</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.container.Cluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.container.Cluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.GetClusterResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.container.</code><code class="descname">GetClusterResult</code><span class="sig-paren">(</span><em>additional_zones=None</em>, <em>addons_configs=None</em>, <em>authenticator_groups_configs=None</em>, <em>cluster_autoscalings=None</em>, <em>cluster_ipv4_cidr=None</em>, <em>database_encryptions=None</em>, <em>default_max_pods_per_node=None</em>, <em>description=None</em>, <em>enable_binary_authorization=None</em>, <em>enable_intranode_visibility=None</em>, <em>enable_kubernetes_alpha=None</em>, <em>enable_legacy_abac=None</em>, <em>enable_tpu=None</em>, <em>endpoint=None</em>, <em>initial_node_count=None</em>, <em>instance_group_urls=None</em>, <em>ip_allocation_policies=None</em>, <em>location=None</em>, <em>logging_service=None</em>, <em>maintenance_policies=None</em>, <em>master_auths=None</em>, <em>master_authorized_networks_configs=None</em>, <em>master_version=None</em>, <em>min_master_version=None</em>, <em>monitoring_service=None</em>, <em>name=None</em>, <em>network=None</em>, <em>network_policies=None</em>, <em>node_configs=None</em>, <em>node_locations=None</em>, <em>node_pools=None</em>, <em>node_version=None</em>, <em>pod_security_policy_configs=None</em>, <em>private_cluster_configs=None</em>, <em>project=None</em>, <em>region=None</em>, <em>remove_default_node_pool=None</em>, <em>resource_labels=None</em>, <em>resource_usage_export_configs=None</em>, <em>services_ipv4_cidr=None</em>, <em>subnetwork=None</em>, <em>tpu_ipv4_cidr_block=None</em>, <em>vertical_pod_autoscalings=None</em>, <em>workload_identity_configs=None</em>, <em>zone=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_gcp.container.GetClusterResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.GetEngineVersionsResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.container.</code><code class="descname">GetEngineVersionsResult</code><span class="sig-paren">(</span><em>default_cluster_version=None</em>, <em>latest_master_version=None</em>, <em>latest_node_version=None</em>, <em>location=None</em>, <em>project=None</em>, <em>region=None</em>, <em>valid_master_versions=None</em>, <em>valid_node_versions=None</em>, <em>version_prefix=None</em>, <em>zone=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEngineVersions.</p>
<dl class="attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.default_cluster_version">
<code class="descname">default_cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.default_cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of Kubernetes the service deploys by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.latest_master_version">
<code class="descname">latest_master_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.latest_master_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version available in the given zone for use with master instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.latest_node_version">
<code class="descname">latest_node_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.latest_node_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version available in the given zone for use with node instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.valid_master_versions">
<code class="descname">valid_master_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.valid_master_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of versions available in the given zone for use with master instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.valid_node_versions">
<code class="descname">valid_node_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.valid_node_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of versions available in the given zone for use with node instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.GetRegistryImageResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.container.</code><code class="descname">GetRegistryImageResult</code><span class="sig-paren">(</span><em>digest=None</em>, <em>image_url=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>tag=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetRegistryImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistryImage.</p>
<dl class="attribute">
<dt id="pulumi_gcp.container.GetRegistryImageResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetRegistryImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.GetRegistryRepositoryResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.container.</code><code class="descname">GetRegistryRepositoryResult</code><span class="sig-paren">(</span><em>project=None</em>, <em>region=None</em>, <em>repository_url=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetRegistryRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistryRepository.</p>
<dl class="attribute">
<dt id="pulumi_gcp.container.GetRegistryRepositoryResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetRegistryRepositoryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.NodePool">
<em class="property">class </em><code class="descclassname">pulumi_gcp.container.</code><code class="descname">NodePool</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>autoscaling=None</em>, <em>cluster=None</em>, <em>initial_node_count=None</em>, <em>location=None</em>, <em>management=None</em>, <em>max_pods_per_node=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>node_config=None</em>, <em>node_count=None</em>, <em>project=None</em>, <em>region=None</em>, <em>version=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.NodePool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a node pool in a Google Kubernetes Engine (GKE) cluster separately from
the cluster control plane. For more information see <a class="reference external" href="https://cloud.google.com/container-engine/docs/node-pools">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters.nodePools">the API reference</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>autoscaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.</li>
<li><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster to create the node pool for.  Cluster must be present in <code class="docutils literal notranslate"><span class="pre">zone</span></code> provided for zonal clusters.</li>
<li><strong>initial_node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The initial node count for the pool. Changing this will force
recreation of the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location (region or zone) in which the cluster
resides.</li>
<li><strong>management</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.</li>
<li><strong>max_pods_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>) The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are “route-based” - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p>
</li>
<li><strong>node_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The node configuration of the pool. See
google_container_cluster for schema.</li>
<li><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside <code class="docutils literal notranslate"><span class="pre">autoscaling</span></code>.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the cluster resides (for
regional clusters). <code class="docutils literal notranslate"><span class="pre">zone</span></code> has been deprecated in favor of <code class="docutils literal notranslate"><span class="pre">location</span></code>.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone in which the cluster resides. <code class="docutils literal notranslate"><span class="pre">zone</span></code>
has been deprecated in favor of <code class="docutils literal notranslate"><span class="pre">location</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_node_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/container_node_pool.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.autoscaling">
<code class="descname">autoscaling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.autoscaling" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.cluster">
<code class="descname">cluster</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster to create the node pool for.  Cluster must be present in <code class="docutils literal notranslate"><span class="pre">zone</span></code> provided for zonal clusters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.initial_node_count">
<code class="descname">initial_node_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.initial_node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The initial node count for the pool. Changing this will force
recreation of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location (region or zone) in which the cluster
resides.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.management">
<code class="descname">management</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.management" title="Permalink to this definition">¶</a></dt>
<dd><p>Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.max_pods_per_node">
<code class="descname">max_pods_per_node</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.max_pods_per_node" title="Permalink to this definition">¶</a></dt>
<dd><p>) The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are “route-based” - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.node_config">
<code class="descname">node_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.node_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The node configuration of the pool. See
google_container_cluster for schema.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.node_count">
<code class="descname">node_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside <code class="docutils literal notranslate"><span class="pre">autoscaling</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which the cluster resides (for
regional clusters). <code class="docutils literal notranslate"><span class="pre">zone</span></code> has been deprecated in favor of <code class="docutils literal notranslate"><span class="pre">location</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone in which the cluster resides. <code class="docutils literal notranslate"><span class="pre">zone</span></code>
has been deprecated in favor of <code class="docutils literal notranslate"><span class="pre">location</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.container.NodePool.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.NodePool.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.container.NodePool.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.NodePool.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.container.get_cluster">
<code class="descclassname">pulumi_gcp.container.</code><code class="descname">get_cluster</code><span class="sig-paren">(</span><em>location=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>zone=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Get info about a GKE cluster from its name and location.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_cluster.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.container.get_engine_versions">
<code class="descclassname">pulumi_gcp.container.</code><code class="descname">get_engine_versions</code><span class="sig-paren">(</span><em>location=None</em>, <em>project=None</em>, <em>region=None</em>, <em>version_prefix=None</em>, <em>zone=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_engine_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to available Google Kubernetes Engine versions in a zone or region for a given project.</p>
<blockquote>
<div><p>If you are using the <code class="docutils literal notranslate"><span class="pre">google_container_engine_versions</span></code> datasource with a
regional cluster, ensure that you have provided a region as the <code class="docutils literal notranslate"><span class="pre">location</span></code> to
the datasource. A region can have a different set of supported versions than
its component zones, and not all zones in a region are guaranteed to
support the same version.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_engine_versions.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_engine_versions.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.container.get_registry_image">
<code class="descclassname">pulumi_gcp.container.</code><code class="descname">get_registry_image</code><span class="sig-paren">(</span><em>digest=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>tag=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_registry_image" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source fetches the project name, and provides the appropriate URLs to use for container registry for this project.</p>
<p>The URLs are computed entirely offline - as long as the project exists, they will be valid, but this data source does not contact Google Container Registry (GCR) at any point.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_registry_image.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_registry_image.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.container.get_registry_repository">
<code class="descclassname">pulumi_gcp.container.</code><code class="descname">get_registry_repository</code><span class="sig-paren">(</span><em>project=None</em>, <em>region=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_registry_repository" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source fetches the project name, and provides the appropriate URLs to use for container registry for this project.</p>
<p>The URLs are computed entirely offline - as long as the project exists, they will be valid, but this data source does not contact Google Container Registry (GCR) at any point.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_registry_repository.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/container_registry_repository.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
