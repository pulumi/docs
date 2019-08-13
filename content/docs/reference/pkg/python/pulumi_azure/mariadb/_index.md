---
title: Module mariadb
---

<div class="section" id="mariadb">
<h1>mariadb<a class="headerlink" href="#mariadb" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.mariadb"></span><dl class="class">
<dt id="pulumi_azure.mariadb.Database">
<em class="property">class </em><code class="descclassname">pulumi_azure.mariadb.</code><code class="descname">Database</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>charset=None</em>, <em>collation=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>server_name=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a MariaDB Database within a MariaDB Server</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>charset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Charset for the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/setting-character-sets-and-collations">to be a valid MariaDB Charset</a>. Changing this forces a new resource to be created.</li>
<li><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Collation for the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/setting-character-sets-and-collations">to be a valid MariaDB Collation</a>. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/identifier-names/">to be a valid MariaDB identifier</a>. Changing this forces a
new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.</li>
<li><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_database.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_database.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.mariadb.Database.charset">
<code class="descname">charset</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Database.charset" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Charset for the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/setting-character-sets-and-collations">to be a valid MariaDB Charset</a>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Database.collation">
<code class="descname">collation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Database.collation" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Collation for the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/setting-character-sets-and-collations">to be a valid MariaDB Collation</a>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Database.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/identifier-names/">to be a valid MariaDB identifier</a>. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Database.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Database.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Database.server_name">
<code class="descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Database.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azure.mariadb.Database.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>charset=None</em>, <em>collation=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>server_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] charset: Specifies the Charset for the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/setting-character-sets-and-collations">to be a valid MariaDB Charset</a>. Changing this forces a new resource to be created.
:param pulumi.Input[str] collation: Specifies the Collation for the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/setting-character-sets-and-collations">to be a valid MariaDB Collation</a>. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specifies the name of the MariaDB Database, which needs <a class="reference external" href="https://mariadb.com/kb/en/library/identifier-names/">to be a valid MariaDB identifier</a>. Changing this forces a</p>
<blockquote>
<div>new resource to be created.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.</li>
<li><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_database.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_database.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mariadb.Database.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.Database.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.FirewallRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.mariadb.</code><code class="descname">FirewallRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>end_ip_address=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>server_name=None</em>, <em>start_ip_address=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Firewall Rule for a MariaDB Server</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>end_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Firewall Rule. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.</li>
<li><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</li>
<li><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_firewall_rule.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.mariadb.FirewallRule.end_ip_address">
<code class="descname">end_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.end_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.FirewallRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MariaDB Firewall Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.FirewallRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.FirewallRule.server_name">
<code class="descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.FirewallRule.start_ip_address">
<code class="descname">start_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.start_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azure.mariadb.FirewallRule.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>end_ip_address=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>server_name=None</em>, <em>start_ip_address=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] end_ip_address: Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specifies the name of the MariaDB Firewall Rule. Changing this forces a new resource to be created.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which the MariaDB Server exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] server_name: Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.
:param pulumi.Input[str] start_ip_address: Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_firewall_rule.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mariadb.FirewallRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.FirewallRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.Server">
<em class="property">class </em><code class="descclassname">pulumi_azure.mariadb.</code><code class="descname">Server</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>administrator_login=None</em>, <em>administrator_login_password=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>ssl_enforcement=None</em>, <em>storage_profile=None</em>, <em>tags=None</em>, <em>version=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Server" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a MariaDB Server.</p>
<blockquote>
<div><strong>NOTE</strong> MariaDB Server is currently in Public Preview. You can find more information, including <a class="reference external" href="https://azure.microsoft.com/en-us/updates/mariadb-public-preview/">how to register for the Public Preview here</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>administrator_login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Administrator Login for the MariaDB Server. Changing this forces a new resource to be created.</li>
<li><strong>administrator_login_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> for the MariaDB Server.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the MariaDB Server. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</li>
<li><strong>ssl_enforcement</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if SSL should be enforced on connections. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</li>
<li><strong>storage_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_profile</span></code> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of MariaDB to use. The valid value is <code class="docutils literal notranslate"><span class="pre">10.2</span></code>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_server.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_server.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.administrator_login">
<code class="descname">administrator_login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.administrator_login" title="Permalink to this definition">¶</a></dt>
<dd><p>The Administrator Login for the MariaDB Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.administrator_login_password">
<code class="descname">administrator_login_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.administrator_login_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> for the MariaDB Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.fqdn">
<code class="descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the MariaDB Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the MariaDB Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.ssl_enforcement">
<code class="descname">ssl_enforcement</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.ssl_enforcement" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if SSL should be enforced on connections. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.storage_profile">
<code class="descname">storage_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.storage_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_profile</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.mariadb.Server.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.mariadb.Server.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the version of MariaDB to use. The valid value is <code class="docutils literal notranslate"><span class="pre">10.2</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azure.mariadb.Server.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>administrator_login=None</em>, <em>administrator_login_password=None</em>, <em>fqdn=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>ssl_enforcement=None</em>, <em>storage_profile=None</em>, <em>tags=None</em>, <em>version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Server.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Server resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] administrator_login: The Administrator Login for the MariaDB Server. Changing this forces a new resource to be created.
:param pulumi.Input[str] administrator_login_password: The Password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> for the MariaDB Server.
:param pulumi.Input[str] fqdn: The FQDN of the MariaDB Server.
:param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specifies the name of the MariaDB Server. Changing this forces a new resource to be created.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the MariaDB Server. Changing this forces a new resource to be created.
:param pulumi.Input[dict] sku: A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.
:param pulumi.Input[str] ssl_enforcement: Specifies if SSL should be enforced on connections. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.
:param pulumi.Input[dict] storage_profile: A <code class="docutils literal notranslate"><span class="pre">storage_profile</span></code> block as defined below.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
:param pulumi.Input[str] version: Specifies the version of MariaDB to use. The valid value is <code class="docutils literal notranslate"><span class="pre">10.2</span></code>. Changing this forces a new resource to be created.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_server.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/mariadb_server.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.mariadb.Server.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Server.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.Server.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Server.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
