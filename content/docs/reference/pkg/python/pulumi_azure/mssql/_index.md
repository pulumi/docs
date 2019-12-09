---
title: Module mssql
title_tag: Module mssql | Package pulumi_azure | Python SDK
linktitle: mssql
notitle: true
---

<div class="section" id="mssql">
<h1>mssql<a class="headerlink" href="#mssql" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.mssql"></span><dl class="class">
<dt id="pulumi_azure.mssql.AwaitableGetElasticPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">AwaitableGetElasticPoolResult</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">max_size_bytes=None</em>, <em class="sig-param">max_size_gb=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">per_db_max_capacity=None</em>, <em class="sig-param">per_db_min_capacity=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_redundant=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.AwaitableGetElasticPoolResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.mssql.ElasticPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">ElasticPool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">max_size_bytes=None</em>, <em class="sig-param">max_size_gb=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">per_database_settings=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_redundant=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to manage an Azure SQL Elastic Pool via the <code class="docutils literal notranslate"><span class="pre">2017-10-01-preview</span></code> API which allows for <code class="docutils literal notranslate"><span class="pre">vCore</span></code> and <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based configurations.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_size_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max data size of the elastic pool in bytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_gb</span></code>.</p></li>
<li><p><strong>max_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max data size of the elastic pool in gigabytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_bytes</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the SKU Name for this Elasticpool. The name of the SKU, will be either <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> pattern (e.g. GP_Gen4, BC_Gen5) or the <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based <code class="docutils literal notranslate"><span class="pre">BasicPool</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardPool</span></code>, or <code class="docutils literal notranslate"><span class="pre">PremiumPool</span></code> pattern.</p></li>
<li><p><strong>per_database_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">per_database_settings</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_redundant</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not this elastic pool is zone redundant. <code class="docutils literal notranslate"><span class="pre">tier</span></code> needs to be <code class="docutils literal notranslate"><span class="pre">Premium</span></code> for <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based  or <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code> for <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">sku</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>per_database_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum capacity any one database can consume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum capacity all databases are guaranteed.</p></li>
</ul>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The scale up/out capacity, representing server’s compute units. For more information see the documentation for your Elasticpool configuration: <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-elastic-pools">vCore-based</a> or <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-elastic-pools">DTU-based</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">family</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">family</span></code> of hardware <code class="docutils literal notranslate"><span class="pre">Gen4</span></code> or <code class="docutils literal notranslate"><span class="pre">Gen5</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the SKU Name for this Elasticpool. The name of the SKU, will be either <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> pattern (e.g. GP_Gen4, BC_Gen5) or the <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based <code class="docutils literal notranslate"><span class="pre">BasicPool</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardPool</span></code>, or <code class="docutils literal notranslate"><span class="pre">PremiumPool</span></code> pattern.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tier of the particular SKU. Possible values are <code class="docutils literal notranslate"><span class="pre">GeneralPurpose</span></code>, <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. For more information see the documentation for your Elasticpool configuration: <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-elastic-pools">vCore-based</a> or <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-elastic-pools">DTU-based</a>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_elasticpool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_elasticpool.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.max_size_bytes">
<code class="sig-name descname">max_size_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.max_size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The max data size of the elastic pool in bytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_gb</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.max_size_gb">
<code class="sig-name descname">max_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.max_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The max data size of the elastic pool in gigabytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_bytes</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the SKU Name for this Elasticpool. The name of the SKU, will be either <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> pattern (e.g. GP_Gen4, BC_Gen5) or the <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based <code class="docutils literal notranslate"><span class="pre">BasicPool</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardPool</span></code>, or <code class="docutils literal notranslate"><span class="pre">PremiumPool</span></code> pattern.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.per_database_settings">
<code class="sig-name descname">per_database_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.per_database_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">per_database_settings</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum capacity any one database can consume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum capacity all databases are guaranteed.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The scale up/out capacity, representing server’s compute units. For more information see the documentation for your Elasticpool configuration: <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-elastic-pools">vCore-based</a> or <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-elastic-pools">DTU-based</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">family</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The <code class="docutils literal notranslate"><span class="pre">family</span></code> of hardware <code class="docutils literal notranslate"><span class="pre">Gen4</span></code> or <code class="docutils literal notranslate"><span class="pre">Gen5</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the SKU Name for this Elasticpool. The name of the SKU, will be either <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> pattern (e.g. GP_Gen4, BC_Gen5) or the <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based <code class="docutils literal notranslate"><span class="pre">BasicPool</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardPool</span></code>, or <code class="docutils literal notranslate"><span class="pre">PremiumPool</span></code> pattern.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tier of the particular SKU. Possible values are <code class="docutils literal notranslate"><span class="pre">GeneralPurpose</span></code>, <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. For more information see the documentation for your Elasticpool configuration: <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-elastic-pools">vCore-based</a> or <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-elastic-pools">DTU-based</a>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ElasticPool.zone_redundant">
<code class="sig-name descname">zone_redundant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.zone_redundant" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this elastic pool is zone redundant. <code class="docutils literal notranslate"><span class="pre">tier</span></code> needs to be <code class="docutils literal notranslate"><span class="pre">Premium</span></code> for <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based  or <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code> for <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">sku</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mssql.ElasticPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">elastic_pool_properties=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">max_size_bytes=None</em>, <em class="sig-param">max_size_gb=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">per_database_settings=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_redundant=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ElasticPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_size_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max data size of the elastic pool in bytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_gb</span></code>.</p></li>
<li><p><strong>max_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max data size of the elastic pool in gigabytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_bytes</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the SKU Name for this Elasticpool. The name of the SKU, will be either <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> pattern (e.g. GP_Gen4, BC_Gen5) or the <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based <code class="docutils literal notranslate"><span class="pre">BasicPool</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardPool</span></code>, or <code class="docutils literal notranslate"><span class="pre">PremiumPool</span></code> pattern.</p></li>
<li><p><strong>per_database_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">per_database_settings</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_redundant</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not this elastic pool is zone redundant. <code class="docutils literal notranslate"><span class="pre">tier</span></code> needs to be <code class="docutils literal notranslate"><span class="pre">Premium</span></code> for <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based  or <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code> for <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">sku</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>elastic_pool_properties</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">creationDate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">license_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_size_bytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The max data size of the elastic pool in bytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_gb</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone_redundant</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether or not this elastic pool is zone redundant. <code class="docutils literal notranslate"><span class="pre">tier</span></code> needs to be <code class="docutils literal notranslate"><span class="pre">Premium</span></code> for <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based  or <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code> for <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">sku</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>per_database_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum capacity any one database can consume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum capacity all databases are guaranteed.</p></li>
</ul>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The scale up/out capacity, representing server’s compute units. For more information see the documentation for your Elasticpool configuration: <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-elastic-pools">vCore-based</a> or <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-elastic-pools">DTU-based</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">family</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">family</span></code> of hardware <code class="docutils literal notranslate"><span class="pre">Gen4</span></code> or <code class="docutils literal notranslate"><span class="pre">Gen5</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the SKU Name for this Elasticpool. The name of the SKU, will be either <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> pattern (e.g. GP_Gen4, BC_Gen5) or the <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based <code class="docutils literal notranslate"><span class="pre">BasicPool</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardPool</span></code>, or <code class="docutils literal notranslate"><span class="pre">PremiumPool</span></code> pattern.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tier of the particular SKU. Possible values are <code class="docutils literal notranslate"><span class="pre">GeneralPurpose</span></code>, <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. For more information see the documentation for your Elasticpool configuration: <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-elastic-pools">vCore-based</a> or <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-elastic-pools">DTU-based</a>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_elasticpool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_elasticpool.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mssql.ElasticPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mssql.ElasticPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mssql.GetElasticPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">GetElasticPoolResult</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">max_size_bytes=None</em>, <em class="sig-param">max_size_gb=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">per_db_max_capacity=None</em>, <em class="sig-param">per_db_min_capacity=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_redundant=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getElasticPool.</p>
<dl class="attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.max_size_bytes">
<code class="sig-name descname">max_size_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.max_size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The max data size of the elastic pool in bytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.max_size_gb">
<code class="sig-name descname">max_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.max_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The max data size of the elastic pool in gigabytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.per_db_max_capacity">
<code class="sig-name descname">per_db_max_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.per_db_max_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum capacity any one database can consume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.per_db_min_capacity">
<code class="sig-name descname">per_db_min_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.per_db_min_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum capacity all databases are guaranteed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.zone_redundant">
<code class="sig-name descname">zone_redundant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.zone_redundant" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this elastic pool is zone redundant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_azure.mssql.get_elastic_pool">
<code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">get_elastic_pool</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.get_elastic_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing SQL elastic pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the elastic pool.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group which contains the elastic pool.</p></li>
<li><p><strong>server_name</strong> (<em>str</em>) – The name of the SQL Server which contains the elastic pool.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/mssql_elasticpool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/mssql_elasticpool.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
