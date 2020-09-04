---
title: Package pulumi_mysql
title_tag: Package pulumi_mysql | Python SDK
linktitle: pulumi_mysql
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "mysql" >}}

<div class="section" id="pulumi-mysql">
<h1>Pulumi MySQL<a class="headerlink" href="#pulumi-mysql" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-mysql">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-mysql/issues">pulumi/pulumi-mysql repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-mysql/issues">terraform-providers/terraform-provider-mysql repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_mysql"></span><dl class="py class">
<dt id="pulumi_mysql.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mysql.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_character_set</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_collation</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">Database</span></code> resource creates and manages a database on a MySQL
server.</p>
<blockquote>
<div><p><strong>Caution:</strong> The <code class="docutils literal notranslate"><span class="pre">Database</span></code> resource can completely delete your
database just as easily as it can create it. To avoid costly accidents,
consider setting
<cite>``prevent_destroy`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/configuration/resources.html#prevent_destroy">https://www.terraform.io/docs/configuration/resources.html#prevent_destroy</a>&gt;`_
on your database resources as an extra safety measure.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mysql</span> <span class="k">as</span> <span class="nn">mysql</span>

<span class="n">app</span> <span class="o">=</span> <span class="n">mysql</span><span class="o">.</span><span class="n">Database</span><span class="p">(</span><span class="s2">&quot;app&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_character_set</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default character set to use when
a table is created without specifying an explicit character set. Defaults
to “utf8”.</p></li>
<li><p><strong>default_collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default collation to use when a table
is created without specifying an explicit collation. Defaults to
<code class="docutils literal notranslate"><span class="pre">utf8_general_ci</span></code>. Each character set has its own set of collations, so
changing the character set requires also changing the collation.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database. This must be unique within
a given MySQL server and may or may not be case-sensitive depending on
the operating system on which the MySQL server is running.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mysql.Database.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_character_set</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_collation</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mysql.database.Database<a class="headerlink" href="#pulumi_mysql.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_character_set</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default character set to use when
a table is created without specifying an explicit character set. Defaults
to “utf8”.</p></li>
<li><p><strong>default_collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default collation to use when a table
is created without specifying an explicit collation. Defaults to
<code class="docutils literal notranslate"><span class="pre">utf8_general_ci</span></code>. Each character set has its own set of collations, so
changing the character set requires also changing the collation.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database. This must be unique within
a given MySQL server and may or may not be case-sensitive depending on
the operating system on which the MySQL server is running.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Database.default_character_set">
<em class="property">property </em><code class="sig-name descname">default_character_set</code><a class="headerlink" href="#pulumi_mysql.Database.default_character_set" title="Permalink to this definition">¶</a></dt>
<dd><p>The default character set to use when
a table is created without specifying an explicit character set. Defaults
to “utf8”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Database.default_collation">
<em class="property">property </em><code class="sig-name descname">default_collation</code><a class="headerlink" href="#pulumi_mysql.Database.default_collation" title="Permalink to this definition">¶</a></dt>
<dd><p>The default collation to use when a table
is created without specifying an explicit collation. Defaults to
<code class="docutils literal notranslate"><span class="pre">utf8_general_ci</span></code>. Each character set has its own set of collations, so
changing the character set requires also changing the collation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Database.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_mysql.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database. This must be unique within
a given MySQL server and may or may not be case-sensitive depending on
the operating system on which the MySQL server is running.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Database.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.Database.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.Grant">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mysql.</code><code class="sig-name descname">Grant</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grant</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privileges</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_option</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Grant" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">Grant</span></code> resource creates and manages privileges given to
a user on a MySQL server.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mysql</span> <span class="k">as</span> <span class="nn">mysql</span>

<span class="n">jdoe_user</span> <span class="o">=</span> <span class="n">mysql</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;jdoeUser&quot;</span><span class="p">,</span>
    <span class="n">host</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
    <span class="n">plaintext_password</span><span class="o">=</span><span class="s2">&quot;password&quot;</span><span class="p">,</span>
    <span class="n">user</span><span class="o">=</span><span class="s2">&quot;jdoe&quot;</span><span class="p">)</span>
<span class="n">jdoe_grant</span> <span class="o">=</span> <span class="n">mysql</span><span class="o">.</span><span class="n">Grant</span><span class="p">(</span><span class="s2">&quot;jdoeGrant&quot;</span><span class="p">,</span>
    <span class="n">database</span><span class="o">=</span><span class="s2">&quot;app&quot;</span><span class="p">,</span>
    <span class="n">host</span><span class="o">=</span><span class="n">jdoe_user</span><span class="o">.</span><span class="n">host</span><span class="p">,</span>
    <span class="n">privileges</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;SELECT&quot;</span><span class="p">,</span>
        <span class="s2">&quot;UPDATE&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">user</span><span class="o">=</span><span class="n">jdoe_user</span><span class="o">.</span><span class="n">user</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mysql</span> <span class="k">as</span> <span class="nn">mysql</span>

<span class="n">developer_role</span> <span class="o">=</span> <span class="n">mysql</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;developerRole&quot;</span><span class="p">)</span>
<span class="n">developer_grant</span> <span class="o">=</span> <span class="n">mysql</span><span class="o">.</span><span class="n">Grant</span><span class="p">(</span><span class="s2">&quot;developerGrant&quot;</span><span class="p">,</span>
    <span class="n">database</span><span class="o">=</span><span class="s2">&quot;app&quot;</span><span class="p">,</span>
    <span class="n">privileges</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;SELECT&quot;</span><span class="p">,</span>
        <span class="s2">&quot;UPDATE&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">role</span><span class="o">=</span><span class="n">developer_role</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mysql</span> <span class="k">as</span> <span class="nn">mysql</span>

<span class="n">jdoe</span> <span class="o">=</span> <span class="n">mysql</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;jdoe&quot;</span><span class="p">,</span>
    <span class="n">host</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
    <span class="n">plaintext_password</span><span class="o">=</span><span class="s2">&quot;password&quot;</span><span class="p">,</span>
    <span class="n">user</span><span class="o">=</span><span class="s2">&quot;jdoe&quot;</span><span class="p">)</span>
<span class="n">developer_role</span> <span class="o">=</span> <span class="n">mysql</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;developerRole&quot;</span><span class="p">)</span>
<span class="n">developer_grant</span> <span class="o">=</span> <span class="n">mysql</span><span class="o">.</span><span class="n">Grant</span><span class="p">(</span><span class="s2">&quot;developerGrant&quot;</span><span class="p">,</span>
    <span class="n">database</span><span class="o">=</span><span class="s2">&quot;app&quot;</span><span class="p">,</span>
    <span class="n">host</span><span class="o">=</span><span class="n">jdoe</span><span class="o">.</span><span class="n">host</span><span class="p">,</span>
    <span class="n">roles</span><span class="o">=</span><span class="p">[</span><span class="n">developer_role</span><span class="o">.</span><span class="n">name</span><span class="p">],</span>
    <span class="n">user</span><span class="o">=</span><span class="n">jdoe</span><span class="o">.</span><span class="n">user</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant privileges on.</p></li>
<li><p><strong>grant</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to also give the user privileges to grant the same privileges to other users.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source host of the user. Defaults to “localhost”. Conflicts with <code class="docutils literal notranslate"><span class="pre">role</span></code>.</p></li>
<li><p><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of privileges to grant to the user. Refer to a list of privileges (such as <a class="reference external" href="https://dev.mysql.com/doc/refman/5.5/en/grant.html">here</a>) for applicable privileges. Conflicts with <code class="docutils literal notranslate"><span class="pre">roles</span></code>.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role to grant <code class="docutils literal notranslate"><span class="pre">privileges</span></code> to. Conflicts with <code class="docutils literal notranslate"><span class="pre">user</span></code> and <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of rols to grant to the user. Conflicts with <code class="docutils literal notranslate"><span class="pre">privileges</span></code>.</p></li>
<li><p><strong>table</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which table to grant <code class="docutils literal notranslate"><span class="pre">privileges</span></code> on. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>, which is all tables.</p></li>
<li><p><strong>tls_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An TLS-Option for the <code class="docutils literal notranslate"><span class="pre">GRANT</span></code> statement. The value is suffixed to <code class="docutils literal notranslate"><span class="pre">REQUIRE</span></code>. A value of ‘SSL’ will generate a <code class="docutils literal notranslate"><span class="pre">GRANT</span> <span class="pre">...</span> <span class="pre">REQUIRE</span> <span class="pre">SSL</span></code> statement. See the <cite>MYSQL ``GRANT`</cite> documentation &lt;<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/grant.html">https://dev.mysql.com/doc/refman/5.7/en/grant.html</a>&gt;`_ for more. Ignored if MySQL version is under 5.7.0.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user. Conflicts with <code class="docutils literal notranslate"><span class="pre">role</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mysql.Grant.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grant</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privileges</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_option</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mysql.grant.Grant<a class="headerlink" href="#pulumi_mysql.Grant.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Grant resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database to grant privileges on.</p></li>
<li><p><strong>grant</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to also give the user privileges to grant the same privileges to other users.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source host of the user. Defaults to “localhost”. Conflicts with <code class="docutils literal notranslate"><span class="pre">role</span></code>.</p></li>
<li><p><strong>privileges</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – <p>A list of privileges to grant to the user. Refer to a list of privileges (such as <a class="reference external" href="https://dev.mysql.com/doc/refman/5.5/en/grant.html">here</a>) for applicable privileges. Conflicts with <code class="docutils literal notranslate"><span class="pre">roles</span></code>.</p>
</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role to grant <code class="docutils literal notranslate"><span class="pre">privileges</span></code> to. Conflicts with <code class="docutils literal notranslate"><span class="pre">user</span></code> and <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of rols to grant to the user. Conflicts with <code class="docutils literal notranslate"><span class="pre">privileges</span></code>.</p></li>
<li><p><strong>table</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which table to grant <code class="docutils literal notranslate"><span class="pre">privileges</span></code> on. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>, which is all tables.</p></li>
<li><p><strong>tls_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An TLS-Option for the <code class="docutils literal notranslate"><span class="pre">GRANT</span></code> statement. The value is suffixed to <code class="docutils literal notranslate"><span class="pre">REQUIRE</span></code>. A value of ‘SSL’ will generate a <code class="docutils literal notranslate"><span class="pre">GRANT</span> <span class="pre">...</span> <span class="pre">REQUIRE</span> <span class="pre">SSL</span></code> statement. See the <cite>MYSQL ``GRANT`</cite> documentation &lt;<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/grant.html">https://dev.mysql.com/doc/refman/5.7/en/grant.html</a>&gt;`_ for more. Ignored if MySQL version is under 5.7.0.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user. Conflicts with <code class="docutils literal notranslate"><span class="pre">role</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Grant.database">
<em class="property">property </em><code class="sig-name descname">database</code><a class="headerlink" href="#pulumi_mysql.Grant.database" title="Permalink to this definition">¶</a></dt>
<dd><p>The database to grant privileges on.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Grant.grant">
<em class="property">property </em><code class="sig-name descname">grant</code><a class="headerlink" href="#pulumi_mysql.Grant.grant" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to also give the user privileges to grant the same privileges to other users.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Grant.host">
<em class="property">property </em><code class="sig-name descname">host</code><a class="headerlink" href="#pulumi_mysql.Grant.host" title="Permalink to this definition">¶</a></dt>
<dd><p>The source host of the user. Defaults to “localhost”. Conflicts with <code class="docutils literal notranslate"><span class="pre">role</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Grant.privileges">
<em class="property">property </em><code class="sig-name descname">privileges</code><a class="headerlink" href="#pulumi_mysql.Grant.privileges" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of privileges to grant to the user. Refer to a list of privileges (such as <a class="reference external" href="https://dev.mysql.com/doc/refman/5.5/en/grant.html">here</a>) for applicable privileges. Conflicts with <code class="docutils literal notranslate"><span class="pre">roles</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Grant.role">
<em class="property">property </em><code class="sig-name descname">role</code><a class="headerlink" href="#pulumi_mysql.Grant.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role to grant <code class="docutils literal notranslate"><span class="pre">privileges</span></code> to. Conflicts with <code class="docutils literal notranslate"><span class="pre">user</span></code> and <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Grant.roles">
<em class="property">property </em><code class="sig-name descname">roles</code><a class="headerlink" href="#pulumi_mysql.Grant.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of rols to grant to the user. Conflicts with <code class="docutils literal notranslate"><span class="pre">privileges</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Grant.table">
<em class="property">property </em><code class="sig-name descname">table</code><a class="headerlink" href="#pulumi_mysql.Grant.table" title="Permalink to this definition">¶</a></dt>
<dd><p>Which table to grant <code class="docutils literal notranslate"><span class="pre">privileges</span></code> on. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>, which is all tables.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Grant.tls_option">
<em class="property">property </em><code class="sig-name descname">tls_option</code><a class="headerlink" href="#pulumi_mysql.Grant.tls_option" title="Permalink to this definition">¶</a></dt>
<dd><p>An TLS-Option for the <code class="docutils literal notranslate"><span class="pre">GRANT</span></code> statement. The value is suffixed to <code class="docutils literal notranslate"><span class="pre">REQUIRE</span></code>. A value of ‘SSL’ will generate a <code class="docutils literal notranslate"><span class="pre">GRANT</span> <span class="pre">...</span> <span class="pre">REQUIRE</span> <span class="pre">SSL</span></code> statement. See the <cite>MYSQL ``GRANT`</cite> documentation &lt;<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/grant.html">https://dev.mysql.com/doc/refman/5.7/en/grant.html</a>&gt;`_ for more. Ignored if MySQL version is under 5.7.0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Grant.user">
<em class="property">property </em><code class="sig-name descname">user</code><a class="headerlink" href="#pulumi_mysql.Grant.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user. Conflicts with <code class="docutils literal notranslate"><span class="pre">role</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Grant.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Grant.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.Grant.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Grant.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mysql.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication_plugin</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_conn_lifetime_sec</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_open_conns</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the mysql package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mysql.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.Role">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mysql.</code><code class="sig-name descname">Role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">Role</span></code> resource creates and manages a user on a MySQL
server.</p>
<blockquote>
<div><p><strong>Note:</strong> MySQL introduced roles in version 8. They do not work on MySQL 5 and lower.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mysql</span> <span class="k">as</span> <span class="nn">mysql</span>

<span class="n">developer</span> <span class="o">=</span> <span class="n">mysql</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;developer&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mysql.Role.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mysql.role.Role<a class="headerlink" href="#pulumi_mysql.Role.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Role resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Role.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_mysql.Role.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.Role.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Role.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.Role.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.Role.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mysql.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_plugin</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plaintext_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_option</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.User" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">User</span></code> resource creates and manages a user on a MySQL
server.</p>
<blockquote>
<div><p><strong>Note:</strong> The password for the user is provided in plain text, and is
obscured by an unsalted hash in the state
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.
Care is required when using this resource, to avoid disclosing the password.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mysql</span> <span class="k">as</span> <span class="nn">mysql</span>

<span class="n">jdoe</span> <span class="o">=</span> <span class="n">mysql</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;jdoe&quot;</span><span class="p">,</span>
    <span class="n">host</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
    <span class="n">plaintext_password</span><span class="o">=</span><span class="s2">&quot;password&quot;</span><span class="p">,</span>
    <span class="n">user</span><span class="o">=</span><span class="s2">&quot;jdoe&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mysql</span> <span class="k">as</span> <span class="nn">mysql</span>

<span class="n">nologin</span> <span class="o">=</span> <span class="n">mysql</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;nologin&quot;</span><span class="p">,</span>
    <span class="n">auth_plugin</span><span class="o">=</span><span class="s2">&quot;mysql_no_login&quot;</span><span class="p">,</span>
    <span class="n">host</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
    <span class="n">user</span><span class="o">=</span><span class="s2">&quot;nologin&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_plugin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code>.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source host of the user. Defaults to “localhost”.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Deprecated alias of <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code>, whose value is <em>stored as plaintext in state</em>. Prefer to use <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code> instead, which stores the password as an unsalted hash. Conflicts with <code class="docutils literal notranslate"><span class="pre">auth_plugin</span></code>.</p></li>
<li><p><strong>plaintext_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the user. This must be provided in plain text, so the data source for it must be secured. An <em>unsalted</em> hash of the provided password is stored in state. Conflicts with <code class="docutils literal notranslate"><span class="pre">auth_plugin</span></code>.</p></li>
<li><p><strong>tls_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An TLS-Option for the <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">USER</span></code> or <code class="docutils literal notranslate"><span class="pre">ALTER</span> <span class="pre">USER</span></code> statement. The value is suffixed to <code class="docutils literal notranslate"><span class="pre">REQUIRE</span></code>. A value of ‘SSL’ will generate a <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">USER</span> <span class="pre">...</span> <span class="pre">REQUIRE</span> <span class="pre">SSL</span></code> statement. See the <cite>MYSQL ``CREATE USER`</cite> documentation &lt;<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/create-user.html">https://dev.mysql.com/doc/refman/5.7/en/create-user.html</a>&gt;`_ for more. Ignored if MySQL version is under 5.7.0.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mysql.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_plugin</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plaintext_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_option</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mysql.user.User<a class="headerlink" href="#pulumi_mysql.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_plugin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code>.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source host of the user. Defaults to “localhost”.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Deprecated alias of <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code>, whose value is <em>stored as plaintext in state</em>. Prefer to use <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code> instead, which stores the password as an unsalted hash. Conflicts with <code class="docutils literal notranslate"><span class="pre">auth_plugin</span></code>.</p></li>
<li><p><strong>plaintext_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the user. This must be provided in plain text, so the data source for it must be secured. An <em>unsalted</em> hash of the provided password is stored in state. Conflicts with <code class="docutils literal notranslate"><span class="pre">auth_plugin</span></code>.</p></li>
<li><p><strong>tls_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An TLS-Option for the <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">USER</span></code> or <code class="docutils literal notranslate"><span class="pre">ALTER</span> <span class="pre">USER</span></code> statement. The value is suffixed to <code class="docutils literal notranslate"><span class="pre">REQUIRE</span></code>. A value of ‘SSL’ will generate a <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">USER</span> <span class="pre">...</span> <span class="pre">REQUIRE</span> <span class="pre">SSL</span></code> statement. See the <cite>MYSQL ``CREATE USER`</cite> documentation &lt;<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/create-user.html">https://dev.mysql.com/doc/refman/5.7/en/create-user.html</a>&gt;`_ for more. Ignored if MySQL version is under 5.7.0.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.User.auth_plugin">
<em class="property">property </em><code class="sig-name descname">auth_plugin</code><a class="headerlink" href="#pulumi_mysql.User.auth_plugin" title="Permalink to this definition">¶</a></dt>
<dd><p>Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.User.host">
<em class="property">property </em><code class="sig-name descname">host</code><a class="headerlink" href="#pulumi_mysql.User.host" title="Permalink to this definition">¶</a></dt>
<dd><p>The source host of the user. Defaults to “localhost”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.User.password">
<em class="property">property </em><code class="sig-name descname">password</code><a class="headerlink" href="#pulumi_mysql.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Deprecated alias of <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code>, whose value is <em>stored as plaintext in state</em>. Prefer to use <code class="docutils literal notranslate"><span class="pre">plaintext_password</span></code> instead, which stores the password as an unsalted hash. Conflicts with <code class="docutils literal notranslate"><span class="pre">auth_plugin</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.User.plaintext_password">
<em class="property">property </em><code class="sig-name descname">plaintext_password</code><a class="headerlink" href="#pulumi_mysql.User.plaintext_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password for the user. This must be provided in plain text, so the data source for it must be secured. An <em>unsalted</em> hash of the provided password is stored in state. Conflicts with <code class="docutils literal notranslate"><span class="pre">auth_plugin</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.User.tls_option">
<em class="property">property </em><code class="sig-name descname">tls_option</code><a class="headerlink" href="#pulumi_mysql.User.tls_option" title="Permalink to this definition">¶</a></dt>
<dd><p>An TLS-Option for the <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">USER</span></code> or <code class="docutils literal notranslate"><span class="pre">ALTER</span> <span class="pre">USER</span></code> statement. The value is suffixed to <code class="docutils literal notranslate"><span class="pre">REQUIRE</span></code>. A value of ‘SSL’ will generate a <code class="docutils literal notranslate"><span class="pre">CREATE</span> <span class="pre">USER</span> <span class="pre">...</span> <span class="pre">REQUIRE</span> <span class="pre">SSL</span></code> statement. See the <cite>MYSQL ``CREATE USER`</cite> documentation &lt;<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/create-user.html">https://dev.mysql.com/doc/refman/5.7/en/create-user.html</a>&gt;`_ for more. Ignored if MySQL version is under 5.7.0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.User.user">
<em class="property">property </em><code class="sig-name descname">user</code><a class="headerlink" href="#pulumi_mysql.User.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.UserPassword">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mysql.</code><code class="sig-name descname">UserPassword</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pgp_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.UserPassword" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a UserPassword resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] host: The source host of the user. Defaults to <code class="docutils literal notranslate"><span class="pre">localhost</span></code>.
:param pulumi.Input[str] pgp_key: Either a base-64 encoded PGP public key, or a keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:some_person_that_exists</span></code>.
:param pulumi.Input[str] user: The IAM user to associate with this access key.</p>
<dl class="py method">
<dt id="pulumi_mysql.UserPassword.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_fingerprint</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pgp_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mysql.user_password.UserPassword<a class="headerlink" href="#pulumi_mysql.UserPassword.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserPassword resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encrypted password, base64 encoded.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source host of the user. Defaults to <code class="docutils literal notranslate"><span class="pre">localhost</span></code>.</p></li>
<li><p><strong>key_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fingerprint of the PGP key used to encrypt the password</p></li>
<li><p><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Either a base-64 encoded PGP public key, or a keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:some_person_that_exists</span></code>.</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM user to associate with this access key.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.UserPassword.encrypted_password">
<em class="property">property </em><code class="sig-name descname">encrypted_password</code><a class="headerlink" href="#pulumi_mysql.UserPassword.encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The encrypted password, base64 encoded.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.UserPassword.host">
<em class="property">property </em><code class="sig-name descname">host</code><a class="headerlink" href="#pulumi_mysql.UserPassword.host" title="Permalink to this definition">¶</a></dt>
<dd><p>The source host of the user. Defaults to <code class="docutils literal notranslate"><span class="pre">localhost</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.UserPassword.key_fingerprint">
<em class="property">property </em><code class="sig-name descname">key_fingerprint</code><a class="headerlink" href="#pulumi_mysql.UserPassword.key_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the PGP key used to encrypt the password</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.UserPassword.pgp_key">
<em class="property">property </em><code class="sig-name descname">pgp_key</code><a class="headerlink" href="#pulumi_mysql.UserPassword.pgp_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Either a base-64 encoded PGP public key, or a keybase username in the form <code class="docutils literal notranslate"><span class="pre">keybase:some_person_that_exists</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.UserPassword.user">
<em class="property">property </em><code class="sig-name descname">user</code><a class="headerlink" href="#pulumi_mysql.UserPassword.user" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM user to associate with this access key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mysql.UserPassword.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.UserPassword.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mysql.UserPassword.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mysql.UserPassword.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
