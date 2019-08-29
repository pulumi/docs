---
title: Module sql
---

<div class="section" id="sql">
<h1>sql<a class="headerlink" href="#sql" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.sql"></span><dl class="class">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.sql.</code><code class="sig-name descname">ActiveDirectoryAdministrator</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">login=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to set a user or group as the AD administrator for an Azure SQL server</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The login name of the principal to set as the server administrator</p></li>
<li><p><strong>object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the principal to set as the server administrator</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group for the SQL server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server on which to set the administrator. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Tenant ID</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_active_directory_administrator.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_active_directory_administrator.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.login">
<code class="sig-name descname">login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.login" title="Permalink to this definition">¶</a></dt>
<dd><p>The login name of the principal to set as the server administrator</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.object_id">
<code class="sig-name descname">object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the principal to set as the server administrator</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group for the SQL server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server on which to set the administrator. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Tenant ID</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">login=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ActiveDirectoryAdministrator resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] login: The login name of the principal to set as the server administrator
:param pulumi.Input[str] object_id: The ID of the principal to set as the server administrator
:param pulumi.Input[str] resource_group_name: The name of the resource group for the SQL server. Changing this forces a new resource to be created.
:param pulumi.Input[str] server_name: The name of the SQL Server on which to set the administrator. Changing this forces a new resource to be created.
:param pulumi.Input[str] tenant_id: The Azure Tenant ID</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_active_directory_administrator.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_active_directory_administrator.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sql.ActiveDirectoryAdministrator.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.ActiveDirectoryAdministrator.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sql.AwaitableGetServerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.sql.</code><code class="sig-name descname">AwaitableGetServerResult</code><span class="sig-paren">(</span><em class="sig-param">administrator_login=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.AwaitableGetServerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.sql.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.sql.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">collation=None</em>, <em class="sig-param">create_mode=None</em>, <em class="sig-param">edition=None</em>, <em class="sig-param">elastic_pool_name=None</em>, <em class="sig-param">import_=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">max_size_bytes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">read_scale=None</em>, <em class="sig-param">requested_service_objective_id=None</em>, <em class="sig-param">requested_service_objective_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">restore_point_in_time=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">source_database_deletion_date=None</em>, <em class="sig-param">source_database_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">threat_detection_policy=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to manage an Azure SQL Database</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the collation. Applies only if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Default</span></code>.  Azure default is <code class="docutils literal notranslate"><span class="pre">SQL_LATIN1_GENERAL_CP1_CI_AS</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>create_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how to create the database. Must be either <code class="docutils literal notranslate"><span class="pre">Default</span></code> to create a new database or <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code> to restore from a snapshot. Defaults to <code class="docutils literal notranslate"><span class="pre">Default</span></code>.</p></li>
<li><p><strong>edition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The edition of the database to be created. Applies only if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Default</span></code>. Valid values are: <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">DataWarehouse</span></code>, <code class="docutils literal notranslate"><span class="pre">Business</span></code>, <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code>, <code class="docutils literal notranslate"><span class="pre">Free</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralPurpose</span></code>, <code class="docutils literal notranslate"><span class="pre">Hyperscale</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">PremiumRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Stretch</span></code>, <code class="docutils literal notranslate"><span class="pre">System</span></code>, <code class="docutils literal notranslate"><span class="pre">System2</span></code>, or <code class="docutils literal notranslate"><span class="pre">Web</span></code>. Please see <a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">Azure SQL Database Service Tiers</a>.</p></li>
<li><p><strong>elastic_pool*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the elastic database pool.</p>
</p></li>
</ul>
</dd>
</dl>
<p>:param pulumi.Input[dict] import*: A Database Import block as documented below. <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">Default</span></code>.
:param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] max_size_bytes: The maximum size that the database can grow to. Applies only if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Default</span></code>.  Please see <a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">Azure SQL Database Service Tiers</a>.
:param pulumi.Input[str] name: The name of the database.
:param pulumi.Input[bool] read_scale: Read-only connections will be redirected to a high-available replica. Please see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-read-scale-out">Use read-only replicas to load-balance read-only query workloads</a>.
:param pulumi.Input[str] requested_service_objective_id: Use <code class="docutils literal notranslate"><span class="pre">requested_service_objective_id</span></code> or <code class="docutils literal notranslate"><span class="pre">requested_service_objective_name</span></code> to set the performance level for the database.</p>
<blockquote>
<div><p>Please see <a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">Azure SQL Database Service Tiers</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>requested_service_objective_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Use <code class="docutils literal notranslate"><span class="pre">requested_service_objective_name</span></code> or <code class="docutils literal notranslate"><span class="pre">requested_service_objective_id</span></code> to set the performance level for the database. Valid values are: <code class="docutils literal notranslate"><span class="pre">S0</span></code>, <code class="docutils literal notranslate"><span class="pre">S1</span></code>, <code class="docutils literal notranslate"><span class="pre">S2</span></code>, <code class="docutils literal notranslate"><span class="pre">S3</span></code>, <code class="docutils literal notranslate"><span class="pre">P1</span></code>, <code class="docutils literal notranslate"><span class="pre">P2</span></code>, <code class="docutils literal notranslate"><span class="pre">P4</span></code>, <code class="docutils literal notranslate"><span class="pre">P6</span></code>, <code class="docutils literal notranslate"><span class="pre">P11</span></code> and <code class="docutils literal notranslate"><span class="pre">ElasticPool</span></code>.  Please see <a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">Azure SQL Database Service Tiers</a>.</p>
</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the database.  This must be the same as Database Server resource group currently.</p></li>
<li><p><strong>restore_point_in_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The point in time for the restore. Only applies if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code> e.g. 2013-11-08T22:00:40Z</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server on which to create the database.</p></li>
<li><p><strong>source_database_deletion_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deletion date time of the source database. Only applies to deleted databases where <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code>.</p></li>
<li><p><strong>source_database_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the source database if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> value is not <code class="docutils literal notranslate"><span class="pre">Default</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>threat_detection_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Threat detection policy configuration. The <code class="docutils literal notranslate"><span class="pre">threat_detection_policy</span></code> block supports fields documented below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_database.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_database.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.sql.Database.collation">
<code class="sig-name descname">collation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.collation" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the collation. Applies only if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Default</span></code>.  Azure default is <code class="docutils literal notranslate"><span class="pre">SQL_LATIN1_GENERAL_CP1_CI_AS</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.create_mode">
<code class="sig-name descname">create_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.create_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how to create the database. Must be either <code class="docutils literal notranslate"><span class="pre">Default</span></code> to create a new database or <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code> to restore from a snapshot. Defaults to <code class="docutils literal notranslate"><span class="pre">Default</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.creation_date">
<code class="sig-name descname">creation_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.creation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the SQL Database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.default_secondary_location">
<code class="sig-name descname">default_secondary_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.default_secondary_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The default secondary location of the SQL Database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.edition">
<code class="sig-name descname">edition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.edition" title="Permalink to this definition">¶</a></dt>
<dd><p>The edition of the database to be created. Applies only if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Default</span></code>. Valid values are: <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">DataWarehouse</span></code>, <code class="docutils literal notranslate"><span class="pre">Business</span></code>, <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code>, <code class="docutils literal notranslate"><span class="pre">Free</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralPurpose</span></code>, <code class="docutils literal notranslate"><span class="pre">Hyperscale</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">PremiumRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Stretch</span></code>, <code class="docutils literal notranslate"><span class="pre">System</span></code>, <code class="docutils literal notranslate"><span class="pre">System2</span></code>, or <code class="docutils literal notranslate"><span class="pre">Web</span></code>. Please see <a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">Azure SQL Database Service Tiers</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.elastic_pool_name">
<code class="sig-name descname">elastic_pool_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.elastic_pool_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the elastic database pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.import_">
<code class="sig-name descname">import_</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.import_" title="Permalink to this definition">¶</a></dt>
<dd><p>A Database Import block as documented below. <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">Default</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.max_size_bytes">
<code class="sig-name descname">max_size_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.max_size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum size that the database can grow to. Applies only if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Default</span></code>.  Please see <a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">Azure SQL Database Service Tiers</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.read_scale">
<code class="sig-name descname">read_scale</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.read_scale" title="Permalink to this definition">¶</a></dt>
<dd><p>Read-only connections will be redirected to a high-available replica. Please see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-read-scale-out">Use read-only replicas to load-balance read-only query workloads</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.requested_service_objective_id">
<code class="sig-name descname">requested_service_objective_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.requested_service_objective_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Use <code class="docutils literal notranslate"><span class="pre">requested_service_objective_id</span></code> or <code class="docutils literal notranslate"><span class="pre">requested_service_objective_name</span></code> to set the performance level for the database.
Please see <a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">Azure SQL Database Service Tiers</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.requested_service_objective_name">
<code class="sig-name descname">requested_service_objective_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.requested_service_objective_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Use <code class="docutils literal notranslate"><span class="pre">requested_service_objective_name</span></code> or <code class="docutils literal notranslate"><span class="pre">requested_service_objective_id</span></code> to set the performance level for the database. Valid values are: <code class="docutils literal notranslate"><span class="pre">S0</span></code>, <code class="docutils literal notranslate"><span class="pre">S1</span></code>, <code class="docutils literal notranslate"><span class="pre">S2</span></code>, <code class="docutils literal notranslate"><span class="pre">S3</span></code>, <code class="docutils literal notranslate"><span class="pre">P1</span></code>, <code class="docutils literal notranslate"><span class="pre">P2</span></code>, <code class="docutils literal notranslate"><span class="pre">P4</span></code>, <code class="docutils literal notranslate"><span class="pre">P6</span></code>, <code class="docutils literal notranslate"><span class="pre">P11</span></code> and <code class="docutils literal notranslate"><span class="pre">ElasticPool</span></code>.  Please see <a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">Azure SQL Database Service Tiers</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the database.  This must be the same as Database Server resource group currently.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.restore_point_in_time">
<code class="sig-name descname">restore_point_in_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.restore_point_in_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The point in time for the restore. Only applies if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code> e.g. 2013-11-08T22:00:40Z</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server on which to create the database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.source_database_deletion_date">
<code class="sig-name descname">source_database_deletion_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.source_database_deletion_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The deletion date time of the source database. Only applies to deleted databases where <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.source_database_id">
<code class="sig-name descname">source_database_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.source_database_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the source database if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> value is not <code class="docutils literal notranslate"><span class="pre">Default</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.Database.threat_detection_policy">
<code class="sig-name descname">threat_detection_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.Database.threat_detection_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Threat detection policy configuration. The <code class="docutils literal notranslate"><span class="pre">threat_detection_policy</span></code> block supports fields documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.Database.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">collation=None</em>, <em class="sig-param">create_mode=None</em>, <em class="sig-param">creation_date=None</em>, <em class="sig-param">default_secondary_location=None</em>, <em class="sig-param">edition=None</em>, <em class="sig-param">elastic_pool_name=None</em>, <em class="sig-param">encryption=None</em>, <em class="sig-param">import_=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">max_size_bytes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">read_scale=None</em>, <em class="sig-param">requested_service_objective_id=None</em>, <em class="sig-param">requested_service_objective_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">restore_point_in_time=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">source_database_deletion_date=None</em>, <em class="sig-param">source_database_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">threat_detection_policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] collation: The name of the collation. Applies only if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Default</span></code>.  Azure default is <code class="docutils literal notranslate"><span class="pre">SQL_LATIN1_GENERAL_CP1_CI_AS</span></code>. Changing this forces a new resource to be created.
:param pulumi.Input[str] create_mode: Specifies how to create the database. Must be either <code class="docutils literal notranslate"><span class="pre">Default</span></code> to create a new database or <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code> to restore from a snapshot. Defaults to <code class="docutils literal notranslate"><span class="pre">Default</span></code>.
:param pulumi.Input[str] creation_date: The creation date of the SQL Database.
:param pulumi.Input[str] default_secondary_location: The default secondary location of the SQL Database.
:param pulumi.Input[str] edition: The edition of the database to be created. Applies only if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Default</span></code>. Valid values are: <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">DataWarehouse</span></code>, <code class="docutils literal notranslate"><span class="pre">Business</span></code>, <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code>, <code class="docutils literal notranslate"><span class="pre">Free</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralPurpose</span></code>, <code class="docutils literal notranslate"><span class="pre">Hyperscale</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">PremiumRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Stretch</span></code>, <code class="docutils literal notranslate"><span class="pre">System</span></code>, <code class="docutils literal notranslate"><span class="pre">System2</span></code>, or <code class="docutils literal notranslate"><span class="pre">Web</span></code>. Please see <a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">Azure SQL Database Service Tiers</a>.
:param pulumi.Input[str] elastic_pool<em>name: The name of the elastic database pool.
:param pulumi.Input[dict] import</em>: A Database Import block as documented below. <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">Default</span></code>.
:param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] max_size_bytes: The maximum size that the database can grow to. Applies only if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Default</span></code>.  Please see <a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">Azure SQL Database Service Tiers</a>.
:param pulumi.Input[str] name: The name of the database.
:param pulumi.Input[bool] read_scale: Read-only connections will be redirected to a high-available replica. Please see <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-read-scale-out">Use read-only replicas to load-balance read-only query workloads</a>.
:param pulumi.Input[str] requested_service_objective_id: Use <code class="docutils literal notranslate"><span class="pre">requested_service_objective_id</span></code> or <code class="docutils literal notranslate"><span class="pre">requested_service_objective_name</span></code> to set the performance level for the database.</p>
<blockquote>
<div><p>Please see <a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">Azure SQL Database Service Tiers</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>requested_service_objective_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Use <code class="docutils literal notranslate"><span class="pre">requested_service_objective_name</span></code> or <code class="docutils literal notranslate"><span class="pre">requested_service_objective_id</span></code> to set the performance level for the database. Valid values are: <code class="docutils literal notranslate"><span class="pre">S0</span></code>, <code class="docutils literal notranslate"><span class="pre">S1</span></code>, <code class="docutils literal notranslate"><span class="pre">S2</span></code>, <code class="docutils literal notranslate"><span class="pre">S3</span></code>, <code class="docutils literal notranslate"><span class="pre">P1</span></code>, <code class="docutils literal notranslate"><span class="pre">P2</span></code>, <code class="docutils literal notranslate"><span class="pre">P4</span></code>, <code class="docutils literal notranslate"><span class="pre">P6</span></code>, <code class="docutils literal notranslate"><span class="pre">P11</span></code> and <code class="docutils literal notranslate"><span class="pre">ElasticPool</span></code>.  Please see <a class="reference external" href="https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/">Azure SQL Database Service Tiers</a>.</p>
</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the database.  This must be the same as Database Server resource group currently.</p></li>
<li><p><strong>restore_point_in_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The point in time for the restore. Only applies if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code> e.g. 2013-11-08T22:00:40Z</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server on which to create the database.</p></li>
<li><p><strong>source_database_deletion_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deletion date time of the source database. Only applies to deleted databases where <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code>.</p></li>
<li><p><strong>source_database_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the source database if <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> value is not <code class="docutils literal notranslate"><span class="pre">Default</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>threat_detection_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Threat detection policy configuration. The <code class="docutils literal notranslate"><span class="pre">threat_detection_policy</span></code> block supports fields documented below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_database.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_database.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.Database.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sql.Database.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sql.ElasticPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.sql.</code><code class="sig-name descname">ElasticPool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">db_dtu_max=None</em>, <em class="sig-param">db_dtu_min=None</em>, <em class="sig-param">dtu=None</em>, <em class="sig-param">edition=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_size=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.ElasticPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to manage an Azure SQL Elastic Pool.</p>
<blockquote>
<div><p><strong>NOTE:</strong> -  This version of the <code class="docutils literal notranslate"><span class="pre">Elasticpool</span></code> resource is being <strong>deprecated</strong> and should no longer be used. Please use the mssql.ElasticPool version instead.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>db_dtu_max</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum DTU which will be guaranteed to all databases in the elastic pool to be created.</p></li>
<li><p><strong>db_dtu_min</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum DTU which will be guaranteed to all databases in the elastic pool to be created.</p></li>
<li><p><strong>dtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The total shared DTU for the elastic pool. Valid values depend on the <code class="docutils literal notranslate"><span class="pre">edition</span></code> which has been defined. Refer to <a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">Azure SQL Database Service Tiers</a> for valid combinations.</p>
</p></li>
<li><p><strong>edition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The edition of the elastic pool to be created. Valid values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Refer to <a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">Azure SQL Database Service Tiers</a> for details. Changing this forces a new resource to be created.</p>
</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.</p></li>
<li><p><strong>pool_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The maximum size in MB that all databases in the elastic pool can grow to. The maximum size must be consistent with combination of <code class="docutils literal notranslate"><span class="pre">edition</span></code> and <code class="docutils literal notranslate"><span class="pre">dtu</span></code> and the limits documented in <a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">Azure SQL Database Service Tiers</a>. If not defined when creating an elastic pool, the value is set to the size implied by <code class="docutils literal notranslate"><span class="pre">edition</span></code> and <code class="docutils literal notranslate"><span class="pre">dtu</span></code>.</p>
</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_elasticpool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_elasticpool.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.creation_date">
<code class="sig-name descname">creation_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.creation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the SQL Elastic Pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.db_dtu_max">
<code class="sig-name descname">db_dtu_max</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.db_dtu_max" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum DTU which will be guaranteed to all databases in the elastic pool to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.db_dtu_min">
<code class="sig-name descname">db_dtu_min</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.db_dtu_min" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum DTU which will be guaranteed to all databases in the elastic pool to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.dtu">
<code class="sig-name descname">dtu</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.dtu" title="Permalink to this definition">¶</a></dt>
<dd><p>The total shared DTU for the elastic pool. Valid values depend on the <code class="docutils literal notranslate"><span class="pre">edition</span></code> which has been defined. Refer to <a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">Azure SQL Database Service Tiers</a> for valid combinations.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.edition">
<code class="sig-name descname">edition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.edition" title="Permalink to this definition">¶</a></dt>
<dd><p>The edition of the elastic pool to be created. Valid values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Refer to <a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">Azure SQL Database Service Tiers</a> for details. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.pool_size">
<code class="sig-name descname">pool_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.pool_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum size in MB that all databases in the elastic pool can grow to. The maximum size must be consistent with combination of <code class="docutils literal notranslate"><span class="pre">edition</span></code> and <code class="docutils literal notranslate"><span class="pre">dtu</span></code> and the limits documented in <a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">Azure SQL Database Service Tiers</a>. If not defined when creating an elastic pool, the value is set to the size implied by <code class="docutils literal notranslate"><span class="pre">edition</span></code> and <code class="docutils literal notranslate"><span class="pre">dtu</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.ElasticPool.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.ElasticPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">creation_date=None</em>, <em class="sig-param">db_dtu_max=None</em>, <em class="sig-param">db_dtu_min=None</em>, <em class="sig-param">dtu=None</em>, <em class="sig-param">edition=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_size=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ElasticPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] creation_date: The creation date of the SQL Elastic Pool.
:param pulumi.Input[float] db_dtu_max: The maximum DTU which will be guaranteed to all databases in the elastic pool to be created.
:param pulumi.Input[float] db_dtu_min: The minimum DTU which will be guaranteed to all databases in the elastic pool to be created.
:param pulumi.Input[float] dtu: The total shared DTU for the elastic pool. Valid values depend on the <code class="docutils literal notranslate"><span class="pre">edition</span></code> which has been defined. Refer to <a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">Azure SQL Database Service Tiers</a> for valid combinations.
:param pulumi.Input[str] edition: The edition of the elastic pool to be created. Valid values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Refer to <a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">Azure SQL Database Service Tiers</a> for details. Changing this forces a new resource to be created.
:param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.
:param pulumi.Input[float] pool_size: The maximum size in MB that all databases in the elastic pool can grow to. The maximum size must be consistent with combination of <code class="docutils literal notranslate"><span class="pre">edition</span></code> and <code class="docutils literal notranslate"><span class="pre">dtu</span></code> and the limits documented in <a class="reference external" href="https://docs.microsoft.com/en-gb/azure/sql-database/sql-database-service-tiers#elastic-pool-service-tiers-and-performance-in-edtus">Azure SQL Database Service Tiers</a>. If not defined when creating an elastic pool, the value is set to the size implied by <code class="docutils literal notranslate"><span class="pre">edition</span></code> and <code class="docutils literal notranslate"><span class="pre">dtu</span></code>.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.
:param pulumi.Input[str] server_name: The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_elasticpool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_elasticpool.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.ElasticPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sql.ElasticPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.ElasticPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sql.FirewallRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.sql.</code><code class="sig-name descname">FirewallRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">end_ip_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">start_ip_address=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to manage an Azure SQL Firewall Rule</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ending IP address to allow through the firewall for this rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the firewall rule.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the sql server.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server on which to create the Firewall Rule.</p></li>
<li><p><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The starting IP address to allow through the firewall for this rule.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_firewall_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.sql.FirewallRule.end_ip_address">
<code class="sig-name descname">end_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.end_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The ending IP address to allow through the firewall for this rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.FirewallRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the firewall rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.FirewallRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the sql server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.FirewallRule.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server on which to create the Firewall Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.FirewallRule.start_ip_address">
<code class="sig-name descname">start_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.start_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The starting IP address to allow through the firewall for this rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.FirewallRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">end_ip_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">start_ip_address=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] end_ip_address: The ending IP address to allow through the firewall for this rule.
:param pulumi.Input[str] name: The name of the firewall rule.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to</p>
<blockquote>
<div><p>create the sql server.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server on which to create the Firewall Rule.</p></li>
<li><p><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The starting IP address to allow through the firewall for this rule.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_firewall_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.FirewallRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sql.FirewallRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sql.GetServerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.sql.</code><code class="sig-name descname">GetServerResult</code><span class="sig-paren">(</span><em class="sig-param">administrator_login=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.GetServerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServer.</p>
<dl class="attribute">
<dt id="pulumi_azure.sql.GetServerResult.administrator_login">
<code class="sig-name descname">administrator_login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.GetServerResult.administrator_login" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrator username of the SQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.GetServerResult.fqdn">
<code class="sig-name descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.GetServerResult.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified domain name of the SQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.GetServerResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.GetServerResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the Resource Group in which the SQL Server exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.GetServerResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.GetServerResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.GetServerResult.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.GetServerResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the SQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.GetServerResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.GetServerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.sql.SqlServer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.sql.</code><code class="sig-name descname">SqlServer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">administrator_login=None</em>, <em class="sig-param">administrator_login_password=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.SqlServer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a SQL Azure Database Server.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the administrator login and password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>administrator_login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The administrator login name for the new server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>administrator_login_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> user. Needs to comply with Azure’s <a class="reference external" href="https://msdn.microsoft.com/library/ms161959.aspx">Password Policy</a></p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server. This needs to be globally unique within Azure.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the SQL Server.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_server.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_server.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.administrator_login">
<code class="sig-name descname">administrator_login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.administrator_login" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrator login name for the new server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.administrator_login_password">
<code class="sig-name descname">administrator_login_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.administrator_login_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> user. Needs to comply with Azure’s <a class="reference external" href="https://msdn.microsoft.com/library/ms161959.aspx">Password Policy</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.fully_qualified_domain_name">
<code class="sig-name descname">fully_qualified_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.fully_qualified_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified domain name of the Azure SQL Server (e.g. myServerName.database.windows.net)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server. This needs to be globally unique within Azure.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the SQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.SqlServer.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.SqlServer.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.SqlServer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">administrator_login=None</em>, <em class="sig-param">administrator_login_password=None</em>, <em class="sig-param">fully_qualified_domain_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.SqlServer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SqlServer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] administrator_login: The administrator login name for the new server. Changing this forces a new resource to be created.
:param pulumi.Input[str] administrator_login_password: The password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> user. Needs to comply with Azure’s <a class="reference external" href="https://msdn.microsoft.com/library/ms161959.aspx">Password Policy</a>
:param pulumi.Input[str] fully_qualified_domain_name: The fully qualified domain name of the Azure SQL Server (e.g. myServerName.database.windows.net)
:param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: The name of the SQL Server. This needs to be globally unique within Azure.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the SQL Server.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
:param pulumi.Input[str] version: The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_server.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_server.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.SqlServer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.SqlServer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sql.SqlServer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.SqlServer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sql.VirtualNetworkRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.sql.</code><code class="sig-name descname">VirtualNetworkRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ignore_missing_vnet_service_endpoint=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to add, update, or remove an Azure SQL server to a subnet of a virtual network.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ignore_missing_vnet_service_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Create the virtual network rule before the subnet has the virtual network service endpoint enabled. The default value is false.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL virtual network rule. Changing this forces a new resource to be created. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the SQL server resides. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server to which this SQL virtual network rule will be applied to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet that the SQL server will be connected to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_virtual_network_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_virtual_network_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.sql.VirtualNetworkRule.ignore_missing_vnet_service_endpoint">
<code class="sig-name descname">ignore_missing_vnet_service_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.ignore_missing_vnet_service_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Create the virtual network rule before the subnet has the virtual network service endpoint enabled. The default value is false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.VirtualNetworkRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL virtual network rule. Changing this forces a new resource to be created. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.VirtualNetworkRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group where the SQL server resides. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.VirtualNetworkRule.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server to which this SQL virtual network rule will be applied to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.sql.VirtualNetworkRule.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the subnet that the SQL server will be connected to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.VirtualNetworkRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ignore_missing_vnet_service_endpoint=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualNetworkRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] ignore_missing_vnet_service_endpoint: Create the virtual network rule before the subnet has the virtual network service endpoint enabled. The default value is false.
:param pulumi.Input[str] name: The name of the SQL virtual network rule. Changing this forces a new resource to be created. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen.
:param pulumi.Input[str] resource_group_name: The name of the resource group where the SQL server resides. Changing this forces a new resource to be created.
:param pulumi.Input[str] server_name: The name of the SQL Server to which this SQL virtual network rule will be applied to. Changing this forces a new resource to be created.
:param pulumi.Input[str] subnet_id: The ID of the subnet that the SQL server will be connected to.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_virtual_network_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/sql_virtual_network_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.sql.VirtualNetworkRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sql.VirtualNetworkRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.VirtualNetworkRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sql.get_server">
<code class="sig-prename descclassname">pulumi_azure.sql.</code><code class="sig-name descname">get_server</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sql.get_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing SQL Azure Database Server.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/sql_server.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/sql_server.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
