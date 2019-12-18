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
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">DatabaseVulnerabilityAssessmentRuleBaseline</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">baseline_name=None</em>, <em class="sig-param">baseline_results=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">rule_id=None</em>, <em class="sig-param">server_vulnerability_assessment_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Database Vulnerability Assessment Rule Baseline.</p>
<blockquote>
<div><p><strong>NOTE</strong> Database Vulnerability Assessment is currently only available for MS SQL databases.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>baseline_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vulnerability assessment rule baseline. Valid options are <code class="docutils literal notranslate"><span class="pre">default</span></code> and <code class="docutils literal notranslate"><span class="pre">master</span></code>. <code class="docutils literal notranslate"><span class="pre">default</span></code> implies a baseline on a database level rule and <code class="docutils literal notranslate"><span class="pre">master</span></code> for server level rule. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>baseline_results</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">baseline_result</span></code> block as documented below. Multiple blocks can be defined.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MS SQL Database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vulnerability assessment rule ID. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_vulnerability_assessment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Vulnerability Assessment ID of the MS SQL Server. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>baseline_results</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">results</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_database_vulnerability_assessment_rule_baseline.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_database_vulnerability_assessment_rule_baseline.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.baseline_name">
<code class="sig-name descname">baseline_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.baseline_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the vulnerability assessment rule baseline. Valid options are <code class="docutils literal notranslate"><span class="pre">default</span></code> and <code class="docutils literal notranslate"><span class="pre">master</span></code>. <code class="docutils literal notranslate"><span class="pre">default</span></code> implies a baseline on a database level rule and <code class="docutils literal notranslate"><span class="pre">master</span></code> for server level rule. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.baseline_results">
<code class="sig-name descname">baseline_results</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.baseline_results" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">baseline_result</span></code> block as documented below. Multiple blocks can be defined.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">results</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.database_name">
<code class="sig-name descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MS SQL Database. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.rule_id">
<code class="sig-name descname">rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The vulnerability assessment rule ID. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.server_vulnerability_assessment_id">
<code class="sig-name descname">server_vulnerability_assessment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.server_vulnerability_assessment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Vulnerability Assessment ID of the MS SQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">baseline_name=None</em>, <em class="sig-param">baseline_results=None</em>, <em class="sig-param">database_name=None</em>, <em class="sig-param">rule_id=None</em>, <em class="sig-param">server_vulnerability_assessment_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DatabaseVulnerabilityAssessmentRuleBaseline resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>baseline_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vulnerability assessment rule baseline. Valid options are <code class="docutils literal notranslate"><span class="pre">default</span></code> and <code class="docutils literal notranslate"><span class="pre">master</span></code>. <code class="docutils literal notranslate"><span class="pre">default</span></code> implies a baseline on a database level rule and <code class="docutils literal notranslate"><span class="pre">master</span></code> for server level rule. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>baseline_results</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">baseline_result</span></code> block as documented below. Multiple blocks can be defined.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MS SQL Database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vulnerability assessment rule ID. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_vulnerability_assessment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Vulnerability Assessment ID of the MS SQL Server. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>baseline_results</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">results</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_database_vulnerability_assessment_rule_baseline.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_database_vulnerability_assessment_rule_baseline.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">ServerSecurityAlertPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disabled_alerts=None</em>, <em class="sig-param">email_account_admins=None</em>, <em class="sig-param">email_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">retention_days=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">storage_account_access_key=None</em>, <em class="sig-param">storage_endpoint=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Security Alert Policy for a MSSQL Server.</p>
<blockquote>
<div><p><strong>NOTE</strong> Security Alert Policy is currently only available for MS SQL databases.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disabled_alerts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies an array of alerts that are disabled. Allowed values are: <code class="docutils literal notranslate"><span class="pre">Sql_Injection</span></code>, <code class="docutils literal notranslate"><span class="pre">Sql_Injection_Vulnerability</span></code>, <code class="docutils literal notranslate"><span class="pre">Access_Anomaly</span></code>, <code class="docutils literal notranslate"><span class="pre">Data_Exfiltration</span></code>, <code class="docutils literal notranslate"><span class="pre">Unsafe_Action</span></code>.</p></li>
<li><p><strong>email_account_admins</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which specifies if the alert is sent to the account administrators or not. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>email_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies an array of e-mail addresses to which the alert is sent.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group that contains the MS SQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of days to keep in the Threat Detection audit logs. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MS SQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database server. Allowed values are: <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">New</span></code>.</p></li>
<li><p><strong>storage_account_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the identifier key of the Threat Detection audit storage account.</p></li>
<li><p><strong>storage_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>). This blob storage will hold all Threat Detection audit logs.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_server_security_alert_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_server_security_alert_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.disabled_alerts">
<code class="sig-name descname">disabled_alerts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.disabled_alerts" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an array of alerts that are disabled. Allowed values are: <code class="docutils literal notranslate"><span class="pre">Sql_Injection</span></code>, <code class="docutils literal notranslate"><span class="pre">Sql_Injection_Vulnerability</span></code>, <code class="docutils literal notranslate"><span class="pre">Access_Anomaly</span></code>, <code class="docutils literal notranslate"><span class="pre">Data_Exfiltration</span></code>, <code class="docutils literal notranslate"><span class="pre">Unsafe_Action</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.email_account_admins">
<code class="sig-name descname">email_account_admins</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.email_account_admins" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which specifies if the alert is sent to the account administrators or not. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.email_addresses">
<code class="sig-name descname">email_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.email_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an array of e-mail addresses to which the alert is sent.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group that contains the MS SQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.retention_days">
<code class="sig-name descname">retention_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.retention_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of days to keep in the Threat Detection audit logs. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MS SQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database server. Allowed values are: <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">New</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.storage_account_access_key">
<code class="sig-name descname">storage_account_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.storage_account_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the identifier key of the Threat Detection audit storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.storage_endpoint">
<code class="sig-name descname">storage_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.storage_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>). This blob storage will hold all Threat Detection audit logs.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disabled_alerts=None</em>, <em class="sig-param">email_account_admins=None</em>, <em class="sig-param">email_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">retention_days=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">storage_account_access_key=None</em>, <em class="sig-param">storage_endpoint=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServerSecurityAlertPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disabled_alerts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies an array of alerts that are disabled. Allowed values are: <code class="docutils literal notranslate"><span class="pre">Sql_Injection</span></code>, <code class="docutils literal notranslate"><span class="pre">Sql_Injection_Vulnerability</span></code>, <code class="docutils literal notranslate"><span class="pre">Access_Anomaly</span></code>, <code class="docutils literal notranslate"><span class="pre">Data_Exfiltration</span></code>, <code class="docutils literal notranslate"><span class="pre">Unsafe_Action</span></code>.</p></li>
<li><p><strong>email_account_admins</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which specifies if the alert is sent to the account administrators or not. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>email_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies an array of e-mail addresses to which the alert is sent.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group that contains the MS SQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of days to keep in the Threat Detection audit logs. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MS SQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database server. Allowed values are: <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">New</span></code>.</p></li>
<li><p><strong>storage_account_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the identifier key of the Threat Detection audit storage account.</p></li>
<li><p><strong>storage_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>). This blob storage will hold all Threat Detection audit logs.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_server_security_alert_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_server_security_alert_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">ServerVulnerabilityAssessment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">recurring_scans=None</em>, <em class="sig-param">server_security_alert_policy_id=None</em>, <em class="sig-param">storage_account_access_key=None</em>, <em class="sig-param">storage_container_path=None</em>, <em class="sig-param">storage_container_sas_key=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the Vulnerability Assessment for a MS SQL Server.</p>
<blockquote>
<div><p><strong>NOTE</strong> Vulnerability Assessment is currently only available for MS SQL databases.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>recurring_scans</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The recurring scans settings. The <code class="docutils literal notranslate"><span class="pre">recurring_scans</span></code> block supports fields documented below.</p></li>
<li><p><strong>server_security_alert_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the security alert policy of the MS SQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the identifier key of the storage account for vulnerability assessment scan results. If <code class="docutils literal notranslate"><span class="pre">storage_container_sas_key</span></code> isn’t specified, <code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> is required.</p></li>
<li><p><strong>storage_container_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A blob storage container path to hold the scan results (e.g. <a class="reference external" href="https://myStorage.blob.core.windows.net/VaScans/">https://myStorage.blob.core.windows.net/VaScans/</a>).</p></li>
<li><p><strong>storage_container_sas_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A shared access signature (SAS Key) that has write access to the blob container specified in <code class="docutils literal notranslate"><span class="pre">storage_container_path</span></code> parameter. If <code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> isn’t specified, <code class="docutils literal notranslate"><span class="pre">storage_container_sas_key</span></code> is required.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>recurring_scans</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubscriptionAdmins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean flag which specifies if the schedule scan notification will be sent to the subscription administrators. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies an array of e-mail addresses to which the scan notification is sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean flag which specifies if recurring scans is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_server_vulnerability_assessment.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_server_vulnerability_assessment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.recurring_scans">
<code class="sig-name descname">recurring_scans</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.recurring_scans" title="Permalink to this definition">¶</a></dt>
<dd><p>The recurring scans settings. The <code class="docutils literal notranslate"><span class="pre">recurring_scans</span></code> block supports fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubscriptionAdmins</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean flag which specifies if the schedule scan notification will be sent to the subscription administrators. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies an array of e-mail addresses to which the scan notification is sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean flag which specifies if recurring scans is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.server_security_alert_policy_id">
<code class="sig-name descname">server_security_alert_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.server_security_alert_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the security alert policy of the MS SQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.storage_account_access_key">
<code class="sig-name descname">storage_account_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.storage_account_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the identifier key of the storage account for vulnerability assessment scan results. If <code class="docutils literal notranslate"><span class="pre">storage_container_sas_key</span></code> isn’t specified, <code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> is required.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.storage_container_path">
<code class="sig-name descname">storage_container_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.storage_container_path" title="Permalink to this definition">¶</a></dt>
<dd><p>A blob storage container path to hold the scan results (e.g. <a class="reference external" href="https://myStorage.blob.core.windows.net/VaScans/">https://myStorage.blob.core.windows.net/VaScans/</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.storage_container_sas_key">
<code class="sig-name descname">storage_container_sas_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.storage_container_sas_key" title="Permalink to this definition">¶</a></dt>
<dd><p>A shared access signature (SAS Key) that has write access to the blob container specified in <code class="docutils literal notranslate"><span class="pre">storage_container_path</span></code> parameter. If <code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> isn’t specified, <code class="docutils literal notranslate"><span class="pre">storage_container_sas_key</span></code> is required.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">recurring_scans=None</em>, <em class="sig-param">server_security_alert_policy_id=None</em>, <em class="sig-param">storage_account_access_key=None</em>, <em class="sig-param">storage_container_path=None</em>, <em class="sig-param">storage_container_sas_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServerVulnerabilityAssessment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>recurring_scans</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The recurring scans settings. The <code class="docutils literal notranslate"><span class="pre">recurring_scans</span></code> block supports fields documented below.</p></li>
<li><p><strong>server_security_alert_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the security alert policy of the MS SQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the identifier key of the storage account for vulnerability assessment scan results. If <code class="docutils literal notranslate"><span class="pre">storage_container_sas_key</span></code> isn’t specified, <code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> is required.</p></li>
<li><p><strong>storage_container_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A blob storage container path to hold the scan results (e.g. <a class="reference external" href="https://myStorage.blob.core.windows.net/VaScans/">https://myStorage.blob.core.windows.net/VaScans/</a>).</p></li>
<li><p><strong>storage_container_sas_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A shared access signature (SAS Key) that has write access to the blob container specified in <code class="docutils literal notranslate"><span class="pre">storage_container_path</span></code> parameter. If <code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> isn’t specified, <code class="docutils literal notranslate"><span class="pre">storage_container_sas_key</span></code> is required.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>recurring_scans</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubscriptionAdmins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean flag which specifies if the schedule scan notification will be sent to the subscription administrators. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies an array of e-mail addresses to which the scan notification is sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean flag which specifies if recurring scans is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_server_vulnerability_assessment.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mssql_server_vulnerability_assessment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
