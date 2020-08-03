---
title: Package pulumi_civo
title_tag: Package pulumi_civo | Python SDK
linktitle: pulumi_civo
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "civo" >}}

<div class="section" id="pulumi-civo">
<h1>Pulumi Civo<a class="headerlink" href="#pulumi-civo" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-civo">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-civo/issues">pulumi/pulumi-civo repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-civo/issues">terraform-providers/terraform-provider-civo repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_civo"></span><dl class="py class">
<dt id="pulumi_civo.AwaitableGetDnsDomainNameResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetDnsDomainNameResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetDnsDomainNameResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetDnsDomainRecordResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetDnsDomainRecordResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetDnsDomainRecordResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetInstanceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetInstanceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cpu_cores</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">firewall_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pseudo_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ram_mb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reverse_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sshkey_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetInstanceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetInstancesSizeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetInstancesSizeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sizes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetInstancesSizeResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetKubernetesClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetKubernetesClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">api_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">built_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_entry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">installed_applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubeconfig</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_target_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ready</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_nodes_size</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetKubernetesClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetKubernetesVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetKubernetesVersionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">versions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetKubernetesVersionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetLoadBalancerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetLoadBalancerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">backends</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fail_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_invalid_backend_tls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_conns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_request_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetLoadBalancerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetNetworkResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">completed_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cron_timing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">next_execution</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requested_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">safe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetSshKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetSshKeyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetSshKeyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetTemplateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetTemplateResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">templates</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetTemplateResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.AwaitableGetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">AwaitableGetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">bootable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mount_point</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_gb</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.AwaitableGetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_civo.DnsDomainName">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">DnsDomainName</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.DnsDomainName" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Civo dns domain name resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="c1"># Create a new domain name</span>
<span class="n">main</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">DnsDomainName</span><span class="p">(</span><span class="s2">&quot;main&quot;</span><span class="p">)</span>
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
<dl class="py attribute">
<dt id="pulumi_civo.DnsDomainName.account_id">
<code class="sig-name descname">account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.DnsDomainName.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id account of the domain</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.DnsDomainName.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.DnsDomainName.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the domain</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainName.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.DnsDomainName.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DnsDomainName resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id account of the domain</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the domain</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainName.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.DnsDomainName.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.DnsDomainName.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">DnsDomainRecord</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.DnsDomainRecord" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Civo dns domain record resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="c1"># Create a new domain record</span>
<span class="n">www</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">DnsDomainRecord</span><span class="p">(</span><span class="s2">&quot;www&quot;</span><span class="p">,</span>
    <span class="n">domain_id</span><span class="o">=</span><span class="n">civo_dns_domain_name</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;a&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="n">civo_instance</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">][</span><span class="s2">&quot;public_ip&quot;</span><span class="p">],</span>
    <span class="n">ttl</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
    <span class="n">opts</span><span class="o">=</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span>
            <span class="n">civo_dns_domain_name</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">],</span>
            <span class="n">civo_instance</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">],</span>
        <span class="p">]))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the domain</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The portion before the domain name (e.g. www) or an &#64; for the apex/root domain (you cannot use an A record with an amex/root domain)</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Useful for MX records only, the priority mail should be attempted it (defaults to 10)</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The choice of record type from a, cname, mx or txt</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_civo.DnsDomainRecord.account_id">
<code class="sig-name descname">account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id account of the domain</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.DnsDomainRecord.created_at">
<code class="sig-name descname">created_at</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date when it was created in UTC format</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.DnsDomainRecord.domain_id">
<code class="sig-name descname">domain_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the domain</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.DnsDomainRecord.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The portion before the domain name (e.g. www) or an &#64; for the apex/root domain (you cannot use an A record with an amex/root domain)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.DnsDomainRecord.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Useful for MX records only, the priority mail should be attempted it (defaults to 10)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.DnsDomainRecord.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.DnsDomainRecord.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The choice of record type from a, cname, mx or txt</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.DnsDomainRecord.updated_at">
<code class="sig-name descname">updated_at</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date when it was updated in UTC format</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.DnsDomainRecord.value">
<code class="sig-name descname">value</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainRecord.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DnsDomainRecord resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id account of the domain</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date when it was created in UTC format</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the domain</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The portion before the domain name (e.g. www) or an &#64; for the apex/root domain (you cannot use an A record with an amex/root domain)</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Useful for MX records only, the priority mail should be attempted it (defaults to 10)</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How long caching DNS servers should cache this record for, in seconds (the minimum is 600 and the default if unspecified is 600)</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The choice of record type from a, cname, mx or txt</p></li>
<li><p><strong>updated_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date when it was updated in UTC format</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.DnsDomainRecord.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.DnsDomainRecord.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">Firewall</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Firewall" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Civo Cloud Firewall resource. This can be used to create,
modify, and delete Firewalls.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">www</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">Firewall</span><span class="p">(</span><span class="s2">&quot;www&quot;</span><span class="p">)</span>
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
<dl class="py attribute">
<dt id="pulumi_civo.Firewall.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Firewall.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Firewall name</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Firewall.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Firewall.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where the firewall was create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Firewall.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Firewall.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Firewall resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Firewall name</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region where the firewall was create.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Firewall.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Firewall.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Firewall.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">FirewallRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">direction</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">firewall_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Civo Cloud Firewall Rule resource.
This can be used to create, modify, and delete Firewalls Rules.
This resource don’t have an update option because the backend don’t have the
support for that, so in this case we use ForceNew for all object in the resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – will this rule affect ingress traffic</p></li>
<li><p><strong>end_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end port where traffic to be allowed.</p></li>
<li><p><strong>firewall_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Firewall id</p></li>
<li><p><strong>label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – a string that will be the displayed name/reference for this rule (optional)</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This may be one of “tcp”, “udp”, or “icmp”.</p></li>
<li><p><strong>start_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The start port where traffic to be allowed.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_civo.FirewallRule.cidrs">
<code class="sig-name descname">cidrs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.FirewallRule.cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.FirewallRule.direction">
<code class="sig-name descname">direction</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.FirewallRule.direction" title="Permalink to this definition">¶</a></dt>
<dd><p>will this rule affect ingress traffic</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.FirewallRule.end_port">
<code class="sig-name descname">end_port</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.FirewallRule.end_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The end port where traffic to be allowed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.FirewallRule.firewall_id">
<code class="sig-name descname">firewall_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.FirewallRule.firewall_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Firewall id</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.FirewallRule.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.FirewallRule.label" title="Permalink to this definition">¶</a></dt>
<dd><p>a string that will be the displayed name/reference for this rule (optional)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.FirewallRule.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.FirewallRule.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>This may be one of “tcp”, “udp”, or “icmp”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.FirewallRule.start_port">
<code class="sig-name descname">start_port</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.FirewallRule.start_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The start port where traffic to be allowed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.FirewallRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">direction</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">firewall_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_port</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.FirewallRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – the IP address of the other end (i.e. not your instance) to affect, or a valid network CIDR (defaults to being globally applied, i.e. 0.0.0.0/0).</p></li>
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
<dt id="pulumi_civo.FirewallRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetDnsDomainNameResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetDnsDomainNameResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDnsDomainName.</p>
<dl class="py attribute">
<dt id="pulumi_civo.GetDnsDomainNameResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetDnsDomainNameResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique ID that can be used to identify and reference a domain.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetDnsDomainNameResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetDnsDomainNameResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the domain.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetDnsDomainRecordResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetDnsDomainRecordResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDnsDomainRecord.</p>
<dl class="py attribute">
<dt id="pulumi_civo.GetDnsDomainRecordResult.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id account of the domain.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetDnsDomainRecordResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date when it was created in UTC format</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetDnsDomainRecordResult.domain_id">
<code class="sig-name descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the domain</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetDnsDomainRecordResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetDnsDomainRecordResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The portion before the domain name (e.g. www) or an &#64; for the apex/root domain (you cannot use an A record with an amex/root domain)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetDnsDomainRecordResult.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the record.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetDnsDomainRecordResult.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>How long caching DNS servers should cache this record.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetDnsDomainRecordResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The choice of record type from a, cname, mx or txt</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetDnsDomainRecordResult.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date when it was updated in UTC format</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetDnsDomainRecordResult.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetDnsDomainRecordResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address (A or MX), hostname (CNAME or MX) or text value (TXT) to serve for this record</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetInstanceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetInstanceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cpu_cores</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">firewall_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pseudo_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ram_mb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reverse_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sshkey_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetInstanceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstance.</p>
<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.cpu_cores">
<code class="sig-name descname">cpu_cores</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.cpu_cores" title="Permalink to this definition">¶</a></dt>
<dd><p>Total cpu of the inatance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date of creation of the instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.disk_gb">
<code class="sig-name descname">disk_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.disk_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the disk.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.firewall_id">
<code class="sig-name descname">firewall_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.firewall_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the firewall used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.hostname">
<code class="sig-name descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The Instance hostname.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.initial_password">
<code class="sig-name descname">initial_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.initial_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance initial password</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.initial_user">
<code class="sig-name descname">initial_user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.initial_user" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the initial user created on the server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.network_id">
<code class="sig-name descname">network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>This will be the ID of the network.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.notes">
<code class="sig-name descname">notes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.notes" title="Permalink to this definition">¶</a></dt>
<dd><p>The notes of the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.private_ip">
<code class="sig-name descname">private_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The private ip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.pseudo_ip">
<code class="sig-name descname">pseudo_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.pseudo_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the ip that is used to route the public ip from the internet to the instance using NAT</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.public_ip">
<code class="sig-name descname">public_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The public ip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.ram_mb">
<code class="sig-name descname">ram_mb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.ram_mb" title="Permalink to this definition">¶</a></dt>
<dd><p>Total ram of the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.reverse_dns">
<code class="sig-name descname">reverse_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.reverse_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>A fully qualified domain name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.script">
<code class="sig-name descname">script</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.script" title="Permalink to this definition">¶</a></dt>
<dd><p>the contents of a script uploaded</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the size.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.sshkey_id">
<code class="sig-name descname">sshkey_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.sshkey_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID SSH.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional list of tags</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstanceResult.template">
<code class="sig-name descname">template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstanceResult.template" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for the template to used to build the instance.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstances.</p>
<dl class="py attribute">
<dt id="pulumi_civo.GetInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Instances satisfying any <code class="docutils literal notranslate"><span class="pre">filter</span></code> and <code class="docutils literal notranslate"><span class="pre">sort</span></code> criteria. Each instance has the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetInstancesSizeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetInstancesSizeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sizes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetInstancesSizeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstancesSize.</p>
<dl class="py attribute">
<dt id="pulumi_civo.GetInstancesSizeResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetInstancesSizeResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetKubernetesClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetKubernetesClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">api_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">built_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_entry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">installed_applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubeconfig</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_target_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ready</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_nodes_size</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKubernetesCluster.</p>
<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.api_endpoint">
<code class="sig-name descname">api_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.api_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The base URL of the API server on the Kubernetes master node.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.applications">
<code class="sig-name descname">applications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.applications" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of application installed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.built_at">
<code class="sig-name descname">built_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.built_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date where the Kubernetes cluster was build.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date where the Kubernetes cluster was create.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.dns_entry">
<code class="sig-name descname">dns_entry</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.dns_entry" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique dns entry for the cluster in this case point to the master.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique ID that can be used to identify and reference a Kubernetes cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.installed_applications">
<code class="sig-name descname">installed_applications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.installed_applications" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique ID that can be used to identify and reference a Kubernetes cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>In addition to the arguments provided, these additional attributes about the cluster’s default node instance are exported.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.kubeconfig">
<code class="sig-name descname">kubeconfig</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.kubeconfig" title="Permalink to this definition">¶</a></dt>
<dd><p>A representation of the Kubernetes cluster’s kubeconfig in yaml format.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.kubernetes_version">
<code class="sig-name descname">kubernetes_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.kubernetes_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of Kubernetes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.master_ip">
<code class="sig-name descname">master_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.master_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The Ip of the Kubernetes master node.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of your cluster,.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.num_target_nodes">
<code class="sig-name descname">num_target_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.num_target_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the Kubernetes cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of Kubernetes cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ready</span></code> -If the Kubernetes cluster is ready.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The tag of the instances</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesClusterResult.target_nodes_size">
<code class="sig-name descname">target_nodes_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesClusterResult.target_nodes_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of each node.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetKubernetesVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetKubernetesVersionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">versions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetKubernetesVersionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKubernetesVersion.</p>
<dl class="py attribute">
<dt id="pulumi_civo.GetKubernetesVersionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetKubernetesVersionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetLoadBalancerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetLoadBalancerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">backends</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fail_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_invalid_backend_tls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_conns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_request_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLoadBalancer.</p>
<dl class="py attribute">
<dt id="pulumi_civo.GetLoadBalancerResult.backends">
<code class="sig-name descname">backends</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.backends" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of backend instances</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetLoadBalancerResult.fail_timeout">
<code class="sig-name descname">fail_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.fail_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The wait time until the backend is marked as a failure</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetLoadBalancerResult.health_check_path">
<code class="sig-name descname">health_check_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.health_check_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to check the health of the backend</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetLoadBalancerResult.hostname">
<code class="sig-name descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname of the Load Balancer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetLoadBalancerResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Load Balancer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetLoadBalancerResult.ignore_invalid_backend_tls">
<code class="sig-name descname">ignore_invalid_backend_tls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.ignore_invalid_backend_tls" title="Permalink to this definition">¶</a></dt>
<dd><p>Should self-signed/invalid certificates be ignored from the backend servers</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetLoadBalancerResult.max_conns">
<code class="sig-name descname">max_conns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.max_conns" title="Permalink to this definition">¶</a></dt>
<dd><p>How many concurrent connections can each backend handle</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetLoadBalancerResult.max_request_size">
<code class="sig-name descname">max_request_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.max_request_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The max request size set in the configuration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetLoadBalancerResult.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy set in the Load Balancer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetLoadBalancerResult.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port set in the configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetLoadBalancerResult.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol used in the configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetLoadBalancerResult.tls_certificate">
<code class="sig-name descname">tls_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.tls_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>If is set will be returned</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetLoadBalancerResult.tls_key">
<code class="sig-name descname">tls_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetLoadBalancerResult.tls_key" title="Permalink to this definition">¶</a></dt>
<dd><p>If is set will be returned</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetNetworkResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetwork.</p>
<dl class="py attribute">
<dt id="pulumi_civo.GetNetworkResult.cidr">
<code class="sig-name descname">cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetNetworkResult.cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The block ip assigned to the network.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetNetworkResult.default">
<code class="sig-name descname">default</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetNetworkResult.default" title="Permalink to this definition">¶</a></dt>
<dd><p>If is the default network.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetNetworkResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetNetworkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique ID that can be used to identify and reference a Network.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetNetworkResult.label">
<code class="sig-name descname">label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetNetworkResult.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label used in the configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetNetworkResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetNetworkResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the network.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetNetworkResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetNetworkResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where the network was create.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">completed_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cron_timing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">next_execution</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requested_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">safe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSnapshot.</p>
<dl class="py attribute">
<dt id="pulumi_civo.GetSnapshotResult.completed_at">
<code class="sig-name descname">completed_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.completed_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date where the snapshot was completed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetSnapshotResult.cron_timing">
<code class="sig-name descname">cron_timing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.cron_timing" title="Permalink to this definition">¶</a></dt>
<dd><p>A string with the cron format.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetSnapshotResult.hostname">
<code class="sig-name descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname of the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetSnapshotResult.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Instance from which the snapshot was be taken.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetSnapshotResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the snapshot.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetSnapshotResult.next_execution">
<code class="sig-name descname">next_execution</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.next_execution" title="Permalink to this definition">¶</a></dt>
<dd><p>if cron was define this date will be the next execution date.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetSnapshotResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where the snapshot was take.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetSnapshotResult.requested_at">
<code class="sig-name descname">requested_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.requested_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date where the snapshot was requested.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetSnapshotResult.safe">
<code class="sig-name descname">safe</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.safe" title="Permalink to this definition">¶</a></dt>
<dd><p>If is <code class="docutils literal notranslate"><span class="pre">true</span></code> the instance will be shut down during the snapshot if id <code class="docutils literal notranslate"><span class="pre">false</span></code> them not.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetSnapshotResult.size_gb">
<code class="sig-name descname">size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the snapshot in GB.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetSnapshotResult.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the snapshot.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetSnapshotResult.template_id">
<code class="sig-name descname">template_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetSnapshotResult.template_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The template id.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetSshKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetSshKeyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetSshKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSshKey.</p>
</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetTemplateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetTemplateResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">templates</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetTemplateResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTemplate.</p>
<dl class="py attribute">
<dt id="pulumi_civo.GetTemplateResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetTemplateResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.GetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">GetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">bootable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mount_point</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_gb</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.GetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVolume.</p>
<dl class="py attribute">
<dt id="pulumi_civo.GetVolumeResult.bootable">
<code class="sig-name descname">bootable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetVolumeResult.bootable" title="Permalink to this definition">¶</a></dt>
<dd><p>if is bootable or not.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetVolumeResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetVolumeResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date of the creation of the volume.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetVolumeResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetVolumeResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the volume.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetVolumeResult.mount_point">
<code class="sig-name descname">mount_point</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetVolumeResult.mount_point" title="Permalink to this definition">¶</a></dt>
<dd><p>The mount point of the volume.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetVolumeResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetVolumeResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the volume.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.GetVolumeResult.size_gb">
<code class="sig-name descname">size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.GetVolumeResult.size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the volume.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_civo.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">firewall_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip_requiered</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reverse_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sshkey_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Civo Instance resource. This can be used to create,
modify, and delete Instances.</p>
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
<li><p><strong>public_ip_requiered</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This should be either false, true or <code class="docutils literal notranslate"><span class="pre">move_ip_from:intances_id</span></code>.</p></li>
<li><p><strong>reverse_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A fully qualified domain name that should be used as the instance’s IP’s reverse DNS (optional, uses the hostname if unspecified).</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the size, from the current list, e.g. g2.small (required).</p></li>
<li><p><strong>sshkey_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn’t provided a random password will be set and returned in the initial_password field).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An optional list of tags, represented as a key, value pair.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the template to use to build the instance.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_civo.Instance.cpu_cores">
<code class="sig-name descname">cpu_cores</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.cpu_cores" title="Permalink to this definition">¶</a></dt>
<dd><p>Total cpu of the inatance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.created_at">
<code class="sig-name descname">created_at</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date of creation of the instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.disk_gb">
<code class="sig-name descname">disk_gb</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.disk_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the disk.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.firewall_id">
<code class="sig-name descname">firewall_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.firewall_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.hostname">
<code class="sig-name descname">hostname</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The Instance hostname.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.initial_password">
<code class="sig-name descname">initial_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.initial_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance initial password</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.initial_user">
<code class="sig-name descname">initial_user</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.initial_user" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the initial user created on the server (optional; this will default to the template’s default_username and fallback to civo).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.network_id">
<code class="sig-name descname">network_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>This must be the ID of the network from the network listing (optional; default network used when not specified).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.notes">
<code class="sig-name descname">notes</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.notes" title="Permalink to this definition">¶</a></dt>
<dd><p>Add some notes to the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.private_ip">
<code class="sig-name descname">private_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.private_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The private ip.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.pseudo_ip">
<code class="sig-name descname">pseudo_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.pseudo_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the ip that is used to route the public ip from the internet to the instance using NAT</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.public_ip">
<code class="sig-name descname">public_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>This should be either false, true or <code class="docutils literal notranslate"><span class="pre">move_ip_from:intances_id</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.public_ip_requiered">
<code class="sig-name descname">public_ip_requiered</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.public_ip_requiered" title="Permalink to this definition">¶</a></dt>
<dd><p>This should be either false, true or <code class="docutils literal notranslate"><span class="pre">move_ip_from:intances_id</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.ram_mb">
<code class="sig-name descname">ram_mb</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.ram_mb" title="Permalink to this definition">¶</a></dt>
<dd><p>Total ram of the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.reverse_dns">
<code class="sig-name descname">reverse_dns</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.reverse_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>A fully qualified domain name that should be used as the instance’s IP’s reverse DNS (optional, uses the hostname if unspecified).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.script">
<code class="sig-name descname">script</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.script" title="Permalink to this definition">¶</a></dt>
<dd><p>the contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.size">
<code class="sig-name descname">size</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the size, from the current list, e.g. g2.small (required).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.sshkey_id">
<code class="sig-name descname">sshkey_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.sshkey_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn’t provided a random password will be set and returned in the initial_password field).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the instance</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional list of tags, represented as a key, value pair.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Instance.template">
<code class="sig-name descname">template</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Instance.template" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for the template to use to build the instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cpu_cores</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">firewall_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pseudo_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ip_requiered</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ram_mb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reverse_dns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">script</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sshkey_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cpu_cores</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Total cpu of the inatance.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date of creation of the instance</p></li>
<li><p><strong>disk_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the disk.</p></li>
<li><p><strong>firewall_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the firewall to use, from the current list. If left blank or not sent, the default firewall will be used (open to all).</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Instance hostname.</p></li>
<li><p><strong>initial_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance initial password</p></li>
<li><p><strong>initial_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the initial user created on the server (optional; this will default to the template’s default_username and fallback to civo).</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This must be the ID of the network from the network listing (optional; default network used when not specified).</p></li>
<li><p><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Add some notes to the instance.</p></li>
<li><p><strong>private_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private ip.</p></li>
<li><p><strong>pseudo_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Is the ip that is used to route the public ip from the internet to the instance using NAT</p></li>
<li><p><strong>public_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This should be either false, true or <code class="docutils literal notranslate"><span class="pre">move_ip_from:intances_id</span></code>.</p></li>
<li><p><strong>public_ip_requiered</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This should be either false, true or <code class="docutils literal notranslate"><span class="pre">move_ip_from:intances_id</span></code>.</p></li>
<li><p><strong>ram_mb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Total ram of the instance.</p></li>
<li><p><strong>reverse_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A fully qualified domain name that should be used as the instance’s IP’s reverse DNS (optional, uses the hostname if unspecified).</p></li>
<li><p><strong>script</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the contents of a script that will be uploaded to /usr/local/bin/civo-user-init-script on your instance, read/write/executable only by root and then will be executed at the end of the cloud initialization</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the size, from the current list, e.g. g2.small (required).</p></li>
<li><p><strong>sshkey_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an already uploaded SSH public key to use for login to the default user (optional; if one isn’t provided a random password will be set and returned in the initial_password field).</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the instance</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An optional list of tags, represented as a key, value pair.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the template to use to build the instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">KubernetesCluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_target_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_nodes_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.KubernetesCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a KubernetesCluster resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] applications: A comma separated list of applications to install. Spaces within application names are fine, but shouldn’t be either side of the comma. If you want to remove a default installed application, prefix it with a ‘-‘, e.g. -traefik
:param pulumi.Input[str] kubernetes_version: The version of k3s to install (optional, the default is currently the latest available).
:param pulumi.Input[str] name: A name for the Kubernetes cluster.
:param pulumi.Input[float] num_target_nodes: The number of instances to create (optional, the default at the time of writing is 3).
:param pulumi.Input[str] tags: A space separated list of tags, to be used freely as required.
:param pulumi.Input[str] target_nodes_size: The size of each node (optional, the default is currently g2.small)</p>
<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.api_endpoint">
<code class="sig-name descname">api_endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.api_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The base URL of the API server on the Kubernetes master node.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.applications">
<code class="sig-name descname">applications</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.applications" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of applications to install. Spaces within application names are fine, but shouldn’t be either side of the comma. If you want to remove a default installed application, prefix it with a ‘-‘, e.g. -traefik</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.built_at">
<code class="sig-name descname">built_at</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.built_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date where the Kubernetes cluster was build.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.created_at">
<code class="sig-name descname">created_at</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date where the Kubernetes cluster was create.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.dns_entry">
<code class="sig-name descname">dns_entry</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.dns_entry" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique dns entry for the cluster in this case point to the master.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.installed_applications">
<code class="sig-name descname">installed_applications</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.installed_applications" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique ID that can be used to identify and reference a Kubernetes cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">application</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the application</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The category of the application</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">installed</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - if installed or not</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of the application</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.instances">
<code class="sig-name descname">instances</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>In addition to the arguments provided, these additional attributes about the cluster’s default node instance are exported.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpu_cores</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Total cpu of the inatance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">created_at</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The date where the Kubernetes cluster was create.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firewall_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The firewall id assigned to the instance</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The hostname of the instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The public ip of the instances, only available if the instances is the master</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ram_mb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Total ram of the instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region where instance are.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The size of the instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The status of Kubernetes cluster.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ready</span></code> -If the Kubernetes cluster is ready.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A space separated list of tags, to be used freely as required.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.kubeconfig">
<code class="sig-name descname">kubeconfig</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.kubeconfig" title="Permalink to this definition">¶</a></dt>
<dd><p>A representation of the Kubernetes cluster’s kubeconfig in yaml format.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.kubernetes_version">
<code class="sig-name descname">kubernetes_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.kubernetes_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of k3s to install (optional, the default is currently the latest available).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.master_ip">
<code class="sig-name descname">master_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.master_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The Ip of the Kubernetes master node.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the Kubernetes cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.num_target_nodes">
<code class="sig-name descname">num_target_nodes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.num_target_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of instances to create (optional, the default at the time of writing is 3).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of Kubernetes cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ready</span></code> -If the Kubernetes cluster is ready.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A space separated list of tags, to be used freely as required.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.KubernetesCluster.target_nodes_size">
<code class="sig-name descname">target_nodes_size</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.KubernetesCluster.target_nodes_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of each node (optional, the default is currently g2.small)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">built_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_entry</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">installed_applications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubeconfig</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_target_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ready</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_nodes_size</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.KubernetesCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KubernetesCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base URL of the API server on the Kubernetes master node.</p></li>
<li><p><strong>applications</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma separated list of applications to install. Spaces within application names are fine, but shouldn’t be either side of the comma. If you want to remove a default installed application, prefix it with a ‘-‘, e.g. -traefik</p></li>
<li><p><strong>built_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date where the Kubernetes cluster was build.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date where the Kubernetes cluster was create.</p></li>
<li><p><strong>dns_entry</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique dns entry for the cluster in this case point to the master.</p></li>
<li><p><strong>installed_applications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A unique ID that can be used to identify and reference a Kubernetes cluster.</p></li>
<li><p><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – In addition to the arguments provided, these additional attributes about the cluster’s default node instance are exported.</p></li>
<li><p><strong>kubeconfig</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A representation of the Kubernetes cluster’s kubeconfig in yaml format.</p></li>
<li><p><strong>kubernetes_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of k3s to install (optional, the default is currently the latest available).</p></li>
<li><p><strong>master_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Ip of the Kubernetes master node.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the Kubernetes cluster.</p></li>
<li><p><strong>num_target_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of instances to create (optional, the default at the time of writing is 3).</p></li>
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
<li><p><strong>target_nodes_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The size of each node (optional, the default is currently g2.small)</p></li>
</ul>
</dd>
</dl>
<p>The <strong>installed_applications</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">application</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the application</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The category of the application</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">installed</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - if installed or not</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the application</p></li>
</ul>
<p>The <strong>instances</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpu_cores</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Total cpu of the inatance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">created_at</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The date where the Kubernetes cluster was create.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firewall_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The firewall id assigned to the instance</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The hostname of the instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The public ip of the instances, only available if the instances is the master</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ram_mb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Total ram of the instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region where instance are.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The size of the instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The status of Kubernetes cluster.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ready</span></code> -If the Kubernetes cluster is ready.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A space separated list of tags, to be used freely as required.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.KubernetesCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.KubernetesCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.KubernetesCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">LoadBalancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backends</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fail_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_invalid_backend_tls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_conns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_request_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.LoadBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a LoadBalancer resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] backends: a list of backend instances, each containing an instance_id, protocol (http or https) and port
:param pulumi.Input[float] fail_timeout: how long to wait in seconds before determining a backend has failed, defaults to 30
:param pulumi.Input[str] health_check_path: what URL should be used on the backends to determine if it’s OK (2xx/3xx status), defaults to /
:param pulumi.Input[str] hostname: the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if</p>
<blockquote>
<div><p>blank)</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ignore_invalid_backend_tls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – should self-signed/invalid certificates be ignored from the backend servers, defaults to true</p></li>
<li><p><strong>max_conns</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – how many concurrent connections can each backend handle, defaults to 10</p></li>
<li><p><strong>max_request_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – the size in megabytes of the maximum request content that will be accepted, defaults to 20</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
same backend), default is random</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
(commonly 80 for HTTP or 443 for HTTPS)</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – either http or https. If you specify https then you must also provide the next two fields, the default is http</p></li>
<li><p><strong>tls_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format</p></li>
<li><p><strong>tls_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – if your protocol is https then you should send the TLS private key in Base64-encoded PEM format</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backends</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_civo.LoadBalancer.backends">
<code class="sig-name descname">backends</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.LoadBalancer.backends" title="Permalink to this definition">¶</a></dt>
<dd><p>a list of backend instances, each containing an instance_id, protocol (http or https) and port</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.LoadBalancer.fail_timeout">
<code class="sig-name descname">fail_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.LoadBalancer.fail_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>how long to wait in seconds before determining a backend has failed, defaults to 30</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.LoadBalancer.health_check_path">
<code class="sig-name descname">health_check_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.LoadBalancer.health_check_path" title="Permalink to this definition">¶</a></dt>
<dd><p>what URL should be used on the backends to determine if it’s OK (2xx/3xx status), defaults to /</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.LoadBalancer.hostname">
<code class="sig-name descname">hostname</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.LoadBalancer.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if
blank)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.LoadBalancer.ignore_invalid_backend_tls">
<code class="sig-name descname">ignore_invalid_backend_tls</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.LoadBalancer.ignore_invalid_backend_tls" title="Permalink to this definition">¶</a></dt>
<dd><p>should self-signed/invalid certificates be ignored from the backend servers, defaults to true</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.LoadBalancer.max_conns">
<code class="sig-name descname">max_conns</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.LoadBalancer.max_conns" title="Permalink to this definition">¶</a></dt>
<dd><p>how many concurrent connections can each backend handle, defaults to 10</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.LoadBalancer.max_request_size">
<code class="sig-name descname">max_request_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.LoadBalancer.max_request_size" title="Permalink to this definition">¶</a></dt>
<dd><p>the size in megabytes of the maximum request content that will be accepted, defaults to 20</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.LoadBalancer.policy">
<code class="sig-name descname">policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.LoadBalancer.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
same backend), default is random</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.LoadBalancer.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.LoadBalancer.port" title="Permalink to this definition">¶</a></dt>
<dd><p>you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
(commonly 80 for HTTP or 443 for HTTPS)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.LoadBalancer.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.LoadBalancer.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>either http or https. If you specify https then you must also provide the next two fields, the default is http</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.LoadBalancer.tls_certificate">
<code class="sig-name descname">tls_certificate</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.LoadBalancer.tls_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.LoadBalancer.tls_key">
<code class="sig-name descname">tls_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.LoadBalancer.tls_key" title="Permalink to this definition">¶</a></dt>
<dd><p>if your protocol is https then you should send the TLS private key in Base64-encoded PEM format</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backends</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fail_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ignore_invalid_backend_tls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_conns</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_request_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.LoadBalancer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backends</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – a list of backend instances, each containing an instance_id, protocol (http or https) and port</p></li>
<li><p><strong>fail_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – how long to wait in seconds before determining a backend has failed, defaults to 30</p></li>
<li><p><strong>health_check_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – what URL should be used on the backends to determine if it’s OK (2xx/3xx status), defaults to /</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the hostname to receive traffic for, e.g. www.example.com (optional: sets hostname to loadbalancer-uuid.civo.com if
blank)</p></li>
<li><p><strong>ignore_invalid_backend_tls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – should self-signed/invalid certificates be ignored from the backend servers, defaults to true</p></li>
<li><p><strong>max_conns</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – how many concurrent connections can each backend handle, defaults to 10</p></li>
<li><p><strong>max_request_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – the size in megabytes of the maximum request content that will be accepted, defaults to 20</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – one of: least_conn (sends new requests to the least busy server), random (sends new requests to a random backend),
round_robin (sends new requests to the next backend in order), ip_hash (sends requests from a given IP address to the
same backend), default is random</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – you can listen on any port, the default is 80 to match the default protocol of http,if not you must specify it here
(commonly 80 for HTTP or 443 for HTTPS)</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – either http or https. If you specify https then you must also provide the next two fields, the default is http</p></li>
<li><p><strong>tls_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – if your protocol is https then you should send the TLS certificate in Base64-encoded PEM format</p></li>
<li><p><strong>tls_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – if your protocol is https then you should send the TLS private key in Base64-encoded PEM format</p></li>
</ul>
</dd>
</dl>
<p>The <strong>backends</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.LoadBalancer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.LoadBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.LoadBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">Network</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Network" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Civo Network resource. This can be used to create,
modify, and delete Networks.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">custom_net</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;customNet&quot;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s2">&quot;test_network&quot;</span><span class="p">)</span>
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
<dl class="py attribute">
<dt id="pulumi_civo.Network.cidr">
<code class="sig-name descname">cidr</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Network.cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>The block ip assigned to the network.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Network.default">
<code class="sig-name descname">default</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Network.default" title="Permalink to this definition">¶</a></dt>
<dd><p>If is the default network.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Network.label">
<code class="sig-name descname">label</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Network.label" title="Permalink to this definition">¶</a></dt>
<dd><p>The Network label</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Network.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Network.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the network.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Network.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Network.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where the network was create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Network.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Network.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Network resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<dt id="pulumi_civo.Network.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Network.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Network.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Provider" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">Snapshot</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cron_timing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">safe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource which can be used to create a snapshot from an existing Civo Instance.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">myinstance_backup</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">Snapshot</span><span class="p">(</span><span class="s2">&quot;myinstance-backup&quot;</span><span class="p">,</span> <span class="n">instance_id</span><span class="o">=</span><span class="n">civo_instance</span><span class="p">[</span><span class="s2">&quot;myinstance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
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
<dl class="py attribute">
<dt id="pulumi_civo.Snapshot.completed_at">
<code class="sig-name descname">completed_at</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Snapshot.completed_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date where the snapshot was completed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Snapshot.cron_timing">
<code class="sig-name descname">cron_timing</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Snapshot.cron_timing" title="Permalink to this definition">¶</a></dt>
<dd><p>If a valid cron string is passed, the snapshot will be saved as an automated snapshot 
continuing to automatically update based on the schedule of the cron sequence provided
The default is nil meaning the snapshot will be saved as a one-off snapshot.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Snapshot.hostname">
<code class="sig-name descname">hostname</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Snapshot.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname of the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Snapshot.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Snapshot.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Instance from which the snapshot will be taken.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Snapshot.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Snapshot.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the instance snapshot.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Snapshot.next_execution">
<code class="sig-name descname">next_execution</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Snapshot.next_execution" title="Permalink to this definition">¶</a></dt>
<dd><p>if cron was define this date will be the next execution date.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Snapshot.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Snapshot.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region where the snapshot was take.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Snapshot.requested_at">
<code class="sig-name descname">requested_at</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Snapshot.requested_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date where the snapshot was requested.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Snapshot.safe">
<code class="sig-name descname">safe</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Snapshot.safe" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code> the instance will be shut down during the snapshot to ensure all files 
are in a consistent state (e.g. database tables aren’t in the middle of being optimised
and hence risking corruption). The default is <code class="docutils literal notranslate"><span class="pre">false</span></code> so you experience no interruption
of service, but a small risk of corruption.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Snapshot.size_gb">
<code class="sig-name descname">size_gb</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Snapshot.size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the snapshot in GB.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Snapshot.state">
<code class="sig-name descname">state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Snapshot.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the snapshot.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Snapshot.template_id">
<code class="sig-name descname">template_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Snapshot.template_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The template id.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">completed_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cron_timing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">next_execution</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">requested_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">safe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Snapshot.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Snapshot resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<li><p><strong>size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the snapshot in GB.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the snapshot.</p></li>
<li><p><strong>template_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The template id.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Snapshot.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Snapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Snapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">SshKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.SshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Civo SSH key resource to allow you to manage SSH
keys for Instance access. Keys created with this resource
can be referenced in your instance configuration via their ID.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">my_user</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">SshKey</span><span class="p">(</span><span class="s2">&quot;my-user&quot;</span><span class="p">,</span> <span class="n">public_key</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;~/.ssh/id_rsa.pub&quot;</span><span class="p">))</span>
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
<dl class="py attribute">
<dt id="pulumi_civo.SshKey.fingerprint">
<code class="sig-name descname">fingerprint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.SshKey.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the SSH key</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.SshKey.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.SshKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SSH key for identification</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.SshKey.public_key">
<code class="sig-name descname">public_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.SshKey.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key. If this is a file, it
can be read using the file interpolation function.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.SshKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.SshKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SshKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<dt id="pulumi_civo.SshKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.SshKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.SshKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">Template</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Template" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Civo Template resource.
This can be used to create, modify, and delete Templates.</p>
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
<dl class="py attribute">
<dt id="pulumi_civo.Template.cloud_config">
<code class="sig-name descname">cloud_config</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Template.cloud_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Commonly referred to as ‘user-data’, this is a customisation script that is run after
the instance is first booted. We recommend using cloud-config as it’s a great distribution-agnostic
way of configuring cloud servers. If you put <code class="docutils literal notranslate"><span class="pre">$INITIAL_USER</span></code> in your script, this will automatically
be replaced by the initial user chosen when creating the instance, <code class="docutils literal notranslate"><span class="pre">$INITIAL_PASSWORD</span></code> will be
replaced with the random password generated by the system, <code class="docutils literal notranslate"><span class="pre">$HOSTNAME</span></code> is the fully qualified
domain name of the instance and <code class="docutils literal notranslate"><span class="pre">$SSH_KEY</span></code> will be the content of the SSH public key.
(this is technically optional, but you won’t really be able to use instances without it -
see our learn guide on templates for more information).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Template.code">
<code class="sig-name descname">code</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Template.code" title="Permalink to this definition">¶</a></dt>
<dd><p>This is a unqiue, alphanumerical, short, human readable code for the template.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Template.default_username">
<code class="sig-name descname">default_username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Template.default_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The default username to suggest that the user creates</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Template.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Template.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A multi-line description of the template, in Markdown format</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Template.image_id">
<code class="sig-name descname">image_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Template.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the Image ID of any default template or the ID of another template
either owned by you or global (optional; but must be specified if no volume_id is specified).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Template.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Template.name" title="Permalink to this definition">¶</a></dt>
<dd><p>This is a short human readable name for the template</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Template.short_description">
<code class="sig-name descname">short_description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Template.short_description" title="Permalink to this definition">¶</a></dt>
<dd><p>A one line description of the template</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Template.volume_id">
<code class="sig-name descname">volume_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Template.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the ID of a bootable volume, either owned by you or global
(optional; but must be specified if no image_id is specified)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Template.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Template.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Template resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<dt id="pulumi_civo.Template.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Template.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Template.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">Volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Civo volume which can be attached to a Instance in order to provide expanded storage.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">db</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">Volume</span><span class="p">(</span><span class="s2">&quot;db&quot;</span><span class="p">,</span>
    <span class="n">bootable</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">size_gb</span><span class="o">=</span><span class="mi">60</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bootable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Mark the volume as bootable.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name that you wish to use to refer to this volume .</p></li>
<li><p><strong>size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes .</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_civo.Volume.bootable">
<code class="sig-name descname">bootable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Volume.bootable" title="Permalink to this definition">¶</a></dt>
<dd><p>Mark the volume as bootable.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Volume.created_at">
<code class="sig-name descname">created_at</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Volume.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The date of the creation of the volume.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Volume.mount_point">
<code class="sig-name descname">mount_point</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Volume.mount_point" title="Permalink to this definition">¶</a></dt>
<dd><p>The mount point of the volume.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Volume.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Volume.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name that you wish to use to refer to this volume .</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.Volume.size_gb">
<code class="sig-name descname">size_gb</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.Volume.size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes .</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Volume.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mount_point</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size_gb</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Volume.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Volume resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bootable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Mark the volume as bootable.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date of the creation of the volume.</p></li>
<li><p><strong>mount_point</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mount point of the volume.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name that you wish to use to refer to this volume .</p></li>
<li><p><strong>size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A minimum of 1 and a maximum of your available disk space from your quota specifies the size of the volume in gigabytes .</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.Volume.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Volume.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.Volume.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">VolumeAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.VolumeAttachment" title="Permalink to this definition">¶</a></dt>
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
<dl class="py attribute">
<dt id="pulumi_civo.VolumeAttachment.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.VolumeAttachment.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the instance to attach the volume to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_civo.VolumeAttachment.volume_id">
<code class="sig-name descname">volume_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_civo.VolumeAttachment.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Volume to be attached to the instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.VolumeAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.VolumeAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VolumeAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the instance to attach the volume to.</p></li>
<li><p><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the Volume to be attached to the instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_civo.VolumeAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.VolumeAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.VolumeAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_dns_domain_name</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.get_dns_domain_name" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_dns_domain_record</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domain_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.get_dns_domain_record" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.get_instance" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_instances</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.get_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – Filter the results.
The <code class="docutils literal notranslate"><span class="pre">filter</span></code> block is documented below.</p></li>
<li><p><strong>sorts</strong> (<em>list</em>) – Sort the results.
The <code class="docutils literal notranslate"><span class="pre">sort</span></code> block is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Filter the Instances by this key. This may be one of ‘<code class="docutils literal notranslate"><span class="pre">id</span></code>, <code class="docutils literal notranslate"><span class="pre">hostname</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ip</span></code>, <code class="docutils literal notranslate"><span class="pre">private_ip</span></code>,
<code class="docutils literal notranslate"><span class="pre">pseudo_ip</span></code>, <code class="docutils literal notranslate"><span class="pre">size</span></code>, <code class="docutils literal notranslate"><span class="pre">cpu_cores</span></code>, <code class="docutils literal notranslate"><span class="pre">ram_mb</span></code>, <code class="docutils literal notranslate"><span class="pre">disk_gb</span></code>, <code class="docutils literal notranslate"><span class="pre">template</span></code> or <code class="docutils literal notranslate"><span class="pre">created_at</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of values to match against the <code class="docutils literal notranslate"><span class="pre">key</span></code> field. Only retrieves Instances
where the <code class="docutils literal notranslate"><span class="pre">key</span></code> field takes on one or more of the values provided here.</p></li>
</ul>
<p>The <strong>sorts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">direction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The sort direction. This may be either <code class="docutils literal notranslate"><span class="pre">asc</span></code> or <code class="docutils literal notranslate"><span class="pre">desc</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Sort the Instance by this key. This may be one of <code class="docutils literal notranslate"><span class="pre">id</span></code>, <code class="docutils literal notranslate"><span class="pre">hostname</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ip</span></code>, <code class="docutils literal notranslate"><span class="pre">private_ip</span></code>,
<code class="docutils literal notranslate"><span class="pre">pseudo_ip</span></code>, <code class="docutils literal notranslate"><span class="pre">size</span></code>, <code class="docutils literal notranslate"><span class="pre">cpu_cores</span></code>, <code class="docutils literal notranslate"><span class="pre">ram_mb</span></code>, <code class="docutils literal notranslate"><span class="pre">disk_gb</span></code>, <code class="docutils literal notranslate"><span class="pre">template</span></code> or <code class="docutils literal notranslate"><span class="pre">created_at</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_instances_size">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_instances_size</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.get_instances_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
<p>The <strong>sorts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">direction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_kubernetes_cluster">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_kubernetes_cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.get_kubernetes_cluster" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_kubernetes_version</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.get_kubernetes_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides access to the available Civo Kubernetes Service versions, with the ability to filter the results.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">stable</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">get_kubernetes_version</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;type&quot;</span><span class="p">,</span>
    <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;stable&quot;</span><span class="p">],</span>
<span class="p">}])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_civo</span> <span class="k">as</span> <span class="nn">civo</span>

<span class="n">minor_version</span> <span class="o">=</span> <span class="n">civo</span><span class="o">.</span><span class="n">get_kubernetes_version</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;version&quot;</span><span class="p">,</span>
    <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;0.9.1&quot;</span><span class="p">],</span>
<span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – Filter the results.
The <code class="docutils literal notranslate"><span class="pre">filter</span></code> block is documented below.</p></li>
<li><p><strong>sorts</strong> (<em>list</em>) – Sort the results.
The <code class="docutils literal notranslate"><span class="pre">sort</span></code> block is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Filter the sizes by this key. This may be one of <code class="docutils literal notranslate"><span class="pre">version</span></code>,
<code class="docutils literal notranslate"><span class="pre">label</span></code>, <code class="docutils literal notranslate"><span class="pre">type</span></code>, <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Only retrieves the version which keys has value that matches
one of the values provided here.</p></li>
</ul>
<p>The <strong>sorts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">direction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The sort direction. This may be either <code class="docutils literal notranslate"><span class="pre">asc</span></code> or <code class="docutils literal notranslate"><span class="pre">desc</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Sort the sizes by this key. This may be one of <code class="docutils literal notranslate"><span class="pre">version</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_load_balancer">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_load_balancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.get_load_balancer" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_network</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">label</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.get_network" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_snapshot</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.get_snapshot" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_ssh_key</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.get_ssh_key" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_template</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sorts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.get_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – Filter the results.
The <code class="docutils literal notranslate"><span class="pre">filter</span></code> block is documented below.</p></li>
<li><p><strong>sorts</strong> (<em>list</em>) – Sort the results.
The <code class="docutils literal notranslate"><span class="pre">sort</span></code> block is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Filter the sizes by this key. This may be one of <code class="docutils literal notranslate"><span class="pre">code</span></code>,
<code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Only retrieves the template which keys has value that matches
one of the values provided here.</p></li>
</ul>
<p>The <strong>sorts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">direction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The sort direction. This may be either <code class="docutils literal notranslate"><span class="pre">asc</span></code> or <code class="docutils literal notranslate"><span class="pre">desc</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Sort the sizes by this key. This may be one of <code class="docutils literal notranslate"><span class="pre">code</span></code>, 
<code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_civo.get_volume">
<code class="sig-prename descclassname">pulumi_civo.</code><code class="sig-name descname">get_volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_civo.get_volume" title="Permalink to this definition">¶</a></dt>
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
