---
title: Module multai
title_tag: Module multai | Package pulumi_spotinst | Python SDK
linktitle: multai
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "spotinst" >}}

<div class="section" id="multai">
<h1>multai<a class="headerlink" href="#multai" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-spotinst/issues">pulumi/pulumi-spotinst repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-spotinst/issues">terraform-providers/terraform-provider-spotinst repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_spotinst.multai"></span><dl class="py class">
<dt id="pulumi_spotinst.multai.Balancer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.multai.</code><code class="sig-name descname">Balancer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_timeouts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_cname_aliases</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Balancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst Multai Balancer.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">my_balancer</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">multai</span><span class="o">.</span><span class="n">Balancer</span><span class="p">(</span><span class="s2">&quot;myBalancer&quot;</span><span class="p">,</span>
    <span class="n">connection_timeouts</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;draining&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
        <span class="s2">&quot;idle&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">scheme</span><span class="o">=</span><span class="s2">&quot;internal&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;env&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;prod&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The balancer name. May contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of key:value paired tags.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>connection_timeouts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">draining</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time for the load balancer to keep connections alive before reporting the target as de-registered, in seconds (range: 1 - 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The idle timeout value, in seconds. (range: 1 - 3600).</p></li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s value.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Balancer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Balancer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The balancer name. May contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Balancer.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Balancer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of key:value paired tags.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag’s value.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.multai.Balancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_timeouts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_cname_aliases</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Balancer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Balancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The balancer name. May contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of key:value paired tags.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>connection_timeouts</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">draining</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time for the load balancer to keep connections alive before reporting the target as de-registered, in seconds (range: 1 - 3600).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The idle timeout value, in seconds. (range: 1 - 3600).</p></li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s value.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.multai.Balancer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Balancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.multai.Balancer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Balancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.multai.Deployment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.multai.</code><code class="sig-name descname">Deployment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst Multai Deployment.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">my_deployment</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">multai</span><span class="o">.</span><span class="n">Deployment</span><span class="p">(</span><span class="s2">&quot;myDeployment&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deployment name.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Deployment.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Deployment.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The deployment name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.multai.Deployment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Deployment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Deployment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deployment name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.multai.Deployment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Deployment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.multai.Deployment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Deployment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.multai.Listener">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.multai.</code><code class="sig-name descname">Listener</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Listener" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst Multai Listener.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">my_listener</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">multai</span><span class="o">.</span><span class="n">Listener</span><span class="p">(</span><span class="s2">&quot;myListener&quot;</span><span class="p">,</span>
    <span class="n">balancer_id</span><span class="o">=</span><span class="s2">&quot;b-12345&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">port</span><span class="o">=</span><span class="mi">1337</span><span class="p">,</span>
    <span class="n">protocol</span><span class="o">=</span><span class="s2">&quot;http&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;env&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;prod&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">tls_config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;certificateIds&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;ce-12345&quot;</span><span class="p">],</span>
        <span class="s2">&quot;cipherSuites&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;&quot;</span><span class="p">],</span>
        <span class="s2">&quot;maxVersion&quot;</span><span class="p">:</span> <span class="s2">&quot;TLS12&quot;</span><span class="p">,</span>
        <span class="s2">&quot;minVersion&quot;</span><span class="p">:</span> <span class="s2">&quot;TLS10&quot;</span><span class="p">,</span>
        <span class="s2">&quot;preferServerCipherSuites&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;sessionTicketsDisabled&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the balancer.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the load balancer is listening.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to allow connections to the load balancer.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of key:value paired tags.</p></li>
<li><p><strong>tls_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the TLSConfig configuration.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s value.</p></li>
</ul>
<p>The <strong>tls_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificateIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Contains one or more certificate chains to present to the other side of the connection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cipherSuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of supported cipher suites. If cipherSuites is nil, TLS uses a list of suites supported by the implementation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - MaxVersion contains the maximum SSL/TLS version that is acceptable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - MinVersion contains the minimum SSL/TLS version that is acceptable (1.0 is the minimum).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preferServerCipherSuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Controls whether the server selects the client’s most preferred ciphersuite, or the server’s most preferred ciphersuite.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTicketsDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - May be set to true to disable session ticket (resumption) support.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Listener.balancer_id">
<code class="sig-name descname">balancer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Listener.balancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the balancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Listener.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Listener.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which the load balancer is listening.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Listener.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Listener.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to allow connections to the load balancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Listener.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Listener.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of key:value paired tags.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag’s value.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Listener.tls_config">
<code class="sig-name descname">tls_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Listener.tls_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the TLSConfig configuration.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificateIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Contains one or more certificate chains to present to the other side of the connection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cipherSuites</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of supported cipher suites. If cipherSuites is nil, TLS uses a list of suites supported by the implementation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - MaxVersion contains the maximum SSL/TLS version that is acceptable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - MinVersion contains the minimum SSL/TLS version that is acceptable (1.0 is the minimum).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preferServerCipherSuites</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Controls whether the server selects the client’s most preferred ciphersuite, or the server’s most preferred ciphersuite.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTicketsDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - May be set to true to disable session ticket (resumption) support.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.multai.Listener.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_config</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Listener.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Listener resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the balancer.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the load balancer is listening.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to allow connections to the load balancer.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of key:value paired tags.</p></li>
<li><p><strong>tls_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Describes the TLSConfig configuration.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s value.</p></li>
</ul>
<p>The <strong>tls_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificateIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Contains one or more certificate chains to present to the other side of the connection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cipherSuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of supported cipher suites. If cipherSuites is nil, TLS uses a list of suites supported by the implementation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - MaxVersion contains the maximum SSL/TLS version that is acceptable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - MinVersion contains the minimum SSL/TLS version that is acceptable (1.0 is the minimum).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preferServerCipherSuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Controls whether the server selects the client’s most preferred ciphersuite, or the server’s most preferred ciphersuite.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sessionTicketsDisabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - May be set to true to disable session ticket (resumption) support.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.multai.Listener.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Listener.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.multai.Listener.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Listener.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.multai.RoutingRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.multai.</code><code class="sig-name descname">RoutingRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">middleware_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_set_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.RoutingRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst Multai Routing Rule.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">my_routing_rule</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">multai</span><span class="o">.</span><span class="n">RoutingRule</span><span class="p">(</span><span class="s2">&quot;myRoutingRule&quot;</span><span class="p">,</span>
    <span class="n">balancer_id</span><span class="o">=</span><span class="s2">&quot;b-12345&quot;</span><span class="p">,</span>
    <span class="n">listener_id</span><span class="o">=</span><span class="s2">&quot;l-98765&quot;</span><span class="p">,</span>
    <span class="n">route</span><span class="o">=</span><span class="s2">&quot;Path(`/bar`)&quot;</span><span class="p">,</span>
    <span class="n">strategy</span><span class="o">=</span><span class="s2">&quot;LEASTCONN&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;env&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;prod&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the balancer.</p></li>
<li><p><strong>listener_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the listener.</p></li>
<li><p><strong>route</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Route defines a simple language for matching HTTP requests and route the traffic accordingly. Route provides series of matchers that follow the syntax: Path matcher: — Path(“/foo/bar”) // trie-based PathRegexp(“/foo/.<em>”) // regexp-based Method matcher: — Method(“GET”) // trie-based MethodRegexp(“POST|PUT”) // regexp based Header matcher: — Header(“Content-Type”, “application/json”) // trie-based HeaderRegexp(“Content-Type”, “application/.</em>”) // regexp based Matchers can be combined using &amp;&amp; operator: — Method(“POST”) &amp;&amp; Path(“/v1”)</p></li>
<li><p><strong>strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Balancing strategy. Valid values: <code class="docutils literal notranslate"><span class="pre">ROUNDROBIN</span></code>, <code class="docutils literal notranslate"><span class="pre">RANDOM</span></code>, <code class="docutils literal notranslate"><span class="pre">LEASTCONN</span></code>, <code class="docutils literal notranslate"><span class="pre">IPHASH</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of key:value paired tags.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s value.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.multai.RoutingRule.balancer_id">
<code class="sig-name descname">balancer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.RoutingRule.balancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the balancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.RoutingRule.listener_id">
<code class="sig-name descname">listener_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.RoutingRule.listener_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the listener.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.RoutingRule.route">
<code class="sig-name descname">route</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.RoutingRule.route" title="Permalink to this definition">¶</a></dt>
<dd><p>Route defines a simple language for matching HTTP requests and route the traffic accordingly. Route provides series of matchers that follow the syntax: Path matcher: — Path(“/foo/bar”) // trie-based PathRegexp(“/foo/.<em>”) // regexp-based Method matcher: — Method(“GET”) // trie-based MethodRegexp(“POST|PUT”) // regexp based Header matcher: — Header(“Content-Type”, “application/json”) // trie-based HeaderRegexp(“Content-Type”, “application/.</em>”) // regexp based Matchers can be combined using &amp;&amp; operator: — Method(“POST”) &amp;&amp; Path(“/v1”)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.RoutingRule.strategy">
<code class="sig-name descname">strategy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.RoutingRule.strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>Balancing strategy. Valid values: <code class="docutils literal notranslate"><span class="pre">ROUNDROBIN</span></code>, <code class="docutils literal notranslate"><span class="pre">RANDOM</span></code>, <code class="docutils literal notranslate"><span class="pre">LEASTCONN</span></code>, <code class="docutils literal notranslate"><span class="pre">IPHASH</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.RoutingRule.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.RoutingRule.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of key:value paired tags.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag’s value.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.multai.RoutingRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">listener_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">middleware_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_set_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.RoutingRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RoutingRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the balancer.</p></li>
<li><p><strong>listener_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the listener.</p></li>
<li><p><strong>route</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Route defines a simple language for matching HTTP requests and route the traffic accordingly. Route provides series of matchers that follow the syntax: Path matcher: — Path(“/foo/bar”) // trie-based PathRegexp(“/foo/.<em>”) // regexp-based Method matcher: — Method(“GET”) // trie-based MethodRegexp(“POST|PUT”) // regexp based Header matcher: — Header(“Content-Type”, “application/json”) // trie-based HeaderRegexp(“Content-Type”, “application/.</em>”) // regexp based Matchers can be combined using &amp;&amp; operator: — Method(“POST”) &amp;&amp; Path(“/v1”)</p></li>
<li><p><strong>strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Balancing strategy. Valid values: <code class="docutils literal notranslate"><span class="pre">ROUNDROBIN</span></code>, <code class="docutils literal notranslate"><span class="pre">RANDOM</span></code>, <code class="docutils literal notranslate"><span class="pre">LEASTCONN</span></code>, <code class="docutils literal notranslate"><span class="pre">IPHASH</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of key:value paired tags.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s value.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.multai.RoutingRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.RoutingRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.multai.RoutingRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.RoutingRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.multai.Target">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.multai.</code><code class="sig-name descname">Target</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_set_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Target" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst Multai Target.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">my_target</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">multai</span><span class="o">.</span><span class="n">Target</span><span class="p">(</span><span class="s2">&quot;myTarget&quot;</span><span class="p">,</span>
    <span class="n">balancer_id</span><span class="o">=</span><span class="s2">&quot;b-12345&quot;</span><span class="p">,</span>
    <span class="n">host</span><span class="o">=</span><span class="s2">&quot;host&quot;</span><span class="p">,</span>
    <span class="n">port</span><span class="o">=</span><span class="mi">1338</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;env&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;prod&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">target_set_id</span><span class="o">=</span><span class="s2">&quot;l-98765&quot;</span><span class="p">,</span>
    <span class="n">weight</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the balancer.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address (IP or URL) of the targets to register</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Target . Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port the target will register to.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of key:value paired tags.</p></li>
<li><p><strong>target_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the target set.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Defines how traffic is distributed between targets.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s value.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Target.balancer_id">
<code class="sig-name descname">balancer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Target.balancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the balancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Target.host">
<code class="sig-name descname">host</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Target.host" title="Permalink to this definition">¶</a></dt>
<dd><p>The address (IP or URL) of the targets to register</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Target.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Target.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Target . Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Target.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Target.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port the target will register to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Target.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Target.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of key:value paired tags.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag’s value.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Target.target_set_id">
<code class="sig-name descname">target_set_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Target.target_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the target set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.Target.weight">
<code class="sig-name descname">weight</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.Target.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines how traffic is distributed between targets.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.multai.Target.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_set_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Target.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Target resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the balancer.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address (IP or URL) of the targets to register</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Target . Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port the target will register to.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of key:value paired tags.</p></li>
<li><p><strong>target_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the target set.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Defines how traffic is distributed between targets.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s value.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.multai.Target.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Target.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.multai.Target.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.Target.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.multai.TargetSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_spotinst.multai.</code><code class="sig-name descname">TargetSet</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.TargetSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Spotinst Multai Target Set.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_spotinst</span> <span class="k">as</span> <span class="nn">spotinst</span>

<span class="n">my_target_set</span> <span class="o">=</span> <span class="n">spotinst</span><span class="o">.</span><span class="n">multai</span><span class="o">.</span><span class="n">TargetSet</span><span class="p">(</span><span class="s2">&quot;myTargetSet&quot;</span><span class="p">,</span>
    <span class="n">balancer_id</span><span class="o">=</span><span class="s2">&quot;b-12345&quot;</span><span class="p">,</span>
    <span class="n">deployment_id</span><span class="o">=</span><span class="s2">&quot;dp-12345&quot;</span><span class="p">,</span>
    <span class="n">health_check</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;healthyThreshold&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span>
        <span class="s2">&quot;interval&quot;</span><span class="p">:</span> <span class="mi">20</span><span class="p">,</span>
        <span class="s2">&quot;path&quot;</span><span class="p">:</span> <span class="s2">&quot;/&quot;</span><span class="p">,</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">3001</span><span class="p">,</span>
        <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;http&quot;</span><span class="p">,</span>
        <span class="s2">&quot;timeout&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span>
        <span class="s2">&quot;unhealthyThreshold&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">port</span><span class="o">=</span><span class="mi">1338</span><span class="p">,</span>
    <span class="n">protocol</span><span class="o">=</span><span class="s2">&quot;http&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;env&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;prod&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">weight</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the balancer.</p></li>
<li><p><strong>deployment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the deployment.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Target Set. Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the load balancer is listening.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to allow connections to the target for the health check.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of key:value paired tags.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Defines how traffic is distributed between the Target Set.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Total number of allowed healthy Targets.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The interval for the health check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to perform the health check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port on which the load balancer is listening.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol to allow connections to the target for the health check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time out for the health check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unhealthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Total number of allowed unhealthy Targets.</p></li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s value.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_spotinst.multai.TargetSet.balancer_id">
<code class="sig-name descname">balancer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.TargetSet.balancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the balancer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.TargetSet.deployment_id">
<code class="sig-name descname">deployment_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.TargetSet.deployment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the deployment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.TargetSet.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.TargetSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Target Set. Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.TargetSet.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.TargetSet.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port on which the load balancer is listening.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.TargetSet.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.TargetSet.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to allow connections to the target for the health check.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.TargetSet.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.TargetSet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of key:value paired tags.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tag’s value.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_spotinst.multai.TargetSet.weight">
<code class="sig-name descname">weight</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_spotinst.multai.TargetSet.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines how traffic is distributed between the Target Set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.multai.TargetSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">balancer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_check</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.TargetSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TargetSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>balancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the balancer.</p></li>
<li><p><strong>deployment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the deployment.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Target Set. Must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port on which the load balancer is listening.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to allow connections to the target for the health check.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of key:value paired tags.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Defines how traffic is distributed between the Target Set.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>health_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">healthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Total number of allowed healthy Targets.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The interval for the health check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path to perform the health check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port on which the load balancer is listening.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol to allow connections to the target for the health check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time out for the health check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unhealthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Total number of allowed unhealthy Targets.</p></li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tag’s value.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_spotinst.multai.TargetSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.TargetSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_spotinst.multai.TargetSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_spotinst.multai.TargetSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
