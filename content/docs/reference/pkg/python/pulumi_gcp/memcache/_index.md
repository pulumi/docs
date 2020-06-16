---
title: Module memcache
title_tag: Module memcache | Package pulumi_gcp | Python SDK
linktitle: memcache
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "gcp" >}}

<div class="section" id="memcache">
<h1>memcache<a class="headerlink" href="#memcache" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.memcache"></span><dl class="py class">
<dt id="pulumi_gcp.memcache.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.memcache.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memcache_parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.memcache.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Instance resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] authorized_network: The full name of the GCE network to connect the instance to.  If not provided,</p>
<blockquote>
<div><p>‘default’ will be used.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-visible name for the instance.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Resource labels to represent user-provided metadata.</p></li>
<li><p><strong>memcache_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User-specified parameters for this memcache instance.  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the instance.</p></li>
<li><p><strong>node_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for memcache nodes.  Structure is documented below.</p></li>
<li><p><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of nodes in the memcache instance.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Memcache region of the instance.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Zones where memcache nodes should be provisioned.  If not
provided, all zones will be used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>memcache_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
This is a unique ID associated with this set of parameters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">params</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - User-defined set of parameters to use in the memcache process.</p></li>
</ul>
<p>The <strong>node_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpuCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of CPUs per node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memorySizeMb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Memory size in Mebibytes for each memcache node.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.memcache.Instance.authorized_network">
<code class="sig-name descname">authorized_network</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.memcache.Instance.authorized_network" title="Permalink to this definition">¶</a></dt>
<dd><p>The full name of the GCE network to connect the instance to.  If not provided,
‘default’ will be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.memcache.Instance.create_time">
<code class="sig-name descname">create_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.memcache.Instance.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Creation timestamp in RFC3339 text format.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.memcache.Instance.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.memcache.Instance.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-visible name for the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.memcache.Instance.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.memcache.Instance.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource labels to represent user-provided metadata.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.memcache.Instance.memcache_parameters">
<code class="sig-name descname">memcache_parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.memcache.Instance.memcache_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>User-specified parameters for this memcache instance.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
This is a unique ID associated with this set of parameters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">params</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - User-defined set of parameters to use in the memcache process.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.memcache.Instance.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.memcache.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.memcache.Instance.node_config">
<code class="sig-name descname">node_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.memcache.Instance.node_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for memcache nodes.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpuCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of CPUs per node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memorySizeMb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Memory size in Mebibytes for each memcache node.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.memcache.Instance.node_count">
<code class="sig-name descname">node_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.memcache.Instance.node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of nodes in the memcache instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.memcache.Instance.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.memcache.Instance.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.memcache.Instance.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.memcache.Instance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Memcache region of the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.memcache.Instance.zones">
<code class="sig-name descname">zones</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.memcache.Instance.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Zones where memcache nodes should be provisioned.  If not
provided, all zones will be used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.memcache.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">memcache_parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.memcache.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorized_network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full name of the GCE network to connect the instance to.  If not provided,
‘default’ will be used.</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creation timestamp in RFC3339 text format.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-visible name for the instance.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Resource labels to represent user-provided metadata.</p></li>
<li><p><strong>memcache_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User-specified parameters for this memcache instance.  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the instance.</p></li>
<li><p><strong>node_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for memcache nodes.  Structure is documented below.</p></li>
<li><p><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of nodes in the memcache instance.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Memcache region of the instance.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Zones where memcache nodes should be provisioned.  If not
provided, all zones will be used.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>memcache_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
This is a unique ID associated with this set of parameters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">params</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - User-defined set of parameters to use in the memcache process.</p></li>
</ul>
<p>The <strong>node_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cpuCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of CPUs per node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">memorySizeMb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Memory size in Mebibytes for each memcache node.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.memcache.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.memcache.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.memcache.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.memcache.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
