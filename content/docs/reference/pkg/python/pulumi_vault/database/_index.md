---
title: Module database
title_tag: Module database | Package pulumi_vault | Python SDK
linktitle: database
notitle: true
---

<div class="section" id="database">
<h1>database<a class="headerlink" href="#database" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.database"></span><dl class="class">
<dt id="pulumi_vault.database.SecretBackendConnection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.database.</code><code class="sig-name descname">SecretBackendConnection</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowed_roles=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">cassandra=None</em>, <em class="sig-param">data=None</em>, <em class="sig-param">hana=None</em>, <em class="sig-param">mongodb=None</em>, <em class="sig-param">mssql=None</em>, <em class="sig-param">mysql=None</em>, <em class="sig-param">mysql_aurora=None</em>, <em class="sig-param">mysql_legacy=None</em>, <em class="sig-param">mysql_rds=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">oracle=None</em>, <em class="sig-param">postgresql=None</em>, <em class="sig-param">root_rotation_statements=None</em>, <em class="sig-param">verify_connection=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretBackendConnection resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of roles that are allowed to use this
connection.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the Vault mount to configure.</p></li>
<li><p><strong>cassandra</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for Cassandra connections.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of sensitive data to pass to the endpoint. Useful for templated connection strings.</p></li>
<li><p><strong>hana</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for SAP HanaDB connections.</p></li>
<li><p><strong>mongodb</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for MongoDB connections.</p></li>
<li><p><strong>mssql</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for MSSQL connections.</p></li>
<li><p><strong>mysql</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for MySQL connections.</p></li>
<li><p><strong>mysql_aurora</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for Aurora MySQL connections.</p></li>
<li><p><strong>mysql_legacy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for legacy MySQL connections.</p></li>
<li><p><strong>mysql_rds</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for RDS MySQL connections.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name to give the database connection.</p></li>
<li><p><strong>oracle</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for Oracle connections.</p></li>
<li><p><strong>postgresql</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for PostgreSQL connections.</p></li>
<li><p><strong>root_rotation_statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of database statements to be executed to rotate the root user’s credentials.</p></li>
<li><p><strong>verify_connection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the connection should be verified on
initial configuration or not.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cassandra</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of seconds to use as a connection
timeout.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The hosts to connect to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to skip verification of the server
certificate when using TLS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password to authenticate with.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pemBundle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Concatenated PEM blocks configuring the certificate
chain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pemJson</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A JSON structure configuring the certificate chain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The default port to connect to if no port is specified as
part of the host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocolVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The CQL protocol version to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS when connecting to Cassandra.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username to authenticate with.</p></li>
</ul>
<p>The <strong>hana</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>mongodb</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>mssql</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>mysql</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>mysql_aurora</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>mysql_legacy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>mysql_rds</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>oracle</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>postgresql</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/database_secret_backend_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/database_secret_backend_connection.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.allowed_roles">
<code class="sig-name descname">allowed_roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.allowed_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of roles that are allowed to use this
connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name of the Vault mount to configure.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.cassandra">
<code class="sig-name descname">cassandra</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.cassandra" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block containing configuration options for Cassandra connections.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of seconds to use as a connection
timeout.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hosts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The hosts to connect to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureTls</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to skip verification of the server
certificate when using TLS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password to authenticate with.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pemBundle</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Concatenated PEM blocks configuring the certificate
chain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pemJson</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A JSON structure configuring the certificate chain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The default port to connect to if no port is specified as
part of the host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocolVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The CQL protocol version to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to use TLS when connecting to Cassandra.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username to authenticate with.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.data">
<code class="sig-name descname">data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.data" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of sensitive data to pass to the endpoint. Useful for templated connection strings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.hana">
<code class="sig-name descname">hana</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.hana" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block containing configuration options for SAP HanaDB connections.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.mongodb">
<code class="sig-name descname">mongodb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.mongodb" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block containing configuration options for MongoDB connections.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.mssql">
<code class="sig-name descname">mssql</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.mssql" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block containing configuration options for MSSQL connections.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.mysql">
<code class="sig-name descname">mysql</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.mysql" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block containing configuration options for MySQL connections.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.mysql_aurora">
<code class="sig-name descname">mysql_aurora</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.mysql_aurora" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block containing configuration options for Aurora MySQL connections.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.mysql_legacy">
<code class="sig-name descname">mysql_legacy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.mysql_legacy" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block containing configuration options for legacy MySQL connections.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.mysql_rds">
<code class="sig-name descname">mysql_rds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.mysql_rds" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block containing configuration options for RDS MySQL connections.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name to give the database connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.oracle">
<code class="sig-name descname">oracle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.oracle" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block containing configuration options for Oracle connections.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.postgresql">
<code class="sig-name descname">postgresql</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.postgresql" title="Permalink to this definition">¶</a></dt>
<dd><p>A nested block containing configuration options for PostgreSQL connections.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.root_rotation_statements">
<code class="sig-name descname">root_rotation_statements</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.root_rotation_statements" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of database statements to be executed to rotate the root user’s credentials.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendConnection.verify_connection">
<code class="sig-name descname">verify_connection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.verify_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the connection should be verified on
initial configuration or not.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.database.SecretBackendConnection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowed_roles=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">cassandra=None</em>, <em class="sig-param">data=None</em>, <em class="sig-param">hana=None</em>, <em class="sig-param">mongodb=None</em>, <em class="sig-param">mssql=None</em>, <em class="sig-param">mysql=None</em>, <em class="sig-param">mysql_aurora=None</em>, <em class="sig-param">mysql_legacy=None</em>, <em class="sig-param">mysql_rds=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">oracle=None</em>, <em class="sig-param">postgresql=None</em>, <em class="sig-param">root_rotation_statements=None</em>, <em class="sig-param">verify_connection=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendConnection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of roles that are allowed to use this
connection.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the Vault mount to configure.</p></li>
<li><p><strong>cassandra</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for Cassandra connections.</p></li>
<li><p><strong>data</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of sensitive data to pass to the endpoint. Useful for templated connection strings.</p></li>
<li><p><strong>hana</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for SAP HanaDB connections.</p></li>
<li><p><strong>mongodb</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for MongoDB connections.</p></li>
<li><p><strong>mssql</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for MSSQL connections.</p></li>
<li><p><strong>mysql</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for MySQL connections.</p></li>
<li><p><strong>mysql_aurora</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for Aurora MySQL connections.</p></li>
<li><p><strong>mysql_legacy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for legacy MySQL connections.</p></li>
<li><p><strong>mysql_rds</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for RDS MySQL connections.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name to give the database connection.</p></li>
<li><p><strong>oracle</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for Oracle connections.</p></li>
<li><p><strong>postgresql</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A nested block containing configuration options for PostgreSQL connections.</p></li>
<li><p><strong>root_rotation_statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of database statements to be executed to rotate the root user’s credentials.</p></li>
<li><p><strong>verify_connection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the connection should be verified on
initial configuration or not.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cassandra</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of seconds to use as a connection
timeout.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The hosts to connect to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureTls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to skip verification of the server
certificate when using TLS.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password to authenticate with.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pemBundle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Concatenated PEM blocks configuring the certificate
chain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pemJson</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A JSON structure configuring the certificate chain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The default port to connect to if no port is specified as
part of the host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocolVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The CQL protocol version to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to use TLS when connecting to Cassandra.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username to authenticate with.</p></li>
</ul>
<p>The <strong>hana</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>mongodb</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>mssql</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>mysql</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>mysql_aurora</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>mysql_legacy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>mysql_rds</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>oracle</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<p>The <strong>postgresql</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectionUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A URL containing connection information. See
the <a class="reference external" href="https://www.vaultproject.io/api/secret/databases/oracle.html#sample-payload">Vault
docs</a>
for an example.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConnectionLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of seconds to keep
a connection alive for.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxIdleConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of idle connections to
maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxOpenConnections</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of open connections to
use.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/database_secret_backend_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/database_secret_backend_connection.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.database.SecretBackendConnection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.database.SecretBackendConnection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.database.SecretBackendConnection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.database.SecretBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.database.</code><code class="sig-name descname">SecretBackendRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">creation_statements=None</em>, <em class="sig-param">db_name=None</em>, <em class="sig-param">default_ttl=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">renew_statements=None</em>, <em class="sig-param">revocation_statements=None</em>, <em class="sig-param">rollback_statements=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.database.SecretBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretBackendRole resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the Vault mount to configure.</p></li>
<li><p><strong>creation_statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The database statements to execute when
creating a user.</p></li>
<li><p><strong>db_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the database connection to use for
the role.</p></li>
<li><p><strong>default_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default number of seconds for leases for this
role.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of seconds for leases for this
role.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name to give the role.</p></li>
<li><p><strong>renew_statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The database statements to execute when
renewing a user.</p></li>
<li><p><strong>revocation_statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The database statements to execute when
revoking a user.</p></li>
<li><p><strong>rollback_statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The database statements to execute when
rolling back creation due to an error.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/database_secret_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/database_secret_backend_role.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendRole.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name of the Vault mount to configure.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendRole.creation_statements">
<code class="sig-name descname">creation_statements</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendRole.creation_statements" title="Permalink to this definition">¶</a></dt>
<dd><p>The database statements to execute when
creating a user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendRole.db_name">
<code class="sig-name descname">db_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendRole.db_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name of the database connection to use for
the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendRole.default_ttl">
<code class="sig-name descname">default_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendRole.default_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The default number of seconds for leases for this
role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendRole.max_ttl">
<code class="sig-name descname">max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendRole.max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of seconds for leases for this
role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendRole.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendRole.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name to give the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendRole.renew_statements">
<code class="sig-name descname">renew_statements</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendRole.renew_statements" title="Permalink to this definition">¶</a></dt>
<dd><p>The database statements to execute when
renewing a user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendRole.revocation_statements">
<code class="sig-name descname">revocation_statements</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendRole.revocation_statements" title="Permalink to this definition">¶</a></dt>
<dd><p>The database statements to execute when
revoking a user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendRole.rollback_statements">
<code class="sig-name descname">rollback_statements</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendRole.rollback_statements" title="Permalink to this definition">¶</a></dt>
<dd><p>The database statements to execute when
rolling back creation due to an error.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.database.SecretBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">creation_statements=None</em>, <em class="sig-param">db_name=None</em>, <em class="sig-param">default_ttl=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">renew_statements=None</em>, <em class="sig-param">revocation_statements=None</em>, <em class="sig-param">rollback_statements=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.database.SecretBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the Vault mount to configure.</p></li>
<li><p><strong>creation_statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The database statements to execute when
creating a user.</p></li>
<li><p><strong>db_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the database connection to use for
the role.</p></li>
<li><p><strong>default_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default number of seconds for leases for this
role.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of seconds for leases for this
role.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name to give the role.</p></li>
<li><p><strong>renew_statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The database statements to execute when
renewing a user.</p></li>
<li><p><strong>revocation_statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The database statements to execute when
revoking a user.</p></li>
<li><p><strong>rollback_statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The database statements to execute when
rolling back creation due to an error.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/database_secret_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/database_secret_backend_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.database.SecretBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.database.SecretBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.database.SecretBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.database.SecretBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.database.SecretBackendStaticRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.database.</code><code class="sig-name descname">SecretBackendStaticRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">db_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rotation_period=None</em>, <em class="sig-param">rotation_statements=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.database.SecretBackendStaticRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Database Secret Backend static role in Vault. Database secret backend
static roles can be used to manage 1-to-1 mapping of a Vault Role to a user in a
database for the database.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the Vault mount to configure.</p></li>
<li><p><strong>db_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the database connection to use for the static role.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name to give the static role.</p></li>
<li><p><strong>rotation_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time Vault should wait before rotating the password, in seconds.</p></li>
<li><p><strong>rotation_statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Database statements to execute to rotate the password for the configured database user.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database username that this static role corresponds to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/database_secret_backend_static_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/database_secret_backend_static_role.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendStaticRole.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendStaticRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name of the Vault mount to configure.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendStaticRole.db_name">
<code class="sig-name descname">db_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendStaticRole.db_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name of the database connection to use for the static role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendStaticRole.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendStaticRole.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name to give the static role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendStaticRole.rotation_period">
<code class="sig-name descname">rotation_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendStaticRole.rotation_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time Vault should wait before rotating the password, in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendStaticRole.rotation_statements">
<code class="sig-name descname">rotation_statements</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendStaticRole.rotation_statements" title="Permalink to this definition">¶</a></dt>
<dd><p>Database statements to execute to rotate the password for the configured database user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.database.SecretBackendStaticRole.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.database.SecretBackendStaticRole.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The database username that this static role corresponds to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.database.SecretBackendStaticRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">db_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rotation_period=None</em>, <em class="sig-param">rotation_statements=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.database.SecretBackendStaticRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackendStaticRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the Vault mount to configure.</p></li>
<li><p><strong>db_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the database connection to use for the static role.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name to give the static role.</p></li>
<li><p><strong>rotation_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time Vault should wait before rotating the password, in seconds.</p></li>
<li><p><strong>rotation_statements</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Database statements to execute to rotate the password for the configured database user.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database username that this static role corresponds to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/database_secret_backend_static_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/database_secret_backend_static_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.database.SecretBackendStaticRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.database.SecretBackendStaticRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.database.SecretBackendStaticRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.database.SecretBackendStaticRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
