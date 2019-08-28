---
title: Module sql
---

<div class="section" id="sql">
<h1>sql<a class="headerlink" href="#sql" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.sql"></span><dl class="class">
<dt id="pulumi_gcp.sql.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.sql.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">charset=None</em>, <em class="sig-param">collation=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new Google SQL Database on a Google SQL Database Instance. For more information, see
the <a class="reference external" href="https://cloud.google.com/sql/">official documentation</a>,
or the <a class="reference external" href="https://cloud.google.com/sql/docs/admin-api/v1beta4/databases">JSON API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>charset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The charset value. See MySQL’s
<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and Collations</a>
and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/multibyte.html">Character Set Support</a>
for more details and supported values. Postgres databases are in beta
and have limited <code class="docutils literal notranslate"><span class="pre">charset</span></code> support; they only support a value of <code class="docutils literal notranslate"><span class="pre">UTF8</span></code> at creation time.</p></li>
<li><p><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The collation value. See MySQL’s
<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and Collations</a>
and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/collation.html">Collation Support</a>
for more details and supported values. Postgres databases are in beta
and have limited <code class="docutils literal notranslate"><span class="pre">collation</span></code> support; they only support a value of <code class="docutils literal notranslate"><span class="pre">en_US.UTF8</span></code> at creation time.</p>
</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of containing instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_database.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_database.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.charset">
<code class="sig-name descname">charset</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.charset" title="Permalink to this definition">¶</a></dt>
<dd><p>The charset value. See MySQL’s
<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and Collations</a>
and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/multibyte.html">Character Set Support</a>
for more details and supported values. Postgres databases are in beta
and have limited <code class="docutils literal notranslate"><span class="pre">charset</span></code> support; they only support a value of <code class="docutils literal notranslate"><span class="pre">UTF8</span></code> at creation time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.collation">
<code class="sig-name descname">collation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.collation" title="Permalink to this definition">¶</a></dt>
<dd><p>The collation value. See MySQL’s
<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and Collations</a>
and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/collation.html">Collation Support</a>
for more details and supported values. Postgres databases are in beta
and have limited <code class="docutils literal notranslate"><span class="pre">collation</span></code> support; they only support a value of <code class="docutils literal notranslate"><span class="pre">en_US.UTF8</span></code> at creation time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.instance">
<code class="sig-name descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of containing instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.Database.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">charset=None</em>, <em class="sig-param">collation=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">self_link=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] charset: The charset value. See MySQL’s</p>
<blockquote>
<div><p><a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and Collations</a>
and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/multibyte.html">Character Set Support</a>
for more details and supported values. Postgres databases are in beta
and have limited <code class="docutils literal notranslate"><span class="pre">charset</span></code> support; they only support a value of <code class="docutils literal notranslate"><span class="pre">UTF8</span></code> at creation time.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The collation value. See MySQL’s
<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and Collations</a>
and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/collation.html">Collation Support</a>
for more details and supported values. Postgres databases are in beta
and have limited <code class="docutils literal notranslate"><span class="pre">collation</span></code> support; they only support a value of <code class="docutils literal notranslate"><span class="pre">en_US.UTF8</span></code> at creation time.</p>
</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of containing instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_database.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_database.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.Database.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.Database.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.DatabaseInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.sql.</code><code class="sig-name descname">DatabaseInstance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database_version=None</em>, <em class="sig-param">master_instance_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">replica_configuration=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new Google SQL Database Instance. For more information, see the <a class="reference external" href="https://cloud.google.com/sql/">official documentation</a>,
or the <a class="reference external" href="https://cloud.google.com/sql/docs/admin-api/v1beta4/instances">JSON API</a>.</p>
<blockquote>
<div><p><strong>NOTE on ``sql.DatabaseInstance``:</strong> - Second-generation instances include a
default ‘root’&#64;’%’ user with no password. This user will be deleted by this provider on
instance creation. You should use <code class="docutils literal notranslate"><span class="pre">sql.User</span></code> to define a custom user with
a restricted host and strong password.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MySQL or PostgreSQL version to
use. Can be <code class="docutils literal notranslate"><span class="pre">MYSQL_5_6</span></code>, <code class="docutils literal notranslate"><span class="pre">MYSQL_5_7</span></code>, <code class="docutils literal notranslate"><span class="pre">POSTGRES_9_6</span></code> or <code class="docutils literal notranslate"><span class="pre">POSTGRES_11</span></code> (beta) for second-generation
instances, or <code class="docutils literal notranslate"><span class="pre">MYSQL_5_5</span></code> or <code class="docutils literal notranslate"><span class="pre">MYSQL_5_6</span></code> for first-generation instances.
See <a class="reference external" href="https://cloud.google.com/sql/docs/1st-2nd-gen-differences">Second Generation Capabilities</a>
for more information.</p></li>
<li><p><strong>master_instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
<code class="docutils literal notranslate"><span class="pre">binary_log_enabled</span></code> set, as well as existing backups.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance. If the name is left
blank, this provider will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to <a class="reference external" href="https://cloud.google.com/sql/docs/delete-instance">one week</a>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region the instance will sit in. Note, first-generation Cloud SQL instance
regions do not line up with the Google Compute Engine (GCE) regions, and Cloud SQL is not
available in all regions - choose from one of the options listed <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/instance-locations">here</a>.
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for all first-generation
instances <em>and</em> for second-generation instances if the provider region is not supported with Cloud SQL.
If you choose not to provide the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument for this resource, make sure you understand this.</p></li>
<li><p><strong>replica_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for replication. The
configuration is detailed below.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings to use for the database. The
configuration is detailed below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_database_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_database_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.connection_name">
<code class="sig-name descname">connection_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.connection_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection name of the instance to be used in
connection strings. For example, when connecting with <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/connect-admin-proxy">Cloud SQL Proxy</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.database_version">
<code class="sig-name descname">database_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.database_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The MySQL or PostgreSQL version to
use. Can be <code class="docutils literal notranslate"><span class="pre">MYSQL_5_6</span></code>, <code class="docutils literal notranslate"><span class="pre">MYSQL_5_7</span></code>, <code class="docutils literal notranslate"><span class="pre">POSTGRES_9_6</span></code> or <code class="docutils literal notranslate"><span class="pre">POSTGRES_11</span></code> (beta) for second-generation
instances, or <code class="docutils literal notranslate"><span class="pre">MYSQL_5_5</span></code> or <code class="docutils literal notranslate"><span class="pre">MYSQL_5_6</span></code> for first-generation instances.
See <a class="reference external" href="https://cloud.google.com/sql/docs/1st-2nd-gen-differences">Second Generation Capabilities</a>
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.master_instance_name">
<code class="sig-name descname">master_instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.master_instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
<code class="docutils literal notranslate"><span class="pre">binary_log_enabled</span></code> set, as well as existing backups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance. If the name is left
blank, this provider will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to <a class="reference external" href="https://cloud.google.com/sql/docs/delete-instance">one week</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.private_ip_address">
<code class="sig-name descname">private_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The first private (<code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>) IPv4 address assigned. This provides a convenient way to access an IP of a specific type without
performing filtering.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.public_ip_address">
<code class="sig-name descname">public_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.public_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The first public (<code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code>) IPv4 address assigned. This provides a convenient way to access an IP of a specific type without
performing filtering.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region the instance will sit in. Note, first-generation Cloud SQL instance
regions do not line up with the Google Compute Engine (GCE) regions, and Cloud SQL is not
available in all regions - choose from one of the options listed <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/instance-locations">here</a>.
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for all first-generation
instances <em>and</em> for second-generation instances if the provider region is not supported with Cloud SQL.
If you choose not to provide the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument for this resource, make sure you understand this.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.replica_configuration">
<code class="sig-name descname">replica_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.replica_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for replication. The
configuration is detailed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.self_link">
<code class="sig-name descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.service_account_email_address">
<code class="sig-name descname">service_account_email_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.service_account_email_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The service account email address assigned to the
instance. This property is applicable only to Second Generation instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.settings">
<code class="sig-name descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The settings to use for the database. The
configuration is detailed below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.DatabaseInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_name=None</em>, <em class="sig-param">database_version=None</em>, <em class="sig-param">first_ip_address=None</em>, <em class="sig-param">ip_addresses=None</em>, <em class="sig-param">master_instance_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">private_ip_address=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">public_ip_address=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">replica_configuration=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">server_ca_cert=None</em>, <em class="sig-param">service_account_email_address=None</em>, <em class="sig-param">settings=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DatabaseInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] connection_name: The connection name of the instance to be used in</p>
<blockquote>
<div><p>connection strings. For example, when connecting with <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/connect-admin-proxy">Cloud SQL Proxy</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>database_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The MySQL or PostgreSQL version to
use. Can be <code class="docutils literal notranslate"><span class="pre">MYSQL_5_6</span></code>, <code class="docutils literal notranslate"><span class="pre">MYSQL_5_7</span></code>, <code class="docutils literal notranslate"><span class="pre">POSTGRES_9_6</span></code> or <code class="docutils literal notranslate"><span class="pre">POSTGRES_11</span></code> (beta) for second-generation
instances, or <code class="docutils literal notranslate"><span class="pre">MYSQL_5_5</span></code> or <code class="docutils literal notranslate"><span class="pre">MYSQL_5_6</span></code> for first-generation instances.
See <a class="reference external" href="https://cloud.google.com/sql/docs/1st-2nd-gen-differences">Second Generation Capabilities</a>
for more information.</p>
</p></li>
<li><p><strong>master_instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
<code class="docutils literal notranslate"><span class="pre">binary_log_enabled</span></code> set, as well as existing backups.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the instance. If the name is left
blank, this provider will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to <a class="reference external" href="https://cloud.google.com/sql/docs/delete-instance">one week</a>.</p>
</p></li>
<li><p><strong>private_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first private (<code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>) IPv4 address assigned. This provides a convenient way to access an IP of a specific type without
performing filtering.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>public_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first public (<code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code>) IPv4 address assigned. This provides a convenient way to access an IP of a specific type without
performing filtering.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The region the instance will sit in. Note, first-generation Cloud SQL instance
regions do not line up with the Google Compute Engine (GCE) regions, and Cloud SQL is not
available in all regions - choose from one of the options listed <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/instance-locations">here</a>.
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for all first-generation
instances <em>and</em> for second-generation instances if the provider region is not supported with Cloud SQL.
If you choose not to provide the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument for this resource, make sure you understand this.</p>
</p></li>
<li><p><strong>replica_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for replication. The
configuration is detailed below.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
<li><p><strong>service_account_email_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service account email address assigned to the
instance. This property is applicable only to Second Generation instances.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings to use for the database. The
configuration is detailed below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_database_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_database_instance.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.DatabaseInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.DatabaseInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.SslCert">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.sql.</code><code class="sig-name descname">SslCert</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">common_name=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.SslCert" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new Google SQL SSL Cert on a Google SQL Instance. For more information, see the <a class="reference external" href="https://cloud.google.com/sql/">official documentation</a>, or the <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/sslCerts">JSON API</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the private key will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>common*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The common name to be used in the certificate to identify the
client. Constrained to [a-zA-Z.-* ]+. Changing this forces a new resource to be created.</p>
</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cloud SQL instance. Changing this
forces a new resource to be created.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_ssl_cert.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_ssl_cert.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.cert">
<code class="sig-name descname">cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The actual certificate data for this client certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.cert_serial_number">
<code class="sig-name descname">cert_serial_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.cert_serial_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The serial number extracted from the certificate data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.common_name">
<code class="sig-name descname">common_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.common_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The common name to be used in the certificate to identify the
client. Constrained to [a-zA-Z.-_ ]+. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.create_time">
<code class="sig-name descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the certificate was created in RFC 3339 format,
for example 2012-11-15T16:19:00.094Z.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.expiration_time">
<code class="sig-name descname">expiration_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.expiration_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the certificate expires in RFC 3339 format,
for example 2012-11-15T16:19:00.094Z.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.instance">
<code class="sig-name descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Cloud SQL instance. Changing this
forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.private_key">
<code class="sig-name descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key associated with the client certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.server_ca_cert">
<code class="sig-name descname">server_ca_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.server_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The CA cert of the server this client cert was generated from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.sha1_fingerprint">
<code class="sig-name descname">sha1_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.sha1_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SHA1 Fingerprint of the certificate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.SslCert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cert=None</em>, <em class="sig-param">cert_serial_number=None</em>, <em class="sig-param">common_name=None</em>, <em class="sig-param">create_time=None</em>, <em class="sig-param">expiration_time=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">server_ca_cert=None</em>, <em class="sig-param">sha1_fingerprint=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.SslCert.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SslCert resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] cert: The actual certificate data for this client certificate.
:param pulumi.Input[str] cert_serial_number: The serial number extracted from the certificate data.
:param pulumi.Input[str] common<a href="#id23"><span class="problematic" id="id24">*</span></a>name: The common name to be used in the certificate to identify the</p>
<blockquote>
<div><p>client. Constrained to [a-zA-Z.-* ]+. Changing this forces a new resource to be created.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the certificate was created in RFC 3339 format,
for example 2012-11-15T16:19:00.094Z.</p></li>
<li><p><strong>expiration_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when the certificate expires in RFC 3339 format,
for example 2012-11-15T16:19:00.094Z.</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cloud SQL instance. Changing this
forces a new resource to be created.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key associated with the client certificate.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>server_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CA cert of the server this client cert was generated from.</p></li>
<li><p><strong>sha1_fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SHA1 Fingerprint of the certificate.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_ssl_cert.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_ssl_cert.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.SslCert.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.SslCert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.SslCert.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.SslCert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.sql.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new Google SQL User on a Google SQL User Instance. For more information, see the <a class="reference external" href="https://cloud.google.com/sql/">official documentation</a>, or the <a class="reference external" href="https://cloud.google.com/sql/docs/admin-api/v1beta4/users">JSON API</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the username and password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>. Passwords will not be retrieved when running import.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host the user can connect from. This is only supported
for MySQL instances. Don’t set this field for PostgreSQL instances.
Can be an IP address. Changing this forces a new resource to be created.</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cloud SQL instance. Changing this
forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user. Changing this forces a new resource
to be created.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the user. Can be updated.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_user.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_user.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.sql.User.host">
<code class="sig-name descname">host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.User.host" title="Permalink to this definition">¶</a></dt>
<dd><p>The host the user can connect from. This is only supported
for MySQL instances. Don’t set this field for PostgreSQL instances.
Can be an IP address. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.User.instance">
<code class="sig-name descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.User.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Cloud SQL instance. Changing this
forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.User.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.User.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user. Changing this forces a new resource
to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.User.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password for the user. Can be updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.User.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.User.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] host: The host the user can connect from. This is only supported</p>
<blockquote>
<div><p>for MySQL instances. Don’t set this field for PostgreSQL instances.
Can be an IP address. Changing this forces a new resource to be created.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cloud SQL instance. Changing this
forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user. Changing this forces a new resource
to be created.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the user. Can be updated.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_user.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_user.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
