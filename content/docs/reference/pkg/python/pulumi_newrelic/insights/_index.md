---
title: Module insights
title_tag: Module insights | Package pulumi_newrelic | Python SDK
linktitle: insights
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "newrelic" >}}

<div class="section" id="insights">
<h1>insights<a class="headerlink" href="#insights" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-newrelic/issues">pulumi/pulumi-newrelic repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic/issues">terraform-providers/terraform-provider-newrelic repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_newrelic.insights"></span><dl class="py class">
<dt id="pulumi_newrelic.insights.Event">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.insights.</code><code class="sig-name descname">Event</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.insights.Event" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create one or more Insights events.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">insights</span><span class="o">.</span><span class="n">Event</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span> <span class="n">events</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;attribute&quot;</span><span class="p">:</span> <span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;a_string_attribute&quot;</span><span class="p">,</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;a string&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;an_integer_attribute&quot;</span><span class="p">,</span>
            <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;int&quot;</span><span class="p">,</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="mi">42</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;a_float_attribute&quot;</span><span class="p">,</span>
            <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;float&quot;</span><span class="p">,</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="mf">101.1</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="s2">&quot;timestamp&quot;</span><span class="p">:</span> <span class="mi">1232471100</span><span class="p">,</span>
    <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;MyEvent&quot;</span><span class="p">,</span>
<span class="p">}])</span>
</pre></div>
</div>
<p>The <code class="docutils literal notranslate"><span class="pre">event</span></code> mapping supports the following arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Required) The event’s name. Can be a combination of alphanumeric characters, underscores, and colons.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestamp</span></code> - (Optional) Must be a Unix epoch timestamp. You can define timestamps either in seconds or in milliseconds.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attribute</span></code> - (Required) An attribute to include in your event payload. Multiple attribute blocks can be defined for an event. See Attributes below for details.</p></li>
</ul>
<p>The <code class="docutils literal notranslate"><span class="pre">attribute</span></code> mapping supports the following arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> - (Required) The name of the attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> - (Required) The value of the attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Optional) Specify the type for the attribute value. This is useful when passing integer or float values to Insights. Allowed values are <code class="docutils literal notranslate"><span class="pre">string</span></code>, <code class="docutils literal notranslate"><span class="pre">int</span></code>, or <code class="docutils literal notranslate"><span class="pre">float</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">string</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>events</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An event to insert into Insights. Multiple event blocks can be defined. See Events below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>events</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestamp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_newrelic.insights.Event.events">
<code class="sig-name descname">events</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.insights.Event.events" title="Permalink to this definition">¶</a></dt>
<dd><p>An event to insert into Insights. Multiple event blocks can be defined. See Events below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestamp</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.insights.Event.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.insights.Event.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Event resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>events</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An event to insert into Insights. Multiple event blocks can be defined. See Events below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>events</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">timestamp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.insights.Event.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.insights.Event.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.insights.Event.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.insights.Event.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
