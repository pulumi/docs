<div class="section" id="module-pulumi_gcp.sql">
<span id="sql"></span><h1>sql<a class="headerlink" href="#module-pulumi_gcp.sql" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.sql.Database">
<em class="property">class </em><code class="descclassname">pulumi_gcp.sql.</code><code class="descname">Database</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>charset=None</em>, <em>collation=None</em>, <em>instance=None</em>, <em>name=None</em>, <em>project=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new Google SQL Database on a Google SQL Database Instance. For more information, see
the <a class="reference external" href="https://cloud.google.com/sql/">official documentation</a>,
or the <a class="reference external" href="https://cloud.google.com/sql/docs/admin-api/v1beta4/databases">JSON API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>charset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The charset value. See MySQL’s
<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and Collations</a>
and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/multibyte.html">Character Set Support</a>
for more details and supported values. Postgres databases are in beta
and have limited <code class="docutils literal notranslate"><span class="pre">charset</span></code> support; they only support a value of <code class="docutils literal notranslate"><span class="pre">UTF8</span></code> at creation time.</li>
<li><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The collation value. See MySQL’s
<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and Collations</a>
and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/collation.html">Collation Support</a>
for more details and supported values. Postgres databases are in beta
and have limited <code class="docutils literal notranslate"><span class="pre">collation</span></code> support; they only support a value of <code class="docutils literal notranslate"><span class="pre">en_US.UTF8</span></code> at creation time.</p>
</li>
<li><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of containing instance.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.charset">
<code class="descname">charset</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.charset" title="Permalink to this definition">¶</a></dt>
<dd><p>The charset value. See MySQL’s
<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and Collations</a>
and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/multibyte.html">Character Set Support</a>
for more details and supported values. Postgres databases are in beta
and have limited <code class="docutils literal notranslate"><span class="pre">charset</span></code> support; they only support a value of <code class="docutils literal notranslate"><span class="pre">UTF8</span></code> at creation time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.collation">
<code class="descname">collation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.collation" title="Permalink to this definition">¶</a></dt>
<dd><p>The collation value. See MySQL’s
<a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and Collations</a>
and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/collation.html">Collation Support</a>
for more details and supported values. Postgres databases are in beta
and have limited <code class="docutils literal notranslate"><span class="pre">collation</span></code> support; they only support a value of <code class="docutils literal notranslate"><span class="pre">en_US.UTF8</span></code> at creation time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.instance">
<code class="descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of containing instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.Database.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.Database.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.DatabaseInstance">
<em class="property">class </em><code class="descclassname">pulumi_gcp.sql.</code><code class="descname">DatabaseInstance</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>database_version=None</em>, <em>master_instance_name=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>replica_configuration=None</em>, <em>settings=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new Google SQL Database Instance. For more information, see the <a class="reference external" href="https://cloud.google.com/sql/">official documentation</a>,
or the <a class="reference external" href="https://cloud.google.com/sql/docs/admin-api/v1beta4/instances">JSON API</a>.</p>
<blockquote>
<div><strong>NOTE on ``google_sql_database_instance``:</strong> - Second-generation instances include a
default ‘root’&#64;’%’ user with no password. This user will be deleted by Terraform on
instance creation. You should use <code class="docutils literal notranslate"><span class="pre">google_sql_user</span></code> to define a custom user with
a restricted host and strong password.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>database_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MySQL version to
use. Can be <code class="docutils literal notranslate"><span class="pre">MYSQL_5_6</span></code>, <code class="docutils literal notranslate"><span class="pre">MYSQL_5_7</span></code> or <code class="docutils literal notranslate"><span class="pre">POSTGRES_9_6</span></code> for second-generation
instances, or <code class="docutils literal notranslate"><span class="pre">MYSQL_5_5</span></code> or <code class="docutils literal notranslate"><span class="pre">MYSQL_5_6</span></code> for first-generation instances.
See <a class="reference external" href="https://cloud.google.com/sql/docs/1st-2nd-gen-differences">Second Generation Capabilities</a>
for more information. <code class="docutils literal notranslate"><span class="pre">POSTGRES_9_6</span></code> support is in beta.</li>
<li><strong>master_instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
<code class="docutils literal notranslate"><span class="pre">binary_log_enabled</span></code> set, as well as existing backups.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance. If the name is left
blank, Terraform will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to <a class="reference external" href="https://cloud.google.com/sql/docs/delete-instance">one week</a>.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region the instance will sit in. Note, first-generation Cloud SQL instance
regions do not line up with the Google Compute Engine (GCE) regions, and Cloud SQL is not
available in all regions - choose from one of the options listed <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/instance-locations">here</a>.
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for all first-generation
instances <em>and</em> for second-generation instances if the provider region is not supported with Cloud SQL.
If you choose not to provide the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument for this resource, make sure you understand this.</li>
<li><strong>replica_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for replication. The
configuration is detailed below.</li>
<li><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings to use for the database. The
configuration is detailed below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.connection_name">
<code class="descname">connection_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.connection_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection name of the instance to be used in connection strings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.database_version">
<code class="descname">database_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.database_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The MySQL version to
use. Can be <code class="docutils literal notranslate"><span class="pre">MYSQL_5_6</span></code>, <code class="docutils literal notranslate"><span class="pre">MYSQL_5_7</span></code> or <code class="docutils literal notranslate"><span class="pre">POSTGRES_9_6</span></code> for second-generation
instances, or <code class="docutils literal notranslate"><span class="pre">MYSQL_5_5</span></code> or <code class="docutils literal notranslate"><span class="pre">MYSQL_5_6</span></code> for first-generation instances.
See <a class="reference external" href="https://cloud.google.com/sql/docs/1st-2nd-gen-differences">Second Generation Capabilities</a>
for more information. <code class="docutils literal notranslate"><span class="pre">POSTGRES_9_6</span></code> support is in beta.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.first_ip_address">
<code class="descname">first_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.first_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The first IPv4 address of the addresses assigned. This is
is to support accessing the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues/912">first address in the list in a terraform output</a>
when the resource is configured with a <code class="docutils literal notranslate"><span class="pre">count</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.master_instance_name">
<code class="descname">master_instance_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.master_instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
<code class="docutils literal notranslate"><span class="pre">binary_log_enabled</span></code> set, as well as existing backups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance. If the name is left
blank, Terraform will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to <a class="reference external" href="https://cloud.google.com/sql/docs/delete-instance">one week</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.region" title="Permalink to this definition">¶</a></dt>
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
<code class="descname">replica_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.replica_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for replication. The
configuration is detailed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.self_link">
<code class="descname">self_link</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.self_link" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the created resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.service_account_email_address">
<code class="descname">service_account_email_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.service_account_email_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The service account email address assigned to the
instance. This property is applicable only to Second Generation instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.settings">
<code class="descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The settings to use for the database. The
configuration is detailed below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.DatabaseInstance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.DatabaseInstance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.SslCert">
<em class="property">class </em><code class="descclassname">pulumi_gcp.sql.</code><code class="descname">SslCert</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>common_name=None</em>, <em>instance=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.SslCert" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new Google SQL SSL Cert on a Google SQL Instance. For more information, see the <a class="reference external" href="https://cloud.google.com/sql/">official documentation</a>, or the <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/sslCerts">JSON API</a>.</p>
<blockquote>
<div><strong>Note:</strong> All arguments including the private key will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>common*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The common name to be used in the certificate to identify the 
client. Constrained to [a-zA-Z.-* ]+. Changing this forces a new resource to be created.</p>
</li>
<li><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cloud SQL instance. Changing this
forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.cert">
<code class="descname">cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The actual certificate data for this client certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.cert_serial_number">
<code class="descname">cert_serial_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.cert_serial_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The serial number extracted from the certificate data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.common_name">
<code class="descname">common_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.common_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The common name to be used in the certificate to identify the 
client. Constrained to [a-zA-Z.-_ ]+. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.create_time">
<code class="descname">create_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the certificate was created in RFC 3339 format, 
for example 2012-11-15T16:19:00.094Z.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.expiration_time">
<code class="descname">expiration_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.expiration_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when the certificate expires in RFC 3339 format, 
for example 2012-11-15T16:19:00.094Z.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.instance">
<code class="descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Cloud SQL instance. Changing this
forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.private_key">
<code class="descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key associated with the client certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.server_ca_cert">
<code class="descname">server_ca_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.server_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>The CA cert of the server this client cert was generated from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SslCert.sha1_fingerprint">
<code class="descname">sha1_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SslCert.sha1_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The SHA1 Fingerprint of the certificate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.SslCert.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.SslCert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.SslCert.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.SslCert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.User">
<em class="property">class </em><code class="descclassname">pulumi_gcp.sql.</code><code class="descname">User</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>host=None</em>, <em>instance=None</em>, <em>name=None</em>, <em>password=None</em>, <em>project=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new Google SQL User on a Google SQL User Instance. For more information, see the <a class="reference external" href="https://cloud.google.com/sql/">official documentation</a>, or the <a class="reference external" href="https://cloud.google.com/sql/docs/admin-api/v1beta4/users">JSON API</a>.</p>
<blockquote>
<div><strong>Note:</strong> All arguments including the username and password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>. Passwords will not be retrieved when running
“terraform import”.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host the user can connect from. This is only supported
for MySQL instances. Don’t set this field for PostgreSQL instances.
Can be an IP address. Changing this forces a new resource to be created.</li>
<li><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cloud SQL instance. Changing this
forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user. Changing this forces a new resource
to be created.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the user. Can be updated.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.sql.User.host">
<code class="descname">host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.User.host" title="Permalink to this definition">¶</a></dt>
<dd><p>The host the user can connect from. This is only supported
for MySQL instances. Don’t set this field for PostgreSQL instances.
Can be an IP address. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.User.instance">
<code class="descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.User.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Cloud SQL instance. Changing this
forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.User.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.User.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user. Changing this forces a new resource
to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.User.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password for the user. Can be updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.User.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.User.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.User.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.User.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
