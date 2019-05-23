<div class="section" id="module-pulumi_azure.mariadb">
<span id="mariadb"></span><h1>mariadb<a class="headerlink" href="#module-pulumi_azure.mariadb" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.mariadb.Database">
<em class="property">class </em><code class="descclassname">pulumi_azure.mariadb.</code><code class="descname">Database</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>charset=None</em>, <em>collation=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>server_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Database" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.mariadb.Server">
<em class="property">class </em><code class="descclassname">pulumi_azure.mariadb.</code><code class="descname">Server</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>administrator_login=None</em>, <em>administrator_login_password=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>ssl_enforcement=None</em>, <em>storage_profile=None</em>, <em>tags=None</em>, <em>version=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.mariadb.Server" title="Permalink to this definition">¶</a></dt>
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
