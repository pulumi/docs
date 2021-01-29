---
title: Package pulumi_postgresql
title_tag: Package pulumi_postgresql | Python SDK
linktitle: pulumi_postgresql
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "postgresql" >}}

<div class="section" id="pulumi-postgresql">
<h1>Pulumi PostgreSQL<a class="headerlink" href="#pulumi-postgresql" title="Permalink to this headline"></a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-postgresql">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-postgresql/issues">pulumi/pulumi-postgresql repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-postgresql/issues">terraform-providers/terraform-provider-postgresql repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_postgresql"></span><dl class="py class">
<dt id="pulumi_postgresql.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_connections</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_limit</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encoding</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_template</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lc_collate</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lc_ctype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tablespace_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Database" title="Permalink to this definition"></a></dt>
<dd><p>Create a Database resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] allow_connections: If <code class="docutils literal notranslate"><span class="pre">false</span></code> then no one can connect to this</p>
<blockquote>
<div><p>database. The default is <code class="docutils literal notranslate"><span class="pre">true</span></code>, allowing connections (except as restricted by
other mechanisms, such as <code class="docutils literal notranslate"><span class="pre">GRANT</span></code> or <code class="docutils literal notranslate"><span class="pre">REVOKE</span> <span class="pre">CONNECT</span></code>).</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>connection_limit</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How many concurrent connections can be
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
<dl class="py method">
<dt id="pulumi_postgresql.Database.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_connections</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_limit</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encoding</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_template</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lc_collate</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lc_ctype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tablespace_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_postgresql.Database" title="pulumi_postgresql.Database">Database</a><a class="headerlink" href="#pulumi_postgresql.Database.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_connections</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">false</span></code> then no one can connect to this
database. The default is <code class="docutils literal notranslate"><span class="pre">true</span></code>, allowing connections (except as restricted by
other mechanisms, such as <code class="docutils literal notranslate"><span class="pre">GRANT</span></code> or <code class="docutils literal notranslate"><span class="pre">REVOKE</span> <span class="pre">CONNECT</span></code>).</p></li>
<li><p><strong>connection_limit</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How many concurrent connections can be
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

<dl class="py method">
<dt id="pulumi_postgresql.Database.allow_connections">
<em class="property">property </em><code class="sig-name descname">allow_connections</code><a class="headerlink" href="#pulumi_postgresql.Database.allow_connections" title="Permalink to this definition"></a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code> then no one can connect to this
database. The default is <code class="docutils literal notranslate"><span class="pre">true</span></code>, allowing connections (except as restricted by
other mechanisms, such as <code class="docutils literal notranslate"><span class="pre">GRANT</span></code> or <code class="docutils literal notranslate"><span class="pre">REVOKE</span> <span class="pre">CONNECT</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Database.connection_limit">
<em class="property">property </em><code class="sig-name descname">connection_limit</code><a class="headerlink" href="#pulumi_postgresql.Database.connection_limit" title="Permalink to this definition"></a></dt>
<dd><p>How many concurrent connections can be
established to this database. <code class="docutils literal notranslate"><span class="pre">-1</span></code> (the default) means no limit.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Database.encoding">
<em class="property">property </em><code class="sig-name descname">encoding</code><a class="headerlink" href="#pulumi_postgresql.Database.encoding" title="Permalink to this definition"></a></dt>
<dd><p>Character set encoding to use in the new database</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Database.is_template">
<em class="property">property </em><code class="sig-name descname">is_template</code><a class="headerlink" href="#pulumi_postgresql.Database.is_template" title="Permalink to this definition"></a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, then this database can be cloned by any
user with <code class="docutils literal notranslate"><span class="pre">CREATEDB</span></code> privileges; if <code class="docutils literal notranslate"><span class="pre">false</span></code> (the default), then only
superusers or the owner of the database can clone it.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Database.lc_collate">
<em class="property">property </em><code class="sig-name descname">lc_collate</code><a class="headerlink" href="#pulumi_postgresql.Database.lc_collate" title="Permalink to this definition"></a></dt>
<dd><p>Collation order (LC_COLLATE) to use in the new database</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Database.lc_ctype">
<em class="property">property </em><code class="sig-name descname">lc_ctype</code><a class="headerlink" href="#pulumi_postgresql.Database.lc_ctype" title="Permalink to this definition"></a></dt>
<dd><p>Character classification (LC_CTYPE) to use in the new database</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Database.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_postgresql.Database.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the database. Must be unique on the PostgreSQL
server instance where it is configured.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Database.owner">
<em class="property">property </em><code class="sig-name descname">owner</code><a class="headerlink" href="#pulumi_postgresql.Database.owner" title="Permalink to this definition"></a></dt>
<dd><p>The role name of the user who will own the database, or
<code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code> to use the default (namely, the user executing the command). To
create a database owned by another role or to change the owner of an existing
database, you must be a direct or indirect member of the specified role, or
the username in the provider is a superuser.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Database.tablespace_name">
<em class="property">property </em><code class="sig-name descname">tablespace_name</code><a class="headerlink" href="#pulumi_postgresql.Database.tablespace_name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the tablespace that will be
associated with the database, or <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code> to use the template database’s
tablespace.  This tablespace will be the default tablespace used for objects
created in this database.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Database.template">
<em class="property">property </em><code class="sig-name descname">template</code><a class="headerlink" href="#pulumi_postgresql.Database.template" title="Permalink to this definition"></a></dt>
<dd><p>The name of the template from which to create the new database</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Database.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Database.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.Database.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Database.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.DefaultPrivileg">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">DefaultPrivileg</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privileges</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg" title="Permalink to this definition"></a></dt>
<dd><p>Create a DefaultPrivileg resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] database: The database to grant default privileges for this role
:param pulumi.Input[str] object_type: The PostgreSQL object type to set the default privileges on (one of: table, sequence, function, type)
:param pulumi.Input[str] owner: Target role for which to alter default privileges.
:param pulumi.Input[Sequence[pulumi.Input[str]]] privileges: The list of privileges to apply as default privileges
:param pulumi.Input[str] role: The name of the role to which grant default privileges on
:param pulumi.Input[str] schema: The database schema to set default privileges for this role</p>
<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileg.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privileges</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_postgresql.DefaultPrivileg" title="pulumi_postgresql.DefaultPrivileg">DefaultPrivileg</a><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing DefaultPrivileg resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant default privileges for this role</p></li>
<li><p><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PostgreSQL object type to set the default privileges on (one of: table, sequence, function, type)</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target role for which to alter default privileges.</p></li>
<li><p><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The list of privileges to apply as default privileges</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to which grant default privileges on</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database schema to set default privileges for this role</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileg.database">
<em class="property">property </em><code class="sig-name descname">database</code><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.database" title="Permalink to this definition"></a></dt>
<dd><p>The database to grant default privileges for this role</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileg.object_type">
<em class="property">property </em><code class="sig-name descname">object_type</code><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.object_type" title="Permalink to this definition"></a></dt>
<dd><p>The PostgreSQL object type to set the default privileges on (one of: table, sequence, function, type)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileg.owner">
<em class="property">property </em><code class="sig-name descname">owner</code><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.owner" title="Permalink to this definition"></a></dt>
<dd><p>Target role for which to alter default privileges.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileg.privileges">
<em class="property">property </em><code class="sig-name descname">privileges</code><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.privileges" title="Permalink to this definition"></a></dt>
<dd><p>The list of privileges to apply as default privileges</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileg.role">
<em class="property">property </em><code class="sig-name descname">role</code><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.role" title="Permalink to this definition"></a></dt>
<dd><p>The name of the role to which grant default privileges on</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileg.schema">
<em class="property">property </em><code class="sig-name descname">schema</code><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.schema" title="Permalink to this definition"></a></dt>
<dd><p>The database schema to set default privileges for this role</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileg.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.DefaultPrivileg.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileg.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.DefaultPrivileges">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">DefaultPrivileges</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privileges</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges" title="Permalink to this definition"></a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">DefaultPrivileges</span></code> resource creates and manages default privileges given to a user for a database schema.</p>
<blockquote>
<div><p><strong>Note:</strong> This resource needs Postgresql version 9 or above.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_postgresql</span> <span class="k">as</span> <span class="nn">postgresql</span>

<span class="n">read_only_tables</span> <span class="o">=</span> <span class="n">postgresql</span><span class="o">.</span><span class="n">DefaultPrivileges</span><span class="p">(</span><span class="s2">&quot;readOnlyTables&quot;</span><span class="p">,</span>
    <span class="n">database</span><span class="o">=</span><span class="s2">&quot;test_db&quot;</span><span class="p">,</span>
    <span class="n">object_type</span><span class="o">=</span><span class="s2">&quot;table&quot;</span><span class="p">,</span>
    <span class="n">owner</span><span class="o">=</span><span class="s2">&quot;db_owner&quot;</span><span class="p">,</span>
    <span class="n">privileges</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;SELECT&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;test_role&quot;</span><span class="p">,</span>
    <span class="n">schema</span><span class="o">=</span><span class="s2">&quot;public&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant default privileges for this role.</p></li>
<li><p><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PostgreSQL object type to set the default privileges on (one of: table, sequence, function, type).</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).</p></li>
<li><p><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The list of privileges to apply as default privileges.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to which grant default privileges on.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database schema to set default privileges for this role.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileges.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privileges</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_postgresql.DefaultPrivileges" title="pulumi_postgresql.DefaultPrivileges">DefaultPrivileges</a><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing DefaultPrivileges resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant default privileges for this role.</p></li>
<li><p><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PostgreSQL object type to set the default privileges on (one of: table, sequence, function, type).</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).</p></li>
<li><p><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The list of privileges to apply as default privileges.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to which grant default privileges on.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database schema to set default privileges for this role.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileges.database">
<em class="property">property </em><code class="sig-name descname">database</code><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.database" title="Permalink to this definition"></a></dt>
<dd><p>The database to grant default privileges for this role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileges.object_type">
<em class="property">property </em><code class="sig-name descname">object_type</code><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.object_type" title="Permalink to this definition"></a></dt>
<dd><p>The PostgreSQL object type to set the default privileges on (one of: table, sequence, function, type).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileges.owner">
<em class="property">property </em><code class="sig-name descname">owner</code><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.owner" title="Permalink to this definition"></a></dt>
<dd><p>Role for which apply default privileges (You can change default privileges only for objects that will be created by yourself or by roles that you are a member of).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileges.privileges">
<em class="property">property </em><code class="sig-name descname">privileges</code><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.privileges" title="Permalink to this definition"></a></dt>
<dd><p>The list of privileges to apply as default privileges.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileges.role">
<em class="property">property </em><code class="sig-name descname">role</code><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.role" title="Permalink to this definition"></a></dt>
<dd><p>The name of the role to which grant default privileges on.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileges.schema">
<em class="property">property </em><code class="sig-name descname">schema</code><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.schema" title="Permalink to this definition"></a></dt>
<dd><p>The database schema to set default privileges for this role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.DefaultPrivileges.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.DefaultPrivileges.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.DefaultPrivileges.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.Extension">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">Extension</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Extension" title="Permalink to this definition"></a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">Extension</span></code> resource creates and manages an extension on a PostgreSQL
server.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_postgresql</span> <span class="k">as</span> <span class="nn">postgresql</span>

<span class="n">my_extension</span> <span class="o">=</span> <span class="n">postgresql</span><span class="o">.</span><span class="n">Extension</span><span class="p">(</span><span class="s2">&quot;myExtension&quot;</span><span class="p">)</span>
</pre></div>
</div>
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
<dl class="py method">
<dt id="pulumi_postgresql.Extension.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_postgresql.Extension" title="pulumi_postgresql.Extension">Extension</a><a class="headerlink" href="#pulumi_postgresql.Extension.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Extension resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which database to create the extension on. Defaults to provider database.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the extension.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the schema of an extension.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the version number of the extension.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Extension.database">
<em class="property">property </em><code class="sig-name descname">database</code><a class="headerlink" href="#pulumi_postgresql.Extension.database" title="Permalink to this definition"></a></dt>
<dd><p>Which database to create the extension on. Defaults to provider database.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Extension.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_postgresql.Extension.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the extension.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Extension.schema">
<em class="property">property </em><code class="sig-name descname">schema</code><a class="headerlink" href="#pulumi_postgresql.Extension.schema" title="Permalink to this definition"></a></dt>
<dd><p>Sets the schema of an extension.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Extension.version">
<em class="property">property </em><code class="sig-name descname">version</code><a class="headerlink" href="#pulumi_postgresql.Extension.version" title="Permalink to this definition"></a></dt>
<dd><p>Sets the version number of the extension.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Extension.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Extension.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.Extension.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Extension.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.Grant">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">Grant</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privileges</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_grant_option</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Grant" title="Permalink to this definition"></a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">Grant</span></code> resource creates and manages privileges given to a user for a database schema.</p>
<p>See <a class="reference external" href="https://www.postgresql.org/docs/current/sql-grant.html">PostgreSQL documentation</a></p>
<blockquote>
<div><p><strong>Note:</strong> This resource needs Postgresql version 9 or above.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_postgresql</span> <span class="k">as</span> <span class="nn">postgresql</span>

<span class="n">readonly_tables</span> <span class="o">=</span> <span class="n">postgresql</span><span class="o">.</span><span class="n">Grant</span><span class="p">(</span><span class="s2">&quot;readonlyTables&quot;</span><span class="p">,</span>
    <span class="n">database</span><span class="o">=</span><span class="s2">&quot;test_db&quot;</span><span class="p">,</span>
    <span class="n">object_type</span><span class="o">=</span><span class="s2">&quot;table&quot;</span><span class="p">,</span>
    <span class="n">privileges</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;SELECT&quot;</span><span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;test_role&quot;</span><span class="p">,</span>
    <span class="n">schema</span><span class="o">=</span><span class="s2">&quot;public&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant privileges on for this role.</p></li>
<li><p><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PostgreSQL object type to grant the privileges on (one of: database, table, sequence,function).</p></li>
<li><p><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The list of privileges to grant. There are different kinds of privileges: SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER, CREATE, CONNECT, TEMPORARY, EXECUTE, and USAGE.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to grant privileges on.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database schema to grant privileges on for this role.</p></li>
<li><p><strong>with_grant_option</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Permit the grant recipient to grant it to others</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_postgresql.Grant.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">object_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privileges</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_grant_option</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_postgresql.Grant" title="pulumi_postgresql.Grant">Grant</a><a class="headerlink" href="#pulumi_postgresql.Grant.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Grant resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant privileges on for this role.</p></li>
<li><p><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PostgreSQL object type to grant the privileges on (one of: database, table, sequence,function).</p></li>
<li><p><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The list of privileges to grant. There are different kinds of privileges: SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER, CREATE, CONNECT, TEMPORARY, EXECUTE, and USAGE.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to grant privileges on.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database schema to grant privileges on for this role.</p></li>
<li><p><strong>with_grant_option</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Permit the grant recipient to grant it to others</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Grant.database">
<em class="property">property </em><code class="sig-name descname">database</code><a class="headerlink" href="#pulumi_postgresql.Grant.database" title="Permalink to this definition"></a></dt>
<dd><p>The database to grant privileges on for this role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Grant.object_type">
<em class="property">property </em><code class="sig-name descname">object_type</code><a class="headerlink" href="#pulumi_postgresql.Grant.object_type" title="Permalink to this definition"></a></dt>
<dd><p>The PostgreSQL object type to grant the privileges on (one of: database, table, sequence,function).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Grant.privileges">
<em class="property">property </em><code class="sig-name descname">privileges</code><a class="headerlink" href="#pulumi_postgresql.Grant.privileges" title="Permalink to this definition"></a></dt>
<dd><p>The list of privileges to grant. There are different kinds of privileges: SELECT, INSERT, UPDATE, DELETE, TRUNCATE, REFERENCES, TRIGGER, CREATE, CONNECT, TEMPORARY, EXECUTE, and USAGE.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Grant.role">
<em class="property">property </em><code class="sig-name descname">role</code><a class="headerlink" href="#pulumi_postgresql.Grant.role" title="Permalink to this definition"></a></dt>
<dd><p>The name of the role to grant privileges on.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Grant.schema">
<em class="property">property </em><code class="sig-name descname">schema</code><a class="headerlink" href="#pulumi_postgresql.Grant.schema" title="Permalink to this definition"></a></dt>
<dd><p>The database schema to grant privileges on for this role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Grant.with_grant_option">
<em class="property">property </em><code class="sig-name descname">with_grant_option</code><a class="headerlink" href="#pulumi_postgresql.Grant.with_grant_option" title="Permalink to this definition"></a></dt>
<dd><p>Permit the grant recipient to grant it to others</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Grant.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Grant.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.Grant.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Grant.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clientcert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>ProviderClientcertArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>ProviderClientcertArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connect_timeout</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expected_version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_connections</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_mode</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sslmode</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sslrootcert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">superuser</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Provider" title="Permalink to this definition"></a></dt>
<dd><p>The provider type for the postgresql package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>clientcert</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ProviderClientcertArgs'</em><em>]</em><em>]</em>) – SSL client certificate if required by the database.</p></li>
<li><p><strong>connect_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum wait for connection, in seconds. Zero or not specified means wait indefinitely.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database to connect to in order to conenct to (defaults to <code class="docutils literal notranslate"><span class="pre">postgres</span></code>).</p></li>
<li><p><strong>database_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database username associated to the connected user (for user name maps)</p></li>
<li><p><strong>expected_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the expected version of PostgreSQL.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of PostgreSQL server address to connect to</p></li>
<li><p><strong>max_connections</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of connections to establish to the database. Zero means unlimited.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password to be used if the PostgreSQL server demands password authentication</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The PostgreSQL port number to connect to at the server host, or socket file name extension for Unix-domain connections</p></li>
<li><p><strong>sslmode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This option determines whether or with what priority a secure SSL TCP/IP connection will be negotiated with the
PostgreSQL server</p></li>
<li><p><strong>sslrootcert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSL server root certificate file path. The file must contain PEM encoded data.</p></li>
<li><p><strong>superuser</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify if the user to connect as is a Postgres superuser or not.If not, some feature might be disabled (e.g.:
Refreshing state password from Postgres)</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PostgreSQL user name to connect as</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_postgresql.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Provider.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Provider.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.Role">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">Role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bypass_row_level_security</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_limit</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_database</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inherit</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_paths</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_drop_role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_reassign_owned</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statement_timeout</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">superuser</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">valid_until</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Role" title="Permalink to this definition"></a></dt>
<dd><p>Create a Role resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] bypass_row_level_security: Defines whether a role bypasses every</p>
<blockquote>
<div><p>row-level security (RLS) policy.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>connection_limit</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – If this role can log in, this specifies how
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
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Defines list of roles which will be granted to this new role.</p></li>
<li><p><strong>search_paths</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Alters the search path of this new role. Note that
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
<li><p><strong>statement_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Defines <cite>``statement_timeout`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT">https://www.postgresql.org/docs/current/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT</a>&gt;`_ setting for this role which allows to abort any statement that takes more than the specified amount of time.</p></li>
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
<dl class="py method">
<dt id="pulumi_postgresql.Role.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bypass_row_level_security</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_limit</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_database</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inherit</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_paths</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_drop_role</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_reassign_owned</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statement_timeout</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>int<span class="p">, </span>Awaitable<span class="p">[</span>int<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">superuser</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">valid_until</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_postgresql.Role" title="pulumi_postgresql.Role">Role</a><a class="headerlink" href="#pulumi_postgresql.Role.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Role resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bypass_row_level_security</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defines whether a role bypasses every
row-level security (RLS) policy.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>connection_limit</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – If this role can log in, this specifies how
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
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Defines list of roles which will be granted to this new role.</p></li>
<li><p><strong>search_paths</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Alters the search path of this new role. Note that
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
<li><p><strong>statement_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Defines <cite>``statement_timeout`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT">https://www.postgresql.org/docs/current/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT</a>&gt;`_ setting for this role which allows to abort any statement that takes more than the specified amount of time.</p></li>
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

<dl class="py method">
<dt id="pulumi_postgresql.Role.bypass_row_level_security">
<em class="property">property </em><code class="sig-name descname">bypass_row_level_security</code><a class="headerlink" href="#pulumi_postgresql.Role.bypass_row_level_security" title="Permalink to this definition"></a></dt>
<dd><p>Defines whether a role bypasses every
row-level security (RLS) policy.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.connection_limit">
<em class="property">property </em><code class="sig-name descname">connection_limit</code><a class="headerlink" href="#pulumi_postgresql.Role.connection_limit" title="Permalink to this definition"></a></dt>
<dd><p>If this role can log in, this specifies how
many concurrent connections the role can establish. <code class="docutils literal notranslate"><span class="pre">-1</span></code> (the default) means no
limit.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.create_database">
<em class="property">property </em><code class="sig-name descname">create_database</code><a class="headerlink" href="#pulumi_postgresql.Role.create_database" title="Permalink to this definition"></a></dt>
<dd><p>Defines a role’s ability to execute <code class="docutils literal notranslate"><span class="pre">CREATE</span>
<span class="pre">DATABASE</span></code>.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.create_role">
<em class="property">property </em><code class="sig-name descname">create_role</code><a class="headerlink" href="#pulumi_postgresql.Role.create_role" title="Permalink to this definition"></a></dt>
<dd><p>Defines a role’s ability to execute <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">ROLE</span></code>.
A role with this privilege can also alter and drop other roles.  Default value
is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.encrypted_password">
<em class="property">property </em><code class="sig-name descname">encrypted_password</code><a class="headerlink" href="#pulumi_postgresql.Role.encrypted_password" title="Permalink to this definition"></a></dt>
<dd><p>Defines whether the password is stored
encrypted in the system catalogs.  Default value is <code class="docutils literal notranslate"><span class="pre">true</span></code>.  NOTE: this value
is always set (to the conservative and safe value), but may interfere with the
behavior of
<cite>PostgreSQL’s ``password_encryption`</cite> setting &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION">https://www.postgresql.org/docs/current/static/runtime-config-connection.html#GUC-PASSWORD-ENCRYPTION</a>&gt;`_.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.inherit">
<em class="property">property </em><code class="sig-name descname">inherit</code><a class="headerlink" href="#pulumi_postgresql.Role.inherit" title="Permalink to this definition"></a></dt>
<dd><p>Defines whether a role “inherits” the privileges of
roles it is a member of.  Default value is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.login">
<em class="property">property </em><code class="sig-name descname">login</code><a class="headerlink" href="#pulumi_postgresql.Role.login" title="Permalink to this definition"></a></dt>
<dd><p>Defines whether role is allowed to log in.  Roles without
this attribute are useful for managing database privileges, but are not users
in the usual sense of the word.  Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_postgresql.Role.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the role. Must be unique on the PostgreSQL
server instance where it is configured.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.password">
<em class="property">property </em><code class="sig-name descname">password</code><a class="headerlink" href="#pulumi_postgresql.Role.password" title="Permalink to this definition"></a></dt>
<dd><p>Sets the role’s password. A password is only of use
for roles having the <code class="docutils literal notranslate"><span class="pre">login</span></code> attribute set to true.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.replication">
<em class="property">property </em><code class="sig-name descname">replication</code><a class="headerlink" href="#pulumi_postgresql.Role.replication" title="Permalink to this definition"></a></dt>
<dd><p>Defines whether a role is allowed to initiate
streaming replication or put the system in and out of backup mode.  Default
value is <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.roles">
<em class="property">property </em><code class="sig-name descname">roles</code><a class="headerlink" href="#pulumi_postgresql.Role.roles" title="Permalink to this definition"></a></dt>
<dd><p>Defines list of roles which will be granted to this new role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.search_paths">
<em class="property">property </em><code class="sig-name descname">search_paths</code><a class="headerlink" href="#pulumi_postgresql.Role.search_paths" title="Permalink to this definition"></a></dt>
<dd><p>Alters the search path of this new role. Note that
due to limitations in the implementation, values cannot contain the substring
<code class="docutils literal notranslate"><span class="pre">&quot;,</span> <span class="pre">&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.skip_drop_role">
<em class="property">property </em><code class="sig-name descname">skip_drop_role</code><a class="headerlink" href="#pulumi_postgresql.Role.skip_drop_role" title="Permalink to this definition"></a></dt>
<dd><p>When a PostgreSQL ROLE exists in multiple
databases and the ROLE is dropped, the
<a class="reference external" href="https://www.postgresql.org/docs/current/static/role-removal.html">cleanup of ownership of objects</a>
in each of the respective databases must occur before the ROLE can be dropped
from the catalog.  Set this option to true when there are multiple databases
in a PostgreSQL cluster using the same PostgreSQL ROLE for object ownership.
This is the third and final step taken when removing a ROLE from a database.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.skip_reassign_owned">
<em class="property">property </em><code class="sig-name descname">skip_reassign_owned</code><a class="headerlink" href="#pulumi_postgresql.Role.skip_reassign_owned" title="Permalink to this definition"></a></dt>
<dd><p>When a PostgreSQL ROLE exists in multiple
databases and the ROLE is dropped, a
<cite>``REASSIGN OWNED`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-reassign-owned.html">https://www.postgresql.org/docs/current/static/sql-reassign-owned.html</a>&gt;`_ in
must be executed on each of the respective databases before the <code class="docutils literal notranslate"><span class="pre">DROP</span> <span class="pre">ROLE</span></code>
can be executed to dropped the ROLE from the catalog.  This is the first and
second steps taken when removing a ROLE from a database (the second step being
an implicit
<cite>``DROP OWNED`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/static/sql-drop-owned.html">https://www.postgresql.org/docs/current/static/sql-drop-owned.html</a>&gt;`_).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.statement_timeout">
<em class="property">property </em><code class="sig-name descname">statement_timeout</code><a class="headerlink" href="#pulumi_postgresql.Role.statement_timeout" title="Permalink to this definition"></a></dt>
<dd><p>Defines <cite>``statement_timeout`</cite> &lt;<a class="reference external" href="https://www.postgresql.org/docs/current/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT">https://www.postgresql.org/docs/current/runtime-config-client.html#RUNTIME-CONFIG-CLIENT-STATEMENT</a>&gt;`_ setting for this role which allows to abort any statement that takes more than the specified amount of time.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.superuser">
<em class="property">property </em><code class="sig-name descname">superuser</code><a class="headerlink" href="#pulumi_postgresql.Role.superuser" title="Permalink to this definition"></a></dt>
<dd><p>Defines whether the role is a “superuser”, and
therefore can override all access restrictions within the database.  Default
value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.valid_until">
<em class="property">property </em><code class="sig-name descname">valid_until</code><a class="headerlink" href="#pulumi_postgresql.Role.valid_until" title="Permalink to this definition"></a></dt>
<dd><p>Defines the date and time after which the role’s
password is no longer valid.  Established connections past this <code class="docutils literal notranslate"><span class="pre">valid_time</span></code>
will have to be manually terminated.  This value corresponds to a PostgreSQL
datetime. If omitted or the magic value <code class="docutils literal notranslate"><span class="pre">NULL</span></code> is used, <code class="docutils literal notranslate"><span class="pre">valid_until</span></code> will be
set to <code class="docutils literal notranslate"><span class="pre">infinity</span></code>.  Default is <code class="docutils literal notranslate"><span class="pre">NULL</span></code>, therefore <code class="docutils literal notranslate"><span class="pre">infinity</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Role.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Role.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.Role.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Role.translate_input_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.Schema">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_postgresql.</code><code class="sig-name descname">Schema</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drop_cascade</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">if_not_exists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>SchemaPolicyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>SchemaPolicyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>SchemaPolicyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>SchemaPolicyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Schema" title="Permalink to this definition"></a></dt>
<dd><p>Create a Schema resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] database: The DATABASE in which where this schema will be created. (Default: The database used by your <code class="docutils literal notranslate"><span class="pre">provider</span></code> configuration)
:param pulumi.Input[bool] drop_cascade: When true, will also drop all the objects that are contained in the schema. (Default: false)
:param pulumi.Input[bool] if_not_exists: When true, use the existing schema if it exists. (Default: true)
:param pulumi.Input[str] name: The name of the schema. Must be unique in the PostgreSQL</p>
<blockquote>
<div><p>database instance where it is configured.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ROLE who owns the schema.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SchemaPolicyArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Can be specified multiple times for each policy.  Each
policy block supports fields documented below.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_postgresql.Schema.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">drop_cascade</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">if_not_exists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>bool<span class="p">, </span>Awaitable<span class="p">[</span>bool<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Union<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>SchemaPolicyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>SchemaPolicyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>SchemaPolicyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">, </span>Awaitable<span class="p">[</span>Union<span class="p">[</span>SchemaPolicyArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; <a class="reference internal" href="#pulumi_postgresql.Schema" title="pulumi_postgresql.Schema">Schema</a><a class="headerlink" href="#pulumi_postgresql.Schema.get" title="Permalink to this definition"></a></dt>
<dd><p>Get an existing Schema resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DATABASE in which where this schema will be created. (Default: The database used by your <code class="docutils literal notranslate"><span class="pre">provider</span></code> configuration)</p></li>
<li><p><strong>drop_cascade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, will also drop all the objects that are contained in the schema. (Default: false)</p></li>
<li><p><strong>if_not_exists</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, use the existing schema if it exists. (Default: true)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the schema. Must be unique in the PostgreSQL
database instance where it is configured.</p></li>
<li><p><strong>owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ROLE who owns the schema.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SchemaPolicyArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Can be specified multiple times for each policy.  Each
policy block supports fields documented below.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Schema.database">
<em class="property">property </em><code class="sig-name descname">database</code><a class="headerlink" href="#pulumi_postgresql.Schema.database" title="Permalink to this definition"></a></dt>
<dd><p>The DATABASE in which where this schema will be created. (Default: The database used by your <code class="docutils literal notranslate"><span class="pre">provider</span></code> configuration)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Schema.drop_cascade">
<em class="property">property </em><code class="sig-name descname">drop_cascade</code><a class="headerlink" href="#pulumi_postgresql.Schema.drop_cascade" title="Permalink to this definition"></a></dt>
<dd><p>When true, will also drop all the objects that are contained in the schema. (Default: false)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Schema.if_not_exists">
<em class="property">property </em><code class="sig-name descname">if_not_exists</code><a class="headerlink" href="#pulumi_postgresql.Schema.if_not_exists" title="Permalink to this definition"></a></dt>
<dd><p>When true, use the existing schema if it exists. (Default: true)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Schema.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_postgresql.Schema.name" title="Permalink to this definition"></a></dt>
<dd><p>The name of the schema. Must be unique in the PostgreSQL
database instance where it is configured.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Schema.owner">
<em class="property">property </em><code class="sig-name descname">owner</code><a class="headerlink" href="#pulumi_postgresql.Schema.owner" title="Permalink to this definition"></a></dt>
<dd><p>The ROLE who owns the schema.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Schema.policies">
<em class="property">property </em><code class="sig-name descname">policies</code><a class="headerlink" href="#pulumi_postgresql.Schema.policies" title="Permalink to this definition"></a></dt>
<dd><p>Can be specified multiple times for each policy.  Each
policy block supports fields documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_postgresql.Schema.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Schema.translate_output_property" title="Permalink to this definition"></a></dt>
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
<dt id="pulumi_postgresql.Schema.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_postgresql.Schema.translate_input_property" title="Permalink to this definition"></a></dt>
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
