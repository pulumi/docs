<div class="section" id="module-pulumi_azure.mssql">
<span id="mssql"></span><h1>mssql<a class="headerlink" href="#module-pulumi_azure.mssql" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.mssql.ElasticPool">
<em class="property">class </em><code class="descclassname">pulumi_azure.mssql.</code><code class="descname">ElasticPool</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>max_size_bytes=None</em>, <em>max_size_gb=None</em>, <em>name=None</em>, <em>per_database_settings=None</em>, <em>resource_group_name=None</em>, <em>server_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>zone_redundant=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to manage an Azure SQL Elastic Pool via the <code class="docutils literal notranslate"><span class="pre">2017-10-01-preview</span></code> API which allows for <code class="docutils literal notranslate"><span class="pre">vCore</span></code> and <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based configurations.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>max_size_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max data size of the elastic pool in bytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_gb</span></code>.</li>
<li><strong>max_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max data size of the elastic pool in gigabytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_bytes</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the SKU Name for this Elasticpool. The name of the SKU, will be either <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> pattern (e.g. GP_Gen4, BC_Gen5) or the <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based <code class="docutils literal notranslate"><span class="pre">BasicPool</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardPool</span></code>, or <code class="docutils literal notranslate"><span class="pre">PremiumPool</span></code> pattern.</li>
<li><strong>per_database_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">per_database_settings</span></code> block as defined below.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.</li>
<li><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>zone_redundant</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not this elastic pool is zone redundant. <code class="docutils literal notranslate"><span class="pre">tier</span></code> needs to be <code class="docutils literal notranslate"><span class="pre">Premium</span></code> for <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based  or <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code> for <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">sku</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.max_size_bytes">
<code class="descname">max_size_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.max_size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The max data size of the elastic pool in bytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_gb</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.max_size_gb">
<code class="descname">max_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.max_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The max data size of the elastic pool in gigabytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_bytes</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the SKU Name for this Elasticpool. The name of the SKU, will be either <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> pattern (e.g. GP_Gen4, BC_Gen5) or the <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based <code class="docutils literal notranslate"><span class="pre">BasicPool</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardPool</span></code>, or <code class="docutils literal notranslate"><span class="pre">PremiumPool</span></code> pattern.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.per_database_settings">
<code class="descname">per_database_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.per_database_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">per_database_settings</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.server_name">
<code class="descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.zone_redundant">
<code class="descname">zone_redundant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.zone_redundant" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this elastic pool is zone redundant. <code class="docutils literal notranslate"><span class="pre">tier</span></code> needs to be <code class="docutils literal notranslate"><span class="pre">Premium</span></code> for <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based  or <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code> for <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">sku</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mssql.ElasticPool.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mssql.ElasticPool.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

</div>
