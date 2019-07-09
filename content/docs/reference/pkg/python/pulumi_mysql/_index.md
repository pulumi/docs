---
---

<div class="section" id="module-pulumi_mysql">
<span id="pulumi-mysql"></span><h1>Pulumi MySQL<a class="headerlink" href="#module-pulumi_mysql" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_mysql.Database">
<em class="property">class </em><code class="descclassname">pulumi_mysql.</code><code class="descname">Database</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>default_character_set=None</em>, <em>default_collation=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">mysql_database</span></code> resource creates and manages a database on a MySQL
server.</p>
<blockquote>
<div><strong>Caution:</strong> The <code class="docutils literal notranslate"><span class="pre">mysql_database</span></code> resource can completely delete your
database just as easily as it can create it. To avoid costly accidents,
consider setting
<cite>``prevent_destroy`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/configuration/resources.html#prevent_destroy">https://www.terraform.io/docs/configuration/resources.html#prevent_destroy</a>&gt;`_
on your database resources as an extra safety measure.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>default_character_set</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default character set to use when
a table is created without specifying an explicit character set. Defaults
to “utf8”.</li>
<li><strong>default_collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default collation to use when a table
is created without specifying an explicit collation. Defaults to
<code class="docutils literal notranslate"><span class="pre">utf8_general_ci</span></code>. Each character set has its own set of collations, so
changing the character set requires also changing the collation.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database. This must be unique within
a given MySQL server and may or may not be case-sensitive depending on
the operating system on which the MySQL server is running.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/database.html.markdown">https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/database.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_mysql.Database.default_character_set">
<code class="descname">default_character_set</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.Database.default_character_set" title="Permalink to this definition">¶</a></dt>
<dd><p>The default character set to use when
a table is created without specifying an explicit character set. Defaults
to “utf8”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.Database.default_collation">
<code class="descname">default_collation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.Database.default_collation" title="Permalink to this definition">¶</a></dt>
<dd><p>The default collation to use when a table
is created without specifying an explicit collation. Defaults to
<code class="docutils literal notranslate"><span class="pre">utf8_general_ci</span></code>. Each character set has its own set of collations, so
changing the character set requires also changing the collation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.Database.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database. This must be unique within
a given MySQL server and may or may not be case-sensitive depending on
the operating system on which the MySQL server is running.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mysql.Database.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.Database.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.Grant">
<em class="property">class </em><code class="descclassname">pulumi_mysql.</code><code class="descname">Grant</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>database=None</em>, <em>grant=None</em>, <em>host=None</em>, <em>privileges=None</em>, <em>role=None</em>, <em>roles=None</em>, <em>table=None</em>, <em>tls_option=None</em>, <em>user=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Grant" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">mysql_grant</span></code> resource creates and manages privileges given to
a user on a MySQL server.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant privileges on.</li>
<li><strong>grant</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to also give the user privileges to grant the same privileges to other users.</li>
<li><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source host of the user. Defaults to “localhost”. Conflicts with <code class="docutils literal notranslate"><span class="pre">role</span></code>.</li>
<li><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of privileges to grant to the user. Refer to a list of privileges (such as <a class="reference external" href="https://dev.mysql.com/doc/refman/5.5/en/grant.html">here</a>) for applicable privileges. Conflicts with <code class="docutils literal notranslate"><span class="pre">roles</span></code>.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role to grant <code class="docutils literal notranslate"><span class="pre">privileges</span></code> to. Conflicts with <code class="docutils literal notranslate"><span class="pre">user</span></code> and <code class="docutils literal notranslate"><span class="pre">host</span></code>.</li>
<li><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of rols to grant to the user. Conflicts with <code class="docutils literal notranslate"><span class="pre">privileges</span></code>.</li>
<li><strong>table</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which table to grant <code class="docutils literal notranslate"><span class="pre">privileges</span></code> on. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>, which is all tables.</li>
<li><strong>tls_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An TLS-Option for the <code class="docutils literal notranslate"><span class="pre">GRANT</span></code> statement. The value is suffixed to <code class="docutils literal notranslate"><span class="pre">REQUIRE</span></code>. A value of ‘SSL’ will generate a <code class="docutils literal notranslate"><span class="pre">GRANT</span> <span class="pre">...</span> <span class="pre">REQUIRE</span> <span class="pre">SSL</span></code> statement. See the <cite>MYSQL ``GRANT`</cite> documentation &lt;<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/grant.html">https://dev.mysql.com/doc/refman/5.7/en/grant.html</a>&gt;`_ for more. Ignored if MySQL version is under 5.7.0.</li>
<li><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user. Conflicts with <code class="docutils literal notranslate"><span class="pre">role</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/grant.html.markdown">https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/grant.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_mysql.Grant.database">
<code class="descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.Grant.database" title="Permalink to this definition">¶</a></dt>
<dd><p>The database to grant privileges on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.Grant.grant">
<code class="descname">grant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.Grant.grant" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to also give the user privileges to grant the same privileges to other users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.Grant.host">
<code class="descname">host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.Grant.host" title="Permalink to this definition">¶</a></dt>
<dd><p>The source host of the user. Defaults to “localhost”. Conflicts with <code class="docutils literal notranslate"><span class="pre">role</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.Grant.privileges">
<code class="descname">privileges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.Grant.privileges" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of privileges to grant to the user. Refer to a list of privileges (such as <a class="reference external" href="https://dev.mysql.com/doc/refman/5.5/en/grant.html">here</a>) for applicable privileges. Conflicts with <code class="docutils literal notranslate"><span class="pre">roles</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.Grant.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.Grant.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role to grant <code class="docutils literal notranslate"><span class="pre">privileges</span></code> to. Conflicts with <code class="docutils literal notranslate"><span class="pre">user</span></code> and <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.Grant.roles">
<code class="descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.Grant.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of rols to grant to the user. Conflicts with <code class="docutils literal notranslate"><span class="pre">privileges</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.Grant.table">
<code class="descname">table</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.Grant.table" title="Permalink to this definition">¶</a></dt>
<dd><p>Which table to grant <code class="docutils literal notranslate"><span class="pre">privileges</span></code> on. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>, which is all tables.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.Grant.tls_option">
<code class="descname">tls_option</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.Grant.tls_option" title="Permalink to this definition">¶</a></dt>
<dd><p>An TLS-Option for the <code class="docutils literal notranslate"><span class="pre">GRANT</span></code> statement. The value is suffixed to <code class="docutils literal notranslate"><span class="pre">REQUIRE</span></code>. A value of ‘SSL’ will generate a <code class="docutils literal notranslate"><span class="pre">GRANT</span> <span class="pre">...</span> <span class="pre">REQUIRE</span> <span class="pre">SSL</span></code> statement. See the <cite>MYSQL ``GRANT`</cite> documentation &lt;<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/grant.html">https://dev.mysql.com/doc/refman/5.7/en/grant.html</a>&gt;`_ for more. Ignored if MySQL version is under 5.7.0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.Grant.user">
<code class="descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.Grant.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user. Conflicts with <code class="docutils literal notranslate"><span class="pre">role</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mysql.Grant.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Grant.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.Grant.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Grant.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.Provider">
<em class="property">class </em><code class="descclassname">pulumi_mysql.</code><code class="descname">Provider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>endpoint=None</em>, <em>password=None</em>, <em>tls=None</em>, <em>username=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the mysql package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://pulumi.io/reference/programming-model.html#providers">documentation</a> for more information.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/index.html.markdown</a>.</div></blockquote>
<dl class="method">
<dt id="pulumi_mysql.Provider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.Provider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.Role">
<em class="property">class </em><code class="descclassname">pulumi_mysql.</code><code class="descname">Role</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">mysql_role</span></code> resource creates and manages a user on a MySQL
server.</p>
<blockquote>
<div><strong>Note:</strong> MySQL introduced roles in version 8. They do not work on MySQL 5 and lower.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/role.html.markdown">https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/role.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_mysql.Role.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.Role.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mysql.Role.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Role.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.Role.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Role.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.User">
<em class="property">class </em><code class="descclassname">pulumi_mysql.</code><code class="descname">User</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auth_plugin=None</em>, <em>host=None</em>, <em>password=None</em>, <em>plaintext_password=None</em>, <em>tls_option=None</em>, <em>user=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.User" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">mysql_user</span></code> resource creates and manages a user on a MySQL
server.</p>
<blockquote>
<div><strong>Note:</strong> The password for the user is provided in plain text, and is
obscured by an unsalted hash in the state
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.
Care is required when using this resource, to avoid disclosing the password.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>auth_plugin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code>.<span class="raw-html-m2r"><br></span></li>
<li><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source host of the user. Defaults to “localhost”.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Deprecated alias of <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code>, whose value is <em>stored as plaintext in state</em>. Prefer to use <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code> instead, which stores the password as an unsalted hash. Conflicts with <code class="docutils literal notranslate"><span class="pre">auth_plugin</span></code>.</li>
<li><strong>plaintext_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the user. This must be provided in plain text, so the data source for it must be secured. An <em>unsalted</em> hash of the provided password is stored in state. Conflicts with <code class="docutils literal notranslate"><span class="pre">auth_plugin</span></code>.</li>
<li><strong>tls_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An TLS-Option for the <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">USER</span></code> or <code class="docutils literal notranslate"><span class="pre">ALTER</span> <span class="pre">USER</span></code> statement. The value is suffixed to <code class="docutils literal notranslate"><span class="pre">REQUIRE</span></code>. A value of ‘SSL’ will generate a <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">USER</span> <span class="pre">...</span> <span class="pre">REQUIRE</span> <span class="pre">SSL</span></code> statement. See the <cite>MYSQL ``CREATE USER`</cite> documentation &lt;<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/create-user.html">https://dev.mysql.com/doc/refman/5.7/en/create-user.html</a>&gt;`_ for more. Ignored if MySQL version is under 5.7.0.</li>
<li><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/user.html.markdown">https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/user.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_mysql.User.auth_plugin">
<code class="descname">auth_plugin</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.User.auth_plugin" title="Permalink to this definition">¶</a></dt>
<dd><p>Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.User.host">
<code class="descname">host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.User.host" title="Permalink to this definition">¶</a></dt>
<dd><p>The source host of the user. Defaults to “localhost”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.User.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Deprecated alias of <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code>, whose value is <em>stored as plaintext in state</em>. Prefer to use <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code> instead, which stores the password as an unsalted hash. Conflicts with <code class="docutils literal notranslate"><span class="pre">auth_plugin</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.User.plaintext_password">
<code class="descname">plaintext_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.User.plaintext_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password for the user. This must be provided in plain text, so the data source for it must be secured. An <em>unsalted</em> hash of the provided password is stored in state. Conflicts with <code class="docutils literal notranslate"><span class="pre">auth_plugin</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.User.tls_option">
<code class="descname">tls_option</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.User.tls_option" title="Permalink to this definition">¶</a></dt>
<dd><p>An TLS-Option for the <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">USER</span></code> or <code class="docutils literal notranslate"><span class="pre">ALTER</span> <span class="pre">USER</span></code> statement. The value is suffixed to <code class="docutils literal notranslate"><span class="pre">REQUIRE</span></code>. A value of ‘SSL’ will generate a <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">USER</span> <span class="pre">...</span> <span class="pre">REQUIRE</span> <span class="pre">SSL</span></code> statement. See the <cite>MYSQL ``CREATE USER`</cite> documentation &lt;<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/create-user.html">https://dev.mysql.com/doc/refman/5.7/en/create-user.html</a>&gt;`_ for more. Ignored if MySQL version is under 5.7.0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.User.user">
<code class="descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.User.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mysql.User.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.User.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.UserPassword">
<em class="property">class </em><code class="descclassname">pulumi_mysql.</code><code class="descname">UserPassword</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>host=None</em>, <em>pgp_key=None</em>, <em>user=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.UserPassword" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a UserPassword resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source host of the user. Defaults to <code class="docutils literal notranslate"><span class="pre">localhost</span></code>.</li>
<li><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Either a base-64 encoded PGP public key, or a keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:some_person_that_exists</span></code>.</li>
<li><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM user to associate with this access key.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/user_password.html.markdown">https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/user_password.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_mysql.UserPassword.encrypted_password">
<code class="descname">encrypted_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.UserPassword.encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The encrypted password, base64 encoded.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.UserPassword.host">
<code class="descname">host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.UserPassword.host" title="Permalink to this definition">¶</a></dt>
<dd><p>The source host of the user. Defaults to <code class="docutils literal notranslate"><span class="pre">localhost</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.UserPassword.key_fingerprint">
<code class="descname">key_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.UserPassword.key_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the PGP key used to encrypt the password</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.UserPassword.pgp_key">
<code class="descname">pgp_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.UserPassword.pgp_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Either a base-64 encoded PGP public key, or a keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:some_person_that_exists</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_mysql.UserPassword.user">
<code class="descname">user</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_mysql.UserPassword.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM user to associate with this access key.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_mysql.UserPassword.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.UserPassword.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.UserPassword.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.UserPassword.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
