---
title: Package pulumi_dnsimple
title_tag: Package pulumi_dnsimple | Python SDK
linktitle: pulumi_dnsimple
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "dnsimple" >}}

<div class="section" id="pulumi-dnsimple">
<h1>Pulumi DNSimple<a class="headerlink" href="#pulumi-dnsimple" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-dnsimple">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-dnsimple/issues">pulumi/pulumi-dnsimple repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-dnsimple/issues">terraform-providers/terraform-provider-dnsimple repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_dnsimple"></span><dl class="py class">
<dt id="pulumi_dnsimple.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_dnsimple.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_dnsimple.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the dnsimple package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account for API operations.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API v2 token for API operations.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_dnsimple.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_dnsimple.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_dnsimple.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_dnsimple.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_dnsimple.Record">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_dnsimple.</code><code class="sig-name descname">Record</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_dnsimple.Record" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DNSimple record resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_dnsimple</span> <span class="k">as</span> <span class="nn">dnsimple</span>

<span class="c1"># Add a record to the root domain</span>
<span class="n">foobar</span> <span class="o">=</span> <span class="n">dnsimple</span><span class="o">.</span><span class="n">Record</span><span class="p">(</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;dnsimple_domain&quot;</span><span class="p">],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
    <span class="n">ttl</span><span class="o">=</span><span class="mi">3600</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;A&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;192.168.0.11&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_dnsimple</span> <span class="k">as</span> <span class="nn">dnsimple</span>

<span class="c1"># Add a record to a sub-domain</span>
<span class="n">foobar</span> <span class="o">=</span> <span class="n">dnsimple</span><span class="o">.</span><span class="n">Record</span><span class="p">(</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;dnsimple_domain&quot;</span><span class="p">],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;terraform&quot;</span><span class="p">,</span>
    <span class="n">ttl</span><span class="o">=</span><span class="mi">3600</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;A&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;192.168.0.11&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain to add the record to</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the record - only useful for some record types</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TTL of the record</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the record</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the record</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_dnsimple.Record.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_dnsimple.record.Record<a class="headerlink" href="#pulumi_dnsimple.Record.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Record resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain to add the record to</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain ID of the record</p></li>
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN of the record</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the record - only useful for some record types</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TTL of the record</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the record</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the record</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_dnsimple.Record.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_dnsimple.Record.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain to add the record to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_dnsimple.Record.domain_id">
<em class="property">property </em><code class="sig-name descname">domain_id</code><a class="headerlink" href="#pulumi_dnsimple.Record.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain ID of the record</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_dnsimple.Record.hostname">
<em class="property">property </em><code class="sig-name descname">hostname</code><a class="headerlink" href="#pulumi_dnsimple.Record.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the record</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_dnsimple.Record.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_dnsimple.Record.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the record</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_dnsimple.Record.priority">
<em class="property">property </em><code class="sig-name descname">priority</code><a class="headerlink" href="#pulumi_dnsimple.Record.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the record - only useful for some record types</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_dnsimple.Record.ttl">
<em class="property">property </em><code class="sig-name descname">ttl</code><a class="headerlink" href="#pulumi_dnsimple.Record.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL of the record</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_dnsimple.Record.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_dnsimple.Record.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the record</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_dnsimple.Record.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_dnsimple.Record.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the record</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_dnsimple.Record.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_dnsimple.Record.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_dnsimple.Record.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_dnsimple.Record.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
