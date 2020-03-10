---
title: Module mariadb
title_tag: Module mariadb | Package pulumi_azure | Python SDK
linktitle: mariadb
notitle: true
---

<div class="section" id="mariadb">
<h1>mariadb<a class="headerlink" href="#mariadb" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.mariadb"></span><dl class="class">
<dt id="pulumi_azure.mariadb.AwaitableGetMariaDbServerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mariadb.</code><code class="sig-name descname">AwaitableGetMariaDbServerResult</code><span class="sig-paren">(</span><em class="sig-param">administrator_login=None</em>, <em class="sig-param">administrator_login_password=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">ssl_enforcement=None</em>, <em class="sig-param">storage_profiles=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.AwaitableGetMariaDbServerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.mariadb.Configuration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mariadb.</code><code class="sig-name descname">Configuration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets a MariaDB Configuration value on a MariaDB Server.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Configuration, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/server-system-variables/">to be a valid MariaDB configuration name</a>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the value of the MariaDB Configuration. See the MariaDB documentation for valid values.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_configuration.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.mariadb.Configuration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Configuration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MariaDB Configuration, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/server-system-variables/">to be a valid MariaDB configuration name</a>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Configuration.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Configuration.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Configuration.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Configuration.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Configuration.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Configuration.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the value of the MariaDB Configuration. See the MariaDB documentation for valid values.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mariadb.Configuration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Configuration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Configuration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the MariaDB Configuration, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/server-system-variables/">to be a valid MariaDB configuration name</a>. Changing this forces a new resource to be created.</p>
</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the value of the MariaDB Configuration. See the MariaDB documentation for valid values.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_configuration.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mariadb.Configuration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Configuration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.Configuration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Configuration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mariadb.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">charset=None</em>, <em class="sig-param">collation=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a MariaDB Database within a MariaDB Server</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>charset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Charset for the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/setting-character-sets-and-collations">to be a valid MariaDB Charset</a>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Collation for the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/setting-character-sets-and-collations">to be a valid MariaDB Collation</a>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/identifier-names/">to be a valid MariaDB identifier</a>. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_database.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_database.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.mariadb.Database.charset">
<code class="sig-name descname">charset</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Database.charset" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Charset for the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/setting-character-sets-and-collations">to be a valid MariaDB Charset</a>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Database.collation">
<code class="sig-name descname">collation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Database.collation" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Collation for the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/setting-character-sets-and-collations">to be a valid MariaDB Collation</a>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Database.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/identifier-names/">to be a valid MariaDB identifier</a>. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Database.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Database.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Database.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Database.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mariadb.Database.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">charset=None</em>, <em class="sig-param">collation=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>charset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the Charset for the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/setting-character-sets-and-collations">to be a valid MariaDB Charset</a>. Changing this forces a new resource to be created.</p>
</p></li>
<li><p><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the Collation for the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/setting-character-sets-and-collations">to be a valid MariaDB Collation</a>. Changing this forces a new resource to be created.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/identifier-names/">to be a valid MariaDB identifier</a>. Changing this forces a
new resource to be created.</p>
</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_database.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_database.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mariadb.Database.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.Database.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.FirewallRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mariadb.</code><code class="sig-name descname">FirewallRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">end_ip_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">start_ip_address=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Firewall Rule for a MariaDB Server</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Firewall Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_firewall_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.mariadb.FirewallRule.end_ip_address">
<code class="sig-name descname">end_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.end_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.FirewallRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MariaDB Firewall Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.FirewallRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.FirewallRule.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.FirewallRule.start_ip_address">
<code class="sig-name descname">start_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.start_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mariadb.FirewallRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">end_ip_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">start_ip_address=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Firewall Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_firewall_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mariadb.FirewallRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.FirewallRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.GetMariaDbServerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mariadb.</code><code class="sig-name descname">GetMariaDbServerResult</code><span class="sig-paren">(</span><em class="sig-param">administrator_login=None</em>, <em class="sig-param">administrator_login_password=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">ssl_enforcement=None</em>, <em class="sig-param">storage_profiles=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.GetMariaDbServerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMariaDbServer.</p>
<dl class="attribute">
<dt id="pulumi_azure.mariadb.GetMariaDbServerResult.administrator_login">
<code class="sig-name descname">administrator_login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.GetMariaDbServerResult.administrator_login" title="Permalink to this definition">¶</a></dt>
<dd><p>The Administrator Login for the MariaDB Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.GetMariaDbServerResult.administrator_login_password">
<code class="sig-name descname">administrator_login_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.GetMariaDbServerResult.administrator_login_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> for the MariaDB Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.GetMariaDbServerResult.fqdn">
<code class="sig-name descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.GetMariaDbServerResult.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the MariaDB Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.GetMariaDbServerResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.GetMariaDbServerResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the resource exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.GetMariaDbServerResult.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.GetMariaDbServerResult.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU Name for this MariaDB Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.GetMariaDbServerResult.ssl_enforcement">
<code class="sig-name descname">ssl_enforcement</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.GetMariaDbServerResult.ssl_enforcement" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSL being enforced on connections.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.GetMariaDbServerResult.storage_profiles">
<code class="sig-name descname">storage_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.GetMariaDbServerResult.storage_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_profile</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.GetMariaDbServerResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.GetMariaDbServerResult.tags" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.GetMariaDbServerResult.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.GetMariaDbServerResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of MariaDB being used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.GetMariaDbServerResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.GetMariaDbServerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.mariadb.Server">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mariadb.</code><code class="sig-name descname">Server</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">administrator_login=None</em>, <em class="sig-param">administrator_login_password=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">ssl_enforcement=None</em>, <em class="sig-param">storage_profile=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Server" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a MariaDB Server.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>administrator_login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Administrator Login for the MariaDB Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>administrator_login_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> for the MariaDB Server.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the MariaDB Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the SKU Name for this MariaDB Server. The name of the SKU, follows the <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> + <code class="docutils literal notranslate"><span class="pre">cores</span></code> pattern (e.g. <code class="docutils literal notranslate"><span class="pre">B_Gen4_1</span></code>, <code class="docutils literal notranslate"><span class="pre">GP_Gen5_8</span></code>). For more information see the <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/mariadb/servers/create#sku">product documentation</a>.</p></li>
<li><p><strong>ssl_enforcement</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if SSL should be enforced on connections. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
<li><p><strong>storage_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_profile</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of MariaDB to use. Possible values are <code class="docutils literal notranslate"><span class="pre">10.2</span></code> and <code class="docutils literal notranslate"><span class="pre">10.3</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>storage_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoGrow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupRetentionDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoRedundantBackup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageMb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_server.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_server.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.administrator_login">
<code class="sig-name descname">administrator_login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.administrator_login" title="Permalink to this definition">¶</a></dt>
<dd><p>The Administrator Login for the MariaDB Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.administrator_login_password">
<code class="sig-name descname">administrator_login_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.administrator_login_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> for the MariaDB Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.fqdn">
<code class="sig-name descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the MariaDB Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the MariaDB Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the SKU Name for this MariaDB Server. The name of the SKU, follows the <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> + <code class="docutils literal notranslate"><span class="pre">cores</span></code> pattern (e.g. <code class="docutils literal notranslate"><span class="pre">B_Gen4_1</span></code>, <code class="docutils literal notranslate"><span class="pre">GP_Gen5_8</span></code>). For more information see the <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/mariadb/servers/create#sku">product documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.ssl_enforcement">
<code class="sig-name descname">ssl_enforcement</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.ssl_enforcement" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if SSL should be enforced on connections. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.storage_profile">
<code class="sig-name descname">storage_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.storage_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_profile</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoGrow</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupRetentionDays</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoRedundantBackup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageMb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the version of MariaDB to use. Possible values are <code class="docutils literal notranslate"><span class="pre">10.2</span></code> and <code class="docutils literal notranslate"><span class="pre">10.3</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mariadb.Server.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">administrator_login=None</em>, <em class="sig-param">administrator_login_password=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">ssl_enforcement=None</em>, <em class="sig-param">storage_profile=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Server.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Server resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>administrator_login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Administrator Login for the MariaDB Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>administrator_login_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> for the MariaDB Server.</p></li>
<li><p><strong>fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN of the MariaDB Server.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the MariaDB Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the SKU Name for this MariaDB Server. The name of the SKU, follows the <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> + <code class="docutils literal notranslate"><span class="pre">cores</span></code> pattern (e.g. <code class="docutils literal notranslate"><span class="pre">B_Gen4_1</span></code>, <code class="docutils literal notranslate"><span class="pre">GP_Gen5_8</span></code>). For more information see the <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/mariadb/servers/create#sku">product documentation</a>.</p>
</p></li>
<li><p><strong>ssl_enforcement</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if SSL should be enforced on connections. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
<li><p><strong>storage_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_profile</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of MariaDB to use. Possible values are <code class="docutils literal notranslate"><span class="pre">10.2</span></code> and <code class="docutils literal notranslate"><span class="pre">10.3</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>storage_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoGrow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupRetentionDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoRedundantBackup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageMb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_server.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_server.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mariadb.Server.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Server.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.Server.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Server.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.VirtualNetworkRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.mariadb.</code><code class="sig-name descname">VirtualNetworkRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.VirtualNetworkRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a MariaDB Virtual Network Rule.</p>
<blockquote>
<div><p><strong>NOTE:</strong> MariaDB Virtual Network Rules <cite>can only be used with SKU Tiers of ``GeneralPurpose`</cite> or <code class="docutils literal notranslate"><span class="pre">MemoryOptimized</span></code> &lt;<a class="reference external" href="https://docs.microsoft.com/en-us/azure/mariadb/concepts-data-access-security-vnet">https://docs.microsoft.com/en-us/azure/mariadb/concepts-data-access-security-vnet</a>&gt;`_</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the MariaDB Virtual Network Rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the MariaDB server resides. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server to which this MariaDB virtual network rule will be applied to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet that the MariaDB server will be connected to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_virtual_network_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_virtual_network_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.mariadb.VirtualNetworkRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.VirtualNetworkRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the MariaDB Virtual Network Rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.VirtualNetworkRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.VirtualNetworkRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group where the MariaDB server resides. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.VirtualNetworkRule.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.VirtualNetworkRule.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server to which this MariaDB virtual network rule will be applied to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.VirtualNetworkRule.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.VirtualNetworkRule.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the subnet that the MariaDB server will be connected to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mariadb.VirtualNetworkRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.VirtualNetworkRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualNetworkRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the MariaDB Virtual Network Rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the MariaDB server resides. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server to which this MariaDB virtual network rule will be applied to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet that the MariaDB server will be connected to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_virtual_network_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_virtual_network_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mariadb.VirtualNetworkRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.VirtualNetworkRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.VirtualNetworkRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.VirtualNetworkRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.get_maria_db_server">
<code class="sig-prename descclassname">pulumi_azure.mariadb.</code><code class="sig-name descname">get_maria_db_server</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.get_maria_db_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing MariaDB Server.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the MariaDB Server to retrieve information about.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group where the MariaDB Server exists.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/mariadb_server.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/mariadb_server.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
