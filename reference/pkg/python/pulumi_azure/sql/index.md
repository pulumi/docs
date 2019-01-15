<div class="section" id="module-pulumi_azure.sql">
<span id="sql"></span><h1>sql<a class="headerlink" href="#module-pulumi_azure.sql" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator">
<em class="property">class </em><code class="descclassname">pulumi_azure.sql.</code><code class="descname">ActiveDirectoryAdministrator</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>login=None</em>, <em>object_id=None</em>, <em>resource_group_name=None</em>, <em>server_name=None</em>, <em>tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to set a user or group as the AD administrator for an Azure SQL server</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The login name of the principal to set as the server administrator</li>
<li><strong>object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the principal to set as the server administrator</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group for the SQL server. Changing this forces a new resource to be created.</li>
<li><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server on which to set the administrator. Changing this forces a new resource to be created.</li>
<li><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Tenant ID</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.login">
<code class="descname">login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.login" title="Permalink to this definition">¶</a></dt>
<dd><p>The login name of the principal to set as the server administrator</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.object_id">
<code class="descname">object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the principal to set as the server administrator</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group for the SQL server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.server_name">
<code class="descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server on which to set the administrator. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Tenant ID</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.sql.Database">
<em class="property">class </em><code class="descclassname">pulumi_azure.sql.</code><code class="descname">Database</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>collation=None</em>, <em>create_mode=None</em>, <em>edition=None</em>, <em>elastic_pool_name=None</em>, <em>import_=None</em>, <em>location=None</em>, <em>max_size_bytes=None</em>, <em>name=None</em>, <em>requested_service_objective_id=None</em>, <em>requested_service_objective_name=None</em>, <em>resource_group_name=None</em>, <em>restore_point_in_time=None</em>, <em>server_name=None</em>, <em>source_database_deletion_date=None</em>, <em>source_database_id=None</em>, <em>tags=None</em>, <em>threat_detection_policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to manage an Azure SQL Database</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the collation. Applies only if <cite>create_mode</cite> is <cite>Default</cite>.  Azure default is <cite>SQL_LATIN1_GENERAL_CP1_CI_AS</cite>. Changing this forces a new resource to be created.</li>
<li><strong>create_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of database to create. Defaults to <cite>Default</cite>. See below for the accepted values/</li>
<li><strong>edition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The edition of the database to be created. Applies only if <cite>create_mode</cite> is <cite>Default</cite>. Valid values are: <cite>Basic</cite>, <cite>Standard</cite>, <cite>Premium</cite>, or <cite>DataWarehouse</cite>. Please see [Azure SQL Database Service Tiers](<a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/</a>).</li>
<li><strong>elastic_pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the elastic database pool.</li>
<li><strong>import</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Database Import block as documented below. <cite>create_mode</cite> must be set to <cite>Default</cite>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>max_size_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum size that the database can grow to. Applies only if <cite>create_mode</cite> is <cite>Default</cite>.  Please see [Azure SQL Database Service Tiers](<a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/</a>).</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database.</li>
<li><strong>requested_service_objective_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use <cite>requested_service_objective_id</cite> or <cite>requested_service_objective_name</cite> to set the performance level for the database.
Valid values are: <cite>S0</cite>, <cite>S1</cite>, <cite>S2</cite>, <cite>S3</cite>, <cite>P1</cite>, <cite>P2</cite>, <cite>P4</cite>, <cite>P6</cite>, <cite>P11</cite> and <cite>ElasticPool</cite>.  Please see [Azure SQL Database Service Tiers](<a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/</a>).</li>
<li><strong>requested_service_objective_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use <cite>requested_service_objective_name</cite> or <cite>requested_service_objective_id</cite> to set the performance level for the database.  Please see [Azure SQL Database Service Tiers](<a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/</a>).</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the database.  This must be the same as Database Server resource group currently.</li>
<li><strong>restore_point_in_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The point in time for the restore. Only applies if <cite>create_mode</cite> is <cite>PointInTimeRestore</cite> e.g. 2013-11-08T22:00:40Z</li>
<li><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server on which to create the database.</li>
<li><strong>source_database_deletion_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deletion date time of the source database. Only applies to deleted databases where <cite>create_mode</cite> is <cite>PointInTimeRestore</cite>.</li>
<li><strong>source_database_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the source database if <cite>create_mode</cite> value is not <cite>Default</cite>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>threat_detection_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Threat detection policy configuration. The <cite>threat_detection_policy</cite> block supports fields documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.sql.Database.collation">
<code class="descname">collation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.collation" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the collation. Applies only if <cite>create_mode</cite> is <cite>Default</cite>.  Azure default is <cite>SQL_LATIN1_GENERAL_CP1_CI_AS</cite>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.create_mode">
<code class="descname">create_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.create_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of database to create. Defaults to <cite>Default</cite>. See below for the accepted values/</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.creation_date">
<code class="descname">creation_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.creation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the SQL Database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.default_secondary_location">
<code class="descname">default_secondary_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.default_secondary_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The default secondary location of the SQL Database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.edition">
<code class="descname">edition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.edition" title="Permalink to this definition">¶</a></dt>
<dd><p>The edition of the database to be created. Applies only if <cite>create_mode</cite> is <cite>Default</cite>. Valid values are: <cite>Basic</cite>, <cite>Standard</cite>, <cite>Premium</cite>, or <cite>DataWarehouse</cite>. Please see [Azure SQL Database Service Tiers](<a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.elastic_pool_name">
<code class="descname">elastic_pool_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.elastic_pool_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the elastic database pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.import_">
<code class="descname">import_</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.import_" title="Permalink to this definition">¶</a></dt>
<dd><p>A Database Import block as documented below. <cite>create_mode</cite> must be set to <cite>Default</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.max_size_bytes">
<code class="descname">max_size_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.max_size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum size that the database can grow to. Applies only if <cite>create_mode</cite> is <cite>Default</cite>.  Please see [Azure SQL Database Service Tiers](<a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.requested_service_objective_id">
<code class="descname">requested_service_objective_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.requested_service_objective_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Use <cite>requested_service_objective_id</cite> or <cite>requested_service_objective_name</cite> to set the performance level for the database.
Valid values are: <cite>S0</cite>, <cite>S1</cite>, <cite>S2</cite>, <cite>S3</cite>, <cite>P1</cite>, <cite>P2</cite>, <cite>P4</cite>, <cite>P6</cite>, <cite>P11</cite> and <cite>ElasticPool</cite>.  Please see [Azure SQL Database Service Tiers](<a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.requested_service_objective_name">
<code class="descname">requested_service_objective_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.requested_service_objective_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Use <cite>requested_service_objective_name</cite> or <cite>requested_service_objective_id</cite> to set the performance level for the database.  Please see [Azure SQL Database Service Tiers](<a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the database.  This must be the same as Database Server resource group currently.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.restore_point_in_time">
<code class="descname">restore_point_in_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.restore_point_in_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The point in time for the restore. Only applies if <cite>create_mode</cite> is <cite>PointInTimeRestore</cite> e.g. 2013-11-08T22:00:40Z</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.server_name">
<code class="descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server on which to create the database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.source_database_deletion_date">
<code class="descname">source_database_deletion_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.source_database_deletion_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The deletion date time of the source database. Only applies to deleted databases where <cite>create_mode</cite> is <cite>PointInTimeRestore</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.source_database_id">
<code class="descname">source_database_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.source_database_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the source database if <cite>create_mode</cite> value is not <cite>Default</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.threat_detection_policy">
<code class="descname">threat_detection_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.threat_detection_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Threat detection policy configuration. The <cite>threat_detection_policy</cite> block supports fields documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.Database.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.Database.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.sql.ElasticPool">
<em class="property">class </em><code class="descclassname">pulumi_azure.sql.</code><code class="descname">ElasticPool</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>db_dtu_max=None</em>, <em>db_dtu_min=None</em>, <em>dtu=None</em>, <em>edition=None</em>, <em>location=None</em>, <em>name=None</em>, <em>pool_size=None</em>, <em>resource_group_name=None</em>, <em>server_name=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.ElasticPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to manage an Azure SQL Elastic Pool.</p>
<p>&gt; <strong>NOTE:</strong> -  This version of the <cite>Elasticpool</cite> resource is being <strong>deprecated</strong> and should no longer be used. Please use the azurerm_mssql_elasticpool version instead.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>db_dtu_max</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum DTU which will be guaranteed to all databases in the elastic pool to be created.</li>
<li><strong>db_dtu_min</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The minimum DTU which will be guaranteed to all databases in the elastic pool to be created.</li>
<li><strong>dtu</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The total shared DTU for the elastic pool. Valid values depend on the <cite>edition</cite> which has been defined. Refer to [Azure SQL Database Service Tiers](<a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus</a>) for valid combinations.</li>
<li><strong>edition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The edition of the elastic pool to be created. Valid values are <cite>Basic</cite>, <cite>Standard</cite>, and <cite>Premium</cite>. Refer to [Azure SQL Database Service Tiers](<a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus</a>) for details. Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.</li>
<li><strong>pool_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum size in MB that all databases in the elastic pool can grow to. The maximum size must be consistent with combination of <cite>edition</cite> and <cite>dtu</cite> and the limits documented in [Azure SQL Database Service Tiers](<a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus</a>). If not defined when creating an elastic pool, the value is set to the size implied by <cite>edition</cite> and <cite>dtu</cite>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.</li>
<li><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.creation_date">
<code class="descname">creation_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.creation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the SQL Elastic Pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.db_dtu_max">
<code class="descname">db_dtu_max</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.db_dtu_max" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum DTU which will be guaranteed to all databases in the elastic pool to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.db_dtu_min">
<code class="descname">db_dtu_min</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.db_dtu_min" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum DTU which will be guaranteed to all databases in the elastic pool to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.dtu">
<code class="descname">dtu</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.dtu" title="Permalink to this definition">¶</a></dt>
<dd><p>The total shared DTU for the elastic pool. Valid values depend on the <cite>edition</cite> which has been defined. Refer to [Azure SQL Database Service Tiers](<a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus</a>) for valid combinations.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.edition">
<code class="descname">edition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.edition" title="Permalink to this definition">¶</a></dt>
<dd><p>The edition of the elastic pool to be created. Valid values are <cite>Basic</cite>, <cite>Standard</cite>, and <cite>Premium</cite>. Refer to [Azure SQL Database Service Tiers](<a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus</a>) for details. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.pool_size">
<code class="descname">pool_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.pool_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum size in MB that all databases in the elastic pool can grow to. The maximum size must be consistent with combination of <cite>edition</cite> and <cite>dtu</cite> and the limits documented in [Azure SQL Database Service Tiers](<a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus</a>). If not defined when creating an elastic pool, the value is set to the size implied by <cite>edition</cite> and <cite>dtu</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.server_name">
<code class="descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.ElasticPool.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.ElasticPool.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.sql.FirewallRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.sql.</code><code class="descname">FirewallRule</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>end_ip_address=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>server_name=None</em>, <em>start_ip_address=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to manage an Azure SQL Firewall Rule</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>end_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ending IP address to allow through the firewall for this rule.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the firewall rule.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the sql server.</li>
<li><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server on which to create the Firewall Rule.</li>
<li><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The starting IP address to allow through the firewall for this rule.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.sql.FirewallRule.end_ip_address">
<code class="descname">end_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.end_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The ending IP address to allow through the firewall for this rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.FirewallRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.FirewallRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the sql server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.FirewallRule.server_name">
<code class="descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server on which to create the Firewall Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.FirewallRule.start_ip_address">
<code class="descname">start_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.start_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The starting IP address to allow through the firewall for this rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.FirewallRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.FirewallRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.sql.SqlServer">
<em class="property">class </em><code class="descclassname">pulumi_azure.sql.</code><code class="descname">SqlServer</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>administrator_login=None</em>, <em>administrator_login_password=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.SqlServer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a SQL Azure Database Server.</p>
<p>&gt; <strong>Note:</strong> All arguments including the administrator login and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">https://www.terraform.io/docs/state/sensitive-data.html</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>administrator_login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The administrator login name for the new server. Changing this forces a new resource to be created.</li>
<li><strong>administrator_login_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with the <cite>administrator_login</cite> user. Needs to comply with Azure’s [Password Policy](<a class="reference external" href="https://msdn.microsoft.com/library/ms161959.aspx">https://msdn.microsoft.com/library/ms161959.aspx</a>)</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server. This needs to be globally unique within Azure.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the SQL Server.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.administrator_login">
<code class="descname">administrator_login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.administrator_login" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrator login name for the new server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.administrator_login_password">
<code class="descname">administrator_login_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.administrator_login_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password associated with the <cite>administrator_login</cite> user. Needs to comply with Azure’s [Password Policy](<a class="reference external" href="https://msdn.microsoft.com/library/ms161959.aspx">https://msdn.microsoft.com/library/ms161959.aspx</a>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.fully_qualified_domain_name">
<code class="descname">fully_qualified_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.fully_qualified_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified domain name of the Azure SQL Server (e.g. myServerName.database.windows.net)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server. This needs to be globally unique within Azure.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the SQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.SqlServer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.SqlServer.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.SqlServer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.SqlServer.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.sql.VirtualNetworkRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.sql.</code><code class="descname">VirtualNetworkRule</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>ignore_missing_vnet_service_endpoint=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>server_name=None</em>, <em>subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to add, update, or remove an Azure SQL server to a subnet of a virtual network.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>ignore_missing_vnet_service_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Create the virtual network rule before the subnet has the virtual network service endpoint enabled. The default value is false.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL virtual network rule. Changing this forces a new resource to be created. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the SQL server resides. Changing this forces a new resource to be created.</li>
<li><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server to which this SQL virtual network rule will be applied to. Changing this forces a new resource to be created.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet that the SQL server will be connected to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.sql.VirtualNetworkRule.ignore_missing_vnet_service_endpoint">
<code class="descname">ignore_missing_vnet_service_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.ignore_missing_vnet_service_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Create the virtual network rule before the subnet has the virtual network service endpoint enabled. The default value is false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.VirtualNetworkRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL virtual network rule. Changing this forces a new resource to be created. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.VirtualNetworkRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group where the SQL server resides. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.VirtualNetworkRule.server_name">
<code class="descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server to which this SQL virtual network rule will be applied to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.VirtualNetworkRule.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the subnet that the SQL server will be connected to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.VirtualNetworkRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.VirtualNetworkRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
