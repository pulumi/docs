---
title: Package pulumi_rabbitmq
title_tag: Package pulumi_rabbitmq | Python SDK
linktitle: pulumi_rabbitmq
notitle: true
---

<div class="section" id="pulumi-rabbitmq">
<h1>Pulumi RabbitMQ<a class="headerlink" href="#pulumi-rabbitmq" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-rabbitmq">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-rabbitmq/issues">pulumi/pulumi-rabbitmq repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-rabbitmq/issues">terraform-providers/terraform-provider-rabbitmq repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_rabbitmq"></span><dl class="class">
<dt id="pulumi_rabbitmq.Binding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">Binding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arguments=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">destination_type=None</em>, <em class="sig-param">routing_key=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">vhost=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Binding" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.Binding</span></code> resource creates and manages a binding relationship
between a queue an exchange.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/binding.html.markdown">https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/binding.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arguments</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Additional key/value arguments for the binding.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination queue or exchange.</p></li>
<li><p><strong>destination_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of destination (queue or exchange).</p></li>
<li><p><strong>routing_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A routing key for the binding.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source exchange.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_rabbitmq.Binding.arguments">
<code class="sig-name descname">arguments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Binding.arguments" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional key/value arguments for the binding.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.Binding.destination">
<code class="sig-name descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Binding.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination queue or exchange.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.Binding.destination_type">
<code class="sig-name descname">destination_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Binding.destination_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of destination (queue or exchange).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.Binding.properties_key">
<code class="sig-name descname">properties_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Binding.properties_key" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique key to refer to the binding.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.Binding.routing_key">
<code class="sig-name descname">routing_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Binding.routing_key" title="Permalink to this definition">¶</a></dt>
<dd><p>A routing key for the binding.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.Binding.source">
<code class="sig-name descname">source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Binding.source" title="Permalink to this definition">¶</a></dt>
<dd><p>The source exchange.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.Binding.vhost">
<code class="sig-name descname">vhost</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Binding.vhost" title="Permalink to this definition">¶</a></dt>
<dd><p>The vhost to create the resource in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.Binding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arguments=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">destination_type=None</em>, <em class="sig-param">properties_key=None</em>, <em class="sig-param">routing_key=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">vhost=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Binding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Binding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arguments</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Additional key/value arguments for the binding.</p></li>
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

<dl class="method">
<dt id="pulumi_rabbitmq.Binding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Binding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_rabbitmq.Binding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Binding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_rabbitmq.Exchange">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">Exchange</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">vhost=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Exchange" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.Exchange</span></code> resource creates and manages an exchange.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/exchange.html.markdown">https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/exchange.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the exchange.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings of the exchange. The structure is
described below.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arguments</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">durable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_rabbitmq.Exchange.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Exchange.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the exchange.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.Exchange.settings">
<code class="sig-name descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Exchange.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The settings of the exchange. The structure is
described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arguments</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">durable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.Exchange.vhost">
<code class="sig-name descname">vhost</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Exchange.vhost" title="Permalink to this definition">¶</a></dt>
<dd><p>The vhost to create the resource in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.Exchange.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">vhost=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Exchange.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Exchange resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the exchange.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings of the exchange. The structure is
described below.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arguments</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">durable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.Exchange.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Exchange.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_rabbitmq.Exchange.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Exchange.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_rabbitmq.Permissions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">Permissions</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">user=None</em>, <em class="sig-param">vhost=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.Permissions</span></code> resource creates and manages a user’s set of
permissions.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/permissions.html.markdown">https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/permissions.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings of the permissions. The structure is
described below.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to apply the permissions to.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">configure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_rabbitmq.Permissions.permissions">
<code class="sig-name descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Permissions.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>The settings of the permissions. The structure is
described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">configure</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.Permissions.user">
<code class="sig-name descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Permissions.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The user to apply the permissions to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.Permissions.vhost">
<code class="sig-name descname">vhost</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Permissions.vhost" title="Permalink to this definition">¶</a></dt>
<dd><p>The vhost to create the resource in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.Permissions.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">user=None</em>, <em class="sig-param">vhost=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Permissions.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Permissions resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings of the permissions. The structure is
described below.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to apply the permissions to.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">configure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.Permissions.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Permissions.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_rabbitmq.Permissions.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Permissions.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_rabbitmq.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">vhost=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.Policy</span></code> resource creates and manages policies for exchanges
and queues.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/policy.html.markdown">https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings of the policy. The structure is
described below.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applyTo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">definition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_rabbitmq.Policy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.Policy.policy">
<code class="sig-name descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Policy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The settings of the policy. The structure is
described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applyTo</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">definition</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pattern</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.Policy.vhost">
<code class="sig-name descname">vhost</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Policy.vhost" title="Permalink to this definition">¶</a></dt>
<dd><p>The vhost to create the resource in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">vhost=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings of the policy. The structure is
described below.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applyTo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">definition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_rabbitmq.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_rabbitmq.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cacert_file=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">insecure=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the rabbitmq package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/index.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_rabbitmq.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_rabbitmq.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_rabbitmq.Queue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">Queue</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">vhost=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Queue" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.Queue</span></code> resource creates and manages a queue.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/queue.html.markdown">https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/queue.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the queue.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings of the queue. The structure is
described below.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arguments</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">argumentsJson</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">durable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_rabbitmq.Queue.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Queue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.Queue.settings">
<code class="sig-name descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Queue.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The settings of the queue. The structure is
described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arguments</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">argumentsJson</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">durable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.Queue.vhost">
<code class="sig-name descname">vhost</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.Queue.vhost" title="Permalink to this definition">¶</a></dt>
<dd><p>The vhost to create the resource in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.Queue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">vhost=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Queue.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Queue resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the queue.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings of the queue. The structure is
described below.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arguments</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">argumentsJson</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoDelete</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">durable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.Queue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Queue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_rabbitmq.Queue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.Queue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_rabbitmq.TopicPermissions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">TopicPermissions</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">user=None</em>, <em class="sig-param">vhost=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.TopicPermissions" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.TopicPermissions</span></code> resource creates and manages a user’s set of
topic permissions.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/topic-permissions.html.markdown">https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/topic-permissions.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The settings of the permissions. The structure is
described below.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to apply the permissions to.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exchange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_rabbitmq.TopicPermissions.permissions">
<code class="sig-name descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.TopicPermissions.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>The settings of the permissions. The structure is
described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exchange</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.TopicPermissions.user">
<code class="sig-name descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.TopicPermissions.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The user to apply the permissions to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.TopicPermissions.vhost">
<code class="sig-name descname">vhost</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.TopicPermissions.vhost" title="Permalink to this definition">¶</a></dt>
<dd><p>The vhost to create the resource in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.TopicPermissions.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">user=None</em>, <em class="sig-param">vhost=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.TopicPermissions.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TopicPermissions resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The settings of the permissions. The structure is
described below.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to apply the permissions to.</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vhost to create the resource in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>permissions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exchange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">read</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.TopicPermissions.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.TopicPermissions.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_rabbitmq.TopicPermissions.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.TopicPermissions.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_rabbitmq.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.User" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.User</span></code> resource creates and manages a user.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including username and password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/user.html.markdown">https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/user.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the user. The value of this argument
is plain-text so make sure to secure where this is defined.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Which permission model to apply to the user. Valid
options are: management, policymaker, monitoring, and administrator.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_rabbitmq.User.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.User.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.User.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of the user. The value of this argument
is plain-text so make sure to secure where this is defined.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_rabbitmq.User.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.User.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Which permission model to apply to the user. Valid
options are: management, policymaker, monitoring, and administrator.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the user. The value of this argument
is plain-text so make sure to secure where this is defined.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Which permission model to apply to the user. Valid
options are: management, policymaker, monitoring, and administrator.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_rabbitmq.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_rabbitmq.VHost">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_rabbitmq.</code><code class="sig-name descname">VHost</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.VHost" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.VHost</span></code> resource creates and manages a vhost.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/vhost.html.markdown">https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/vhost.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vhost.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_rabbitmq.VHost.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_rabbitmq.VHost.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the vhost.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.VHost.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.VHost.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VHost resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vhost.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_rabbitmq.VHost.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.VHost.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_rabbitmq.VHost.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_rabbitmq.VHost.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
