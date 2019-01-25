<div class="section" id="module-pulumi_aws.dms">
<span id="dms"></span><h1>dms<a class="headerlink" href="#module-pulumi_aws.dms" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.dms.Certificate">
<em class="property">class </em><code class="descclassname">pulumi_aws.dms.</code><code class="descname">Certificate</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>certificate_id=None</em>, <em>certificate_pem=None</em>, <em>certificate_wallet=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DMS (Data Migration Service) certificate resource. DMS certificates can be created, deleted, and imported.</p>
<p>&gt; <strong>Note:</strong> All arguments including the PEM encoded certificate will be stored in the raw state as plain-text.
[Read more about sensitive data in state](<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">https://www.terraform.io/docs/state/sensitive-data.html</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate identifier.</li>
<li><strong>certificate_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the .pem X.509 certificate file for the certificate. Either <cite>certificate_pem</cite> or <cite>certificate_wallet</cite> must be set.</li>
<li><strong>certificate_wallet</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the Oracle Wallet certificate for use with SSL. Either <cite>certificate_pem</cite> or <cite>certificate_wallet</cite> must be set.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.dms.Certificate.certificate_arn">
<code class="descname">certificate_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Certificate.certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Certificate.certificate_id">
<code class="descname">certificate_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Certificate.certificate_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Certificate.certificate_pem">
<code class="descname">certificate_pem</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Certificate.certificate_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of the .pem X.509 certificate file for the certificate. Either <cite>certificate_pem</cite> or <cite>certificate_wallet</cite> must be set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Certificate.certificate_wallet">
<code class="descname">certificate_wallet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Certificate.certificate_wallet" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of the Oracle Wallet certificate for use with SSL. Either <cite>certificate_pem</cite> or <cite>certificate_wallet</cite> must be set.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dms.Certificate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.Certificate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.Endpoint">
<em class="property">class </em><code class="descclassname">pulumi_aws.dms.</code><code class="descname">Endpoint</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>certificate_arn=None</em>, <em>database_name=None</em>, <em>endpoint_id=None</em>, <em>endpoint_type=None</em>, <em>engine_name=None</em>, <em>extra_connection_attributes=None</em>, <em>kms_key_arn=None</em>, <em>mongodb_settings=None</em>, <em>password=None</em>, <em>port=None</em>, <em>s3_settings=None</em>, <em>server_name=None</em>, <em>service_access_role=None</em>, <em>ssl_mode=None</em>, <em>tags=None</em>, <em>username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.Endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DMS (Data Migration Service) endpoint resource. DMS endpoints can be created, updated, deleted, and imported.</p>
<p>&gt; <strong>Note:</strong> All arguments including the password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">https://www.terraform.io/docs/state/sensitive-data.html</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) for the certificate.</li>
<li><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the endpoint database.</li>
<li><strong>endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The database endpoint identifier.</li>
<li><strong>endpoint_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of endpoint. Can be one of <cite>source | target</cite>.</li>
<li><strong>engine_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of engine for the endpoint. Can be one of <cite>mysql | oracle | postgres | mariadb | aurora | redshift | sybase | sqlserver | dynamodb | mongodb | s3 | azuredb</cite>.</li>
<li><strong>extra_connection_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](<a class="reference external" href="http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html">http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html</a>).</li>
<li><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for <cite>kms_key_arn</cite>, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.</li>
<li><strong>mongodb_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings for the source MongoDB endpoint. Available settings are <cite>auth_type</cite> (default: <cite>PASSWORD</cite>), <cite>auth_mechanism</cite> (default: <cite>DEFAULT</cite>), <cite>nesting_level</cite> (default: <cite>NONE</cite>), <cite>extract_doc_id</cite> (default: <cite>false</cite>), <cite>docs_to_investigate</cite> (default: <cite>1000</cite>) and <cite>auth_source</cite> (default: <cite>admin</cite>). For more details, see [Using MongoDB as a Source for AWS DMS](<a class="reference external" href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html">https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html</a>).</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to be used to login to the endpoint database.</li>
<li><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The port used by the endpoint database.</li>
<li><strong>s3_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings for the target S3 endpoint. Available settings are <cite>service_access_role_arn</cite>, <cite>external_table_definition</cite>, <cite>csv_row_delimiter</cite> (default: <cite>n</cite>), <cite>csv_delimiter</cite> (default: <cite>,</cite>), <cite>bucket_folder</cite>, <cite>bucket_name</cite> and <cite>compression_type</cite> (default: <cite>NONE</cite>). For more details, see [Using Amazon S3 as a Target for AWS Database Migration Service](<a class="reference external" href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html">https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html</a>).</li>
<li><strong>server_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host name of the server.</li>
<li><strong>service_access_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.</li>
<li><strong>ssl_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSL mode to use for the connection. Can be one of <cite>none | require | verify-ca | verify-full</cite></li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user name to be used to login to the endpoint database.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.certificate_arn">
<code class="descname">certificate_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.database_name">
<code class="descname">database_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the endpoint database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.endpoint_arn">
<code class="descname">endpoint_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.endpoint_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.endpoint_id">
<code class="descname">endpoint_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The database endpoint identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.endpoint_type">
<code class="descname">endpoint_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.endpoint_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of endpoint. Can be one of <cite>source | target</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.engine_name">
<code class="descname">engine_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.engine_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of engine for the endpoint. Can be one of <cite>mysql | oracle | postgres | mariadb | aurora | redshift | sybase | sqlserver | dynamodb | mongodb | s3 | azuredb</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.extra_connection_attributes">
<code class="descname">extra_connection_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.extra_connection_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](<a class="reference external" href="http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html">http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.kms_key_arn">
<code class="descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for <cite>kms_key_arn</cite>, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.mongodb_settings">
<code class="descname">mongodb_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.mongodb_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings for the source MongoDB endpoint. Available settings are <cite>auth_type</cite> (default: <cite>PASSWORD</cite>), <cite>auth_mechanism</cite> (default: <cite>DEFAULT</cite>), <cite>nesting_level</cite> (default: <cite>NONE</cite>), <cite>extract_doc_id</cite> (default: <cite>false</cite>), <cite>docs_to_investigate</cite> (default: <cite>1000</cite>) and <cite>auth_source</cite> (default: <cite>admin</cite>). For more details, see [Using MongoDB as a Source for AWS DMS](<a class="reference external" href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html">https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password to be used to login to the endpoint database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port used by the endpoint database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.s3_settings">
<code class="descname">s3_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.s3_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings for the target S3 endpoint. Available settings are <cite>service_access_role_arn</cite>, <cite>external_table_definition</cite>, <cite>csv_row_delimiter</cite> (default: <cite>n</cite>), <cite>csv_delimiter</cite> (default: <cite>,</cite>), <cite>bucket_folder</cite>, <cite>bucket_name</cite> and <cite>compression_type</cite> (default: <cite>NONE</cite>). For more details, see [Using Amazon S3 as a Target for AWS Database Migration Service](<a class="reference external" href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html">https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.server_name">
<code class="descname">server_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The host name of the server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.service_access_role">
<code class="descname">service_access_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.service_access_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.ssl_mode">
<code class="descname">ssl_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.ssl_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSL mode to use for the connection. Can be one of <cite>none | require | verify-ca | verify-full</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.Endpoint.username">
<code class="descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The user name to be used to login to the endpoint database.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dms.Endpoint.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.Endpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.Endpoint.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.Endpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.ReplicationInstance">
<em class="property">class </em><code class="descclassname">pulumi_aws.dms.</code><code class="descname">ReplicationInstance</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>allocated_storage=None</em>, <em>apply_immediately=None</em>, <em>auto_minor_version_upgrade=None</em>, <em>availability_zone=None</em>, <em>engine_version=None</em>, <em>kms_key_arn=None</em>, <em>multi_az=None</em>, <em>preferred_maintenance_window=None</em>, <em>publicly_accessible=None</em>, <em>replication_instance_class=None</em>, <em>replication_instance_id=None</em>, <em>replication_subnet_group_id=None</em>, <em>tags=None</em>, <em>vpc_security_group_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DMS (Data Migration Service) replication instance resource. DMS replication instances can be created, updated, deleted, and imported.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allocated_storage</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The amount of storage (in gigabytes) to be initially allocated for the replication instance.</li>
<li><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the changes should be applied immediately or during the next maintenance window. Only used when updating an existing resource.</li>
<li><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates that minor engine upgrades will be applied automatically to the replication instance during the maintenance window.</li>
<li><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 Availability Zone that the replication instance will be created in.</li>
<li><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The engine version number of the replication instance.</li>
<li><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for <cite>kms_key_arn</cite>, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.</li>
<li><strong>multi_az</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the replication instance is a multi-az deployment. You cannot set the <cite>availability_zone</cite> parameter if the <cite>multi_az</cite> parameter is set to <cite>true</cite>.</li>
<li><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</li>
<li><strong>publicly_accessible</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address.</li>
<li><strong>replication_instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compute and memory capacity of the replication instance as specified by the replication instance class. Can be one of <cite>dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge</cite></li>
<li><strong>replication_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The replication instance identifier. This parameter is stored as a lowercase string.</li>
<li><strong>replication_subnet_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A subnet group to associate with the replication instance.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPC security group IDs to be used with the replication instance. The VPC security groups must work with the VPC containing the replication instance.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.allocated_storage">
<code class="descname">allocated_storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.allocated_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of storage (in gigabytes) to be initially allocated for the replication instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.apply_immediately">
<code class="descname">apply_immediately</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the changes should be applied immediately or during the next maintenance window. Only used when updating an existing resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.auto_minor_version_upgrade">
<code class="descname">auto_minor_version_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.auto_minor_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates that minor engine upgrades will be applied automatically to the replication instance during the maintenance window.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.availability_zone">
<code class="descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 Availability Zone that the replication instance will be created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.engine_version">
<code class="descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The engine version number of the replication instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.kms_key_arn">
<code class="descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for <cite>kms_key_arn</cite>, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.multi_az">
<code class="descname">multi_az</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.multi_az" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the replication instance is a multi-az deployment. You cannot set the <cite>availability_zone</cite> parameter if the <cite>multi_az</cite> parameter is set to <cite>true</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.preferred_maintenance_window">
<code class="descname">preferred_maintenance_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.preferred_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.publicly_accessible">
<code class="descname">publicly_accessible</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.publicly_accessible" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.replication_instance_arn">
<code class="descname">replication_instance_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.replication_instance_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the replication instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.replication_instance_class">
<code class="descname">replication_instance_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.replication_instance_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute and memory capacity of the replication instance as specified by the replication instance class. Can be one of <cite>dms.t2.micro | dms.t2.small | dms.t2.medium | dms.t2.large | dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.replication_instance_id">
<code class="descname">replication_instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.replication_instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The replication instance identifier. This parameter is stored as a lowercase string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.replication_instance_private_ips">
<code class="descname">replication_instance_private_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.replication_instance_private_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the private IP addresses of the replication instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.replication_instance_public_ips">
<code class="descname">replication_instance_public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.replication_instance_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the public IP addresses of the replication instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.replication_subnet_group_id">
<code class="descname">replication_subnet_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.replication_subnet_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A subnet group to associate with the replication instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.vpc_security_group_ids">
<code class="descname">vpc_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPC security group IDs to be used with the replication instance. The VPC security groups must work with the VPC containing the replication instance.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dms.ReplicationInstance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.ReplicationInstance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.ReplicationSubnetGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.dms.</code><code class="descname">ReplicationSubnetGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>replication_subnet_group_description=None</em>, <em>replication_subnet_group_id=None</em>, <em>subnet_ids=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DMS (Data Migration Service) replication subnet group resource. DMS replication subnet groups can be created, updated, deleted, and imported.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>replication_subnet_group_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the subnet group.</li>
<li><strong>replication_subnet_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the replication subnet group. This value is stored as a lowercase string.</li>
<li><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the EC2 subnet IDs for the subnet group.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.replication_subnet_group_description">
<code class="descname">replication_subnet_group_description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.replication_subnet_group_description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the subnet group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.replication_subnet_group_id">
<code class="descname">replication_subnet_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.replication_subnet_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the replication subnet group. This value is stored as a lowercase string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the EC2 subnet IDs for the subnet group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC the subnet group is in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.ReplicationTask">
<em class="property">class </em><code class="descclassname">pulumi_aws.dms.</code><code class="descname">ReplicationTask</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>cdc_start_time=None</em>, <em>migration_type=None</em>, <em>replication_instance_arn=None</em>, <em>replication_task_id=None</em>, <em>replication_task_settings=None</em>, <em>source_endpoint_arn=None</em>, <em>table_mappings=None</em>, <em>tags=None</em>, <em>target_endpoint_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DMS (Data Migration Service) replication task resource. DMS replication tasks can be created, updated, deleted, and imported.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cdc_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Unix timestamp integer for the start of the Change Data Capture (CDC) operation.</li>
<li><strong>migration_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The migration type. Can be one of <cite>full-load | cdc | full-load-and-cdc</cite>.</li>
<li><strong>replication_instance_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the replication instance.</li>
<li><strong>replication_task_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The replication task identifier.</li>
<li><strong>replication_task_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An escaped JSON string that contains the task settings. For a complete list of task settings, see [Task Settings for AWS Database Migration Service Tasks](<a class="reference external" href="http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html">http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html</a>).</li>
<li><strong>source_endpoint_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) string that uniquely identifies the source endpoint.</li>
<li><strong>table_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An escaped JSON string that contains the table mappings. For information on table mapping see [Using Table Mapping with an AWS Database Migration Service Task to Select and Filter Data](<a class="reference external" href="http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html">http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html</a>)</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>target_endpoint_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) string that uniquely identifies the target endpoint.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationTask.cdc_start_time">
<code class="descname">cdc_start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.cdc_start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The Unix timestamp integer for the start of the Change Data Capture (CDC) operation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationTask.migration_type">
<code class="descname">migration_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.migration_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The migration type. Can be one of <cite>full-load | cdc | full-load-and-cdc</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationTask.replication_instance_arn">
<code class="descname">replication_instance_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.replication_instance_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the replication instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationTask.replication_task_arn">
<code class="descname">replication_task_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.replication_task_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the replication task.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationTask.replication_task_id">
<code class="descname">replication_task_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.replication_task_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The replication task identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationTask.replication_task_settings">
<code class="descname">replication_task_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.replication_task_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>An escaped JSON string that contains the task settings. For a complete list of task settings, see [Task Settings for AWS Database Migration Service Tasks](<a class="reference external" href="http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html">http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationTask.source_endpoint_arn">
<code class="descname">source_endpoint_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.source_endpoint_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) string that uniquely identifies the source endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationTask.table_mappings">
<code class="descname">table_mappings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.table_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>An escaped JSON string that contains the table mappings. For information on table mapping see [Using Table Mapping with an AWS Database Migration Service Task to Select and Filter Data](<a class="reference external" href="http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html">http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html</a>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationTask.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dms.ReplicationTask.target_endpoint_arn">
<code class="descname">target_endpoint_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.target_endpoint_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) string that uniquely identifies the target endpoint.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dms.ReplicationTask.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.ReplicationTask.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
