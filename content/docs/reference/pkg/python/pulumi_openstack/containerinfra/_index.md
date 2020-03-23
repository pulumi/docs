---
title: Module containerinfra
title_tag: Module containerinfra | Package pulumi_openstack | Python SDK
linktitle: containerinfra
notitle: true
---

<div class="section" id="containerinfra">
<h1>containerinfra<a class="headerlink" href="#containerinfra" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_openstack.containerinfra"></span><dl class="class">
<dt id="pulumi_openstack.containerinfra.AwaitableGetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.containerinfra.</code><code class="sig-name descname">AwaitableGetClusterResult</code><span class="sig-paren">(</span><em class="sig-param">api_address=None</em>, <em class="sig-param">cluster_template_id=None</em>, <em class="sig-param">coe_version=None</em>, <em class="sig-param">container_version=None</em>, <em class="sig-param">create_timeout=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">discovery_url=None</em>, <em class="sig-param">docker_volume_size=None</em>, <em class="sig-param">fixed_network=None</em>, <em class="sig-param">fixed_subnet=None</em>, <em class="sig-param">flavor=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">keypair=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">master_addresses=None</em>, <em class="sig-param">master_count=None</em>, <em class="sig-param">master_flavor=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">node_addresses=None</em>, <em class="sig-param">node_count=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">updated_at=None</em>, <em class="sig-param">user_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.containerinfra.AwaitableGetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.containerinfra.AwaitableGetClusterTemplateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.containerinfra.</code><code class="sig-name descname">AwaitableGetClusterTemplateResult</code><span class="sig-paren">(</span><em class="sig-param">apiserver_port=None</em>, <em class="sig-param">cluster_distro=None</em>, <em class="sig-param">coe=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">dns_nameserver=None</em>, <em class="sig-param">docker_storage_driver=None</em>, <em class="sig-param">docker_volume_size=None</em>, <em class="sig-param">external_network_id=None</em>, <em class="sig-param">fixed_network=None</em>, <em class="sig-param">fixed_subnet=None</em>, <em class="sig-param">flavor=None</em>, <em class="sig-param">floating_ip_enabled=None</em>, <em class="sig-param">http_proxy=None</em>, <em class="sig-param">https_proxy=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">image=None</em>, <em class="sig-param">insecure_registry=None</em>, <em class="sig-param">keypair_id=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">master_flavor=None</em>, <em class="sig-param">master_lb_enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_driver=None</em>, <em class="sig-param">no_proxy=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">public=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">registry_enabled=None</em>, <em class="sig-param">server_type=None</em>, <em class="sig-param">tls_disabled=None</em>, <em class="sig-param">updated_at=None</em>, <em class="sig-param">user_id=None</em>, <em class="sig-param">volume_driver=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.containerinfra.AwaitableGetClusterTemplateResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.containerinfra.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.containerinfra.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_template_id=None</em>, <em class="sig-param">create_timeout=None</em>, <em class="sig-param">discovery_url=None</em>, <em class="sig-param">docker_volume_size=None</em>, <em class="sig-param">fixed_network=None</em>, <em class="sig-param">fixed_subnet=None</em>, <em class="sig-param">flavor=None</em>, <em class="sig-param">keypair=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">master_count=None</em>, <em class="sig-param">master_flavor=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">node_count=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.containerinfra.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V1 Magnum cluster resource within OpenStack.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">region</span></code> - (Optional) The region in which to obtain the V1 Container Infra</dt><dd><p>client. A Container Infra client is needed to create a cluster. If omitted,
the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The name of the cluster. Changing this updates the name</dt><dd><p>of the existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">project_id</span></code> - (Optional) The project of the cluster. Required if admin wants</dt><dd><p>to create a cluster in another project. Changing this creates a new
cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">user_id</span></code> - (Optional) The user of the cluster. Required if admin wants to</dt><dd><p>create a cluster template for another user. Changing this creates a new
cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">cluster_template_id</span></code> - (Required) The UUID of the V1 Container Infra cluster</dt><dd><p>template. Changing this creates a new cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">create_timeout</span></code> - (Optional) The timeout (in minutes) for creating the</dt><dd><p>cluster. Changing this creates a new cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">discovery_url</span></code> - (Optional) The URL used for cluster node discovery.</dt><dd><p>Changing this creates a new cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">docker_volume_size</span></code> - (Optional) The size (in GB) of the Docker volume.</dt><dd><p>Changing this creates a new cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">flavor</span></code> - (Optional) The flavor for the nodes of the cluster. Can be set via</dt><dd><p>the <code class="docutils literal notranslate"><span class="pre">OS_MAGNUM_FLAVOR</span></code> environment variable. Changing this creates a new
cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">master_flavor</span></code> - (Optional) The flavor for the master nodes. Can be set via</dt><dd><p>the <code class="docutils literal notranslate"><span class="pre">OS_MAGNUM_MASTER_FLAVOR</span></code> environment variable. Changing this creates a
new cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">keypair</span></code> - (Optional) The name of the Compute service SSH keypair. Changing</dt><dd><p>this creates a new cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">labels</span></code> - (Optional) The list of key value pairs representing additional</dt><dd><p>properties of the cluster. Changing this creates a new cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">master_count</span></code> - (Optional) The number of master nodes for the cluster.</dt><dd><p>Changing this creates a new cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">node_count</span></code> - (Optional) The number of nodes for the cluster. Changing this</dt><dd><p>creates a new cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">fixed_network</span></code> - (Optional) The fixed network that will be attached to the</dt><dd><p>cluster. Changing this creates a new cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">fixed_subnet</span></code> - (Optional) The fixed subnet that will be attached to the</dt><dd><p>cluster. Changing this creates a new cluster.</p>
</dd>
</dl>
</li>
</ul>
<p>The following attributes are exported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">created_at</span></code> - The time at which cluster was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updated_at</span></code> - The time at which cluster was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">api_address</span></code> - COE API address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">coe_version</span></code> - COE software version.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_template_id</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">container_version</span></code> - Container software version.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create_timeout</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">discovery_url</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">docker_volume_size</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flavor</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_flavor</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keypair</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_count</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_count</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixed_network</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixed_subnet</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_addresses</span></code> - IP addresses of the master node of the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_addresses</span></code> - IP addresses of the node of the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stack_id</span></code> - UUID of the Orchestration service stack.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/containerinfra_cluster_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/containerinfra_cluster_v1.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_openstack.containerinfra.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_address=None</em>, <em class="sig-param">cluster_template_id=None</em>, <em class="sig-param">coe_version=None</em>, <em class="sig-param">container_version=None</em>, <em class="sig-param">create_timeout=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">discovery_url=None</em>, <em class="sig-param">docker_volume_size=None</em>, <em class="sig-param">fixed_network=None</em>, <em class="sig-param">fixed_subnet=None</em>, <em class="sig-param">flavor=None</em>, <em class="sig-param">keypair=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">master_addresses=None</em>, <em class="sig-param">master_count=None</em>, <em class="sig-param">master_flavor=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">node_addresses=None</em>, <em class="sig-param">node_count=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">updated_at=None</em>, <em class="sig-param">user_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.containerinfra.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.containerinfra.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.containerinfra.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.containerinfra.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.containerinfra.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.containerinfra.ClusterTemplate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.containerinfra.</code><code class="sig-name descname">ClusterTemplate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">apiserver_port=None</em>, <em class="sig-param">cluster_distro=None</em>, <em class="sig-param">coe=None</em>, <em class="sig-param">dns_nameserver=None</em>, <em class="sig-param">docker_storage_driver=None</em>, <em class="sig-param">docker_volume_size=None</em>, <em class="sig-param">external_network_id=None</em>, <em class="sig-param">fixed_network=None</em>, <em class="sig-param">fixed_subnet=None</em>, <em class="sig-param">flavor=None</em>, <em class="sig-param">floating_ip_enabled=None</em>, <em class="sig-param">http_proxy=None</em>, <em class="sig-param">https_proxy=None</em>, <em class="sig-param">image=None</em>, <em class="sig-param">insecure_registry=None</em>, <em class="sig-param">keypair_id=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">master_flavor=None</em>, <em class="sig-param">master_lb_enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_driver=None</em>, <em class="sig-param">no_proxy=None</em>, <em class="sig-param">public=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">registry_enabled=None</em>, <em class="sig-param">server_type=None</em>, <em class="sig-param">tls_disabled=None</em>, <em class="sig-param">volume_driver=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.containerinfra.ClusterTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V1 Magnum cluster template resource within OpenStack.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">region</span></code> - (Optional) The region in which to obtain the V1 Container Infra</dt><dd><p>client. A Container Infra client is needed to create a cluster template. If
omitted,the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates a new cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The name of the cluster template. Changing this updates</dt><dd><p>the name of the existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">project_id</span></code> - (Optional) The project of the cluster template. Required if</dt><dd><p>admin wants to create a cluster template in another project. Changing this
creates a new cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">user_id</span></code> - (Optional) The user of the cluster template. Required if admin</dt><dd><p>wants to create a cluster template for another user. Changing this creates
a new cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">apiserver_port</span></code> - (Optional) The API server port for the Container</dt><dd><p>Orchestration Engine for this cluster template. Changing this updates the
API server port of the existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">coe</span></code> - (Required) The Container Orchestration Engine for this cluster</dt><dd><p>template. Changing this updates the engine of the existing cluster
template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">cluster_distro</span></code> - (Optional) The distro for the cluster (fedora-atomic,</dt><dd><p>coreos, etc.). Changing this updates the cluster distro of the existing
cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">dns_nameserver</span></code> - (Optional) Address of the DNS nameserver that is used in</dt><dd><p>nodes of the cluster. Changing this updates the DNS nameserver of the
existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">docker_storage_driver</span></code> - (Optional) Docker storage driver. Changing this</dt><dd><p>updates the Docker storage driver of the existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">docker_volume_size</span></code> - (Optional) The size (in GB) of the Docker volume.</dt><dd><p>Changing this updates the Docker volume size of the existing cluster
template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">external_network_id</span></code> - (Optional) The ID of the external network that will</dt><dd><p>be used for the cluster. Changing this updates the external network ID of
the existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">fixed_network</span></code> - (Optional) The fixed network that will be attached to the</dt><dd><p>cluster. Changing this updates the fixed network of the existing cluster
template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">fixed_subnet</span></code> - (Optional) The fixed subnet that will be attached to the</dt><dd><p>cluster. Changing this updates the fixed subnet of the existing cluster
template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">flavor</span></code> - (Optional) The flavor for the nodes of the cluster. Can be set via</dt><dd><p>the <code class="docutils literal notranslate"><span class="pre">OS_MAGNUM_FLAVOR</span></code> environment variable. Changing this updates the
flavor of the existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">master_flavor</span></code> - (Optional) The flavor for the master nodes. Can be set via</dt><dd><p>the <code class="docutils literal notranslate"><span class="pre">OS_MAGNUM_MASTER_FLAVOR</span></code> environment variable. Changing this updates
the master flavor of the existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">floating_ip_enabled</span></code> - (Optional) Indicates whether created cluster should</dt><dd><p>create floating IP for every node or not. Changing this updates the
floating IP enabled attribute of the existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">http_proxy</span></code> - (Optional) The address of a proxy for receiving all HTTP</dt><dd><p>requests and relay them. Changing this updates the HTTP proxy address of
the existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">https_proxy</span></code> - (Optional) The address of a proxy for receiving all HTTPS</dt><dd><p>requests and relay them. Changing this updates the HTTPS proxy address of
the existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">image</span></code> - (Required) The reference to an image that is used for nodes of the</dt><dd><p>cluster. Can be set via the <code class="docutils literal notranslate"><span class="pre">OS_MAGNUM_IMAGE</span></code> environment variable.
Changing this updates the image attribute of the existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">insecure_registry</span></code> - (Optional) The insecure registry URL for the cluster</dt><dd><p>template. Changing this updates the insecure registry attribute of the
existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">keypair_id</span></code> - (Optional) The name of the Compute service SSH keypair.</dt><dd><p>Changing this updates the keypair of the existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">labels</span></code> - (Optional) The list of key value pairs representing additional</dt><dd><p>properties of the cluster template. Changing this updates the labels of the
existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">master_lb_enabled</span></code> - (Optional) Indicates whether created cluster should</dt><dd><p>has a loadbalancer for master nodes or not. Changing this updates the
attribute of the existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">network_driver</span></code> - (Optional) The name of the driver for the container</dt><dd><p>network. Changing this updates the network driver of the existing cluster
template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">no_proxy</span></code> - (Optional) A comma-separated list of IP addresses that shouldn’t</dt><dd><p>be used in the cluster. Changing this updates the no proxy list of the
existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">public</span></code> - (Optional) Indicates whether cluster template should be public.</dt><dd><p>Changing this updates the public attribute of the existing cluster
template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">registry_enabled</span></code> - (Optional) Indicates whether Docker registry is enabled</dt><dd><p>in the cluster. Changing this updates the registry enabled attribute of the
existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">server_type</span></code> - (Optional) The server type for the cluster template. Changing</dt><dd><p>this updates the server type of the existing cluster template.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">tls_disabled</span></code> - (Optional) Indicates whether the TLS should be disabled in</dt><dd><p>the cluster. Changing this updates the attribute of the existing cluster.</p>
</dd>
</dl>
</li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">volume_driver</span></code> - (Optional) The name of the driver that is used for the</dt><dd><p>volumes of the cluster nodes. Changing this updates the volume driver of
the existing cluster template.</p>
</dd>
</dl>
</li>
</ul>
<p>The following attributes are exported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">created_at</span></code> - The time at which cluster template was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updated_at</span></code> - The time at which cluster template was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apiserver_port</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">coe</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cluster_distro</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dns_nameserver</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">docker_storage_driver</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">docker_volume_size</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">external_network_id</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixed_network</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixed_subnet</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">flavor</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_flavor</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">floating_ip_enabled</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">http_proxy</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">https_proxy</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecure_registry</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keypair_id</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">links</span></code> - A list containing associated cluster template links.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_lb_enabled</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_driver</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">no_proxy</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">registry_enabled</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_type</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls_disabled</span></code> - See Argument Reference above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_driver</span></code> - See Argument Reference above.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/containerinfra_clustertemplate_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/containerinfra_clustertemplate_v1.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_openstack.containerinfra.ClusterTemplate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">apiserver_port=None</em>, <em class="sig-param">cluster_distro=None</em>, <em class="sig-param">coe=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">dns_nameserver=None</em>, <em class="sig-param">docker_storage_driver=None</em>, <em class="sig-param">docker_volume_size=None</em>, <em class="sig-param">external_network_id=None</em>, <em class="sig-param">fixed_network=None</em>, <em class="sig-param">fixed_subnet=None</em>, <em class="sig-param">flavor=None</em>, <em class="sig-param">floating_ip_enabled=None</em>, <em class="sig-param">http_proxy=None</em>, <em class="sig-param">https_proxy=None</em>, <em class="sig-param">image=None</em>, <em class="sig-param">insecure_registry=None</em>, <em class="sig-param">keypair_id=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">master_flavor=None</em>, <em class="sig-param">master_lb_enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_driver=None</em>, <em class="sig-param">no_proxy=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">public=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">registry_enabled=None</em>, <em class="sig-param">server_type=None</em>, <em class="sig-param">tls_disabled=None</em>, <em class="sig-param">updated_at=None</em>, <em class="sig-param">user_id=None</em>, <em class="sig-param">volume_driver=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.containerinfra.ClusterTemplate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClusterTemplate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.containerinfra.ClusterTemplate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.containerinfra.ClusterTemplate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.containerinfra.ClusterTemplate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.containerinfra.ClusterTemplate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.containerinfra.GetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.containerinfra.</code><code class="sig-name descname">GetClusterResult</code><span class="sig-paren">(</span><em class="sig-param">api_address=None</em>, <em class="sig-param">cluster_template_id=None</em>, <em class="sig-param">coe_version=None</em>, <em class="sig-param">container_version=None</em>, <em class="sig-param">create_timeout=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">discovery_url=None</em>, <em class="sig-param">docker_volume_size=None</em>, <em class="sig-param">fixed_network=None</em>, <em class="sig-param">fixed_subnet=None</em>, <em class="sig-param">flavor=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">keypair=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">master_addresses=None</em>, <em class="sig-param">master_count=None</em>, <em class="sig-param">master_flavor=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">node_addresses=None</em>, <em class="sig-param">node_count=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">stack_id=None</em>, <em class="sig-param">updated_at=None</em>, <em class="sig-param">user_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.api_address">
<code class="sig-name descname">api_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.api_address" title="Permalink to this definition">¶</a></dt>
<dd><p>COE API address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.cluster_template_id">
<code class="sig-name descname">cluster_template_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.cluster_template_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of the V1 Container Infra cluster template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.coe_version">
<code class="sig-name descname">coe_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.coe_version" title="Permalink to this definition">¶</a></dt>
<dd><p>COE software version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.create_timeout">
<code class="sig-name descname">create_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.create_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The timeout (in minutes) for creating the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which cluster was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.discovery_url">
<code class="sig-name descname">discovery_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.discovery_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL used for cluster node discovery.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.docker_volume_size">
<code class="sig-name descname">docker_volume_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.docker_volume_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size (in GB) of the Docker volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.fixed_network">
<code class="sig-name descname">fixed_network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.fixed_network" title="Permalink to this definition">¶</a></dt>
<dd><p>The fixed network that is attached to the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.fixed_subnet">
<code class="sig-name descname">fixed_subnet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.fixed_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>The fixed subnet that is attached to the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.flavor">
<code class="sig-name descname">flavor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.flavor" title="Permalink to this definition">¶</a></dt>
<dd><p>The flavor for the nodes of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.keypair">
<code class="sig-name descname">keypair</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.keypair" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Compute service SSH keypair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of key value pairs representing additional properties of
the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.master_addresses">
<code class="sig-name descname">master_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.master_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>IP addresses of the master node of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.master_count">
<code class="sig-name descname">master_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.master_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of master nodes for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.master_flavor">
<code class="sig-name descname">master_flavor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.master_flavor" title="Permalink to this definition">¶</a></dt>
<dd><p>The flavor for the master nodes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.node_addresses">
<code class="sig-name descname">node_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.node_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>IP addresses of the node of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.node_count">
<code class="sig-name descname">node_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of nodes for the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.stack_id">
<code class="sig-name descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>UUID of the Orchestration service stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which cluster was updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterResult.user_id">
<code class="sig-name descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterResult.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The user of the cluster.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.containerinfra.</code><code class="sig-name descname">GetClusterTemplateResult</code><span class="sig-paren">(</span><em class="sig-param">apiserver_port=None</em>, <em class="sig-param">cluster_distro=None</em>, <em class="sig-param">coe=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">dns_nameserver=None</em>, <em class="sig-param">docker_storage_driver=None</em>, <em class="sig-param">docker_volume_size=None</em>, <em class="sig-param">external_network_id=None</em>, <em class="sig-param">fixed_network=None</em>, <em class="sig-param">fixed_subnet=None</em>, <em class="sig-param">flavor=None</em>, <em class="sig-param">floating_ip_enabled=None</em>, <em class="sig-param">http_proxy=None</em>, <em class="sig-param">https_proxy=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">image=None</em>, <em class="sig-param">insecure_registry=None</em>, <em class="sig-param">keypair_id=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">master_flavor=None</em>, <em class="sig-param">master_lb_enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_driver=None</em>, <em class="sig-param">no_proxy=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">public=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">registry_enabled=None</em>, <em class="sig-param">server_type=None</em>, <em class="sig-param">tls_disabled=None</em>, <em class="sig-param">updated_at=None</em>, <em class="sig-param">user_id=None</em>, <em class="sig-param">volume_driver=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClusterTemplate.</p>
<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.apiserver_port">
<code class="sig-name descname">apiserver_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.apiserver_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The API server port for the Container Orchestration
Engine for this cluster template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.cluster_distro">
<code class="sig-name descname">cluster_distro</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.cluster_distro" title="Permalink to this definition">¶</a></dt>
<dd><p>The distro for the cluster (fedora-atomic, coreos, etc.).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.coe">
<code class="sig-name descname">coe</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.coe" title="Permalink to this definition">¶</a></dt>
<dd><p>The Container Orchestration Engine for this cluster template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which cluster template was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.dns_nameserver">
<code class="sig-name descname">dns_nameserver</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.dns_nameserver" title="Permalink to this definition">¶</a></dt>
<dd><p>Address of the DNS nameserver that is used in nodes of the
cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.docker_storage_driver">
<code class="sig-name descname">docker_storage_driver</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.docker_storage_driver" title="Permalink to this definition">¶</a></dt>
<dd><p>Docker storage driver. Changing this updates the
Docker storage driver of the existing cluster template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.docker_volume_size">
<code class="sig-name descname">docker_volume_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.docker_volume_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size (in GB) of the Docker volume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.external_network_id">
<code class="sig-name descname">external_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.external_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the external network that will be used for
the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.fixed_network">
<code class="sig-name descname">fixed_network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.fixed_network" title="Permalink to this definition">¶</a></dt>
<dd><p>The fixed network that will be attached to the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.fixed_subnet">
<code class="sig-name descname">fixed_subnet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.fixed_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>=The fixed subnet that will be attached to the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.flavor">
<code class="sig-name descname">flavor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.flavor" title="Permalink to this definition">¶</a></dt>
<dd><p>The flavor for the nodes of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.floating_ip_enabled">
<code class="sig-name descname">floating_ip_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.floating_ip_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether created cluster should create IP
floating IP for every node or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.http_proxy">
<code class="sig-name descname">http_proxy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.http_proxy" title="Permalink to this definition">¶</a></dt>
<dd><p>The address of a proxy for receiving all HTTP requests and
relay them.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.https_proxy">
<code class="sig-name descname">https_proxy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.https_proxy" title="Permalink to this definition">¶</a></dt>
<dd><p>The address of a proxy for receiving all HTTPS requests and
relay them.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.image">
<code class="sig-name descname">image</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.image" title="Permalink to this definition">¶</a></dt>
<dd><p>The reference to an image that is used for nodes of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.insecure_registry">
<code class="sig-name descname">insecure_registry</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.insecure_registry" title="Permalink to this definition">¶</a></dt>
<dd><p>The insecure registry URL for the cluster template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.keypair_id">
<code class="sig-name descname">keypair_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.keypair_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Compute service SSH keypair.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of key value pairs representing additional properties
of the cluster template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.master_flavor">
<code class="sig-name descname">master_flavor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.master_flavor" title="Permalink to this definition">¶</a></dt>
<dd><p>The flavor for the master nodes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.master_lb_enabled">
<code class="sig-name descname">master_lb_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.master_lb_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether created cluster should has a
loadbalancer for master nodes or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.network_driver">
<code class="sig-name descname">network_driver</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.network_driver" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the driver for the container network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.no_proxy">
<code class="sig-name descname">no_proxy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.no_proxy" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma-separated list of IP addresses that shouldn’t be used in
the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project of the cluster template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.public">
<code class="sig-name descname">public</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.public" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether cluster template should be public.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.registry_enabled">
<code class="sig-name descname">registry_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.registry_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Docker registry is enabled in the
cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.server_type">
<code class="sig-name descname">server_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.server_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The server type for the cluster template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.tls_disabled">
<code class="sig-name descname">tls_disabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.tls_disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the TLS should be disabled in the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which cluster template was updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.user_id">
<code class="sig-name descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The user of the cluster template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.containerinfra.GetClusterTemplateResult.volume_driver">
<code class="sig-name descname">volume_driver</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.containerinfra.GetClusterTemplateResult.volume_driver" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the driver that is used for the volumes of the
cluster nodes.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.containerinfra.get_cluster">
<code class="sig-prename descclassname">pulumi_openstack.containerinfra.</code><code class="sig-name descname">get_cluster</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.containerinfra.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack Magnum cluster.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/containerinfra_cluster_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/containerinfra_cluster_v1.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the cluster.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V1 Container Infra
client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.containerinfra.get_cluster_template">
<code class="sig-prename descclassname">pulumi_openstack.containerinfra.</code><code class="sig-name descname">get_cluster_template</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.containerinfra.get_cluster_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack Magnum cluster
template.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/containerinfra_clustertemplate_v1.html.markdown">https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/containerinfra_clustertemplate_v1.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the cluster template.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V1 Container Infra
client.
If omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
