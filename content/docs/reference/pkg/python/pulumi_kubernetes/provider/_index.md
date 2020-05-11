---
title: Module provider
title_tag: Module provider | Package pulumi_kubernetes | Python SDK
linktitle: provider
notitle: true
---

<div class="section" id="module-pulumi_kubernetes.provider">
<span id="provider"></span><h1>provider<a class="headerlink" href="#module-pulumi_kubernetes.provider" title="Permalink to this headline">¶</a></h1>
<dl class="py class">
<dt id="pulumi_kubernetes.provider.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.provider.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_dry_run</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubeconfig</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suppress_deprecation_warnings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">render_yaml_to_directory</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.provider.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the kubernetes package.</p>
<p>Create a Provider resource with the given unique name, arguments, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – An optional bag of options that controls this resource’s behavior.</p></li>
<li><p><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If present, the name of the kubeconfig cluster to use.</p></li>
<li><p><strong>context</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If present, the name of the kubeconfig context to use.</p></li>
<li><p><strong>enable_dry_run</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – BETA FEATURE - If present and set to True, enable server-side diff
calculations. This feature is in developer preview, and is disabled by default.
This config can be specified in the following ways, using this precedence:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>1. This `enableDryRun` parameter.
2. The `PULUMI_K8S_ENABLE_DRY_RUN` environment variable.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>kubeconfig</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of a kubeconfig file.
If this is set, this config will be used instead of $KUBECONFIG.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If present, the default namespace to use.
This flag is ignored for cluster-scoped resources.
A namespace can be specified in multiple places, and the precedence is as follows:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>1. `.metadata.namespace` set on the resource.
2. This `namespace` parameter.
3. `namespace` set for the active context in the kubeconfig.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>suppress_deprecation_warnings</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If present and set to True, suppress apiVersion
deprecation warnings from the CLI.
This config can be specified in the following ways, using this precedence:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>1. This `suppressDeprecationWarnings` parameter.
2. The `PULUMI_K8S_SUPPRESS_DEPRECATION_WARNINGS` environment variable.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>render_yaml_to_directory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BETA FEATURE - If present, render resource manifests to this
directory. In this mode, resources will not be created on a Kubernetes cluster, but
the rendered manifests will be kept in sync with changes to the Pulumi program.
This feature is in developer preview, and is disabled by default. Note that some
computed Outputs such as status fields will not be populated since the resources are
not created on a Kubernetes cluster. These Output values will remain undefined,
and may result in an error if they are referenced by other resources. Also note that
any secret values used in these resources will be rendered in plaintext to the
resulting YAML.</p>
</dd>
</dl>
</dd></dl>

</div>
