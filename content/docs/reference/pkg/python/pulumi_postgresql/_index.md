---
---

<div class="section" id="module-pulumi_postgresql">
<span id="pulumi-postgresql"></span><h1>Pulumi PostgreSQL<a class="headerlink" href="#module-pulumi_postgresql" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_postgresql.Database">
<em class="property">class </em><code class="descclassname">pulumi_postgresql.</code><code class="descname">Database</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allow_connections=None</em>, <em>connection_limit=None</em>, <em>encoding=None</em>, <em>is_template=None</em>, <em>lc_collate=None</em>, <em>lc_ctype=None</em>, <em>name=None</em>, <em>owner=None</em>, <em>tablespace_name=None</em>, <em>template=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">postgresql_database</span></code> resource creates and manages <a class="reference external" href="https://www.postgresql.org/docs/current/static/managing-databases.html">database
objects</a>
within a PostgreSQL server instance.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allow_connections</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">false</span></code> then no one can connect to this
database. The default is <code class="docutils literal notranslate"><span class="pre">true</span></code>, allowing connections (except as restricted by
other mechanisms, such as <code class="docutils literal notranslate"><span class="pre">GRANT</span></code> or <code class="docutils literal notranslate"><span class="pre">REVOKE</span> <span class="pre">CONNECT</span></code>).</li>
<li><strong>connection_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How many concurrent connections can be
established to this database. <code class="docutils literal notranslate"><span class="pre">-1</span></code> (the default) means no limit.</li>
<li><strong>is_template</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, then this database can be cloned by any
user with <code class="docutils literal notranslate"><span class="pre">CREATEDB</span></code> privileges; if <code class="docutils literal notranslate"><span class="pre">false</span></code> (the default), then only
superusers or the owner of the database can clone it.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database. Must be unique on the PostgreSQL
server instance where it is configured.</li>
<li><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role name of the user who will own the database, or
<code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code> to use the default (namely, the user executing the command). To
create a database owned by another role or to change the owner of an existing
database, you must be a direct or indirect member of the specified role, or
the username in the provider is a superuser.</li>
<li><strong>tablespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the tablespace that will be
associated with the database, or <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code> to use the template database’s
tablespace.  This tablespace will be the default tablespace used for objects
created in this database.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/database.html.markdown">https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/database.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_postgresql.Database.allow_connections">
<code class="descname">allow_connections</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.allow_connections" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code> then no one can connect to this
database. The default is <code class="docutils literal notranslate"><span class="pre">true</span></code>, allowing connections (except as restricted by
other mechanisms, such as <code class="docutils literal notranslate"><span class="pre">GRANT</span></code> or <code class="docutils literal notranslate"><span class="pre">REVOKE</span> <span class="pre">CONNECT</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Database.connection_limit">
<code class="descname">connection_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.connection_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>How many concurrent connections can be
established to this database. <code class="docutils literal notranslate"><span class="pre">-1</span></code> (the default) means no limit.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Database.is_template">
<code class="descname">is_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.is_template" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, then this database can be cloned by any
user with <code class="docutils literal notranslate"><span class="pre">CREATEDB</span></code> privileges; if <code class="docutils literal notranslate"><span class="pre">false</span></code> (the default), then only
superusers or the owner of the database can clone it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Database.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database. Must be unique on the PostgreSQL
server instance where it is configured.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Database.owner">
<code class="descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The role name of the user who will own the database, or
<code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code> to use the default (namely, the user executing the command). To
create a database owned by another role or to change the owner of an existing
database, you must be a direct or indirect member of the specified role, or
the username in the provider is a superuser.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Database.tablespace_name">
<code class="descname">tablespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.tablespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the tablespace that will be
associated with the database, or <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code> to use the template database’s
tablespace.  This tablespace will be the default tablespace used for objects
created in this database.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Database.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Database.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.DefaultPrivileg">
<em class="property">class </em><code class="descclassname">pulumi_postgresql.</code><code class="descname">DefaultPrivileg</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>database=None</em>, <em>object_type=None</em>, <em>owner=None</em>, <em>privileges=None</em>, <em>role=None</em>, <em>schema=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">postgresql_default_privileges</span></code> resource creates and manages default privileges given to a user for a database schema.</p>
<blockquote>
<div><strong>Note:</strong> This resource needs Postgresql version 9 or above.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant default privileges for this role.</li>
<li><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PostgreSQL object type to set the default privileges on (one of: table, sequence).</li>
<li><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).</li>
<li><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of privileges to apply as default privileges.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to which grant default privileges on.</li>
<li><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database schema to set default privileges for this role.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/default_privileges.html.markdown">https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/default_privileges.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileg.database">
<code class="descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.database" title="Permalink to this definition">¶</a></dt>
<dd><p>The database to grant default privileges for this role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileg.object_type">
<code class="descname">object_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.object_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The PostgreSQL object type to set the default privileges on (one of: table, sequence).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileg.owner">
<code class="descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileg.privileges">
<code class="descname">privileges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.privileges" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of privileges to apply as default privileges.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileg.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role to which grant default privileges on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileg.schema">
<code class="descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The database schema to set default privileges for this role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.DefaultPrivileg.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.DefaultPrivileg.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Extension">
<em class="property">class </em><code class="descclassname">pulumi_postgresql.</code><code class="descname">Extension</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>database=None</em>, <em>name=None</em>, <em>schema=None</em>, <em>version=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Extension" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">postgresql_extension</span></code> resource creates and manages an extension on a PostgreSQL
server.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which database to create the extension on. Defaults to provider database.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the extension.</li>
<li><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the schema of an extension.</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the version number of the extension.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/extension.html.markdown">https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/extension.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_postgresql.Extension.database">
<code class="descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Extension.database" title="Permalink to this definition">¶</a></dt>
<dd><p>Which database to create the extension on. Defaults to provider database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Extension.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Extension.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the extension.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Extension.schema">
<code class="descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Extension.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the schema of an extension.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Extension.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Extension.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the version number of the extension.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Extension.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Extension.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Extension.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Extension.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Grant">
<em class="property">class </em><code class="descclassname">pulumi_postgresql.</code><code class="descname">Grant</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>database=None</em>, <em>object_type=None</em>, <em>privileges=None</em>, <em>role=None</em>, <em>schema=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Grant" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">postgresql_grant</span></code> resource creates and manages privileges given to a user for a database schema.</p>
<blockquote>
<div><strong>Note:</strong> This resource needs Postgresql version 9 or above.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant privileges on for this role.</li>
<li><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PostgreSQL object type to grant the privileges on (one of: table, sequence).</li>
<li><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of privileges to grant.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to grant privileges on.</li>
<li><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database schema to grant privileges on for this role.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/grant.html.markdown">https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/grant.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_postgresql.Grant.database">
<code class="descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Grant.database" title="Permalink to this definition">¶</a></dt>
<dd><p>The database to grant privileges on for this role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Grant.object_type">
<code class="descname">object_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Grant.object_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The PostgreSQL object type to grant the privileges on (one of: table, sequence).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Grant.privileges">
<code class="descname">privileges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Grant.privileges" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of privileges to grant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Grant.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Grant.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role to grant privileges on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Grant.schema">
<code class="descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Grant.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The database schema to grant privileges on for this role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Grant.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Grant.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Grant.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Grant.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Provider">
<em class="property">class </em><code class="descclassname">pulumi_postgresql.</code><code class="descname">Provider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>connect_timeout=None</em>, <em>database=None</em>, <em>database_username=None</em>, <em>expected_version=None</em>, <em>host=None</em>, <em>max_connections=None</em>, <em>password=None</em>, <em>port=None</em>, <em>ssl_mode=None</em>, <em>sslmode=None</em>, <em>superuser=None</em>, <em>username=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the postgresql package. By default, resources use package-wide configuration
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
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/index.html.markdown</a>.</div></blockquote>
<dl class="method">
<dt id="pulumi_postgresql.Provider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Provider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Role">
<em class="property">class </em><code class="descclassname">pulumi_postgresql.</code><code class="descname">Role</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bypass_row_level_security=None</em>, <em>connection_limit=None</em>, <em>create_database=None</em>, <em>create_role=None</em>, <em>encrypted=None</em>, <em>encrypted_password=None</em>, <em>inherit=None</em>, <em>login=None</em>, <em>name=None</em>, <em>password=None</em>, <em>replication=None</em>, <em>roles=None</em>, <em>skip_drop_role=None</em>, <em>skip_reassign_owned=None</em>, <em>superuser=None</em>, <em>valid_until=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">postgresql_role</span></code> resource creates and manages a role on a PostgreSQL
server.</p>
<p>When a <code class="docutils literal notranslate"><span class="pre">postgresql_role</span></code> resource is removed, the PostgreSQL ROLE will
automatically run a <cite>``REASSIGN
OWNED`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-reassign-owned.html">https://www.postgresql.org/docs/current/static/sql-reassign-owned.html</a>&gt;`_
and <cite>``DROP
OWNED`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-drop-owned.html">https://www.postgresql.org/docs/current/static/sql-drop-owned.html</a>&gt;`_ to
the <code class="docutils literal notranslate"><span class="pre">CURRENT_USER</span></code> (normally the connected user for the provider).  If the
specified PostgreSQL ROLE owns objects in multiple PostgreSQL databases in the
same PostgreSQL Cluster, one PostgreSQL provider per database must be created
and all but the final <code class="docutils literal notranslate"><span class="pre">postgresql_role</span></code> must specify a <code class="docutils literal notranslate"><span class="pre">skip_drop_role</span></code>.</p>
<blockquote>
<div><strong>Note:</strong> All arguments including role name and password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bypass_row_level_security</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether a role bypasses every
row-level security (RLS) policy.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>connection_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If this role can log in, this specifies how
many concurrent connections the role can establish. <code class="docutils literal notranslate"><span class="pre">-1</span></code> (the default) means no
limit.</li>
<li><strong>create_database</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines a role’s ability to execute <code class="docutils literal notranslate"><span class="pre">CREATE</span>
<span class="pre">DATABASE</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>create_role</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines a role’s ability to execute <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">ROLE</span></code>.
A role with this privilege can also alter and drop other roles.  Default value
is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether the password is stored
encrypted in the system catalogs.  Default value is <code class="docutils literal notranslate"><span class="pre">true</span></code>.  NOTE: this value
is always set (to the conservative and safe value), but may interfere with the
behavior of
<cite>PostgreSQL’s ``password_encryption`</cite> setting &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION">https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION</a>&gt;`_.</li>
<li><strong>inherit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether a role “inherits” the privileges of
roles it is a member of.  Default value is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>login</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether role is allowed to log in.  Roles without
this attribute are useful for managing database privileges, but are not users
in the usual sense of the word.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role. Must be unique on the PostgreSQL
server instance where it is configured.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the role’s password. A password is only of use
for roles having the <code class="docutils literal notranslate"><span class="pre">login</span></code> attribute set to true.</li>
<li><strong>replication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether a role is allowed to initiate
streaming replication or put the system in and out of backup mode.  Default
value is <code class="docutils literal notranslate"><span class="pre">false</span></code></li>
<li><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Defines list of roles which will be granted to this new role.</li>
<li><strong>skip_drop_role</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When a PostgreSQL ROLE exists in multiple
databases and the ROLE is dropped, the
<a class="reference external" href="https://www.postgresql.org/docs/current/static/role-removal.html">cleanup of ownership of objects</a>
in each of the respective databases must occur before the ROLE can be dropped
from the catalog.  Set this option to true when there are multiple databases
in a PostgreSQL cluster using the same PostgreSQL ROLE for object ownership.
This is the third and final step taken when removing a ROLE from a database.</li>
<li><strong>skip_reassign_owned</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When a PostgreSQL ROLE exists in multiple
databases and the ROLE is dropped, a
<cite>``REASSIGN OWNED`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-reassign-owned.html">https://www.postgresql.org/docs/current/static/sql-reassign-owned.html</a>&gt;`_ in
must be executed on each of the respective databases before the <code class="docutils literal notranslate"><span class="pre">DROP</span> <span class="pre">ROLE</span></code>
can be executed to dropped the ROLE from the catalog.  This is the first and
second steps taken when removing a ROLE from a database (the second step being
an implicit
<cite>``DROP OWNED`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-drop-owned.html">https://www.postgresql.org/docs/current/static/sql-drop-owned.html</a>&gt;`_).</li>
<li><strong>superuser</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether the role is a “superuser”, and
therefore can override all access restrictions within the database.  Default
value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>valid_until</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the date and time after which the role’s
password is no longer valid.  Established connections past this <code class="docutils literal notranslate"><span class="pre">valid_time</span></code>
will have to be manually terminated.  This value corresponds to a PostgreSQL
datetime. If omitted or the magic value <code class="docutils literal notranslate"><span class="pre">NULL</span></code> is used, <code class="docutils literal notranslate"><span class="pre">valid_until</span></code> will be
set to <code class="docutils literal notranslate"><span class="pre">infinity</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">NULL</span></code>, therefore <code class="docutils literal notranslate"><span class="pre">infinity</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/role.html.markdown">https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/role.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_postgresql.Role.bypass_row_level_security">
<code class="descname">bypass_row_level_security</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.bypass_row_level_security" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines whether a role bypasses every
row-level security (RLS) policy.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.connection_limit">
<code class="descname">connection_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.connection_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>If this role can log in, this specifies how
many concurrent connections the role can establish. <code class="docutils literal notranslate"><span class="pre">-1</span></code> (the default) means no
limit.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.create_database">
<code class="descname">create_database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.create_database" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines a role’s ability to execute <code class="docutils literal notranslate"><span class="pre">CREATE</span>
<span class="pre">DATABASE</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.create_role">
<code class="descname">create_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.create_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines a role’s ability to execute <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">ROLE</span></code>.
A role with this privilege can also alter and drop other roles.  Default value
is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.encrypted_password">
<code class="descname">encrypted_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines whether the password is stored
encrypted in the system catalogs.  Default value is <code class="docutils literal notranslate"><span class="pre">true</span></code>.  NOTE: this value
is always set (to the conservative and safe value), but may interfere with the
behavior of
<cite>PostgreSQL’s ``password_encryption`</cite> setting &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION">https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION</a>&gt;`_.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.inherit">
<code class="descname">inherit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.inherit" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines whether a role “inherits” the privileges of
roles it is a member of.  Default value is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.login">
<code class="descname">login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.login" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines whether role is allowed to log in.  Roles without
this attribute are useful for managing database privileges, but are not users
in the usual sense of the word.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role. Must be unique on the PostgreSQL
server instance where it is configured.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the role’s password. A password is only of use
for roles having the <code class="docutils literal notranslate"><span class="pre">login</span></code> attribute set to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.replication">
<code class="descname">replication</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.replication" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines whether a role is allowed to initiate
streaming replication or put the system in and out of backup mode.  Default
value is <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.roles">
<code class="descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines list of roles which will be granted to this new role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.skip_drop_role">
<code class="descname">skip_drop_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.skip_drop_role" title="Permalink to this definition">¶</a></dt>
<dd><p>When a PostgreSQL ROLE exists in multiple
databases and the ROLE is dropped, the
<a class="reference external" href="https://www.postgresql.org/docs/current/static/role-removal.html">cleanup of ownership of objects</a>
in each of the respective databases must occur before the ROLE can be dropped
from the catalog.  Set this option to true when there are multiple databases
in a PostgreSQL cluster using the same PostgreSQL ROLE for object ownership.
This is the third and final step taken when removing a ROLE from a database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.skip_reassign_owned">
<code class="descname">skip_reassign_owned</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.skip_reassign_owned" title="Permalink to this definition">¶</a></dt>
<dd><p>When a PostgreSQL ROLE exists in multiple
databases and the ROLE is dropped, a
<cite>``REASSIGN OWNED`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-reassign-owned.html">https://www.postgresql.org/docs/current/static/sql-reassign-owned.html</a>&gt;`_ in
must be executed on each of the respective databases before the <code class="docutils literal notranslate"><span class="pre">DROP</span> <span class="pre">ROLE</span></code>
can be executed to dropped the ROLE from the catalog.  This is the first and
second steps taken when removing a ROLE from a database (the second step being
an implicit
<cite>``DROP OWNED`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-drop-owned.html">https://www.postgresql.org/docs/current/static/sql-drop-owned.html</a>&gt;`_).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.superuser">
<code class="descname">superuser</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.superuser" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines whether the role is a “superuser”, and
therefore can override all access restrictions within the database.  Default
value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.valid_until">
<code class="descname">valid_until</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.valid_until" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the date and time after which the role’s
password is no longer valid.  Established connections past this <code class="docutils literal notranslate"><span class="pre">valid_time</span></code>
will have to be manually terminated.  This value corresponds to a PostgreSQL
datetime. If omitted or the magic value <code class="docutils literal notranslate"><span class="pre">NULL</span></code> is used, <code class="docutils literal notranslate"><span class="pre">valid_until</span></code> will be
set to <code class="docutils literal notranslate"><span class="pre">infinity</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">NULL</span></code>, therefore <code class="docutils literal notranslate"><span class="pre">infinity</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Role.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Role.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Role.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Role.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Schema">
<em class="property">class </em><code class="descclassname">pulumi_postgresql.</code><code class="descname">Schema</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>if_not_exists=None</em>, <em>name=None</em>, <em>owner=None</em>, <em>policies=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">postgresql_schema</span></code> resource creates and manages <a class="reference external" href="https://www.postgresql.org/docs/current/static/ddl-schemas.html">schema
objects</a> within
a PostgreSQL database.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>if_not_exists</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, use the existing schema if it exists. (Default: true)</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the schema. Must be unique in the PostgreSQL
database instance where it is configured.</li>
<li><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ROLE who owns the schema.</li>
<li><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Can be specified multiple times for each policy.  Each
policy block supports fields documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/schema.html.markdown">https://github.com/terraform-providers/terraform-provider-postgresql/blob/master/website/docs/r/schema.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_postgresql.Schema.if_not_exists">
<code class="descname">if_not_exists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Schema.if_not_exists" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, use the existing schema if it exists. (Default: true)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Schema.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Schema.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the schema. Must be unique in the PostgreSQL
database instance where it is configured.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Schema.owner">
<code class="descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Schema.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The ROLE who owns the schema.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Schema.policies">
<code class="descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Schema.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be specified multiple times for each policy.  Each
policy block supports fields documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Schema.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Schema.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Schema.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Schema.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
