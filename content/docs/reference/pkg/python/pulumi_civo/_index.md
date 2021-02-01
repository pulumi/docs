---
title: Package pulumi_civo
title_tag: Package pulumi_civo | Python SDK
linktitle: pulumi_civo
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "civo" >}}

<div class="section" id="pulumi-civo">
<h1>Pulumi Civo<a class="headerlink" href="#pulumi-civo" title="Permalink to this headline"></a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-civo">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-civo/issues">pulumi/pulumi-civo repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-civo/issues">terraform-providers/terraform-provider-civo repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_civo"></span><dl class="py class">
<dt id="pulumi_civo.AwaitableGetDnsDomainNameResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetDnsDomainNameResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetDnsDomainNameResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetDnsDomainRecordResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetDnsDomainRecordResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetDnsDomainRecordResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetInstanceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetInstanceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cpu_cores</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">firewall_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pseudo_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ram_mb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reverse_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sshkey_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetInstanceResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetInstancesResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetInstancesSizeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetInstancesSizeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sizes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetInstancesSizeResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetKubernetesClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetKubernetesClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">api_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">built_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_entry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">installed_applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubeconfig</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_target_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ready</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_nodes_size</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetKubernetesClusterResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetKubernetesVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetKubernetesVersionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">versions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetKubernetesVersionResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetLoadBalancerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetLoadBalancerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">backends</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fail_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_invalid_backend_tls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_conns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_request_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetLoadBalancerResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetNetworkResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetNetworkResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">completed_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cron_timing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">next_execution</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requested_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">safe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetSnapshotResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetSshKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetSshKeyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetSshKeyResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetTemplateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetTemplateResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">templates</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetTemplateResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">bootable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mount_point</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_gb</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetVolumeResult" title="Permalink to this definition"></a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.DnsDomainName">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">DnsDomainName</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.DnsDomainName" title="Permalink to this definition"></a></dt>
<dd><p>Provides a Civo dns domain name resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="c1"># Create a new domain name</span>
<span class="n">main</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">DnsDomainName</span><span class="p">(</span><span class="s2">&quot;main&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Domains can be imported using the <code class="docutils literal notranslate"><span class="pre">domain</span> <span class="pre">name</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import civo:index/dnsDomainName:DnsDomainName main mydomain.com
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the domain</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_civo.DnsDomainName.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_civo.DnsDomainName" title="pulumi_civo.DnsDomainName">DnsDomainName</a><a class="headerlink" href="#pulumi_civo.DnsDomainName.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing DnsDomainName resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id account of the domain</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the domain</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainName.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_civo.DnsDomainName.account_id" title="Permalink to this definition"></a></dt>
<dd><p>The id account of the domain</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainName.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.DnsDomainName.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the domain</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainName.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.DnsDomainName.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.DnsDomainName.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.DnsDomainName.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.DnsDomainRecord">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">DnsDomainRecord</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.DnsDomainRecord" title="Permalink to this definition"></a></dt>
<dd><p>Provides a Civo dns domain record resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="c1"># Create a new domain record</span>
<span class="n">www</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">DnsDomainRecord</span><span class="p">(</span><span class="s2">&quot;www&quot;</span><span class="p">,</span>
    <span class="n">domain_id</span><span class="o">=</span><span class="n">civo_dns_domain_name</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;A&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="n">civo_instance</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">][</span><span class="s2">&quot;public_ip&quot;</span><span class="p">],</span>
    <span class="n">ttl</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
    <span class="n">opts</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span>
            <span class="n">civo_dns_domain_name</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">],</span>
            <span class="n">civo_instance</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">],</span>
        <span class="p">]))</span>
</pre></div>
</div>
<p>Domains can be imported using the <code class="docutils literal notranslate"><span class="pre">id_domain:id_domain_record</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import civo:index/dnsDomainRecord:DnsDomainRecord www a3cd6832-9577-4017-afd7-17d239fc0bf0:c9a39d14-ee1b-4870-8fb0-a2d4f465e822
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the domain</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The portion before the domain name (e.g. www) or an &#64; for the apex/root domain (you cannot use an A record with an amex/root domain)</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Useful for MX records only, the priority mail should be attempted it (defaults to 10)</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The choice of record type from A, CNAME, MX, SRV or TXT</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_civo.DnsDomainRecord.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_civo.DnsDomainRecord" title="pulumi_civo.DnsDomainRecord">DnsDomainRecord</a><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing DnsDomainRecord resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id account of the domain</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date when it was created in UTC format</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the domain</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The portion before the domain name (e.g. www) or an &#64; for the apex/root domain (you cannot use an A record with an amex/root domain)</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Useful for MX records only, the priority mail should be attempted it (defaults to 10)</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The choice of record type from A, CNAME, MX, SRV or TXT</p></li>
<li><p><strong>updated_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date when it was updated in UTC format</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainRecord.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.account_id" title="Permalink to this definition"></a></dt>
<dd><p>The id account of the domain</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainRecord.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.created_at" title="Permalink to this definition"></a></dt>
<dd><p>The date when it was created in UTC format</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainRecord.domain_id">
<em class="property">property </em><code class="sig-name descname">domain_id</code><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.domain_id" title="Permalink to this definition"></a></dt>
<dd><p>The id of the domain</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainRecord.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.name" title="Permalink to this definition"></a></dt>
<dd><p>The portion before the domain name (e.g. www) or an &#64; for the apex/root domain (you cannot use an A record with an amex/root domain)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainRecord.priority">
<em class="property">property </em><code class="sig-name descname">priority</code><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.priority" title="Permalink to this definition"></a></dt>
<dd><p>Useful for MX records only, the priority mail should be attempted it (defaults to 10)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainRecord.ttl">
<em class="property">property </em><code class="sig-name descname">ttl</code><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.ttl" title="Permalink to this definition"></a></dt>
<dd><p>How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainRecord.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.type" title="Permalink to this definition"></a></dt>
<dd><p>The choice of record type from A, CNAME, MX, SRV or TXT</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainRecord.updated_at">
<em class="property">property </em><code class="sig-name descname">updated_at</code><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.updated_at" title="Permalink to this definition"></a></dt>
<dd><p>The date when it was updated in UTC format</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainRecord.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.value" title="Permalink to this definition"></a></dt>
<dd><p>The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainRecord.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.DnsDomainRecord.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.Firewall">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">Firewall</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Firewall" title="Permalink to this definition"></a></dt>
<dd><p>Provides a Civo Cloud Firewall resource. This can be used to create,
modify, and delete Firewalls.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">www</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">Firewall</span><span class="p">(</span><span class="s2">&quot;www&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Firewalls can be imported using the firewall <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import civo:index/firewall:Firewall www b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Firewall name</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_civo.Firewall.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_civo.Firewall" title="pulumi_civo.Firewall">Firewall</a><a class="headerlink" href="#pulumi_civo.Firewall.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Firewall resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Firewall name</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where the firewall was create.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Firewall.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.Firewall.name" title="Permalink to this definition"></a></dt>
<dd><p>The Firewall name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Firewall.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_civo.Firewall.region" title="Permalink to this definition"></a></dt>
<dd><p>The region where the firewall was create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Firewall.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Firewall.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.Firewall.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Firewall.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.FirewallRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">FirewallRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidrs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">direction</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">firewall_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.FirewallRule" title="Permalink to this definition"></a></dt>
<dd><p>Provides a Civo Cloud Firewall Rule resource.
This can be used to create, modify, and delete Firewalls Rules.
This resource don’t have an update option because the backend don’t have the
support for that, so in this case we use ForceNew for all object in the resource.</p>
<p>Firewalls can be imported using the firewall <code class="docutils literal notranslate"><span class="pre">firewall_id:firewall_rule_id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import civo:index/firewallRule:FirewallRule http b8ecd2ab-2267-4a5e-8692-cbf1d32583e3:4b0022ee-00b2-4f81-a40d-b4f8728923a7
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – will this rule affect ingress traffic</p></li>
<li><p><strong>end_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end port where traffic to be allowed.</p></li>
<li><p><strong>firewall_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Firewall id</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – a string that will be the displayed name/reference for this rule (optional)</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This may be one of “tcp”, “udp”, or “icmp”.</p></li>
<li><p><strong>start_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The start port where traffic to be allowed.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_civo.FirewallRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidrs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">direction</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">firewall_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_civo.FirewallRule" title="pulumi_civo.FirewallRule">FirewallRule</a><a class="headerlink" href="#pulumi_civo.FirewallRule.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing FirewallRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – will this rule affect ingress traffic</p></li>
<li><p><strong>end_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end port where traffic to be allowed.</p></li>
<li><p><strong>firewall_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Firewall id</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – a string that will be the displayed name/reference for this rule (optional)</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This may be one of “tcp”, “udp”, or “icmp”.</p></li>
<li><p><strong>start_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The start port where traffic to be allowed.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.FirewallRule.cidrs">
<em class="property">property </em><code class="sig-name descname">cidrs</code><a class="headerlink" href="#pulumi_civo.FirewallRule.cidrs" title="Permalink to this definition"></a></dt>
<dd><p>the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.FirewallRule.direction">
<em class="property">property </em><code class="sig-name descname">direction</code><a class="headerlink" href="#pulumi_civo.FirewallRule.direction" title="Permalink to this definition"></a></dt>
<dd><p>will this rule affect ingress traffic</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.FirewallRule.end_port">
<em class="property">property </em><code class="sig-name descname">end_port</code><a class="headerlink" href="#pulumi_civo.FirewallRule.end_port" title="Permalink to this definition"></a></dt>
<dd><p>The end port where traffic to be allowed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.FirewallRule.firewall_id">
<em class="property">property </em><code class="sig-name descname">firewall_id</code><a class="headerlink" href="#pulumi_civo.FirewallRule.firewall_id" title="Permalink to this definition"></a></dt>
<dd><p>The Firewall id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.FirewallRule.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_civo.FirewallRule.label" title="Permalink to this definition"></a></dt>
<dd><p>a string that will be the displayed name/reference for this rule (optional)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.FirewallRule.protocol">
<em class="property">property </em><code class="sig-name descname">protocol</code><a class="headerlink" href="#pulumi_civo.FirewallRule.protocol" title="Permalink to this definition"></a></dt>
<dd><p>This may be one of “tcp”, “udp”, or “icmp”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.FirewallRule.start_port">
<em class="property">property </em><code class="sig-name descname">start_port</code><a class="headerlink" href="#pulumi_civo.FirewallRule.start_port" title="Permalink to this definition"></a></dt>
<dd><p>The start port where traffic to be allowed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.FirewallRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.FirewallRule.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.FirewallRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.FirewallRule.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.GetDnsDomainNameResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetDnsDomainNameResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetDnsDomainNameResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getDnsDomainName.</p>
<dl class="py method">
<dt id="pulumi_civo.GetDnsDomainNameResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_civo.GetDnsDomainNameResult.id" title="Permalink to this definition"></a></dt>
<dd><p>A unique ID that can be used to identify and reference a domain.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetDnsDomainNameResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.GetDnsDomainNameResult.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the domain.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetDnsDomainRecordResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetDnsDomainRecordResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getDnsDomainRecord.</p>
<dl class="py method">
<dt id="pulumi_civo.GetDnsDomainRecordResult.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.account_id" title="Permalink to this definition"></a></dt>
<dd><p>The id account of the domain.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetDnsDomainRecordResult.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.created_at" title="Permalink to this definition"></a></dt>
<dd><p>The date when it was created in UTC format</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetDnsDomainRecordResult.domain_id">
<em class="property">property </em><code class="sig-name descname">domain_id</code><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.domain_id" title="Permalink to this definition"></a></dt>
<dd><p>The id of the domain</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetDnsDomainRecordResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetDnsDomainRecordResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.name" title="Permalink to this definition"></a></dt>
<dd><p>The portion before the domain name (e.g. www) or an &#64; for the apex/root domain (you cannot use an A record with an amex/root domain)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetDnsDomainRecordResult.priority">
<em class="property">property </em><code class="sig-name descname">priority</code><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.priority" title="Permalink to this definition"></a></dt>
<dd><p>The priority of the record.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetDnsDomainRecordResult.ttl">
<em class="property">property </em><code class="sig-name descname">ttl</code><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.ttl" title="Permalink to this definition"></a></dt>
<dd><p>How long caching DNS servers should cache this record.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetDnsDomainRecordResult.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.type" title="Permalink to this definition"></a></dt>
<dd><p>The choice of record type from A, CNAME, MX, SRV or TXT</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetDnsDomainRecordResult.updated_at">
<em class="property">property </em><code class="sig-name descname">updated_at</code><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.updated_at" title="Permalink to this definition"></a></dt>
<dd><p>The date when it was updated in UTC format</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetDnsDomainRecordResult.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.value" title="Permalink to this definition"></a></dt>
<dd><p>The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetInstanceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetInstanceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cpu_cores</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">firewall_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pseudo_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ram_mb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reverse_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sshkey_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetInstanceResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getInstance.</p>
<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.cpu_cores">
<em class="property">property </em><code class="sig-name descname">cpu_cores</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.cpu_cores" title="Permalink to this definition"></a></dt>
<dd><p>Total cpu of the inatance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.created_at" title="Permalink to this definition"></a></dt>
<dd><p>The date of creation of the instance</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.disk_gb">
<em class="property">property </em><code class="sig-name descname">disk_gb</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.disk_gb" title="Permalink to this definition"></a></dt>
<dd><p>The size of the disk.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.firewall_id">
<em class="property">property </em><code class="sig-name descname">firewall_id</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.firewall_id" title="Permalink to this definition"></a></dt>
<dd><p>The ID of the firewall used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.hostname">
<em class="property">property </em><code class="sig-name descname">hostname</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.hostname" title="Permalink to this definition"></a></dt>
<dd><p>The Instance hostname.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The ID of the Instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.initial_password">
<em class="property">property </em><code class="sig-name descname">initial_password</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.initial_password" title="Permalink to this definition"></a></dt>
<dd><p>Instance initial password</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.initial_user">
<em class="property">property </em><code class="sig-name descname">initial_user</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.initial_user" title="Permalink to this definition"></a></dt>
<dd><p>The name of the initial user created on the server.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.network_id">
<em class="property">property </em><code class="sig-name descname">network_id</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.network_id" title="Permalink to this definition"></a></dt>
<dd><p>This will be the ID of the network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.notes">
<em class="property">property </em><code class="sig-name descname">notes</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.notes" title="Permalink to this definition"></a></dt>
<dd><p>The notes of the instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.private_ip">
<em class="property">property </em><code class="sig-name descname">private_ip</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.private_ip" title="Permalink to this definition"></a></dt>
<dd><p>The private ip.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.pseudo_ip">
<em class="property">property </em><code class="sig-name descname">pseudo_ip</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.pseudo_ip" title="Permalink to this definition"></a></dt>
<dd><p>Is the ip that is used to route the public ip from the internet to the instance using NAT</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.public_ip">
<em class="property">property </em><code class="sig-name descname">public_ip</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.public_ip" title="Permalink to this definition"></a></dt>
<dd><p>The public ip.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.ram_mb">
<em class="property">property </em><code class="sig-name descname">ram_mb</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.ram_mb" title="Permalink to this definition"></a></dt>
<dd><p>Total ram of the instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.reverse_dns">
<em class="property">property </em><code class="sig-name descname">reverse_dns</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.reverse_dns" title="Permalink to this definition"></a></dt>
<dd><p>A fully qualified domain name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.script">
<em class="property">property </em><code class="sig-name descname">script</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.script" title="Permalink to this definition"></a></dt>
<dd><p>the contents of a script uploaded</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.size">
<em class="property">property </em><code class="sig-name descname">size</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.size" title="Permalink to this definition"></a></dt>
<dd><p>The name of the size.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.sshkey_id">
<em class="property">property </em><code class="sig-name descname">sshkey_id</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.sshkey_id" title="Permalink to this definition"></a></dt>
<dd><p>The ID SSH.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.status" title="Permalink to this definition"></a></dt>
<dd><p>The status of the instance</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.tags" title="Permalink to this definition"></a></dt>
<dd><p>An optional list of tags</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstanceResult.template">
<em class="property">property </em><code class="sig-name descname">template</code><a class="headerlink" href="#pulumi_civo.GetInstanceResult.template" title="Permalink to this definition"></a></dt>
<dd><p>The ID for the template to used to build the instance.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetInstancesResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getInstances.</p>
<dl class="py method">
<dt id="pulumi_civo.GetInstancesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_civo.GetInstancesResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetInstancesResult.instances">
<em class="property">property </em><code class="sig-name descname">instances</code><a class="headerlink" href="#pulumi_civo.GetInstancesResult.instances" title="Permalink to this definition"></a></dt>
<dd><p>A list of Instances satisfying any <code class="docutils literal notranslate"><span class="pre">filter</span></code> and <code class="docutils literal notranslate"><span class="pre">sort</span></code> criteria. Each instance has the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetInstancesSizeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetInstancesSizeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sizes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetInstancesSizeResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getInstancesSize.</p>
<dl class="py method">
<dt id="pulumi_civo.GetInstancesSizeResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_civo.GetInstancesSizeResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetKubernetesClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetKubernetesClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">api_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">built_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_entry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">installed_applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubeconfig</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_target_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ready</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_nodes_size</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getKubernetesCluster.</p>
<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.api_endpoint">
<em class="property">property </em><code class="sig-name descname">api_endpoint</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.api_endpoint" title="Permalink to this definition"></a></dt>
<dd><p>The base URL of the API server on the Kubernetes master node.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.applications">
<em class="property">property </em><code class="sig-name descname">applications</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.applications" title="Permalink to this definition"></a></dt>
<dd><p>A list of application installed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.built_at">
<em class="property">property </em><code class="sig-name descname">built_at</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.built_at" title="Permalink to this definition"></a></dt>
<dd><p>The date where the Kubernetes cluster was build.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.created_at" title="Permalink to this definition"></a></dt>
<dd><p>The date where the Kubernetes cluster was create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.dns_entry">
<em class="property">property </em><code class="sig-name descname">dns_entry</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.dns_entry" title="Permalink to this definition"></a></dt>
<dd><p>The unique dns entry for the cluster in this case point to the master.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.id" title="Permalink to this definition"></a></dt>
<dd><p>A unique ID that can be used to identify and reference a Kubernetes cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.installed_applications">
<em class="property">property </em><code class="sig-name descname">installed_applications</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.installed_applications" title="Permalink to this definition"></a></dt>
<dd><p>A unique ID that can be used to identify and reference a Kubernetes cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.instances">
<em class="property">property </em><code class="sig-name descname">instances</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.instances" title="Permalink to this definition"></a></dt>
<dd><p>In addition to the arguments provided, these additional attributes about the cluster’s default node instance are exported.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.kubeconfig">
<em class="property">property </em><code class="sig-name descname">kubeconfig</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.kubeconfig" title="Permalink to this definition"></a></dt>
<dd><p>A representation of the Kubernetes cluster’s kubeconfig in yaml format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.kubernetes_version">
<em class="property">property </em><code class="sig-name descname">kubernetes_version</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.kubernetes_version" title="Permalink to this definition"></a></dt>
<dd><p>The version of Kubernetes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.master_ip">
<em class="property">property </em><code class="sig-name descname">master_ip</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.master_ip" title="Permalink to this definition"></a></dt>
<dd><p>The Ip of the Kubernetes master node.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of your cluster,.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.num_target_nodes">
<em class="property">property </em><code class="sig-name descname">num_target_nodes</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.num_target_nodes" title="Permalink to this definition"></a></dt>
<dd><p>The size of the Kubernetes cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.status" title="Permalink to this definition"></a></dt>
<dd><p>The status of Kubernetes cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ready</span></code> -If the Kubernetes cluster is ready.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.tags" title="Permalink to this definition"></a></dt>
<dd><p>The tag of the instances</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetKubernetesClusterResult.target_nodes_size">
<em class="property">property </em><code class="sig-name descname">target_nodes_size</code><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.target_nodes_size" title="Permalink to this definition"></a></dt>
<dd><p>The size of each node.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetKubernetesVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetKubernetesVersionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">versions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetKubernetesVersionResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getKubernetesVersion.</p>
<dl class="py method">
<dt id="pulumi_civo.GetKubernetesVersionResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_civo.GetKubernetesVersionResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetLoadBalancerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetLoadBalancerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">backends</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fail_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_invalid_backend_tls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_conns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_request_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getLoadBalancer.</p>
<dl class="py method">
<dt id="pulumi_civo.GetLoadBalancerResult.backends">
<em class="property">property </em><code class="sig-name descname">backends</code><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.backends" title="Permalink to this definition"></a></dt>
<dd><p>A list of backend instances</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetLoadBalancerResult.fail_timeout">
<em class="property">property </em><code class="sig-name descname">fail_timeout</code><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.fail_timeout" title="Permalink to this definition"></a></dt>
<dd><p>The wait time until the backend is marked as a failure</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetLoadBalancerResult.health_check_path">
<em class="property">property </em><code class="sig-name descname">health_check_path</code><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.health_check_path" title="Permalink to this definition"></a></dt>
<dd><p>The path to check the health of the backend</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetLoadBalancerResult.hostname">
<em class="property">property </em><code class="sig-name descname">hostname</code><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.hostname" title="Permalink to this definition"></a></dt>
<dd><p>The hostname of the Load Balancer</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetLoadBalancerResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The ID of the Load Balancer</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetLoadBalancerResult.ignore_invalid_backend_tls">
<em class="property">property </em><code class="sig-name descname">ignore_invalid_backend_tls</code><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.ignore_invalid_backend_tls" title="Permalink to this definition"></a></dt>
<dd><p>Should self-signed/invalid certificates be ignored from the backend servers</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetLoadBalancerResult.max_conns">
<em class="property">property </em><code class="sig-name descname">max_conns</code><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.max_conns" title="Permalink to this definition"></a></dt>
<dd><p>How many concurrent connections can each backend handle</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetLoadBalancerResult.max_request_size">
<em class="property">property </em><code class="sig-name descname">max_request_size</code><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.max_request_size" title="Permalink to this definition"></a></dt>
<dd><p>The max request size set in the configuration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetLoadBalancerResult.policy">
<em class="property">property </em><code class="sig-name descname">policy</code><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.policy" title="Permalink to this definition"></a></dt>
<dd><p>The policy set in the Load Balancer</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetLoadBalancerResult.port">
<em class="property">property </em><code class="sig-name descname">port</code><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.port" title="Permalink to this definition"></a></dt>
<dd><p>The port set in the configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetLoadBalancerResult.protocol">
<em class="property">property </em><code class="sig-name descname">protocol</code><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.protocol" title="Permalink to this definition"></a></dt>
<dd><p>The protocol used in the configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetLoadBalancerResult.tls_certificate">
<em class="property">property </em><code class="sig-name descname">tls_certificate</code><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.tls_certificate" title="Permalink to this definition"></a></dt>
<dd><p>If is set will be returned</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetLoadBalancerResult.tls_key">
<em class="property">property </em><code class="sig-name descname">tls_key</code><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.tls_key" title="Permalink to this definition"></a></dt>
<dd><p>If is set will be returned</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetNetworkResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetNetworkResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getNetwork.</p>
<dl class="py method">
<dt id="pulumi_civo.GetNetworkResult.cidr">
<em class="property">property </em><code class="sig-name descname">cidr</code><a class="headerlink" href="#pulumi_civo.GetNetworkResult.cidr" title="Permalink to this definition"></a></dt>
<dd><p>The block ip assigned to the network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetNetworkResult.default">
<em class="property">property </em><code class="sig-name descname">default</code><a class="headerlink" href="#pulumi_civo.GetNetworkResult.default" title="Permalink to this definition"></a></dt>
<dd><p>If is the default network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetNetworkResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_civo.GetNetworkResult.id" title="Permalink to this definition"></a></dt>
<dd><p>A unique ID that can be used to identify and reference a Network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetNetworkResult.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_civo.GetNetworkResult.label" title="Permalink to this definition"></a></dt>
<dd><p>The label used in the configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetNetworkResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.GetNetworkResult.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetNetworkResult.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_civo.GetNetworkResult.region" title="Permalink to this definition"></a></dt>
<dd><p>The region where the network was create.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">completed_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cron_timing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">next_execution</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requested_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">safe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetSnapshotResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getSnapshot.</p>
<dl class="py method">
<dt id="pulumi_civo.GetSnapshotResult.completed_at">
<em class="property">property </em><code class="sig-name descname">completed_at</code><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.completed_at" title="Permalink to this definition"></a></dt>
<dd><p>The date where the snapshot was completed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetSnapshotResult.cron_timing">
<em class="property">property </em><code class="sig-name descname">cron_timing</code><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.cron_timing" title="Permalink to this definition"></a></dt>
<dd><p>A string with the cron format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetSnapshotResult.hostname">
<em class="property">property </em><code class="sig-name descname">hostname</code><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.hostname" title="Permalink to this definition"></a></dt>
<dd><p>The hostname of the instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetSnapshotResult.instance_id">
<em class="property">property </em><code class="sig-name descname">instance_id</code><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.instance_id" title="Permalink to this definition"></a></dt>
<dd><p>The ID of the Instance from which the snapshot was be taken.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetSnapshotResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetSnapshotResult.next_execution">
<em class="property">property </em><code class="sig-name descname">next_execution</code><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.next_execution" title="Permalink to this definition"></a></dt>
<dd><p>if cron was define this date will be the next execution date.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetSnapshotResult.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.region" title="Permalink to this definition"></a></dt>
<dd><p>The region where the snapshot was take.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetSnapshotResult.requested_at">
<em class="property">property </em><code class="sig-name descname">requested_at</code><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.requested_at" title="Permalink to this definition"></a></dt>
<dd><p>The date where the snapshot was requested.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetSnapshotResult.safe">
<em class="property">property </em><code class="sig-name descname">safe</code><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.safe" title="Permalink to this definition"></a></dt>
<dd><p>If is <code class="docutils literal notranslate"><span class="pre">true</span></code> the instance will be shut down during the snapshot if id <code class="docutils literal notranslate"><span class="pre">false</span></code> them not.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetSnapshotResult.size_gb">
<em class="property">property </em><code class="sig-name descname">size_gb</code><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.size_gb" title="Permalink to this definition"></a></dt>
<dd><p>The size of the snapshot in GB.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetSnapshotResult.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.state" title="Permalink to this definition"></a></dt>
<dd><p>The status of the snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetSnapshotResult.template_id">
<em class="property">property </em><code class="sig-name descname">template_id</code><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.template_id" title="Permalink to this definition"></a></dt>
<dd><p>The template id.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetSshKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetSshKeyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetSshKeyResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getSshKey.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetTemplateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetTemplateResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">templates</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetTemplateResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getTemplate.</p>
<dl class="py method">
<dt id="pulumi_civo.GetTemplateResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_civo.GetTemplateResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">bootable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mount_point</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_gb</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetVolumeResult" title="Permalink to this definition"></a></dt>
<dd><p>A collection of values returned by getVolume.</p>
<dl class="py method">
<dt id="pulumi_civo.GetVolumeResult.bootable">
<em class="property">property </em><code class="sig-name descname">bootable</code><a class="headerlink" href="#pulumi_civo.GetVolumeResult.bootable" title="Permalink to this definition"></a></dt>
<dd><p>if is bootable or not.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetVolumeResult.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_civo.GetVolumeResult.created_at" title="Permalink to this definition"></a></dt>
<dd><p>The date of the creation of the volume.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetVolumeResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_civo.GetVolumeResult.id" title="Permalink to this definition"></a></dt>
<dd><p>The unique identifier for the volume.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetVolumeResult.mount_point">
<em class="property">property </em><code class="sig-name descname">mount_point</code><a class="headerlink" href="#pulumi_civo.GetVolumeResult.mount_point" title="Permalink to this definition"></a></dt>
<dd><p>The mount point of the volume.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetVolumeResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.GetVolumeResult.name" title="Permalink to this definition"></a></dt>
<dd><p>Name of the volume.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.GetVolumeResult.size_gb">
<em class="property">property </em><code class="sig-name descname">size_gb</code><a class="headerlink" href="#pulumi_civo.GetVolumeResult.size_gb" title="Permalink to this definition"></a></dt>
<dd><p>The size of the volume.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">firewall_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_user</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip_required</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reverse_dns</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sshkey_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Instance" title="Permalink to this definition"></a></dt>
<dd><p>Provides a Civo Instance resource. This can be used to create,
modify, and delete Instances.</p>
<p>Instances can be imported using the instance <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import civo:index/instance:Instance myintance 18bd98ad-1b6e-4f87-b48f-e690b4fd7413
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>firewall_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all).</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Instance hostname.</p></li>
<li><p><strong>initial_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the initial user created on the server (optional; this will default to the template’s default_username and fallback to civo).</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This must be the ID of the network from the network listing (optional; default network used when not specified).</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Add some notes to the instance.</p></li>
<li><p><strong>public_ip_required</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This should be either false, true or <code class="docutils literal notranslate"><span class="pre">move_ip_from:intances_id</span></code>.</p></li>
<li><p><strong>reverse_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A fully qualified domain name that should be used as the instance’s IP’s reverse DNS (optional, uses the hostname if unspecified).</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the size, from the current list, e.g. g2.small (required).</p></li>
<li><p><strong>sshkey_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn’t provided a random password will be set and returned in the initial_password field).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – An optional list of tags, represented as a key, value pair.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the template to use to build the instance.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_civo.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_cores</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_gb</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">firewall_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_user</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pseudo_ip</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip_required</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ram_mb</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reverse_dns</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sshkey_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_civo.Instance" title="pulumi_civo.Instance">Instance</a><a class="headerlink" href="#pulumi_civo.Instance.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cpu_cores</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Total cpu of the inatance.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date of creation of the instance</p></li>
<li><p><strong>disk_gb</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The size of the disk.</p></li>
<li><p><strong>firewall_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all).</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Instance hostname.</p></li>
<li><p><strong>initial_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance initial password</p></li>
<li><p><strong>initial_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the initial user created on the server (optional; this will default to the template’s default_username and fallback to civo).</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This must be the ID of the network from the network listing (optional; default network used when not specified).</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Add some notes to the instance.</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private ip.</p></li>
<li><p><strong>pseudo_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Is the ip that is used to route the public ip from the internet to the instance using NAT</p></li>
<li><p><strong>public_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public ip.</p></li>
<li><p><strong>public_ip_required</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This should be either false, true or <code class="docutils literal notranslate"><span class="pre">move_ip_from:intances_id</span></code>.</p></li>
<li><p><strong>ram_mb</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Total ram of the instance.</p></li>
<li><p><strong>reverse_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A fully qualified domain name that should be used as the instance’s IP’s reverse DNS (optional, uses the hostname if unspecified).</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the size, from the current list, e.g. g2.small (required).</p></li>
<li><p><strong>sshkey_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn’t provided a random password will be set and returned in the initial_password field).</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the instance</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – An optional list of tags, represented as a key, value pair.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the template to use to build the instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.cpu_cores">
<em class="property">property </em><code class="sig-name descname">cpu_cores</code><a class="headerlink" href="#pulumi_civo.Instance.cpu_cores" title="Permalink to this definition"></a></dt>
<dd><p>Total cpu of the inatance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_civo.Instance.created_at" title="Permalink to this definition"></a></dt>
<dd><p>The date of creation of the instance</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.disk_gb">
<em class="property">property </em><code class="sig-name descname">disk_gb</code><a class="headerlink" href="#pulumi_civo.Instance.disk_gb" title="Permalink to this definition"></a></dt>
<dd><p>The size of the disk.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.firewall_id">
<em class="property">property </em><code class="sig-name descname">firewall_id</code><a class="headerlink" href="#pulumi_civo.Instance.firewall_id" title="Permalink to this definition"></a></dt>
<dd><p>The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.hostname">
<em class="property">property </em><code class="sig-name descname">hostname</code><a class="headerlink" href="#pulumi_civo.Instance.hostname" title="Permalink to this definition"></a></dt>
<dd><p>The Instance hostname.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.initial_password">
<em class="property">property </em><code class="sig-name descname">initial_password</code><a class="headerlink" href="#pulumi_civo.Instance.initial_password" title="Permalink to this definition"></a></dt>
<dd><p>Instance initial password</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.initial_user">
<em class="property">property </em><code class="sig-name descname">initial_user</code><a class="headerlink" href="#pulumi_civo.Instance.initial_user" title="Permalink to this definition"></a></dt>
<dd><p>The name of the initial user created on the server (optional; this will default to the template’s default_username and fallback to civo).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.network_id">
<em class="property">property </em><code class="sig-name descname">network_id</code><a class="headerlink" href="#pulumi_civo.Instance.network_id" title="Permalink to this definition"></a></dt>
<dd><p>This must be the ID of the network from the network listing (optional; default network used when not specified).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.notes">
<em class="property">property </em><code class="sig-name descname">notes</code><a class="headerlink" href="#pulumi_civo.Instance.notes" title="Permalink to this definition"></a></dt>
<dd><p>Add some notes to the instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.private_ip">
<em class="property">property </em><code class="sig-name descname">private_ip</code><a class="headerlink" href="#pulumi_civo.Instance.private_ip" title="Permalink to this definition"></a></dt>
<dd><p>The private ip.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.pseudo_ip">
<em class="property">property </em><code class="sig-name descname">pseudo_ip</code><a class="headerlink" href="#pulumi_civo.Instance.pseudo_ip" title="Permalink to this definition"></a></dt>
<dd><p>Is the ip that is used to route the public ip from the internet to the instance using NAT</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.public_ip">
<em class="property">property </em><code class="sig-name descname">public_ip</code><a class="headerlink" href="#pulumi_civo.Instance.public_ip" title="Permalink to this definition"></a></dt>
<dd><p>The public ip.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.public_ip_required">
<em class="property">property </em><code class="sig-name descname">public_ip_required</code><a class="headerlink" href="#pulumi_civo.Instance.public_ip_required" title="Permalink to this definition"></a></dt>
<dd><p>This should be either false, true or <code class="docutils literal notranslate"><span class="pre">move_ip_from:intances_id</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.ram_mb">
<em class="property">property </em><code class="sig-name descname">ram_mb</code><a class="headerlink" href="#pulumi_civo.Instance.ram_mb" title="Permalink to this definition"></a></dt>
<dd><p>Total ram of the instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.reverse_dns">
<em class="property">property </em><code class="sig-name descname">reverse_dns</code><a class="headerlink" href="#pulumi_civo.Instance.reverse_dns" title="Permalink to this definition"></a></dt>
<dd><p>A fully qualified domain name that should be used as the instance’s IP’s reverse DNS (optional, uses the hostname if unspecified).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.script">
<em class="property">property </em><code class="sig-name descname">script</code><a class="headerlink" href="#pulumi_civo.Instance.script" title="Permalink to this definition"></a></dt>
<dd><p>the contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.size">
<em class="property">property </em><code class="sig-name descname">size</code><a class="headerlink" href="#pulumi_civo.Instance.size" title="Permalink to this definition"></a></dt>
<dd><p>The name of the size, from the current list, e.g. g2.small (required).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.sshkey_id">
<em class="property">property </em><code class="sig-name descname">sshkey_id</code><a class="headerlink" href="#pulumi_civo.Instance.sshkey_id" title="Permalink to this definition"></a></dt>
<dd><p>The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn’t provided a random password will be set and returned in the initial_password field).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_civo.Instance.status" title="Permalink to this definition"></a></dt>
<dd><p>The status of the instance</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_civo.Instance.tags" title="Permalink to this definition"></a></dt>
<dd><p>An optional list of tags, represented as a key, value pair.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.template">
<em class="property">property </em><code class="sig-name descname">template</code><a class="headerlink" href="#pulumi_civo.Instance.template" title="Permalink to this definition"></a></dt>
<dd><p>The ID for the template to use to build the instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Instance.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Instance.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.KubernetesCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">KubernetesCluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">applications</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_target_nodes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_nodes_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.KubernetesCluster" title="Permalink to this definition"></a></dt>
<dd><p>Then the Kubernetes cluster can be imported using the cluster’s <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import civo:index/kubernetesCluster:KubernetesCluster my-cluster 1b8b2100-0e9f-4e8f-ad78-9eb578c2a0af
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>applications</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma separated list of applications to install. Spaces within application names are fine, but shouldn’t be either side of the comma. If you want to remove a default installed application, prefix it with a ‘-‘, e.g. -traefik</p></li>
<li><p><strong>kubernetes_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of k3s to install (The default is currently the latest available).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the Kubernetes cluster.</p></li>
<li><p><strong>num_target_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of instances to create (The default at the time of writing is 3).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A space separated list of tags, to be used freely as required.</p></li>
<li><p><strong>target_nodes_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The size of each node (The default is currently g2.small)</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_endpoint</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">applications</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">built_at</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_entry</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">installed_applications</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>KubernetesClusterInstalledApplicationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>KubernetesClusterInstalledApplicationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>KubernetesClusterInstalledApplicationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>KubernetesClusterInstalledApplicationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>KubernetesClusterInstanceArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>KubernetesClusterInstanceArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>KubernetesClusterInstanceArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>KubernetesClusterInstanceArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubeconfig</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ip</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_target_nodes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ready</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_nodes_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_civo.KubernetesCluster" title="pulumi_civo.KubernetesCluster">KubernetesCluster</a><a class="headerlink" href="#pulumi_civo.KubernetesCluster.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing KubernetesCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base URL of the API server on the Kubernetes master node.</p></li>
<li><p><strong>applications</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma separated list of applications to install. Spaces within application names are fine, but shouldn’t be either side of the comma. If you want to remove a default installed application, prefix it with a ‘-‘, e.g. -traefik</p></li>
<li><p><strong>built_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date where the Kubernetes cluster was build.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date where the Kubernetes cluster was create.</p></li>
<li><p><strong>dns_entry</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique dns entry for the cluster in this case point to the master.</p></li>
<li><p><strong>installed_applications</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KubernetesClusterInstalledApplicationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A unique ID that can be used to identify and reference a Kubernetes cluster.</p></li>
<li><p><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KubernetesClusterInstanceArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – In addition to the arguments provided, these additional attributes about the cluster’s default node instance are exported.</p></li>
<li><p><strong>kubeconfig</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A representation of the Kubernetes cluster’s kubeconfig in yaml format.</p></li>
<li><p><strong>kubernetes_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of k3s to install (The default is currently the latest available).</p></li>
<li><p><strong>master_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Ip of the Kubernetes master node.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the Kubernetes cluster.</p></li>
<li><p><strong>num_target_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of instances to create (The default at the time of writing is 3).</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of Kubernetes cluster.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `ready` -If the Kubernetes cluster is ready.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A space separated list of tags, to be used freely as required.</p></li>
<li><p><strong>target_nodes_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The size of each node (The default is currently g2.small)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.api_endpoint">
<em class="property">property </em><code class="sig-name descname">api_endpoint</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.api_endpoint" title="Permalink to this definition"></a></dt>
<dd><p>The base URL of the API server on the Kubernetes master node.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.applications">
<em class="property">property </em><code class="sig-name descname">applications</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.applications" title="Permalink to this definition"></a></dt>
<dd><p>A comma separated list of applications to install. Spaces within application names are fine, but shouldn’t be either side of the comma. If you want to remove a default installed application, prefix it with a ‘-‘, e.g. -traefik</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.built_at">
<em class="property">property </em><code class="sig-name descname">built_at</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.built_at" title="Permalink to this definition"></a></dt>
<dd><p>The date where the Kubernetes cluster was build.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.created_at" title="Permalink to this definition"></a></dt>
<dd><p>The date where the Kubernetes cluster was create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.dns_entry">
<em class="property">property </em><code class="sig-name descname">dns_entry</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.dns_entry" title="Permalink to this definition"></a></dt>
<dd><p>The unique dns entry for the cluster in this case point to the master.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.installed_applications">
<em class="property">property </em><code class="sig-name descname">installed_applications</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.installed_applications" title="Permalink to this definition"></a></dt>
<dd><p>A unique ID that can be used to identify and reference a Kubernetes cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.instances">
<em class="property">property </em><code class="sig-name descname">instances</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.instances" title="Permalink to this definition"></a></dt>
<dd><p>In addition to the arguments provided, these additional attributes about the cluster’s default node instance are exported.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.kubeconfig">
<em class="property">property </em><code class="sig-name descname">kubeconfig</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.kubeconfig" title="Permalink to this definition"></a></dt>
<dd><p>A representation of the Kubernetes cluster’s kubeconfig in yaml format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.kubernetes_version">
<em class="property">property </em><code class="sig-name descname">kubernetes_version</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.kubernetes_version" title="Permalink to this definition"></a></dt>
<dd><p>The version of k3s to install (The default is currently the latest available).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.master_ip">
<em class="property">property </em><code class="sig-name descname">master_ip</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.master_ip" title="Permalink to this definition"></a></dt>
<dd><p>The Ip of the Kubernetes master node.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.name" title="Permalink to this definition"></a></dt>
<dd><p>A name for the Kubernetes cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.num_target_nodes">
<em class="property">property </em><code class="sig-name descname">num_target_nodes</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.num_target_nodes" title="Permalink to this definition"></a></dt>
<dd><p>The number of instances to create (The default at the time of writing is 3).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.status" title="Permalink to this definition"></a></dt>
<dd><p>The status of Kubernetes cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ready</span></code> -If the Kubernetes cluster is ready.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.tags" title="Permalink to this definition"></a></dt>
<dd><p>A space separated list of tags, to be used freely as required.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.target_nodes_size">
<em class="property">property </em><code class="sig-name descname">target_nodes_size</code><a class="headerlink" href="#pulumi_civo.KubernetesCluster.target_nodes_size" title="Permalink to this definition"></a></dt>
<dd><p>The size of each node (The default is currently g2.small)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.KubernetesCluster.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.KubernetesCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.KubernetesCluster.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.LoadBalancer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">LoadBalancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backends</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>LoadBalancerBackendArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>LoadBalancerBackendArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>LoadBalancerBackendArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>LoadBalancerBackendArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fail_timeout</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_invalid_backend_tls</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_conns</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_request_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_certificate</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.LoadBalancer" title="Permalink to this definition"></a></dt>
<dd><p>Create a LoadBalancer resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType[‘LoadBalancerBackendArgs’]]]] backends: a list of backend instances, each containing an instance_id, protocol (http or https) and port
:param pulumi.Input[int] fail_timeout: how long to wait in seconds before determining a backend has failed, defaults to 30
:param pulumi.Input[str] health_check_path: what URL should be used on the backends to determine if it’s OK (2xx/3xx status), defaults to /
:param pulumi.Input[str] hostname: the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if</p>
<blockquote>
<div><p>blank)</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ignore_invalid_backend_tls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – should self-signed/invalid certificates be ignored from the backend servers, defaults to true</p></li>
<li><p><strong>max_conns</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – how many concurrent connections can each backend handle, defaults to 10</p></li>
<li><p><strong>max_request_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – the size in megabytes of the maximum request content that will be accepted, defaults to 20</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
same backend), default is random</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
(commonly 80 for HTTP or 443 for HTTPS)</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – either http or https. If you specify https then you must also provide the next two fields, the default is http</p></li>
<li><p><strong>tls_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format</p></li>
<li><p><strong>tls_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – if your protocol is https then you should send the TLS private key in Base64-encoded PEM format</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backends</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>LoadBalancerBackendArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>LoadBalancerBackendArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>LoadBalancerBackendArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>LoadBalancerBackendArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fail_timeout</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_invalid_backend_tls</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_conns</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_request_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_certificate</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_civo.LoadBalancer" title="pulumi_civo.LoadBalancer">LoadBalancer</a><a class="headerlink" href="#pulumi_civo.LoadBalancer.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing LoadBalancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backends</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LoadBalancerBackendArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – a list of backend instances, each containing an instance_id, protocol (http or https) and port</p></li>
<li><p><strong>fail_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – how long to wait in seconds before determining a backend has failed, defaults to 30</p></li>
<li><p><strong>health_check_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – what URL should be used on the backends to determine if it’s OK (2xx/3xx status), defaults to /</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if
blank)</p></li>
<li><p><strong>ignore_invalid_backend_tls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – should self-signed/invalid certificates be ignored from the backend servers, defaults to true</p></li>
<li><p><strong>max_conns</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – how many concurrent connections can each backend handle, defaults to 10</p></li>
<li><p><strong>max_request_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – the size in megabytes of the maximum request content that will be accepted, defaults to 20</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
same backend), default is random</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
(commonly 80 for HTTP or 443 for HTTPS)</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – either http or https. If you specify https then you must also provide the next two fields, the default is http</p></li>
<li><p><strong>tls_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format</p></li>
<li><p><strong>tls_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – if your protocol is https then you should send the TLS private key in Base64-encoded PEM format</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.backends">
<em class="property">property </em><code class="sig-name descname">backends</code><a class="headerlink" href="#pulumi_civo.LoadBalancer.backends" title="Permalink to this definition"></a></dt>
<dd><p>a list of backend instances, each containing an instance_id, protocol (http or https) and port</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.fail_timeout">
<em class="property">property </em><code class="sig-name descname">fail_timeout</code><a class="headerlink" href="#pulumi_civo.LoadBalancer.fail_timeout" title="Permalink to this definition"></a></dt>
<dd><p>how long to wait in seconds before determining a backend has failed, defaults to 30</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.health_check_path">
<em class="property">property </em><code class="sig-name descname">health_check_path</code><a class="headerlink" href="#pulumi_civo.LoadBalancer.health_check_path" title="Permalink to this definition"></a></dt>
<dd><p>what URL should be used on the backends to determine if it’s OK (2xx/3xx status), defaults to /</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.hostname">
<em class="property">property </em><code class="sig-name descname">hostname</code><a class="headerlink" href="#pulumi_civo.LoadBalancer.hostname" title="Permalink to this definition"></a></dt>
<dd><p>the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if
blank)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.ignore_invalid_backend_tls">
<em class="property">property </em><code class="sig-name descname">ignore_invalid_backend_tls</code><a class="headerlink" href="#pulumi_civo.LoadBalancer.ignore_invalid_backend_tls" title="Permalink to this definition"></a></dt>
<dd><p>should self-signed/invalid certificates be ignored from the backend servers, defaults to true</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.max_conns">
<em class="property">property </em><code class="sig-name descname">max_conns</code><a class="headerlink" href="#pulumi_civo.LoadBalancer.max_conns" title="Permalink to this definition"></a></dt>
<dd><p>how many concurrent connections can each backend handle, defaults to 10</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.max_request_size">
<em class="property">property </em><code class="sig-name descname">max_request_size</code><a class="headerlink" href="#pulumi_civo.LoadBalancer.max_request_size" title="Permalink to this definition"></a></dt>
<dd><p>the size in megabytes of the maximum request content that will be accepted, defaults to 20</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.policy">
<em class="property">property </em><code class="sig-name descname">policy</code><a class="headerlink" href="#pulumi_civo.LoadBalancer.policy" title="Permalink to this definition"></a></dt>
<dd><p>one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
same backend), default is random</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.port">
<em class="property">property </em><code class="sig-name descname">port</code><a class="headerlink" href="#pulumi_civo.LoadBalancer.port" title="Permalink to this definition"></a></dt>
<dd><p>you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
(commonly 80 for HTTP or 443 for HTTPS)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.protocol">
<em class="property">property </em><code class="sig-name descname">protocol</code><a class="headerlink" href="#pulumi_civo.LoadBalancer.protocol" title="Permalink to this definition"></a></dt>
<dd><p>either http or https. If you specify https then you must also provide the next two fields, the default is http</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.tls_certificate">
<em class="property">property </em><code class="sig-name descname">tls_certificate</code><a class="headerlink" href="#pulumi_civo.LoadBalancer.tls_certificate" title="Permalink to this definition"></a></dt>
<dd><p>if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.tls_key">
<em class="property">property </em><code class="sig-name descname">tls_key</code><a class="headerlink" href="#pulumi_civo.LoadBalancer.tls_key" title="Permalink to this definition"></a></dt>
<dd><p>if your protocol is https then you should send the TLS private key in Base64-encoded PEM format</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.LoadBalancer.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.LoadBalancer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.LoadBalancer.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.Network">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">Network</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Network" title="Permalink to this definition"></a></dt>
<dd><p>Provides a Civo Network resource. This can be used to create,
modify, and delete Networks.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">custom_net</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;customNet&quot;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s2">&quot;test_network&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Firewalls can be imported using the firewall <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import civo:index/network:Network custom_net b8ecd2ab-2267-4a5e-8692-cbf1d32583e3
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Network label</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_civo.Network.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_civo.Network" title="pulumi_civo.Network">Network</a><a class="headerlink" href="#pulumi_civo.Network.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Network resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The block ip assigned to the network.</p></li>
<li><p><strong>default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If is the default network.</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Network label</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where the network was create.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Network.cidr">
<em class="property">property </em><code class="sig-name descname">cidr</code><a class="headerlink" href="#pulumi_civo.Network.cidr" title="Permalink to this definition"></a></dt>
<dd><p>The block ip assigned to the network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Network.default">
<em class="property">property </em><code class="sig-name descname">default</code><a class="headerlink" href="#pulumi_civo.Network.default" title="Permalink to this definition"></a></dt>
<dd><p>If is the default network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Network.label">
<em class="property">property </em><code class="sig-name descname">label</code><a class="headerlink" href="#pulumi_civo.Network.label" title="Permalink to this definition"></a></dt>
<dd><p>The Network label</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Network.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.Network.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the network.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Network.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_civo.Network.region" title="Permalink to this definition"></a></dt>
<dd><p>The region where the network was create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Network.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Network.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.Network.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Network.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Provider" title="Permalink to this definition"></a></dt>
<dd><p>The provider type for the civo package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_civo.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Provider.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Provider.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.Snapshot">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">Snapshot</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cron_timing</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">safe</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Snapshot" title="Permalink to this definition"></a></dt>
<dd><p>Provides a resource which can be used to create a snapshot from an existing Civo Instance.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">myinstance_backup</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">Snapshot</span><span class="p">(</span><span class="s2">&quot;myinstance-backup&quot;</span><span class="p">,</span> <span class="n">instance_id</span><span class="o">=</span><span class="n">civo_instance</span><span class="p">[</span><span class="s2">&quot;myinstance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>Instance Snapshots can be imported using the <code class="docutils literal notranslate"><span class="pre">snapshot</span> <span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import civo:index/snapshot:Snapshot myinstance-backup 4cc87851-e1d0-4270-822a-b36d28c7a77f
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cron_timing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If a valid cron string is passed, the snapshot will be saved as an automated snapshot 
continuing to automatically update based on the schedule of the cron sequence provided
The default is nil meaning the snapshot will be saved as a one-off snapshot.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Instance from which the snapshot will be taken.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the instance snapshot.</p></li>
<li><p><strong>safe</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code> the instance will be shut down during the snapshot to ensure all files 
are in a consistent state (e.g. database tables aren’t in the middle of being optimised
and hence risking corruption). The default is <code class="docutils literal notranslate"><span class="pre">false</span></code> so you experience no interruption
of service, but a small risk of corruption.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_civo.Snapshot.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">completed_at</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cron_timing</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">next_execution</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requested_at</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">safe</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_gb</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_civo.Snapshot" title="pulumi_civo.Snapshot">Snapshot</a><a class="headerlink" href="#pulumi_civo.Snapshot.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Snapshot resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>completed_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date where the snapshot was completed.</p></li>
<li><p><strong>cron_timing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If a valid cron string is passed, the snapshot will be saved as an automated snapshot 
continuing to automatically update based on the schedule of the cron sequence provided
The default is nil meaning the snapshot will be saved as a one-off snapshot.</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname of the instance.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Instance from which the snapshot will be taken.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the instance snapshot.</p></li>
<li><p><strong>next_execution</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – if cron was define this date will be the next execution date.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where the snapshot was take.</p></li>
<li><p><strong>requested_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date where the snapshot was requested.</p></li>
<li><p><strong>safe</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code> the instance will be shut down during the snapshot to ensure all files 
are in a consistent state (e.g. database tables aren’t in the middle of being optimised
and hence risking corruption). The default is <code class="docutils literal notranslate"><span class="pre">false</span></code> so you experience no interruption
of service, but a small risk of corruption.</p></li>
<li><p><strong>size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The size of the snapshot in GB.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the snapshot.</p></li>
<li><p><strong>template_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The template id.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.completed_at">
<em class="property">property </em><code class="sig-name descname">completed_at</code><a class="headerlink" href="#pulumi_civo.Snapshot.completed_at" title="Permalink to this definition"></a></dt>
<dd><p>The date where the snapshot was completed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.cron_timing">
<em class="property">property </em><code class="sig-name descname">cron_timing</code><a class="headerlink" href="#pulumi_civo.Snapshot.cron_timing" title="Permalink to this definition"></a></dt>
<dd><p>If a valid cron string is passed, the snapshot will be saved as an automated snapshot 
continuing to automatically update based on the schedule of the cron sequence provided
The default is nil meaning the snapshot will be saved as a one-off snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.hostname">
<em class="property">property </em><code class="sig-name descname">hostname</code><a class="headerlink" href="#pulumi_civo.Snapshot.hostname" title="Permalink to this definition"></a></dt>
<dd><p>The hostname of the instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.instance_id">
<em class="property">property </em><code class="sig-name descname">instance_id</code><a class="headerlink" href="#pulumi_civo.Snapshot.instance_id" title="Permalink to this definition"></a></dt>
<dd><p>The ID of the Instance from which the snapshot will be taken.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.Snapshot.name" title="Permalink to this definition"></a></dt>
<dd><p>A name for the instance snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.next_execution">
<em class="property">property </em><code class="sig-name descname">next_execution</code><a class="headerlink" href="#pulumi_civo.Snapshot.next_execution" title="Permalink to this definition"></a></dt>
<dd><p>if cron was define this date will be the next execution date.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_civo.Snapshot.region" title="Permalink to this definition"></a></dt>
<dd><p>The region where the snapshot was take.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.requested_at">
<em class="property">property </em><code class="sig-name descname">requested_at</code><a class="headerlink" href="#pulumi_civo.Snapshot.requested_at" title="Permalink to this definition"></a></dt>
<dd><p>The date where the snapshot was requested.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.safe">
<em class="property">property </em><code class="sig-name descname">safe</code><a class="headerlink" href="#pulumi_civo.Snapshot.safe" title="Permalink to this definition"></a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code> the instance will be shut down during the snapshot to ensure all files 
are in a consistent state (e.g. database tables aren’t in the middle of being optimised
and hence risking corruption). The default is <code class="docutils literal notranslate"><span class="pre">false</span></code> so you experience no interruption
of service, but a small risk of corruption.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.size_gb">
<em class="property">property </em><code class="sig-name descname">size_gb</code><a class="headerlink" href="#pulumi_civo.Snapshot.size_gb" title="Permalink to this definition"></a></dt>
<dd><p>The size of the snapshot in GB.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_civo.Snapshot.state" title="Permalink to this definition"></a></dt>
<dd><p>The status of the snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.template_id">
<em class="property">property </em><code class="sig-name descname">template_id</code><a class="headerlink" href="#pulumi_civo.Snapshot.template_id" title="Permalink to this definition"></a></dt>
<dd><p>The template id.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Snapshot.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.Snapshot.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Snapshot.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.SshKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">SshKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.SshKey" title="Permalink to this definition"></a></dt>
<dd><p>Provides a Civo SSH key resource to allow you to manage SSH
keys for Instance access. Keys created with this resource
can be referenced in your instance configuration via their ID.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">my_user</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">SshKey</span><span class="p">(</span><span class="s2">&quot;my-user&quot;</span><span class="p">,</span> <span class="n">public_key</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;~/.ssh/id_rsa.pub&quot;</span><span class="p">))</span>
</pre></div>
</div>
<p>SSH Keys can be imported using the <code class="docutils literal notranslate"><span class="pre">ssh</span> <span class="pre">key</span> <span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import civo:index/sshKey:SshKey mykey 87ca2ee4-57d3-4420-b9b6-411b0b4b2a0e
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSH key for identification</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key. If this is a file, it
can be read using the file interpolation function.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_civo.SshKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_civo.SshKey" title="pulumi_civo.SshKey">SshKey</a><a class="headerlink" href="#pulumi_civo.SshKey.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing SshKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fingerprint of the SSH key</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSH key for identification</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key. If this is a file, it
can be read using the file interpolation function.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.SshKey.fingerprint">
<em class="property">property </em><code class="sig-name descname">fingerprint</code><a class="headerlink" href="#pulumi_civo.SshKey.fingerprint" title="Permalink to this definition"></a></dt>
<dd><p>The fingerprint of the SSH key</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.SshKey.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.SshKey.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the SSH key for identification</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.SshKey.public_key">
<em class="property">property </em><code class="sig-name descname">public_key</code><a class="headerlink" href="#pulumi_civo.SshKey.public_key" title="Permalink to this definition"></a></dt>
<dd><p>The public key. If this is a file, it
can be read using the file interpolation function.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.SshKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.SshKey.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.SshKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.SshKey.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.Template">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">Template</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_config</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">code</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Template" title="Permalink to this definition"></a></dt>
<dd><p>Provides a Civo Template resource.
This can be used to create, modify, and delete Templates.</p>
<p>Template can be imported using the template <code class="docutils literal notranslate"><span class="pre">code</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import civo:index/template:Template my-custom-template my-template-code
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Commonly referred to as ‘user-data’, this is a customisation script that is run after
the instance is first booted. We recommend using cloud-config as it’s a great distribution-agnostic
way of configuring cloud servers. If you put <code class="docutils literal notranslate"><span class="pre">$INITIAL_USER</span></code> in your script, this will automatically
be replaced by the initial user chosen when creating the instance, <code class="docutils literal notranslate"><span class="pre">$INITIAL_PASSWORD</span></code> will be
replaced with the random password generated by the system, <code class="docutils literal notranslate"><span class="pre">$HOSTNAME</span></code> is the fully qualified
domain name of the instance and <code class="docutils literal notranslate"><span class="pre">$SSH_KEY</span></code> will be the content of the SSH public key.
(this is technically optional, but you won’t really be able to use instances without it -
see our learn guide on templates for more information).</p></li>
<li><p><strong>code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is a unqiue, alphanumerical, short, human readable code for the template.</p></li>
<li><p><strong>default_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default username to suggest that the user creates</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A multi-line description of the template, in Markdown format</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the Image ID of any default template or the ID of another template
either owned by you or global (optional; but must be specified if no volume_id is specified).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is a short human readable name for the template</p></li>
<li><p><strong>short_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A one line description of the template</p></li>
<li><p><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the ID of a bootable volume, either owned by you or global
(optional; but must be specified if no image_id is specified)</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_civo.Template.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_config</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">code</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_description</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_civo.Template" title="pulumi_civo.Template">Template</a><a class="headerlink" href="#pulumi_civo.Template.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Template resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Commonly referred to as ‘user-data’, this is a customisation script that is run after
the instance is first booted. We recommend using cloud-config as it’s a great distribution-agnostic
way of configuring cloud servers. If you put <code class="docutils literal notranslate"><span class="pre">$INITIAL_USER</span></code> in your script, this will automatically
be replaced by the initial user chosen when creating the instance, <code class="docutils literal notranslate"><span class="pre">$INITIAL_PASSWORD</span></code> will be
replaced with the random password generated by the system, <code class="docutils literal notranslate"><span class="pre">$HOSTNAME</span></code> is the fully qualified
domain name of the instance and <code class="docutils literal notranslate"><span class="pre">$SSH_KEY</span></code> will be the content of the SSH public key.
(this is technically optional, but you won’t really be able to use instances without it -
see our learn guide on templates for more information).</p></li>
<li><p><strong>code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is a unqiue, alphanumerical, short, human readable code for the template.</p></li>
<li><p><strong>default_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default username to suggest that the user creates</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A multi-line description of the template, in Markdown format</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the Image ID of any default template or the ID of another template
either owned by you or global (optional; but must be specified if no volume_id is specified).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is a short human readable name for the template</p></li>
<li><p><strong>short_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A one line description of the template</p></li>
<li><p><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the ID of a bootable volume, either owned by you or global
(optional; but must be specified if no image_id is specified)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Template.cloud_config">
<em class="property">property </em><code class="sig-name descname">cloud_config</code><a class="headerlink" href="#pulumi_civo.Template.cloud_config" title="Permalink to this definition"></a></dt>
<dd><p>Commonly referred to as ‘user-data’, this is a customisation script that is run after
the instance is first booted. We recommend using cloud-config as it’s a great distribution-agnostic
way of configuring cloud servers. If you put <code class="docutils literal notranslate"><span class="pre">$INITIAL_USER</span></code> in your script, this will automatically
be replaced by the initial user chosen when creating the instance, <code class="docutils literal notranslate"><span class="pre">$INITIAL_PASSWORD</span></code> will be
replaced with the random password generated by the system, <code class="docutils literal notranslate"><span class="pre">$HOSTNAME</span></code> is the fully qualified
domain name of the instance and <code class="docutils literal notranslate"><span class="pre">$SSH_KEY</span></code> will be the content of the SSH public key.
(this is technically optional, but you won’t really be able to use instances without it -
see our learn guide on templates for more information).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Template.code">
<em class="property">property </em><code class="sig-name descname">code</code><a class="headerlink" href="#pulumi_civo.Template.code" title="Permalink to this definition"></a></dt>
<dd><p>This is a unqiue, alphanumerical, short, human readable code for the template.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Template.default_username">
<em class="property">property </em><code class="sig-name descname">default_username</code><a class="headerlink" href="#pulumi_civo.Template.default_username" title="Permalink to this definition"></a></dt>
<dd><p>The default username to suggest that the user creates</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Template.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_civo.Template.description" title="Permalink to this definition"></a></dt>
<dd><p>A multi-line description of the template, in Markdown format</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Template.image_id">
<em class="property">property </em><code class="sig-name descname">image_id</code><a class="headerlink" href="#pulumi_civo.Template.image_id" title="Permalink to this definition"></a></dt>
<dd><p>This is the Image ID of any default template or the ID of another template
either owned by you or global (optional; but must be specified if no volume_id is specified).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Template.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.Template.name" title="Permalink to this definition"></a></dt>
<dd><p>This is a short human readable name for the template</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Template.short_description">
<em class="property">property </em><code class="sig-name descname">short_description</code><a class="headerlink" href="#pulumi_civo.Template.short_description" title="Permalink to this definition"></a></dt>
<dd><p>A one line description of the template</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Template.volume_id">
<em class="property">property </em><code class="sig-name descname">volume_id</code><a class="headerlink" href="#pulumi_civo.Template.volume_id" title="Permalink to this definition"></a></dt>
<dd><p>This is the ID of a bootable volume, either owned by you or global
(optional; but must be specified if no image_id is specified)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Template.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Template.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.Template.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Template.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.Volume">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">Volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootable</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_gb</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Volume" title="Permalink to this definition"></a></dt>
<dd><p>Provides a Civo volume which can be attached to a Instance in order to provide expanded storage.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">db</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">Volume</span><span class="p">(</span><span class="s2">&quot;db&quot;</span><span class="p">,</span>
    <span class="n">bootable</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">size_gb</span><span class="o">=</span><span class="mi">60</span><span class="p">)</span>
</pre></div>
</div>
<p>Volumes can be imported using the <code class="docutils literal notranslate"><span class="pre">volume</span> <span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import civo:index/volume:Volume db 506f78a4-e098-11e5-ad9f-000f53306ae1
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bootable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Mark the volume as bootable.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name that you wish to use to refer to this volume .</p></li>
<li><p><strong>size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes .</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_civo.Volume.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootable</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mount_point</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_gb</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_civo.Volume" title="pulumi_civo.Volume">Volume</a><a class="headerlink" href="#pulumi_civo.Volume.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Volume resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bootable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Mark the volume as bootable.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date of the creation of the volume.</p></li>
<li><p><strong>mount_point</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mount point of the volume.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name that you wish to use to refer to this volume .</p></li>
<li><p><strong>size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes .</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Volume.bootable">
<em class="property">property </em><code class="sig-name descname">bootable</code><a class="headerlink" href="#pulumi_civo.Volume.bootable" title="Permalink to this definition"></a></dt>
<dd><p>Mark the volume as bootable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Volume.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_civo.Volume.created_at" title="Permalink to this definition"></a></dt>
<dd><p>The date of the creation of the volume.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Volume.mount_point">
<em class="property">property </em><code class="sig-name descname">mount_point</code><a class="headerlink" href="#pulumi_civo.Volume.mount_point" title="Permalink to this definition"></a></dt>
<dd><p>The mount point of the volume.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Volume.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_civo.Volume.name" title="Permalink to this definition"></a></dt>
<dd><p>A name that you wish to use to refer to this volume .</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Volume.size_gb">
<em class="property">property </em><code class="sig-name descname">size_gb</code><a class="headerlink" href="#pulumi_civo.Volume.size_gb" title="Permalink to this definition"></a></dt>
<dd><p>A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes .</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Volume.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Volume.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.Volume.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Volume.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.VolumeAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">VolumeAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.VolumeAttachment" title="Permalink to this definition"></a></dt>
<dd><p>Manages attaching a Volume to a Instance.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">db</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">Volume</span><span class="p">(</span><span class="s2">&quot;db&quot;</span><span class="p">,</span>
    <span class="n">size_gb</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
    <span class="n">bootable</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">foobar</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">VolumeAttachment</span><span class="p">(</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">civo_instance</span><span class="p">[</span><span class="s2">&quot;my-test-instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">volume_id</span><span class="o">=</span><span class="n">db</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the instance to attach the volume to.</p></li>
<li><p><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Volume to be attached to the instance.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_civo.VolumeAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_civo.VolumeAttachment" title="pulumi_civo.VolumeAttachment">VolumeAttachment</a><a class="headerlink" href="#pulumi_civo.VolumeAttachment.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing VolumeAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the instance to attach the volume to.</p></li>
<li><p><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Volume to be attached to the instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.VolumeAttachment.instance_id">
<em class="property">property </em><code class="sig-name descname">instance_id</code><a class="headerlink" href="#pulumi_civo.VolumeAttachment.instance_id" title="Permalink to this definition"></a></dt>
<dd><p>ID of the instance to attach the volume to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.VolumeAttachment.volume_id">
<em class="property">property </em><code class="sig-name descname">volume_id</code><a class="headerlink" href="#pulumi_civo.VolumeAttachment.volume_id" title="Permalink to this definition"></a></dt>
<dd><p>ID of the Volume to be attached to the instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.VolumeAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.VolumeAttachment.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.VolumeAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.VolumeAttachment.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_civo.get_dns_domain_name">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_dns_domain_name</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_civo.get_dns_domain_name.AwaitableGetDnsDomainNameResult<a class="headerlink" href="#pulumi_civo.get_dns_domain_name" title="Permalink to this definition"></a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>str</em>) – The id of the domain.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the domain.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_dns_domain_record">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_dns_domain_record</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_civo.get_dns_domain_record.AwaitableGetDnsDomainRecordResult<a class="headerlink" href="#pulumi_civo.get_dns_domain_record" title="Permalink to this definition"></a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain_id</strong> (<em>str</em>) – The domain id of the record.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the record.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_instance">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_civo.get_instance.AwaitableGetInstanceResult<a class="headerlink" href="#pulumi_civo.get_instance" title="Permalink to this definition"></a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hostname</strong> (<em>str</em>) – The hostname of the Instance.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The ID of the Instance</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_instances">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_instances</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>pulumi_civo._inputs.GetInstancesFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>pulumi_civo._inputs.GetInstancesSortArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_civo.get_instances.AwaitableGetInstancesResult<a class="headerlink" href="#pulumi_civo.get_instances" title="Permalink to this definition"></a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>Sequence</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GetInstancesFilterArgs'</em><em>]</em><em>]</em>) – Filter the results.
The <code class="docutils literal notranslate"><span class="pre">filter</span></code> block is documented below.</p></li>
<li><p><strong>sorts</strong> (<em>Sequence</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GetInstancesSortArgs'</em><em>]</em><em>]</em>) – Sort the results.
The <code class="docutils literal notranslate"><span class="pre">sort</span></code> block is documented below.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_instances_size">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_instances_size</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>pulumi_civo._inputs.GetInstancesSizeFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>pulumi_civo._inputs.GetInstancesSizeSortArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_civo.get_instances_size.AwaitableGetInstancesSizeResult<a class="headerlink" href="#pulumi_civo.get_instances_size" title="Permalink to this definition"></a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_kubernetes_cluster">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_kubernetes_cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_civo.get_kubernetes_cluster.AwaitableGetKubernetesClusterResult<a class="headerlink" href="#pulumi_civo.get_kubernetes_cluster" title="Permalink to this definition"></a></dt>
<dd><p>Provides a Civo Kubernetes cluster data source.</p>
<p><strong>Note:</strong> This data source returns a single kubernetes cluster. When specifying a <code class="docutils literal notranslate"><span class="pre">name</span></code>, an
error is triggered if more than one kubernetes Cluster is found.</p>
<p>Get the Kubernetes Cluster by name:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">my_cluster</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">get_kubernetes_cluster</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;my-super-cluster&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;kubernetesClusterOutput&quot;</span><span class="p">,</span> <span class="n">my_cluster</span><span class="o">.</span><span class="n">master_ip</span><span class="p">)</span>
</pre></div>
</div>
<p>Get the Kubernetes Cluster by id:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">my_cluster</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">get_kubernetes_cluster</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;40ac97ee-b82b-4231-9b60-079c7e2e5d79&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>str</em>) – The ID of the kubernetes Cluster</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the kubernetes Cluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_kubernetes_version">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_kubernetes_version</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>pulumi_civo._inputs.GetKubernetesVersionFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>pulumi_civo._inputs.GetKubernetesVersionSortArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_civo.get_kubernetes_version.AwaitableGetKubernetesVersionResult<a class="headerlink" href="#pulumi_civo.get_kubernetes_version" title="Permalink to this definition"></a></dt>
<dd><p>Provides access to the available Civo Kubernetes Service versions, with the ability to filter the results.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">stable</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">get_kubernetes_version</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">civo</span><span class="o">.</span><span class="n">GetKubernetesVersionFilterArgs</span><span class="p">(</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;type&quot;</span><span class="p">,</span>
    <span class="n">values</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;stable&quot;</span><span class="p">],</span>
<span class="p">)])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">minor_version</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">get_kubernetes_version</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">civo</span><span class="o">.</span><span class="n">GetKubernetesVersionFilterArgs</span><span class="p">(</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;version&quot;</span><span class="p">,</span>
    <span class="n">values</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;0.9.1&quot;</span><span class="p">],</span>
<span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>Sequence</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GetKubernetesVersionFilterArgs'</em><em>]</em><em>]</em>) – Filter the results.
The <code class="docutils literal notranslate"><span class="pre">filter</span></code> block is documented below.</p></li>
<li><p><strong>sorts</strong> (<em>Sequence</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GetKubernetesVersionSortArgs'</em><em>]</em><em>]</em>) – Sort the results.
The <code class="docutils literal notranslate"><span class="pre">sort</span></code> block is documented below.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_load_balancer">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_load_balancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_civo.get_load_balancer.AwaitableGetLoadBalancerResult<a class="headerlink" href="#pulumi_civo.get_load_balancer" title="Permalink to this definition"></a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hostname</strong> (<em>str</em>) – The hostname of the Load Balancer.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The ID of the Load Balancer.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_network">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_network</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_civo.get_network.AwaitableGetNetworkResult<a class="headerlink" href="#pulumi_civo.get_network" title="Permalink to this definition"></a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>str</em>) – The unique identifier of an existing Network.</p></li>
<li><p><strong>label</strong> (<em>str</em>) – The name of an existing Network.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_snapshot">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_snapshot</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_civo.get_snapshot.AwaitableGetSnapshotResult<a class="headerlink" href="#pulumi_civo.get_snapshot" title="Permalink to this definition"></a></dt>
<dd><p>Snapshots are saved instances of a block storage volume. Use this data
source to retrieve the ID of a Civo snapshot for use in other
resources.</p>
<p>Get the snapshot:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">mysql_vm</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">get_snapshot</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;mysql-vm&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>str</em>) – The ID of the snapshot.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the snapshot.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_ssh_key">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_ssh_key</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_civo.get_ssh_key.AwaitableGetSshKeyResult<a class="headerlink" href="#pulumi_civo.get_ssh_key" title="Permalink to this definition"></a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>str</em>) – The ID of the ssh key.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the ssh key.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_template">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_template</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>pulumi_civo._inputs.GetTemplateFilterArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>pulumi_civo._inputs.GetTemplateSortArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_civo.get_template.AwaitableGetTemplateResult<a class="headerlink" href="#pulumi_civo.get_template" title="Permalink to this definition"></a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>Sequence</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GetTemplateFilterArgs'</em><em>]</em><em>]</em>) – Filter the results.
The <code class="docutils literal notranslate"><span class="pre">filter</span></code> block is documented below.</p></li>
<li><p><strong>sorts</strong> (<em>Sequence</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GetTemplateSortArgs'</em><em>]</em><em>]</em>) – Sort the results.
The <code class="docutils literal notranslate"><span class="pre">sort</span></code> block is documented below.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_volume">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_civo.get_volume.AwaitableGetVolumeResult<a class="headerlink" href="#pulumi_civo.get_volume" title="Permalink to this definition"></a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>id</strong> (<em>str</em>) – The unique identifier for the volume.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the volume.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
