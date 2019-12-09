---
title: Module kusto
title_tag: Module kusto | Package pulumi_azure | Python SDK
linktitle: kusto
notitle: true
---

<div class="section" id="kusto">
<h1>kusto<a class="headerlink" href="#kusto" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.kusto"></span><dl class="class">
<dt id="pulumi_azure.kusto.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.kusto.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.kusto.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Kusto (also known as Azure Data Explorer) Cluster</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Kusto Cluster should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Kusto Cluster to create. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Resource Group where the Kusto Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Kusto Cluster to create. Changing this forces a new resource to be created.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kusto_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kusto_cluster.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.kusto.Cluster.data_ingestion_uri">
<code class="sig-name descname">data_ingestion_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.Cluster.data_ingestion_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The Kusto Cluster URI to be used for data ingestion.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.Cluster.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.Cluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the Kusto Cluster should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.Cluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Kusto Cluster to create. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.Cluster.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.Cluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Resource Group where the Kusto Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.Cluster.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.Cluster.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Kusto Cluster to create. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.Cluster.uri">
<code class="sig-name descname">uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.Cluster.uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the Azure Kusto Cluster.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.kusto.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data_ingestion_uri=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.kusto.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_ingestion_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Kusto Cluster URI to be used for data ingestion.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Kusto Cluster should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Kusto Cluster to create. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Resource Group where the Kusto Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN of the Azure Kusto Cluster.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Kusto Cluster to create. Changing this forces a new resource to be created.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kusto_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kusto_cluster.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.kusto.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.kusto.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.kusto.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.kusto.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.kusto.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.kusto.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">hot_cache_period=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">soft_delete_period=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.kusto.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Kusto (also known as Azure Data Explorer) Database</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Kusto Cluster this database will be added to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>hot_cache_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time the data that should be kept in cache for fast queries as ISO 8601 timespan. Default is unlimited. For more information see: <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 Timespan</a></p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Kusto Database should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Kusto Database to create. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>soft_delete_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The time the data should be kept before it stops being accessible to queries as ISO 8601 timespan. Default is unlimited. For more information see: <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 Timespan</a></p>
</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kusto_database.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kusto_database.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.kusto.Database.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.Database.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Kusto Cluster this database will be added to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.Database.hot_cache_period">
<code class="sig-name descname">hot_cache_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.Database.hot_cache_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the data that should be kept in cache for fast queries as ISO 8601 timespan. Default is unlimited. For more information see: <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 Timespan</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.Database.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.Database.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the Kusto Database should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.Database.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Kusto Database to create. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.Database.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.Database.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.Database.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.Database.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the database in bytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.Database.soft_delete_period">
<code class="sig-name descname">soft_delete_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.Database.soft_delete_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the data should be kept before it stops being accessible to queries as ISO 8601 timespan. Default is unlimited. For more information see: <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 Timespan</a></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.kusto.Database.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">hot_cache_period=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">soft_delete_period=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.kusto.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Kusto Cluster this database will be added to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>hot_cache_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The time the data that should be kept in cache for fast queries as ISO 8601 timespan. Default is unlimited. For more information see: <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 Timespan</a></p>
</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Kusto Database should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Kusto Database to create. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the database in bytes.</p></li>
<li><p><strong>soft_delete_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The time the data should be kept before it stops being accessible to queries as ISO 8601 timespan. Default is unlimited. For more information see: <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 Timespan</a></p>
</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kusto_database.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kusto_database.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.kusto.Database.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.kusto.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.kusto.Database.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.kusto.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.kusto.EventhubDataConnection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.kusto.</code><code class="sig-name descname">EventhubDataConnection</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">consumer_group=None</em>, <em class="sig-param">data_format=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">eventhub_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">mapping_rule_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">table_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.kusto.EventhubDataConnection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Kusto (also known as Azure Data Explorer) EventHub Data Connection</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Kusto Cluster this data connection will be added to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>consumer_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the EventHub consumer group this data connection will use for ingestion. Changing this forces a new resource to be created.</p></li>
<li><p><strong>data_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the data format of the EventHub messages. Allowed values: <code class="docutils literal notranslate"><span class="pre">AVRO</span></code>, <code class="docutils literal notranslate"><span class="pre">CSV</span></code>, <code class="docutils literal notranslate"><span class="pre">JSON</span></code>, <code class="docutils literal notranslate"><span class="pre">MULTIJSON</span></code>, <code class="docutils literal notranslate"><span class="pre">PSV</span></code>, <code class="docutils literal notranslate"><span class="pre">RAW</span></code>, <code class="docutils literal notranslate"><span class="pre">SCSV</span></code>, <code class="docutils literal notranslate"><span class="pre">SINGLEJSON</span></code>, <code class="docutils literal notranslate"><span class="pre">SOHSV</span></code>, <code class="docutils literal notranslate"><span class="pre">TSV</span></code> and <code class="docutils literal notranslate"><span class="pre">TXT</span></code></p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Kusto Database this data connection will be added to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>eventhub_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource id of the EventHub this data connection will use for ingestion. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Kusto Database should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>mapping_rule_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the mapping rule used for the message ingestion. Mapping rule must exist before resource is created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Kusto EventHub Data Connection to create. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the target table name used for the message ingestion. Table must exist before resource is created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kusto_eventhub_data_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kusto_eventhub_data_connection.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.kusto.EventhubDataConnection.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.EventhubDataConnection.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Kusto Cluster this data connection will be added to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.EventhubDataConnection.consumer_group">
<code class="sig-name descname">consumer_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.EventhubDataConnection.consumer_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the EventHub consumer group this data connection will use for ingestion. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.EventhubDataConnection.data_format">
<code class="sig-name descname">data_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.EventhubDataConnection.data_format" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the data format of the EventHub messages. Allowed values: <code class="docutils literal notranslate"><span class="pre">AVRO</span></code>, <code class="docutils literal notranslate"><span class="pre">CSV</span></code>, <code class="docutils literal notranslate"><span class="pre">JSON</span></code>, <code class="docutils literal notranslate"><span class="pre">MULTIJSON</span></code>, <code class="docutils literal notranslate"><span class="pre">PSV</span></code>, <code class="docutils literal notranslate"><span class="pre">RAW</span></code>, <code class="docutils literal notranslate"><span class="pre">SCSV</span></code>, <code class="docutils literal notranslate"><span class="pre">SINGLEJSON</span></code>, <code class="docutils literal notranslate"><span class="pre">SOHSV</span></code>, <code class="docutils literal notranslate"><span class="pre">TSV</span></code> and <code class="docutils literal notranslate"><span class="pre">TXT</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.EventhubDataConnection.database_name">
<code class="sig-name descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.EventhubDataConnection.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Kusto Database this data connection will be added to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.EventhubDataConnection.eventhub_id">
<code class="sig-name descname">eventhub_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.EventhubDataConnection.eventhub_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource id of the EventHub this data connection will use for ingestion. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.EventhubDataConnection.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.EventhubDataConnection.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the Kusto Database should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.EventhubDataConnection.mapping_rule_name">
<code class="sig-name descname">mapping_rule_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.EventhubDataConnection.mapping_rule_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the mapping rule used for the message ingestion. Mapping rule must exist before resource is created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.EventhubDataConnection.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.EventhubDataConnection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Kusto EventHub Data Connection to create. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.EventhubDataConnection.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.EventhubDataConnection.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.kusto.EventhubDataConnection.table_name">
<code class="sig-name descname">table_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.kusto.EventhubDataConnection.table_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the target table name used for the message ingestion. Table must exist before resource is created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.kusto.EventhubDataConnection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">consumer_group=None</em>, <em class="sig-param">data_format=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">eventhub_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">mapping_rule_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">table_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.kusto.EventhubDataConnection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventhubDataConnection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Kusto Cluster this data connection will be added to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>consumer_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the EventHub consumer group this data connection will use for ingestion. Changing this forces a new resource to be created.</p></li>
<li><p><strong>data_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the data format of the EventHub messages. Allowed values: <code class="docutils literal notranslate"><span class="pre">AVRO</span></code>, <code class="docutils literal notranslate"><span class="pre">CSV</span></code>, <code class="docutils literal notranslate"><span class="pre">JSON</span></code>, <code class="docutils literal notranslate"><span class="pre">MULTIJSON</span></code>, <code class="docutils literal notranslate"><span class="pre">PSV</span></code>, <code class="docutils literal notranslate"><span class="pre">RAW</span></code>, <code class="docutils literal notranslate"><span class="pre">SCSV</span></code>, <code class="docutils literal notranslate"><span class="pre">SINGLEJSON</span></code>, <code class="docutils literal notranslate"><span class="pre">SOHSV</span></code>, <code class="docutils literal notranslate"><span class="pre">TSV</span></code> and <code class="docutils literal notranslate"><span class="pre">TXT</span></code></p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Kusto Database this data connection will be added to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>eventhub_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource id of the EventHub this data connection will use for ingestion. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Kusto Database should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>mapping_rule_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the mapping rule used for the message ingestion. Mapping rule must exist before resource is created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Kusto EventHub Data Connection to create. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Resource Group where the Kusto Database should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the target table name used for the message ingestion. Table must exist before resource is created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kusto_eventhub_data_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kusto_eventhub_data_connection.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.kusto.EventhubDataConnection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.kusto.EventhubDataConnection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.kusto.EventhubDataConnection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.kusto.EventhubDataConnection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
