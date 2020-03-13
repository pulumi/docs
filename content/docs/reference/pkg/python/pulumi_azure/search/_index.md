---
title: Module search
title_tag: Module search | Package pulumi_azure | Python SDK
linktitle: search
notitle: true
---

<div class="section" id="search">
<h1>search<a class="headerlink" href="#search" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.search"></span><dl class="class">
<dt id="pulumi_azure.search.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.search.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partition_count=None</em>, <em class="sig-param">replica_count=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.search.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Search Service.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/search_service.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/search_service.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region where the Search Service should exist. Changing this forces a new Search Service to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name which should be used for this Search Service. Changing this forces a new Search Service to be created.</p></li>
<li><p><strong>partition_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of partitions which should be created.</p></li>
<li><p><strong>replica_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of replica’s which should be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Search Service should exist. Changing this forces a new Search Service to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU which should be used for this Search Service. Possible values are <code class="docutils literal notranslate"><span class="pre">basic</span></code>, <code class="docutils literal notranslate"><span class="pre">free</span></code>, <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">standard2</span></code> and <code class="docutils literal notranslate"><span class="pre">standard3</span></code> Changing this forces a new Search Service to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags which should be assigned to the Search Service.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.search.Service.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.search.Service.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region where the Search Service should exist. Changing this forces a new Search Service to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.search.Service.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.search.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name which should be used for this Search Service. Changing this forces a new Search Service to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.search.Service.partition_count">
<code class="sig-name descname">partition_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.search.Service.partition_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of partitions which should be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.search.Service.primary_key">
<code class="sig-name descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.search.Service.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key used for Search Service Administration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.search.Service.query_keys">
<code class="sig-name descname">query_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.search.Service.query_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">query_keys</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of this Query Key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name which should be used for this Search Service. Changing this forces a new Search Service to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.search.Service.replica_count">
<code class="sig-name descname">replica_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.search.Service.replica_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of replica’s which should be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.search.Service.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.search.Service.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Search Service should exist. Changing this forces a new Search Service to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.search.Service.secondary_key">
<code class="sig-name descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.search.Service.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key used for Search Service Administration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.search.Service.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.search.Service.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU which should be used for this Search Service. Possible values are <code class="docutils literal notranslate"><span class="pre">basic</span></code>, <code class="docutils literal notranslate"><span class="pre">free</span></code>, <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">standard2</span></code> and <code class="docutils literal notranslate"><span class="pre">standard3</span></code> Changing this forces a new Search Service to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.search.Service.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.search.Service.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags which should be assigned to the Search Service.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.search.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partition_count=None</em>, <em class="sig-param">primary_key=None</em>, <em class="sig-param">query_keys=None</em>, <em class="sig-param">replica_count=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_key=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.search.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region where the Search Service should exist. Changing this forces a new Search Service to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name which should be used for this Search Service. Changing this forces a new Search Service to be created.</p></li>
<li><p><strong>partition_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of partitions which should be created.</p></li>
<li><p><strong>primary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Key used for Search Service Administration.</p></li>
<li><p><strong>query_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">query_keys</span></code> block as defined below.</p></li>
<li><p><strong>replica_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of replica’s which should be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Search Service should exist. Changing this forces a new Search Service to be created.</p></li>
<li><p><strong>secondary_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Key used for Search Service Administration.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU which should be used for this Search Service. Possible values are <code class="docutils literal notranslate"><span class="pre">basic</span></code>, <code class="docutils literal notranslate"><span class="pre">free</span></code>, <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">standard2</span></code> and <code class="docutils literal notranslate"><span class="pre">standard3</span></code> Changing this forces a new Search Service to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags which should be assigned to the Search Service.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>query_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of this Query Key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this Search Service. Changing this forces a new Search Service to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.search.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.search.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.search.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.search.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
