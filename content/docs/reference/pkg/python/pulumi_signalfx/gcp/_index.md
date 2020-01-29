---
title: Module gcp
title_tag: Module gcp | Package pulumi_signalfx | Python SDK
linktitle: gcp
notitle: true
---

<div class="section" id="gcp">
<h1>gcp<a class="headerlink" href="#gcp" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-signalfx/issues">pulumi/pulumi-signalfx repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/issues">terraform-providers/terraform-provider-signalfx repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_signalfx.gcp"></span><dl class="class">
<dt id="pulumi_signalfx.gcp.Integration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.gcp.</code><code class="sig-name descname">Integration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">poll_rate=None</em>, <em class="sig-param">project_service_keys=None</em>, <em class="sig-param">services=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.gcp.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>SignalFx GCP Integration</p>
<p><strong>Note:</strong> When managing integrations you’ll need to use an admin token to authenticate the SignalFx provider. Otherwise you’ll receive a 4xx error.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the integration is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the integration.</p></li>
<li><p><strong>poll_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – GCP integration poll rate in seconds. Can be set to either 60 or 300 (1 minute or 5 minutes).</p></li>
<li><p><strong>project_service_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – GCP projects to add.</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – GCP service metrics to import. Can be an empty list, or not included, to import ‘All services’.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>project_service_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/gcp_integration.html.markdown">https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/gcp_integration.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_signalfx.gcp.Integration.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.gcp.Integration.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the integration is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.gcp.Integration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.gcp.Integration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the integration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.gcp.Integration.poll_rate">
<code class="sig-name descname">poll_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.gcp.Integration.poll_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>GCP integration poll rate in seconds. Can be set to either 60 or 300 (1 minute or 5 minutes).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.gcp.Integration.project_service_keys">
<code class="sig-name descname">project_service_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.gcp.Integration.project_service_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>GCP projects to add.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.gcp.Integration.services">
<code class="sig-name descname">services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.gcp.Integration.services" title="Permalink to this definition">¶</a></dt>
<dd><p>GCP service metrics to import. Can be an empty list, or not included, to import ‘All services’.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_signalfx.gcp.Integration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">poll_rate=None</em>, <em class="sig-param">project_service_keys=None</em>, <em class="sig-param">services=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.gcp.Integration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Integration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the integration is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the integration.</p></li>
<li><p><strong>poll_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – GCP integration poll rate in seconds. Can be set to either 60 or 300 (1 minute or 5 minutes).</p></li>
<li><p><strong>project_service_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – GCP projects to add.</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – GCP service metrics to import. Can be an empty list, or not included, to import ‘All services’.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>project_service_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">projectId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/gcp_integration.html.markdown">https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/gcp_integration.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_signalfx.gcp.Integration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.gcp.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.gcp.Integration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.gcp.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
