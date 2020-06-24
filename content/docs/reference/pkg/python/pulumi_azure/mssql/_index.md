---
title: Module mssql
title_tag: Module mssql | Package pulumi_azure | Python SDK
linktitle: mssql
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azure" >}}

<div class="section" id="mssql">
<h1>mssql<a class="headerlink" href="#mssql" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.mssql"></span><dl class="py class">
<dt id="pulumi_azure.mssql.AwaitableGetDatabaseResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">AwaitableGetDatabaseResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">collation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_replica_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_scale</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_redundant</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.AwaitableGetDatabaseResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.mssql.AwaitableGetElasticPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">AwaitableGetElasticPoolResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size_bytes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">per_db_max_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">per_db_min_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_redundant</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.AwaitableGetElasticPoolResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.mssql.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_pause_delay_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">collation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_source_database_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_auditing_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_replica_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_scale</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restore_point_in_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sample_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threat_detection_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_redundant</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a MS SQL Database.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West Europe&quot;</span><span class="p">)</span>
<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;exampleAccount&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">account_tier</span><span class="o">=</span><span class="s2">&quot;Standard&quot;</span><span class="p">,</span>
    <span class="n">account_replication_type</span><span class="o">=</span><span class="s2">&quot;LRS&quot;</span><span class="p">)</span>
<span class="n">example_sql_server</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">sql</span><span class="o">.</span><span class="n">SqlServer</span><span class="p">(</span><span class="s2">&quot;exampleSqlServer&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">&quot;12.0&quot;</span><span class="p">,</span>
    <span class="n">administrator_login</span><span class="o">=</span><span class="s2">&quot;4dm1n157r470r&quot;</span><span class="p">,</span>
    <span class="n">administrator_login_password</span><span class="o">=</span><span class="s2">&quot;4-v3ry-53cr37-p455w0rd&quot;</span><span class="p">)</span>
<span class="n">test</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">mssql</span><span class="o">.</span><span class="n">Database</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">server_id</span><span class="o">=</span><span class="n">example_sql_server</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">collation</span><span class="o">=</span><span class="s2">&quot;SQL_Latin1_General_CP1_CI_AS&quot;</span><span class="p">,</span>
    <span class="n">license_type</span><span class="o">=</span><span class="s2">&quot;LicenseIncluded&quot;</span><span class="p">,</span>
    <span class="n">max_size_gb</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span>
    <span class="n">read_scale</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">sku_name</span><span class="o">=</span><span class="s2">&quot;BC_Gen5_2&quot;</span><span class="p">,</span>
    <span class="n">zone_redundant</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">extended_auditing_policy</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;storage_endpoint&quot;</span><span class="p">:</span> <span class="n">example_account</span><span class="o">.</span><span class="n">primary_blob_endpoint</span><span class="p">,</span>
        <span class="s2">&quot;storage_account_access_key&quot;</span><span class="p">:</span> <span class="n">example_account</span><span class="o">.</span><span class="n">primary_access_key</span><span class="p">,</span>
        <span class="s2">&quot;storageAccountAccessKeyIsSecondary&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;retention_in_days&quot;</span><span class="p">:</span> <span class="mi">6</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_pause_delay_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time in minutes after which database is automatically paused. A value of <code class="docutils literal notranslate"><span class="pre">-1</span></code> means that automatic pause is disabled. This property is only settable for General Purpose Serverless databases.</p></li>
<li><p><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the collation of the database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>create_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The create mode of the database. Possible values are <code class="docutils literal notranslate"><span class="pre">Copy</span></code>, <code class="docutils literal notranslate"><span class="pre">Default</span></code>, <code class="docutils literal notranslate"><span class="pre">OnlineSecondary</span></code>, <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code>, <code class="docutils literal notranslate"><span class="pre">Restore</span></code>, <code class="docutils literal notranslate"><span class="pre">RestoreExternalBackup</span></code>, <code class="docutils literal notranslate"><span class="pre">RestoreExternalBackupSecondary</span></code>, <code class="docutils literal notranslate"><span class="pre">RestoreLongTermRetentionBackup</span></code> and <code class="docutils literal notranslate"><span class="pre">Secondary</span></code>.</p></li>
<li><p><strong>creation_source_database_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the source database to be referred to create the new database. This should only be used for databases with <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> values that use another database as reference. Changing this forces a new resource to be created.</p></li>
<li><p><strong>elastic_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the elastic pool containing this database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>extended_auditing_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">extended_auditing_policy</span></code> block as defined below.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the license type applied to this database. Possible values are <code class="docutils literal notranslate"><span class="pre">LicenseIncluded</span></code> and <code class="docutils literal notranslate"><span class="pre">BasePrice</span></code>.</p></li>
<li><p><strong>max_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max size of the database in gigabytes.</p></li>
<li><p><strong>min_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimal capacity that database will always have allocated, if not paused. This property is only settable for General Purpose Serverless databases.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Ms SQL Database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>read_replica_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of readonly secondary replicas associated with the database to which readonly application intent connections may be routed. This property is only settable for Hyperscale edition databases.</p></li>
<li><p><strong>read_scale</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.</p></li>
<li><p><strong>restore_point_in_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. This property is only settable for <code class="docutils literal notranslate"><span class="pre">create_mode</span></code>= <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code>  databases.</p></li>
<li><p><strong>sample_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the sample schema to apply when creating this database. Possible value is <code class="docutils literal notranslate"><span class="pre">AdventureWorksLT</span></code>.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the Ms SQL Server on which to create the database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the sku used by the database. Changing this forces a new resource to be created. For example, <code class="docutils literal notranslate"><span class="pre">GP_S_Gen5_2</span></code>,<code class="docutils literal notranslate"><span class="pre">HS_Gen4_1</span></code>,<code class="docutils literal notranslate"><span class="pre">BC_Gen5_2</span></code>, <code class="docutils literal notranslate"><span class="pre">ElasticPool</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code>,<code class="docutils literal notranslate"><span class="pre">S0</span></code>, <code class="docutils literal notranslate"><span class="pre">P2</span></code> ,<code class="docutils literal notranslate"><span class="pre">DW100c</span></code>, <code class="docutils literal notranslate"><span class="pre">DS100</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>threat_detection_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Threat detection policy configuration. The <code class="docutils literal notranslate"><span class="pre">threat_detection_policy</span></code> block supports fields documented below.</p></li>
<li><p><strong>zone_redundant</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones. This property is only settable for Premium and Business Critical databases.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>extended_auditing_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of days to retain logs for in the storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the access key to use for the auditing storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountAccessKeyIsSecondary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether <code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> value is the storage’s secondary key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>).</p></li>
</ul>
<p>The <strong>threat_detection_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disabled_alerts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of alerts which should be disabled. Possible values include <code class="docutils literal notranslate"><span class="pre">Access_Anomaly</span></code>, <code class="docutils literal notranslate"><span class="pre">Sql_Injection</span></code> and <code class="docutils literal notranslate"><span class="pre">Sql_Injection_Vulnerability</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email_account_admins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Should the account administrators be emailed when this alert is triggered?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of email addresses which alerts should be sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of days to keep in the Threat Detection audit logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The State of the Policy. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Disabled</span></code> or <code class="docutils literal notranslate"><span class="pre">New</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identifier key of the Threat Detection audit storage account. Required if <code class="docutils literal notranslate"><span class="pre">state</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>). This blob storage will hold all Threat Detection audit logs. Required if <code class="docutils literal notranslate"><span class="pre">state</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useServerDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Should the default server policy be used? Defaults to <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.auto_pause_delay_in_minutes">
<code class="sig-name descname">auto_pause_delay_in_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.auto_pause_delay_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Time in minutes after which database is automatically paused. A value of <code class="docutils literal notranslate"><span class="pre">-1</span></code> means that automatic pause is disabled. This property is only settable for General Purpose Serverless databases.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.collation">
<code class="sig-name descname">collation</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.collation" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the collation of the database. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.create_mode">
<code class="sig-name descname">create_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.create_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The create mode of the database. Possible values are <code class="docutils literal notranslate"><span class="pre">Copy</span></code>, <code class="docutils literal notranslate"><span class="pre">Default</span></code>, <code class="docutils literal notranslate"><span class="pre">OnlineSecondary</span></code>, <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code>, <code class="docutils literal notranslate"><span class="pre">Restore</span></code>, <code class="docutils literal notranslate"><span class="pre">RestoreExternalBackup</span></code>, <code class="docutils literal notranslate"><span class="pre">RestoreExternalBackupSecondary</span></code>, <code class="docutils literal notranslate"><span class="pre">RestoreLongTermRetentionBackup</span></code> and <code class="docutils literal notranslate"><span class="pre">Secondary</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.creation_source_database_id">
<code class="sig-name descname">creation_source_database_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.creation_source_database_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the source database to be referred to create the new database. This should only be used for databases with <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> values that use another database as reference. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.elastic_pool_id">
<code class="sig-name descname">elastic_pool_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.elastic_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the elastic pool containing this database. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.extended_auditing_policy">
<code class="sig-name descname">extended_auditing_policy</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.extended_auditing_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">extended_auditing_policy</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the number of days to retain logs for in the storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the access key to use for the auditing storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountAccessKeyIsSecondary</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether <code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> value is the storage’s secondary key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.license_type">
<code class="sig-name descname">license_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the license type applied to this database. Possible values are <code class="docutils literal notranslate"><span class="pre">LicenseIncluded</span></code> and <code class="docutils literal notranslate"><span class="pre">BasePrice</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.max_size_gb">
<code class="sig-name descname">max_size_gb</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.max_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The max size of the database in gigabytes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.min_capacity">
<code class="sig-name descname">min_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.min_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimal capacity that database will always have allocated, if not paused. This property is only settable for General Purpose Serverless databases.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Ms SQL Database. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.read_replica_count">
<code class="sig-name descname">read_replica_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.read_replica_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of readonly secondary replicas associated with the database to which readonly application intent connections may be routed. This property is only settable for Hyperscale edition databases.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.read_scale">
<code class="sig-name descname">read_scale</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.read_scale" title="Permalink to this definition">¶</a></dt>
<dd><p>If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.restore_point_in_time">
<code class="sig-name descname">restore_point_in_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.restore_point_in_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. This property is only settable for <code class="docutils literal notranslate"><span class="pre">create_mode</span></code>= <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code>  databases.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.sample_name">
<code class="sig-name descname">sample_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.sample_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the sample schema to apply when creating this database. Possible value is <code class="docutils literal notranslate"><span class="pre">AdventureWorksLT</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.server_id">
<code class="sig-name descname">server_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the Ms SQL Server on which to create the database. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.sku_name">
<code class="sig-name descname">sku_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the sku used by the database. Changing this forces a new resource to be created. For example, <code class="docutils literal notranslate"><span class="pre">GP_S_Gen5_2</span></code>,<code class="docutils literal notranslate"><span class="pre">HS_Gen4_1</span></code>,<code class="docutils literal notranslate"><span class="pre">BC_Gen5_2</span></code>, <code class="docutils literal notranslate"><span class="pre">ElasticPool</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code>,<code class="docutils literal notranslate"><span class="pre">S0</span></code>, <code class="docutils literal notranslate"><span class="pre">P2</span></code> ,<code class="docutils literal notranslate"><span class="pre">DW100c</span></code>, <code class="docutils literal notranslate"><span class="pre">DS100</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.threat_detection_policy">
<code class="sig-name descname">threat_detection_policy</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.threat_detection_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Threat detection policy configuration. The <code class="docutils literal notranslate"><span class="pre">threat_detection_policy</span></code> block supports fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disabled_alerts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies a list of alerts which should be disabled. Possible values include <code class="docutils literal notranslate"><span class="pre">Access_Anomaly</span></code>, <code class="docutils literal notranslate"><span class="pre">Sql_Injection</span></code> and <code class="docutils literal notranslate"><span class="pre">Sql_Injection_Vulnerability</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email_account_admins</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Should the account administrators be emailed when this alert is triggered?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of email addresses which alerts should be sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the number of days to keep in the Threat Detection audit logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The State of the Policy. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Disabled</span></code> or <code class="docutils literal notranslate"><span class="pre">New</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the identifier key of the Threat Detection audit storage account. Required if <code class="docutils literal notranslate"><span class="pre">state</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>). This blob storage will hold all Threat Detection audit logs. Required if <code class="docutils literal notranslate"><span class="pre">state</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useServerDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Should the default server policy be used? Defaults to <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Database.zone_redundant">
<code class="sig-name descname">zone_redundant</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Database.zone_redundant" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones. This property is only settable for Premium and Business Critical databases.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.mssql.Database.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_pause_delay_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">collation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_source_database_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_auditing_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_replica_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_scale</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restore_point_in_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sample_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threat_detection_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_redundant</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_pause_delay_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time in minutes after which database is automatically paused. A value of <code class="docutils literal notranslate"><span class="pre">-1</span></code> means that automatic pause is disabled. This property is only settable for General Purpose Serverless databases.</p></li>
<li><p><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the collation of the database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>create_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The create mode of the database. Possible values are <code class="docutils literal notranslate"><span class="pre">Copy</span></code>, <code class="docutils literal notranslate"><span class="pre">Default</span></code>, <code class="docutils literal notranslate"><span class="pre">OnlineSecondary</span></code>, <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code>, <code class="docutils literal notranslate"><span class="pre">Restore</span></code>, <code class="docutils literal notranslate"><span class="pre">RestoreExternalBackup</span></code>, <code class="docutils literal notranslate"><span class="pre">RestoreExternalBackupSecondary</span></code>, <code class="docutils literal notranslate"><span class="pre">RestoreLongTermRetentionBackup</span></code> and <code class="docutils literal notranslate"><span class="pre">Secondary</span></code>.</p></li>
<li><p><strong>creation_source_database_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the source database to be referred to create the new database. This should only be used for databases with <code class="docutils literal notranslate"><span class="pre">create_mode</span></code> values that use another database as reference. Changing this forces a new resource to be created.</p></li>
<li><p><strong>elastic_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the elastic pool containing this database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>extended_auditing_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">extended_auditing_policy</span></code> block as defined below.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the license type applied to this database. Possible values are <code class="docutils literal notranslate"><span class="pre">LicenseIncluded</span></code> and <code class="docutils literal notranslate"><span class="pre">BasePrice</span></code>.</p></li>
<li><p><strong>max_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max size of the database in gigabytes.</p></li>
<li><p><strong>min_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimal capacity that database will always have allocated, if not paused. This property is only settable for General Purpose Serverless databases.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Ms SQL Database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>read_replica_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of readonly secondary replicas associated with the database to which readonly application intent connections may be routed. This property is only settable for Hyperscale edition databases.</p></li>
<li><p><strong>read_scale</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.</p></li>
<li><p><strong>restore_point_in_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. This property is only settable for <code class="docutils literal notranslate"><span class="pre">create_mode</span></code>= <code class="docutils literal notranslate"><span class="pre">PointInTimeRestore</span></code>  databases.</p></li>
<li><p><strong>sample_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the sample schema to apply when creating this database. Possible value is <code class="docutils literal notranslate"><span class="pre">AdventureWorksLT</span></code>.</p></li>
<li><p><strong>server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the Ms SQL Server on which to create the database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the sku used by the database. Changing this forces a new resource to be created. For example, <code class="docutils literal notranslate"><span class="pre">GP_S_Gen5_2</span></code>,<code class="docutils literal notranslate"><span class="pre">HS_Gen4_1</span></code>,<code class="docutils literal notranslate"><span class="pre">BC_Gen5_2</span></code>, <code class="docutils literal notranslate"><span class="pre">ElasticPool</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code>,<code class="docutils literal notranslate"><span class="pre">S0</span></code>, <code class="docutils literal notranslate"><span class="pre">P2</span></code> ,<code class="docutils literal notranslate"><span class="pre">DW100c</span></code>, <code class="docutils literal notranslate"><span class="pre">DS100</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>threat_detection_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Threat detection policy configuration. The <code class="docutils literal notranslate"><span class="pre">threat_detection_policy</span></code> block supports fields documented below.</p></li>
<li><p><strong>zone_redundant</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones. This property is only settable for Premium and Business Critical databases.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>extended_auditing_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of days to retain logs for in the storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the access key to use for the auditing storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountAccessKeyIsSecondary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether <code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> value is the storage’s secondary key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>).</p></li>
</ul>
<p>The <strong>threat_detection_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disabled_alerts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of alerts which should be disabled. Possible values include <code class="docutils literal notranslate"><span class="pre">Access_Anomaly</span></code>, <code class="docutils literal notranslate"><span class="pre">Sql_Injection</span></code> and <code class="docutils literal notranslate"><span class="pre">Sql_Injection_Vulnerability</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email_account_admins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Should the account administrators be emailed when this alert is triggered?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of email addresses which alerts should be sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retention_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of days to keep in the Threat Detection audit logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The State of the Policy. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Disabled</span></code> or <code class="docutils literal notranslate"><span class="pre">New</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identifier key of the Threat Detection audit storage account. Required if <code class="docutils literal notranslate"><span class="pre">state</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>). This blob storage will hold all Threat Detection audit logs. Required if <code class="docutils literal notranslate"><span class="pre">state</span></code> is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useServerDefault</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Should the default server policy be used? Defaults to <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.mssql.Database.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mssql.Database.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">DatabaseVulnerabilityAssessmentRuleBaseline</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">baseline_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">baseline_results</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_vulnerability_assessment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Database Vulnerability Assessment Rule Baseline.</p>
<blockquote>
<div><p><strong>NOTE</strong> Database Vulnerability Assessment is currently only available for MS SQL databases.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West US&quot;</span><span class="p">)</span>
<span class="n">example_sql_server</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">sql</span><span class="o">.</span><span class="n">SqlServer</span><span class="p">(</span><span class="s2">&quot;exampleSqlServer&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">&quot;12.0&quot;</span><span class="p">,</span>
    <span class="n">administrator_login</span><span class="o">=</span><span class="s2">&quot;4dm1n157r470r&quot;</span><span class="p">,</span>
    <span class="n">administrator_login_password</span><span class="o">=</span><span class="s2">&quot;4-v3ry-53cr37-p455w0rd&quot;</span><span class="p">)</span>
<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;exampleAccount&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">account_tier</span><span class="o">=</span><span class="s2">&quot;Standard&quot;</span><span class="p">,</span>
    <span class="n">account_replication_type</span><span class="o">=</span><span class="s2">&quot;GRS&quot;</span><span class="p">)</span>
<span class="n">example_container</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Container</span><span class="p">(</span><span class="s2">&quot;exampleContainer&quot;</span><span class="p">,</span>
    <span class="n">storage_account_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">container_access_type</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">)</span>
<span class="n">example_server_security_alert_policy</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">mssql</span><span class="o">.</span><span class="n">ServerSecurityAlertPolicy</span><span class="p">(</span><span class="s2">&quot;exampleServerSecurityAlertPolicy&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">server_name</span><span class="o">=</span><span class="n">example_sql_server</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">state</span><span class="o">=</span><span class="s2">&quot;Enabled&quot;</span><span class="p">)</span>
<span class="n">example_database</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">sql</span><span class="o">.</span><span class="n">Database</span><span class="p">(</span><span class="s2">&quot;exampleDatabase&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">server_name</span><span class="o">=</span><span class="n">example_sql_server</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">edition</span><span class="o">=</span><span class="s2">&quot;Standard&quot;</span><span class="p">)</span>
<span class="n">example_server_vulnerability_assessment</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">mssql</span><span class="o">.</span><span class="n">ServerVulnerabilityAssessment</span><span class="p">(</span><span class="s2">&quot;exampleServerVulnerabilityAssessment&quot;</span><span class="p">,</span>
    <span class="n">server_security_alert_policy_id</span><span class="o">=</span><span class="n">example_server_security_alert_policy</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">storage_container_path</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">Output</span><span class="o">.</span><span class="n">all</span><span class="p">(</span><span class="n">example_account</span><span class="o">.</span><span class="n">primary_blob_endpoint</span><span class="p">,</span> <span class="n">example_container</span><span class="o">.</span><span class="n">name</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">primary_blob_endpoint</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">primary_blob_endpoint</span><span class="si">}{</span><span class="n">name</span><span class="si">}</span><span class="s2">/&quot;</span><span class="p">),</span>
    <span class="n">storage_account_access_key</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">primary_access_key</span><span class="p">)</span>
<span class="n">example_database_vulnerability_assessment_rule_baseline</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">mssql</span><span class="o">.</span><span class="n">DatabaseVulnerabilityAssessmentRuleBaseline</span><span class="p">(</span><span class="s2">&quot;exampleDatabaseVulnerabilityAssessmentRuleBaseline&quot;</span><span class="p">,</span>
    <span class="n">server_vulnerability_assessment_id</span><span class="o">=</span><span class="n">example_server_vulnerability_assessment</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">database_name</span><span class="o">=</span><span class="n">example_database</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">rule_id</span><span class="o">=</span><span class="s2">&quot;VA2065&quot;</span><span class="p">,</span>
    <span class="n">baseline_name</span><span class="o">=</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
    <span class="n">baseline_result</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;results&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="s2">&quot;allowedip1&quot;</span><span class="p">,</span>
                <span class="s2">&quot;123.123.123.123&quot;</span><span class="p">,</span>
                <span class="s2">&quot;123.123.123.123&quot;</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;results&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="s2">&quot;allowedip2&quot;</span><span class="p">,</span>
                <span class="s2">&quot;255.255.255.255&quot;</span><span class="p">,</span>
                <span class="s2">&quot;255.255.255.255&quot;</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">},</span>
    <span class="p">])</span>
</pre></div>
</div>
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
<li><p><code class="docutils literal notranslate"><span class="pre">results</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list representing a result of the baseline.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.baseline_name">
<code class="sig-name descname">baseline_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.baseline_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the vulnerability assessment rule baseline. Valid options are <code class="docutils literal notranslate"><span class="pre">default</span></code> and <code class="docutils literal notranslate"><span class="pre">master</span></code>. <code class="docutils literal notranslate"><span class="pre">default</span></code> implies a baseline on a database level rule and <code class="docutils literal notranslate"><span class="pre">master</span></code> for server level rule. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.baseline_results">
<code class="sig-name descname">baseline_results</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.baseline_results" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">baseline_result</span></code> block as documented below. Multiple blocks can be defined.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">results</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list representing a result of the baseline.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.database_name">
<code class="sig-name descname">database_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MS SQL Database. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.rule_id">
<code class="sig-name descname">rule_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The vulnerability assessment rule ID. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.server_vulnerability_assessment_id">
<code class="sig-name descname">server_vulnerability_assessment_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.server_vulnerability_assessment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Vulnerability Assessment ID of the MS SQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">baseline_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">baseline_results</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_vulnerability_assessment_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><code class="docutils literal notranslate"><span class="pre">results</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list representing a result of the baseline.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.DatabaseVulnerabilityAssessmentRuleBaseline.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azure.mssql.ElasticPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">ElasticPool</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size_bytes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">per_database_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_redundant</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to manage an Azure SQL Elastic Pool via the <code class="docutils literal notranslate"><span class="pre">v3.0</span></code> API which allows for <code class="docutils literal notranslate"><span class="pre">vCore</span></code> and <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based configurations.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;westeurope&quot;</span><span class="p">)</span>
<span class="n">example_sql_server</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">sql</span><span class="o">.</span><span class="n">SqlServer</span><span class="p">(</span><span class="s2">&quot;exampleSqlServer&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">&quot;12.0&quot;</span><span class="p">,</span>
    <span class="n">administrator_login</span><span class="o">=</span><span class="s2">&quot;4dm1n157r470r&quot;</span><span class="p">,</span>
    <span class="n">administrator_login_password</span><span class="o">=</span><span class="s2">&quot;4-v3ry-53cr37-p455w0rd&quot;</span><span class="p">)</span>
<span class="n">example_elastic_pool</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">mssql</span><span class="o">.</span><span class="n">ElasticPool</span><span class="p">(</span><span class="s2">&quot;exampleElasticPool&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">server_name</span><span class="o">=</span><span class="n">example_sql_server</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">license_type</span><span class="o">=</span><span class="s2">&quot;LicenseIncluded&quot;</span><span class="p">,</span>
    <span class="n">max_size_gb</span><span class="o">=</span><span class="mi">756</span><span class="p">,</span>
    <span class="n">sku</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;GP_Gen5&quot;</span><span class="p">,</span>
        <span class="s2">&quot;tier&quot;</span><span class="p">:</span> <span class="s2">&quot;GeneralPurpose&quot;</span><span class="p">,</span>
        <span class="s2">&quot;family&quot;</span><span class="p">:</span> <span class="s2">&quot;Gen5&quot;</span><span class="p">,</span>
        <span class="s2">&quot;capacity&quot;</span><span class="p">:</span> <span class="mi">4</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">per_database_settings</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;min_capacity&quot;</span><span class="p">:</span> <span class="mf">0.25</span><span class="p">,</span>
        <span class="s2">&quot;maxCapacity&quot;</span><span class="p">:</span> <span class="mi">4</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the license type applied to this database. Possible values are <code class="docutils literal notranslate"><span class="pre">LicenseIncluded</span></code> and <code class="docutils literal notranslate"><span class="pre">BasePrice</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_size_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max data size of the elastic pool in bytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_gb</span></code>.</p></li>
<li><p><strong>max_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max data size of the elastic pool in gigabytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_bytes</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">min_capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum capacity all databases are guaranteed.</p></li>
</ul>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The scale up/out capacity, representing server’s compute units. For more information see the documentation for your Elasticpool configuration: <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-elastic-pools">vCore-based</a> or <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-elastic-pools">DTU-based</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">family</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">family</span></code> of hardware <code class="docutils literal notranslate"><span class="pre">Gen4</span></code> or <code class="docutils literal notranslate"><span class="pre">Gen5</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the SKU Name for this Elasticpool. The name of the SKU, will be either <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> pattern (e.g. GP_Gen4, BC_Gen5) or the <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based <code class="docutils literal notranslate"><span class="pre">BasicPool</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardPool</span></code>, or <code class="docutils literal notranslate"><span class="pre">PremiumPool</span></code> pattern.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tier of the particular SKU. Possible values are <code class="docutils literal notranslate"><span class="pre">GeneralPurpose</span></code>, <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. For more information see the documentation for your Elasticpool configuration: <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-elastic-pools">vCore-based</a> or <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-elastic-pools">DTU-based</a>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.mssql.ElasticPool.license_type">
<code class="sig-name descname">license_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the license type applied to this database. Possible values are <code class="docutils literal notranslate"><span class="pre">LicenseIncluded</span></code> and <code class="docutils literal notranslate"><span class="pre">BasePrice</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ElasticPool.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ElasticPool.max_size_bytes">
<code class="sig-name descname">max_size_bytes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.max_size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The max data size of the elastic pool in bytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_gb</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ElasticPool.max_size_gb">
<code class="sig-name descname">max_size_gb</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.max_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The max data size of the elastic pool in gigabytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_bytes</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ElasticPool.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ElasticPool.per_database_settings">
<code class="sig-name descname">per_database_settings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.per_database_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">per_database_settings</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum capacity any one database can consume.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum capacity all databases are guaranteed.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ElasticPool.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the elastic pool. This must be the same as the resource group of the underlying SQL server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ElasticPool.server_name">
<code class="sig-name descname">server_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server on which to create the elastic pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ElasticPool.sku">
<code class="sig-name descname">sku</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The scale up/out capacity, representing server’s compute units. For more information see the documentation for your Elasticpool configuration: <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-elastic-pools">vCore-based</a> or <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-elastic-pools">DTU-based</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">family</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The <code class="docutils literal notranslate"><span class="pre">family</span></code> of hardware <code class="docutils literal notranslate"><span class="pre">Gen4</span></code> or <code class="docutils literal notranslate"><span class="pre">Gen5</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the SKU Name for this Elasticpool. The name of the SKU, will be either <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> pattern (e.g. GP_Gen4, BC_Gen5) or the <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based <code class="docutils literal notranslate"><span class="pre">BasicPool</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardPool</span></code>, or <code class="docutils literal notranslate"><span class="pre">PremiumPool</span></code> pattern.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tier of the particular SKU. Possible values are <code class="docutils literal notranslate"><span class="pre">GeneralPurpose</span></code>, <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. For more information see the documentation for your Elasticpool configuration: <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-elastic-pools">vCore-based</a> or <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-elastic-pools">DTU-based</a>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ElasticPool.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ElasticPool.zone_redundant">
<code class="sig-name descname">zone_redundant</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.zone_redundant" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this elastic pool is zone redundant. <code class="docutils literal notranslate"><span class="pre">tier</span></code> needs to be <code class="docutils literal notranslate"><span class="pre">Premium</span></code> for <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based  or <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code> for <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">sku</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.mssql.ElasticPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size_bytes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">per_database_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_redundant</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ElasticPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the license type applied to this database. Possible values are <code class="docutils literal notranslate"><span class="pre">LicenseIncluded</span></code> and <code class="docutils literal notranslate"><span class="pre">BasePrice</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_size_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max data size of the elastic pool in bytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_gb</span></code>.</p></li>
<li><p><strong>max_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max data size of the elastic pool in gigabytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">max_size_bytes</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the elastic pool. This needs to be globally unique. Changing this forces a new resource to be created.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">min_capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum capacity all databases are guaranteed.</p></li>
</ul>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The scale up/out capacity, representing server’s compute units. For more information see the documentation for your Elasticpool configuration: <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-elastic-pools">vCore-based</a> or <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-elastic-pools">DTU-based</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">family</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The <code class="docutils literal notranslate"><span class="pre">family</span></code> of hardware <code class="docutils literal notranslate"><span class="pre">Gen4</span></code> or <code class="docutils literal notranslate"><span class="pre">Gen5</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the SKU Name for this Elasticpool. The name of the SKU, will be either <code class="docutils literal notranslate"><span class="pre">vCore</span></code> based <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> pattern (e.g. GP_Gen4, BC_Gen5) or the <code class="docutils literal notranslate"><span class="pre">DTU</span></code> based <code class="docutils literal notranslate"><span class="pre">BasicPool</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardPool</span></code>, or <code class="docutils literal notranslate"><span class="pre">PremiumPool</span></code> pattern.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tier of the particular SKU. Possible values are <code class="docutils literal notranslate"><span class="pre">GeneralPurpose</span></code>, <code class="docutils literal notranslate"><span class="pre">BusinessCritical</span></code>, <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. For more information see the documentation for your Elasticpool configuration: <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-elastic-pools">vCore-based</a> or <a class="reference external" href="https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-elastic-pools">DTU-based</a>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.mssql.ElasticPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mssql.ElasticPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ElasticPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azure.mssql.GetDatabaseResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">GetDatabaseResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">collation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elastic_pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_replica_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_scale</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_redundant</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.GetDatabaseResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDatabase.</p>
<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetDatabaseResult.collation">
<code class="sig-name descname">collation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetDatabaseResult.collation" title="Permalink to this definition">¶</a></dt>
<dd><p>The collation of the database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetDatabaseResult.elastic_pool_id">
<code class="sig-name descname">elastic_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetDatabaseResult.elastic_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the elastic pool containing this database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetDatabaseResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetDatabaseResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetDatabaseResult.license_type">
<code class="sig-name descname">license_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetDatabaseResult.license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The license type to apply for this database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetDatabaseResult.max_size_gb">
<code class="sig-name descname">max_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetDatabaseResult.max_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The max size of the database in gigabytes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetDatabaseResult.read_replica_count">
<code class="sig-name descname">read_replica_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetDatabaseResult.read_replica_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of readonly secondary replicas associated with the database to which readonly application intent connections may be routed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetDatabaseResult.read_scale">
<code class="sig-name descname">read_scale</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetDatabaseResult.read_scale" title="Permalink to this definition">¶</a></dt>
<dd><p>If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetDatabaseResult.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetDatabaseResult.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the sku of the database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetDatabaseResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetDatabaseResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetDatabaseResult.zone_redundant">
<code class="sig-name descname">zone_redundant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetDatabaseResult.zone_redundant" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.mssql.GetElasticPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">GetElasticPoolResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size_bytes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">per_db_max_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">per_db_min_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_redundant</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getElasticPool.</p>
<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.license_type">
<code class="sig-name descname">license_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The license type to apply for this database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.max_size_bytes">
<code class="sig-name descname">max_size_bytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.max_size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>The max data size of the elastic pool in bytes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.max_size_gb">
<code class="sig-name descname">max_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.max_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The max data size of the elastic pool in gigabytes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.per_db_max_capacity">
<code class="sig-name descname">per_db_max_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.per_db_max_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum capacity any one database can consume.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.per_db_min_capacity">
<code class="sig-name descname">per_db_min_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.per_db_min_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum capacity all databases are guaranteed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.GetElasticPoolResult.zone_redundant">
<code class="sig-name descname">zone_redundant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.GetElasticPoolResult.zone_redundant" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this elastic pool is zone redundant.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.mssql.Server">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">Server</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">administrator_login</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">administrator_login_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azuread_administrator</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_auditing_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_network_access_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.Server" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Microsoft SQL Azure Database Server.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the administrator login and password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West US&quot;</span><span class="p">)</span>
<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;exampleAccount&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">account_tier</span><span class="o">=</span><span class="s2">&quot;Standard&quot;</span><span class="p">,</span>
    <span class="n">account_replication_type</span><span class="o">=</span><span class="s2">&quot;LRS&quot;</span><span class="p">)</span>
<span class="n">example_server</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">mssql</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;exampleServer&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">&quot;12.0&quot;</span><span class="p">,</span>
    <span class="n">administrator_login</span><span class="o">=</span><span class="s2">&quot;missadministrator&quot;</span><span class="p">,</span>
    <span class="n">administrator_login_password</span><span class="o">=</span><span class="s2">&quot;thisIsKat11&quot;</span><span class="p">,</span>
    <span class="n">azuread_administrator</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;loginUsername&quot;</span><span class="p">:</span> <span class="s2">&quot;AzureAD Admin&quot;</span><span class="p">,</span>
        <span class="s2">&quot;object_id&quot;</span><span class="p">:</span> <span class="s2">&quot;00000000-0000-0000-0000-000000000000&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">extended_auditing_policy</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;storage_endpoint&quot;</span><span class="p">:</span> <span class="n">example_account</span><span class="o">.</span><span class="n">primary_blob_endpoint</span><span class="p">,</span>
        <span class="s2">&quot;storage_account_access_key&quot;</span><span class="p">:</span> <span class="n">example_account</span><span class="o">.</span><span class="n">primary_access_key</span><span class="p">,</span>
        <span class="s2">&quot;storageAccountAccessKeyIsSecondary&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;retention_in_days&quot;</span><span class="p">:</span> <span class="mi">6</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;environment&quot;</span><span class="p">:</span> <span class="s2">&quot;production&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>administrator_login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The administrator login name for the new server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>administrator_login_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> user. Needs to comply with Azure’s <a class="reference external" href="https://msdn.microsoft.com/library/ms161959.aspx">Password Policy</a></p></li>
<li><p><strong>azuread_administrator</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">azuread_administrator</span></code> block as defined below.</p></li>
<li><p><strong>connection_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection policy the server will use. Possible values are <code class="docutils literal notranslate"><span class="pre">Default</span></code>, <code class="docutils literal notranslate"><span class="pre">Proxy</span></code>, and <code class="docutils literal notranslate"><span class="pre">Redirect</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Default</span></code>.</p></li>
<li><p><strong>extended_auditing_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">extended_auditing_policy</span></code> block as defined below.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Microsoft SQL Server. This needs to be globally unique within Azure.</p></li>
<li><p><strong>public_network_access_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not public network access is allowed for this server. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Microsoft SQL Server.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>azuread_administrator</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">loginUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (Required)  The login username of the Azure AD Administrator of this SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">object_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (Required) The object id of the Azure AD Administrator of this SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (Optional) The tenant id of the Azure AD Administrator of this SQL Server.</p></li>
</ul>
<p>The <strong>extended_auditing_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - (Optional) Specifies the number of days to retain logs for in the storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (Required)  Specifies the access key to use for the auditing storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountAccessKeyIsSecondary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - (Optional) Specifies whether <code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> value is the storage’s secondary key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (Required) Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>).</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID for the Service Principal associated with the Identity of this SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (Optional) The tenant id of the Azure AD Administrator of this SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identity type of the Microsoft SQL Server. At this time the only allowed value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.mssql.Server.administrator_login">
<code class="sig-name descname">administrator_login</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Server.administrator_login" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrator login name for the new server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Server.administrator_login_password">
<code class="sig-name descname">administrator_login_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Server.administrator_login_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> user. Needs to comply with Azure’s <a class="reference external" href="https://msdn.microsoft.com/library/ms161959.aspx">Password Policy</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Server.azuread_administrator">
<code class="sig-name descname">azuread_administrator</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Server.azuread_administrator" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">azuread_administrator</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">loginUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - (Required)  The login username of the Azure AD Administrator of this SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">object_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - (Required) The object id of the Azure AD Administrator of this SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - (Optional) The tenant id of the Azure AD Administrator of this SQL Server.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Server.connection_policy">
<code class="sig-name descname">connection_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Server.connection_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection policy the server will use. Possible values are <code class="docutils literal notranslate"><span class="pre">Default</span></code>, <code class="docutils literal notranslate"><span class="pre">Proxy</span></code>, and <code class="docutils literal notranslate"><span class="pre">Redirect</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Default</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Server.extended_auditing_policy">
<code class="sig-name descname">extended_auditing_policy</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Server.extended_auditing_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">extended_auditing_policy</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - (Optional) Specifies the number of days to retain logs for in the storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - (Required)  Specifies the access key to use for the auditing storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountAccessKeyIsSecondary</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - (Optional) Specifies whether <code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> value is the storage’s secondary key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - (Required) Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Server.fully_qualified_domain_name">
<code class="sig-name descname">fully_qualified_domain_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Server.fully_qualified_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified domain name of the Azure SQL Server (e.g. myServerName.database.windows.net)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Server.identity">
<code class="sig-name descname">identity</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Server.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Principal ID for the Service Principal associated with the Identity of this SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - (Optional) The tenant id of the Azure AD Administrator of this SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the identity type of the Microsoft SQL Server. At this time the only allowed value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Server.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Server.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Server.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Server.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Microsoft SQL Server. This needs to be globally unique within Azure.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Server.public_network_access_enabled">
<code class="sig-name descname">public_network_access_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Server.public_network_access_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not public network access is allowed for this server. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Server.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Server.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Microsoft SQL Server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Server.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Server.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.Server.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.Server.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.mssql.Server.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">administrator_login</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">administrator_login_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azuread_administrator</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_auditing_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fully_qualified_domain_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_network_access_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.Server.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Server resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>administrator_login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The administrator login name for the new server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>administrator_login_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> user. Needs to comply with Azure’s <a class="reference external" href="https://msdn.microsoft.com/library/ms161959.aspx">Password Policy</a></p>
</p></li>
<li><p><strong>azuread_administrator</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">azuread_administrator</span></code> block as defined below.</p></li>
<li><p><strong>connection_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connection policy the server will use. Possible values are <code class="docutils literal notranslate"><span class="pre">Default</span></code>, <code class="docutils literal notranslate"><span class="pre">Proxy</span></code>, and <code class="docutils literal notranslate"><span class="pre">Redirect</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Default</span></code>.</p></li>
<li><p><strong>extended_auditing_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">extended_auditing_policy</span></code> block as defined below.</p></li>
<li><p><strong>fully_qualified_domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully qualified domain name of the Azure SQL Server (e.g. myServerName.database.windows.net)</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Microsoft SQL Server. This needs to be globally unique within Azure.</p></li>
<li><p><strong>public_network_access_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not public network access is allowed for this server. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Microsoft SQL Server.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version for the new server. Valid values are: 2.0 (for v11 server) and 12.0 (for v12 server).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>azuread_administrator</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">loginUsername</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (Required)  The login username of the Azure AD Administrator of this SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">object_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (Required) The object id of the Azure AD Administrator of this SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (Optional) The tenant id of the Azure AD Administrator of this SQL Server.</p></li>
</ul>
<p>The <strong>extended_auditing_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">retention_in_days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - (Optional) Specifies the number of days to retain logs for in the storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (Required)  Specifies the access key to use for the auditing storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountAccessKeyIsSecondary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - (Optional) Specifies whether <code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> value is the storage’s secondary key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (Required) Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>).</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID for the Service Principal associated with the Identity of this SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - (Optional) The tenant id of the Azure AD Administrator of this SQL Server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identity type of the Microsoft SQL Server. At this time the only allowed value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.mssql.Server.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.Server.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mssql.Server.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.Server.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">ServerSecurityAlertPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled_alerts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_account_admins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_account_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Security Alert Policy for a MSSQL Server.</p>
<blockquote>
<div><p><strong>NOTE</strong> Security Alert Policy is currently only available for MS SQL databases.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West US&quot;</span><span class="p">)</span>
<span class="n">example_sql_server</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">sql</span><span class="o">.</span><span class="n">SqlServer</span><span class="p">(</span><span class="s2">&quot;exampleSqlServer&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">&quot;12.0&quot;</span><span class="p">,</span>
    <span class="n">administrator_login</span><span class="o">=</span><span class="s2">&quot;4dm1n157r470r&quot;</span><span class="p">,</span>
    <span class="n">administrator_login_password</span><span class="o">=</span><span class="s2">&quot;4-v3ry-53cr37-p455w0rd&quot;</span><span class="p">)</span>
<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;exampleAccount&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">account_tier</span><span class="o">=</span><span class="s2">&quot;Standard&quot;</span><span class="p">,</span>
    <span class="n">account_replication_type</span><span class="o">=</span><span class="s2">&quot;GRS&quot;</span><span class="p">)</span>
<span class="n">example_server_security_alert_policy</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">mssql</span><span class="o">.</span><span class="n">ServerSecurityAlertPolicy</span><span class="p">(</span><span class="s2">&quot;exampleServerSecurityAlertPolicy&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">server_name</span><span class="o">=</span><span class="n">example_sql_server</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">state</span><span class="o">=</span><span class="s2">&quot;Enabled&quot;</span><span class="p">,</span>
    <span class="n">storage_endpoint</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">primary_blob_endpoint</span><span class="p">,</span>
    <span class="n">storage_account_access_key</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">primary_access_key</span><span class="p">,</span>
    <span class="n">disabled_alerts</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;Sql_Injection&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Data_Exfiltration&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">retention_days</span><span class="o">=</span><span class="mi">20</span><span class="p">)</span>
</pre></div>
</div>
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
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database server. Allowed values are: <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><strong>storage_account_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the identifier key of the Threat Detection audit storage account.</p></li>
<li><p><strong>storage_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>). This blob storage will hold all Threat Detection audit logs.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.disabled_alerts">
<code class="sig-name descname">disabled_alerts</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.disabled_alerts" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an array of alerts that are disabled. Allowed values are: <code class="docutils literal notranslate"><span class="pre">Sql_Injection</span></code>, <code class="docutils literal notranslate"><span class="pre">Sql_Injection_Vulnerability</span></code>, <code class="docutils literal notranslate"><span class="pre">Access_Anomaly</span></code>, <code class="docutils literal notranslate"><span class="pre">Data_Exfiltration</span></code>, <code class="docutils literal notranslate"><span class="pre">Unsafe_Action</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.email_account_admins">
<code class="sig-name descname">email_account_admins</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.email_account_admins" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which specifies if the alert is sent to the account administrators or not. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.email_addresses">
<code class="sig-name descname">email_addresses</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.email_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an array of e-mail addresses to which the alert is sent.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group that contains the MS SQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.retention_days">
<code class="sig-name descname">retention_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.retention_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of days to keep in the Threat Detection audit logs. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.server_name">
<code class="sig-name descname">server_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MS SQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.state">
<code class="sig-name descname">state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database server. Allowed values are: <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.storage_account_access_key">
<code class="sig-name descname">storage_account_access_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.storage_account_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the identifier key of the Threat Detection audit storage account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.storage_endpoint">
<code class="sig-name descname">storage_endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.storage_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>). This blob storage will hold all Threat Detection audit logs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled_alerts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_account_admins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_account_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_endpoint</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database server. Allowed values are: <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><strong>storage_account_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the identifier key of the Threat Detection audit storage account.</p></li>
<li><p><strong>storage_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the blob storage endpoint (e.g. <a class="reference external" href="https://MyAccount.blob.core.windows.net">https://MyAccount.blob.core.windows.net</a>). This blob storage will hold all Threat Detection audit logs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mssql.ServerSecurityAlertPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerSecurityAlertPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">ServerVulnerabilityAssessment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurring_scans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_security_alert_policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_account_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_container_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_container_sas_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the Vulnerability Assessment for a MS SQL Server.</p>
<blockquote>
<div><p><strong>NOTE</strong> Vulnerability Assessment is currently only available for MS SQL databases.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West US&quot;</span><span class="p">)</span>
<span class="n">example_sql_server</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">sql</span><span class="o">.</span><span class="n">SqlServer</span><span class="p">(</span><span class="s2">&quot;exampleSqlServer&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">&quot;12.0&quot;</span><span class="p">,</span>
    <span class="n">administrator_login</span><span class="o">=</span><span class="s2">&quot;4dm1n157r470r&quot;</span><span class="p">,</span>
    <span class="n">administrator_login_password</span><span class="o">=</span><span class="s2">&quot;4-v3ry-53cr37-p455w0rd&quot;</span><span class="p">)</span>
<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;exampleAccount&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">account_tier</span><span class="o">=</span><span class="s2">&quot;Standard&quot;</span><span class="p">,</span>
    <span class="n">account_replication_type</span><span class="o">=</span><span class="s2">&quot;GRS&quot;</span><span class="p">)</span>
<span class="n">example_container</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">storage</span><span class="o">.</span><span class="n">Container</span><span class="p">(</span><span class="s2">&quot;exampleContainer&quot;</span><span class="p">,</span>
    <span class="n">storage_account_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">container_access_type</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">)</span>
<span class="n">example_server_security_alert_policy</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">mssql</span><span class="o">.</span><span class="n">ServerSecurityAlertPolicy</span><span class="p">(</span><span class="s2">&quot;exampleServerSecurityAlertPolicy&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">server_name</span><span class="o">=</span><span class="n">example_sql_server</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">state</span><span class="o">=</span><span class="s2">&quot;Enabled&quot;</span><span class="p">)</span>
<span class="n">example_server_vulnerability_assessment</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">mssql</span><span class="o">.</span><span class="n">ServerVulnerabilityAssessment</span><span class="p">(</span><span class="s2">&quot;exampleServerVulnerabilityAssessment&quot;</span><span class="p">,</span>
    <span class="n">server_security_alert_policy_id</span><span class="o">=</span><span class="n">example_server_security_alert_policy</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">storage_container_path</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">Output</span><span class="o">.</span><span class="n">all</span><span class="p">(</span><span class="n">example_account</span><span class="o">.</span><span class="n">primary_blob_endpoint</span><span class="p">,</span> <span class="n">example_container</span><span class="o">.</span><span class="n">name</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">primary_blob_endpoint</span><span class="p">,</span> <span class="n">name</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">primary_blob_endpoint</span><span class="si">}{</span><span class="n">name</span><span class="si">}</span><span class="s2">/&quot;</span><span class="p">),</span>
    <span class="n">storage_account_access_key</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">primary_access_key</span><span class="p">,</span>
    <span class="n">recurring_scans</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;enabled&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;emailSubscriptionAdmins&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;emails&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;email@example1.com&quot;</span><span class="p">,</span>
            <span class="s2">&quot;email@example2.com&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">})</span>
</pre></div>
</div>
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
<dl class="py attribute">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.recurring_scans">
<code class="sig-name descname">recurring_scans</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.recurring_scans" title="Permalink to this definition">¶</a></dt>
<dd><p>The recurring scans settings. The <code class="docutils literal notranslate"><span class="pre">recurring_scans</span></code> block supports fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">emailSubscriptionAdmins</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean flag which specifies if the schedule scan notification will be sent to the subscription administrators. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emails</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies an array of e-mail addresses to which the scan notification is sent.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean flag which specifies if recurring scans is enabled or disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.server_security_alert_policy_id">
<code class="sig-name descname">server_security_alert_policy_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.server_security_alert_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the security alert policy of the MS SQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.storage_account_access_key">
<code class="sig-name descname">storage_account_access_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.storage_account_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the identifier key of the storage account for vulnerability assessment scan results. If <code class="docutils literal notranslate"><span class="pre">storage_container_sas_key</span></code> isn’t specified, <code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> is required.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.storage_container_path">
<code class="sig-name descname">storage_container_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.storage_container_path" title="Permalink to this definition">¶</a></dt>
<dd><p>A blob storage container path to hold the scan results (e.g. <a class="reference external" href="https://myStorage.blob.core.windows.net/VaScans/">https://myStorage.blob.core.windows.net/VaScans/</a>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.storage_container_sas_key">
<code class="sig-name descname">storage_container_sas_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.storage_container_sas_key" title="Permalink to this definition">¶</a></dt>
<dd><p>A shared access signature (SAS Key) that has write access to the blob container specified in <code class="docutils literal notranslate"><span class="pre">storage_container_path</span></code> parameter. If <code class="docutils literal notranslate"><span class="pre">storage_account_access_key</span></code> isn’t specified, <code class="docutils literal notranslate"><span class="pre">storage_container_sas_key</span></code> is required.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurring_scans</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_security_alert_policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_account_access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_container_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_container_sas_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.get" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mssql.ServerVulnerabilityAssessment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.ServerVulnerabilityAssessment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_azure.mssql.VirtualMachine">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">VirtualMachine</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_patching</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_vault_credential</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">r_services_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_connectivity_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_connectivity_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_connectivity_update_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_connectivity_update_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_machine_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.VirtualMachine" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Microsoft SQL Virtual Machine</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_virtual_machine</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">compute</span><span class="o">.</span><span class="n">get_virtual_machine</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-vm&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;example-resources&quot;</span><span class="p">)</span>
<span class="n">example_mssql_virtual_machine_virtual_machine</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">mssql</span><span class="o">.</span><span class="n">VirtualMachine</span><span class="p">(</span><span class="s2">&quot;exampleMssql/virtualMachineVirtualMachine&quot;</span><span class="p">,</span>
    <span class="n">virtual_machine_id</span><span class="o">=</span><span class="n">example_virtual_machine</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">sql_license_type</span><span class="o">=</span><span class="s2">&quot;PAYG&quot;</span><span class="p">,</span>
    <span class="n">r_services_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">sql_connectivity_port</span><span class="o">=</span><span class="mi">1433</span><span class="p">,</span>
    <span class="n">sql_connectivity_type</span><span class="o">=</span><span class="s2">&quot;PRIVATE&quot;</span><span class="p">,</span>
    <span class="n">sql_connectivity_update_password</span><span class="o">=</span><span class="s2">&quot;Password1234!&quot;</span><span class="p">,</span>
    <span class="n">sql_connectivity_update_username</span><span class="o">=</span><span class="s2">&quot;sqllogin&quot;</span><span class="p">,</span>
    <span class="n">auto_patching</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;dayOfWeek&quot;</span><span class="p">:</span> <span class="s2">&quot;Sunday&quot;</span><span class="p">,</span>
        <span class="s2">&quot;maintenanceWindowDurationInMinutes&quot;</span><span class="p">:</span> <span class="mi">60</span><span class="p">,</span>
        <span class="s2">&quot;maintenanceWindowStartingHour&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_patching</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">auto_patching</span></code> block as defined below.</p></li>
<li><p><strong>key_vault_credential</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – (Optional) An <code class="docutils literal notranslate"><span class="pre">key_vault_credential</span></code> block as defined below.</p></li>
<li><p><strong>r_services_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should R Services be enabled?</p></li>
<li><p><strong>sql_connectivity_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SQL Server port. Defaults to <code class="docutils literal notranslate"><span class="pre">1433</span></code>.</p></li>
<li><p><strong>sql_connectivity_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connectivity type used for this SQL Server. Defaults to <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>.</p></li>
<li><p><strong>sql_connectivity_update_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SQL Server sysadmin login password.</p></li>
<li><p><strong>sql_connectivity_update_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SQL Server sysadmin login to create.</p></li>
<li><p><strong>sql_license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SQL Server license type. Possible values are <code class="docutils literal notranslate"><span class="pre">AHUB</span></code> (Azure Hybrid Benefit) and <code class="docutils literal notranslate"><span class="pre">PAYG</span></code> (Pay-As-You-Go). Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>virtual_machine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Machine. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auto_patching</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dayOfWeek</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The day of week to apply the patch on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maintenanceWindowDurationInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the Maintenance Window in minutes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maintenanceWindowStartingHour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Hour, in the Virtual Machine Time-Zone when the patching maintenance window should begin.</p></li>
</ul>
<p>The <strong>key_vault_credential</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keyVaultUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The azure Key Vault url. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The credential name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicePrincipalName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service principal name to access key vault. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicePrincipalSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service principal name secret to access key vault. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.mssql.VirtualMachine.auto_patching">
<code class="sig-name descname">auto_patching</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.VirtualMachine.auto_patching" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">auto_patching</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dayOfWeek</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The day of week to apply the patch on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maintenanceWindowDurationInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the Maintenance Window in minutes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maintenanceWindowStartingHour</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Hour, in the Virtual Machine Time-Zone when the patching maintenance window should begin.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.VirtualMachine.key_vault_credential">
<code class="sig-name descname">key_vault_credential</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.VirtualMachine.key_vault_credential" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) An <code class="docutils literal notranslate"><span class="pre">key_vault_credential</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keyVaultUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The azure Key Vault url. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The credential name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicePrincipalName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The service principal name to access key vault. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicePrincipalSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The service principal name secret to access key vault. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.VirtualMachine.r_services_enabled">
<code class="sig-name descname">r_services_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.VirtualMachine.r_services_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should R Services be enabled?</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.VirtualMachine.sql_connectivity_port">
<code class="sig-name descname">sql_connectivity_port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.VirtualMachine.sql_connectivity_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The SQL Server port. Defaults to <code class="docutils literal notranslate"><span class="pre">1433</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.VirtualMachine.sql_connectivity_type">
<code class="sig-name descname">sql_connectivity_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.VirtualMachine.sql_connectivity_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The connectivity type used for this SQL Server. Defaults to <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.VirtualMachine.sql_connectivity_update_password">
<code class="sig-name descname">sql_connectivity_update_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.VirtualMachine.sql_connectivity_update_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The SQL Server sysadmin login password.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.VirtualMachine.sql_connectivity_update_username">
<code class="sig-name descname">sql_connectivity_update_username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.VirtualMachine.sql_connectivity_update_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The SQL Server sysadmin login to create.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.VirtualMachine.sql_license_type">
<code class="sig-name descname">sql_license_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.VirtualMachine.sql_license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The SQL Server license type. Possible values are <code class="docutils literal notranslate"><span class="pre">AHUB</span></code> (Azure Hybrid Benefit) and <code class="docutils literal notranslate"><span class="pre">PAYG</span></code> (Pay-As-You-Go). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.VirtualMachine.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.VirtualMachine.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.mssql.VirtualMachine.virtual_machine_id">
<code class="sig-name descname">virtual_machine_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mssql.VirtualMachine.virtual_machine_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.mssql.VirtualMachine.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_patching</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_vault_credential</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">r_services_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_connectivity_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_connectivity_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_connectivity_update_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_connectivity_update_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sql_license_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_machine_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.VirtualMachine.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualMachine resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_patching</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">auto_patching</span></code> block as defined below.</p></li>
<li><p><strong>key_vault_credential</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – (Optional) An <code class="docutils literal notranslate"><span class="pre">key_vault_credential</span></code> block as defined below.</p></li>
<li><p><strong>r_services_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should R Services be enabled?</p></li>
<li><p><strong>sql_connectivity_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The SQL Server port. Defaults to <code class="docutils literal notranslate"><span class="pre">1433</span></code>.</p></li>
<li><p><strong>sql_connectivity_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The connectivity type used for this SQL Server. Defaults to <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>.</p></li>
<li><p><strong>sql_connectivity_update_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SQL Server sysadmin login password.</p></li>
<li><p><strong>sql_connectivity_update_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SQL Server sysadmin login to create.</p></li>
<li><p><strong>sql_license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SQL Server license type. Possible values are <code class="docutils literal notranslate"><span class="pre">AHUB</span></code> (Azure Hybrid Benefit) and <code class="docutils literal notranslate"><span class="pre">PAYG</span></code> (Pay-As-You-Go). Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>virtual_machine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Machine. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auto_patching</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dayOfWeek</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The day of week to apply the patch on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maintenanceWindowDurationInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the Maintenance Window in minutes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maintenanceWindowStartingHour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Hour, in the Virtual Machine Time-Zone when the patching maintenance window should begin.</p></li>
</ul>
<p>The <strong>key_vault_credential</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keyVaultUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The azure Key Vault url. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The credential name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicePrincipalName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service principal name to access key vault. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servicePrincipalSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service principal name secret to access key vault. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.mssql.VirtualMachine.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.VirtualMachine.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mssql.VirtualMachine.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.VirtualMachine.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_azure.mssql.get_database">
<code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">get_database</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.get_database" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing SQL database.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">mssql</span><span class="o">.</span><span class="n">get_database</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-mssql-db&quot;</span><span class="p">,</span>
    <span class="n">server_id</span><span class="o">=</span><span class="s2">&quot;example-mssql-server-id&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;databaseId&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Ms SQL Database.</p></li>
<li><p><strong>server_id</strong> (<em>str</em>) – The id of the Ms SQL Server on which to create the database.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.mssql.get_elastic_pool">
<code class="sig-prename descclassname">pulumi_azure.mssql.</code><code class="sig-name descname">get_elastic_pool</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mssql.get_elastic_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing SQL elastic pool.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">mssql</span><span class="o">.</span><span class="n">get_elastic_pool</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;mssqlelasticpoolname&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;example-resources&quot;</span><span class="p">,</span>
    <span class="n">server_name</span><span class="o">=</span><span class="s2">&quot;example-sql-server&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;elasticpoolId&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the elastic pool.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group which contains the elastic pool.</p></li>
<li><p><strong>server_name</strong> (<em>str</em>) – The name of the SQL Server which contains the elastic pool.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
