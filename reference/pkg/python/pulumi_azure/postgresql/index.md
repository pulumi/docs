<div class="section" id="module-pulumi_azure.postgresql">
<span id="postgresql"></span><h1>postgresql<a class="headerlink" href="#module-pulumi_azure.postgresql" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.postgresql.Configuration">
<em class="property">class </em><code class="descclassname">pulumi_azure.postgresql.</code><code class="descname">Configuration</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>server_name=None</em>, <em>value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets a PostgreSQL Configuration value on a PostgreSQL Server.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Configuration, which needs [to be a valid PostgreSQL configuration name](<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIER">https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIER</a>). Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</li>
<li><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the value of the PostgreSQL Configuration. See the PostgreSQL documentation for valid values.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.postgresql.Configuration.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Configuration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the PostgreSQL Configuration, which needs [to be a valid PostgreSQL configuration name](<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIER">https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIER</a>). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Configuration.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Configuration.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Configuration.server_name">
<code class="descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Configuration.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Configuration.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Configuration.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the value of the PostgreSQL Configuration. See the PostgreSQL documentation for valid values.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.Configuration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Configuration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.Configuration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Configuration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.Database">
<em class="property">class </em><code class="descclassname">pulumi_azure.postgresql.</code><code class="descname">Database</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>charset=None</em>, <em>collation=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>server_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a PostgreSQL Database within a PostgreSQL Server</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>charset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Charset for the PostgreSQL Database, which needs [to be a valid PostgreSQL Charset](<a class="reference external" href="https://www.postgresql.org/docs/current/static/multibyte.html">https://www.postgresql.org/docs/current/static/multibyte.html</a>). Changing this forces a new resource to be created.</li>
<li><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Collation for the PostgreSQL Database, which needs [to be a valid PostgreSQL Collation](<a class="reference external" href="https://www.postgresql.org/docs/current/static/collation.html">https://www.postgresql.org/docs/current/static/collation.html</a>). Note that Microsoft uses different [notation](<a class="reference external" href="https://msdn.microsoft.com/library/windows/desktop/dd373814.aspx">https://msdn.microsoft.com/library/windows/desktop/dd373814.aspx</a>) - en-US instead of en_US. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Database, which needs [to be a valid PostgreSQL identifier](<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS">https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS</a>). Changing this forces a
new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</li>
<li><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.postgresql.Database.charset">
<code class="descname">charset</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Database.charset" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Charset for the PostgreSQL Database, which needs [to be a valid PostgreSQL Charset](<a class="reference external" href="https://www.postgresql.org/docs/current/static/multibyte.html">https://www.postgresql.org/docs/current/static/multibyte.html</a>). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Database.collation">
<code class="descname">collation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Database.collation" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Collation for the PostgreSQL Database, which needs [to be a valid PostgreSQL Collation](<a class="reference external" href="https://www.postgresql.org/docs/current/static/collation.html">https://www.postgresql.org/docs/current/static/collation.html</a>). Note that Microsoft uses different [notation](<a class="reference external" href="https://msdn.microsoft.com/library/windows/desktop/dd373814.aspx">https://msdn.microsoft.com/library/windows/desktop/dd373814.aspx</a>) - en-US instead of en_US. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Database.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the PostgreSQL Database, which needs [to be a valid PostgreSQL identifier](<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS">https://www.postgresql.org/docs/current/static/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS</a>). Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Database.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Database.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Database.server_name">
<code class="descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Database.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.Database.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.Database.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.FirewallRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.postgresql.</code><code class="descname">FirewallRule</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>end_ip_address=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>server_name=None</em>, <em>start_ip_address=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Firewall Rule for a PostgreSQL Server</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>end_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Firewall Rule. Changing this forces a
new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</li>
<li><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</li>
<li><strong>start_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.postgresql.FirewallRule.end_ip_address">
<code class="descname">end_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.end_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the End IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.FirewallRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the PostgreSQL Firewall Rule. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.FirewallRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the PostgreSQL Server exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.FirewallRule.server_name">
<code class="descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the PostgreSQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.FirewallRule.start_ip_address">
<code class="descname">start_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.start_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Start IP Address associated with this Firewall Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.FirewallRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.FirewallRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.FirewallRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.Server">
<em class="property">class </em><code class="descclassname">pulumi_azure.postgresql.</code><code class="descname">Server</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>administrator_login=None</em>, <em>administrator_login_password=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>ssl_enforcement=None</em>, <em>storage_profile=None</em>, <em>tags=None</em>, <em>version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Server" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a PostgreSQL Server.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>administrator_login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Administrator Login for the PostgreSQL Server. Changing this forces a new resource to be created.</li>
<li><strong>administrator_login_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password associated with the <cite>administrator_login</cite> for the PostgreSQL Server.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the SKU Name for this PostgreSQL Server. The name of the SKU, follows the <cite>tier</cite> + <cite>family</cite> + <cite>cores</cite> pattern (e.g. B_Gen4_1, GP_Gen5_8). For more information see the [product documentation](<a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#sku">https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#sku</a>).</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the PostgreSQL Server. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>sku</cite> block as defined below.</li>
<li><strong>ssl_enforcement</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if SSL should be enforced on connections. Possible values are <cite>Enabled</cite> and <cite>Disabled</cite>.</li>
<li><strong>storage_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>storage_profile</cite> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of PostgreSQL to use. Valid values are <cite>9.5</cite>, <cite>9.6</cite>, and <cite>10.0</cite>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.administrator_login">
<code class="descname">administrator_login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.administrator_login" title="Permalink to this definition">¶</a></dt>
<dd><p>The Administrator Login for the PostgreSQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.administrator_login_password">
<code class="descname">administrator_login_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.administrator_login_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password associated with the <cite>administrator_login</cite> for the PostgreSQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.fqdn">
<code class="descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the PostgreSQL Server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the SKU Name for this PostgreSQL Server. The name of the SKU, follows the <cite>tier</cite> + <cite>family</cite> + <cite>cores</cite> pattern (e.g. B_Gen4_1, GP_Gen5_8). For more information see the [product documentation](<a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#sku">https://docs.microsoft.com/en-us/rest/api/postgresql/servers/create#sku</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the PostgreSQL Server. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>sku</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.ssl_enforcement">
<code class="descname">ssl_enforcement</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.ssl_enforcement" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if SSL should be enforced on connections. Possible values are <cite>Enabled</cite> and <cite>Disabled</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.storage_profile">
<code class="descname">storage_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.storage_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>storage_profile</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.Server.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.Server.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the version of PostgreSQL to use. Valid values are <cite>9.5</cite>, <cite>9.6</cite>, and <cite>10.0</cite>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.Server.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Server.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.Server.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.Server.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.VirtualNetworkRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.postgresql.</code><code class="descname">VirtualNetworkRule</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>ignore_missing_vnet_service_endpoint=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>server_name=None</em>, <em>subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a PostgreSQL Virtual Network Rule.</p>
<p>-&gt; <strong>NOTE:</strong> PostgreSQL Virtual Network Rules [can only be used with SKU Tiers of <cite>GeneralPurpose</cite> or <cite>MemoryOptimized</cite>](<a class="reference external" href="https://docs.microsoft.com/en-us/azure/postgresql/concepts-data-access-and-security-vnet">https://docs.microsoft.com/en-us/azure/postgresql/concepts-data-access-and-security-vnet</a>)</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ignore_missing_vnet_service_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled? Defaults to <cite>false</cite>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.</li>
<li><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet that the PostgreSQL server will be connected to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.ignore_missing_vnet_service_endpoint">
<code class="descname">ignore_missing_vnet_service_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.ignore_missing_vnet_service_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Virtual Network Rule be created before the Subnet has the Virtual Network Service Endpoint enabled? Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the PostgreSQL virtual network rule. Cannot be empty and must only contain alphanumeric characters and hyphens. Cannot start with a number, and cannot start or end with a hyphen. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group where the PostgreSQL server resides. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.server_name">
<code class="descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SQL Server to which this PostgreSQL virtual network rule will be applied to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the subnet that the PostgreSQL server will be connected to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.postgresql.VirtualNetworkRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.postgresql.VirtualNetworkRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
