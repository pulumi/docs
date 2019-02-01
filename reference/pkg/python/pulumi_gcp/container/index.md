<div class="section" id="module-pulumi_gcp.container">
<span id="container"></span><h1>container<a class="headerlink" href="#module-pulumi_gcp.container" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.container.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_gcp.container.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>additional_zones=None</em>, <em>addons_config=None</em>, <em>cluster_ipv4_cidr=None</em>, <em>description=None</em>, <em>enable_binary_authorization=None</em>, <em>enable_kubernetes_alpha=None</em>, <em>enable_legacy_abac=None</em>, <em>enable_tpu=None</em>, <em>initial_node_count=None</em>, <em>ip_allocation_policy=None</em>, <em>logging_service=None</em>, <em>maintenance_policy=None</em>, <em>master_auth=None</em>, <em>master_authorized_networks_config=None</em>, <em>master_ipv4_cidr_block=None</em>, <em>min_master_version=None</em>, <em>monitoring_service=None</em>, <em>name=None</em>, <em>network=None</em>, <em>network_policy=None</em>, <em>node_config=None</em>, <em>node_pools=None</em>, <em>node_version=None</em>, <em>pod_security_policy_config=None</em>, <em>private_cluster=None</em>, <em>private_cluster_config=None</em>, <em>project=None</em>, <em>region=None</em>, <em>remove_default_node_pool=None</em>, <em>resource_labels=None</em>, <em>subnetwork=None</em>, <em>zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Google Kubernetes Engine (GKE) cluster. For more information see
[the official documentation](<a class="reference external" href="https://cloud.google.com/container-engine/docs/clusters">https://cloud.google.com/container-engine/docs/clusters</a>)
and
[API](<a class="reference external" href="https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters">https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters</a>).</p>
<p>&gt; <strong>Note:</strong> All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">https://www.terraform.io/docs/state/sensitive-data.html</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>additional_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of additional Google Compute Engine
locations in which the cluster’s nodes should be located. If additional zones are
configured, the number of nodes specified in <cite>initial_node_count</cite> is created in
all specified zones.</li>
<li><strong>addons_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for addons supported by GKE.
Structure is documented below.</li>
<li><strong>cluster_ipv4_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address range of the kubernetes pods in
this cluster. Default is an automatically assigned CIDR.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the cluster.</li>
<li><strong>enable_binary_authorization</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.</li>
<li><strong>enable_kubernetes_alpha</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.</li>
<li><strong>enable_legacy_abac</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to <cite>false</cite></li>
<li><strong>enable_tpu</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](<a class="reference external" href="https://cloud.google.com/tpu/docs/kubernetes-engine-setup">https://cloud.google.com/tpu/docs/kubernetes-engine-setup</a>).
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.</li>
<li><strong>initial_node_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of nodes to create in this
cluster (not including the Kubernetes master). Must be set if <cite>node_pool</cite> is not set.</li>
<li><strong>ip_allocation_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for cluster IP allocation. As of now, only pre-allocated subnetworks (custom type with secondary ranges) are supported.
This will activate IP aliases. See the [official documentation](<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases">https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases</a>)
Structure is documented below.</li>
<li><strong>logging_service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The logging service that the cluster should
write logs to. Available options include <cite>logging.googleapis.com</cite>,
<cite>logging.googleapis.com/kubernetes</cite> (beta), and <cite>none</cite>. Defaults to <cite>logging.googleapis.com</cite></li>
<li><strong>maintenance_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The maintenance policy to use for the cluster. Structure is
documented below.</li>
<li><strong>master_auth</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The authentication information for accessing the
Kubernetes master. Structure is documented below.</li>
<li><strong>master_authorized_networks_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The desired configuration options
for master authorized networks. Omit the nested <cite>cidr_blocks</cite> attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).</li>
<li><strong>master_ipv4_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a private
[RFC1918](<a class="reference external" href="https://tools.ietf.org/html/rfc1918">https://tools.ietf.org/html/rfc1918</a>) block for the master’s VPC. The master range must not overlap with any subnet in your cluster’s VPC.
The master and your cluster use VPC peering. Must be specified in CIDR notation and must be <cite>/28</cite> subnet.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.
This field is deprecated, use <cite>private_cluster_config.master_ipv4_cidr_block</cite> instead.</li>
<li><strong>min_master_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version–use the read-only <cite>master_version</cite> field to obtain that.
If unset, the cluster’s version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).</li>
<li><strong>monitoring_service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
<cite>monitoring.googleapis.com</cite>, <cite>monitoring.googleapis.com/kubernetes</cite> (beta) and <cite>none</cite>.
Defaults to <cite>monitoring.googleapis.com</cite></li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cluster, unique within the project and
zone.</li>
<li><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.</li>
<li><strong>network_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration options for the
[NetworkPolicy](<a class="reference external" href="https://kubernetes.io/docs/concepts/services-networking/networkpolicies/">https://kubernetes.io/docs/concepts/services-networking/networkpolicies/</a>)
feature. Structure is documented below.</li>
<li><strong>node_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Parameters used in creating the cluster’s nodes.
Structure is documented below.</li>
<li><strong>node_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of node pools associated with this cluster.
See google_container_node_pool for schema.
<strong>Warning:</strong> node pools defined inside a cluster can’t be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say “these are the _only_ node pools associated with this cluster”, use the
google_container_node_pool resource instead of this property.</li>
<li><strong>node_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Kubernetes version on the nodes. Must either be unset
or set to the same value as <cite>min_master_version</cite> on create. Defaults to the default
version set by GKE which is not necessarily the latest version.</li>
<li><strong>pod_security_policy_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for the
[PodSecurityPolicy](<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies">https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies</a>) feature.
Structure is documented below.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.</li>
<li><strong>private_cluster</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, a
[private cluster](<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters">https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters</a>) will be created, meaning
nodes do not get public IP addresses. It is mandatory to specify <cite>master_ipv4_cidr_block</cite> and
<cite>ip_allocation_policy</cite> with this option.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.
This field is deprecated, use <cite>private_cluster_config.enable_private_nodes</cite> instead.</li>
<li><strong>private_cluster_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of options for creating
a private cluster. Structure is documented below.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] region
:param pulumi.Input[bool] remove_default_node_pool: If true, deletes the default node pool upon cluster creation.
:param pulumi.Input[dict] resource_labels: The GCE resource labels (a map of key/value pairs) to be applied to the cluster.
:param pulumi.Input[str] subnetwork: The name or self_link of the Google Compute Engine subnetwork in</p>
<blockquote>
<div>which the cluster’s instances are launched.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone that the master and the number of nodes specified
in <cite>initial_node_count</cite> should be created in. Only one of <cite>zone</cite> and <cite>region</cite>
may be set. If neither zone nor region are set, the provider zone is used.</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.additional_zones">
<code class="descname">additional_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.additional_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of additional Google Compute Engine
locations in which the cluster’s nodes should be located. If additional zones are
configured, the number of nodes specified in <cite>initial_node_count</cite> is created in
all specified zones.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.addons_config">
<code class="descname">addons_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.addons_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for addons supported by GKE.
Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.cluster_ipv4_cidr">
<code class="descname">cluster_ipv4_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.cluster_ipv4_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address range of the kubernetes pods in
this cluster. Default is an automatically assigned CIDR.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.enable_binary_authorization">
<code class="descname">enable_binary_authorization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_binary_authorization" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.</p>
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
Defaults to <cite>false</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.enable_tpu">
<code class="descname">enable_tpu</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_tpu" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Cloud TPU resources in this cluster.
See the [official documentation](<a class="reference external" href="https://cloud.google.com/tpu/docs/kubernetes-engine-setup">https://cloud.google.com/tpu/docs/kubernetes-engine-setup</a>).
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.</p>
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
cluster (not including the Kubernetes master). Must be set if <cite>node_pool</cite> is not set.</p>
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
This will activate IP aliases. See the [official documentation](<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases">https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases</a>)
Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.logging_service">
<code class="descname">logging_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.logging_service" title="Permalink to this definition">¶</a></dt>
<dd><p>The logging service that the cluster should
write logs to. Available options include <cite>logging.googleapis.com</cite>,
<cite>logging.googleapis.com/kubernetes</cite> (beta), and <cite>none</cite>. Defaults to <cite>logging.googleapis.com</cite></p>
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
Kubernetes master. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.master_authorized_networks_config">
<code class="descname">master_authorized_networks_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.master_authorized_networks_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired configuration options
for master authorized networks. Omit the nested <cite>cidr_blocks</cite> attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.master_ipv4_cidr_block">
<code class="descname">master_ipv4_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.master_ipv4_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a private
[RFC1918](<a class="reference external" href="https://tools.ietf.org/html/rfc1918">https://tools.ietf.org/html/rfc1918</a>) block for the master’s VPC. The master range must not overlap with any subnet in your cluster’s VPC.
The master and your cluster use VPC peering. Must be specified in CIDR notation and must be <cite>/28</cite> subnet.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.
This field is deprecated, use <cite>private_cluster_config.master_ipv4_cidr_block</cite> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.master_version">
<code class="descname">master_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.master_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the master in the cluster. This may
be different than the <cite>min_master_version</cite> set in the config if the master
has been updated by GKE.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.min_master_version">
<code class="descname">min_master_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.min_master_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version–use the read-only <cite>master_version</cite> field to obtain that.
If unset, the cluster’s version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.monitoring_service">
<code class="descname">monitoring_service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.monitoring_service" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
<cite>monitoring.googleapis.com</cite>, <cite>monitoring.googleapis.com/kubernetes</cite> (beta) and <cite>none</cite>.
Defaults to <cite>monitoring.googleapis.com</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the cluster, unique within the project and
zone.</p>
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
[NetworkPolicy](<a class="reference external" href="https://kubernetes.io/docs/concepts/services-networking/networkpolicies/">https://kubernetes.io/docs/concepts/services-networking/networkpolicies/</a>)
feature. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.node_config">
<code class="descname">node_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.node_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters used in creating the cluster’s nodes.
Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.node_pools">
<code class="descname">node_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.node_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>List of node pools associated with this cluster.
See google_container_node_pool for schema.
<strong>Warning:</strong> node pools defined inside a cluster can’t be changed (or added/removed) after
cluster creation without deleting and recreating the entire cluster. Unless you absolutely need the ability
to say “these are the _only_ node pools associated with this cluster”, use the
google_container_node_pool resource instead of this property.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.node_version">
<code class="descname">node_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.node_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Kubernetes version on the nodes. Must either be unset
or set to the same value as <cite>min_master_version</cite> on create. Defaults to the default
version set by GKE which is not necessarily the latest version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.pod_security_policy_config">
<code class="descname">pod_security_policy_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.pod_security_policy_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the
[PodSecurityPolicy](<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies">https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies</a>) feature.
Structure is documented below.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.private_cluster">
<code class="descname">private_cluster</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.private_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, a
[private cluster](<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters">https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters</a>) will be created, meaning
nodes do not get public IP addresses. It is mandatory to specify <cite>master_ipv4_cidr_block</cite> and
<cite>ip_allocation_policy</cite> with this option.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.
This field is deprecated, use <cite>private_cluster_config.enable_private_nodes</cite> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.private_cluster_config">
<code class="descname">private_cluster_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.private_cluster_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of options for creating
a private cluster. Structure is documented below.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.</p>
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
<dd><p>If true, deletes the default node pool upon cluster creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.resource_labels">
<code class="descname">resource_labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.resource_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCE resource labels (a map of key/value pairs) to be applied to the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.subnetwork">
<code class="descname">subnetwork</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or self_link of the Google Compute Engine subnetwork in
which the cluster’s instances are launched.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.Cluster.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone that the master and the number of nodes specified
in <cite>initial_node_count</cite> should be created in. Only one of <cite>zone</cite> and <cite>region</cite>
may be set. If neither zone nor region are set, the provider zone is used.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_gcp.container.</code><code class="descname">GetClusterResult</code><span class="sig-paren">(</span><em>additional_zones=None</em>, <em>addons_configs=None</em>, <em>cluster_autoscalings=None</em>, <em>cluster_ipv4_cidr=None</em>, <em>description=None</em>, <em>enable_binary_authorization=None</em>, <em>enable_kubernetes_alpha=None</em>, <em>enable_legacy_abac=None</em>, <em>enable_tpu=None</em>, <em>endpoint=None</em>, <em>initial_node_count=None</em>, <em>instance_group_urls=None</em>, <em>ip_allocation_policies=None</em>, <em>logging_service=None</em>, <em>maintenance_policies=None</em>, <em>master_auths=None</em>, <em>master_authorized_networks_configs=None</em>, <em>master_ipv4_cidr_block=None</em>, <em>master_version=None</em>, <em>min_master_version=None</em>, <em>monitoring_service=None</em>, <em>network=None</em>, <em>network_policies=None</em>, <em>node_configs=None</em>, <em>node_pools=None</em>, <em>node_version=None</em>, <em>pod_security_policy_configs=None</em>, <em>private_cluster=None</em>, <em>private_cluster_configs=None</em>, <em>remove_default_node_pool=None</em>, <em>resource_labels=None</em>, <em>subnetwork=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_gcp.container.GetClusterResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.GetEngineVersionsResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.container.</code><code class="descname">GetEngineVersionsResult</code><span class="sig-paren">(</span><em>default_cluster_version=None</em>, <em>latest_master_version=None</em>, <em>latest_node_version=None</em>, <em>valid_master_versions=None</em>, <em>valid_node_versions=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="descclassname">pulumi_gcp.container.</code><code class="descname">GetRegistryImageResult</code><span class="sig-paren">(</span><em>image_url=None</em>, <em>project=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetRegistryImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistryImage.</p>
<dl class="attribute">
<dt id="pulumi_gcp.container.GetRegistryImageResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetRegistryImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.GetRegistryRepositoryResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.container.</code><code class="descname">GetRegistryRepositoryResult</code><span class="sig-paren">(</span><em>project=None</em>, <em>repository_url=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetRegistryRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistryRepository.</p>
<dl class="attribute">
<dt id="pulumi_gcp.container.GetRegistryRepositoryResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetRegistryRepositoryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.container.NodePool">
<em class="property">class </em><code class="descclassname">pulumi_gcp.container.</code><code class="descname">NodePool</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>autoscaling=None</em>, <em>cluster=None</em>, <em>initial_node_count=None</em>, <em>management=None</em>, <em>max_pods_per_node=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>node_config=None</em>, <em>node_count=None</em>, <em>project=None</em>, <em>region=None</em>, <em>version=None</em>, <em>zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.NodePool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Node Pool resource within GKE. For more information see
[the official documentation](<a class="reference external" href="https://cloud.google.com/container-engine/docs/node-pools">https://cloud.google.com/container-engine/docs/node-pools</a>)
and
[API](<a class="reference external" href="https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters.nodePools">https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters.nodePools</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>autoscaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.</li>
<li><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster to create the node pool for.  Cluster must be present in <cite>zone</cite> provided for zonal clusters.</li>
<li><strong>initial_node_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The initial node count for the pool. Changing this will force
recreation of the resource.</li>
<li><strong>management</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.</li>
<li><strong>max_pods_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are “route-based” - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the node pool. If left blank, Terraform will
auto-generate a unique name.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with <cite>name</cite>.</li>
<li><strong>node_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The node configuration of the pool. See
google_container_cluster for schema.</li>
<li><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside <cite>autoscaling</cite>.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the cluster resides (for regional clusters).
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Kubernetes version for the nodes in this pool. Note that if this field
and <cite>auto_upgrade</cite> are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone in which the cluster resides.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.autoscaling">
<code class="descname">autoscaling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.autoscaling" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.cluster">
<code class="descname">cluster</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster to create the node pool for.  Cluster must be present in <cite>zone</cite> provided for zonal clusters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.initial_node_count">
<code class="descname">initial_node_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.initial_node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The initial node count for the pool. Changing this will force
recreation of the resource.</p>
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
<dd><p>The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are “route-based” - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the node pool. If left blank, Terraform will
auto-generate a unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with <cite>name</cite>.</p>
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
update the number of nodes per instance group but should not be used alongside <cite>autoscaling</cite>.</p>
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
<dd><p>The region in which the cluster resides (for regional clusters).
This property is in beta, and should be used with the terraform-provider-google-beta provider.
See [Provider Versions](<a class="reference external" href="https://terraform.io/docs/providers/google/provider_versions.html">https://terraform.io/docs/providers/google/provider_versions.html</a>) for more details on beta fields.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Kubernetes version for the nodes in this pool. Note that if this field
and <cite>auto_upgrade</cite> are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.container.NodePool.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone in which the cluster resides.</p>
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
<code class="descclassname">pulumi_gcp.container.</code><code class="descname">get_cluster</code><span class="sig-paren">(</span><em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Get info about a cluster within GKE from its name and zone.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.container.get_engine_versions">
<code class="descclassname">pulumi_gcp.container.</code><code class="descname">get_engine_versions</code><span class="sig-paren">(</span><em>project=None</em>, <em>region=None</em>, <em>zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_engine_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to available Google Container Engine versions in a zone or region for a given project.</p>
<p><a href="#id1"><span class="problematic" id="id2">``</span></a><a href="#id3"><span class="problematic" id="id4">`</span></a>hcl
data “google_container_engine_versions” “central1b” {</p>
<blockquote>
<div>zone = “us-central1-b”</div></blockquote>
<p>}</p>
<dl class="docutils">
<dt>resource “google_container_cluster” “foo” {</dt>
<dd><p class="first">name               = “terraform-test-cluster”
zone               = “us-central1-b”
node_version       = “${data.google_container_engine_versions.central1b.latest_node_version}”
initial_node_count = 1</p>
<dl class="docutils">
<dt>master_auth {</dt>
<dd>username = “mr.yoda”
password = “adoy.rm”</dd>
</dl>
<p class="last">}</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.container.get_registry_image">
<code class="descclassname">pulumi_gcp.container.</code><code class="descname">get_registry_image</code><span class="sig-paren">(</span><em>digest=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>tag=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_registry_image" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source fetches the project name, and provides the appropriate URLs to use for container registry for this project.</p>
<p>The URLs are computed entirely offline - as long as the project exists, they will be valid, but this data source does not contact Google Container Registry (GCR) at any point.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.container.get_registry_repository">
<code class="descclassname">pulumi_gcp.container.</code><code class="descname">get_registry_repository</code><span class="sig-paren">(</span><em>project=None</em>, <em>region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_registry_repository" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source fetches the project name, and provides the appropriate URLs to use for container registry for this project.</p>
<p>The URLs are computed entirely offline - as long as the project exists, they will be valid, but this data source does not contact Google Container Registry (GCR) at any point.</p>
</dd></dl>

</div>
