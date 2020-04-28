---
title: Package pulumi_postgresql
title_tag: Package pulumi_postgresql | Python SDK
linktitle: pulumi_postgresql
notitle: true
---

<div class="section" id="pulumi-postgresql">
<h1>Pulumi PostgreSQL<a class="headerlink" href="#pulumi-postgresql" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-postgresql">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-postgresql/issues">pulumi/pulumi-postgresql repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-postgresql/issues">terraform-providers/terraform-provider-postgresql repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_postgresql"></span><dl class="class">
<dt id="pulumi_postgresql.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_connections=None</em>, <em class="sig-param">connection_limit=None</em>, <em class="sig-param">encoding=None</em>, <em class="sig-param">is_template=None</em>, <em class="sig-param">lc_collate=None</em>, <em class="sig-param">lc_ctype=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">tablespace_name=None</em>, <em class="sig-param">template=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.Database</span></code> resource creates and manages <a class="reference external" href="https://www.postgresql.org/docs/current/static/managing-databases.html">database
objects</a>
within a PostgreSQL server instance.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_connections</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">false</span></code> then no one can connect to this
database. The default is <code class="docutils literal notranslate"><span class="pre">true</span></code>, allowing connections (except as restricted by
other mechanisms, such as <code class="docutils literal notranslate"><span class="pre">GRANT</span></code> or <code class="docutils literal notranslate"><span class="pre">REVOKE</span> <span class="pre">CONNECT</span></code>).</p></li>
<li><p><strong>connection_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How many concurrent connections can be
established to this database. <code class="docutils literal notranslate"><span class="pre">-1</span></code> (the default) means no limit.</p></li>
<li><p><strong>encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Character set encoding to use in the new database</p></li>
<li><p><strong>is_template</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, then this database can be cloned by any
user with <code class="docutils literal notranslate"><span class="pre">CREATEDB</span></code> privileges; if <code class="docutils literal notranslate"><span class="pre">false</span></code> (the default), then only
superusers or the owner of the database can clone it.</p></li>
<li><p><strong>lc_collate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Collation order (LC_COLLATE) to use in the new database</p></li>
<li><p><strong>lc_ctype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Character classification (LC_CTYPE) to use in the new database</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database. Must be unique on the PostgreSQL
server instance where it is configured.</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role name of the user who will own the database, or
<code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code> to use the default (namely, the user executing the command). To
create a database owned by another role or to change the owner of an existing
database, you must be a direct or indirect member of the specified role, or
the username in the provider is a superuser.</p></li>
<li><p><strong>tablespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the tablespace that will be
associated with the database, or <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code> to use the template database’s
tablespace.  This tablespace will be the default tablespace used for objects
created in this database.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the template from which to create the new database</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_postgresql.Database.allow_connections">
<code class="sig-name descname">allow_connections</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.allow_connections" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code> then no one can connect to this
database. The default is <code class="docutils literal notranslate"><span class="pre">true</span></code>, allowing connections (except as restricted by
other mechanisms, such as <code class="docutils literal notranslate"><span class="pre">GRANT</span></code> or <code class="docutils literal notranslate"><span class="pre">REVOKE</span> <span class="pre">CONNECT</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Database.connection_limit">
<code class="sig-name descname">connection_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.connection_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>How many concurrent connections can be
established to this database. <code class="docutils literal notranslate"><span class="pre">-1</span></code> (the default) means no limit.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Database.encoding">
<code class="sig-name descname">encoding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.encoding" title="Permalink to this definition">¶</a></dt>
<dd><p>Character set encoding to use in the new database</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Database.is_template">
<code class="sig-name descname">is_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.is_template" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, then this database can be cloned by any
user with <code class="docutils literal notranslate"><span class="pre">CREATEDB</span></code> privileges; if <code class="docutils literal notranslate"><span class="pre">false</span></code> (the default), then only
superusers or the owner of the database can clone it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Database.lc_collate">
<code class="sig-name descname">lc_collate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.lc_collate" title="Permalink to this definition">¶</a></dt>
<dd><p>Collation order (LC_COLLATE) to use in the new database</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Database.lc_ctype">
<code class="sig-name descname">lc_ctype</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.lc_ctype" title="Permalink to this definition">¶</a></dt>
<dd><p>Character classification (LC_CTYPE) to use in the new database</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Database.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database. Must be unique on the PostgreSQL
server instance where it is configured.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Database.owner">
<code class="sig-name descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The role name of the user who will own the database, or
<code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code> to use the default (namely, the user executing the command). To
create a database owned by another role or to change the owner of an existing
database, you must be a direct or indirect member of the specified role, or
the username in the provider is a superuser.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Database.tablespace_name">
<code class="sig-name descname">tablespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.tablespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the tablespace that will be
associated with the database, or <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code> to use the template database’s
tablespace.  This tablespace will be the default tablespace used for objects
created in this database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Database.template">
<code class="sig-name descname">template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Database.template" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the template from which to create the new database</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Database.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_connections=None</em>, <em class="sig-param">connection_limit=None</em>, <em class="sig-param">encoding=None</em>, <em class="sig-param">is_template=None</em>, <em class="sig-param">lc_collate=None</em>, <em class="sig-param">lc_ctype=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">tablespace_name=None</em>, <em class="sig-param">template=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_connections</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">false</span></code> then no one can connect to this
database. The default is <code class="docutils literal notranslate"><span class="pre">true</span></code>, allowing connections (except as restricted by
other mechanisms, such as <code class="docutils literal notranslate"><span class="pre">GRANT</span></code> or <code class="docutils literal notranslate"><span class="pre">REVOKE</span> <span class="pre">CONNECT</span></code>).</p></li>
<li><p><strong>connection_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How many concurrent connections can be
established to this database. <code class="docutils literal notranslate"><span class="pre">-1</span></code> (the default) means no limit.</p></li>
<li><p><strong>encoding</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Character set encoding to use in the new database</p></li>
<li><p><strong>is_template</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, then this database can be cloned by any
user with <code class="docutils literal notranslate"><span class="pre">CREATEDB</span></code> privileges; if <code class="docutils literal notranslate"><span class="pre">false</span></code> (the default), then only
superusers or the owner of the database can clone it.</p></li>
<li><p><strong>lc_collate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Collation order (LC_COLLATE) to use in the new database</p></li>
<li><p><strong>lc_ctype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Character classification (LC_CTYPE) to use in the new database</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database. Must be unique on the PostgreSQL
server instance where it is configured.</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role name of the user who will own the database, or
<code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code> to use the default (namely, the user executing the command). To
create a database owned by another role or to change the owner of an existing
database, you must be a direct or indirect member of the specified role, or
the username in the provider is a superuser.</p></li>
<li><p><strong>tablespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the tablespace that will be
associated with the database, or <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code> to use the template database’s
tablespace.  This tablespace will be the default tablespace used for objects
created in this database.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the template from which to create the new database</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Database.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Database.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.DefaultPrivileg">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">DefaultPrivileg</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">object_type=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">privileges=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg" title="Permalink to this definition">¶</a></dt>
<dd><p>Deprecated: postgresql.DefaultPrivileg has been deprecated in favour of postgresql.DefaultPrivileges</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant default privileges for this role</p></li>
<li><p><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PostgreSQL object type to set the default privileges on (one of: table, sequence)</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target role for which to alter default privileges.</p></li>
<li><p><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of privileges to apply as default privileges</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to which grant default privileges on</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database schema to set default privileges for this role</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileg.database">
<code class="sig-name descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.database" title="Permalink to this definition">¶</a></dt>
<dd><p>The database to grant default privileges for this role</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileg.object_type">
<code class="sig-name descname">object_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.object_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The PostgreSQL object type to set the default privileges on (one of: table, sequence)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileg.owner">
<code class="sig-name descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>Target role for which to alter default privileges.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileg.privileges">
<code class="sig-name descname">privileges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.privileges" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of privileges to apply as default privileges</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileg.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role to which grant default privileges on</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileg.schema">
<code class="sig-name descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The database schema to set default privileges for this role</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.DefaultPrivileg.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">object_type=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">privileges=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">schema=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DefaultPrivileg resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant default privileges for this role</p></li>
<li><p><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PostgreSQL object type to set the default privileges on (one of: table, sequence)</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target role for which to alter default privileges.</p></li>
<li><p><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of privileges to apply as default privileges</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to which grant default privileges on</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database schema to set default privileges for this role</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.DefaultPrivileg.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.DefaultPrivileg.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.DefaultPrivileges">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">DefaultPrivileges</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">object_type=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">privileges=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.DefaultPrivileges</span></code> resource creates and manages default privileges given to a user for a database schema.</p>
<blockquote>
<div><p><strong>Note:</strong> This resource needs Postgresql version 9 or above.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant default privileges for this role.</p></li>
<li><p><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PostgreSQL object type to set the default privileges on (one of: table, sequence).</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).</p></li>
<li><p><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of privileges to apply as default privileges.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to which grant default privileges on.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database schema to set default privileges for this role.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileges.database">
<code class="sig-name descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.database" title="Permalink to this definition">¶</a></dt>
<dd><p>The database to grant default privileges for this role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileges.object_type">
<code class="sig-name descname">object_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.object_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The PostgreSQL object type to set the default privileges on (one of: table, sequence).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileges.owner">
<code class="sig-name descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileges.privileges">
<code class="sig-name descname">privileges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.privileges" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of privileges to apply as default privileges.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileges.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role to which grant default privileges on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.DefaultPrivileges.schema">
<code class="sig-name descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The database schema to set default privileges for this role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.DefaultPrivileges.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">object_type=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">privileges=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">schema=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DefaultPrivileges resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant default privileges for this role.</p></li>
<li><p><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PostgreSQL object type to set the default privileges on (one of: table, sequence).</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).</p></li>
<li><p><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of privileges to apply as default privileges.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to which grant default privileges on.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database schema to set default privileges for this role.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.DefaultPrivileges.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.DefaultPrivileges.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Extension">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">Extension</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Extension" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.Extension</span></code> resource creates and manages an extension on a PostgreSQL
server.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which database to create the extension on. Defaults to provider database.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the extension.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the schema of an extension.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the version number of the extension.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_postgresql.Extension.database">
<code class="sig-name descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Extension.database" title="Permalink to this definition">¶</a></dt>
<dd><p>Which database to create the extension on. Defaults to provider database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Extension.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Extension.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the extension.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Extension.schema">
<code class="sig-name descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Extension.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the schema of an extension.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Extension.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Extension.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the version number of the extension.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Extension.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Extension.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Extension resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which database to create the extension on. Defaults to provider database.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the extension.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the schema of an extension.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the version number of the extension.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Extension.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Extension.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Extension.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Extension.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Grant">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">Grant</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">object_type=None</em>, <em class="sig-param">privileges=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Grant" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.Grant</span></code> resource creates and manages privileges given to a user for a database schema.</p>
<blockquote>
<div><p><strong>Note:</strong> This resource needs Postgresql version 9 or above.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant privileges on for this role.</p></li>
<li><p><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PostgreSQL object type to grant the privileges on (one of: table, sequence).</p></li>
<li><p><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of privileges to grant.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to grant privileges on.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database schema to grant privileges on for this role.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_postgresql.Grant.database">
<code class="sig-name descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Grant.database" title="Permalink to this definition">¶</a></dt>
<dd><p>The database to grant privileges on for this role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Grant.object_type">
<code class="sig-name descname">object_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Grant.object_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The PostgreSQL object type to grant the privileges on (one of: table, sequence).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Grant.privileges">
<code class="sig-name descname">privileges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Grant.privileges" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of privileges to grant.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Grant.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Grant.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role to grant privileges on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Grant.schema">
<code class="sig-name descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Grant.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The database schema to grant privileges on for this role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Grant.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">object_type=None</em>, <em class="sig-param">privileges=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">schema=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Grant.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Grant resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant privileges on for this role.</p></li>
<li><p><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PostgreSQL object type to grant the privileges on (one of: table, sequence).</p></li>
<li><p><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of privileges to grant.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to grant privileges on.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database schema to grant privileges on for this role.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Grant.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Grant.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Grant.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Grant.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connect_timeout=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">database_username=None</em>, <em class="sig-param">expected_version=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">max_connections=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">ssl_mode=None</em>, <em class="sig-param">sslmode=None</em>, <em class="sig-param">superuser=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the postgresql package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connect_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database to connect to in order to conenct to (defaults to <code class="docutils literal notranslate"><span class="pre">postgres</span></code>).</p></li>
<li><p><strong>database_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database username associated to the connected user (for user name maps)</p></li>
<li><p><strong>expected_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the expected version of PostgreSQL.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of PostgreSQL server address to connect to</p></li>
<li><p><strong>max_connections</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number of connections to establish to the database. Zero means unlimited.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password to be used if the PostgreSQL server demands password authentication</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The PostgreSQL port number to connect to at the server host, or socket file name extension for Unix-domain connections</p></li>
<li><p><strong>sslmode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This option determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the
PostgreSQL server</p></li>
<li><p><strong>superuser</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify if the user to connect as is a Postgres superuser or not.If not, some feature might be disabled (e.g.:
Refreshing state password from Postgres)</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PostgreSQL user name to connect as</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_postgresql.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Role">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">Role</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bypass_row_level_security=None</em>, <em class="sig-param">connection_limit=None</em>, <em class="sig-param">create_database=None</em>, <em class="sig-param">create_role=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">encrypted_password=None</em>, <em class="sig-param">inherit=None</em>, <em class="sig-param">login=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">replication=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">search_paths=None</em>, <em class="sig-param">skip_drop_role=None</em>, <em class="sig-param">skip_reassign_owned=None</em>, <em class="sig-param">statement_timeout=None</em>, <em class="sig-param">superuser=None</em>, <em class="sig-param">valid_until=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.Role</span></code> resource creates and manages a role on a PostgreSQL
server.</p>
<p>When a <code class="docutils literal notranslate"><span class="pre">.Role</span></code> resource is removed, the PostgreSQL ROLE will
automatically run a <cite>``REASSIGN
OWNED`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-reassign-owned.html">https://www.postgresql.org/docs/current/static/sql-reassign-owned.html</a>&gt;`_
and <cite>``DROP
OWNED`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-drop-owned.html">https://www.postgresql.org/docs/current/static/sql-drop-owned.html</a>&gt;`_ to
the <code class="docutils literal notranslate"><span class="pre">CURRENT_USER</span></code> (normally the connected user for the provider).  If the
specified PostgreSQL ROLE owns objects in multiple PostgreSQL databases in the
same PostgreSQL Cluster, one PostgreSQL provider per database must be created
and all but the final <code class="docutils literal notranslate"><span class="pre">.Role</span></code> must specify a <code class="docutils literal notranslate"><span class="pre">skip_drop_role</span></code>.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including role name and password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bypass_row_level_security</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether a role bypasses every
row-level security (RLS) policy.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>connection_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If this role can log in, this specifies how
many concurrent connections the role can establish. <code class="docutils literal notranslate"><span class="pre">-1</span></code> (the default) means no
limit.</p></li>
<li><p><strong>create_database</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines a role’s ability to execute <code class="docutils literal notranslate"><span class="pre">CREATE</span>
<span class="pre">DATABASE</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>create_role</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines a role’s ability to execute <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">ROLE</span></code>.
A role with this privilege can also alter and drop other roles.  Default value
is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether the password is stored
encrypted in the system catalogs.  Default value is <code class="docutils literal notranslate"><span class="pre">true</span></code>.  NOTE: this value
is always set (to the conservative and safe value), but may interfere with the
behavior of
<cite>PostgreSQL’s ``password_encryption`</cite> setting &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION">https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION</a>&gt;`_.</p></li>
<li><p><strong>inherit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether a role “inherits” the privileges of
roles it is a member of.  Default value is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>login</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether role is allowed to log in.  Roles without
this attribute are useful for managing database privileges, but are not users
in the usual sense of the word.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role. Must be unique on the PostgreSQL
server instance where it is configured.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the role’s password. A password is only of use
for roles having the <code class="docutils literal notranslate"><span class="pre">login</span></code> attribute set to true.</p></li>
<li><p><strong>replication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether a role is allowed to initiate
streaming replication or put the system in and out of backup mode.  Default
value is <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Defines list of roles which will be granted to this new role.</p></li>
<li><p><strong>search_paths</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Alters the search path of this new role. Note that
due to limitations in the implementation, values cannot contain the substring
<code class="docutils literal notranslate"><span class="pre">&quot;,</span> <span class="pre">&quot;</span></code>.</p></li>
<li><p><strong>skip_drop_role</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When a PostgreSQL ROLE exists in multiple
databases and the ROLE is dropped, the
<a class="reference external" href="https://www.postgresql.org/docs/current/static/role-removal.html">cleanup of ownership of objects</a>
in each of the respective databases must occur before the ROLE can be dropped
from the catalog.  Set this option to true when there are multiple databases
in a PostgreSQL cluster using the same PostgreSQL ROLE for object ownership.
This is the third and final step taken when removing a ROLE from a database.</p></li>
<li><p><strong>skip_reassign_owned</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When a PostgreSQL ROLE exists in multiple
databases and the ROLE is dropped, a
<cite>``REASSIGN OWNED`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-reassign-owned.html">https://www.postgresql.org/docs/current/static/sql-reassign-owned.html</a>&gt;`_ in
must be executed on each of the respective databases before the <code class="docutils literal notranslate"><span class="pre">DROP</span> <span class="pre">ROLE</span></code>
can be executed to dropped the ROLE from the catalog.  This is the first and
second steps taken when removing a ROLE from a database (the second step being
an implicit
<cite>``DROP OWNED`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-drop-owned.html">https://www.postgresql.org/docs/current/static/sql-drop-owned.html</a>&gt;`_).</p></li>
<li><p><strong>statement_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Defines <cite>``statement_timeout`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT">https://www.postgresql.org/docs/current/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT</a>&gt;`_ setting for this role which allows to abort any statement that takes more than the specified amount of time.</p></li>
<li><p><strong>superuser</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether the role is a “superuser”, and
therefore can override all access restrictions within the database.  Default
value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>valid_until</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the date and time after which the role’s
password is no longer valid.  Established connections past this <code class="docutils literal notranslate"><span class="pre">valid_time</span></code>
will have to be manually terminated.  This value corresponds to a PostgreSQL
datetime. If omitted or the magic value <code class="docutils literal notranslate"><span class="pre">NULL</span></code> is used, <code class="docutils literal notranslate"><span class="pre">valid_until</span></code> will be
set to <code class="docutils literal notranslate"><span class="pre">infinity</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">NULL</span></code>, therefore <code class="docutils literal notranslate"><span class="pre">infinity</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_postgresql.Role.bypass_row_level_security">
<code class="sig-name descname">bypass_row_level_security</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.bypass_row_level_security" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines whether a role bypasses every
row-level security (RLS) policy.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.connection_limit">
<code class="sig-name descname">connection_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.connection_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>If this role can log in, this specifies how
many concurrent connections the role can establish. <code class="docutils literal notranslate"><span class="pre">-1</span></code> (the default) means no
limit.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.create_database">
<code class="sig-name descname">create_database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.create_database" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines a role’s ability to execute <code class="docutils literal notranslate"><span class="pre">CREATE</span>
<span class="pre">DATABASE</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.create_role">
<code class="sig-name descname">create_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.create_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines a role’s ability to execute <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">ROLE</span></code>.
A role with this privilege can also alter and drop other roles.  Default value
is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.encrypted_password">
<code class="sig-name descname">encrypted_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines whether the password is stored
encrypted in the system catalogs.  Default value is <code class="docutils literal notranslate"><span class="pre">true</span></code>.  NOTE: this value
is always set (to the conservative and safe value), but may interfere with the
behavior of
<cite>PostgreSQL’s ``password_encryption`</cite> setting &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION">https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION</a>&gt;`_.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.inherit">
<code class="sig-name descname">inherit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.inherit" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines whether a role “inherits” the privileges of
roles it is a member of.  Default value is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.login">
<code class="sig-name descname">login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.login" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines whether role is allowed to log in.  Roles without
this attribute are useful for managing database privileges, but are not users
in the usual sense of the word.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role. Must be unique on the PostgreSQL
server instance where it is configured.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the role’s password. A password is only of use
for roles having the <code class="docutils literal notranslate"><span class="pre">login</span></code> attribute set to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.replication">
<code class="sig-name descname">replication</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.replication" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines whether a role is allowed to initiate
streaming replication or put the system in and out of backup mode.  Default
value is <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.roles">
<code class="sig-name descname">roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines list of roles which will be granted to this new role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.search_paths">
<code class="sig-name descname">search_paths</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.search_paths" title="Permalink to this definition">¶</a></dt>
<dd><p>Alters the search path of this new role. Note that
due to limitations in the implementation, values cannot contain the substring
<code class="docutils literal notranslate"><span class="pre">&quot;,</span> <span class="pre">&quot;</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.skip_drop_role">
<code class="sig-name descname">skip_drop_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.skip_drop_role" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-name descname">skip_reassign_owned</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.skip_reassign_owned" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Role.statement_timeout">
<code class="sig-name descname">statement_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.statement_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines <cite>``statement_timeout`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT">https://www.postgresql.org/docs/current/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT</a>&gt;`_ setting for this role which allows to abort any statement that takes more than the specified amount of time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.superuser">
<code class="sig-name descname">superuser</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.superuser" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines whether the role is a “superuser”, and
therefore can override all access restrictions within the database.  Default
value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Role.valid_until">
<code class="sig-name descname">valid_until</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Role.valid_until" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the date and time after which the role’s
password is no longer valid.  Established connections past this <code class="docutils literal notranslate"><span class="pre">valid_time</span></code>
will have to be manually terminated.  This value corresponds to a PostgreSQL
datetime. If omitted or the magic value <code class="docutils literal notranslate"><span class="pre">NULL</span></code> is used, <code class="docutils literal notranslate"><span class="pre">valid_until</span></code> will be
set to <code class="docutils literal notranslate"><span class="pre">infinity</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">NULL</span></code>, therefore <code class="docutils literal notranslate"><span class="pre">infinity</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Role.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bypass_row_level_security=None</em>, <em class="sig-param">connection_limit=None</em>, <em class="sig-param">create_database=None</em>, <em class="sig-param">create_role=None</em>, <em class="sig-param">encrypted=None</em>, <em class="sig-param">encrypted_password=None</em>, <em class="sig-param">inherit=None</em>, <em class="sig-param">login=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">replication=None</em>, <em class="sig-param">roles=None</em>, <em class="sig-param">search_paths=None</em>, <em class="sig-param">skip_drop_role=None</em>, <em class="sig-param">skip_reassign_owned=None</em>, <em class="sig-param">statement_timeout=None</em>, <em class="sig-param">superuser=None</em>, <em class="sig-param">valid_until=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Role.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Role resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bypass_row_level_security</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether a role bypasses every
row-level security (RLS) policy.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>connection_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If this role can log in, this specifies how
many concurrent connections the role can establish. <code class="docutils literal notranslate"><span class="pre">-1</span></code> (the default) means no
limit.</p></li>
<li><p><strong>create_database</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines a role’s ability to execute <code class="docutils literal notranslate"><span class="pre">CREATE</span>
<span class="pre">DATABASE</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>create_role</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines a role’s ability to execute <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">ROLE</span></code>.
A role with this privilege can also alter and drop other roles.  Default value
is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether the password is stored
encrypted in the system catalogs.  Default value is <code class="docutils literal notranslate"><span class="pre">true</span></code>.  NOTE: this value
is always set (to the conservative and safe value), but may interfere with the
behavior of
<cite>PostgreSQL’s ``password_encryption`</cite> setting &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION">https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION</a>&gt;`_.</p></li>
<li><p><strong>inherit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether a role “inherits” the privileges of
roles it is a member of.  Default value is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>login</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether role is allowed to log in.  Roles without
this attribute are useful for managing database privileges, but are not users
in the usual sense of the word.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role. Must be unique on the PostgreSQL
server instance where it is configured.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the role’s password. A password is only of use
for roles having the <code class="docutils literal notranslate"><span class="pre">login</span></code> attribute set to true.</p></li>
<li><p><strong>replication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether a role is allowed to initiate
streaming replication or put the system in and out of backup mode.  Default
value is <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Defines list of roles which will be granted to this new role.</p></li>
<li><p><strong>search_paths</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Alters the search path of this new role. Note that
due to limitations in the implementation, values cannot contain the substring
<code class="docutils literal notranslate"><span class="pre">&quot;,</span> <span class="pre">&quot;</span></code>.</p></li>
<li><p><strong>skip_drop_role</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>When a PostgreSQL ROLE exists in multiple
databases and the ROLE is dropped, the
<a class="reference external" href="https://www.postgresql.org/docs/current/static/role-removal.html">cleanup of ownership of objects</a>
in each of the respective databases must occur before the ROLE can be dropped
from the catalog.  Set this option to true when there are multiple databases
in a PostgreSQL cluster using the same PostgreSQL ROLE for object ownership.
This is the third and final step taken when removing a ROLE from a database.</p>
</p></li>
<li><p><strong>skip_reassign_owned</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When a PostgreSQL ROLE exists in multiple
databases and the ROLE is dropped, a
<cite>``REASSIGN OWNED`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-reassign-owned.html">https://www.postgresql.org/docs/current/static/sql-reassign-owned.html</a>&gt;`_ in
must be executed on each of the respective databases before the <code class="docutils literal notranslate"><span class="pre">DROP</span> <span class="pre">ROLE</span></code>
can be executed to dropped the ROLE from the catalog.  This is the first and
second steps taken when removing a ROLE from a database (the second step being
an implicit
<cite>``DROP OWNED`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-drop-owned.html">https://www.postgresql.org/docs/current/static/sql-drop-owned.html</a>&gt;`_).</p></li>
<li><p><strong>statement_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Defines <cite>``statement_timeout`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT">https://www.postgresql.org/docs/current/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT</a>&gt;`_ setting for this role which allows to abort any statement that takes more than the specified amount of time.</p></li>
<li><p><strong>superuser</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether the role is a “superuser”, and
therefore can override all access restrictions within the database.  Default
value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>valid_until</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the date and time after which the role’s
password is no longer valid.  Established connections past this <code class="docutils literal notranslate"><span class="pre">valid_time</span></code>
will have to be manually terminated.  This value corresponds to a PostgreSQL
datetime. If omitted or the magic value <code class="docutils literal notranslate"><span class="pre">NULL</span></code> is used, <code class="docutils literal notranslate"><span class="pre">valid_until</span></code> will be
set to <code class="docutils literal notranslate"><span class="pre">infinity</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">NULL</span></code>, therefore <code class="docutils literal notranslate"><span class="pre">infinity</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Role.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Role.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Role.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Role.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Schema">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">Schema</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">drop_cascade=None</em>, <em class="sig-param">if_not_exists=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">.Schema</span></code> resource creates and manages <a class="reference external" href="https://www.postgresql.org/docs/current/static/ddl-schemas.html">schema
objects</a> within
a PostgreSQL database.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DATABASE in which where this schema will be created. (Default: The database used by your <code class="docutils literal notranslate"><span class="pre">provider</span></code> configuration)</p></li>
<li><p><strong>drop_cascade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, will also drop all the objects that are contained in the schema. (Default: false)</p></li>
<li><p><strong>if_not_exists</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, use the existing schema if it exists. (Default: true)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the schema. Must be unique in the PostgreSQL
database instance where it is configured.</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ROLE who owns the schema.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Can be specified multiple times for each policy.  Each
policy block supports fields documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">create</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the specified ROLE have CREATE privileges to the specified SCHEMA.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createWithGrant</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the specified ROLE have CREATE privileges to the specified SCHEMA and the ability to GRANT the CREATE privilege to other ROLEs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ROLE who is receiving the policy.  If this value is empty or not specified it implies the policy is referring to the <cite>``PUBLIC`</cite> role &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-grant.html">https://www.postgresql.org/docs/current/static/sql-grant.html</a>&gt;`_.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the specified ROLE have USAGE privileges to the specified SCHEMA.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usageWithGrant</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the specified ROLE have USAGE privileges to the specified SCHEMA and the ability to GRANT the USAGE privilege to other ROLEs.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_postgresql.Schema.database">
<code class="sig-name descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Schema.database" title="Permalink to this definition">¶</a></dt>
<dd><p>The DATABASE in which where this schema will be created. (Default: The database used by your <code class="docutils literal notranslate"><span class="pre">provider</span></code> configuration)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Schema.drop_cascade">
<code class="sig-name descname">drop_cascade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Schema.drop_cascade" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, will also drop all the objects that are contained in the schema. (Default: false)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Schema.if_not_exists">
<code class="sig-name descname">if_not_exists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Schema.if_not_exists" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, use the existing schema if it exists. (Default: true)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Schema.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Schema.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the schema. Must be unique in the PostgreSQL
database instance where it is configured.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Schema.owner">
<code class="sig-name descname">owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Schema.owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The ROLE who owns the schema.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_postgresql.Schema.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_postgresql.Schema.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be specified multiple times for each policy.  Each
policy block supports fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">create</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the specified ROLE have CREATE privileges to the specified SCHEMA.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createWithGrant</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the specified ROLE have CREATE privileges to the specified SCHEMA and the ability to GRANT the CREATE privilege to other ROLEs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ROLE who is receiving the policy.  If this value is empty or not specified it implies the policy is referring to the <cite>``PUBLIC`</cite> role &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-grant.html">https://www.postgresql.org/docs/current/static/sql-grant.html</a>&gt;`_.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usage</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the specified ROLE have USAGE privileges to the specified SCHEMA.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usageWithGrant</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the specified ROLE have USAGE privileges to the specified SCHEMA and the ability to GRANT the USAGE privilege to other ROLEs.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Schema.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database=None</em>, <em class="sig-param">drop_cascade=None</em>, <em class="sig-param">if_not_exists=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner=None</em>, <em class="sig-param">policies=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Schema.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Schema resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DATABASE in which where this schema will be created. (Default: The database used by your <code class="docutils literal notranslate"><span class="pre">provider</span></code> configuration)</p></li>
<li><p><strong>drop_cascade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, will also drop all the objects that are contained in the schema. (Default: false)</p></li>
<li><p><strong>if_not_exists</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, use the existing schema if it exists. (Default: true)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the schema. Must be unique in the PostgreSQL
database instance where it is configured.</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ROLE who owns the schema.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Can be specified multiple times for each policy.  Each
policy block supports fields documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">create</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the specified ROLE have CREATE privileges to the specified SCHEMA.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createWithGrant</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the specified ROLE have CREATE privileges to the specified SCHEMA and the ability to GRANT the CREATE privilege to other ROLEs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ROLE who is receiving the policy.  If this value is empty or not specified it implies the policy is referring to the <cite>``PUBLIC`</cite> role &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-grant.html">https://www.postgresql.org/docs/current/static/sql-grant.html</a>&gt;`_.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the specified ROLE have USAGE privileges to the specified SCHEMA.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">usageWithGrant</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the specified ROLE have USAGE privileges to the specified SCHEMA and the ability to GRANT the USAGE privilege to other ROLEs.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_postgresql.Schema.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Schema.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_postgresql.Schema.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Schema.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
