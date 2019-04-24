<div class="section" id="module-pulumi_azure.cosmosdb">
<span id="cosmosdb"></span><h1>cosmosdb<a class="headerlink" href="#module-pulumi_azure.cosmosdb" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.cosmosdb.Account">
<em class="property">class </em><code class="descclassname">pulumi_azure.cosmosdb.</code><code class="descname">Account</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>capabilities=None</em>, <em>consistency_policy=None</em>, <em>enable_automatic_failover=None</em>, <em>enable_multiple_write_locations=None</em>, <em>failover_policies=None</em>, <em>geo_locations=None</em>, <em>ip_range_filter=None</em>, <em>is_virtual_network_filter_enabled=None</em>, <em>kind=None</em>, <em>location=None</em>, <em>name=None</em>, <em>offer_type=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>virtual_network_rules=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a CosmosDB (formally DocumentDB) Account.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The capabilities which should be enabled for this Cosmos DB account. Possible values are <code class="docutils literal notranslate"><span class="pre">EnableAggregationPipeline</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableCassandra</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableGremlin</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableTable</span></code>, <code class="docutils literal notranslate"><span class="pre">MongoDBv3.4</span></code>, and <code class="docutils literal notranslate"><span class="pre">mongoEnableDocLevelTTL</span></code>.</li>
<li><strong>consistency_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a <code class="docutils literal notranslate"><span class="pre">consistency_policy</span></code> resource, used to define the consistency policy for this CosmosDB account.</li>
<li><strong>enable_automatic_failover</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable automatic fail over for this Cosmos DB account.</li>
<li><strong>enable_multiple_write_locations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable multi-master support for this Cosmos DB account.</li>
<li><strong>geo_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies a <code class="docutils literal notranslate"><span class="pre">geo_location</span></code> resource, used to define where data should be replicated with the <code class="docutils literal notranslate"><span class="pre">failover_priority</span></code> 0 specifying the primary location.</li>
<li><strong>ip_range_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP’s for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.</li>
<li><strong>is_virtual_network_filter_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables virtual network filtering for this Cosmos DB account.</li>
<li><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Kind of CosmosDB to create - possible values are <code class="docutils literal notranslate"><span class="pre">GlobalDocumentDB</span></code> and <code class="docutils literal notranslate"><span class="pre">MongoDB</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">GlobalDocumentDB</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Azure region to host replicated data.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The capability to enable - Possible values are <code class="docutils literal notranslate"><span class="pre">EnableTable</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableCassandra</span></code>, and <code class="docutils literal notranslate"><span class="pre">EnableGremlin</span></code>.</li>
<li><strong>offer_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>virtual_network_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies a <code class="docutils literal notranslate"><span class="pre">virtual_network_rules</span></code> resource, used to define which subnets are allowed to access this CosmosDB account.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.capabilities">
<code class="descname">capabilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>The capabilities which should be enabled for this Cosmos DB account. Possible values are <code class="docutils literal notranslate"><span class="pre">EnableAggregationPipeline</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableCassandra</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableGremlin</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableTable</span></code>, <code class="docutils literal notranslate"><span class="pre">MongoDBv3.4</span></code>, and <code class="docutils literal notranslate"><span class="pre">mongoEnableDocLevelTTL</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.connection_strings">
<code class="descname">connection_strings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of connection strings available for this CosmosDB account. If the kind is <code class="docutils literal notranslate"><span class="pre">GlobalDocumentDB</span></code>, this will be empty.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.consistency_policy">
<code class="descname">consistency_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.consistency_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a <code class="docutils literal notranslate"><span class="pre">consistency_policy</span></code> resource, used to define the consistency policy for this CosmosDB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.enable_automatic_failover">
<code class="descname">enable_automatic_failover</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.enable_automatic_failover" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable automatic fail over for this Cosmos DB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.enable_multiple_write_locations">
<code class="descname">enable_multiple_write_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.enable_multiple_write_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable multi-master support for this Cosmos DB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint used to connect to the CosmosDB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.geo_locations">
<code class="descname">geo_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.geo_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a <code class="docutils literal notranslate"><span class="pre">geo_location</span></code> resource, used to define where data should be replicated with the <code class="docutils literal notranslate"><span class="pre">failover_priority</span></code> 0 specifying the primary location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.ip_range_filter">
<code class="descname">ip_range_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.ip_range_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP’s for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.is_virtual_network_filter_enabled">
<code class="descname">is_virtual_network_filter_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.is_virtual_network_filter_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables virtual network filtering for this Cosmos DB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.kind">
<code class="descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Kind of CosmosDB to create - possible values are <code class="docutils literal notranslate"><span class="pre">GlobalDocumentDB</span></code> and <code class="docutils literal notranslate"><span class="pre">MongoDB</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">GlobalDocumentDB</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Azure region to host replicated data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The capability to enable - Possible values are <code class="docutils literal notranslate"><span class="pre">EnableTable</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableCassandra</span></code>, and <code class="docutils literal notranslate"><span class="pre">EnableGremlin</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.offer_type">
<code class="descname">offer_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.offer_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.primary_master_key">
<code class="descname">primary_master_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.primary_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary master key for the CosmosDB Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.primary_readonly_master_key">
<code class="descname">primary_readonly_master_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.primary_readonly_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary read-only master Key for the CosmosDB Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.read_endpoints">
<code class="descname">read_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.read_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of read endpoints available for this CosmosDB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.secondary_master_key">
<code class="descname">secondary_master_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.secondary_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary master key for the CosmosDB Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.secondary_readonly_master_key">
<code class="descname">secondary_readonly_master_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.secondary_readonly_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary read-only master key for the CosmosDB Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.virtual_network_rules">
<code class="descname">virtual_network_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.virtual_network_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a <code class="docutils literal notranslate"><span class="pre">virtual_network_rules</span></code> resource, used to define which subnets are allowed to access this CosmosDB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.Account.write_endpoints">
<code class="descname">write_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.write_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of write endpoints available for this CosmosDB account.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.cosmosdb.Account.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.Account.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.cosmosdb.GetAccountResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.cosmosdb.</code><code class="descname">GetAccountResult</code><span class="sig-paren">(</span><em>capabilities=None</em>, <em>consistency_policies=None</em>, <em>enable_automatic_failover=None</em>, <em>enable_multiple_write_locations=None</em>, <em>endpoint=None</em>, <em>geo_locations=None</em>, <em>ip_range_filter=None</em>, <em>is_virtual_network_filter_enabled=None</em>, <em>kind=None</em>, <em>location=None</em>, <em>name=None</em>, <em>offer_type=None</em>, <em>primary_master_key=None</em>, <em>primary_readonly_master_key=None</em>, <em>read_endpoints=None</em>, <em>resource_group_name=None</em>, <em>secondary_master_key=None</em>, <em>secondary_readonly_master_key=None</em>, <em>tags=None</em>, <em>virtual_network_rules=None</em>, <em>write_endpoints=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.capabilities">
<code class="descname">capabilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>Capabilities enabled on this Cosmos DB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.enable_automatic_failover">
<code class="descname">enable_automatic_failover</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.enable_automatic_failover" title="Permalink to this definition">¶</a></dt>
<dd><p>If automatic failover is enabled for this CosmosDB Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.enable_multiple_write_locations">
<code class="descname">enable_multiple_write_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.enable_multiple_write_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>If multi-master is enabled for this Cosmos DB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint used to connect to the CosmosDB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.ip_range_filter">
<code class="descname">ip_range_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.ip_range_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The current IP Filter for this CosmosDB account</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.is_virtual_network_filter_enabled">
<code class="descname">is_virtual_network_filter_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.is_virtual_network_filter_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If virtual network filtering is enabled for this Cosmos DB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.kind">
<code class="descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The Kind of the CosmosDB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Azure region hosting replicated data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.offer_type">
<code class="descname">offer_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.offer_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Offer Type to used by this CosmosDB Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.primary_master_key">
<code class="descname">primary_master_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.primary_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary master key for the CosmosDB Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.primary_readonly_master_key">
<code class="descname">primary_readonly_master_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.primary_readonly_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary read-only master Key for the CosmosDB Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.read_endpoints">
<code class="descname">read_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.read_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of read endpoints available for this CosmosDB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.secondary_master_key">
<code class="descname">secondary_master_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.secondary_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary master key for the CosmosDB Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.secondary_readonly_master_key">
<code class="descname">secondary_readonly_master_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.secondary_readonly_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary read-only master key for the CosmosDB Account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.virtual_network_rules">
<code class="descname">virtual_network_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.virtual_network_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnets that are allowed to access this CosmosDB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.write_endpoints">
<code class="descname">write_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.write_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of write endpoints available for this CosmosDB account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_azure.cosmosdb.get_account">
<code class="descclassname">pulumi_azure.cosmosdb.</code><code class="descname">get_account</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing CosmosDB (formally DocumentDB) Account.</p>
</dd></dl>

</div>
