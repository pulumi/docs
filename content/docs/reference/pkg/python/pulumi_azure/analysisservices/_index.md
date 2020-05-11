---
title: Module analysisservices
title_tag: Module analysisservices | Package pulumi_azure | Python SDK
linktitle: analysisservices
notitle: true
---

<div class="section" id="analysisservices">
<h1>analysisservices<a class="headerlink" href="#analysisservices" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.analysisservices"></span><dl class="py class">
<dt id="pulumi_azure.analysisservices.Server">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.analysisservices.</code><code class="sig-name descname">Server</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_blob_container_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_power_bi_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4_firewall_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">querypool_connection_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.analysisservices.Server" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Analysis Services Server.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">rg</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;rg&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;northeurope&quot;</span><span class="p">)</span>
<span class="n">server</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">analysisservices</span><span class="o">.</span><span class="n">Server</span><span class="p">(</span><span class="s2">&quot;server&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;northeurope&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">rg</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">sku</span><span class="o">=</span><span class="s2">&quot;S0&quot;</span><span class="p">,</span>
    <span class="n">admin_users</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;myuser@domain.tld&quot;</span><span class="p">],</span>
    <span class="n">enable_power_bi_service</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">ipv4_firewall_rule</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;myRule1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;rangeStart&quot;</span><span class="p">:</span> <span class="s2">&quot;210.117.252.0&quot;</span><span class="p">,</span>
        <span class="s2">&quot;rangeEnd&quot;</span><span class="p">:</span> <span class="s2">&quot;210.117.252.255&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;abc&quot;</span><span class="p">:</span> <span class="mi">123</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of email addresses of admin users.</p></li>
<li><p><strong>backup_blob_container_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI and SAS token for a blob container to store backups.</p></li>
<li><p><strong>enable_power_bi_service</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if the Power BI service is allowed to access or not.</p></li>
<li><p><strong>ipv4_firewall_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">ipv4_firewall_rule</span></code> block(s) as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the Analysis Services Server exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the firewall rule.</p></li>
<li><p><strong>querypool_connection_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls how the read-write server is used in the query pool. If this value is set to <code class="docutils literal notranslate"><span class="pre">All</span></code> then read-write servers are also used for queries. Otherwise with <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> these servers do not participate in query operations.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Analysis Services Server should be exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SKU for the Analysis Services Server. Possible values are: <code class="docutils literal notranslate"><span class="pre">D1</span></code>, <code class="docutils literal notranslate"><span class="pre">B1</span></code>, <code class="docutils literal notranslate"><span class="pre">B2</span></code>, <code class="docutils literal notranslate"><span class="pre">S0</span></code>, <code class="docutils literal notranslate"><span class="pre">S1</span></code>, <code class="docutils literal notranslate"><span class="pre">S2</span></code>, <code class="docutils literal notranslate"><span class="pre">S4</span></code>, <code class="docutils literal notranslate"><span class="pre">S8</span></code> and <code class="docutils literal notranslate"><span class="pre">S9</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>ipv4_firewall_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the firewall rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rangeEnd</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - End of the firewall rule range as IPv4 address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rangeStart</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Start of the firewall rule range as IPv4 address.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.analysisservices.Server.admin_users">
<code class="sig-name descname">admin_users</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.analysisservices.Server.admin_users" title="Permalink to this definition">¶</a></dt>
<dd><p>List of email addresses of admin users.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.analysisservices.Server.backup_blob_container_uri">
<code class="sig-name descname">backup_blob_container_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.analysisservices.Server.backup_blob_container_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI and SAS token for a blob container to store backups.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.analysisservices.Server.enable_power_bi_service">
<code class="sig-name descname">enable_power_bi_service</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.analysisservices.Server.enable_power_bi_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates if the Power BI service is allowed to access or not.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.analysisservices.Server.ipv4_firewall_rules">
<code class="sig-name descname">ipv4_firewall_rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.analysisservices.Server.ipv4_firewall_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">ipv4_firewall_rule</span></code> block(s) as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the firewall rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rangeEnd</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - End of the firewall rule range as IPv4 address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rangeStart</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Start of the firewall rule range as IPv4 address.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.analysisservices.Server.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.analysisservices.Server.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Analysis Services Server exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.analysisservices.Server.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.analysisservices.Server.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the firewall rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.analysisservices.Server.querypool_connection_mode">
<code class="sig-name descname">querypool_connection_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.analysisservices.Server.querypool_connection_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls how the read-write server is used in the query pool. If this value is set to <code class="docutils literal notranslate"><span class="pre">All</span></code> then read-write servers are also used for queries. Otherwise with <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> these servers do not participate in query operations.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.analysisservices.Server.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.analysisservices.Server.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Analysis Services Server should be exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.analysisservices.Server.server_full_name">
<code class="sig-name descname">server_full_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.analysisservices.Server.server_full_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full name of the Analysis Services Server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.analysisservices.Server.sku">
<code class="sig-name descname">sku</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.analysisservices.Server.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>SKU for the Analysis Services Server. Possible values are: <code class="docutils literal notranslate"><span class="pre">D1</span></code>, <code class="docutils literal notranslate"><span class="pre">B1</span></code>, <code class="docutils literal notranslate"><span class="pre">B2</span></code>, <code class="docutils literal notranslate"><span class="pre">S0</span></code>, <code class="docutils literal notranslate"><span class="pre">S1</span></code>, <code class="docutils literal notranslate"><span class="pre">S2</span></code>, <code class="docutils literal notranslate"><span class="pre">S4</span></code>, <code class="docutils literal notranslate"><span class="pre">S8</span></code> and <code class="docutils literal notranslate"><span class="pre">S9</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.analysisservices.Server.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_users</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_blob_container_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_power_bi_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv4_firewall_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">querypool_connection_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_full_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.analysisservices.Server.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Server resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_users</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of email addresses of admin users.</p></li>
<li><p><strong>backup_blob_container_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI and SAS token for a blob container to store backups.</p></li>
<li><p><strong>enable_power_bi_service</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if the Power BI service is allowed to access or not.</p></li>
<li><p><strong>ipv4_firewall_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">ipv4_firewall_rule</span></code> block(s) as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the Analysis Services Server exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the firewall rule.</p></li>
<li><p><strong>querypool_connection_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls how the read-write server is used in the query pool. If this value is set to <code class="docutils literal notranslate"><span class="pre">All</span></code> then read-write servers are also used for queries. Otherwise with <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> these servers do not participate in query operations.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Analysis Services Server should be exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_full_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full name of the Analysis Services Server.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SKU for the Analysis Services Server. Possible values are: <code class="docutils literal notranslate"><span class="pre">D1</span></code>, <code class="docutils literal notranslate"><span class="pre">B1</span></code>, <code class="docutils literal notranslate"><span class="pre">B2</span></code>, <code class="docutils literal notranslate"><span class="pre">S0</span></code>, <code class="docutils literal notranslate"><span class="pre">S1</span></code>, <code class="docutils literal notranslate"><span class="pre">S2</span></code>, <code class="docutils literal notranslate"><span class="pre">S4</span></code>, <code class="docutils literal notranslate"><span class="pre">S8</span></code> and <code class="docutils literal notranslate"><span class="pre">S9</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>ipv4_firewall_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the firewall rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rangeEnd</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - End of the firewall rule range as IPv4 address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rangeStart</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Start of the firewall rule range as IPv4 address.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.analysisservices.Server.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.analysisservices.Server.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.analysisservices.Server.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.analysisservices.Server.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
