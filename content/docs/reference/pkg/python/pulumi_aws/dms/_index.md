---
title: Module dms
title_tag: Module dms | Package pulumi_aws | Python SDK
linktitle: dms
notitle: true
---

<div class="section" id="dms">
<h1>dms<a class="headerlink" href="#dms" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.dms"></span><dl class="py class">
<dt id="pulumi_aws.dms.Certificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dms.</code><code class="sig-name descname">Certificate</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_pem</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_wallet</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DMS (Data Migration Service) certificate resource. DMS certificates can be created, deleted, and imported.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the PEM encoded certificate will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate identifier.</p></li>
<li><p><strong>certificate_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the .pem X.509 certificate file for the certificate. Either <code class="docutils literal notranslate"><span class="pre">certificate_pem</span></code> or <code class="docutils literal notranslate"><span class="pre">certificate_wallet</span></code> must be set.</p></li>
<li><p><strong>certificate_wallet</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the Oracle Wallet certificate for use with SSL. Either <code class="docutils literal notranslate"><span class="pre">certificate_pem</span></code> or <code class="docutils literal notranslate"><span class="pre">certificate_wallet</span></code> must be set.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.dms.Certificate.certificate_arn">
<code class="sig-name descname">certificate_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Certificate.certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the certificate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Certificate.certificate_id">
<code class="sig-name descname">certificate_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Certificate.certificate_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Certificate.certificate_pem">
<code class="sig-name descname">certificate_pem</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Certificate.certificate_pem" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of the .pem X.509 certificate file for the certificate. Either <code class="docutils literal notranslate"><span class="pre">certificate_pem</span></code> or <code class="docutils literal notranslate"><span class="pre">certificate_wallet</span></code> must be set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Certificate.certificate_wallet">
<code class="sig-name descname">certificate_wallet</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Certificate.certificate_wallet" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of the Oracle Wallet certificate for use with SSL. Either <code class="docutils literal notranslate"><span class="pre">certificate_pem</span></code> or <code class="docutils literal notranslate"><span class="pre">certificate_wallet</span></code> must be set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.dms.Certificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_pem</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_wallet</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.Certificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Certificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) for the certificate.</p></li>
<li><p><strong>certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate identifier.</p></li>
<li><p><strong>certificate_pem</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the .pem X.509 certificate file for the certificate. Either <code class="docutils literal notranslate"><span class="pre">certificate_pem</span></code> or <code class="docutils literal notranslate"><span class="pre">certificate_wallet</span></code> must be set.</p></li>
<li><p><strong>certificate_wallet</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the Oracle Wallet certificate for use with SSL. Either <code class="docutils literal notranslate"><span class="pre">certificate_pem</span></code> or <code class="docutils literal notranslate"><span class="pre">certificate_wallet</span></code> must be set.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.dms.Certificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.Certificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.Endpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dms.</code><code class="sig-name descname">Endpoint</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_connection_attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kinesis_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongodb_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_access_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.Endpoint" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>Provides a DMS (Data Migration Service) endpoint resource. DMS endpoints can be created, updated, deleted, and imported.

&gt; **Note:** All arguments including the password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).



:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] certificate_arn: The Amazon Resource Name (ARN) for the certificate.
:param pulumi.Input[str] database_name: The name of the endpoint database.
:param pulumi.Input[dict] elasticsearch_settings: Configuration block with Elasticsearch settings. Detailed below.
:param pulumi.Input[str] endpoint_id: The database endpoint identifier.
:param pulumi.Input[str] endpoint_type: The type of endpoint. Can be one of `source | target`.
:param pulumi.Input[str] engine_name: The type of engine for the endpoint. Can be one of `aurora | aurora-postgresql| azuredb | db2 | docdb | dynamodb | elasticsearch | kafka | kinesis | mariadb | mongodb | mysql | oracle | postgres | redshift | s3 | sqlserver | sybase`.
:param pulumi.Input[str] extra_connection_attributes: Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).
:param pulumi.Input[dict] kafka_settings: Configuration block with Kafka settings. Detailed below.
:param pulumi.Input[dict] kinesis_settings: Configuration block with Kinesis settings. Detailed below.
:param pulumi.Input[str] kms_key_arn: The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kms_key_arn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
:param pulumi.Input[dict] mongodb_settings: Configuration block with MongoDB settings. Detailed below.
:param pulumi.Input[str] password: The password to be used to login to the endpoint database.
:param pulumi.Input[float] port: The port used by the endpoint database.
:param pulumi.Input[dict] s3_settings: Configuration block with S3 settings. Detailed below.
:param pulumi.Input[str] server_name: The host name of the server.
:param pulumi.Input[str] service_access_role: The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.
:param pulumi.Input[str] ssl_mode: The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`
:param pulumi.Input[dict] tags: A map of tags to assign to the resource.
:param pulumi.Input[str] username: The user name to be used to login to the endpoint database.

The **elasticsearch_settings** object supports the following:

  * `endpointUri` (`pulumi.Input[str]`) - Endpoint for the Elasticsearch cluster.
  * `errorRetryDuration` (`pulumi.Input[float]`) - Maximum number of seconds for which DMS retries failed API requests to the Elasticsearch cluster. Defaults to `300`.
  * `fullLoadErrorPercentage` (`pulumi.Input[float]`) - Maximum percentage of records that can fail to be written before a full load operation stops. Defaults to `10`.
  * `serviceAccessRoleArn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Elasticsearch cluster.

The **kafka_settings** object supports the following:

  * `broker` (`pulumi.Input[str]`) - Kafka broker location. Specify in the form broker-hostname-or-ip:port.
  * `topic` (`pulumi.Input[str]`) - Kafka topic for migration. Defaults to `kafka-default-topic`.

The **kinesis_settings** object supports the following:

  * `messageFormat` (`pulumi.Input[str]`) - Output format for the records created. Defaults to `json`. Valid values are `json` and `json_unformatted` (a single line with no tab).
  * `serviceAccessRoleArn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Kinesis data stream.
  * `stream_arn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the Kinesis data stream.

The **mongodb_settings** object supports the following:

  * `authMechanism` (`pulumi.Input[str]`) - Authentication mechanism to access the MongoDB source endpoint. Defaults to `default`.
  * `authSource` (`pulumi.Input[str]`) - Authentication database name. Not used when `auth_type` is `no`. Defaults to `admin`.
  * `auth_type` (`pulumi.Input[str]`) - Authentication type to access the MongoDB source endpoint. Defaults to `password`.
  * `docsToInvestigate` (`pulumi.Input[str]`) - Number of documents to preview to determine the document organization. Use this setting when `nesting_level` is set to `one`. Defaults to `1000`.
  * `extractDocId` (`pulumi.Input[str]`) - Document ID. Use this setting when `nesting_level` is set to `none`. Defaults to `false`.
  * `nestingLevel` (`pulumi.Input[str]`) - Specifies either document or table mode. Defaults to `none`. Valid values are `one` (table mode) and `none` (document mode).

The **s3_settings** object supports the following:

  * `bucketFolder` (`pulumi.Input[str]`) - S3 Bucket Object prefix.
  * `bucket_name` (`pulumi.Input[str]`) - S3 Bucket name.
  * `compressionType` (`pulumi.Input[str]`) - Set to compress target files. Defaults to `NONE`. Valid values are `GZIP` and `NONE`.
  * `csvDelimiter` (`pulumi.Input[str]`) - Delimiter used to separate columns in the source files. Defaults to `,`.
  * `csvRowDelimiter` (`pulumi.Input[str]`) - Delimiter used to separate rows in the source files. Defaults to `
</pre></div>
</div>
<p><a href="#id1"><span class="problematic" id="id2">`</span></a>.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `externalTableDefinition` (`pulumi.Input[str]`) - JSON document that describes how AWS DMS should interpret the data.
* `serviceAccessRoleArn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the IAM Role with permissions to read from or write to the S3 Bucket.
</pre></div>
</div>
<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.certificate_arn">
<code class="sig-name descname">certificate_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the certificate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.database_name">
<code class="sig-name descname">database_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the endpoint database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.elasticsearch_settings">
<code class="sig-name descname">elasticsearch_settings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.elasticsearch_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block with Elasticsearch settings. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpointUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Endpoint for the Elasticsearch cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorRetryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Maximum number of seconds for which DMS retries failed API requests to the Elasticsearch cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fullLoadErrorPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Maximum percentage of records that can fail to be written before a full load operation stops. Defaults to <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccessRoleArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Elasticsearch cluster.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.endpoint_arn">
<code class="sig-name descname">endpoint_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.endpoint_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the endpoint.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.endpoint_id">
<code class="sig-name descname">endpoint_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The database endpoint identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.endpoint_type">
<code class="sig-name descname">endpoint_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.endpoint_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of endpoint. Can be one of <code class="docutils literal notranslate"><span class="pre">source</span> <span class="pre">|</span> <span class="pre">target</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.engine_name">
<code class="sig-name descname">engine_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.engine_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of engine for the endpoint. Can be one of <code class="docutils literal notranslate"><span class="pre">aurora</span> <span class="pre">|</span> <span class="pre">aurora-postgresql|</span> <span class="pre">azuredb</span> <span class="pre">|</span> <span class="pre">db2</span> <span class="pre">|</span> <span class="pre">docdb</span> <span class="pre">|</span> <span class="pre">dynamodb</span> <span class="pre">|</span> <span class="pre">elasticsearch</span> <span class="pre">|</span> <span class="pre">kafka</span> <span class="pre">|</span> <span class="pre">kinesis</span> <span class="pre">|</span> <span class="pre">mariadb</span> <span class="pre">|</span> <span class="pre">mongodb</span> <span class="pre">|</span> <span class="pre">mysql</span> <span class="pre">|</span> <span class="pre">oracle</span> <span class="pre">|</span> <span class="pre">postgres</span> <span class="pre">|</span> <span class="pre">redshift</span> <span class="pre">|</span> <span class="pre">s3</span> <span class="pre">|</span> <span class="pre">sqlserver</span> <span class="pre">|</span> <span class="pre">sybase</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.extra_connection_attributes">
<code class="sig-name descname">extra_connection_attributes</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.extra_connection_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional attributes associated with the connection. For available attributes see <a class="reference external" href="http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html">Using Extra Connection Attributes with AWS Database Migration Service</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.kafka_settings">
<code class="sig-name descname">kafka_settings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.kafka_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block with Kafka settings. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">broker</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Kafka broker location. Specify in the form broker-hostname-or-ip:port.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Kafka topic for migration. Defaults to <code class="docutils literal notranslate"><span class="pre">kafka-default-topic</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.kinesis_settings">
<code class="sig-name descname">kinesis_settings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.kinesis_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block with Kinesis settings. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">messageFormat</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Output format for the records created. Defaults to <code class="docutils literal notranslate"><span class="pre">json</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">json</span></code> and <code class="docutils literal notranslate"><span class="pre">json_unformatted</span></code> (a single line with no tab).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccessRoleArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Kinesis data stream.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stream_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon Resource Name (ARN) of the Kinesis data stream.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.kms_key_arn">
<code class="sig-name descname">kms_key_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for <code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code>, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.mongodb_settings">
<code class="sig-name descname">mongodb_settings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.mongodb_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block with MongoDB settings. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authMechanism</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Authentication mechanism to access the MongoDB source endpoint. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authSource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Authentication database name. Not used when <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is <code class="docutils literal notranslate"><span class="pre">no</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">admin</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">auth_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Authentication type to access the MongoDB source endpoint. Defaults to <code class="docutils literal notranslate"><span class="pre">password</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">docsToInvestigate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Number of documents to preview to determine the document organization. Use this setting when <code class="docutils literal notranslate"><span class="pre">nesting_level</span></code> is set to <code class="docutils literal notranslate"><span class="pre">one</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">1000</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">extractDocId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Document ID. Use this setting when <code class="docutils literal notranslate"><span class="pre">nesting_level</span></code> is set to <code class="docutils literal notranslate"><span class="pre">none</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nestingLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies either document or table mode. Defaults to <code class="docutils literal notranslate"><span class="pre">none</span></code>. Valid values are <code class="docutils literal notranslate"><span class="pre">one</span></code> (table mode) and <code class="docutils literal notranslate"><span class="pre">none</span></code> (document mode).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.password">
<code class="sig-name descname">password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password to be used to login to the endpoint database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port used by the endpoint database.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.s3_settings">
<code class="sig-name descname">s3_settings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.s3_settings" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>Configuration block with S3 settings. Detailed below.

  * `bucketFolder` (`str`) - S3 Bucket Object prefix.
  * `bucket_name` (`str`) - S3 Bucket name.
  * `compressionType` (`str`) - Set to compress target files. Defaults to `NONE`. Valid values are `GZIP` and `NONE`.
  * `csvDelimiter` (`str`) - Delimiter used to separate columns in the source files. Defaults to `,`.
  * `csvRowDelimiter` (`str`) - Delimiter used to separate rows in the source files. Defaults to `
</pre></div>
</div>
<p><a href="#id3"><span class="problematic" id="id4">`</span></a>.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `externalTableDefinition` (`str`) - JSON document that describes how AWS DMS should interpret the data.
* `serviceAccessRoleArn` (`str`) - Amazon Resource Name (ARN) of the IAM Role with permissions to read from or write to the S3 Bucket.
</pre></div>
</div>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.server_name">
<code class="sig-name descname">server_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.server_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The host name of the server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.service_access_role">
<code class="sig-name descname">service_access_role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.service_access_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.ssl_mode">
<code class="sig-name descname">ssl_mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.ssl_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSL mode to use for the connection. Can be one of <code class="docutils literal notranslate"><span class="pre">none</span> <span class="pre">|</span> <span class="pre">require</span> <span class="pre">|</span> <span class="pre">verify-ca</span> <span class="pre">|</span> <span class="pre">verify-full</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.Endpoint.username">
<code class="sig-name descname">username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.Endpoint.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The user name to be used to login to the endpoint database.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.dms.Endpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_connection_attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kinesis_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongodb_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_access_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.Endpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>Get an existing Endpoint resource&#39;s state with the given name, id, and optional extra
properties used to qualify the lookup.

:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] certificate_arn: The Amazon Resource Name (ARN) for the certificate.
:param pulumi.Input[str] database_name: The name of the endpoint database.
:param pulumi.Input[dict] elasticsearch_settings: Configuration block with Elasticsearch settings. Detailed below.
:param pulumi.Input[str] endpoint_arn: The Amazon Resource Name (ARN) for the endpoint.
:param pulumi.Input[str] endpoint_id: The database endpoint identifier.
:param pulumi.Input[str] endpoint_type: The type of endpoint. Can be one of `source | target`.
:param pulumi.Input[str] engine_name: The type of engine for the endpoint. Can be one of `aurora | aurora-postgresql| azuredb | db2 | docdb | dynamodb | elasticsearch | kafka | kinesis | mariadb | mongodb | mysql | oracle | postgres | redshift | s3 | sqlserver | sybase`.
:param pulumi.Input[str] extra_connection_attributes: Additional attributes associated with the connection. For available attributes see [Using Extra Connection Attributes with AWS Database Migration Service](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.ConnectionAttributes.html).
:param pulumi.Input[dict] kafka_settings: Configuration block with Kafka settings. Detailed below.
:param pulumi.Input[dict] kinesis_settings: Configuration block with Kinesis settings. Detailed below.
:param pulumi.Input[str] kms_key_arn: The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for `kms_key_arn`, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.
:param pulumi.Input[dict] mongodb_settings: Configuration block with MongoDB settings. Detailed below.
:param pulumi.Input[str] password: The password to be used to login to the endpoint database.
:param pulumi.Input[float] port: The port used by the endpoint database.
:param pulumi.Input[dict] s3_settings: Configuration block with S3 settings. Detailed below.
:param pulumi.Input[str] server_name: The host name of the server.
:param pulumi.Input[str] service_access_role: The Amazon Resource Name (ARN) used by the service access IAM role for dynamodb endpoints.
:param pulumi.Input[str] ssl_mode: The SSL mode to use for the connection. Can be one of `none | require | verify-ca | verify-full`
:param pulumi.Input[dict] tags: A map of tags to assign to the resource.
:param pulumi.Input[str] username: The user name to be used to login to the endpoint database.

The **elasticsearch_settings** object supports the following:

  * `endpointUri` (`pulumi.Input[str]`) - Endpoint for the Elasticsearch cluster.
  * `errorRetryDuration` (`pulumi.Input[float]`) - Maximum number of seconds for which DMS retries failed API requests to the Elasticsearch cluster. Defaults to `300`.
  * `fullLoadErrorPercentage` (`pulumi.Input[float]`) - Maximum percentage of records that can fail to be written before a full load operation stops. Defaults to `10`.
  * `serviceAccessRoleArn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Elasticsearch cluster.

The **kafka_settings** object supports the following:

  * `broker` (`pulumi.Input[str]`) - Kafka broker location. Specify in the form broker-hostname-or-ip:port.
  * `topic` (`pulumi.Input[str]`) - Kafka topic for migration. Defaults to `kafka-default-topic`.

The **kinesis_settings** object supports the following:

  * `messageFormat` (`pulumi.Input[str]`) - Output format for the records created. Defaults to `json`. Valid values are `json` and `json_unformatted` (a single line with no tab).
  * `serviceAccessRoleArn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Kinesis data stream.
  * `stream_arn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the Kinesis data stream.

The **mongodb_settings** object supports the following:

  * `authMechanism` (`pulumi.Input[str]`) - Authentication mechanism to access the MongoDB source endpoint. Defaults to `default`.
  * `authSource` (`pulumi.Input[str]`) - Authentication database name. Not used when `auth_type` is `no`. Defaults to `admin`.
  * `auth_type` (`pulumi.Input[str]`) - Authentication type to access the MongoDB source endpoint. Defaults to `password`.
  * `docsToInvestigate` (`pulumi.Input[str]`) - Number of documents to preview to determine the document organization. Use this setting when `nesting_level` is set to `one`. Defaults to `1000`.
  * `extractDocId` (`pulumi.Input[str]`) - Document ID. Use this setting when `nesting_level` is set to `none`. Defaults to `false`.
  * `nestingLevel` (`pulumi.Input[str]`) - Specifies either document or table mode. Defaults to `none`. Valid values are `one` (table mode) and `none` (document mode).

The **s3_settings** object supports the following:

  * `bucketFolder` (`pulumi.Input[str]`) - S3 Bucket Object prefix.
  * `bucket_name` (`pulumi.Input[str]`) - S3 Bucket name.
  * `compressionType` (`pulumi.Input[str]`) - Set to compress target files. Defaults to `NONE`. Valid values are `GZIP` and `NONE`.
  * `csvDelimiter` (`pulumi.Input[str]`) - Delimiter used to separate columns in the source files. Defaults to `,`.
  * `csvRowDelimiter` (`pulumi.Input[str]`) - Delimiter used to separate rows in the source files. Defaults to `
</pre></div>
</div>
<p><a href="#id5"><span class="problematic" id="id6">`</span></a>.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `externalTableDefinition` (`pulumi.Input[str]`) - JSON document that describes how AWS DMS should interpret the data.
* `serviceAccessRoleArn` (`pulumi.Input[str]`) - Amazon Resource Name (ARN) of the IAM Role with permissions to read from or write to the S3 Bucket.
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.dms.Endpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.Endpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.Endpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.Endpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.EventSubscription">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dms.</code><code class="sig-name descname">EventSubscription</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_categories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sns_topic_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.EventSubscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DMS (Data Migration Service) event subscription resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the event subscription should be enabled.</p></li>
<li><p><strong>event_categories</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of event categories to listen for, see <code class="docutils literal notranslate"><span class="pre">DescribeEventCategories</span></code> for a canonical list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of event subscription.</p></li>
<li><p><strong>sns_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNS topic arn to send events on.</p></li>
<li><p><strong>source_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids of sources to listen to.</p></li>
<li><p><strong>source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of source for events. Valid values: <code class="docutils literal notranslate"><span class="pre">replication-instance</span></code> or <code class="docutils literal notranslate"><span class="pre">replication-task</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.dms.EventSubscription.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.EventSubscription.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the event subscription should be enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.EventSubscription.event_categories">
<code class="sig-name descname">event_categories</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.EventSubscription.event_categories" title="Permalink to this definition">¶</a></dt>
<dd><p>List of event categories to listen for, see <code class="docutils literal notranslate"><span class="pre">DescribeEventCategories</span></code> for a canonical list.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.EventSubscription.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.EventSubscription.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of event subscription.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.EventSubscription.sns_topic_arn">
<code class="sig-name descname">sns_topic_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.EventSubscription.sns_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>SNS topic arn to send events on.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.EventSubscription.source_ids">
<code class="sig-name descname">source_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.EventSubscription.source_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids of sources to listen to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.EventSubscription.source_type">
<code class="sig-name descname">source_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.EventSubscription.source_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of source for events. Valid values: <code class="docutils literal notranslate"><span class="pre">replication-instance</span></code> or <code class="docutils literal notranslate"><span class="pre">replication-task</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.dms.EventSubscription.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_categories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sns_topic_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.EventSubscription.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventSubscription resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the event subscription should be enabled.</p></li>
<li><p><strong>event_categories</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of event categories to listen for, see <code class="docutils literal notranslate"><span class="pre">DescribeEventCategories</span></code> for a canonical list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of event subscription.</p></li>
<li><p><strong>sns_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNS topic arn to send events on.</p></li>
<li><p><strong>source_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ids of sources to listen to.</p></li>
<li><p><strong>source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of source for events. Valid values: <code class="docutils literal notranslate"><span class="pre">replication-instance</span></code> or <code class="docutils literal notranslate"><span class="pre">replication-task</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.dms.EventSubscription.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.EventSubscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.EventSubscription.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.EventSubscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.ReplicationInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dms.</code><code class="sig-name descname">ReplicationInstance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allocated_storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apply_immediately</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_minor_version_upgrade</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi_az</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_maintenance_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">publicly_accessible</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_instance_class</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_subnet_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DMS (Data Migration Service) replication instance resource. DMS replication instances can be created, updated, deleted, and imported.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocated_storage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of storage (in gigabytes) to be initially allocated for the replication instance.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the changes should be applied immediately or during the next maintenance window. Only used when updating an existing resource.</p></li>
<li><p><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates that minor engine upgrades will be applied automatically to the replication instance during the maintenance window.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 Availability Zone that the replication instance will be created in.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The engine version number of the replication instance.</p></li>
<li><p><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for <code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code>, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.</p></li>
<li><p><strong>multi_az</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the replication instance is a multi-az deployment. You cannot set the <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> parameter if the <code class="docutils literal notranslate"><span class="pre">multi_az</span></code> parameter is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p></li>
<li><p><strong>publicly_accessible</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address.</p></li>
<li><p><strong>replication_instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compute and memory capacity of the replication instance as specified by the replication instance class. Can be one of <code class="docutils literal notranslate"><span class="pre">dms.t2.micro</span> <span class="pre">|</span> <span class="pre">dms.t2.small</span> <span class="pre">|</span> <span class="pre">dms.t2.medium</span> <span class="pre">|</span> <span class="pre">dms.t2.large</span> <span class="pre">|</span> <span class="pre">dms.c4.large</span> <span class="pre">|</span> <span class="pre">dms.c4.xlarge</span> <span class="pre">|</span> <span class="pre">dms.c4.2xlarge</span> <span class="pre">|</span> <span class="pre">dms.c4.4xlarge</span></code></p></li>
<li><p><strong>replication_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The replication instance identifier. This parameter is stored as a lowercase string.</p></li>
<li><p><strong>replication_subnet_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A subnet group to associate with the replication instance.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPC security group IDs to be used with the replication instance. The VPC security groups must work with the VPC containing the replication instance.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.allocated_storage">
<code class="sig-name descname">allocated_storage</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.allocated_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of storage (in gigabytes) to be initially allocated for the replication instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.apply_immediately">
<code class="sig-name descname">apply_immediately</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.apply_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the changes should be applied immediately or during the next maintenance window. Only used when updating an existing resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.auto_minor_version_upgrade">
<code class="sig-name descname">auto_minor_version_upgrade</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.auto_minor_version_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates that minor engine upgrades will be applied automatically to the replication instance during the maintenance window.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 Availability Zone that the replication instance will be created in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.engine_version">
<code class="sig-name descname">engine_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The engine version number of the replication instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.kms_key_arn">
<code class="sig-name descname">kms_key_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for <code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code>, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.multi_az">
<code class="sig-name descname">multi_az</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.multi_az" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the replication instance is a multi-az deployment. You cannot set the <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> parameter if the <code class="docutils literal notranslate"><span class="pre">multi_az</span></code> parameter is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.preferred_maintenance_window">
<code class="sig-name descname">preferred_maintenance_window</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.preferred_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.publicly_accessible">
<code class="sig-name descname">publicly_accessible</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.publicly_accessible" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.replication_instance_arn">
<code class="sig-name descname">replication_instance_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.replication_instance_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the replication instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.replication_instance_class">
<code class="sig-name descname">replication_instance_class</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.replication_instance_class" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute and memory capacity of the replication instance as specified by the replication instance class. Can be one of <code class="docutils literal notranslate"><span class="pre">dms.t2.micro</span> <span class="pre">|</span> <span class="pre">dms.t2.small</span> <span class="pre">|</span> <span class="pre">dms.t2.medium</span> <span class="pre">|</span> <span class="pre">dms.t2.large</span> <span class="pre">|</span> <span class="pre">dms.c4.large</span> <span class="pre">|</span> <span class="pre">dms.c4.xlarge</span> <span class="pre">|</span> <span class="pre">dms.c4.2xlarge</span> <span class="pre">|</span> <span class="pre">dms.c4.4xlarge</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.replication_instance_id">
<code class="sig-name descname">replication_instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.replication_instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The replication instance identifier. This parameter is stored as a lowercase string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.replication_instance_private_ips">
<code class="sig-name descname">replication_instance_private_ips</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.replication_instance_private_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the private IP addresses of the replication instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.replication_instance_public_ips">
<code class="sig-name descname">replication_instance_public_ips</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.replication_instance_public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the public IP addresses of the replication instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.replication_subnet_group_id">
<code class="sig-name descname">replication_subnet_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.replication_subnet_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A subnet group to associate with the replication instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationInstance.vpc_security_group_ids">
<code class="sig-name descname">vpc_security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.vpc_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPC security group IDs to be used with the replication instance. The VPC security groups must work with the VPC containing the replication instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.dms.ReplicationInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allocated_storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apply_immediately</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_minor_version_upgrade</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi_az</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preferred_maintenance_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">publicly_accessible</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_instance_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_instance_class</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_instance_private_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_instance_public_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_subnet_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReplicationInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocated_storage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of storage (in gigabytes) to be initially allocated for the replication instance.</p></li>
<li><p><strong>apply_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the changes should be applied immediately or during the next maintenance window. Only used when updating an existing resource.</p></li>
<li><p><strong>auto_minor_version_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates that minor engine upgrades will be applied automatically to the replication instance during the maintenance window.</p></li>
<li><p><strong>availability_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 Availability Zone that the replication instance will be created in.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The engine version number of the replication instance.</p></li>
<li><p><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) for the KMS key that will be used to encrypt the connection parameters. If you do not specify a value for <code class="docutils literal notranslate"><span class="pre">kms_key_arn</span></code>, then AWS DMS will use your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS region.</p></li>
<li><p><strong>multi_az</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the replication instance is a multi-az deployment. You cannot set the <code class="docutils literal notranslate"><span class="pre">availability_zone</span></code> parameter if the <code class="docutils literal notranslate"><span class="pre">multi_az</span></code> parameter is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>preferred_maintenance_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p></li>
<li><p><strong>publicly_accessible</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address.</p></li>
<li><p><strong>replication_instance_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the replication instance.</p></li>
<li><p><strong>replication_instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The compute and memory capacity of the replication instance as specified by the replication instance class. Can be one of <code class="docutils literal notranslate"><span class="pre">dms.t2.micro</span> <span class="pre">|</span> <span class="pre">dms.t2.small</span> <span class="pre">|</span> <span class="pre">dms.t2.medium</span> <span class="pre">|</span> <span class="pre">dms.t2.large</span> <span class="pre">|</span> <span class="pre">dms.c4.large</span> <span class="pre">|</span> <span class="pre">dms.c4.xlarge</span> <span class="pre">|</span> <span class="pre">dms.c4.2xlarge</span> <span class="pre">|</span> <span class="pre">dms.c4.4xlarge</span></code></p></li>
<li><p><strong>replication_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The replication instance identifier. This parameter is stored as a lowercase string.</p></li>
<li><p><strong>replication_instance_private_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the private IP addresses of the replication instance.</p></li>
<li><p><strong>replication_instance_public_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the public IP addresses of the replication instance.</p></li>
<li><p><strong>replication_subnet_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A subnet group to associate with the replication instance.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>vpc_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPC security group IDs to be used with the replication instance. The VPC security groups must work with the VPC containing the replication instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.dms.ReplicationInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.ReplicationInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.ReplicationSubnetGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dms.</code><code class="sig-name descname">ReplicationSubnetGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_subnet_group_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_subnet_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DMS (Data Migration Service) replication subnet group resource. DMS replication subnet groups can be created, updated, deleted, and imported.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>replication_subnet_group_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the subnet group.</p></li>
<li><p><strong>replication_subnet_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the replication subnet group. This value is stored as a lowercase string.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the EC2 subnet IDs for the subnet group.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.replication_subnet_group_description">
<code class="sig-name descname">replication_subnet_group_description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.replication_subnet_group_description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the subnet group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.replication_subnet_group_id">
<code class="sig-name descname">replication_subnet_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.replication_subnet_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the replication subnet group. This value is stored as a lowercase string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the EC2 subnet IDs for the subnet group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC the subnet group is in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_subnet_group_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_subnet_group_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_subnet_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReplicationSubnetGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>replication_subnet_group_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the subnet group.</p></li>
<li><p><strong>replication_subnet_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the replication subnet group. This value is stored as a lowercase string.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the EC2 subnet IDs for the subnet group.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC the subnet group is in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.ReplicationSubnetGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationSubnetGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.ReplicationTask">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dms.</code><code class="sig-name descname">ReplicationTask</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cdc_start_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">migration_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_instance_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_task_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_task_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_endpoint_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_endpoint_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DMS (Data Migration Service) replication task resource. DMS replication tasks can be created, updated, deleted, and imported.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cdc_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Unix timestamp integer for the start of the Change Data Capture (CDC) operation.</p></li>
<li><p><strong>migration_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The migration type. Can be one of <code class="docutils literal notranslate"><span class="pre">full-load</span> <span class="pre">|</span> <span class="pre">cdc</span> <span class="pre">|</span> <span class="pre">full-load-and-cdc</span></code>.</p></li>
<li><p><strong>replication_instance_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the replication instance.</p></li>
<li><p><strong>replication_task_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The replication task identifier.</p></li>
<li><p><strong>replication_task_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An escaped JSON string that contains the task settings. For a complete list of task settings, see <a class="reference external" href="http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html">Task Settings for AWS Database Migration Service Tasks</a>.</p></li>
<li><p><strong>source_endpoint_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) string that uniquely identifies the source endpoint.</p></li>
<li><p><strong>table_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An escaped JSON string that contains the table mappings. For information on table mapping see <a class="reference external" href="http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html">Using Table Mapping with an AWS Database Migration Service Task to Select and Filter Data</a></p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>target_endpoint_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) string that uniquely identifies the target endpoint.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationTask.cdc_start_time">
<code class="sig-name descname">cdc_start_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.cdc_start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The Unix timestamp integer for the start of the Change Data Capture (CDC) operation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationTask.migration_type">
<code class="sig-name descname">migration_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.migration_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The migration type. Can be one of <code class="docutils literal notranslate"><span class="pre">full-load</span> <span class="pre">|</span> <span class="pre">cdc</span> <span class="pre">|</span> <span class="pre">full-load-and-cdc</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationTask.replication_instance_arn">
<code class="sig-name descname">replication_instance_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.replication_instance_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the replication instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationTask.replication_task_arn">
<code class="sig-name descname">replication_task_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.replication_task_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) for the replication task.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationTask.replication_task_id">
<code class="sig-name descname">replication_task_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.replication_task_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The replication task identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationTask.replication_task_settings">
<code class="sig-name descname">replication_task_settings</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.replication_task_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>An escaped JSON string that contains the task settings. For a complete list of task settings, see <a class="reference external" href="http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html">Task Settings for AWS Database Migration Service Tasks</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationTask.source_endpoint_arn">
<code class="sig-name descname">source_endpoint_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.source_endpoint_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) string that uniquely identifies the source endpoint.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationTask.table_mappings">
<code class="sig-name descname">table_mappings</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.table_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>An escaped JSON string that contains the table mappings. For information on table mapping see <a class="reference external" href="http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html">Using Table Mapping with an AWS Database Migration Service Task to Select and Filter Data</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationTask.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dms.ReplicationTask.target_endpoint_arn">
<code class="sig-name descname">target_endpoint_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.target_endpoint_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) string that uniquely identifies the target endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.dms.ReplicationTask.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cdc_start_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">migration_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_instance_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_task_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_task_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_task_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_endpoint_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_mappings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_endpoint_arn</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReplicationTask resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cdc_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Unix timestamp integer for the start of the Change Data Capture (CDC) operation.</p></li>
<li><p><strong>migration_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The migration type. Can be one of <code class="docutils literal notranslate"><span class="pre">full-load</span> <span class="pre">|</span> <span class="pre">cdc</span> <span class="pre">|</span> <span class="pre">full-load-and-cdc</span></code>.</p></li>
<li><p><strong>replication_instance_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the replication instance.</p></li>
<li><p><strong>replication_task_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) for the replication task.</p></li>
<li><p><strong>replication_task_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The replication task identifier.</p></li>
<li><p><strong>replication_task_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>An escaped JSON string that contains the task settings. For a complete list of task settings, see <a class="reference external" href="http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html">Task Settings for AWS Database Migration Service Tasks</a>.</p>
</p></li>
<li><p><strong>source_endpoint_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) string that uniquely identifies the source endpoint.</p></li>
<li><p><strong>table_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>An escaped JSON string that contains the table mappings. For information on table mapping see <a class="reference external" href="http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html">Using Table Mapping with an AWS Database Migration Service Task to Select and Filter Data</a></p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>target_endpoint_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) string that uniquely identifies the target endpoint.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.dms.ReplicationTask.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dms.ReplicationTask.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dms.ReplicationTask.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
