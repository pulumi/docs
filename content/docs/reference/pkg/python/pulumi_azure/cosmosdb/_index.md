---
title: Module cosmosdb
title_tag: Module cosmosdb | Package pulumi_azure | Python SDK
linktitle: cosmosdb
notitle: true
---

<div class="section" id="cosmosdb">
<h1>cosmosdb<a class="headerlink" href="#cosmosdb" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.cosmosdb"></span><dl class="py class">
<dt id="pulumi_azure.cosmosdb.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cosmosdb.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">capabilities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">consistency_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_automatic_failover</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_multiple_write_locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">geo_locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_virtual_network_filter_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_network_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a CosmosDB (formally DocumentDB) Account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>
<span class="kn">import</span> <span class="nn">pulumi_random</span> <span class="k">as</span> <span class="nn">random</span>

<span class="n">rg</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;rg&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;resource_group_location&quot;</span><span class="p">])</span>
<span class="n">ri</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">RandomInteger</span><span class="p">(</span><span class="s2">&quot;ri&quot;</span><span class="p">,</span>
    <span class="nb">min</span><span class="o">=</span><span class="mi">10000</span><span class="p">,</span>
    <span class="nb">max</span><span class="o">=</span><span class="mi">99999</span><span class="p">)</span>
<span class="n">db</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;db&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">rg</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">rg</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">offer_type</span><span class="o">=</span><span class="s2">&quot;Standard&quot;</span><span class="p">,</span>
    <span class="n">kind</span><span class="o">=</span><span class="s2">&quot;GlobalDocumentDB&quot;</span><span class="p">,</span>
    <span class="n">enable_automatic_failover</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">consistency_policy</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;consistencyLevel&quot;</span><span class="p">:</span> <span class="s2">&quot;BoundedStaleness&quot;</span><span class="p">,</span>
        <span class="s2">&quot;maxIntervalInSeconds&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
        <span class="s2">&quot;maxStalenessPrefix&quot;</span><span class="p">:</span> <span class="mi">200</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">geo_location</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;location&quot;</span><span class="p">:</span> <span class="n">var</span><span class="p">[</span><span class="s2">&quot;failover_location&quot;</span><span class="p">],</span>
            <span class="s2">&quot;failoverPriority&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;prefix&quot;</span><span class="p">:</span> <span class="n">ri</span><span class="o">.</span><span class="n">result</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">result</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;tfex-cosmos-db-</span><span class="si">{</span><span class="n">result</span><span class="si">}</span><span class="s2">-customid&quot;</span><span class="p">),</span>
            <span class="s2">&quot;location&quot;</span><span class="p">:</span> <span class="n">rg</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
            <span class="s2">&quot;failoverPriority&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The capabilities which should be enabled for this Cosmos DB account. Possible values are <code class="docutils literal notranslate"><span class="pre">EnableAggregationPipeline</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableCassandra</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableGremlin</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableTable</span></code>, <code class="docutils literal notranslate"><span class="pre">MongoDBv3.4</span></code>, and <code class="docutils literal notranslate"><span class="pre">mongoEnableDocLevelTTL</span></code>.</p></li>
<li><p><strong>consistency_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a <code class="docutils literal notranslate"><span class="pre">consistency_policy</span></code> resource, used to define the consistency policy for this CosmosDB account.</p></li>
<li><p><strong>enable_automatic_failover</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable automatic fail over for this Cosmos DB account.</p></li>
<li><p><strong>enable_multiple_write_locations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable multi-master support for this Cosmos DB account.</p></li>
<li><p><strong>geo_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies a <code class="docutils literal notranslate"><span class="pre">geo_location</span></code> resource, used to define where data should be replicated with the <code class="docutils literal notranslate"><span class="pre">failover_priority</span></code> 0 specifying the primary location.</p></li>
<li><p><strong>ip_range_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP’s for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.</p></li>
<li><p><strong>is_virtual_network_filter_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables virtual network filtering for this Cosmos DB account.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Kind of CosmosDB to create - possible values are <code class="docutils literal notranslate"><span class="pre">GlobalDocumentDB</span></code> and <code class="docutils literal notranslate"><span class="pre">MongoDB</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">GlobalDocumentDB</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>offer_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>virtual_network_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies a <code class="docutils literal notranslate"><span class="pre">virtual_network_rules</span></code> resource, used to define which subnets are allowed to access this CosmosDB account.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>capabilities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>consistency_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consistencyLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Consistency Level to use for this CosmosDB Account - can be either <code class="docutils literal notranslate"><span class="pre">BoundedStaleness</span></code>, <code class="docutils literal notranslate"><span class="pre">Eventual</span></code>, <code class="docutils literal notranslate"><span class="pre">Session</span></code>, <code class="docutils literal notranslate"><span class="pre">Strong</span></code> or <code class="docutils literal notranslate"><span class="pre">ConsistentPrefix</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIntervalInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - When used with the Bounded Staleness consistency level, this value represents the time amount of staleness (in seconds) tolerated. Accepted range for this value is <code class="docutils literal notranslate"><span class="pre">5</span></code> - <code class="docutils literal notranslate"><span class="pre">86400</span></code> (1 day). Defaults to <code class="docutils literal notranslate"><span class="pre">5</span></code>. Required when <code class="docutils literal notranslate"><span class="pre">consistency_level</span></code> is set to <code class="docutils literal notranslate"><span class="pre">BoundedStaleness</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStalenessPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - When used with the Bounded Staleness consistency level, this value represents the number of stale requests tolerated. Accepted range for this value is <code class="docutils literal notranslate"><span class="pre">10</span></code> – <code class="docutils literal notranslate"><span class="pre">2147483647</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>. Required when <code class="docutils literal notranslate"><span class="pre">consistency_level</span></code> is set to <code class="docutils literal notranslate"><span class="pre">BoundedStaleness</span></code>.</p></li>
</ul>
<p>The <strong>geo_locations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">failoverPriority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The failover priority of the region. A failover priority of <code class="docutils literal notranslate"><span class="pre">0</span></code> indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. Changing this causes the location to be re-provisioned and cannot be changed for the location with failover priority <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the virtual network subnet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure region to host replicated data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The string used to generate the document endpoints for this region. If not specified it defaults to <code class="docutils literal notranslate"><span class="pre">${cosmosdb_account.name}-${location}</span></code>. Changing this causes the location to be deleted and re-provisioned and cannot be changed for the location with failover priority <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
</ul>
<p>The <strong>virtual_network_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the virtual network subnet.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.capabilities">
<code class="sig-name descname">capabilities</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>The capabilities which should be enabled for this Cosmos DB account. Possible values are <code class="docutils literal notranslate"><span class="pre">EnableAggregationPipeline</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableCassandra</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableGremlin</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableTable</span></code>, <code class="docutils literal notranslate"><span class="pre">MongoDBv3.4</span></code>, and <code class="docutils literal notranslate"><span class="pre">mongoEnableDocLevelTTL</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.connection_strings">
<code class="sig-name descname">connection_strings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of connection strings available for this CosmosDB account. If the kind is <code class="docutils literal notranslate"><span class="pre">GlobalDocumentDB</span></code>, this will be empty.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.consistency_policy">
<code class="sig-name descname">consistency_policy</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.consistency_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a <code class="docutils literal notranslate"><span class="pre">consistency_policy</span></code> resource, used to define the consistency policy for this CosmosDB account.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consistencyLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Consistency Level to use for this CosmosDB Account - can be either <code class="docutils literal notranslate"><span class="pre">BoundedStaleness</span></code>, <code class="docutils literal notranslate"><span class="pre">Eventual</span></code>, <code class="docutils literal notranslate"><span class="pre">Session</span></code>, <code class="docutils literal notranslate"><span class="pre">Strong</span></code> or <code class="docutils literal notranslate"><span class="pre">ConsistentPrefix</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIntervalInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - When used with the Bounded Staleness consistency level, this value represents the time amount of staleness (in seconds) tolerated. Accepted range for this value is <code class="docutils literal notranslate"><span class="pre">5</span></code> - <code class="docutils literal notranslate"><span class="pre">86400</span></code> (1 day). Defaults to <code class="docutils literal notranslate"><span class="pre">5</span></code>. Required when <code class="docutils literal notranslate"><span class="pre">consistency_level</span></code> is set to <code class="docutils literal notranslate"><span class="pre">BoundedStaleness</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStalenessPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - When used with the Bounded Staleness consistency level, this value represents the number of stale requests tolerated. Accepted range for this value is <code class="docutils literal notranslate"><span class="pre">10</span></code> – <code class="docutils literal notranslate"><span class="pre">2147483647</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>. Required when <code class="docutils literal notranslate"><span class="pre">consistency_level</span></code> is set to <code class="docutils literal notranslate"><span class="pre">BoundedStaleness</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.enable_automatic_failover">
<code class="sig-name descname">enable_automatic_failover</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.enable_automatic_failover" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable automatic fail over for this Cosmos DB account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.enable_multiple_write_locations">
<code class="sig-name descname">enable_multiple_write_locations</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.enable_multiple_write_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable multi-master support for this Cosmos DB account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.endpoint">
<code class="sig-name descname">endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint used to connect to the CosmosDB account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.geo_locations">
<code class="sig-name descname">geo_locations</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.geo_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a <code class="docutils literal notranslate"><span class="pre">geo_location</span></code> resource, used to define where data should be replicated with the <code class="docutils literal notranslate"><span class="pre">failover_priority</span></code> 0 specifying the primary location.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">failoverPriority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The failover priority of the region. A failover priority of <code class="docutils literal notranslate"><span class="pre">0</span></code> indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. Changing this causes the location to be re-provisioned and cannot be changed for the location with failover priority <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the virtual network subnet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Azure region to host replicated data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The string used to generate the document endpoints for this region. If not specified it defaults to <code class="docutils literal notranslate"><span class="pre">${cosmosdb_account.name}-${location}</span></code>. Changing this causes the location to be deleted and re-provisioned and cannot be changed for the location with failover priority <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.ip_range_filter">
<code class="sig-name descname">ip_range_filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.ip_range_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP’s for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.is_virtual_network_filter_enabled">
<code class="sig-name descname">is_virtual_network_filter_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.is_virtual_network_filter_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables virtual network filtering for this Cosmos DB account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.kind">
<code class="sig-name descname">kind</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Kind of CosmosDB to create - possible values are <code class="docutils literal notranslate"><span class="pre">GlobalDocumentDB</span></code> and <code class="docutils literal notranslate"><span class="pre">MongoDB</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">GlobalDocumentDB</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.offer_type">
<code class="sig-name descname">offer_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.offer_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.primary_master_key">
<code class="sig-name descname">primary_master_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.primary_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary master key for the CosmosDB Account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.primary_readonly_master_key">
<code class="sig-name descname">primary_readonly_master_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.primary_readonly_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary read-only master Key for the CosmosDB Account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.read_endpoints">
<code class="sig-name descname">read_endpoints</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.read_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of read endpoints available for this CosmosDB account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.secondary_master_key">
<code class="sig-name descname">secondary_master_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.secondary_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary master key for the CosmosDB Account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.secondary_readonly_master_key">
<code class="sig-name descname">secondary_readonly_master_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.secondary_readonly_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary read-only master key for the CosmosDB Account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.virtual_network_rules">
<code class="sig-name descname">virtual_network_rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.virtual_network_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a <code class="docutils literal notranslate"><span class="pre">virtual_network_rules</span></code> resource, used to define which subnets are allowed to access this CosmosDB account.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the virtual network subnet.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Account.write_endpoints">
<code class="sig-name descname">write_endpoints</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.write_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of write endpoints available for this CosmosDB account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">capabilities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_strings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">consistency_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_automatic_failover</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_multiple_write_locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">geo_locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_virtual_network_filter_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_master_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_readonly_master_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_endpoints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_master_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_readonly_master_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_network_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">write_endpoints</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The capabilities which should be enabled for this Cosmos DB account. Possible values are <code class="docutils literal notranslate"><span class="pre">EnableAggregationPipeline</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableCassandra</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableGremlin</span></code>, <code class="docutils literal notranslate"><span class="pre">EnableTable</span></code>, <code class="docutils literal notranslate"><span class="pre">MongoDBv3.4</span></code>, and <code class="docutils literal notranslate"><span class="pre">mongoEnableDocLevelTTL</span></code>.</p></li>
<li><p><strong>connection_strings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of connection strings available for this CosmosDB account. If the kind is <code class="docutils literal notranslate"><span class="pre">GlobalDocumentDB</span></code>, this will be empty.</p></li>
<li><p><strong>consistency_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a <code class="docutils literal notranslate"><span class="pre">consistency_policy</span></code> resource, used to define the consistency policy for this CosmosDB account.</p></li>
<li><p><strong>enable_automatic_failover</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable automatic fail over for this Cosmos DB account.</p></li>
<li><p><strong>enable_multiple_write_locations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable multi-master support for this Cosmos DB account.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint used to connect to the CosmosDB account.</p></li>
<li><p><strong>geo_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies a <code class="docutils literal notranslate"><span class="pre">geo_location</span></code> resource, used to define where data should be replicated with the <code class="docutils literal notranslate"><span class="pre">failover_priority</span></code> 0 specifying the primary location.</p></li>
<li><p><strong>ip_range_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP’s for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.</p></li>
<li><p><strong>is_virtual_network_filter_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables virtual network filtering for this Cosmos DB account.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Kind of CosmosDB to create - possible values are <code class="docutils literal notranslate"><span class="pre">GlobalDocumentDB</span></code> and <code class="docutils literal notranslate"><span class="pre">MongoDB</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">GlobalDocumentDB</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>offer_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><strong>primary_master_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary master key for the CosmosDB Account.</p></li>
<li><p><strong>primary_readonly_master_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary read-only master Key for the CosmosDB Account.</p></li>
<li><p><strong>read_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of read endpoints available for this CosmosDB account.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_master_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary master key for the CosmosDB Account.</p></li>
<li><p><strong>secondary_readonly_master_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary read-only master key for the CosmosDB Account.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>virtual_network_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies a <code class="docutils literal notranslate"><span class="pre">virtual_network_rules</span></code> resource, used to define which subnets are allowed to access this CosmosDB account.</p></li>
<li><p><strong>write_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of write endpoints available for this CosmosDB account.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>capabilities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>consistency_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">consistencyLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Consistency Level to use for this CosmosDB Account - can be either <code class="docutils literal notranslate"><span class="pre">BoundedStaleness</span></code>, <code class="docutils literal notranslate"><span class="pre">Eventual</span></code>, <code class="docutils literal notranslate"><span class="pre">Session</span></code>, <code class="docutils literal notranslate"><span class="pre">Strong</span></code> or <code class="docutils literal notranslate"><span class="pre">ConsistentPrefix</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIntervalInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - When used with the Bounded Staleness consistency level, this value represents the time amount of staleness (in seconds) tolerated. Accepted range for this value is <code class="docutils literal notranslate"><span class="pre">5</span></code> - <code class="docutils literal notranslate"><span class="pre">86400</span></code> (1 day). Defaults to <code class="docutils literal notranslate"><span class="pre">5</span></code>. Required when <code class="docutils literal notranslate"><span class="pre">consistency_level</span></code> is set to <code class="docutils literal notranslate"><span class="pre">BoundedStaleness</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxStalenessPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - When used with the Bounded Staleness consistency level, this value represents the number of stale requests tolerated. Accepted range for this value is <code class="docutils literal notranslate"><span class="pre">10</span></code> – <code class="docutils literal notranslate"><span class="pre">2147483647</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>. Required when <code class="docutils literal notranslate"><span class="pre">consistency_level</span></code> is set to <code class="docutils literal notranslate"><span class="pre">BoundedStaleness</span></code>.</p></li>
</ul>
<p>The <strong>geo_locations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">failoverPriority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The failover priority of the region. A failover priority of <code class="docutils literal notranslate"><span class="pre">0</span></code> indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. Changing this causes the location to be re-provisioned and cannot be changed for the location with failover priority <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the virtual network subnet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Azure region to host replicated data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The string used to generate the document endpoints for this region. If not specified it defaults to <code class="docutils literal notranslate"><span class="pre">${cosmosdb_account.name}-${location}</span></code>. Changing this causes the location to be deleted and re-provisioned and cannot be changed for the location with failover priority <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
</ul>
<p>The <strong>virtual_network_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the virtual network subnet.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.AwaitableGetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cosmosdb.</code><code class="sig-name descname">AwaitableGetAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">capabilities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">consistency_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_automatic_failover</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_multiple_write_locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">geo_locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_virtual_network_filter_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_master_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_readonly_master_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_endpoints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_master_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_readonly_master_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_network_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">write_endpoints</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.AwaitableGetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.cosmosdb.CassandraKeyspace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cosmosdb.</code><code class="sig-name descname">CassandraKeyspace</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.CassandraKeyspace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Cassandra KeySpace within a Cosmos DB Account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">get_resource_group</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;tflex-cosmosdb-account-rg&quot;</span><span class="p">)</span>
<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;exampleAccount&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">offer_type</span><span class="o">=</span><span class="s2">&quot;Standard&quot;</span><span class="p">,</span>
    <span class="n">capabilities</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;EnableCassandra&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">consistency_policy</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;consistencyLevel&quot;</span><span class="p">:</span> <span class="s2">&quot;Strong&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">geo_location</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;location&quot;</span><span class="p">:</span> <span class="s2">&quot;West US&quot;</span><span class="p">,</span>
        <span class="s2">&quot;failoverPriority&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
    <span class="p">}])</span>
<span class="n">example_cassandra_keyspace</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">CassandraKeyspace</span><span class="p">(</span><span class="s2">&quot;exampleCassandraKeyspace&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">resource_group_name</span><span class="p">,</span>
    <span class="n">account_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">throughput</span><span class="o">=</span><span class="mi">400</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB Cassandra KeySpace to create the table within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB Cassandra KeySpace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB Cassandra KeySpace is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of Cassandra keyspace (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.CassandraKeyspace.account_name">
<code class="sig-name descname">account_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.CassandraKeyspace.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Cosmos DB Cassandra KeySpace to create the table within. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.CassandraKeyspace.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.CassandraKeyspace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Cosmos DB Cassandra KeySpace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.CassandraKeyspace.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.CassandraKeyspace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Cosmos DB Cassandra KeySpace is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.CassandraKeyspace.throughput">
<code class="sig-name descname">throughput</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.CassandraKeyspace.throughput" title="Permalink to this definition">¶</a></dt>
<dd><p>The throughput of Cassandra keyspace (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.CassandraKeyspace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.CassandraKeyspace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CassandraKeyspace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB Cassandra KeySpace to create the table within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB Cassandra KeySpace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB Cassandra KeySpace is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of Cassandra keyspace (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.CassandraKeyspace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.CassandraKeyspace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.CassandraKeyspace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.CassandraKeyspace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.GetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cosmosdb.</code><code class="sig-name descname">GetAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">capabilities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">consistency_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_automatic_failover</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_multiple_write_locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">geo_locations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_range_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_virtual_network_filter_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_master_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_readonly_master_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_endpoints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_master_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_readonly_master_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_network_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">write_endpoints</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.capabilities">
<code class="sig-name descname">capabilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>Capabilities enabled on this Cosmos DB account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.enable_automatic_failover">
<code class="sig-name descname">enable_automatic_failover</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.enable_automatic_failover" title="Permalink to this definition">¶</a></dt>
<dd><p>If automatic failover is enabled for this CosmosDB Account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.enable_multiple_write_locations">
<code class="sig-name descname">enable_multiple_write_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.enable_multiple_write_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>If multi-master is enabled for this Cosmos DB account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint used to connect to the CosmosDB account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.ip_range_filter">
<code class="sig-name descname">ip_range_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.ip_range_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The current IP Filter for this CosmosDB account</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.is_virtual_network_filter_enabled">
<code class="sig-name descname">is_virtual_network_filter_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.is_virtual_network_filter_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If virtual network filtering is enabled for this Cosmos DB account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The Kind of the CosmosDB account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Azure region hosting replicated data.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.offer_type">
<code class="sig-name descname">offer_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.offer_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Offer Type to used by this CosmosDB Account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.primary_master_key">
<code class="sig-name descname">primary_master_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.primary_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary master key for the CosmosDB Account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.primary_readonly_master_key">
<code class="sig-name descname">primary_readonly_master_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.primary_readonly_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary read-only master Key for the CosmosDB Account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.read_endpoints">
<code class="sig-name descname">read_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.read_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of read endpoints available for this CosmosDB account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.secondary_master_key">
<code class="sig-name descname">secondary_master_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.secondary_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary master key for the CosmosDB Account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.secondary_readonly_master_key">
<code class="sig-name descname">secondary_readonly_master_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.secondary_readonly_master_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary read-only master key for the CosmosDB Account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.virtual_network_rules">
<code class="sig-name descname">virtual_network_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.virtual_network_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnets that are allowed to access this CosmosDB account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GetAccountResult.write_endpoints">
<code class="sig-name descname">write_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GetAccountResult.write_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of write endpoints available for this CosmosDB account.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.cosmosdb.GremlinDatabase">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cosmosdb.</code><code class="sig-name descname">GremlinDatabase</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinDatabase" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Gremlin Database within a Cosmos DB Account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">get_account</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;tfex-cosmosdb-account&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;tfex-cosmosdb-account-rg&quot;</span><span class="p">)</span>
<span class="n">example_gremlin_database</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">GremlinDatabase</span><span class="p">(</span><span class="s2">&quot;exampleGremlinDatabase&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">resource_group_name</span><span class="p">,</span>
    <span class="n">account_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">throughput</span><span class="o">=</span><span class="mi">400</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the CosmosDB Account to create the Gremlin Database within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB Gremlin Database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB Gremlin Database is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of the Gremlin database (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GremlinDatabase.account_name">
<code class="sig-name descname">account_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinDatabase.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the CosmosDB Account to create the Gremlin Database within. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GremlinDatabase.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinDatabase.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Cosmos DB Gremlin Database. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GremlinDatabase.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinDatabase.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Cosmos DB Gremlin Database is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GremlinDatabase.throughput">
<code class="sig-name descname">throughput</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinDatabase.throughput" title="Permalink to this definition">¶</a></dt>
<dd><p>The throughput of the Gremlin database (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.GremlinDatabase.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinDatabase.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GremlinDatabase resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the CosmosDB Account to create the Gremlin Database within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB Gremlin Database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB Gremlin Database is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of the Gremlin database (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.GremlinDatabase.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinDatabase.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.GremlinDatabase.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinDatabase.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.GremlinGraph">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cosmosdb.</code><code class="sig-name descname">GremlinGraph</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conflict_resolution_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">index_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partition_key_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unique_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinGraph" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Gremlin Graph within a Cosmos DB Account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">get_account</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;tfex-cosmosdb-account&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;tfex-cosmosdb-account-rg&quot;</span><span class="p">)</span>
<span class="n">example_gremlin_database</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">GremlinDatabase</span><span class="p">(</span><span class="s2">&quot;exampleGremlinDatabase&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">resource_group_name</span><span class="p">,</span>
    <span class="n">account_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_gremlin_graph</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">GremlinGraph</span><span class="p">(</span><span class="s2">&quot;exampleGremlinGraph&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">azurerm_cosmosdb_account</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;resource_group_name&quot;</span><span class="p">],</span>
    <span class="n">account_name</span><span class="o">=</span><span class="n">azurerm_cosmosdb_account</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">database_name</span><span class="o">=</span><span class="n">example_gremlin_database</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">partition_key_path</span><span class="o">=</span><span class="s2">&quot;/Example&quot;</span><span class="p">,</span>
    <span class="n">throughput</span><span class="o">=</span><span class="mi">400</span><span class="p">,</span>
    <span class="n">index_policy</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;automatic&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;indexingMode&quot;</span><span class="p">:</span> <span class="s2">&quot;Consistent&quot;</span><span class="p">,</span>
        <span class="s2">&quot;includedPaths&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;/*&quot;</span><span class="p">],</span>
        <span class="s2">&quot;excludedPaths&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;/&quot;</span><span class="n">_etag</span><span class="s2">&quot;/?&quot;</span><span class="p">],</span>
    <span class="p">}],</span>
    <span class="n">conflict_resolution_policy</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;mode&quot;</span><span class="p">:</span> <span class="s2">&quot;LastWriterWins&quot;</span><span class="p">,</span>
        <span class="s2">&quot;conflictResolutionPath&quot;</span><span class="p">:</span> <span class="s2">&quot;/_ts&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">unique_key</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;paths&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;/definition/id1&quot;</span><span class="p">,</span>
            <span class="s2">&quot;/definition/id2&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the CosmosDB Account to create the Gremlin Graph within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>conflict_resolution_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The conflict resolution policy for the graph. One or more <code class="docutils literal notranslate"><span class="pre">conflict_resolution_policy</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB Graph Database in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>index_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The configuration of the indexing policy. One or more <code class="docutils literal notranslate"><span class="pre">index_policy</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB Gremlin Graph. Changing this forces a new resource to be created.</p></li>
<li><p><strong>partition_key_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Define a partition key. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of the Gremlin database (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
<li><p><strong>unique_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">unique_key</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>conflict_resolution_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conflictResolutionPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The conflict resolution path in the case of LastWriterWins mode.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">conflictResolutionProcedure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The procedure to resolve conflicts in the case of custom mode.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates the conflict resolution mode. Possible values include: <code class="docutils literal notranslate"><span class="pre">LastWriterWins</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>.</p></li>
</ul>
<p>The <strong>index_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automatic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if the indexing policy is automatic. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">excludedPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of paths to exclude from indexing. Required if <code class="docutils literal notranslate"><span class="pre">indexing_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Consistent</span></code> or <code class="docutils literal notranslate"><span class="pre">Lazy</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includedPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of paths to include in the indexing. Required if <code class="docutils literal notranslate"><span class="pre">indexing_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Consistent</span></code> or <code class="docutils literal notranslate"><span class="pre">Lazy</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexingMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates the indexing mode. Possible values include: <code class="docutils literal notranslate"><span class="pre">Consistent</span></code>, <code class="docutils literal notranslate"><span class="pre">Lazy</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
</ul>
<p>The <strong>unique_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">paths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of paths to use for this unique key.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GremlinGraph.account_name">
<code class="sig-name descname">account_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinGraph.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the CosmosDB Account to create the Gremlin Graph within. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GremlinGraph.conflict_resolution_policies">
<code class="sig-name descname">conflict_resolution_policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinGraph.conflict_resolution_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The conflict resolution policy for the graph. One or more <code class="docutils literal notranslate"><span class="pre">conflict_resolution_policy</span></code> blocks as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conflictResolutionPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The conflict resolution path in the case of LastWriterWins mode.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">conflictResolutionProcedure</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The procedure to resolve conflicts in the case of custom mode.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Indicates the conflict resolution mode. Possible values include: <code class="docutils literal notranslate"><span class="pre">LastWriterWins</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GremlinGraph.database_name">
<code class="sig-name descname">database_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinGraph.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Cosmos DB Graph Database in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GremlinGraph.index_policies">
<code class="sig-name descname">index_policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinGraph.index_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration of the indexing policy. One or more <code class="docutils literal notranslate"><span class="pre">index_policy</span></code> blocks as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automatic</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates if the indexing policy is automatic. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">excludedPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of paths to exclude from indexing. Required if <code class="docutils literal notranslate"><span class="pre">indexing_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Consistent</span></code> or <code class="docutils literal notranslate"><span class="pre">Lazy</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includedPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of paths to include in the indexing. Required if <code class="docutils literal notranslate"><span class="pre">indexing_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Consistent</span></code> or <code class="docutils literal notranslate"><span class="pre">Lazy</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexingMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Indicates the indexing mode. Possible values include: <code class="docutils literal notranslate"><span class="pre">Consistent</span></code>, <code class="docutils literal notranslate"><span class="pre">Lazy</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GremlinGraph.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinGraph.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Cosmos DB Gremlin Graph. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GremlinGraph.partition_key_path">
<code class="sig-name descname">partition_key_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinGraph.partition_key_path" title="Permalink to this definition">¶</a></dt>
<dd><p>Define a partition key. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GremlinGraph.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinGraph.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GremlinGraph.throughput">
<code class="sig-name descname">throughput</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinGraph.throughput" title="Permalink to this definition">¶</a></dt>
<dd><p>The throughput of the Gremlin database (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.GremlinGraph.unique_keys">
<code class="sig-name descname">unique_keys</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinGraph.unique_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">unique_key</span></code> blocks as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">paths</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of paths to use for this unique key.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.GremlinGraph.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conflict_resolution_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">index_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partition_key_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unique_keys</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinGraph.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GremlinGraph resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the CosmosDB Account to create the Gremlin Graph within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>conflict_resolution_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The conflict resolution policy for the graph. One or more <code class="docutils literal notranslate"><span class="pre">conflict_resolution_policy</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB Graph Database in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>index_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The configuration of the indexing policy. One or more <code class="docutils literal notranslate"><span class="pre">index_policy</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB Gremlin Graph. Changing this forces a new resource to be created.</p></li>
<li><p><strong>partition_key_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Define a partition key. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB Gremlin Graph is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of the Gremlin database (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
<li><p><strong>unique_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">unique_key</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>conflict_resolution_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conflictResolutionPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The conflict resolution path in the case of LastWriterWins mode.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">conflictResolutionProcedure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The procedure to resolve conflicts in the case of custom mode.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates the conflict resolution mode. Possible values include: <code class="docutils literal notranslate"><span class="pre">LastWriterWins</span></code>, <code class="docutils literal notranslate"><span class="pre">Custom</span></code>.</p></li>
</ul>
<p>The <strong>index_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automatic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates if the indexing policy is automatic. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">excludedPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of paths to exclude from indexing. Required if <code class="docutils literal notranslate"><span class="pre">indexing_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Consistent</span></code> or <code class="docutils literal notranslate"><span class="pre">Lazy</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includedPaths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of paths to include in the indexing. Required if <code class="docutils literal notranslate"><span class="pre">indexing_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Consistent</span></code> or <code class="docutils literal notranslate"><span class="pre">Lazy</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">indexingMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Indicates the indexing mode. Possible values include: <code class="docutils literal notranslate"><span class="pre">Consistent</span></code>, <code class="docutils literal notranslate"><span class="pre">Lazy</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
</ul>
<p>The <strong>unique_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">paths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of paths to use for this unique key.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.GremlinGraph.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinGraph.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.GremlinGraph.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.GremlinGraph.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.MongoCollection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cosmosdb.</code><code class="sig-name descname">MongoCollection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_ttl_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">indices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shard_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoCollection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Mongo Collection within a Cosmos DB Account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">get_account</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;tfex-cosmosdb-account&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;tfex-cosmosdb-account-rg&quot;</span><span class="p">)</span>
<span class="n">example_mongo_database</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">MongoDatabase</span><span class="p">(</span><span class="s2">&quot;exampleMongoDatabase&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">resource_group_name</span><span class="p">,</span>
    <span class="n">account_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_mongo_collection</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">MongoCollection</span><span class="p">(</span><span class="s2">&quot;exampleMongoCollection&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">resource_group_name</span><span class="p">,</span>
    <span class="n">account_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">database_name</span><span class="o">=</span><span class="n">example_mongo_database</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">default_ttl_seconds</span><span class="o">=</span><span class="s2">&quot;777&quot;</span><span class="p">,</span>
    <span class="n">shard_key</span><span class="o">=</span><span class="s2">&quot;uniqueKey&quot;</span><span class="p">,</span>
    <span class="n">throughput</span><span class="o">=</span><span class="mi">400</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB Mongo Database in which the Cosmos DB Mongo Collection is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>default_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default Time To Live in seconds. If the value is <code class="docutils literal notranslate"><span class="pre">0</span></code> items are not automatically expired.</p></li>
<li><p><strong>indices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">index</span></code> blocks as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB Mongo Collection. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB Mongo Collection is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>shard_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the key to partition on for sharding. There must not be any other unique index keys.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of the MongoDB collection (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>indices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the list of user settable keys for each Cosmos DB Mongo Collection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unique</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the index unique or not? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.MongoCollection.database_name">
<code class="sig-name descname">database_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoCollection.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Cosmos DB Mongo Database in which the Cosmos DB Mongo Collection is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.MongoCollection.default_ttl_seconds">
<code class="sig-name descname">default_ttl_seconds</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoCollection.default_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The default Time To Live in seconds. If the value is <code class="docutils literal notranslate"><span class="pre">0</span></code> items are not automatically expired.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.MongoCollection.indices">
<code class="sig-name descname">indices</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoCollection.indices" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">index</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies the list of user settable keys for each Cosmos DB Mongo Collection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unique</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the index unique or not? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.MongoCollection.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoCollection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Cosmos DB Mongo Collection. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.MongoCollection.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoCollection.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Cosmos DB Mongo Collection is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.MongoCollection.shard_key">
<code class="sig-name descname">shard_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoCollection.shard_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the key to partition on for sharding. There must not be any other unique index keys.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.MongoCollection.system_indexes">
<code class="sig-name descname">system_indexes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoCollection.system_indexes" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">system_indexes</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies the list of user settable keys for each Cosmos DB Mongo Collection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unique</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the index unique or not? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.MongoCollection.throughput">
<code class="sig-name descname">throughput</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoCollection.throughput" title="Permalink to this definition">¶</a></dt>
<dd><p>The throughput of the MongoDB collection (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.MongoCollection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_ttl_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">indices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shard_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_indexes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoCollection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MongoCollection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB Mongo Database in which the Cosmos DB Mongo Collection is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>default_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default Time To Live in seconds. If the value is <code class="docutils literal notranslate"><span class="pre">0</span></code> items are not automatically expired.</p></li>
<li><p><strong>indices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">index</span></code> blocks as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB Mongo Collection. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB Mongo Collection is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>shard_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the key to partition on for sharding. There must not be any other unique index keys.</p></li>
<li><p><strong>system_indexes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">system_indexes</span></code> blocks as defined below.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of the MongoDB collection (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>indices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the list of user settable keys for each Cosmos DB Mongo Collection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unique</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the index unique or not? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>system_indexes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">keys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the list of user settable keys for each Cosmos DB Mongo Collection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unique</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the index unique or not? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.MongoCollection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoCollection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.MongoCollection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoCollection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.MongoDatabase">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cosmosdb.</code><code class="sig-name descname">MongoDatabase</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoDatabase" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Mongo Database within a Cosmos DB Account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">get_account</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;tfex-cosmosdb-account&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;tfex-cosmosdb-account-rg&quot;</span><span class="p">)</span>
<span class="n">example_mongo_database</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">MongoDatabase</span><span class="p">(</span><span class="s2">&quot;exampleMongoDatabase&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">resource_group_name</span><span class="p">,</span>
    <span class="n">account_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">throughput</span><span class="o">=</span><span class="mi">400</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB Mongo Database to create the table within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB Mongo Database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB Mongo Database is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of the MongoDB collection (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.MongoDatabase.account_name">
<code class="sig-name descname">account_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoDatabase.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Cosmos DB Mongo Database to create the table within. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.MongoDatabase.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoDatabase.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Cosmos DB Mongo Database. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.MongoDatabase.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoDatabase.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Cosmos DB Mongo Database is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.MongoDatabase.throughput">
<code class="sig-name descname">throughput</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoDatabase.throughput" title="Permalink to this definition">¶</a></dt>
<dd><p>The throughput of the MongoDB collection (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.MongoDatabase.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoDatabase.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MongoDatabase resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB Mongo Database to create the table within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB Mongo Database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB Mongo Database is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of the MongoDB collection (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.MongoDatabase.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoDatabase.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.MongoDatabase.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.MongoDatabase.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.SqlContainer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cosmosdb.</code><code class="sig-name descname">SqlContainer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partition_key_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unique_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlContainer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a SQL Container within a Cosmos DB Account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">SqlContainer</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">azurerm_cosmosdb_account</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;resource_group_name&quot;</span><span class="p">],</span>
    <span class="n">account_name</span><span class="o">=</span><span class="n">azurerm_cosmosdb_account</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">database_name</span><span class="o">=</span><span class="n">azurerm_cosmosdb_sql_database</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">partition_key_path</span><span class="o">=</span><span class="s2">&quot;/definition/id&quot;</span><span class="p">,</span>
    <span class="n">throughput</span><span class="o">=</span><span class="mi">400</span><span class="p">,</span>
    <span class="n">unique_key</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;paths&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;/definition/idlong&quot;</span><span class="p">,</span>
            <span class="s2">&quot;/definition/idshort&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB Account to create the container within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB SQL Database to create the container within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>default_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default time to live of SQL container. If missing, items are not expired automatically. If present and the value is set to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, it is equal to infinity, and items don’t expire by default. If present and the value is set to some number <code class="docutils literal notranslate"><span class="pre">n</span></code> – items will expire <code class="docutils literal notranslate"><span class="pre">n</span></code> seconds after their last modified time.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB SQL Database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>partition_key_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Define a partition key. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB SQL Database is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of SQL container (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon container creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
<li><p><strong>unique_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">unique_key</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>unique_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">paths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of paths to use for this unique key.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.SqlContainer.account_name">
<code class="sig-name descname">account_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlContainer.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Cosmos DB Account to create the container within. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.SqlContainer.database_name">
<code class="sig-name descname">database_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlContainer.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Cosmos DB SQL Database to create the container within. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.SqlContainer.default_ttl">
<code class="sig-name descname">default_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlContainer.default_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The default time to live of SQL container. If missing, items are not expired automatically. If present and the value is set to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, it is equal to infinity, and items don’t expire by default. If present and the value is set to some number <code class="docutils literal notranslate"><span class="pre">n</span></code> – items will expire <code class="docutils literal notranslate"><span class="pre">n</span></code> seconds after their last modified time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.SqlContainer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlContainer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Cosmos DB SQL Database. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.SqlContainer.partition_key_path">
<code class="sig-name descname">partition_key_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlContainer.partition_key_path" title="Permalink to this definition">¶</a></dt>
<dd><p>Define a partition key. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.SqlContainer.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlContainer.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Cosmos DB SQL Database is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.SqlContainer.throughput">
<code class="sig-name descname">throughput</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlContainer.throughput" title="Permalink to this definition">¶</a></dt>
<dd><p>The throughput of SQL container (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon container creation otherwise it cannot be updated without a manual resource destroy-apply.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.SqlContainer.unique_keys">
<code class="sig-name descname">unique_keys</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlContainer.unique_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">unique_key</span></code> blocks as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">paths</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of paths to use for this unique key.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.SqlContainer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partition_key_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unique_keys</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlContainer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SqlContainer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB Account to create the container within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB SQL Database to create the container within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>default_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default time to live of SQL container. If missing, items are not expired automatically. If present and the value is set to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, it is equal to infinity, and items don’t expire by default. If present and the value is set to some number <code class="docutils literal notranslate"><span class="pre">n</span></code> – items will expire <code class="docutils literal notranslate"><span class="pre">n</span></code> seconds after their last modified time.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB SQL Database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>partition_key_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Define a partition key. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB SQL Database is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of SQL container (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon container creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
<li><p><strong>unique_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">unique_key</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>unique_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">paths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of paths to use for this unique key.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.SqlContainer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlContainer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.SqlContainer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlContainer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.SqlDatabase">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cosmosdb.</code><code class="sig-name descname">SqlDatabase</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlDatabase" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a SQL Database within a Cosmos DB Account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">get_account</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;tfex-cosmosdb-account&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;tfex-cosmosdb-account-rg&quot;</span><span class="p">)</span>
<span class="n">example_sql_database</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">SqlDatabase</span><span class="p">(</span><span class="s2">&quot;exampleSqlDatabase&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">resource_group_name</span><span class="p">,</span>
    <span class="n">account_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">throughput</span><span class="o">=</span><span class="mi">400</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB SQL Database to create the table within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB SQL Database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB SQL Database is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of SQL database (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.SqlDatabase.account_name">
<code class="sig-name descname">account_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlDatabase.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Cosmos DB SQL Database to create the table within. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.SqlDatabase.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlDatabase.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Cosmos DB SQL Database. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.SqlDatabase.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlDatabase.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Cosmos DB SQL Database is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.SqlDatabase.throughput">
<code class="sig-name descname">throughput</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlDatabase.throughput" title="Permalink to this definition">¶</a></dt>
<dd><p>The throughput of SQL database (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.SqlDatabase.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlDatabase.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SqlDatabase resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB SQL Database to create the table within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB SQL Database. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB SQL Database is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of SQL database (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.SqlDatabase.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlDatabase.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.SqlDatabase.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.SqlDatabase.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.Table">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cosmosdb.</code><code class="sig-name descname">Table</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.Table" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Table within a Cosmos DB Account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">get_account</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;tfex-cosmosdb-account&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;tfex-cosmosdb-account-rg&quot;</span><span class="p">)</span>
<span class="n">example_table</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">Table</span><span class="p">(</span><span class="s2">&quot;exampleTable&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">resource_group_name</span><span class="p">,</span>
    <span class="n">account_name</span><span class="o">=</span><span class="n">example_account</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">throughput</span><span class="o">=</span><span class="mi">400</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB Table to create the table within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB Table. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB Table is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of Table (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Table.account_name">
<code class="sig-name descname">account_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Table.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Cosmos DB Table to create the table within. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Table.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Table.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Cosmos DB Table. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Table.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Table.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Cosmos DB Table is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cosmosdb.Table.throughput">
<code class="sig-name descname">throughput</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cosmosdb.Table.throughput" title="Permalink to this definition">¶</a></dt>
<dd><p>The throughput of Table (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.Table.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">throughput</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.Table.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Table resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cosmos DB Table to create the table within. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Cosmos DB Table. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Cosmos DB Table is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>throughput</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The throughput of Table (RU/s). Must be set in increments of <code class="docutils literal notranslate"><span class="pre">100</span></code>. The minimum value is <code class="docutils literal notranslate"><span class="pre">400</span></code>. This must be set upon database creation otherwise it cannot be updated without a manual resource destroy-apply.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cosmosdb.Table.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.Table.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.Table.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.Table.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cosmosdb.get_account">
<code class="sig-prename descclassname">pulumi_azure.cosmosdb.</code><code class="sig-name descname">get_account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cosmosdb.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing CosmosDB (formally DocumentDB) Account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cosmosdb</span><span class="o">.</span><span class="n">get_account</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;tfex-cosmosdb-account&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;tfex-cosmosdb-account-rg&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;cosmosdbAccountEndpoint&quot;</span><span class="p">,</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;cosmosdb.Account&quot;</span><span class="p">][</span><span class="s2">&quot;jobs&quot;</span><span class="p">][</span><span class="s2">&quot;endpoint&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the CosmosDB Account.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group in which the CosmosDB Account resides.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
