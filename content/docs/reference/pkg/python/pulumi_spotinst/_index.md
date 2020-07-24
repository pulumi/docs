---
title: Package pulumi_spotinst
title_tag: Package pulumi_spotinst | Python SDK
linktitle: pulumi_spotinst
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "spotinst" >}}

<div class="section" id="pulumi-spotinst">
<h1>Pulumi SpotInst<a class="headerlink" href="#pulumi-spotinst" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-spotinst/issues">pulumi/pulumi-spotinst repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/issues">terraform-providers/terraform-provider-spotinst repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_spotinst"></span><dl class="py class">
<dt id="pulumi_spotinst.HealthCheck">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.</code><code class="sig-name descname">HealthCheck</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.HealthCheck" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst Health Check resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">http_check</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">HealthCheck</span><span class="p">(</span><span class="s2">&quot;httpCheck&quot;</span><span class="p">,</span>
    <span class="n">check</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;endpoint&quot;</span><span class="p">:</span> <span class="s2">&quot;http://endpoint.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;healthy&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
        <span class="s2">&quot;interval&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">1337</span><span class="p">,</span>
        <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;http&quot;</span><span class="p">,</span>
        <span class="s2">&quot;timeout&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
        <span class="s2">&quot;unhealthy&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">proxy_address</span><span class="o">=</span><span class="s2">&quot;http://proxy.com&quot;</span><span class="p">,</span>
    <span class="n">proxy_port</span><span class="o">=</span><span class="mi">80</span><span class="p">,</span>
    <span class="n">resource_id</span><span class="o">=</span><span class="s2">&quot;sig-123&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the check to execute.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the health check.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource to check.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The destination for the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of consecutive successful health checks that must occur before declaring an instance healthy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of time (in seconds) between each health check (minimum: 10).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port of the Spotinst HCS (default: 80).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol to use to connect with the instance. Valid values: http, https.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - the amount of time (in seconds) to wait when receiving a response from the health check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unhealthy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of consecutive failed health checks that must occur before declaring an instance unhealthy.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.HealthCheck.check">
<code class="sig-name descname">check</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.HealthCheck.check" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the check to execute.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The destination for the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthy</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of consecutive successful health checks that must occur before declaring an instance healthy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The amount of time (in seconds) between each health check (minimum: 10).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port of the Spotinst HCS (default: 80).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The protocol to use to connect with the instance. Valid values: http, https.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - the amount of time (in seconds) to wait when receiving a response from the health check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unhealthy</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of consecutive failed health checks that must occur before declaring an instance unhealthy.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.HealthCheck.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.HealthCheck.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the health check.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.HealthCheck.resource_id">
<code class="sig-name descname">resource_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.HealthCheck.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the resource to check.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.HealthCheck.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.HealthCheck.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HealthCheck resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the check to execute.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the health check.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource to check.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The destination for the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">healthy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of consecutive successful health checks that must occur before declaring an instance healthy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The amount of time (in seconds) between each health check (minimum: 10).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port of the Spotinst HCS (default: 80).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol to use to connect with the instance. Valid values: http, https.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - the amount of time (in seconds) to wait when receiving a response from the health check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unhealthy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of consecutive failed health checks that must occur before declaring an instance unhealthy.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.HealthCheck.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.HealthCheck.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.HealthCheck.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.HealthCheck.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">feature_flags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the spotinst package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Spotinst Account ID</p></li>
<li><p><strong>feature_flags</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Spotinst SDK Feature Flags</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Spotinst Personal API Access Token</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_spotinst.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.Subscription">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.</code><code class="sig-name descname">Subscription</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.Subscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst subscription resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="c1"># Create a Subscription</span>
<span class="n">default_subscription</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">Subscription</span><span class="p">(</span><span class="s2">&quot;default-subscription&quot;</span><span class="p">,</span>
    <span class="n">endpoint</span><span class="o">=</span><span class="s2">&quot;http://endpoint.com&quot;</span><span class="p">,</span>
    <span class="n">event_type</span><span class="o">=</span><span class="s2">&quot;AWS_EC2_INSTANCE_LAUNCH&quot;</span><span class="p">,</span>
    <span class="nb">format</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;event&quot;</span><span class="p">:</span> <span class="s2">&quot;</span><span class="si">%e</span><span class="s2">vent%&quot;</span><span class="p">,</span>
        <span class="s2">&quot;instance_id&quot;</span><span class="p">:</span> <span class="s2">&quot;</span><span class="si">%i</span><span class="s2">nstance-id%&quot;</span><span class="p">,</span>
        <span class="s2">&quot;resource_id&quot;</span><span class="p">:</span> <span class="s2">&quot;</span><span class="si">%r</span><span class="s2">esource-id%&quot;</span><span class="p">,</span>
        <span class="s2">&quot;resource_name&quot;</span><span class="p">:</span> <span class="s2">&quot;</span><span class="si">%r</span><span class="s2">esource-name%&quot;</span><span class="p">,</span>
        <span class="s2">&quot;tags&quot;</span><span class="p">:</span> <span class="s2">&quot;foo,baz,baz&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">protocol</span><span class="o">=</span><span class="s2">&quot;http&quot;</span><span class="p">,</span>
    <span class="n">resource_id</span><span class="o">=</span><span class="n">spotinst_elastigroup_aws</span><span class="p">[</span><span class="s2">&quot;my-eg&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint the notification will be sent to. url in case of <code class="docutils literal notranslate"><span class="pre">&quot;http&quot;</span></code>/<code class="docutils literal notranslate"><span class="pre">&quot;https&quot;</span></code>/<code class="docutils literal notranslate"><span class="pre">&quot;web&quot;</span></code>, email address in case of <code class="docutils literal notranslate"><span class="pre">&quot;email&quot;</span></code>/<code class="docutils literal notranslate"><span class="pre">&quot;email-json&quot;</span></code> and sns-topic-arn in case of <code class="docutils literal notranslate"><span class="pre">&quot;aws-sns&quot;</span></code>.</p></li>
<li><p><strong>event_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The event to send the notification when triggered. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_TERMINATE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_TERMINATED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_LAUNCH&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_READY_SIGNAL_TIMEOUT&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_CANT_SPIN_OD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_UNHEALTHY_IN_ELB&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;GROUP_ROLL_FAILED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;GROUP_ROLL_FINISHED&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;CANT_SCALE_UP_GROUP_MAX_CAPACITY&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;GROUP_UPDATED&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EMR_PROVISION_TIMEOUT&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;GROUP_BEANSTALK_INIT_READY&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AZURE_VM_TERMINATED&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AZURE_VM_TERMINATE&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_MANAGED_INSTANCE_PAUSING&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_MANAGED_INSTANCE_RESUMING&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_MANAGED_INSTANCE_RECYCLING&quot;</span></code>,<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_MANAGED_INSTANCE_DELETING&quot;</span></code>.
Ocean Events:<code class="docutils literal notranslate"><span class="pre">&quot;CLUSTER_ROLL_FINISHED&quot;</span></code>,<code class="docutils literal notranslate"><span class="pre">&quot;GROUP_ROLL_FAILED&quot;</span></code>.</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The format of the notification content (JSON Format - Key+Value). Valid Values : <code class="docutils literal notranslate"><span class="pre">&quot;instance-id&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;event&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;resource-id&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;resource-name&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;subnet-id&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;availability-zone&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;reason&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;private-ip&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;launchspec-id&quot;</span></code>
Example: {“event”: <code class="docutils literal notranslate"><span class="pre">&quot;event&quot;</span></code>, <cite>“resourceId”</cite>: <cite>“resource-id”</cite>, <cite>“resourceName”</cite>: <code class="docutils literal notranslate"><span class="pre">&quot;resource-name&quot;</span></code>”, <code class="docutils literal notranslate"><span class="pre">&quot;myCustomKey&quot;</span></code>: <code class="docutils literal notranslate"><span class="pre">&quot;My</span> <span class="pre">content</span> <span class="pre">is</span> <span class="pre">set</span> <span class="pre">here&quot;</span></code> }
Default: {<cite>“event”</cite>: <cite>“&lt;event&gt;”</cite>, <cite>“instanceId”</cite>: <code class="docutils literal notranslate"><span class="pre">&quot;&lt;instance-id&gt;&quot;</span></code>, <cite>“resourceId”</cite>: <cite>“&lt;resource-id&gt;”</cite>, <cite>“resourceName”</cite>: <code class="docutils literal notranslate"><span class="pre">&quot;&lt;resource-name&gt;&quot;</span></code> }.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to send the notification. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;email&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;email-json&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;aws-sns&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;web&quot;</span></code>. 
The following values are deprecated: <code class="docutils literal notranslate"><span class="pre">&quot;http&quot;</span></code> , <code class="docutils literal notranslate"><span class="pre">&quot;https&quot;</span></code>
You can use the generic <code class="docutils literal notranslate"><span class="pre">&quot;web&quot;</span></code> protocol instead.
<code class="docutils literal notranslate"><span class="pre">&quot;aws-sns&quot;</span></code> is only supported with AWS provider</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Spotinst Resource id (Elastigroup or Ocean ID).</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_spotinst.Subscription.endpoint">
<code class="sig-name descname">endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.Subscription.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint the notification will be sent to. url in case of <code class="docutils literal notranslate"><span class="pre">&quot;http&quot;</span></code>/<code class="docutils literal notranslate"><span class="pre">&quot;https&quot;</span></code>/<code class="docutils literal notranslate"><span class="pre">&quot;web&quot;</span></code>, email address in case of <code class="docutils literal notranslate"><span class="pre">&quot;email&quot;</span></code>/<code class="docutils literal notranslate"><span class="pre">&quot;email-json&quot;</span></code> and sns-topic-arn in case of <code class="docutils literal notranslate"><span class="pre">&quot;aws-sns&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.Subscription.event_type">
<code class="sig-name descname">event_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.Subscription.event_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The event to send the notification when triggered. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_TERMINATE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_TERMINATED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_LAUNCH&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_READY_SIGNAL_TIMEOUT&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_CANT_SPIN_OD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_UNHEALTHY_IN_ELB&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;GROUP_ROLL_FAILED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;GROUP_ROLL_FINISHED&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;CANT_SCALE_UP_GROUP_MAX_CAPACITY&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;GROUP_UPDATED&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EMR_PROVISION_TIMEOUT&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;GROUP_BEANSTALK_INIT_READY&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AZURE_VM_TERMINATED&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AZURE_VM_TERMINATE&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_MANAGED_INSTANCE_PAUSING&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_MANAGED_INSTANCE_RESUMING&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_MANAGED_INSTANCE_RECYCLING&quot;</span></code>,<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_MANAGED_INSTANCE_DELETING&quot;</span></code>.
Ocean Events:<code class="docutils literal notranslate"><span class="pre">&quot;CLUSTER_ROLL_FINISHED&quot;</span></code>,<code class="docutils literal notranslate"><span class="pre">&quot;GROUP_ROLL_FAILED&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.Subscription.format">
<code class="sig-name descname">format</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.Subscription.format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of the notification content (JSON Format - Key+Value). Valid Values : <code class="docutils literal notranslate"><span class="pre">&quot;instance-id&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;event&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;resource-id&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;resource-name&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;subnet-id&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;availability-zone&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;reason&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;private-ip&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;launchspec-id&quot;</span></code>
Example: {“event”: <code class="docutils literal notranslate"><span class="pre">&quot;event&quot;</span></code>, <cite>“resourceId”</cite>: <cite>“resource-id”</cite>, <cite>“resourceName”</cite>: <code class="docutils literal notranslate"><span class="pre">&quot;resource-name&quot;</span></code>”, <code class="docutils literal notranslate"><span class="pre">&quot;myCustomKey&quot;</span></code>: <code class="docutils literal notranslate"><span class="pre">&quot;My</span> <span class="pre">content</span> <span class="pre">is</span> <span class="pre">set</span> <span class="pre">here&quot;</span></code> }
Default: {<cite>“event”</cite>: <cite>“&lt;event&gt;”</cite>, <cite>“instanceId”</cite>: <code class="docutils literal notranslate"><span class="pre">&quot;&lt;instance-id&gt;&quot;</span></code>, <cite>“resourceId”</cite>: <cite>“&lt;resource-id&gt;”</cite>, <cite>“resourceName”</cite>: <code class="docutils literal notranslate"><span class="pre">&quot;&lt;resource-name&gt;&quot;</span></code> }.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.Subscription.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.Subscription.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to send the notification. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;email&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;email-json&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;aws-sns&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;web&quot;</span></code>. 
The following values are deprecated: <code class="docutils literal notranslate"><span class="pre">&quot;http&quot;</span></code> , <code class="docutils literal notranslate"><span class="pre">&quot;https&quot;</span></code>
You can use the generic <code class="docutils literal notranslate"><span class="pre">&quot;web&quot;</span></code> protocol instead.
<code class="docutils literal notranslate"><span class="pre">&quot;aws-sns&quot;</span></code> is only supported with AWS provider</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.Subscription.resource_id">
<code class="sig-name descname">resource_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.Subscription.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Spotinst Resource id (Elastigroup or Ocean ID).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.Subscription.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">format</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.Subscription.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Subscription resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint the notification will be sent to. url in case of <code class="docutils literal notranslate"><span class="pre">&quot;http&quot;</span></code>/<code class="docutils literal notranslate"><span class="pre">&quot;https&quot;</span></code>/<code class="docutils literal notranslate"><span class="pre">&quot;web&quot;</span></code>, email address in case of <code class="docutils literal notranslate"><span class="pre">&quot;email&quot;</span></code>/<code class="docutils literal notranslate"><span class="pre">&quot;email-json&quot;</span></code> and sns-topic-arn in case of <code class="docutils literal notranslate"><span class="pre">&quot;aws-sns&quot;</span></code>.</p></li>
<li><p><strong>event_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The event to send the notification when triggered. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_TERMINATE&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_TERMINATED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_LAUNCH&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_READY_SIGNAL_TIMEOUT&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_CANT_SPIN_OD&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_INSTANCE_UNHEALTHY_IN_ELB&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;GROUP_ROLL_FAILED&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;GROUP_ROLL_FINISHED&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;CANT_SCALE_UP_GROUP_MAX_CAPACITY&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;GROUP_UPDATED&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EMR_PROVISION_TIMEOUT&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;GROUP_BEANSTALK_INIT_READY&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AZURE_VM_TERMINATED&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AZURE_VM_TERMINATE&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_MANAGED_INSTANCE_PAUSING&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_MANAGED_INSTANCE_RESUMING&quot;</span></code>,
<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_MANAGED_INSTANCE_RECYCLING&quot;</span></code>,<code class="docutils literal notranslate"><span class="pre">&quot;AWS_EC2_MANAGED_INSTANCE_DELETING&quot;</span></code>.
Ocean Events:<code class="docutils literal notranslate"><span class="pre">&quot;CLUSTER_ROLL_FINISHED&quot;</span></code>,<code class="docutils literal notranslate"><span class="pre">&quot;GROUP_ROLL_FAILED&quot;</span></code>.</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The format of the notification content (JSON Format - Key+Value). Valid Values : <code class="docutils literal notranslate"><span class="pre">&quot;instance-id&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;event&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;resource-id&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;resource-name&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;subnet-id&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;availability-zone&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;reason&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;private-ip&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;launchspec-id&quot;</span></code>
Example: {“event”: <code class="docutils literal notranslate"><span class="pre">&quot;event&quot;</span></code>, <cite>“resourceId”</cite>: <cite>“resource-id”</cite>, <cite>“resourceName”</cite>: <code class="docutils literal notranslate"><span class="pre">&quot;resource-name&quot;</span></code>”, <code class="docutils literal notranslate"><span class="pre">&quot;myCustomKey&quot;</span></code>: <code class="docutils literal notranslate"><span class="pre">&quot;My</span> <span class="pre">content</span> <span class="pre">is</span> <span class="pre">set</span> <span class="pre">here&quot;</span></code> }
Default: {<cite>“event”</cite>: <cite>“&lt;event&gt;”</cite>, <cite>“instanceId”</cite>: <code class="docutils literal notranslate"><span class="pre">&quot;&lt;instance-id&gt;&quot;</span></code>, <cite>“resourceId”</cite>: <cite>“&lt;resource-id&gt;”</cite>, <cite>“resourceName”</cite>: <code class="docutils literal notranslate"><span class="pre">&quot;&lt;resource-name&gt;&quot;</span></code> }.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to send the notification. Valid values: <code class="docutils literal notranslate"><span class="pre">&quot;email&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;email-json&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;aws-sns&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;web&quot;</span></code>. 
The following values are deprecated: <code class="docutils literal notranslate"><span class="pre">&quot;http&quot;</span></code> , <code class="docutils literal notranslate"><span class="pre">&quot;https&quot;</span></code>
You can use the generic <code class="docutils literal notranslate"><span class="pre">&quot;web&quot;</span></code> protocol instead.
<code class="docutils literal notranslate"><span class="pre">&quot;aws-sns&quot;</span></code> is only supported with AWS provider</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Spotinst Resource id (Elastigroup or Ocean ID).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.Subscription.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.Subscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.Subscription.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.Subscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
