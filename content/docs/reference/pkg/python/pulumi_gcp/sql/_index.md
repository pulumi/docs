---
title: Module sql
title_tag: Module sql | Package pulumi_gcp | Python SDK
linktitle: sql
notitle: true
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
<dt id="pulumi_gcp.sql.AwaitableGetCaCertsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.sql.</code><code class="sig-name descname">AwaitableGetCaCertsResult</code><span class="sig-paren">(</span><em class="sig-param">active_version=None</em>, <em class="sig-param">certs=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.AwaitableGetCaCertsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.sql.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.sql.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">charset=None</em>, <em class="sig-param">collation=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a SQL database inside the Cloud SQL instance, hosted in
Google’s cloud.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_database.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_database.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>charset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The charset value. See MySQL’s <a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and
Collations</a> and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/multibyte.html">Character Set
Support</a> for more details and supported values. Postgres
databases only support a value of ‘UTF8’ at creation time.</p></li>
<li><p><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The collation value. See MySQL’s <a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and
Collations</a> and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/collation.html">Collation
Support</a> for more details and supported values. Postgres
databases only support a value of ‘en_US.UTF8’ at creation time.</p>
</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cloud SQL instance. This does not include the project ID.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database in the Cloud SQL instance. This does not include the project ID or instance name.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.charset">
<code class="sig-name descname">charset</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.charset" title="Permalink to this definition">¶</a></dt>
<dd><p>The charset value. See MySQL’s <a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and
Collations</a> and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/multibyte.html">Character Set
Support</a> for more details and supported values. Postgres
databases only support a value of ‘UTF8’ at creation time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.collation">
<code class="sig-name descname">collation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.collation" title="Permalink to this definition">¶</a></dt>
<dd><p>The collation value. See MySQL’s <a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and
Collations</a> and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/collation.html">Collation
Support</a> for more details and supported values. Postgres
databases only support a value of ‘en_US.UTF8’ at creation time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.instance">
<code class="sig-name descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Cloud SQL instance. This does not include the project ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database in the Cloud SQL instance. This does not include the project ID or instance name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.Database.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.Database.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
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
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>charset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The charset value. See MySQL’s <a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and
Collations</a> and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/multibyte.html">Character Set
Support</a> for more details and supported values. Postgres
databases only support a value of ‘UTF8’ at creation time.</p>
</p></li>
<li><p><strong>collation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The collation value. See MySQL’s <a class="reference external" href="https://dev.mysql.com/doc/refman/5.7/en/charset-charsets.html">Supported Character Sets and
Collations</a> and Postgres’ <a class="reference external" href="https://www.postgresql.org/docs/9.6/static/collation.html">Collation
Support</a> for more details and supported values. Postgres
databases only support a value of ‘en_US.UTF8’ at creation time.</p>
</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cloud SQL instance. This does not include the project ID.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database in the Cloud SQL instance. This does not include the project ID or instance name.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.sql.</code><code class="sig-name descname">DatabaseInstance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database_version=None</em>, <em class="sig-param">encryption_key_name=None</em>, <em class="sig-param">master_instance_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">replica_configuration=None</em>, <em class="sig-param">root_password=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new Google SQL Database Instance. For more information, see the <a class="reference external" href="https://cloud.google.com/sql/">official documentation</a>,
or the <a class="reference external" href="https://cloud.google.com/sql/docs/admin-api/v1beta4/instances">JSON API</a>.</p>
<blockquote>
<div><p><strong>NOTE on ``sql.DatabaseInstance``:</strong> - First-generation instances have been
deprecated and should no longer be created, see <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen">upgrade docs</a>
for more details.
To upgrade your First-generation instance, update your config that the instance has</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">settings.ip_configuration.ipv4_enabled=true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">settings.backup_configuration.enabled=true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">settings.backup_configuration.binary_log_enabled=true</span></code>.<span class="raw-html-m2r"><br></span>
Apply the config, then upgrade the instance in the console as described in the documentation.
Once upgraded, update the following attributes in your config to the correct value according to
the above documentation:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">database_version</span></code> (if applicable)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code><span class="raw-html-m2r"><br></span>
Remove any fields that are not applicable to Second-generation instances:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">settings.crash_safe_replication</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">settings.replication_type</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">settings.authorized_gae_applications</span></code>
And change values to appropriate values for Second-generation instances for:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">activation_policy</span></code> (“ON_DEMAND” is no longer an option)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pricing_plan</span></code> (“PER_USE” is now the only valid option)
Change <code class="docutils literal notranslate"><span class="pre">settings.backup_configuration.enabled</span></code> attribute back to its desired value and apply as necessary.</p></li>
</ul>
<p><strong>NOTE on ``sql.DatabaseInstance``:</strong> - Second-generation instances include a
default ‘root’&#64;’%’ user with no password. This user will be deleted by the provider on
instance creation. You should use <code class="docutils literal notranslate"><span class="pre">sql.User</span></code> to define a custom user with
a restricted host and strong password.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_database_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_database_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MySQL, PostgreSQL or
SQL Server (beta) version to use. Supported values include <code class="docutils literal notranslate"><span class="pre">MYSQL_5_6</span></code>,
<code class="docutils literal notranslate"><span class="pre">MYSQL_5_7</span></code>, <code class="docutils literal notranslate"><span class="pre">POSTGRES_9_6</span></code>,<code class="docutils literal notranslate"><span class="pre">POSTGRES_11</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLSERVER_2017_STANDARD</span></code>,
<code class="docutils literal notranslate"><span class="pre">SQLSERVER_2017_ENTERPRISE</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLSERVER_2017_EXPRESS</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLSERVER_2017_WEB</span></code>.
<a class="reference external" href="https://cloud.google.com/sql/docs/sqlserver/db-versions">Database Version Policies</a>
includes an up-to-date reference of supported versions.</p></li>
<li><p><strong>encryption_key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The full path to the encryption key used for the CMEK disk encryption.  Setting
up disk encryption currently requires manual steps outside of this provider.
The provided key must be in the same region as the SQL instance.  In order
to use this feature, a special kind of service account must be created and
granted permission on this key.  This step can currently only be done
manually, please see <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account">this step</a>.
That service account needs the <code class="docutils literal notranslate"><span class="pre">Cloud</span> <span class="pre">KMS</span> <span class="pre">&gt;</span> <span class="pre">Cloud</span> <span class="pre">KMS</span> <span class="pre">CryptoKey</span> <span class="pre">Encrypter/Decrypter</span></code> role on your
key - please see <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey">this step</a>.</p>
</p></li>
<li><p><strong>master_instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
<code class="docutils literal notranslate"><span class="pre">binary_log_enabled</span></code> set, as well as existing backups.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance. If the name is left
blank, the provider will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to <a class="reference external" href="https://cloud.google.com/sql/docs/delete-instance">one week</a>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region the instance will sit in. Note, Cloud SQL is not
available in all regions - choose from one of the options listed <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/instance-locations">here</a>.
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for instances if the provider
region is not supported with Cloud SQL. If you choose not to provide the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument for this resource,
make sure you understand this.</p></li>
<li><p><strong>replica_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for replication. The
configuration is detailed below.</p></li>
<li><p><strong>root_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings to use for the database. The
configuration is detailed below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>replica_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectRetryInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dumpFilePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failoverTarget</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterHeartbeatPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCipher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verifyServerCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">activationPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizedGaeApplications</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">availabilityType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">binaryLogEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">crashSafeReplication</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">databaseFlags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the instance. If the name is left
blank, the provider will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to <a class="reference external" href="https://cloud.google.com/sql/docs/delete-instance">one week</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskAutoresize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizedNetworks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">expiration_time</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the instance. If the name is left
blank, the provider will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to <a class="reference external" href="https://cloud.google.com/sql/docs/delete-instance">one week</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateNetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">locationPreference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">followGaeApplication</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maintenanceWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">day</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updateTrack</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pricingPlan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicationType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.connection_name">
<code class="sig-name descname">connection_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.connection_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection name of the instance to be used in
connection strings. For example, when connecting with <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/connect-admin-proxy">Cloud SQL Proxy</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.database_version">
<code class="sig-name descname">database_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.database_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The MySQL, PostgreSQL or
SQL Server (beta) version to use. Supported values include <code class="docutils literal notranslate"><span class="pre">MYSQL_5_6</span></code>,
<code class="docutils literal notranslate"><span class="pre">MYSQL_5_7</span></code>, <code class="docutils literal notranslate"><span class="pre">POSTGRES_9_6</span></code>,<code class="docutils literal notranslate"><span class="pre">POSTGRES_11</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLSERVER_2017_STANDARD</span></code>,
<code class="docutils literal notranslate"><span class="pre">SQLSERVER_2017_ENTERPRISE</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLSERVER_2017_EXPRESS</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLSERVER_2017_WEB</span></code>.
<a class="reference external" href="https://cloud.google.com/sql/docs/sqlserver/db-versions">Database Version Policies</a>
includes an up-to-date reference of supported versions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.encryption_key_name">
<code class="sig-name descname">encryption_key_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.encryption_key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full path to the encryption key used for the CMEK disk encryption.  Setting
up disk encryption currently requires manual steps outside of this provider.
The provided key must be in the same region as the SQL instance.  In order
to use this feature, a special kind of service account must be created and
granted permission on this key.  This step can currently only be done
manually, please see <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account">this step</a>.
That service account needs the <code class="docutils literal notranslate"><span class="pre">Cloud</span> <span class="pre">KMS</span> <span class="pre">&gt;</span> <span class="pre">Cloud</span> <span class="pre">KMS</span> <span class="pre">CryptoKey</span> <span class="pre">Encrypter/Decrypter</span></code> role on your
key - please see <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey">this step</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.first_ip_address">
<code class="sig-name descname">first_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.first_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The first IPv4 address of any type assigned.</p>
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
blank, the provider will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to <a class="reference external" href="https://cloud.google.com/sql/docs/delete-instance">one week</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.private_ip_address">
<code class="sig-name descname">private_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The first private (<code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>) IPv4 address assigned.</p>
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
<dd><p>The first public (<code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code>) IPv4 address assigned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region the instance will sit in. Note, Cloud SQL is not
available in all regions - choose from one of the options listed <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/instance-locations">here</a>.
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for instances if the provider
region is not supported with Cloud SQL. If you choose not to provide the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument for this resource,
make sure you understand this.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.replica_configuration">
<code class="sig-name descname">replica_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.replica_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for replication. The
configuration is detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectRetryInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dumpFilePath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failoverTarget</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterHeartbeatPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCipher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verifyServerCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.root_password">
<code class="sig-name descname">root_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.root_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.</p>
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
instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.DatabaseInstance.settings">
<code class="sig-name descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The settings to use for the database. The
configuration is detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">activationPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizedGaeApplications</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">availabilityType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">binaryLogEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">crashSafeReplication</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">databaseFlags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the instance. If the name is left
blank, the provider will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to <a class="reference external" href="https://cloud.google.com/sql/docs/delete-instance">one week</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskAutoresize</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizedNetworks</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">expiration_time</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the instance. If the name is left
blank, the provider will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to <a class="reference external" href="https://cloud.google.com/sql/docs/delete-instance">one week</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateNetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">locationPreference</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">followGaeApplication</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maintenanceWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">day</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hour</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updateTrack</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pricingPlan</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicationType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.DatabaseInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_name=None</em>, <em class="sig-param">database_version=None</em>, <em class="sig-param">encryption_key_name=None</em>, <em class="sig-param">first_ip_address=None</em>, <em class="sig-param">ip_addresses=None</em>, <em class="sig-param">master_instance_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">private_ip_address=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">public_ip_address=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">replica_configuration=None</em>, <em class="sig-param">root_password=None</em>, <em class="sig-param">self_link=None</em>, <em class="sig-param">server_ca_cert=None</em>, <em class="sig-param">service_account_email_address=None</em>, <em class="sig-param">settings=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.DatabaseInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DatabaseInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The connection name of the instance to be used in
connection strings. For example, when connecting with <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/connect-admin-proxy">Cloud SQL Proxy</a>.</p>
</p></li>
<li><p><strong>database_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The MySQL, PostgreSQL or
SQL Server (beta) version to use. Supported values include <code class="docutils literal notranslate"><span class="pre">MYSQL_5_6</span></code>,
<code class="docutils literal notranslate"><span class="pre">MYSQL_5_7</span></code>, <code class="docutils literal notranslate"><span class="pre">POSTGRES_9_6</span></code>,<code class="docutils literal notranslate"><span class="pre">POSTGRES_11</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLSERVER_2017_STANDARD</span></code>,
<code class="docutils literal notranslate"><span class="pre">SQLSERVER_2017_ENTERPRISE</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLSERVER_2017_EXPRESS</span></code>, <code class="docutils literal notranslate"><span class="pre">SQLSERVER_2017_WEB</span></code>.
<a class="reference external" href="https://cloud.google.com/sql/docs/sqlserver/db-versions">Database Version Policies</a>
includes an up-to-date reference of supported versions.</p>
</p></li>
<li><p><strong>encryption_key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The full path to the encryption key used for the CMEK disk encryption.  Setting
up disk encryption currently requires manual steps outside of this provider.
The provided key must be in the same region as the SQL instance.  In order
to use this feature, a special kind of service account must be created and
granted permission on this key.  This step can currently only be done
manually, please see <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account">this step</a>.
That service account needs the <code class="docutils literal notranslate"><span class="pre">Cloud</span> <span class="pre">KMS</span> <span class="pre">&gt;</span> <span class="pre">Cloud</span> <span class="pre">KMS</span> <span class="pre">CryptoKey</span> <span class="pre">Encrypter/Decrypter</span></code> role on your
key - please see <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey">this step</a>.</p>
</p></li>
<li><p><strong>first_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first IPv4 address of any type assigned.</p></li>
<li><p><strong>master_instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
<code class="docutils literal notranslate"><span class="pre">binary_log_enabled</span></code> set, as well as existing backups.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the instance. If the name is left
blank, the provider will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to <a class="reference external" href="https://cloud.google.com/sql/docs/delete-instance">one week</a>.</p>
</p></li>
<li><p><strong>private_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first private (<code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>) IPv4 address assigned.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>public_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first public (<code class="docutils literal notranslate"><span class="pre">PRIMARY</span></code>) IPv4 address assigned.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The region the instance will sit in. Note, Cloud SQL is not
available in all regions - choose from one of the options listed <a class="reference external" href="https://cloud.google.com/sql/docs/mysql/instance-locations">here</a>.
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for instances if the provider
region is not supported with Cloud SQL. If you choose not to provide the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument for this resource,
make sure you understand this.</p>
</p></li>
<li><p><strong>replica_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration for replication. The
configuration is detailed below.</p></li>
<li><p><strong>root_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.</p></li>
<li><p><strong>self_link</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the created resource.</p></li>
<li><p><strong>service_account_email_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service account email address assigned to the
instance.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings to use for the database. The
configuration is detailed below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_addresses</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeToRetire</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>replica_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectRetryInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dumpFilePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failoverTarget</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterHeartbeatPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCipher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">verifyServerCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>server_ca_cert</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cert</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">common_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create_time</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expiration_time</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sha1_fingerprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">activationPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizedGaeApplications</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">availabilityType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backupConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">binaryLogEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">location</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">crashSafeReplication</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">databaseFlags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the instance. If the name is left
blank, the provider will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to <a class="reference external" href="https://cloud.google.com/sql/docs/delete-instance">one week</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskAutoresize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authorizedNetworks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">expiration_time</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the instance. If the name is left
blank, the provider will randomly generate one when the instance is first
created. This is done because after a name is used, it cannot be reused for
up to <a class="reference external" href="https://cloud.google.com/sql/docs/delete-instance">one week</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipv4Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateNetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">locationPreference</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">followGaeApplication</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maintenanceWindow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">day</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">updateTrack</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pricingPlan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">replicationType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
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
<dt id="pulumi_gcp.sql.GetCaCertsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.sql.</code><code class="sig-name descname">GetCaCertsResult</code><span class="sig-paren">(</span><em class="sig-param">active_version=None</em>, <em class="sig-param">certs=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">instance=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.GetCaCertsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCaCerts.</p>
<dl class="attribute">
<dt id="pulumi_gcp.sql.GetCaCertsResult.active_version">
<code class="sig-name descname">active_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.GetCaCertsResult.active_version" title="Permalink to this definition">¶</a></dt>
<dd><p>SHA1 fingerprint of the currently active CA certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.GetCaCertsResult.certs">
<code class="sig-name descname">certs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.GetCaCertsResult.certs" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of server CA certificates for the instance. Each contains:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.GetCaCertsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.GetCaCertsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.sql.SourceRepresentationInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.sql.</code><code class="sig-name descname">SourceRepresentationInstance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database_version=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.SourceRepresentationInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>A source representation instance is a Cloud SQL instance that represents
the source database server to the Cloud SQL replica. It is visible in the
Cloud Console and appears the same as a regular Cloud SQL instance, but it
contains no data, requires no configuration or maintenance, and does not
affect billing. You cannot update the source representation instance.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_source_representation_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_source_representation_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MySQL version running on your source database server: MYSQL_5_6 or MYSQL_5_7.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The externally accessible IPv4 address for the source database server.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the source representation instance. Use any valid Cloud SQL instance name.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The externally accessible port for the source database server. Defaults to 3306.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Region in which the created instance should reside. If it is not provided, the provider region is used.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.sql.SourceRepresentationInstance.database_version">
<code class="sig-name descname">database_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SourceRepresentationInstance.database_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The MySQL version running on your source database server: MYSQL_5_6 or MYSQL_5_7.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SourceRepresentationInstance.host">
<code class="sig-name descname">host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SourceRepresentationInstance.host" title="Permalink to this definition">¶</a></dt>
<dd><p>The externally accessible IPv4 address for the source database server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SourceRepresentationInstance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SourceRepresentationInstance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the source representation instance. Use any valid Cloud SQL instance name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SourceRepresentationInstance.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SourceRepresentationInstance.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The externally accessible port for the source database server. Defaults to 3306.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SourceRepresentationInstance.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SourceRepresentationInstance.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.sql.SourceRepresentationInstance.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.sql.SourceRepresentationInstance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The Region in which the created instance should reside. If it is not provided, the provider region is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.SourceRepresentationInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">database_version=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.SourceRepresentationInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SourceRepresentationInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The MySQL version running on your source database server: MYSQL_5_6 or MYSQL_5_7.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The externally accessible IPv4 address for the source database server.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the source representation instance. Use any valid Cloud SQL instance name.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The externally accessible port for the source database server. Defaults to 3306.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Region in which the created instance should reside. If it is not provided, the provider region is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.sql.SourceRepresentationInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.SourceRepresentationInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.sql.SourceRepresentationInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.SourceRepresentationInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_ssl_cert.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_ssl_cert.html.markdown</a>.</p>
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
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The actual certificate data for this client certificate.</p></li>
<li><p><strong>cert_serial_number</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The serial number extracted from the certificate data.</p></li>
<li><p><strong>common*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The common name to be used in the certificate to identify the
client. Constrained to [a-zA-Z.-* ]+. Changing this forces a new resource to be created.</p>
</p></li>
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
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_user.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_user.html.markdown</a>.</p>
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
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the user. Can be updated. For Postgres
instances this is a Required field.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
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
<dd><p>The password for the user. Can be updated. For Postgres
instances this is a Required field.</p>
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
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host the user can connect from. This is only supported
for MySQL instances. Don’t set this field for PostgreSQL instances.
Can be an IP address. Changing this forces a new resource to be created.</p></li>
<li><p><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Cloud SQL instance. Changing this
forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user. Changing this forces a new resource
to be created.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the user. Can be updated. For Postgres
instances this is a Required field.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
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

<dl class="function">
<dt id="pulumi_gcp.sql.get_ca_certs">
<code class="sig-prename descclassname">pulumi_gcp.sql.</code><code class="sig-name descname">get_ca_certs</code><span class="sig-paren">(</span><em class="sig-param">instance=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.sql.get_ca_certs" title="Permalink to this definition">¶</a></dt>
<dd><p>Get all of the trusted Certificate Authorities (CAs) for the specified SQL database instance. For more information see the
<a class="reference external" href="https://cloud.google.com/sql/">official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/listServerCas">API</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_google_sql_ca_certs.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_google_sql_ca_certs.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>instance</strong> (<em>str</em>) – The name or self link of the instance.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The ID of the project in which the resource belongs. If <code class="docutils literal notranslate"><span class="pre">project</span></code> is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
