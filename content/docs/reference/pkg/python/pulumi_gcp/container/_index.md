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
<span class="target" id="module-pulumi_gcp.container"></span><dl class="py class">
<dt id="pulumi_gcp.container.AwaitableGetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">AwaitableGetClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">additional_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authenticator_groups_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_autoscalings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_ipv4_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_encryptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_max_pods_per_node</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_binary_authorization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_intranode_visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_kubernetes_alpha</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_legacy_abac</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_shielded_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_tpu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_node_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_group_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_allocation_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label_fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_authorized_networks_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_auths</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_master_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_pools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pod_security_policy_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_cluster_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_channels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remove_default_node_pool</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_usage_export_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services_ipv4_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnetwork</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tpu_ipv4_cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vertical_pod_autoscalings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workload_identity_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.AwaitableGetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.container.AwaitableGetEngineVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">AwaitableGetEngineVersionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">default_cluster_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_master_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_node_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_channel_default_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">valid_master_versions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">valid_node_versions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_prefix</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.AwaitableGetEngineVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.container.AwaitableGetRegistryImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">AwaitableGetRegistryImageResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">digest</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.AwaitableGetRegistryImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.container.AwaitableGetRegistryRepositoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">AwaitableGetRegistryRepositoryResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.AwaitableGetRegistryRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.container.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authenticator_groups_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_autoscaling</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_ipv4_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_encryption</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_max_pods_per_node</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_binary_authorization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_intranode_visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_kubernetes_alpha</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_legacy_abac</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_shielded_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_tpu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_node_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_allocation_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_auth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_authorized_networks_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_master_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_pools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pod_security_policy_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_cluster_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_channel</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remove_default_node_pool</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_usage_export_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnetwork</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vertical_pod_autoscaling</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workload_identity_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Google Kubernetes Engine (GKE) cluster. For more information see
<a class="reference external" href="https://cloud.google.com/container-engine/docs/clusters">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters">the API reference</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments and attributes, including basic auth username and
passwords as well as certificate outputs will be stored in the raw state as
plaintext. <a class="reference external" href="https://www.pulumi.com/docs/intro/concepts/programming-model/#secrets">Read more about secrets in state</a>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">primary</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">container</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;primary&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;us-central1&quot;</span><span class="p">,</span>
    <span class="n">remove_default_node_pool</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">initial_node_count</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">master_auth</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;username&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span>
        <span class="s2">&quot;password&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span>
        <span class="s2">&quot;client_certificate_config&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;issueClientCertificate&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">})</span>
<span class="n">primary_preemptible_nodes</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">container</span><span class="o">.</span><span class="n">NodePool</span><span class="p">(</span><span class="s2">&quot;primaryPreemptibleNodes&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;us-central1&quot;</span><span class="p">,</span>
    <span class="n">cluster</span><span class="o">=</span><span class="n">primary</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">node_count</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">node_config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;preemptible&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;machine_type&quot;</span><span class="p">:</span> <span class="s2">&quot;n1-standard-1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;metadata&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;disable-legacy-endpoints&quot;</span><span class="p">:</span> <span class="s2">&quot;true&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;oauthScopes&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;https://www.googleapis.com/auth/logging.write&quot;</span><span class="p">,</span>
            <span class="s2">&quot;https://www.googleapis.com/auth/monitoring&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">primary</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">container</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;primary&quot;</span><span class="p">,</span>
    <span class="n">initial_node_count</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;us-central1-a&quot;</span><span class="p">,</span>
    <span class="n">master_auth</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;clientCertificateConfig&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;issueClientCertificate&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;password&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span>
        <span class="s2">&quot;username&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">node_config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;labels&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;metadata&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;disable-legacy-endpoints&quot;</span><span class="p">:</span> <span class="s2">&quot;true&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;oauthScopes&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;https://www.googleapis.com/auth/logging.write&quot;</span><span class="p">,</span>
            <span class="s2">&quot;https://www.googleapis.com/auth/monitoring&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="s2">&quot;tags&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;foo&quot;</span><span class="p">,</span>
            <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">})</span>
</pre></div>
</div>
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
<li><p><strong>cluster_autoscaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster’s workload. See the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning">guide to using Node Auto-Provisioning</a>
for more details. Structure is documented below.</p></li>
<li><p><strong>cluster_ipv4_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. <code class="docutils literal notranslate"><span class="pre">10.96.0.0/14</span></code>). Leave blank to have one
automatically chosen or specify a <code class="docutils literal notranslate"><span class="pre">/14</span></code> block in <code class="docutils literal notranslate"><span class="pre">10.0.0.0/8</span></code>. This field will
only work for routes-based clusters, where <code class="docutils literal notranslate"><span class="pre">ip_allocation_policy</span></code> is not defined.</p></li>
<li><p><strong>database_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>.
Structure is documented below.</p>
</p></li>
<li><p><strong>default_max_pods_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default maximum number of pods
per node in this cluster. This doesn’t work on “routes-based” clusters, clusters
that don’t have IP Aliasing enabled. See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the cluster.</p></li>
<li><p><strong>enable_binary_authorization</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.</p></li>
<li><p><strong>enable_intranode_visibility</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.</p></li>
<li><p><strong>enable_kubernetes_alpha</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.</p></li>
<li><p><strong>enable_legacy_abac</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><strong>enable_shielded_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Shielded Nodes features on all nodes in this cluster.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_tpu</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Whether to enable Cloud TPU resources in this cluster.
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
are available. If you intend to specify versions manually,
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
manages the default node pool, which isn’t recommended to be used.
Structure is documented below.</p></li>
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
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source’s
<code class="docutils literal notranslate"><span class="pre">version_prefix</span></code> field to approximate fuzzy versions.
To update nodes in other node pools, use the <code class="docutils literal notranslate"><span class="pre">version</span></code> attribute on the node pool.</p></li>
<li><p><strong>pod_security_policy_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies">PodSecurityPolicy</a> feature.
Structure is documented below.</p></li>
<li><p><strong>private_cluster_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters">private clusters</a>,
clusters with private nodes. Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>release_channel</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration options for the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels">Release channel</a>
feature, which provide more control over automatic upgrades of your GKE clusters.
When updating this field, GKE imposes specific version requirements. See
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels#migrating_between_release_channels">Migrating between release channels</a>
for more details; the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> datasource can provide
the default version for a channel. Note that removing the <code class="docutils literal notranslate"><span class="pre">release_channel</span></code>
field from your config will cause this provider to stop managing your cluster’s
release channel, but will not unenroll it. Instead, use the <code class="docutils literal notranslate"><span class="pre">&quot;UNSPECIFIED&quot;</span></code>
channel. Structure is documented below.</p></li>
<li><p><strong>remove_default_node_pool</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, deletes the default node
pool upon cluster creation. If you’re using <code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code>
resources with no default node pool, this should be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, alongside
setting <code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> to at least <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>resource_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The GCE resource labels (a map of key/value pairs) to be applied to the cluster.</p></li>
<li><p><strong>resource_usage_export_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering">ResourceUsageExportConfig</a> feature.
Structure is documented below.</p></li>
<li><p><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or self_link of the Google Compute Engine
subnetwork in which the cluster’s instances are launched.</p></li>
<li><p><strong>vertical_pod_autoscaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.</p></li>
<li><p><strong>workload_identity_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Workload Identity allows Kubernetes service accounts to act as a user-managed
<a class="reference external" href="https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts">Google IAM Service Account</a>.
Structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrunConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - .
The status of the CloudRun addon. It is disabled by default.
Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">configConnectorConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - .
The status of the ConfigConnector addon. It is disabled by default; Set <code class="docutils literal notranslate"><span class="pre">enabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsCacheConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - .
The status of the NodeLocal DNSCache addon. It is disabled by default.
Set <code class="docutils literal notranslate"><span class="pre">enabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">gcePersistentDiskCsiDriverConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - .
Whether this cluster should enable the Google Compute Engine Persistent Disk Container Storage Interface (CSI) Driver. Defaults to disabled; set <code class="docutils literal notranslate"><span class="pre">enabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">horizontalPodAutoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The status of the Horizontal Pod Autoscaling
addon, which increases or decreases the number of replica pods a replication controller
has based on the resource usage of the existing pods.
It ensures that a Heapster pod is running in the cluster, which is also used by the Cloud Monitoring service.
It is enabled by default;
set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to disable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpLoadBalancing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The status of the HTTP (L7) load balancing
controller addon, which makes it easy to set up HTTP load balancers for services in a
cluster. It is enabled by default; set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to disable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">istioConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - .
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">auth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authentication type between services in Istio. Available options include <code class="docutils literal notranslate"><span class="pre">AUTH_MUTUAL_TLS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kalmConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - .
Configuration for the KALM addon, which manages the lifecycle of k8s. It is disabled by default; Set <code class="docutils literal notranslate"><span class="pre">enabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPolicyConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Whether we should enable the network policy addon
for the master.  This must be enabled in order to enable network policy for the nodes.
To enable this, you must also define a <code class="docutils literal notranslate"><span class="pre">network_policy</span></code> block,
otherwise nothing will happen.
It can only be disabled if the nodes already do not have network policies enabled.
Defaults to disabled; set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
</ul>
<p>The <strong>authenticator_groups_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the RBAC security group for use with Google security groups in Kubernetes RBAC. Group name must be in format <code class="docutils literal notranslate"><span class="pre">gke-security-groups&#64;yourdomain.com</span></code>.</p></li>
</ul>
<p>The <strong>cluster_autoscaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoProvisioningDefaults</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Contains defaults for a node pool created by NAP.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code>. See the
<a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">official documentation</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of Google API scopes to be made available
on all of the node VMs under the “default” service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service account to be used by the Node VMs.
If not specified, the “default” service account is used.
In order to use the configured <code class="docutils literal notranslate"><span class="pre">oauth_scopes</span></code> for logging and monitoring, the service account being used needs the
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles">roles/logging.logWriter</a> and
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles">roles/monitoring.metricWriter</a> roles.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscalingProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ) Configuration
options for the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles">Autoscaling profile</a>
feature, which lets you choose whether the cluster autoscaler should optimize for resource utilization or resource availability
when deciding to remove nodes from a cluster. Can be <code class="docutils literal notranslate"><span class="pre">BALANCED</span></code> or <code class="docutils literal notranslate"><span class="pre">OPTIMIZE_UTILIZATION</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BALANCED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLimits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Global constraints for machine resources in the
cluster. Configuring the <code class="docutils literal notranslate"><span class="pre">cpu</span></code> and <code class="docutils literal notranslate"><span class="pre">memory</span></code> types is required if node
auto-provisioning is enabled. These limits will apply to node pool autoscaling
in addition to node auto-provisioning. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum amount of the resource in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Minimum amount of the resource in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the resource. For example, <code class="docutils literal notranslate"><span class="pre">cpu</span></code> and
<code class="docutils literal notranslate"><span class="pre">memory</span></code>.  See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning">guide to using Node Auto-Provisioning</a>
for a list of types.</p></li>
</ul>
</li>
</ul>
<p>The <strong>database_encryption</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - the key to use to encrypt/decrypt secrets.  See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#Cluster.DatabaseEncryption">DatabaseEncryption definition</a> for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <code class="docutils literal notranslate"><span class="pre">ENCRYPTED</span></code> or <code class="docutils literal notranslate"><span class="pre">DECRYPTED</span></code></p></li>
</ul>
<p>The <strong>ip_allocation_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clusterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address range for the cluster pod IPs.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the existing secondary
range in the cluster’s subnetwork to use for pod IP addresses. Alternatively,
<code class="docutils literal notranslate"><span class="pre">cluster_ipv4_cidr_block</span></code> can be used to automatically create a GKE-managed one.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address range of the services IPs in this cluster.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the existing
secondary range in the cluster’s subnetwork to use for service <code class="docutils literal notranslate"><span class="pre">ClusterIP</span></code>s.
Alternatively, <code class="docutils literal notranslate"><span class="pre">services_ipv4_cidr_block</span></code> can be used to automatically create a
GKE-managed one.</p></li>
</ul>
<p>The <strong>maintenance_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dailyMaintenanceWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Time window specified for daily maintenance operations.
Specify <code class="docutils literal notranslate"><span class="pre">start_time</span></code> in <a class="reference external" href="https://www.ietf.org/rfc/rfc3339.txt">RFC3339</a> format “HH:MM”,
where HH : [00-23] and MM : [00-59] GMT. For example:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurringWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Time window for
recurring maintenance operations.</p>
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
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificateConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Whether client certificate authorization is enabled for this cluster.  For example:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">issueClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCaCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password to use for HTTP basic authentication when accessing
the Kubernetes master endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username to use for HTTP basic authentication when accessing
the Kubernetes master endpoint. If not present basic auth will be disabled.</p></li>
</ul>
<p>The <strong>master_authorized_networks_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cidrBlocks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - External networks that can access the
Kubernetes cluster master through HTTPS.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cidr_block</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - External network that can access Kubernetes master through HTTPS.
Must be specified in CIDR notation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Field for users to identify CIDR blocks.</p></li>
</ul>
</li>
</ul>
<p>The <strong>network_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The selected network policy provider. Defaults to PROVIDER_UNSPECIFIED.</p></li>
</ul>
<p>The <strong>node_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskKmsKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: <a class="reference external" href="https://cloud.google.com/compute/docs/disks/customer-managed-encryption">https://cloud.google.com/compute/docs/disks/customer-managed-encryption</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the disk attached to each node
(e.g. ‘pd-standard’ or ‘pd-ssd’). If unspecified, the default disk type is ‘pd-standard’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of the type and count of accelerator cards attached to the instance.
Structure documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of the guest accelerator cards exposed to this instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The accelerator type resource to expose to this instance. E.g. <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-k80</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Kubernetes labels (key/value pairs) to be applied to each node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a Google Compute Engine machine type.
Defaults to <code class="docutils literal notranslate"><span class="pre">n1-standard-1</span></code>. To create a custom machine type, value should be set as specified
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instances#machineType">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The metadata key/value pairs assigned to instances in
the cluster. From GKE <code class="docutils literal notranslate"><span class="pre">1.12</span></code> onwards, <code class="docutils literal notranslate"><span class="pre">disable-legacy-endpoints</span></code> is set to
<code class="docutils literal notranslate"><span class="pre">true</span></code> by the API; if <code class="docutils literal notranslate"><span class="pre">metadata</span></code> is set but that default value is not
included, the provider will attempt to unset the value. To avoid this, set the
value in your config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code>. See the
<a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">official documentation</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of Google API scopes to be made available
on all of the node VMs under the “default” service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - A boolean that represents whether or not the underlying node VMs
are preemptible. See the <a class="reference external" href="https://cloud.google.com/container-engine/docs/preemptible-vm">official documentation</a>
for more information. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods">GKE Sandbox</a> configuration. When enabling this feature you must specify <code class="docutils literal notranslate"><span class="pre">image_type</span> <span class="pre">=</span> <span class="pre">&quot;COS_CONTAINERD&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">node_version</span> <span class="pre">=</span> <span class="pre">&quot;1.12.7-gke.17&quot;</span></code> or later to use it.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which sandbox to use for pods in the node pool.
Accepted values are:</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service account to be used by the Node VMs.
If not specified, the “default” service account is used.
In order to use the configured <code class="docutils literal notranslate"><span class="pre">oauth_scopes</span></code> for logging and monitoring, the service account being used needs the
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles">roles/logging.logWriter</a> and
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles">roles/monitoring.metricWriter</a> roles.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Shielded Instance options. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defines if the instance has integrity monitoring enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defines if the instance has Secure Boot enabled.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of <a class="reference external" href="https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/">Kubernetes taints</a>
to apply to nodes. GKE’s API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause the provider to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through <code class="docutils literal notranslate"><span class="pre">kubectl</span></code>), and it’s recommended that you do not use
this field to manage taints. If you do, <code class="docutils literal notranslate"><span class="pre">lifecycle.ignore_changes</span></code> is
recommended. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Effect for taint. Accepted values are <code class="docutils literal notranslate"><span class="pre">NO_SCHEDULE</span></code>, <code class="docutils literal notranslate"><span class="pre">PREFER_NO_SCHEDULE</span></code>, and <code class="docutils literal notranslate"><span class="pre">NO_EXECUTE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Key for taint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value for taint.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Metadata configuration to expose to workloads on the node pool.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How to expose the node metadata to the workload running on the node.
Accepted values are:</p>
<ul>
<li><p>UNSPECIFIED: Not Set</p></li>
<li><p>SECURE: Prevent workloads not in hostNetwork from accessing certain VM metadata, specifically kube-env, which contains Kubelet credentials, and the instance identity token. See <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy">Metadata Concealment</a> documentation.</p></li>
<li><p>EXPOSE: Expose all VM metadata to pods.</p></li>
<li><p>GKE_METADATA_SERVER: Enables <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity">workload identity</a> on the node.</p></li>
</ul>
</li>
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
manages the default node pool, which isn’t recommended to be used.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskKmsKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: <a class="reference external" href="https://cloud.google.com/compute/docs/disks/customer-managed-encryption">https://cloud.google.com/compute/docs/disks/customer-managed-encryption</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the disk attached to each node
(e.g. ‘pd-standard’ or ‘pd-ssd’). If unspecified, the default disk type is ‘pd-standard’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of the type and count of accelerator cards attached to the instance.
Structure documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of the guest accelerator cards exposed to this instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The accelerator type resource to expose to this instance. E.g. <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-k80</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Kubernetes labels (key/value pairs) to be applied to each node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a Google Compute Engine machine type.
Defaults to <code class="docutils literal notranslate"><span class="pre">n1-standard-1</span></code>. To create a custom machine type, value should be set as specified
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instances#machineType">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The metadata key/value pairs assigned to instances in
the cluster. From GKE <code class="docutils literal notranslate"><span class="pre">1.12</span></code> onwards, <code class="docutils literal notranslate"><span class="pre">disable-legacy-endpoints</span></code> is set to
<code class="docutils literal notranslate"><span class="pre">true</span></code> by the API; if <code class="docutils literal notranslate"><span class="pre">metadata</span></code> is set but that default value is not
included, the provider will attempt to unset the value. To avoid this, set the
value in your config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code>. See the
<a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">official documentation</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of Google API scopes to be made available
on all of the node VMs under the “default” service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - A boolean that represents whether or not the underlying node VMs
are preemptible. See the <a class="reference external" href="https://cloud.google.com/container-engine/docs/preemptible-vm">official documentation</a>
for more information. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods">GKE Sandbox</a> configuration. When enabling this feature you must specify <code class="docutils literal notranslate"><span class="pre">image_type</span> <span class="pre">=</span> <span class="pre">&quot;COS_CONTAINERD&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">node_version</span> <span class="pre">=</span> <span class="pre">&quot;1.12.7-gke.17&quot;</span></code> or later to use it.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which sandbox to use for pods in the node pool.
Accepted values are:</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service account to be used by the Node VMs.
If not specified, the “default” service account is used.
In order to use the configured <code class="docutils literal notranslate"><span class="pre">oauth_scopes</span></code> for logging and monitoring, the service account being used needs the
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles">roles/logging.logWriter</a> and
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles">roles/monitoring.metricWriter</a> roles.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Shielded Instance options. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defines if the instance has integrity monitoring enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defines if the instance has Secure Boot enabled.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of <a class="reference external" href="https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/">Kubernetes taints</a>
to apply to nodes. GKE’s API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause the provider to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through <code class="docutils literal notranslate"><span class="pre">kubectl</span></code>), and it’s recommended that you do not use
this field to manage taints. If you do, <code class="docutils literal notranslate"><span class="pre">lifecycle.ignore_changes</span></code> is
recommended. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Effect for taint. Accepted values are <code class="docutils literal notranslate"><span class="pre">NO_SCHEDULE</span></code>, <code class="docutils literal notranslate"><span class="pre">PREFER_NO_SCHEDULE</span></code>, and <code class="docutils literal notranslate"><span class="pre">NO_EXECUTE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Key for taint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value for taint.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Metadata configuration to expose to workloads on the node pool.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How to expose the node metadata to the workload running on the node.
Accepted values are:</p>
<ul>
<li><p>UNSPECIFIED: Not Set</p></li>
<li><p>SECURE: Prevent workloads not in hostNetwork from accessing certain VM metadata, specifically kube-env, which contains Kubelet credentials, and the instance identity token. See <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy">Metadata Concealment</a> documentation.</p></li>
<li><p>EXPOSE: Expose all VM metadata to pods.</p></li>
<li><p>GKE_METADATA_SERVER: Enables <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity">workload identity</a> on the node.</p></li>
</ul>
</li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
<p>The <strong>private_cluster_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the cluster’s private
endpoint is used as the cluster endpoint and access through the public endpoint
is disabled. When <code class="docutils literal notranslate"><span class="pre">false</span></code>, either endpoint can be used. This field only applies
to private clusters, when <code class="docutils literal notranslate"><span class="pre">enable_private_nodes</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables the private cluster feature,
creating a private endpoint on the cluster. In a private cluster, nodes only
have RFC 1918 private addresses and communicate with the master’s private
endpoint via private networking.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP range in CIDR notation to use for
the hosted master network. This range will be used for assigning private IP
addresses to the cluster master(s) and the ILB VIP. This range must not overlap
with any other ranges in use within the cluster’s network, and it must be a /28
subnet. See <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#limitations">Private Cluster Limitations</a>
for more details. This field only applies to private clusters, when
<code class="docutils literal notranslate"><span class="pre">enable_private_nodes</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peeringName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the peering between this cluster and the Google owned VPC.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The internal IP address of this cluster’s master endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The external IP address of this cluster’s master endpoint.</p></li>
</ul>
<p>The <strong>release_channel</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">channel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The selected release channel.
Accepted values are:</p>
<ul>
<li><p>UNSPECIFIED: Not set.</p></li>
<li><p>RAPID: Weekly upgrade cadence; Early testers and developers who requires new features.</p></li>
<li><p>REGULAR: Multiple per month upgrade cadence; Production users who need features not yet offered in the Stable channel.</p></li>
<li><p>STABLE: Every few months upgrade cadence; Production users who need stability above all else, and for whom frequent upgrades are too risky.</p></li>
</ul>
</li>
</ul>
<p>The <strong>resource_usage_export_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bigqueryDestination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Parameters for using BigQuery as the destination of resource usage export.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableNetworkEgressMetering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable network egress metering for this cluster. If enabled, a daemonset will be created
in the cluster to meter network egress traffic.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableResourceConsumptionMetering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable resource
consumption metering on this cluster. When enabled, a table will be created in
the resource export BigQuery dataset to store resource consumption data. The
resulting table can be joined with the resource usage table or with BigQuery
billing export. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
<p>The <strong>vertical_pod_autoscaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
<p>The <strong>workload_identity_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityNamespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Currently, the only supported identity namespace is the project’s default.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.addons_config">
<code class="sig-name descname">addons_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.addons_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for addons supported by GKE.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrunConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - .
The status of the CloudRun addon. It is disabled by default.
Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">configConnectorConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - .
The status of the ConfigConnector addon. It is disabled by default; Set <code class="docutils literal notranslate"><span class="pre">enabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsCacheConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - .
The status of the NodeLocal DNSCache addon. It is disabled by default.
Set <code class="docutils literal notranslate"><span class="pre">enabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">gcePersistentDiskCsiDriverConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - .
Whether this cluster should enable the Google Compute Engine Persistent Disk Container Storage Interface (CSI) Driver. Defaults to disabled; set <code class="docutils literal notranslate"><span class="pre">enabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">horizontalPodAutoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The status of the Horizontal Pod Autoscaling
addon, which increases or decreases the number of replica pods a replication controller
has based on the resource usage of the existing pods.
It ensures that a Heapster pod is running in the cluster, which is also used by the Cloud Monitoring service.
It is enabled by default;
set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to disable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpLoadBalancing</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The status of the HTTP (L7) load balancing
controller addon, which makes it easy to set up HTTP load balancers for services in a
cluster. It is enabled by default; set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to disable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">istioConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - .
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">auth</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The authentication type between services in Istio. Available options include <code class="docutils literal notranslate"><span class="pre">AUTH_MUTUAL_TLS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kalmConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - .
Configuration for the KALM addon, which manages the lifecycle of k8s. It is disabled by default; Set <code class="docutils literal notranslate"><span class="pre">enabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPolicyConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Whether we should enable the network policy addon
for the master.  This must be enabled in order to enable network policy for the nodes.
To enable this, you must also define a <code class="docutils literal notranslate"><span class="pre">network_policy</span></code> block,
otherwise nothing will happen.
It can only be disabled if the nodes already do not have network policies enabled.
Defaults to disabled; set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.authenticator_groups_config">
<code class="sig-name descname">authenticator_groups_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.authenticator_groups_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite">Google Groups for GKE</a> feature.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the RBAC security group for use with Google security groups in Kubernetes RBAC. Group name must be in format <code class="docutils literal notranslate"><span class="pre">gke-security-groups&#64;yourdomain.com</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.cluster_autoscaling">
<code class="sig-name descname">cluster_autoscaling</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.cluster_autoscaling" title="Permalink to this definition">¶</a></dt>
<dd><p>Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster’s workload. See the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning">guide to using Node Auto-Provisioning</a>
for more details. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoProvisioningDefaults</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Contains defaults for a node pool created by NAP.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code>. See the
<a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">official documentation</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of Google API scopes to be made available
on all of the node VMs under the “default” service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The service account to be used by the Node VMs.
If not specified, the “default” service account is used.
In order to use the configured <code class="docutils literal notranslate"><span class="pre">oauth_scopes</span></code> for logging and monitoring, the service account being used needs the
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles">roles/logging.logWriter</a> and
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles">roles/monitoring.metricWriter</a> roles.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscalingProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ) Configuration
options for the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles">Autoscaling profile</a>
feature, which lets you choose whether the cluster autoscaler should optimize for resource utilization or resource availability
when deciding to remove nodes from a cluster. Can be <code class="docutils literal notranslate"><span class="pre">BALANCED</span></code> or <code class="docutils literal notranslate"><span class="pre">OPTIMIZE_UTILIZATION</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BALANCED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLimits</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Global constraints for machine resources in the
cluster. Configuring the <code class="docutils literal notranslate"><span class="pre">cpu</span></code> and <code class="docutils literal notranslate"><span class="pre">memory</span></code> types is required if node
auto-provisioning is enabled. These limits will apply to node pool autoscaling
in addition to node auto-provisioning. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Maximum amount of the resource in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Minimum amount of the resource in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the resource. For example, <code class="docutils literal notranslate"><span class="pre">cpu</span></code> and
<code class="docutils literal notranslate"><span class="pre">memory</span></code>.  See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning">guide to using Node Auto-Provisioning</a>
for a list of types.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.cluster_ipv4_cidr">
<code class="sig-name descname">cluster_ipv4_cidr</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.cluster_ipv4_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. <code class="docutils literal notranslate"><span class="pre">10.96.0.0/14</span></code>). Leave blank to have one
automatically chosen or specify a <code class="docutils literal notranslate"><span class="pre">/14</span></code> block in <code class="docutils literal notranslate"><span class="pre">10.0.0.0/8</span></code>. This field will
only work for routes-based clusters, where <code class="docutils literal notranslate"><span class="pre">ip_allocation_policy</span></code> is not defined.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.database_encryption">
<code class="sig-name descname">database_encryption</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.database_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keyName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - the key to use to encrypt/decrypt secrets.  See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#Cluster.DatabaseEncryption">DatabaseEncryption definition</a> for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - <code class="docutils literal notranslate"><span class="pre">ENCRYPTED</span></code> or <code class="docutils literal notranslate"><span class="pre">DECRYPTED</span></code></p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.default_max_pods_per_node">
<code class="sig-name descname">default_max_pods_per_node</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.default_max_pods_per_node" title="Permalink to this definition">¶</a></dt>
<dd><p>The default maximum number of pods
per node in this cluster. This doesn’t work on “routes-based” clusters, clusters
that don’t have IP Aliasing enabled. See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.enable_binary_authorization">
<code class="sig-name descname">enable_binary_authorization</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_binary_authorization" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.enable_intranode_visibility">
<code class="sig-name descname">enable_intranode_visibility</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_intranode_visibility" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.enable_kubernetes_alpha">
<code class="sig-name descname">enable_kubernetes_alpha</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_kubernetes_alpha" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.enable_legacy_abac">
<code class="sig-name descname">enable_legacy_abac</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_legacy_abac" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.enable_shielded_nodes">
<code class="sig-name descname">enable_shielded_nodes</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_shielded_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable Shielded Nodes features on all nodes in this cluster.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.enable_tpu">
<code class="sig-name descname">enable_tpu</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.enable_tpu" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable Cloud TPU resources in this cluster.
See the <a class="reference external" href="https://cloud.google.com/tpu/docs/kubernetes-engine-setup">official documentation</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.endpoint">
<code class="sig-name descname">endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of this cluster’s Kubernetes master.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.initial_node_count">
<code class="sig-name descname">initial_node_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.initial_node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of nodes to create in this
cluster’s default node pool. In regional or multi-zonal clusters, this is the
number of nodes per zone. Must be set if <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> is not set. If you’re using
<code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code> objects with no default node pool, you’ll need to
set this to a value of at least <code class="docutils literal notranslate"><span class="pre">1</span></code>, alongside setting
<code class="docutils literal notranslate"><span class="pre">remove_default_node_pool</span></code> to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.instance_group_urls">
<code class="sig-name descname">instance_group_urls</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.instance_group_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>List of instance group URLs which have been assigned
to the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.ip_allocation_policy">
<code class="sig-name descname">ip_allocation_policy</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.ip_allocation_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration of cluster IP allocation for
VPC-native clusters. Adding this block enables <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/ip-aliases">IP aliasing</a>,
making the cluster VPC-native instead of routes-based. Structure is documented
below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clusterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP address range for the cluster pod IPs.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the existing secondary
range in the cluster’s subnetwork to use for pod IP addresses. Alternatively,
<code class="docutils literal notranslate"><span class="pre">cluster_ipv4_cidr_block</span></code> can be used to automatically create a GKE-managed one.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP address range of the services IPs in this cluster.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the existing
secondary range in the cluster’s subnetwork to use for service <code class="docutils literal notranslate"><span class="pre">ClusterIP</span></code>s.
Alternatively, <code class="docutils literal notranslate"><span class="pre">services_ipv4_cidr_block</span></code> can be used to automatically create a
GKE-managed one.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.label_fingerprint">
<code class="sig-name descname">label_fingerprint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.label_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the set of labels for this cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location (region or zone) in which the cluster
master will be created, as well as the default node location. If you specify a
zone (such as <code class="docutils literal notranslate"><span class="pre">us-central1-a</span></code>), the cluster will be a zonal cluster with a
single cluster master. If you specify a region (such as <code class="docutils literal notranslate"><span class="pre">us-west1</span></code>), the
cluster will be a regional cluster with multiple masters spread across zones in
the region, and with default node locations in those zones as well</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.logging_service">
<code class="sig-name descname">logging_service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.logging_service" title="Permalink to this definition">¶</a></dt>
<dd><p>The logging service that the cluster should
write logs to. Available options include <code class="docutils literal notranslate"><span class="pre">logging.googleapis.com</span></code>(Legacy Stackdriver),
<code class="docutils literal notranslate"><span class="pre">logging.googleapis.com/kubernetes</span></code>(Stackdriver Kubernetes Engine Logging), and <code class="docutils literal notranslate"><span class="pre">none</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">logging.googleapis.com/kubernetes</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.maintenance_policy">
<code class="sig-name descname">maintenance_policy</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.maintenance_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The maintenance policy to use for the cluster. Structure is
documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dailyMaintenanceWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Time window specified for daily maintenance operations.
Specify <code class="docutils literal notranslate"><span class="pre">start_time</span></code> in <a class="reference external" href="https://www.ietf.org/rfc/rfc3339.txt">RFC3339</a> format “HH:MM”,
where HH : [00-23] and MM : [00-59] GMT. For example:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurringWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Time window for
recurring maintenance operations.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">endTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurrence</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.master_auth">
<code class="sig-name descname">master_auth</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.master_auth" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication information for accessing the
Kubernetes master. Some values in this block are only returned by the API if
your service account has permission to get credentials for your GKE cluster. If
you see an unexpected diff removing a username/password or unsetting your client
cert, ensure you have the <code class="docutils literal notranslate"><span class="pre">container.clusters.getCredentials</span></code> permission.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificateConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Whether client certificate authorization is enabled for this cluster.  For example:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">issueClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCaCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password to use for HTTP basic authentication when accessing
the Kubernetes master endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username to use for HTTP basic authentication when accessing
the Kubernetes master endpoint. If not present basic auth will be disabled.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.master_authorized_networks_config">
<code class="sig-name descname">master_authorized_networks_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.master_authorized_networks_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired configuration options
for master authorized networks. Omit the nested <code class="docutils literal notranslate"><span class="pre">cidr_blocks</span></code> attribute to disallow
external access (except the cluster node IPs, which GKE automatically whitelists).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cidrBlocks</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - External networks that can access the
Kubernetes cluster master through HTTPS.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cidr_block</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - External network that can access Kubernetes master through HTTPS.
Must be specified in CIDR notation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Field for users to identify CIDR blocks.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.master_version">
<code class="sig-name descname">master_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.master_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The current version of the master in the cluster. This may
be different than the <code class="docutils literal notranslate"><span class="pre">min_master_version</span></code> set in the config if the master
has been updated by GKE.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.min_master_version">
<code class="sig-name descname">min_master_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.min_master_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum version of the master. GKE
will auto-update the master to new versions, so this does not guarantee the
current master version–use the read-only <code class="docutils literal notranslate"><span class="pre">master_version</span></code> field to obtain that.
If unset, the cluster’s version will be set by GKE to the version of the most recent
official release (which is not necessarily the latest version).  Most users will find
the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source useful - it indicates which versions
are available. If you intend to specify versions manually,
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#specifying_cluster_version">the docs</a>
describe the various acceptable formats for this field.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.monitoring_service">
<code class="sig-name descname">monitoring_service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.monitoring_service" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitoring service that the cluster
should write metrics to.
Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.
VM metrics will be collected by Google Compute Engine regardless of this setting
Available options include
<code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com</span></code>(Legacy Stackdriver), <code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com/kubernetes</span></code>(Stackdriver Kubernetes Engine Monitoring), and <code class="docutils literal notranslate"><span class="pre">none</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">monitoring.googleapis.com/kubernetes</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the cluster, unique within the project and
location.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.network">
<code class="sig-name descname">network</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.network" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or self_link of the Google Compute Engine
network to which the cluster is connected. For Shared VPC, set this to the self link of the
shared network.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.network_policy">
<code class="sig-name descname">network_policy</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.network_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration options for the
<a class="reference external" href="https://kubernetes.io/docs/concepts/services-networking/networkpolicies/">NetworkPolicy</a>
feature. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The selected network policy provider. Defaults to PROVIDER_UNSPECIFIED.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.node_config">
<code class="sig-name descname">node_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.node_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Parameters used in creating the default node pool.
Generally, this field should not be used at the same time as a
<code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code> or a <code class="docutils literal notranslate"><span class="pre">node_pool</span></code> block; this configuration
manages the default node pool, which isn’t recommended to be used.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskKmsKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: <a class="reference external" href="https://cloud.google.com/compute/docs/disks/customer-managed-encryption">https://cloud.google.com/compute/docs/disks/customer-managed-encryption</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of the disk attached to each node
(e.g. ‘pd-standard’ or ‘pd-ssd’). If unspecified, the default disk type is ‘pd-standard’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of the type and count of accelerator cards attached to the instance.
Structure documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of the guest accelerator cards exposed to this instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The accelerator type resource to expose to this instance. E.g. <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-k80</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Kubernetes labels (key/value pairs) to be applied to each node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of a Google Compute Engine machine type.
Defaults to <code class="docutils literal notranslate"><span class="pre">n1-standard-1</span></code>. To create a custom machine type, value should be set as specified
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instances#machineType">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The metadata key/value pairs assigned to instances in
the cluster. From GKE <code class="docutils literal notranslate"><span class="pre">1.12</span></code> onwards, <code class="docutils literal notranslate"><span class="pre">disable-legacy-endpoints</span></code> is set to
<code class="docutils literal notranslate"><span class="pre">true</span></code> by the API; if <code class="docutils literal notranslate"><span class="pre">metadata</span></code> is set but that default value is not
included, the provider will attempt to unset the value. To avoid this, set the
value in your config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code>. See the
<a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">official documentation</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of Google API scopes to be made available
on all of the node VMs under the “default” service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - A boolean that represents whether or not the underlying node VMs
are preemptible. See the <a class="reference external" href="https://cloud.google.com/container-engine/docs/preemptible-vm">official documentation</a>
for more information. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods">GKE Sandbox</a> configuration. When enabling this feature you must specify <code class="docutils literal notranslate"><span class="pre">image_type</span> <span class="pre">=</span> <span class="pre">&quot;COS_CONTAINERD&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">node_version</span> <span class="pre">=</span> <span class="pre">&quot;1.12.7-gke.17&quot;</span></code> or later to use it.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Which sandbox to use for pods in the node pool.
Accepted values are:</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The service account to be used by the Node VMs.
If not specified, the “default” service account is used.
In order to use the configured <code class="docutils literal notranslate"><span class="pre">oauth_scopes</span></code> for logging and monitoring, the service account being used needs the
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles">roles/logging.logWriter</a> and
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles">roles/monitoring.metricWriter</a> roles.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Shielded Instance options. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defines if the instance has integrity monitoring enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defines if the instance has Secure Boot enabled.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of <a class="reference external" href="https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/">Kubernetes taints</a>
to apply to nodes. GKE’s API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause the provider to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through <code class="docutils literal notranslate"><span class="pre">kubectl</span></code>), and it’s recommended that you do not use
this field to manage taints. If you do, <code class="docutils literal notranslate"><span class="pre">lifecycle.ignore_changes</span></code> is
recommended. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Effect for taint. Accepted values are <code class="docutils literal notranslate"><span class="pre">NO_SCHEDULE</span></code>, <code class="docutils literal notranslate"><span class="pre">PREFER_NO_SCHEDULE</span></code>, and <code class="docutils literal notranslate"><span class="pre">NO_EXECUTE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Key for taint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value for taint.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Metadata configuration to expose to workloads on the node pool.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How to expose the node metadata to the workload running on the node.
Accepted values are:</p>
<ul>
<li><p>UNSPECIFIED: Not Set</p></li>
<li><p>SECURE: Prevent workloads not in hostNetwork from accessing certain VM metadata, specifically kube-env, which contains Kubelet credentials, and the instance identity token. See <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy">Metadata Concealment</a> documentation.</p></li>
<li><p>EXPOSE: Expose all VM metadata to pods.</p></li>
<li><p>GKE_METADATA_SERVER: Enables <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity">workload identity</a> on the node.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.node_locations">
<code class="sig-name descname">node_locations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.node_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of zones in which the cluster’s nodes
are located. Nodes must be in the region of their regional cluster or in the
same region as their cluster’s zone for zonal clusters. If this is specified for
a zonal cluster, omit the cluster’s zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.node_pools">
<code class="sig-name descname">node_pools</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.node_pools" title="Permalink to this definition">¶</a></dt>
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
manages the default node pool, which isn’t recommended to be used.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskKmsKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: <a class="reference external" href="https://cloud.google.com/compute/docs/disks/customer-managed-encryption">https://cloud.google.com/compute/docs/disks/customer-managed-encryption</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of the disk attached to each node
(e.g. ‘pd-standard’ or ‘pd-ssd’). If unspecified, the default disk type is ‘pd-standard’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of the type and count of accelerator cards attached to the instance.
Structure documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of the guest accelerator cards exposed to this instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The accelerator type resource to expose to this instance. E.g. <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-k80</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Kubernetes labels (key/value pairs) to be applied to each node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of a Google Compute Engine machine type.
Defaults to <code class="docutils literal notranslate"><span class="pre">n1-standard-1</span></code>. To create a custom machine type, value should be set as specified
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instances#machineType">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The metadata key/value pairs assigned to instances in
the cluster. From GKE <code class="docutils literal notranslate"><span class="pre">1.12</span></code> onwards, <code class="docutils literal notranslate"><span class="pre">disable-legacy-endpoints</span></code> is set to
<code class="docutils literal notranslate"><span class="pre">true</span></code> by the API; if <code class="docutils literal notranslate"><span class="pre">metadata</span></code> is set but that default value is not
included, the provider will attempt to unset the value. To avoid this, set the
value in your config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code>. See the
<a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">official documentation</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of Google API scopes to be made available
on all of the node VMs under the “default” service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - A boolean that represents whether or not the underlying node VMs
are preemptible. See the <a class="reference external" href="https://cloud.google.com/container-engine/docs/preemptible-vm">official documentation</a>
for more information. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods">GKE Sandbox</a> configuration. When enabling this feature you must specify <code class="docutils literal notranslate"><span class="pre">image_type</span> <span class="pre">=</span> <span class="pre">&quot;COS_CONTAINERD&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">node_version</span> <span class="pre">=</span> <span class="pre">&quot;1.12.7-gke.17&quot;</span></code> or later to use it.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Which sandbox to use for pods in the node pool.
Accepted values are:</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The service account to be used by the Node VMs.
If not specified, the “default” service account is used.
In order to use the configured <code class="docutils literal notranslate"><span class="pre">oauth_scopes</span></code> for logging and monitoring, the service account being used needs the
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles">roles/logging.logWriter</a> and
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles">roles/monitoring.metricWriter</a> roles.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Shielded Instance options. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defines if the instance has integrity monitoring enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defines if the instance has Secure Boot enabled.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of <a class="reference external" href="https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/">Kubernetes taints</a>
to apply to nodes. GKE’s API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause the provider to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through <code class="docutils literal notranslate"><span class="pre">kubectl</span></code>), and it’s recommended that you do not use
this field to manage taints. If you do, <code class="docutils literal notranslate"><span class="pre">lifecycle.ignore_changes</span></code> is
recommended. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Effect for taint. Accepted values are <code class="docutils literal notranslate"><span class="pre">NO_SCHEDULE</span></code>, <code class="docutils literal notranslate"><span class="pre">PREFER_NO_SCHEDULE</span></code>, and <code class="docutils literal notranslate"><span class="pre">NO_EXECUTE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Key for taint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value for taint.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Metadata configuration to expose to workloads on the node pool.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How to expose the node metadata to the workload running on the node.
Accepted values are:</p>
<ul>
<li><p>UNSPECIFIED: Not Set</p></li>
<li><p>SECURE: Prevent workloads not in hostNetwork from accessing certain VM metadata, specifically kube-env, which contains Kubelet credentials, and the instance identity token. See <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy">Metadata Concealment</a> documentation.</p></li>
<li><p>EXPOSE: Expose all VM metadata to pods.</p></li>
<li><p>GKE_METADATA_SERVER: Enables <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity">workload identity</a> on the node.</p></li>
</ul>
</li>
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

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.node_version">
<code class="sig-name descname">node_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.node_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Kubernetes version on the nodes. Must either be unset
or set to the same value as <code class="docutils literal notranslate"><span class="pre">min_master_version</span></code> on create. Defaults to the default
version set by GKE which is not necessarily the latest version. This only affects
nodes in the default node pool. While a fuzzy version can be specified, it’s
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source’s
<code class="docutils literal notranslate"><span class="pre">version_prefix</span></code> field to approximate fuzzy versions.
To update nodes in other node pools, use the <code class="docutils literal notranslate"><span class="pre">version</span></code> attribute on the node pool.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.pod_security_policy_config">
<code class="sig-name descname">pod_security_policy_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.pod_security_policy_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies">PodSecurityPolicy</a> feature.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.private_cluster_config">
<code class="sig-name descname">private_cluster_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.private_cluster_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters">private clusters</a>,
clusters with private nodes. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the cluster’s private
endpoint is used as the cluster endpoint and access through the public endpoint
is disabled. When <code class="docutils literal notranslate"><span class="pre">false</span></code>, either endpoint can be used. This field only applies
to private clusters, when <code class="docutils literal notranslate"><span class="pre">enable_private_nodes</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables the private cluster feature,
creating a private endpoint on the cluster. In a private cluster, nodes only
have RFC 1918 private addresses and communicate with the master’s private
endpoint via private networking.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP range in CIDR notation to use for
the hosted master network. This range will be used for assigning private IP
addresses to the cluster master(s) and the ILB VIP. This range must not overlap
with any other ranges in use within the cluster’s network, and it must be a /28
subnet. See <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#limitations">Private Cluster Limitations</a>
for more details. This field only applies to private clusters, when
<code class="docutils literal notranslate"><span class="pre">enable_private_nodes</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peeringName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the peering between this cluster and the Google owned VPC.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The internal IP address of this cluster’s master endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The external IP address of this cluster’s master endpoint.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.release_channel">
<code class="sig-name descname">release_channel</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.release_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration options for the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels">Release channel</a>
feature, which provide more control over automatic upgrades of your GKE clusters.
When updating this field, GKE imposes specific version requirements. See
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels#migrating_between_release_channels">Migrating between release channels</a>
for more details; the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> datasource can provide
the default version for a channel. Note that removing the <code class="docutils literal notranslate"><span class="pre">release_channel</span></code>
field from your config will cause this provider to stop managing your cluster’s
release channel, but will not unenroll it. Instead, use the <code class="docutils literal notranslate"><span class="pre">&quot;UNSPECIFIED&quot;</span></code>
channel. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">channel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The selected release channel.
Accepted values are:</p>
<ul>
<li><p>UNSPECIFIED: Not set.</p></li>
<li><p>RAPID: Weekly upgrade cadence; Early testers and developers who requires new features.</p></li>
<li><p>REGULAR: Multiple per month upgrade cadence; Production users who need features not yet offered in the Stable channel.</p></li>
<li><p>STABLE: Every few months upgrade cadence; Production users who need stability above all else, and for whom frequent upgrades are too risky.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.remove_default_node_pool">
<code class="sig-name descname">remove_default_node_pool</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.remove_default_node_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, deletes the default node
pool upon cluster creation. If you’re using <code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code>
resources with no default node pool, this should be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, alongside
setting <code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> to at least <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.resource_labels">
<code class="sig-name descname">resource_labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.resource_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCE resource labels (a map of key/value pairs) to be applied to the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.resource_usage_export_config">
<code class="sig-name descname">resource_usage_export_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.resource_usage_export_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering">ResourceUsageExportConfig</a> feature.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bigqueryDestination</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Parameters for using BigQuery as the destination of resource usage export.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableNetworkEgressMetering</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to enable network egress metering for this cluster. If enabled, a daemonset will be created
in the cluster to meter network egress traffic.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableResourceConsumptionMetering</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to enable resource
consumption metering on this cluster. When enabled, a table will be created in
the resource export BigQuery dataset to store resource consumption data. The
resulting table can be joined with the resource usage table or with BigQuery
billing export. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.services_ipv4_cidr">
<code class="sig-name descname">services_ipv4_cidr</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.services_ipv4_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address range of the Kubernetes services in this
cluster, in <a class="reference external" href="http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">CIDR</a>
notation (e.g. <code class="docutils literal notranslate"><span class="pre">1.2.3.4/29</span></code>). Service addresses are typically put in the last
<code class="docutils literal notranslate"><span class="pre">/16</span></code> from the container CIDR.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.subnetwork">
<code class="sig-name descname">subnetwork</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or self_link of the Google Compute Engine
subnetwork in which the cluster’s instances are launched.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.tpu_ipv4_cidr_block">
<code class="sig-name descname">tpu_ipv4_cidr_block</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.tpu_ipv4_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address range of the Cloud TPUs in this cluster, in
<a class="reference external" href="http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">CIDR</a>
notation (e.g. <code class="docutils literal notranslate"><span class="pre">1.2.3.4/29</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.vertical_pod_autoscaling">
<code class="sig-name descname">vertical_pod_autoscaling</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.vertical_pod_autoscaling" title="Permalink to this definition">¶</a></dt>
<dd><p>Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Cluster.workload_identity_config">
<code class="sig-name descname">workload_identity_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Cluster.workload_identity_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Workload Identity allows Kubernetes service accounts to act as a user-managed
<a class="reference external" href="https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts">Google IAM Service Account</a>.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityNamespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Currently, the only supported identity namespace is the project’s default.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.container.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authenticator_groups_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_autoscaling</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_ipv4_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_encryption</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_max_pods_per_node</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_binary_authorization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_intranode_visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_kubernetes_alpha</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_legacy_abac</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_shielded_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_tpu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_node_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_group_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_allocation_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label_fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_auth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_authorized_networks_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_master_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_pools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pod_security_policy_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_cluster_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_channel</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remove_default_node_pool</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_usage_export_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services_ipv4_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnetwork</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tpu_ipv4_cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vertical_pod_autoscaling</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workload_identity_config</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Cluster.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>cluster_autoscaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to
automatically adjust the size of the cluster and create/delete node pools based
on the current needs of the cluster’s workload. See the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning">guide to using Node Auto-Provisioning</a>
for more details. Structure is documented below.</p>
</p></li>
<li><p><strong>cluster_ipv4_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address range of the Kubernetes pods
in this cluster in CIDR notation (e.g. <code class="docutils literal notranslate"><span class="pre">10.96.0.0/14</span></code>). Leave blank to have one
automatically chosen or specify a <code class="docutils literal notranslate"><span class="pre">/14</span></code> block in <code class="docutils literal notranslate"><span class="pre">10.0.0.0/8</span></code>. This field will
only work for routes-based clusters, where <code class="docutils literal notranslate"><span class="pre">ip_allocation_policy</span></code> is not defined.</p></li>
<li><p><strong>database_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>.
Structure is documented below.</p>
</p></li>
<li><p><strong>default_max_pods_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The default maximum number of pods
per node in this cluster. This doesn’t work on “routes-based” clusters, clusters
that don’t have IP Aliasing enabled. See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the cluster.</p></li>
<li><p><strong>enable_binary_authorization</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Binary Authorization for this cluster.
If enabled, all container images will be validated by Google Binary Authorization.</p></li>
<li><p><strong>enable_intranode_visibility</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.</p></li>
<li><p><strong>enable_kubernetes_alpha</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable Kubernetes Alpha features for
this cluster. Note that when this option is enabled, the cluster cannot be upgraded
and will be automatically deleted after 30 days.</p></li>
<li><p><strong>enable_legacy_abac</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the ABAC authorizer is enabled for this cluster.
When enabled, identities in the system, including service accounts, nodes, and controllers,
will have statically granted permissions beyond those provided by the RBAC configuration or IAM.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><strong>enable_shielded_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Shielded Nodes features on all nodes in this cluster.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_tpu</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Whether to enable Cloud TPU resources in this cluster.
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
<li><p><strong>label_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fingerprint of the set of labels for this cluster.</p></li>
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
are available. If you intend to specify versions manually,
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
manages the default node pool, which isn’t recommended to be used.
Structure is documented below.</p></li>
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
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source’s
<code class="docutils literal notranslate"><span class="pre">version_prefix</span></code> field to approximate fuzzy versions.
To update nodes in other node pools, use the <code class="docutils literal notranslate"><span class="pre">version</span></code> attribute on the node pool.</p></li>
<li><p><strong>pod_security_policy_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration for the
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies">PodSecurityPolicy</a> feature.
Structure is documented below.</p>
</p></li>
<li><p><strong>private_cluster_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration for <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters">private clusters</a>,
clusters with private nodes. Structure is documented below.</p>
</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>release_channel</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration options for the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels">Release channel</a>
feature, which provide more control over automatic upgrades of your GKE clusters.
When updating this field, GKE imposes specific version requirements. See
<a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels#migrating_between_release_channels">Migrating between release channels</a>
for more details; the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> datasource can provide
the default version for a channel. Note that removing the <code class="docutils literal notranslate"><span class="pre">release_channel</span></code>
field from your config will cause this provider to stop managing your cluster’s
release channel, but will not unenroll it. Instead, use the <code class="docutils literal notranslate"><span class="pre">&quot;UNSPECIFIED&quot;</span></code>
channel. Structure is documented below.</p>
</p></li>
<li><p><strong>remove_default_node_pool</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, deletes the default node
pool upon cluster creation. If you’re using <code class="docutils literal notranslate"><span class="pre">container.NodePool</span></code>
resources with no default node pool, this should be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, alongside
setting <code class="docutils literal notranslate"><span class="pre">initial_node_count</span></code> to at least <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>resource_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The GCE resource labels (a map of key/value pairs) to be applied to the cluster.</p></li>
<li><p><strong>resource_usage_export_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration for the
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
<li><p><strong>tpu_ipv4_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The IP address range of the Cloud TPUs in this cluster, in
<a class="reference external" href="http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">CIDR</a>
notation (e.g. <code class="docutils literal notranslate"><span class="pre">1.2.3.4/29</span></code>).</p>
</p></li>
<li><p><strong>vertical_pod_autoscaling</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.
Structure is documented below.</p></li>
<li><p><strong>workload_identity_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Workload Identity allows Kubernetes service accounts to act as a user-managed
<a class="reference external" href="https://cloud.google.com/iam/docs/service-accounts#user-managed_service_accounts">Google IAM Service Account</a>.
Structure is documented below.</p>
</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addons_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudrunConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - .
The status of the CloudRun addon. It is disabled by default.
Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">configConnectorConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - .
The status of the ConfigConnector addon. It is disabled by default; Set <code class="docutils literal notranslate"><span class="pre">enabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsCacheConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - .
The status of the NodeLocal DNSCache addon. It is disabled by default.
Set <code class="docutils literal notranslate"><span class="pre">enabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">gcePersistentDiskCsiDriverConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - .
Whether this cluster should enable the Google Compute Engine Persistent Disk Container Storage Interface (CSI) Driver. Defaults to disabled; set <code class="docutils literal notranslate"><span class="pre">enabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">horizontalPodAutoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The status of the Horizontal Pod Autoscaling
addon, which increases or decreases the number of replica pods a replication controller
has based on the resource usage of the existing pods.
It ensures that a Heapster pod is running in the cluster, which is also used by the Cloud Monitoring service.
It is enabled by default;
set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to disable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpLoadBalancing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The status of the HTTP (L7) load balancing
controller addon, which makes it easy to set up HTTP load balancers for services in a
cluster. It is enabled by default; set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to disable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">istioConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - .
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">auth</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authentication type between services in Istio. Available options include <code class="docutils literal notranslate"><span class="pre">AUTH_MUTUAL_TLS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kalmConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - .
Configuration for the KALM addon, which manages the lifecycle of k8s. It is disabled by default; Set <code class="docutils literal notranslate"><span class="pre">enabled</span> <span class="pre">=</span> <span class="pre">true</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPolicyConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Whether we should enable the network policy addon
for the master.  This must be enabled in order to enable network policy for the nodes.
To enable this, you must also define a <code class="docutils literal notranslate"><span class="pre">network_policy</span></code> block,
otherwise nothing will happen.
It can only be disabled if the nodes already do not have network policies enabled.
Defaults to disabled; set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - The status of the Istio addon, which makes it easy to set up Istio for services in a
cluster. It is disabled by default. Set <code class="docutils literal notranslate"><span class="pre">disabled</span> <span class="pre">=</span> <span class="pre">false</span></code> to enable.</p></li>
</ul>
</li>
</ul>
<p>The <strong>authenticator_groups_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the RBAC security group for use with Google security groups in Kubernetes RBAC. Group name must be in format <code class="docutils literal notranslate"><span class="pre">gke-security-groups&#64;yourdomain.com</span></code>.</p></li>
</ul>
<p>The <strong>cluster_autoscaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoProvisioningDefaults</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Contains defaults for a node pool created by NAP.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code>. See the
<a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">official documentation</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of Google API scopes to be made available
on all of the node VMs under the “default” service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service account to be used by the Node VMs.
If not specified, the “default” service account is used.
In order to use the configured <code class="docutils literal notranslate"><span class="pre">oauth_scopes</span></code> for logging and monitoring, the service account being used needs the
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles">roles/logging.logWriter</a> and
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles">roles/monitoring.metricWriter</a> roles.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscalingProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ) Configuration
options for the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles">Autoscaling profile</a>
feature, which lets you choose whether the cluster autoscaler should optimize for resource utilization or resource availability
when deciding to remove nodes from a cluster. Can be <code class="docutils literal notranslate"><span class="pre">BALANCED</span></code> or <code class="docutils literal notranslate"><span class="pre">OPTIMIZE_UTILIZATION</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BALANCED</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLimits</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Global constraints for machine resources in the
cluster. Configuring the <code class="docutils literal notranslate"><span class="pre">cpu</span></code> and <code class="docutils literal notranslate"><span class="pre">memory</span></code> types is required if node
auto-provisioning is enabled. These limits will apply to node pool autoscaling
in addition to node auto-provisioning. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maximum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum amount of the resource in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimum</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Minimum amount of the resource in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the resource. For example, <code class="docutils literal notranslate"><span class="pre">cpu</span></code> and
<code class="docutils literal notranslate"><span class="pre">memory</span></code>.  See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning">guide to using Node Auto-Provisioning</a>
for a list of types.</p></li>
</ul>
</li>
</ul>
<p>The <strong>database_encryption</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - the key to use to encrypt/decrypt secrets.  See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#Cluster.DatabaseEncryption">DatabaseEncryption definition</a> for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <code class="docutils literal notranslate"><span class="pre">ENCRYPTED</span></code> or <code class="docutils literal notranslate"><span class="pre">DECRYPTED</span></code></p></li>
</ul>
<p>The <strong>ip_allocation_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clusterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address range for the cluster pod IPs.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the existing secondary
range in the cluster’s subnetwork to use for pod IP addresses. Alternatively,
<code class="docutils literal notranslate"><span class="pre">cluster_ipv4_cidr_block</span></code> can be used to automatically create a GKE-managed one.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address range of the services IPs in this cluster.
Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14)
to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14)
from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to
pick a specific range to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicesSecondaryRangeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the existing
secondary range in the cluster’s subnetwork to use for service <code class="docutils literal notranslate"><span class="pre">ClusterIP</span></code>s.
Alternatively, <code class="docutils literal notranslate"><span class="pre">services_ipv4_cidr_block</span></code> can be used to automatically create a
GKE-managed one.</p></li>
</ul>
<p>The <strong>maintenance_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dailyMaintenanceWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Time window specified for daily maintenance operations.
Specify <code class="docutils literal notranslate"><span class="pre">start_time</span></code> in <a class="reference external" href="https://www.ietf.org/rfc/rfc3339.txt">RFC3339</a> format “HH:MM”,
where HH : [00-23] and MM : [00-59] GMT. For example:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">recurringWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Time window for
recurring maintenance operations.</p>
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
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificateConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Whether client certificate authorization is enabled for this cluster.  For example:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">issueClientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCaCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password to use for HTTP basic authentication when accessing
the Kubernetes master endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username to use for HTTP basic authentication when accessing
the Kubernetes master endpoint. If not present basic auth will be disabled.</p></li>
</ul>
<p>The <strong>master_authorized_networks_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cidrBlocks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - External networks that can access the
Kubernetes cluster master through HTTPS.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cidr_block</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - External network that can access Kubernetes master through HTTPS.
Must be specified in CIDR notation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Field for users to identify CIDR blocks.</p></li>
</ul>
</li>
</ul>
<p>The <strong>network_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provider</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The selected network policy provider. Defaults to PROVIDER_UNSPECIFIED.</p></li>
</ul>
<p>The <strong>node_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskKmsKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: <a class="reference external" href="https://cloud.google.com/compute/docs/disks/customer-managed-encryption">https://cloud.google.com/compute/docs/disks/customer-managed-encryption</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the disk attached to each node
(e.g. ‘pd-standard’ or ‘pd-ssd’). If unspecified, the default disk type is ‘pd-standard’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of the type and count of accelerator cards attached to the instance.
Structure documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of the guest accelerator cards exposed to this instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The accelerator type resource to expose to this instance. E.g. <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-k80</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Kubernetes labels (key/value pairs) to be applied to each node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a Google Compute Engine machine type.
Defaults to <code class="docutils literal notranslate"><span class="pre">n1-standard-1</span></code>. To create a custom machine type, value should be set as specified
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instances#machineType">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The metadata key/value pairs assigned to instances in
the cluster. From GKE <code class="docutils literal notranslate"><span class="pre">1.12</span></code> onwards, <code class="docutils literal notranslate"><span class="pre">disable-legacy-endpoints</span></code> is set to
<code class="docutils literal notranslate"><span class="pre">true</span></code> by the API; if <code class="docutils literal notranslate"><span class="pre">metadata</span></code> is set but that default value is not
included, the provider will attempt to unset the value. To avoid this, set the
value in your config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code>. See the
<a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">official documentation</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of Google API scopes to be made available
on all of the node VMs under the “default” service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - A boolean that represents whether or not the underlying node VMs
are preemptible. See the <a class="reference external" href="https://cloud.google.com/container-engine/docs/preemptible-vm">official documentation</a>
for more information. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods">GKE Sandbox</a> configuration. When enabling this feature you must specify <code class="docutils literal notranslate"><span class="pre">image_type</span> <span class="pre">=</span> <span class="pre">&quot;COS_CONTAINERD&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">node_version</span> <span class="pre">=</span> <span class="pre">&quot;1.12.7-gke.17&quot;</span></code> or later to use it.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which sandbox to use for pods in the node pool.
Accepted values are:</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service account to be used by the Node VMs.
If not specified, the “default” service account is used.
In order to use the configured <code class="docutils literal notranslate"><span class="pre">oauth_scopes</span></code> for logging and monitoring, the service account being used needs the
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles">roles/logging.logWriter</a> and
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles">roles/monitoring.metricWriter</a> roles.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Shielded Instance options. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defines if the instance has integrity monitoring enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defines if the instance has Secure Boot enabled.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of <a class="reference external" href="https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/">Kubernetes taints</a>
to apply to nodes. GKE’s API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause the provider to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through <code class="docutils literal notranslate"><span class="pre">kubectl</span></code>), and it’s recommended that you do not use
this field to manage taints. If you do, <code class="docutils literal notranslate"><span class="pre">lifecycle.ignore_changes</span></code> is
recommended. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Effect for taint. Accepted values are <code class="docutils literal notranslate"><span class="pre">NO_SCHEDULE</span></code>, <code class="docutils literal notranslate"><span class="pre">PREFER_NO_SCHEDULE</span></code>, and <code class="docutils literal notranslate"><span class="pre">NO_EXECUTE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Key for taint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value for taint.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Metadata configuration to expose to workloads on the node pool.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How to expose the node metadata to the workload running on the node.
Accepted values are:</p>
<ul>
<li><p>UNSPECIFIED: Not Set</p></li>
<li><p>SECURE: Prevent workloads not in hostNetwork from accessing certain VM metadata, specifically kube-env, which contains Kubelet credentials, and the instance identity token. See <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy">Metadata Concealment</a> documentation.</p></li>
<li><p>EXPOSE: Expose all VM metadata to pods.</p></li>
<li><p>GKE_METADATA_SERVER: Enables <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity">workload identity</a> on the node.</p></li>
</ul>
</li>
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
manages the default node pool, which isn’t recommended to be used.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskKmsKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: <a class="reference external" href="https://cloud.google.com/compute/docs/disks/customer-managed-encryption">https://cloud.google.com/compute/docs/disks/customer-managed-encryption</a></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Size of the disk attached to each node, specified
in GB. The smallest allowed disk size is 10GB. Defaults to 100GB.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the disk attached to each node
(e.g. ‘pd-standard’ or ‘pd-ssd’). If unspecified, the default disk type is ‘pd-standard’</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">guest_accelerators</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of the type and count of accelerator cards attached to the instance.
Structure documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of the guest accelerator cards exposed to this instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The accelerator type resource to expose to this instance. E.g. <code class="docutils literal notranslate"><span class="pre">nvidia-tesla-k80</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The image type to use for this node. Note that changing the image type
will delete and recreate all nodes in the node pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Kubernetes labels (key/value pairs) to be applied to each node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localSsdCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of local SSD disks that will be
attached to each cluster node. Defaults to 0.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">machine_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a Google Compute Engine machine type.
Defaults to <code class="docutils literal notranslate"><span class="pre">n1-standard-1</span></code>. To create a custom machine type, value should be set as specified
<a class="reference external" href="https://cloud.google.com/compute/docs/reference/latest/instances#machineType">here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The metadata key/value pairs assigned to instances in
the cluster. From GKE <code class="docutils literal notranslate"><span class="pre">1.12</span></code> onwards, <code class="docutils literal notranslate"><span class="pre">disable-legacy-endpoints</span></code> is set to
<code class="docutils literal notranslate"><span class="pre">true</span></code> by the API; if <code class="docutils literal notranslate"><span class="pre">metadata</span></code> is set but that default value is not
included, the provider will attempt to unset the value. To avoid this, set the
value in your config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_cpu_platform</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Minimum CPU platform to be used by this instance.
The instance may be scheduled on the specified or newer CPU platform. Applicable
values are the friendly names of CPU platforms, such as <code class="docutils literal notranslate"><span class="pre">Intel</span> <span class="pre">Haswell</span></code>. See the
<a class="reference external" href="https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform">official documentation</a>
for more information.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthScopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of Google API scopes to be made available
on all of the node VMs under the “default” service account. These can be
either FQDNs, or scope aliases. The following scopes are necessary to ensure
the correct functioning of the cluster:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preemptible</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - A boolean that represents whether or not the underlying node VMs
are preemptible. See the <a class="reference external" href="https://cloud.google.com/container-engine/docs/preemptible-vm">official documentation</a>
for more information. Defaults to false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods">GKE Sandbox</a> configuration. When enabling this feature you must specify <code class="docutils literal notranslate"><span class="pre">image_type</span> <span class="pre">=</span> <span class="pre">&quot;COS_CONTAINERD&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">node_version</span> <span class="pre">=</span> <span class="pre">&quot;1.12.7-gke.17&quot;</span></code> or later to use it.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">sandboxType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which sandbox to use for pods in the node pool.
Accepted values are:</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service account to be used by the Node VMs.
If not specified, the “default” service account is used.
In order to use the configured <code class="docutils literal notranslate"><span class="pre">oauth_scopes</span></code> for logging and monitoring, the service account being used needs the
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_logging_roles">roles/logging.logWriter</a> and
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles#stackdriver_monitoring_roles">roles/monitoring.metricWriter</a> roles.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shielded_instance_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Shielded Instance options. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enableIntegrityMonitoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defines if the instance has integrity monitoring enabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableSecureBoot</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defines if the instance has Secure Boot enabled.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The list of instance tags applied to all nodes. Tags are used to identify
valid sources or targets for network firewalls.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of <a class="reference external" href="https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/">Kubernetes taints</a>
to apply to nodes. GKE’s API can only set this field on cluster creation.
However, GKE will add taints to your nodes if you enable certain features such
as GPUs. If this field is set, any diffs on this field will cause the provider to
recreate the underlying resource. Taint values can be updated safely in
Kubernetes (eg. through <code class="docutils literal notranslate"><span class="pre">kubectl</span></code>), and it’s recommended that you do not use
this field to manage taints. If you do, <code class="docutils literal notranslate"><span class="pre">lifecycle.ignore_changes</span></code> is
recommended. Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effect</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Effect for taint. Accepted values are <code class="docutils literal notranslate"><span class="pre">NO_SCHEDULE</span></code>, <code class="docutils literal notranslate"><span class="pre">PREFER_NO_SCHEDULE</span></code>, and <code class="docutils literal notranslate"><span class="pre">NO_EXECUTE</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Key for taint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value for taint.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">workloadMetadataConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Metadata configuration to expose to workloads on the node pool.
Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeMetadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How to expose the node metadata to the workload running on the node.
Accepted values are:</p>
<ul>
<li><p>UNSPECIFIED: Not Set</p></li>
<li><p>SECURE: Prevent workloads not in hostNetwork from accessing certain VM metadata, specifically kube-env, which contains Kubelet credentials, and the instance identity token. See <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/metadata-proxy">Metadata Concealment</a> documentation.</p></li>
<li><p>EXPOSE: Expose all VM metadata to pods.</p></li>
<li><p>GKE_METADATA_SERVER: Enables <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity">workload identity</a> on the node.</p></li>
</ul>
</li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
<p>The <strong>private_cluster_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the cluster’s private
endpoint is used as the cluster endpoint and access through the public endpoint
is disabled. When <code class="docutils literal notranslate"><span class="pre">false</span></code>, either endpoint can be used. This field only applies
to private clusters, when <code class="docutils literal notranslate"><span class="pre">enable_private_nodes</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enablePrivateNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables the private cluster feature,
creating a private endpoint on the cluster. In a private cluster, nodes only
have RFC 1918 private addresses and communicate with the master’s private
endpoint via private networking.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterIpv4CidrBlock</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP range in CIDR notation to use for
the hosted master network. This range will be used for assigning private IP
addresses to the cluster master(s) and the ILB VIP. This range must not overlap
with any other ranges in use within the cluster’s network, and it must be a /28
subnet. See <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#limitations">Private Cluster Limitations</a>
for more details. This field only applies to private clusters, when
<code class="docutils literal notranslate"><span class="pre">enable_private_nodes</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peeringName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the peering between this cluster and the Google owned VPC.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The internal IP address of this cluster’s master endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The external IP address of this cluster’s master endpoint.</p></li>
</ul>
<p>The <strong>release_channel</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">channel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The selected release channel.
Accepted values are:</p>
<ul>
<li><p>UNSPECIFIED: Not set.</p></li>
<li><p>RAPID: Weekly upgrade cadence; Early testers and developers who requires new features.</p></li>
<li><p>REGULAR: Multiple per month upgrade cadence; Production users who need features not yet offered in the Stable channel.</p></li>
<li><p>STABLE: Every few months upgrade cadence; Production users who need stability above all else, and for whom frequent upgrades are too risky.</p></li>
</ul>
</li>
</ul>
<p>The <strong>resource_usage_export_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bigqueryDestination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Parameters for using BigQuery as the destination of resource usage export.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dataset_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableNetworkEgressMetering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable network egress metering for this cluster. If enabled, a daemonset will be created
in the cluster to meter network egress traffic.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableResourceConsumptionMetering</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable resource
consumption metering on this cluster. When enabled, a table will be created in
the resource export BigQuery dataset to store resource consumption data. The
resulting table can be joined with the resource usage table or with BigQuery
billing export. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
<p>The <strong>vertical_pod_autoscaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enable the PodSecurityPolicy controller for this cluster.
If enabled, pods must be valid under a PodSecurityPolicy to be created.</p></li>
</ul>
<p>The <strong>workload_identity_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityNamespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Currently, the only supported identity namespace is the project’s default.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.container.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_gcp.container.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_gcp.container.GetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">GetClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">additional_zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">addons_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authenticator_groups_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_autoscalings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_ipv4_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_encryptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_max_pods_per_node</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_binary_authorization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_intranode_visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_kubernetes_alpha</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_legacy_abac</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_shielded_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_tpu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_node_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_group_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_allocation_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label_fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_authorized_networks_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_auths</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_master_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitoring_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_pools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pod_security_policy_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_cluster_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_channels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remove_default_node_pool</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_usage_export_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services_ipv4_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnetwork</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tpu_ipv4_cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vertical_pod_autoscalings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workload_identity_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="py attribute">
<dt id="pulumi_gcp.container.GetClusterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.container.GetEngineVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">GetEngineVersionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">default_cluster_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_master_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_node_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_channel_default_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">valid_master_versions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">valid_node_versions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_prefix</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEngineVersions.</p>
<dl class="py attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.default_cluster_version">
<code class="sig-name descname">default_cluster_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.default_cluster_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of Kubernetes the service deploys by default.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.latest_master_version">
<code class="sig-name descname">latest_master_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.latest_master_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version available in the given zone for use with master instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.latest_node_version">
<code class="sig-name descname">latest_node_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.latest_node_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version available in the given zone for use with node instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.release_channel_default_version">
<code class="sig-name descname">release_channel_default_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.release_channel_default_version" title="Permalink to this definition">¶</a></dt>
<dd><p>A map from a release channel name to the channel’s default version.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.valid_master_versions">
<code class="sig-name descname">valid_master_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.valid_master_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of versions available in the given zone for use with master instances.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.GetEngineVersionsResult.valid_node_versions">
<code class="sig-name descname">valid_node_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetEngineVersionsResult.valid_node_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of versions available in the given zone for use with node instances.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.container.GetRegistryImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">GetRegistryImageResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">digest</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetRegistryImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistryImage.</p>
<dl class="py attribute">
<dt id="pulumi_gcp.container.GetRegistryImageResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetRegistryImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.container.GetRegistryRepositoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">GetRegistryRepositoryResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.GetRegistryRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistryRepository.</p>
<dl class="py attribute">
<dt id="pulumi_gcp.container.GetRegistryRepositoryResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.GetRegistryRepositoryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gcp.container.NodePool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">NodePool</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autoscaling</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_node_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_pods_per_node</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">upgrade_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.NodePool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a node pool in a Google Kubernetes Engine (GKE) cluster separately from
the cluster control plane. For more information see <a class="reference external" href="https://cloud.google.com/container-engine/docs/node-pools">the official documentation</a>
and <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters.nodePools">the API reference</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">primary</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">container</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;primary&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;us-central1&quot;</span><span class="p">,</span>
    <span class="n">remove_default_node_pool</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">initial_node_count</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">primary_preemptible_nodes</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">container</span><span class="o">.</span><span class="n">NodePool</span><span class="p">(</span><span class="s2">&quot;primaryPreemptibleNodes&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;us-central1&quot;</span><span class="p">,</span>
    <span class="n">cluster</span><span class="o">=</span><span class="n">primary</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">node_count</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">node_config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;preemptible&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;machine_type&quot;</span><span class="p">:</span> <span class="s2">&quot;n1-standard-1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;oauthScopes&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;https://www.googleapis.com/auth/logging.write&quot;</span><span class="p">,</span>
            <span class="s2">&quot;https://www.googleapis.com/auth/monitoring&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">primary</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">container</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;primary&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;us-central1-a&quot;</span><span class="p">,</span>
    <span class="n">initial_node_count</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">node_locations</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;us-central1-c&quot;</span><span class="p">],</span>
    <span class="n">master_auth</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;username&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span>
        <span class="s2">&quot;password&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span>
        <span class="s2">&quot;client_certificate_config&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;issueClientCertificate&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">},</span>
    <span class="n">node_config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;oauthScopes&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;https://www.googleapis.com/auth/logging.write&quot;</span><span class="p">,</span>
            <span class="s2">&quot;https://www.googleapis.com/auth/monitoring&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="s2">&quot;metadata&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;disable-legacy-endpoints&quot;</span><span class="p">:</span> <span class="s2">&quot;true&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="s2">&quot;guest_accelerator&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;nvidia-tesla-k80&quot;</span><span class="p">,</span>
            <span class="s2">&quot;count&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
        <span class="p">}],</span>
    <span class="p">})</span>
<span class="n">np</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">container</span><span class="o">.</span><span class="n">NodePool</span><span class="p">(</span><span class="s2">&quot;np&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;us-central1-a&quot;</span><span class="p">,</span>
    <span class="n">cluster</span><span class="o">=</span><span class="n">primary</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">node_count</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">timeouts</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;create&quot;</span><span class="p">:</span> <span class="s2">&quot;30m&quot;</span><span class="p">,</span>
        <span class="s2">&quot;update&quot;</span><span class="p">:</span> <span class="s2">&quot;20m&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
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
<li><p><strong>max_pods_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are “route-based” - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the node pool. If left blank, the provider will
auto-generate a unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>node_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The node configuration of the pool. See
container.Cluster for schema.</p></li>
<li><p><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside <code class="docutils literal notranslate"><span class="pre">autoscaling</span></code>.</p></li>
<li><p><strong>node_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of zones in which the node pool’s nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster’s zone for zonal clusters. If unspecified, the cluster-level
<code class="docutils literal notranslate"><span class="pre">node_locations</span></code> will be used.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.</p></li>
<li><p><strong>upgrade_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of <code class="docutils literal notranslate"><span class="pre">max_surge</span></code> and <code class="docutils literal notranslate"><span class="pre">max_unavailable</span></code>.
The maximum number of nodes upgraded simultaneously is limited to 20.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Kubernetes version for the nodes in this pool. Note that if this field
and <code class="docutils literal notranslate"><span class="pre">auto_upgrade</span></code> are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it’s
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source’s
<code class="docutils literal notranslate"><span class="pre">version_prefix</span></code> field to approximate fuzzy versions in a provider-compatible way.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum number of nodes in the NodePool. Must be &gt;= min_node_count.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Minimum number of nodes in the NodePool. Must be &gt;=0 and
&lt;= <code class="docutils literal notranslate"><span class="pre">max_node_count</span></code>.</p></li>
</ul>
<p>The <strong>management</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoRepair</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether the nodes will be automatically repaired.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether the nodes will be automatically upgraded.</p></li>
</ul>
<p>The <strong>node_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskKmsKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of additional nodes that can be added to the node pool during
an upgrade. Increasing <code class="docutils literal notranslate"><span class="pre">max_surge</span></code> raises the number of nodes that can be upgraded simultaneously.
Can be set to 0 or greater.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of nodes that can be simultaneously unavailable during
an upgrade. Increasing <code class="docutils literal notranslate"><span class="pre">max_unavailable</span></code> raises the number of nodes that can be upgraded in
parallel. Can be set to 0 or greater.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.autoscaling">
<code class="sig-name descname">autoscaling</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.autoscaling" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration required by cluster autoscaler to adjust
the size of the node pool to the current cluster usage. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Maximum number of nodes in the NodePool. Must be &gt;= min_node_count.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Minimum number of nodes in the NodePool. Must be &gt;=0 and
&lt;= <code class="docutils literal notranslate"><span class="pre">max_node_count</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.cluster">
<code class="sig-name descname">cluster</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster to create the node pool for. Cluster must be present in <code class="docutils literal notranslate"><span class="pre">location</span></code> provided for zonal clusters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.initial_node_count">
<code class="sig-name descname">initial_node_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.initial_node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The initial number of nodes for the pool. In
regional or multi-zonal clusters, this is the number of nodes per zone. Changing
this will force recreation of the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.instance_group_urls">
<code class="sig-name descname">instance_group_urls</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.instance_group_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource URLs of the managed instance groups associated with this node pool.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location (region or zone) of the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.management">
<code class="sig-name descname">management</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.management" title="Permalink to this definition">¶</a></dt>
<dd><p>Node management configuration, wherein auto-repair and
auto-upgrade is configured. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoRepair</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether the nodes will be automatically repaired.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether the nodes will be automatically upgraded.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.max_pods_per_node">
<code class="sig-name descname">max_pods_per_node</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.max_pods_per_node" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are “route-based” - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the node pool. If left blank, the provider will
auto-generate a unique name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.node_config">
<code class="sig-name descname">node_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.node_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The node configuration of the pool. See
container.Cluster for schema.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskKmsKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
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

<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.node_count">
<code class="sig-name descname">node_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside <code class="docutils literal notranslate"><span class="pre">autoscaling</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.node_locations">
<code class="sig-name descname">node_locations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.node_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of zones in which the node pool’s nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster’s zone for zonal clusters. If unspecified, the cluster-level
<code class="docutils literal notranslate"><span class="pre">node_locations</span></code> will be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.upgrade_settings">
<code class="sig-name descname">upgrade_settings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.upgrade_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of <code class="docutils literal notranslate"><span class="pre">max_surge</span></code> and <code class="docutils literal notranslate"><span class="pre">max_unavailable</span></code>.
The maximum number of nodes upgraded simultaneously is limited to 20.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurge</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of additional nodes that can be added to the node pool during
an upgrade. Increasing <code class="docutils literal notranslate"><span class="pre">max_surge</span></code> raises the number of nodes that can be upgraded simultaneously.
Can be set to 0 or greater.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailable</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of nodes that can be simultaneously unavailable during
an upgrade. Increasing <code class="docutils literal notranslate"><span class="pre">max_unavailable</span></code> raises the number of nodes that can be upgraded in
parallel. Can be set to 0 or greater.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.NodePool.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.NodePool.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Kubernetes version for the nodes in this pool. Note that if this field
and <code class="docutils literal notranslate"><span class="pre">auto_upgrade</span></code> are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it’s
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source’s
<code class="docutils literal notranslate"><span class="pre">version_prefix</span></code> field to approximate fuzzy versions in a provider-compatible way.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.container.NodePool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">autoscaling</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_node_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_group_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_pods_per_node</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">upgrade_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.NodePool.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>max_pods_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The maximum number of pods per node in this node pool.
Note that this does not work on node pools which are “route-based” - that is, node
pools belonging to clusters that do not have IP Aliasing enabled.
See the <a class="reference external" href="https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr">official documentation</a>
for more information.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the node pool. If left blank, the provider will
auto-generate a unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name for the node pool beginning
with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>node_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The node configuration of the pool. See
container.Cluster for schema.</p></li>
<li><p><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of nodes per instance group. This field can be used to
update the number of nodes per instance group but should not be used alongside <code class="docutils literal notranslate"><span class="pre">autoscaling</span></code>.</p></li>
<li><p><strong>node_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of zones in which the node pool’s nodes should be located. Nodes must
be in the region of their regional cluster or in the same region as their
cluster’s zone for zonal clusters. If unspecified, the cluster-level
<code class="docutils literal notranslate"><span class="pre">node_locations</span></code> will be used.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to create the node pool. If blank,
the provider-configured project will be used.</p></li>
<li><p><strong>upgrade_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specify node upgrade settings to change how many nodes GKE attempts to
upgrade at once. The number of nodes upgraded simultaneously is the sum of <code class="docutils literal notranslate"><span class="pre">max_surge</span></code> and <code class="docutils literal notranslate"><span class="pre">max_unavailable</span></code>.
The maximum number of nodes upgraded simultaneously is limited to 20.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Kubernetes version for the nodes in this pool. Note that if this field
and <code class="docutils literal notranslate"><span class="pre">auto_upgrade</span></code> are both specified, they will fight each other for what the node version should
be, so setting both is highly discouraged. While a fuzzy version can be specified, it’s
recommended that you specify explicit versions as the provider will see spurious diffs
when fuzzy versions are used. See the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> data source’s
<code class="docutils literal notranslate"><span class="pre">version_prefix</span></code> field to approximate fuzzy versions in a provider-compatible way.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>autoscaling</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Maximum number of nodes in the NodePool. Must be &gt;= min_node_count.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minNodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Minimum number of nodes in the NodePool. Must be &gt;=0 and
&lt;= <code class="docutils literal notranslate"><span class="pre">max_node_count</span></code>.</p></li>
</ul>
<p>The <strong>management</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoRepair</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether the nodes will be automatically repaired.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether the nodes will be automatically upgraded.</p></li>
</ul>
<p>The <strong>node_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bootDiskKmsKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">maxSurge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of additional nodes that can be added to the node pool during
an upgrade. Increasing <code class="docutils literal notranslate"><span class="pre">max_surge</span></code> raises the number of nodes that can be upgraded simultaneously.
Can be set to 0 or greater.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnavailable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of nodes that can be simultaneously unavailable during
an upgrade. Increasing <code class="docutils literal notranslate"><span class="pre">max_unavailable</span></code> raises the number of nodes that can be upgraded in
parallel. Can be set to 0 or greater.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.container.NodePool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.NodePool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_gcp.container.NodePool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.NodePool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_gcp.container.Registry">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">Registry</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Registry" title="Permalink to this definition">¶</a></dt>
<dd><p>Ensures that the Google Cloud Storage bucket that backs Google Container Registry exists. Creating this resource will create the backing bucket if it does not exist, or do nothing if the bucket already exists. Destroying this resource does <em>NOT</em> destroy the backing bucket. For more information see <a class="reference external" href="https://cloud.google.com/container-registry/docs/overview">the official documentation</a></p>
<p>This resource can be used to ensure that the GCS bucket exists prior to assigning permissions. For more information see the <a class="reference external" href="https://cloud.google.com/container-registry/docs/access-control">access control page</a> for GCR.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">registry</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">container</span><span class="o">.</span><span class="n">Registry</span><span class="p">(</span><span class="s2">&quot;registry&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;EU&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="s2">&quot;my-project&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The location of the registry. One of <code class="docutils literal notranslate"><span class="pre">ASIA</span></code>, <code class="docutils literal notranslate"><span class="pre">EU</span></code>, <code class="docutils literal notranslate"><span class="pre">US</span></code> or not specified. See <a class="reference external" href="https://cloud.google.com/container-registry/docs/pushing-and-pulling#pushing_an_image_to_a_registry">the official documentation</a> for more information on registry locations.</p>
</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.container.Registry.bucket_self_link">
<code class="sig-name descname">bucket_self_link</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Registry.bucket_self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Registry.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Registry.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the registry. One of <code class="docutils literal notranslate"><span class="pre">ASIA</span></code>, <code class="docutils literal notranslate"><span class="pre">EU</span></code>, <code class="docutils literal notranslate"><span class="pre">US</span></code> or not specified. See <a class="reference external" href="https://cloud.google.com/container-registry/docs/pushing-and-pulling#pushing_an_image_to_a_registry">the official documentation</a> for more information on registry locations.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.container.Registry.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.container.Registry.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.container.Registry.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_self_link</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Registry.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Registry resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bucket_self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The location of the registry. One of <code class="docutils literal notranslate"><span class="pre">ASIA</span></code>, <code class="docutils literal notranslate"><span class="pre">EU</span></code>, <code class="docutils literal notranslate"><span class="pre">US</span></code> or not specified. See <a class="reference external" href="https://cloud.google.com/container-registry/docs/pushing-and-pulling#pushing_an_image_to_a_registry">the official documentation</a> for more information on registry locations.</p>
</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.container.Registry.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Registry.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_gcp.container.Registry.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.Registry.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_gcp.container.get_cluster">
<code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">get_cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Get info about a GKE cluster from its name and location.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">my_cluster</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">container</span><span class="o">.</span><span class="n">get_cluster</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;my-cluster&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;us-east1-a&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;clusterUsername&quot;</span><span class="p">,</span> <span class="n">my_cluster</span><span class="o">.</span><span class="n">master_auths</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;username&quot;</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;clusterPassword&quot;</span><span class="p">,</span> <span class="n">my_cluster</span><span class="o">.</span><span class="n">master_auths</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;password&quot;</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;endpoint&quot;</span><span class="p">,</span> <span class="n">my_cluster</span><span class="o">.</span><span class="n">endpoint</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;instanceGroupUrls&quot;</span><span class="p">,</span> <span class="n">my_cluster</span><span class="o">.</span><span class="n">instance_group_urls</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;nodeConfig&quot;</span><span class="p">,</span> <span class="n">my_cluster</span><span class="o">.</span><span class="n">node_configs</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;nodePools&quot;</span><span class="p">,</span> <span class="n">my_cluster</span><span class="o">.</span><span class="n">node_pools</span><span class="p">)</span>
</pre></div>
</div>
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
</dd></dl>

<dl class="py function">
<dt id="pulumi_gcp.container.get_engine_versions">
<code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">get_engine_versions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_engine_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to available Google Kubernetes Engine versions in a zone or region for a given project.</p>
<blockquote>
<div><p>If you are using the <code class="docutils literal notranslate"><span class="pre">container.getEngineVersions</span></code> datasource with a
regional cluster, ensure that you have provided a region as the <code class="docutils literal notranslate"><span class="pre">location</span></code> to
the datasource. A region can have a different set of supported versions than
its component zones, and not all zones in a region are guaranteed to
support the same version.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">central1b</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">container</span><span class="o">.</span><span class="n">get_engine_versions</span><span class="p">(</span><span class="n">location</span><span class="o">=</span><span class="s2">&quot;us-central1-b&quot;</span><span class="p">,</span>
    <span class="n">version_prefix</span><span class="o">=</span><span class="s2">&quot;1.12.&quot;</span><span class="p">)</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">container</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;us-central1-b&quot;</span><span class="p">,</span>
    <span class="n">node_version</span><span class="o">=</span><span class="n">central1b</span><span class="o">.</span><span class="n">latest_node_version</span><span class="p">,</span>
    <span class="n">initial_node_count</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">master_auth</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;username&quot;</span><span class="p">:</span> <span class="s2">&quot;mr.yoda&quot;</span><span class="p">,</span>
        <span class="s2">&quot;password&quot;</span><span class="p">:</span> <span class="s2">&quot;adoy.rm&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;stableChannelVersion&quot;</span><span class="p">,</span> <span class="n">central1b</span><span class="o">.</span><span class="n">release_channel_default_version</span><span class="p">[</span><span class="s2">&quot;STABLE&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>location</strong> (<em>str</em>) – The location (region or zone) to list versions for.
Must exactly match the location the cluster will be deployed in, or listed
versions may not be available. If <code class="docutils literal notranslate"><span class="pre">location</span></code>, <code class="docutils literal notranslate"><span class="pre">region</span></code>, and <code class="docutils literal notranslate"><span class="pre">zone</span></code> are not
specified, the provider-level zone must be set and is used instead.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – ID of the project to list available cluster versions for. Should match the project the cluster will be deployed to.
Defaults to the project that the provider is authenticated with.</p></li>
<li><p><strong>version_prefix</strong> (<em>str</em>) – If provided, the provider will only return versions
that match the string prefix. For example, <code class="docutils literal notranslate"><span class="pre">1.11.</span></code> will match all <code class="docutils literal notranslate"><span class="pre">1.11</span></code> series
releases. Since this is just a string match, it’s recommended that you append a
<code class="docutils literal notranslate"><span class="pre">.</span></code> after minor versions to ensure that prefixes such as <code class="docutils literal notranslate"><span class="pre">1.1</span></code> don’t match
versions like <code class="docutils literal notranslate"><span class="pre">1.12.5-gke.10</span></code> accidentally. See <a class="reference external" href="https://cloud.google.com/kubernetes-engine/versioning-and-upgrades#versioning_scheme">the docs on versioning schema</a>
for full details on how version strings are formatted.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_gcp.container.get_registry_image">
<code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">get_registry_image</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">digest</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_registry_image" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source fetches the project name, and provides the appropriate URLs to use for container registry for this project.</p>
<p>The URLs are computed entirely offline - as long as the project exists, they will be valid, but this data source does not contact Google Container Registry (GCR) at any point.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">debian</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">container</span><span class="o">.</span><span class="n">get_registry_image</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;debian&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;gcrLocation&quot;</span><span class="p">,</span> <span class="n">debian</span><span class="o">.</span><span class="n">image_url</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_gcp.container.get_registry_repository">
<code class="sig-prename descclassname">pulumi_gcp.container.</code><code class="sig-name descname">get_registry_repository</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.container.get_registry_repository" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source fetches the project name, and provides the appropriate URLs to use for container registry for this project.</p>
<p>The URLs are computed entirely offline - as long as the project exists, they will be valid, but this data source does not contact Google Container Registry (GCR) at any point.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">container</span><span class="o">.</span><span class="n">get_registry_repository</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;gcrLocation&quot;</span><span class="p">,</span> <span class="n">foo</span><span class="o">.</span><span class="n">repository_url</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

</div>
