---
title: Module postgresql
title_tag: Module postgresql | Package pulumi_azure | Python SDK
linktitle: postgresql
notitle: true
---

<div class="section" id="postgresql">
<h1>postgresql<a class="headerlink" href="#postgresql" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.postgresql"></span><dl class="class">
<dt id="pulumi_azure.postgresql.AwaitableGetServerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.postgresql.</code><code class="sig-name descname">AwaitableGetServerResult</code><span class="sig-paren">(</span><em class="sig-param">administrator_login=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.AwaitableGetServerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.postgresql.Configuration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.postgresql.</code><code class="sig-name descname">Configuration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets a PostgreSQL Configuration value on a PostgreSQL Server.</p>
<blockquote>
<div><p><strong>Note:</strong> Since this resource is provisioned by default, the Azure Provider will not check for the presence of an existing resource prior to attempting to create it.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/postgresql_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/postgresql_configuration.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Configuration, which needs <a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIER">to be a valid PostgreSQL configuration name</a>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the value of the PostgreSQL Configuration. See the PostgreSQL documentation for valid values.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.postgresql.Configuration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Configuration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the PostgreSQL Configuration, which needs <a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIER">to be a valid PostgreSQL configuration name</a>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Configuration.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Configuration.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Configuration.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Configuration.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Configuration.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Configuration.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the value of the PostgreSQL Configuration. See the PostgreSQL documentation for valid values.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.Configuration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Configuration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Configuration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the PostgreSQL Configuration, which needs <a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIER">to be a valid PostgreSQL configuration name</a>. Changing this forces a new resource to be created.</p>
</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the value of the PostgreSQL Configuration. See the PostgreSQL documentation for valid values.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.Configuration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Configuration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.Configuration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Configuration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.postgresql.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">charset=None</em>, <em class="sig-param">collation=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a PostgreSQL Database within a PostgreSQL Server</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/postgresql_database.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/postgresql_database.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>charset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Charset for the PostgreSQL Database, which needs <a class="reference external" href="https://www.postgresql.org/docs/current/static/multibyte.html">to be a valid PostgreSQL Charset</a>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Collation for the PostgreSQL Database, which needs <a class="reference external" href="https://www.postgresql.org/docs/current/static/collation.html">to be a valid PostgreSQL Collation</a>. Note that Microsoft uses different <a class="reference external" href="https://msdn.microsoft.com/library/windows/desktop/dd373814.aspx">notation</a> - en-US instead of en_US. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Database, which needs <a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS">to be a valid PostgreSQL identifier</a>. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.postgresql.Database.charset">
<code class="sig-name descname">charset</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Database.charset" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Charset for the PostgreSQL Database, which needs <a class="reference external" href="https://www.postgresql.org/docs/current/static/multibyte.html">to be a valid PostgreSQL Charset</a>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Database.collation">
<code class="sig-name descname">collation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Database.collation" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Collation for the PostgreSQL Database, which needs <a class="reference external" href="https://www.postgresql.org/docs/current/static/collation.html">to be a valid PostgreSQL Collation</a>. Note that Microsoft uses different <a class="reference external" href="https://msdn.microsoft.com/library/windows/desktop/dd373814.aspx">notation</a> - en-US instead of en_US. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Database.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the PostgreSQL Database, which needs <a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS">to be a valid PostgreSQL identifier</a>. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Database.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Database.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Database.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Database.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.Database.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">charset=None</em>, <em class="sig-param">collation=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>charset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the Charset for the PostgreSQL Database, which needs <a class="reference external" href="https://www.postgresql.org/docs/current/static/multibyte.html">to be a valid PostgreSQL Charset</a>. Changing this forces a new resource to be created.</p>
</p></li>
<li><p><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the Collation for the PostgreSQL Database, which needs <a class="reference external" href="https://www.postgresql.org/docs/current/static/collation.html">to be a valid PostgreSQL Collation</a>. Note that Microsoft uses different <a class="reference external" href="https://msdn.microsoft.com/library/windows/desktop/dd373814.aspx">notation</a> - en-US instead of en_US. Changing this forces a new resource to be created.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the PostgreSQL Database, which needs <a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS">to be a valid PostgreSQL identifier</a>. Changing this forces a
new resource to be created.</p>
</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.Database.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.Database.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.FirewallRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.postgresql.</code><code class="sig-name descname">FirewallRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">end_ip_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">start_ip_address=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Firewall Rule for a PostgreSQL Server</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/postgresql_firewall_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/postgresql_firewall_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Firewall Rule. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.postgresql.FirewallRule.end_ip_address">
<code class="sig-name descname">end_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.end_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.FirewallRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the PostgreSQL Firewall Rule. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.FirewallRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.FirewallRule.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.FirewallRule.start_ip_address">
<code class="sig-name descname">start_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.start_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.FirewallRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">end_ip_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">start_ip_address=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Firewall Rule. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.FirewallRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.FirewallRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.GetServerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.postgresql.</code><code class="sig-name descname">GetServerResult</code><span class="sig-paren">(</span><em class="sig-param">administrator_login=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.GetServerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServer.</p>
<dl class="attribute">
<dt id="pulumi_azure.postgresql.GetServerResult.administrator_login">
<code class="sig-name descname">administrator_login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.GetServerResult.administrator_login" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrator username of the PostgreSQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.GetServerResult.fqdn">
<code class="sig-name descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.GetServerResult.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully qualified domain name of the PostgreSQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.GetServerResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.GetServerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.GetServerResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.GetServerResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the Resource Group in which the PostgreSQL Server exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.GetServerResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.GetServerResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.GetServerResult.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.GetServerResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the PostgreSQL Server.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.postgresql.Server">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.postgresql.</code><code class="sig-name descname">Server</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">administrator_login=None</em>, <em class="sig-param">administrator_login_password=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">ssl_enforcement=None</em>, <em class="sig-param">storage_profile=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Server" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a PostgreSQL Server.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/postgresql_server.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/postgresql_server.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>administrator_login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Administrator Login for the PostgreSQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>administrator_login_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> for the PostgreSQL Server.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the PostgreSQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the SKU Name for this PostgreSQL Server. The name of the SKU, follows the <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> + <code class="docutils literal notranslate"><span class="pre">cores</span></code> pattern (e.g. <code class="docutils literal notranslate"><span class="pre">B_Gen4_1</span></code>, <code class="docutils literal notranslate"><span class="pre">GP_Gen5_8</span></code>). For more information see the <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#sku">product documentation</a>.</p></li>
<li><p><strong>ssl_enforcement</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if SSL should be enforced on connections. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
<li><p><strong>storage_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_profile</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of PostgreSQL to use. Valid values are <code class="docutils literal notranslate"><span class="pre">9.5</span></code>, <code class="docutils literal notranslate"><span class="pre">9.6</span></code>, <code class="docutils literal notranslate"><span class="pre">10</span></code>, <code class="docutils literal notranslate"><span class="pre">10.0</span></code>, and <code class="docutils literal notranslate"><span class="pre">11</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>storage_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoGrow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Enable/Disable auto-growing of the storage. Valid values for this property are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Storage auto-grow prevents your server from running out of storage and becoming read-only. If storage auto grow is enabled, the storage automatically grows without impacting the workload. The default value if not explicitly specified is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupRetentionDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Backup retention days for the server, supported values are between <code class="docutils literal notranslate"><span class="pre">7</span></code> and <code class="docutils literal notranslate"><span class="pre">35</span></code> days.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoRedundantBackup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Enable/Disable Geo-redundant for server backup. Valid values for this property are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, not supported for the <code class="docutils literal notranslate"><span class="pre">basic</span></code> tier.  This allows you to choose between locally redundant or geo-redundant backup storage in the General Purpose and Memory Optimized tiers. When the backups are stored in geo-redundant backup storage, they are not only stored within the region in which your server is hosted, but are also replicated to a paired data center. This provides better protection and ability to restore your server in a different region in the event of a disaster. The Basic tier only offers locally redundant backup storage.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageMb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Max storage allowed for a server. Possible values are between <code class="docutils literal notranslate"><span class="pre">5120</span></code> MB(5GB) and <code class="docutils literal notranslate"><span class="pre">1048576</span></code> MB(1TB) for the Basic SKU and between <code class="docutils literal notranslate"><span class="pre">5120</span></code> MB(5GB) and <code class="docutils literal notranslate"><span class="pre">4194304</span></code> MB(4TB) for General Purpose/Memory Optimized SKUs. For more information see the <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#StorageProfile">product documentation</a>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.administrator_login">
<code class="sig-name descname">administrator_login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.administrator_login" title="Permalink to this definition">¶</a></dt>
<dd><p>The Administrator Login for the PostgreSQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.administrator_login_password">
<code class="sig-name descname">administrator_login_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.administrator_login_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> for the PostgreSQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.fqdn">
<code class="sig-name descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the PostgreSQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the PostgreSQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the SKU Name for this PostgreSQL Server. The name of the SKU, follows the <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> + <code class="docutils literal notranslate"><span class="pre">cores</span></code> pattern (e.g. <code class="docutils literal notranslate"><span class="pre">B_Gen4_1</span></code>, <code class="docutils literal notranslate"><span class="pre">GP_Gen5_8</span></code>). For more information see the <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#sku">product documentation</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.ssl_enforcement">
<code class="sig-name descname">ssl_enforcement</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.ssl_enforcement" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if SSL should be enforced on connections. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.storage_profile">
<code class="sig-name descname">storage_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.storage_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_profile</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoGrow</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Enable/Disable auto-growing of the storage. Valid values for this property are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Storage auto-grow prevents your server from running out of storage and becoming read-only. If storage auto grow is enabled, the storage automatically grows without impacting the workload. The default value if not explicitly specified is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupRetentionDays</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Backup retention days for the server, supported values are between <code class="docutils literal notranslate"><span class="pre">7</span></code> and <code class="docutils literal notranslate"><span class="pre">35</span></code> days.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoRedundantBackup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Enable/Disable Geo-redundant for server backup. Valid values for this property are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, not supported for the <code class="docutils literal notranslate"><span class="pre">basic</span></code> tier.  This allows you to choose between locally redundant or geo-redundant backup storage in the General Purpose and Memory Optimized tiers. When the backups are stored in geo-redundant backup storage, they are not only stored within the region in which your server is hosted, but are also replicated to a paired data center. This provides better protection and ability to restore your server in a different region in the event of a disaster. The Basic tier only offers locally redundant backup storage.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageMb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Max storage allowed for a server. Possible values are between <code class="docutils literal notranslate"><span class="pre">5120</span></code> MB(5GB) and <code class="docutils literal notranslate"><span class="pre">1048576</span></code> MB(1TB) for the Basic SKU and between <code class="docutils literal notranslate"><span class="pre">5120</span></code> MB(5GB) and <code class="docutils literal notranslate"><span class="pre">4194304</span></code> MB(4TB) for General Purpose/Memory Optimized SKUs. For more information see the <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#StorageProfile">product documentation</a>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the version of PostgreSQL to use. Valid values are <code class="docutils literal notranslate"><span class="pre">9.5</span></code>, <code class="docutils literal notranslate"><span class="pre">9.6</span></code>, <code class="docutils literal notranslate"><span class="pre">10</span></code>, <code class="docutils literal notranslate"><span class="pre">10.0</span></code>, and <code class="docutils literal notranslate"><span class="pre">11</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.Server.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">administrator_login=None</em>, <em class="sig-param">administrator_login_password=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">ssl_enforcement=None</em>, <em class="sig-param">storage_profile=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Server.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Server resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>administrator_login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Administrator Login for the PostgreSQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>administrator_login_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password associated with the <code class="docutils literal notranslate"><span class="pre">administrator_login</span></code> for the PostgreSQL Server.</p></li>
<li><p><strong>fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN of the PostgreSQL Server.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the PostgreSQL Server. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the SKU Name for this PostgreSQL Server. The name of the SKU, follows the <code class="docutils literal notranslate"><span class="pre">tier</span></code> + <code class="docutils literal notranslate"><span class="pre">family</span></code> + <code class="docutils literal notranslate"><span class="pre">cores</span></code> pattern (e.g. <code class="docutils literal notranslate"><span class="pre">B_Gen4_1</span></code>, <code class="docutils literal notranslate"><span class="pre">GP_Gen5_8</span></code>). For more information see the <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#sku">product documentation</a>.</p>
</p></li>
<li><p><strong>ssl_enforcement</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if SSL should be enforced on connections. Possible values are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>.</p></li>
<li><p><strong>storage_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_profile</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of PostgreSQL to use. Valid values are <code class="docutils literal notranslate"><span class="pre">9.5</span></code>, <code class="docutils literal notranslate"><span class="pre">9.6</span></code>, <code class="docutils literal notranslate"><span class="pre">10</span></code>, <code class="docutils literal notranslate"><span class="pre">10.0</span></code>, and <code class="docutils literal notranslate"><span class="pre">11</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>storage_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoGrow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Enable/Disable auto-growing of the storage. Valid values for this property are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Storage auto-grow prevents your server from running out of storage and becoming read-only. If storage auto grow is enabled, the storage automatically grows without impacting the workload. The default value if not explicitly specified is <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupRetentionDays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Backup retention days for the server, supported values are between <code class="docutils literal notranslate"><span class="pre">7</span></code> and <code class="docutils literal notranslate"><span class="pre">35</span></code> days.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">geoRedundantBackup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Enable/Disable Geo-redundant for server backup. Valid values for this property are <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, not supported for the <code class="docutils literal notranslate"><span class="pre">basic</span></code> tier.  This allows you to choose between locally redundant or geo-redundant backup storage in the General Purpose and Memory Optimized tiers. When the backups are stored in geo-redundant backup storage, they are not only stored within the region in which your server is hosted, but are also replicated to a paired data center. This provides better protection and ability to restore your server in a different region in the event of a disaster. The Basic tier only offers locally redundant backup storage.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageMb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Max storage allowed for a server. Possible values are between <code class="docutils literal notranslate"><span class="pre">5120</span></code> MB(5GB) and <code class="docutils literal notranslate"><span class="pre">1048576</span></code> MB(1TB) for the Basic SKU and between <code class="docutils literal notranslate"><span class="pre">5120</span></code> MB(5GB) and <code class="docutils literal notranslate"><span class="pre">4194304</span></code> MB(4TB) for General Purpose/Memory Optimized SKUs. For more information see the <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#StorageProfile">product documentation</a>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.Server.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Server.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.Server.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Server.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.VirtualNetworkRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.postgresql.</code><code class="sig-name descname">VirtualNetworkRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ignore_missing_vnet_service_endpoint=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a PostgreSQL Virtual Network Rule.</p>
<blockquote>
<div><p><strong>NOTE:</strong> PostgreSQL Virtual Network Rules <cite>can only be used with SKU Tiers of ``GeneralPurpose`</cite> or <code class="docutils literal notranslate"><span class="pre">MemoryOptimized</span></code> &lt;<a class="reference external" href="https://docs.microsoft.com/en-us/azure/postgresql/concepts-data-access-and-security-vnet">https://docs.microsoft.com/en-us/azure/postgresql/concepts-data-access-and-security-vnet</a>&gt;`_</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/postgresql_virtual_network_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/postgresql_virtual_network_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ignore_missing_vnet_service_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet that the PostgreSQL server will be connected to.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.ignore_missing_vnet_service_endpoint">
<code class="sig-name descname">ignore_missing_vnet_service_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.ignore_missing_vnet_service_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.server_name">
<code class="sig-name descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the subnet that the PostgreSQL server will be connected to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ignore_missing_vnet_service_endpoint=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">server_name=None</em>, <em class="sig-param">subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualNetworkRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ignore_missing_vnet_service_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.</p></li>
<li><p><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet that the PostgreSQL server will be connected to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.get_server">
<code class="sig-prename descclassname">pulumi_azure.postgresql.</code><code class="sig-name descname">get_server</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.get_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing PostgreSQL Azure Database Server.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/postgresql_server.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/postgresql_server.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the PostgreSQL Server.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the Resource Group where the PostgreSQL Server exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
