---
title: Module provider
title_tag: Module provider | Package pulumi_kubernetes | Python SDK
linktitle: provider
notitle: true
---

<div class="section" id="module-pulumi_kubernetes.provider">
<span id="provider"></span><h1>provider<a class="headerlink" href="#module-pulumi_kubernetes.provider" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_kubernetes.provider.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kubernetes.provider.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param">__name__</em>, <em class="sig-param">__opts__=None</em>, <em class="sig-param">cluster=None</em>, <em class="sig-param">context=None</em>, <em class="sig-param">enable_dry_run=None</em>, <em class="sig-param">kubeconfig=None</em>, <em class="sig-param">namespace=None</em>, <em class="sig-param">suppress_deprecation_warnings=None</em>, <em class="sig-param">render_yaml_to_directory=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kubernetes.provider.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the kubernetes package.</p>
<p>Create a Provider resource with the given unique name, arguments, and options.</p>
<p>:param str <strong>name</strong>: The unique name of the resource.
:param pulumi.ResourceOptions <strong>opts</strong>: An optional bag of options that controls this resource’s behavior.
:param pulumi.Input[str] cluster: If present, the name of the kubeconfig cluster to use.
:param pulumi.Input[str] context: If present, the name of the kubeconfig context to use.
:param pulumi.Input[bool] enable_dry_run: BETA FEATURE - If present and set to True, enable server-side diff</p>
<blockquote>
<div><p>calculations. This feature is in developer preview, and is disabled by default.
This config can be specified in the following ways, using this precedence:</p>
</div></blockquote>
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
