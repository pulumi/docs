---
title: Module firestore
title_tag: Module firestore | Package pulumi_gcp | Python SDK
linktitle: firestore
notitle: true
---

<div class="section" id="firestore">
<h1>firestore<a class="headerlink" href="#firestore" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.firestore"></span><dl class="py class">
<dt id="pulumi_gcp.firestore.Index">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.firestore.</code><code class="sig-name descname">Index</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">collection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.firestore.Index" title="Permalink to this definition">¶</a></dt>
<dd><dl class="simple">
<dt>Cloud Firestore indexes enable simple and complex queries against documents in a database.</dt><dd><p>This resource manages composite indexes and not single</p>
</dd>
</dl>
<p>field indexes.</p>
<p>To get more information about Index, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.collectionGroups.indexes">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/firestore/docs/query-data/indexing">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>collection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The collection being indexed.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Firestore database id. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;(default)&quot;</span></code>.</p></li>
<li><p><strong>fields</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The fields supported by this index. The last field entry is always for
the field path <code class="docutils literal notranslate"><span class="pre">__name__</span></code>. If, on creation, <code class="docutils literal notranslate"><span class="pre">__name__</span></code> was not
specified as the last field, it will be added automatically with the
same direction as that of the last field defined. If the final field
in a composite index is not directional, the <code class="docutils literal notranslate"><span class="pre">__name__</span></code> will be
ordered <code class="docutils literal notranslate"><span class="pre">&quot;ASCENDING&quot;</span></code> (unless explicitly specified otherwise).  Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>query_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scope at which a query is run. One of <code class="docutils literal notranslate"><span class="pre">&quot;COLLECTION&quot;</span></code> or
<code class="docutils literal notranslate"><span class="pre">&quot;COLLECTION_GROUP&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;COLLECTION&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>fields</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arrayConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates that this field supports operations on arrayValues. Only one of <code class="docutils literal notranslate"><span class="pre">order</span></code> and <code class="docutils literal notranslate"><span class="pre">arrayConfig</span></code> can
be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates that this field supports ordering by the specified order or comparing using =, &lt;, &lt;=, &gt;, &gt;=.
Only one of <code class="docutils literal notranslate"><span class="pre">order</span></code> and <code class="docutils literal notranslate"><span class="pre">arrayConfig</span></code> can be specified.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.firestore.Index.collection">
<code class="sig-name descname">collection</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.firestore.Index.collection" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection being indexed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.firestore.Index.database">
<code class="sig-name descname">database</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.firestore.Index.database" title="Permalink to this definition">¶</a></dt>
<dd><p>The Firestore database id. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;(default)&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.firestore.Index.fields">
<code class="sig-name descname">fields</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.firestore.Index.fields" title="Permalink to this definition">¶</a></dt>
<dd><p>The fields supported by this index. The last field entry is always for
the field path <code class="docutils literal notranslate"><span class="pre">__name__</span></code>. If, on creation, <code class="docutils literal notranslate"><span class="pre">__name__</span></code> was not
specified as the last field, it will be added automatically with the
same direction as that of the last field defined. If the final field
in a composite index is not directional, the <code class="docutils literal notranslate"><span class="pre">__name__</span></code> will be
ordered <code class="docutils literal notranslate"><span class="pre">&quot;ASCENDING&quot;</span></code> (unless explicitly specified otherwise).  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arrayConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Indicates that this field supports operations on arrayValues. Only one of <code class="docutils literal notranslate"><span class="pre">order</span></code> and <code class="docutils literal notranslate"><span class="pre">arrayConfig</span></code> can
be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Indicates that this field supports ordering by the specified order or comparing using =, &lt;, &lt;=, &gt;, &gt;=.
Only one of <code class="docutils literal notranslate"><span class="pre">order</span></code> and <code class="docutils literal notranslate"><span class="pre">arrayConfig</span></code> can be specified.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.firestore.Index.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.firestore.Index.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A server defined name for this index. Format:
‘projects/{{project}}/databases/{{database}}/collectionGroups/{{collection}}/indexes/{{server_generated_id}}’</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.firestore.Index.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.firestore.Index.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.firestore.Index.query_scope">
<code class="sig-name descname">query_scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.firestore.Index.query_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The scope at which a query is run. One of <code class="docutils literal notranslate"><span class="pre">&quot;COLLECTION&quot;</span></code> or
<code class="docutils literal notranslate"><span class="pre">&quot;COLLECTION_GROUP&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;COLLECTION&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.firestore.Index.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">collection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fields</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_scope</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.firestore.Index.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Index resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>collection</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The collection being indexed.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Firestore database id. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;(default)&quot;</span></code>.</p></li>
<li><p><strong>fields</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The fields supported by this index. The last field entry is always for
the field path <code class="docutils literal notranslate"><span class="pre">__name__</span></code>. If, on creation, <code class="docutils literal notranslate"><span class="pre">__name__</span></code> was not
specified as the last field, it will be added automatically with the
same direction as that of the last field defined. If the final field
in a composite index is not directional, the <code class="docutils literal notranslate"><span class="pre">__name__</span></code> will be
ordered <code class="docutils literal notranslate"><span class="pre">&quot;ASCENDING&quot;</span></code> (unless explicitly specified otherwise).  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A server defined name for this index. Format:
‘projects/{{project}}/databases/{{database}}/collectionGroups/{{collection}}/indexes/{{server_generated_id}}’</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>query_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scope at which a query is run. One of <code class="docutils literal notranslate"><span class="pre">&quot;COLLECTION&quot;</span></code> or
<code class="docutils literal notranslate"><span class="pre">&quot;COLLECTION_GROUP&quot;</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;COLLECTION&quot;</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>fields</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arrayConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates that this field supports operations on arrayValues. Only one of <code class="docutils literal notranslate"><span class="pre">order</span></code> and <code class="docutils literal notranslate"><span class="pre">arrayConfig</span></code> can
be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates that this field supports ordering by the specified order or comparing using =, &lt;, &lt;=, &gt;, &gt;=.
Only one of <code class="docutils literal notranslate"><span class="pre">order</span></code> and <code class="docutils literal notranslate"><span class="pre">arrayConfig</span></code> can be specified.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.firestore.Index.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.firestore.Index.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.firestore.Index.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.firestore.Index.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
