---
title: Package pulumi_rabbitmq
title_tag: Package pulumi_rabbitmq | Python SDK
linktitle: pulumi_rabbitmq
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "rabbitmq" >}}

<div class="section" id="pulumi-rabbitmq">
<h1>Pulumi RabbitMQ<a class="headerlink" href="#pulumi-rabbitmq" title="Permalink to this headline"></a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-rabbitmq">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-rabbitmq/issues">pulumi/pulumi-rabbitmq repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-rabbitmq/issues">terraform-providers/terraform-provider-rabbitmq repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_rabbitmq"></span><dl class="py class">
<dt id="pulumi_rabbitmq.Binding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">Binding</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arguments</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arguments_json</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">routing_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Binding" title="Permalink to this definition"></a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">Binding</span></code> resource creates and manages a binding relationship
between a queue an exchange.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_rabbitmq</span> <span class="k">as</span> <span class="nn">rabbitmq</span>

<span class="n">test_v_host</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">VHost</span><span class="p">(</span><span class="s2">&quot;testVHost&quot;</span><span class="p">)</span>
<span class="n">guest</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Permissions</span><span class="p">(</span><span class="s2">&quot;guest&quot;</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">PermissionsPermissionsArgs</span><span class="p">(</span>
        <span class="n">configure</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
        <span class="n">read</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
        <span class="n">write</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">user</span><span class="o">=</span><span class="s2">&quot;guest&quot;</span><span class="p">,</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">test_v_host</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">test_exchange</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Exchange</span><span class="p">(</span><span class="s2">&quot;testExchange&quot;</span><span class="p">,</span>
    <span class="n">settings</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">ExchangeSettingsArgs</span><span class="p">(</span>
        <span class="n">auto_delete</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">durable</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;fanout&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">guest</span><span class="o">.</span><span class="n">vhost</span><span class="p">)</span>
<span class="n">test_queue</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Queue</span><span class="p">(</span><span class="s2">&quot;testQueue&quot;</span><span class="p">,</span>
    <span class="n">settings</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">QueueSettingsArgs</span><span class="p">(</span>
        <span class="n">auto_delete</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">durable</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">guest</span><span class="o">.</span><span class="n">vhost</span><span class="p">)</span>
<span class="n">test_binding</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Binding</span><span class="p">(</span><span class="s2">&quot;testBinding&quot;</span><span class="p">,</span>
    <span class="n">destination</span><span class="o">=</span><span class="n">test_queue</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">destination_type</span><span class="o">=</span><span class="s2">&quot;queue&quot;</span><span class="p">,</span>
    <span class="n">routing_key</span><span class="o">=</span><span class="s2">&quot;#&quot;</span><span class="p">,</span>
    <span class="n">source</span><span class="o">=</span><span class="n">test_exchange</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">test_v_host</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<p>Bindings can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code> which is composed of</p>
<blockquote>
<div><p><code class="docutils literal notranslate"><span class="pre">vhost/source/destination/destination_type/properties_key</span></code>. E.g.</p>
</div></blockquote>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import rabbitmq:index/binding:Binding <span class="nb">test</span> test/test/test/queue/%23
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>arguments</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Additional key/value arguments for the binding.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination queue or exchange.</p></li>
<li><p><strong>destination_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of destination (queue or exchange).</p></li>
<li><p><strong>routing_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A routing key for the binding.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source exchange.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_rabbitmq.Binding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arguments</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arguments_json</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">properties_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">routing_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_rabbitmq.Binding" title="pulumi_rabbitmq.Binding">Binding</a><a class="headerlink" href="#pulumi_rabbitmq.Binding.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Binding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>arguments</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Additional key/value arguments for the binding.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination queue or exchange.</p></li>
<li><p><strong>destination_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of destination (queue or exchange).</p></li>
<li><p><strong>properties_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique key to refer to the binding.</p></li>
<li><p><strong>routing_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A routing key for the binding.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source exchange.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Binding.arguments">
<em class="property">property </em><code class="sig-name descname">arguments</code><a class="headerlink" href="#pulumi_rabbitmq.Binding.arguments" title="Permalink to this definition"></a></dt>
<dd><p>Additional key/value arguments for the binding.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Binding.destination">
<em class="property">property </em><code class="sig-name descname">destination</code><a class="headerlink" href="#pulumi_rabbitmq.Binding.destination" title="Permalink to this definition"></a></dt>
<dd><p>The destination queue or exchange.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Binding.destination_type">
<em class="property">property </em><code class="sig-name descname">destination_type</code><a class="headerlink" href="#pulumi_rabbitmq.Binding.destination_type" title="Permalink to this definition"></a></dt>
<dd><p>The type of destination (queue or exchange).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Binding.properties_key">
<em class="property">property </em><code class="sig-name descname">properties_key</code><a class="headerlink" href="#pulumi_rabbitmq.Binding.properties_key" title="Permalink to this definition"></a></dt>
<dd><p>A unique key to refer to the binding.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Binding.routing_key">
<em class="property">property </em><code class="sig-name descname">routing_key</code><a class="headerlink" href="#pulumi_rabbitmq.Binding.routing_key" title="Permalink to this definition"></a></dt>
<dd><p>A routing key for the binding.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Binding.source">
<em class="property">property </em><code class="sig-name descname">source</code><a class="headerlink" href="#pulumi_rabbitmq.Binding.source" title="Permalink to this definition"></a></dt>
<dd><p>The source exchange.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Binding.vhost">
<em class="property">property </em><code class="sig-name descname">vhost</code><a class="headerlink" href="#pulumi_rabbitmq.Binding.vhost" title="Permalink to this definition"></a></dt>
<dd><p>The vhost to create the resource in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Binding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Binding.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.Binding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Binding.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.Exchange">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">Exchange</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ExchangeSettingsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ExchangeSettingsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Exchange" title="Permalink to this definition"></a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">Exchange</span></code> resource creates and manages an exchange.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_rabbitmq</span> <span class="k">as</span> <span class="nn">rabbitmq</span>

<span class="n">test_v_host</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">VHost</span><span class="p">(</span><span class="s2">&quot;testVHost&quot;</span><span class="p">)</span>
<span class="n">guest</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Permissions</span><span class="p">(</span><span class="s2">&quot;guest&quot;</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">PermissionsPermissionsArgs</span><span class="p">(</span>
        <span class="n">configure</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
        <span class="n">read</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
        <span class="n">write</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">user</span><span class="o">=</span><span class="s2">&quot;guest&quot;</span><span class="p">,</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">test_v_host</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">test_exchange</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Exchange</span><span class="p">(</span><span class="s2">&quot;testExchange&quot;</span><span class="p">,</span>
    <span class="n">settings</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">ExchangeSettingsArgs</span><span class="p">(</span>
        <span class="n">auto_delete</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">durable</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;fanout&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">guest</span><span class="o">.</span><span class="n">vhost</span><span class="p">)</span>
</pre></div>
</div>
<p>Exchanges can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code> which is composed of</p>
<p><code class="docutils literal notranslate"><span class="pre">name&#64;vhost</span></code>. E.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import rabbitmq:index/exchange:Exchange <span class="nb">test</span> test@vhost
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the exchange.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ExchangeSettingsArgs'</em><em>]</em><em>]</em>) – The settings of the exchange. The structure is
described below.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_rabbitmq.Exchange.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ExchangeSettingsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ExchangeSettingsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_rabbitmq.Exchange" title="pulumi_rabbitmq.Exchange">Exchange</a><a class="headerlink" href="#pulumi_rabbitmq.Exchange.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Exchange resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the exchange.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ExchangeSettingsArgs'</em><em>]</em><em>]</em>) – The settings of the exchange. The structure is
described below.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Exchange.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_rabbitmq.Exchange.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the exchange.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Exchange.settings">
<em class="property">property </em><code class="sig-name descname">settings</code><a class="headerlink" href="#pulumi_rabbitmq.Exchange.settings" title="Permalink to this definition"></a></dt>
<dd><p>The settings of the exchange. The structure is
described below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Exchange.vhost">
<em class="property">property </em><code class="sig-name descname">vhost</code><a class="headerlink" href="#pulumi_rabbitmq.Exchange.vhost" title="Permalink to this definition"></a></dt>
<dd><p>The vhost to create the resource in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Exchange.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Exchange.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.Exchange.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Exchange.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.FederationUpstream">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">FederationUpstream</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">definition</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>FederationUpstreamDefinitionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>FederationUpstreamDefinitionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.FederationUpstream" title="Permalink to this definition"></a></dt>
<dd><p>Create a FederationUpstream resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_rabbitmq.FederationUpstream.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">component</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">definition</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>FederationUpstreamDefinitionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>FederationUpstreamDefinitionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_rabbitmq.FederationUpstream" title="pulumi_rabbitmq.FederationUpstream">FederationUpstream</a><a class="headerlink" href="#pulumi_rabbitmq.FederationUpstream.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing FederationUpstream resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.FederationUpstream.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.FederationUpstream.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.FederationUpstream.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.FederationUpstream.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.Permissions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">Permissions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>PermissionsPermissionsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>PermissionsPermissionsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Permissions" title="Permalink to this definition"></a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">Permissions</span></code> resource creates and manages a user’s set of
permissions.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_rabbitmq</span> <span class="k">as</span> <span class="nn">rabbitmq</span>

<span class="n">test_v_host</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">VHost</span><span class="p">(</span><span class="s2">&quot;testVHost&quot;</span><span class="p">)</span>
<span class="n">test_user</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;testUser&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;administrator&quot;</span><span class="p">])</span>
<span class="n">test_permissions</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Permissions</span><span class="p">(</span><span class="s2">&quot;testPermissions&quot;</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">PermissionsPermissionsArgs</span><span class="p">(</span>
        <span class="n">configure</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
        <span class="n">read</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
        <span class="n">write</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">user</span><span class="o">=</span><span class="n">test_user</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">test_v_host</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<p>Permissions can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code> which is composed of</p>
<p><code class="docutils literal notranslate"><span class="pre">user&#64;vhost</span></code>. E.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import rabbitmq:index/permissions:Permissions <span class="nb">test</span> user@vhost
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'PermissionsPermissionsArgs'</em><em>]</em><em>]</em>) – The settings of the permissions. The structure is
described below.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to apply the permissions to.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_rabbitmq.Permissions.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>PermissionsPermissionsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>PermissionsPermissionsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_rabbitmq.Permissions" title="pulumi_rabbitmq.Permissions">Permissions</a><a class="headerlink" href="#pulumi_rabbitmq.Permissions.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Permissions resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'PermissionsPermissionsArgs'</em><em>]</em><em>]</em>) – The settings of the permissions. The structure is
described below.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to apply the permissions to.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Permissions.permissions">
<em class="property">property </em><code class="sig-name descname">permissions</code><a class="headerlink" href="#pulumi_rabbitmq.Permissions.permissions" title="Permalink to this definition"></a></dt>
<dd><p>The settings of the permissions. The structure is
described below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Permissions.user">
<em class="property">property </em><code class="sig-name descname">user</code><a class="headerlink" href="#pulumi_rabbitmq.Permissions.user" title="Permalink to this definition"></a></dt>
<dd><p>The user to apply the permissions to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Permissions.vhost">
<em class="property">property </em><code class="sig-name descname">vhost</code><a class="headerlink" href="#pulumi_rabbitmq.Permissions.vhost" title="Permalink to this definition"></a></dt>
<dd><p>The vhost to create the resource in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Permissions.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Permissions.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.Permissions.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Permissions.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>PolicyPolicyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>PolicyPolicyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Policy" title="Permalink to this definition"></a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">Policy</span></code> resource creates and manages policies for exchanges
and queues.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_rabbitmq</span> <span class="k">as</span> <span class="nn">rabbitmq</span>

<span class="n">test_v_host</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">VHost</span><span class="p">(</span><span class="s2">&quot;testVHost&quot;</span><span class="p">)</span>
<span class="n">guest</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Permissions</span><span class="p">(</span><span class="s2">&quot;guest&quot;</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">PermissionsPermissionsArgs</span><span class="p">(</span>
        <span class="n">configure</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
        <span class="n">read</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
        <span class="n">write</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">user</span><span class="o">=</span><span class="s2">&quot;guest&quot;</span><span class="p">,</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">test_v_host</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">test_policy</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Policy</span><span class="p">(</span><span class="s2">&quot;testPolicy&quot;</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">PolicyPolicyArgs</span><span class="p">(</span>
        <span class="n">apply_to</span><span class="o">=</span><span class="s2">&quot;all&quot;</span><span class="p">,</span>
        <span class="n">definition</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">&quot;ha-mode&quot;</span><span class="p">:</span> <span class="s2">&quot;all&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="n">pattern</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
        <span class="n">priority</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">guest</span><span class="o">.</span><span class="n">vhost</span><span class="p">)</span>
</pre></div>
</div>
<p>Policies can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code> which is composed of <code class="docutils literal notranslate"><span class="pre">name&#64;vhost</span></code>. E.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import rabbitmq:index/policy:Policy <span class="nb">test</span> name@vhost
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'PolicyPolicyArgs'</em><em>]</em><em>]</em>) – The settings of the policy. The structure is
described below.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_rabbitmq.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>PolicyPolicyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>PolicyPolicyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_rabbitmq.Policy" title="pulumi_rabbitmq.Policy">Policy</a><a class="headerlink" href="#pulumi_rabbitmq.Policy.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'PolicyPolicyArgs'</em><em>]</em><em>]</em>) – The settings of the policy. The structure is
described below.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Policy.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_rabbitmq.Policy.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the policy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Policy.policy">
<em class="property">property </em><code class="sig-name descname">policy</code><a class="headerlink" href="#pulumi_rabbitmq.Policy.policy" title="Permalink to this definition"></a></dt>
<dd><p>The settings of the policy. The structure is
described below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Policy.vhost">
<em class="property">property </em><code class="sig-name descname">vhost</code><a class="headerlink" href="#pulumi_rabbitmq.Policy.vhost" title="Permalink to this definition"></a></dt>
<dd><p>The vhost to create the resource in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Policy.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Policy.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cacert_file</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clientcert_file</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clientkey_file</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insecure</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Provider" title="Permalink to this definition"></a></dt>
<dd><p>The provider type for the rabbitmq package. By default, resources use package-wide configuration
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
<dt id="pulumi_rabbitmq.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Provider.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Provider.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.Queue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">Queue</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>QueueSettingsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>QueueSettingsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Queue" title="Permalink to this definition"></a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">Queue</span></code> resource creates and manages a queue.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_rabbitmq</span> <span class="k">as</span> <span class="nn">rabbitmq</span>

<span class="n">test_v_host</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">VHost</span><span class="p">(</span><span class="s2">&quot;testVHost&quot;</span><span class="p">)</span>
<span class="n">guest</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Permissions</span><span class="p">(</span><span class="s2">&quot;guest&quot;</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">PermissionsPermissionsArgs</span><span class="p">(</span>
        <span class="n">configure</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
        <span class="n">read</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
        <span class="n">write</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">user</span><span class="o">=</span><span class="s2">&quot;guest&quot;</span><span class="p">,</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">test_v_host</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">test_queue</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Queue</span><span class="p">(</span><span class="s2">&quot;testQueue&quot;</span><span class="p">,</span>
    <span class="n">settings</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">QueueSettingsArgs</span><span class="p">(</span>
        <span class="n">auto_delete</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">durable</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">guest</span><span class="o">.</span><span class="n">vhost</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_rabbitmq</span> <span class="k">as</span> <span class="nn">rabbitmq</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">arguments</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;arguments&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">arguments</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">arguments</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">  &quot;x-message-ttl&quot;: 5000</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span>
<span class="n">test_v_host</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">VHost</span><span class="p">(</span><span class="s2">&quot;testVHost&quot;</span><span class="p">)</span>
<span class="n">guest</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Permissions</span><span class="p">(</span><span class="s2">&quot;guest&quot;</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">PermissionsPermissionsArgs</span><span class="p">(</span>
        <span class="n">configure</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
        <span class="n">read</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
        <span class="n">write</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">user</span><span class="o">=</span><span class="s2">&quot;guest&quot;</span><span class="p">,</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">test_v_host</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">test_queue</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Queue</span><span class="p">(</span><span class="s2">&quot;testQueue&quot;</span><span class="p">,</span>
    <span class="n">settings</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">QueueSettingsArgs</span><span class="p">(</span>
        <span class="n">arguments_json</span><span class="o">=</span><span class="n">arguments</span><span class="p">,</span>
        <span class="n">auto_delete</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">durable</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">guest</span><span class="o">.</span><span class="n">vhost</span><span class="p">)</span>
</pre></div>
</div>
<p>Queues can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code> which is composed of <code class="docutils literal notranslate"><span class="pre">name&#64;vhost</span></code>. E.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import rabbitmq:index/queue:Queue <span class="nb">test</span> name@vhost
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the queue.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'QueueSettingsArgs'</em><em>]</em><em>]</em>) – The settings of the queue. The structure is
described below.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_rabbitmq.Queue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>QueueSettingsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>QueueSettingsArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_rabbitmq.Queue" title="pulumi_rabbitmq.Queue">Queue</a><a class="headerlink" href="#pulumi_rabbitmq.Queue.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Queue resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the queue.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'QueueSettingsArgs'</em><em>]</em><em>]</em>) – The settings of the queue. The structure is
described below.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Queue.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_rabbitmq.Queue.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the queue.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Queue.settings">
<em class="property">property </em><code class="sig-name descname">settings</code><a class="headerlink" href="#pulumi_rabbitmq.Queue.settings" title="Permalink to this definition"></a></dt>
<dd><p>The settings of the queue. The structure is
described below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Queue.vhost">
<em class="property">property </em><code class="sig-name descname">vhost</code><a class="headerlink" href="#pulumi_rabbitmq.Queue.vhost" title="Permalink to this definition"></a></dt>
<dd><p>The vhost to create the resource in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Queue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Queue.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.Queue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Queue.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.Shovel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">Shovel</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">info</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ShovelInfoArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ShovelInfoArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Shovel" title="Permalink to this definition"></a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">Shovel</span></code> resource creates and manages a shovel.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_rabbitmq</span> <span class="k">as</span> <span class="nn">rabbitmq</span>

<span class="n">test_v_host</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">VHost</span><span class="p">(</span><span class="s2">&quot;testVHost&quot;</span><span class="p">)</span>
<span class="n">test_exchange</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Exchange</span><span class="p">(</span><span class="s2">&quot;testExchange&quot;</span><span class="p">,</span>
    <span class="n">settings</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">ExchangeSettingsArgs</span><span class="p">(</span>
        <span class="n">auto_delete</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">durable</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;fanout&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">test_v_host</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">test_queue</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Queue</span><span class="p">(</span><span class="s2">&quot;testQueue&quot;</span><span class="p">,</span>
    <span class="n">settings</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">QueueSettingsArgs</span><span class="p">(</span>
        <span class="n">auto_delete</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">durable</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">test_v_host</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">shovel_test</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">Shovel</span><span class="p">(</span><span class="s2">&quot;shovelTest&quot;</span><span class="p">,</span>
    <span class="n">info</span><span class="o">=</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">ShovelInfoArgs</span><span class="p">(</span>
        <span class="n">destination_queue</span><span class="o">=</span><span class="n">test_queue</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
        <span class="n">destination_uri</span><span class="o">=</span><span class="s2">&quot;amqp:///test&quot;</span><span class="p">,</span>
        <span class="n">source_exchange</span><span class="o">=</span><span class="n">test_exchange</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
        <span class="n">source_exchange_key</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
        <span class="n">source_uri</span><span class="o">=</span><span class="s2">&quot;amqp:///test&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">test_v_host</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<p>Shovels can be imported using the <code class="docutils literal notranslate"><span class="pre">name</span></code> and <code class="docutils literal notranslate"><span class="pre">vhost</span></code> E.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import rabbitmq:index/shovel:Shovel <span class="nb">test</span> shovelTest@test
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>info</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ShovelInfoArgs'</em><em>]</em><em>]</em>) – The settings of the shovel. The structure is
described below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shovel name.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_rabbitmq.Shovel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">info</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ShovelInfoArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ShovelInfoArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_rabbitmq.Shovel" title="pulumi_rabbitmq.Shovel">Shovel</a><a class="headerlink" href="#pulumi_rabbitmq.Shovel.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Shovel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>info</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ShovelInfoArgs'</em><em>]</em><em>]</em>) – The settings of the shovel. The structure is
described below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shovel name.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Shovel.info">
<em class="property">property </em><code class="sig-name descname">info</code><a class="headerlink" href="#pulumi_rabbitmq.Shovel.info" title="Permalink to this definition"></a></dt>
<dd><p>The settings of the shovel. The structure is
described below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Shovel.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_rabbitmq.Shovel.name" title="Permalink to this definition"></a></dt>
<dd><p>The shovel name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Shovel.vhost">
<em class="property">property </em><code class="sig-name descname">vhost</code><a class="headerlink" href="#pulumi_rabbitmq.Shovel.vhost" title="Permalink to this definition"></a></dt>
<dd><p>The vhost to create the resource in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.Shovel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Shovel.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.Shovel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Shovel.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.TopicPermissions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">TopicPermissions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TopicPermissionsPermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TopicPermissionsPermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TopicPermissionsPermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TopicPermissionsPermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.TopicPermissions" title="Permalink to this definition"></a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">TopicPermissions</span></code> resource creates and manages a user’s set of
topic permissions.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_rabbitmq</span> <span class="k">as</span> <span class="nn">rabbitmq</span>

<span class="n">test_v_host</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">VHost</span><span class="p">(</span><span class="s2">&quot;testVHost&quot;</span><span class="p">)</span>
<span class="n">test_user</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;testUser&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;administrator&quot;</span><span class="p">])</span>
<span class="n">test_topic_permissions</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">TopicPermissions</span><span class="p">(</span><span class="s2">&quot;testTopicPermissions&quot;</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">[</span><span class="n">rabbitmq</span><span class="o">.</span><span class="n">TopicPermissionsPermissionArgs</span><span class="p">(</span>
        <span class="n">exchange</span><span class="o">=</span><span class="s2">&quot;amq.topic&quot;</span><span class="p">,</span>
        <span class="n">read</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
        <span class="n">write</span><span class="o">=</span><span class="s2">&quot;.*&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">user</span><span class="o">=</span><span class="n">test_user</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">vhost</span><span class="o">=</span><span class="n">test_v_host</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<p>Permissions can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code> which is composed of</p>
<p><code class="docutils literal notranslate"><span class="pre">user&#64;vhost</span></code>. E.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import rabbitmq:index/topicPermissions:TopicPermissions <span class="nb">test</span> user@vhost
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TopicPermissionsPermissionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The settings of the permissions. The structure is
described below.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to apply the permissions to.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_rabbitmq.TopicPermissions.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TopicPermissionsPermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TopicPermissionsPermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>TopicPermissionsPermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>TopicPermissionsPermissionArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_rabbitmq.TopicPermissions" title="pulumi_rabbitmq.TopicPermissions">TopicPermissions</a><a class="headerlink" href="#pulumi_rabbitmq.TopicPermissions.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing TopicPermissions resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TopicPermissionsPermissionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The settings of the permissions. The structure is
described below.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to apply the permissions to.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.TopicPermissions.permissions">
<em class="property">property </em><code class="sig-name descname">permissions</code><a class="headerlink" href="#pulumi_rabbitmq.TopicPermissions.permissions" title="Permalink to this definition"></a></dt>
<dd><p>The settings of the permissions. The structure is
described below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.TopicPermissions.user">
<em class="property">property </em><code class="sig-name descname">user</code><a class="headerlink" href="#pulumi_rabbitmq.TopicPermissions.user" title="Permalink to this definition"></a></dt>
<dd><p>The user to apply the permissions to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.TopicPermissions.vhost">
<em class="property">property </em><code class="sig-name descname">vhost</code><a class="headerlink" href="#pulumi_rabbitmq.TopicPermissions.vhost" title="Permalink to this definition"></a></dt>
<dd><p>The vhost to create the resource in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.TopicPermissions.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.TopicPermissions.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.TopicPermissions.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.TopicPermissions.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.User" title="Permalink to this definition"></a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">User</span></code> resource creates and manages a user.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including username and password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_rabbitmq</span> <span class="k">as</span> <span class="nn">rabbitmq</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;administrator&quot;</span><span class="p">,</span>
        <span class="s2">&quot;management&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>Users can be imported using the <code class="docutils literal notranslate"><span class="pre">name</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import rabbitmq:index/user:User <span class="nb">test</span> mctest
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the user. The value of this argument
is plain-text so make sure to secure where this is defined.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Which permission model to apply to the user. Valid
options are: management, policymaker, monitoring, and administrator.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_rabbitmq.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_rabbitmq.User" title="pulumi_rabbitmq.User">User</a><a class="headerlink" href="#pulumi_rabbitmq.User.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the user. The value of this argument
is plain-text so make sure to secure where this is defined.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Which permission model to apply to the user. Valid
options are: management, policymaker, monitoring, and administrator.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.User.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_rabbitmq.User.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.User.password">
<em class="property">property </em><code class="sig-name descname">password</code><a class="headerlink" href="#pulumi_rabbitmq.User.password" title="Permalink to this definition"></a></dt>
<dd><p>The password of the user. The value of this argument
is plain-text so make sure to secure where this is defined.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.User.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_rabbitmq.User.tags" title="Permalink to this definition"></a></dt>
<dd><p>Which permission model to apply to the user. Valid
options are: management, policymaker, monitoring, and administrator.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.User.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.User.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.VHost">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">VHost</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.VHost" title="Permalink to this definition"></a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">VHost</span></code> resource creates and manages a vhost.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_rabbitmq</span> <span class="k">as</span> <span class="nn">rabbitmq</span>

<span class="n">my_vhost</span> <span class="o">=</span> <span class="n">rabbitmq</span><span class="o">.</span><span class="n">VHost</span><span class="p">(</span><span class="s2">&quot;myVhost&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Vhosts can be imported using the <code class="docutils literal notranslate"><span class="pre">name</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import rabbitmq:index/vHost:VHost my_vhost my_vhost
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vhost.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_rabbitmq.VHost.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_rabbitmq.VHost" title="pulumi_rabbitmq.VHost">VHost</a><a class="headerlink" href="#pulumi_rabbitmq.VHost.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing VHost resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vhost.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.VHost.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_rabbitmq.VHost.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the vhost.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_rabbitmq.VHost.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.VHost.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_rabbitmq.VHost.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.VHost.translate_input_property" title="Permalink to this definition"></a></dt>
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
