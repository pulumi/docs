---
title: Module appsync
title_tag: Module appsync | Package pulumi_aws | Python SDK
linktitle: appsync
notitle: true
---

<div class="section" id="appsync">
<h1>appsync<a class="headerlink" href="#appsync" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.appsync"></span><dl class="class">
<dt id="pulumi_aws.appsync.ApiKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.appsync.</code><code class="sig-name descname">ApiKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expires=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.ApiKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AppSync API Key.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appsync_api_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appsync_api_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated AppSync API</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API key description. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>expires</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – RFC3339 string representation of the expiry date. Rounded down to nearest hour. By default, it is 7 days from the date of creation.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.appsync.ApiKey.api_id">
<code class="sig-name descname">api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.ApiKey.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated AppSync API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.ApiKey.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.ApiKey.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The API key description. Defaults to “Managed by Pulumi”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.ApiKey.expires">
<code class="sig-name descname">expires</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.ApiKey.expires" title="Permalink to this definition">¶</a></dt>
<dd><p>RFC3339 string representation of the expiry date. Rounded down to nearest hour. By default, it is 7 days from the date of creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.ApiKey.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.ApiKey.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The API key</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.ApiKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expires=None</em>, <em class="sig-param">key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.ApiKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApiKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated AppSync API</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API key description. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>expires</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – RFC3339 string representation of the expiry date. Rounded down to nearest hour. By default, it is 7 days from the date of creation.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API key</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.ApiKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.ApiKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.ApiKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.ApiKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.DataSource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.appsync.</code><code class="sig-name descname">DataSource</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dynamodb_config=None</em>, <em class="sig-param">elasticsearch_config=None</em>, <em class="sig-param">http_config=None</em>, <em class="sig-param">lambda_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">service_role_arn=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.DataSource" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AppSync DataSource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appsync_datasource.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appsync_datasource.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API ID for the GraphQL API for the DataSource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the DataSource.</p></li>
<li><p><strong>dynamodb_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – DynamoDB settings. See below</p></li>
<li><p><strong>elasticsearch_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Amazon Elasticsearch settings. See below</p></li>
<li><p><strong>http_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – HTTP settings. See below</p></li>
<li><p><strong>lambda_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – AWS Lambda settings. See below</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-supplied name for the DataSource.</p></li>
<li><p><strong>service_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM service role ARN for the data source.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the DataSource. Valid values: <code class="docutils literal notranslate"><span class="pre">AWS_LAMBDA</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_DYNAMODB</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_ELASTICSEARCH</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dynamodb_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS region of Elasticsearch domain. Defaults to current region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the DynamoDB table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCallerCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to use Amazon Cognito credentials with this data source.</p></li>
</ul>
<p>The <strong>elasticsearch_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS region of Elasticsearch domain. Defaults to current region.</p></li>
</ul>
<p>The <strong>http_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP URL.</p></li>
</ul>
<p>The <strong>lambda_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">function_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN for the Lambda function.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.api_id">
<code class="sig-name descname">api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API ID for the GraphQL API for the DataSource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the DataSource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.dynamodb_config">
<code class="sig-name descname">dynamodb_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.dynamodb_config" title="Permalink to this definition">¶</a></dt>
<dd><p>DynamoDB settings. See below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - AWS region of Elasticsearch domain. Defaults to current region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the DynamoDB table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCallerCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to use Amazon Cognito credentials with this data source.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.elasticsearch_config">
<code class="sig-name descname">elasticsearch_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.elasticsearch_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Elasticsearch settings. See below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - HTTP URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - AWS region of Elasticsearch domain. Defaults to current region.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.http_config">
<code class="sig-name descname">http_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.http_config" title="Permalink to this definition">¶</a></dt>
<dd><p>HTTP settings. See below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - HTTP URL.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.lambda_config">
<code class="sig-name descname">lambda_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.lambda_config" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS Lambda settings. See below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">function_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN for the Lambda function.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-supplied name for the DataSource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.service_role_arn">
<code class="sig-name descname">service_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.service_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM service role ARN for the data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the DataSource. Valid values: <code class="docutils literal notranslate"><span class="pre">AWS_LAMBDA</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_DYNAMODB</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_ELASTICSEARCH</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.DataSource.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dynamodb_config=None</em>, <em class="sig-param">elasticsearch_config=None</em>, <em class="sig-param">http_config=None</em>, <em class="sig-param">lambda_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">service_role_arn=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.DataSource.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DataSource resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API ID for the GraphQL API for the DataSource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the DataSource.</p></li>
<li><p><strong>dynamodb_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – DynamoDB settings. See below</p></li>
<li><p><strong>elasticsearch_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Amazon Elasticsearch settings. See below</p></li>
<li><p><strong>http_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – HTTP settings. See below</p></li>
<li><p><strong>lambda_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – AWS Lambda settings. See below</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-supplied name for the DataSource.</p></li>
<li><p><strong>service_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM service role ARN for the data source.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the DataSource. Valid values: <code class="docutils literal notranslate"><span class="pre">AWS_LAMBDA</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_DYNAMODB</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_ELASTICSEARCH</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dynamodb_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS region of Elasticsearch domain. Defaults to current region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">table_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the DynamoDB table.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useCallerCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to use Amazon Cognito credentials with this data source.</p></li>
</ul>
<p>The <strong>elasticsearch_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - AWS region of Elasticsearch domain. Defaults to current region.</p></li>
</ul>
<p>The <strong>http_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP URL.</p></li>
</ul>
<p>The <strong>lambda_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">function_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN for the Lambda function.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.DataSource.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.DataSource.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.DataSource.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.DataSource.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.Function">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.appsync.</code><code class="sig-name descname">Function</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">data_source=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">function_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">request_mapping_template=None</em>, <em class="sig-param">response_mapping_template=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.Function" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AppSync Function.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appsync_function.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appsync_function.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated AppSync API.</p></li>
<li><p><strong>data_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function DataSource name.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function description.</p></li>
<li><p><strong>function_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the request mapping template. Currently the supported value is <code class="docutils literal notranslate"><span class="pre">2018-05-29</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function name. The function name does not have to be unique.</p></li>
<li><p><strong>request_mapping_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.</p></li>
<li><p><strong>response_mapping_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function response mapping template.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.api_id">
<code class="sig-name descname">api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated AppSync API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Function object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.data_source">
<code class="sig-name descname">data_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.data_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function DataSource name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.function_id">
<code class="sig-name descname">function_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.function_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique ID representing the Function object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.function_version">
<code class="sig-name descname">function_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.function_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the request mapping template. Currently the supported value is <code class="docutils literal notranslate"><span class="pre">2018-05-29</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function name. The function name does not have to be unique.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.request_mapping_template">
<code class="sig-name descname">request_mapping_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.request_mapping_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.response_mapping_template">
<code class="sig-name descname">response_mapping_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.response_mapping_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function response mapping template.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.Function.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">data_source=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">function_id=None</em>, <em class="sig-param">function_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">request_mapping_template=None</em>, <em class="sig-param">response_mapping_template=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.Function.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Function resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated AppSync API.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the Function object.</p></li>
<li><p><strong>data_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function DataSource name.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function description.</p></li>
<li><p><strong>function_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique ID representing the Function object.</p></li>
<li><p><strong>function_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the request mapping template. Currently the supported value is <code class="docutils literal notranslate"><span class="pre">2018-05-29</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function name. The function name does not have to be unique.</p></li>
<li><p><strong>request_mapping_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.</p></li>
<li><p><strong>response_mapping_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function response mapping template.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.Function.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.Function.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.Function.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.Function.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.GraphQLApi">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.appsync.</code><code class="sig-name descname">GraphQLApi</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_authentication_providers=None</em>, <em class="sig-param">authentication_type=None</em>, <em class="sig-param">log_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">openid_connect_config=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">user_pool_config=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AppSync GraphQL API.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appsync_graphql_api.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appsync_graphql_api.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_authentication_providers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more additional authentication providers for the GraphqlApi. Defined below.</p></li>
<li><p><strong>authentication_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication type. Valid values: <code class="docutils literal notranslate"><span class="pre">API_KEY</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_COGNITO_USER_POOLS</span></code>, <code class="docutils literal notranslate"><span class="pre">OPENID_CONNECT</span></code></p></li>
<li><p><strong>log_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing logging configuration. Defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-supplied name for the GraphqlApi.</p></li>
<li><p><strong>openid_connect_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing OpenID Connect configuration. Defined below.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>user_pool_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The Amazon Cognito User Pool configuration. Defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>additional_authentication_providers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authentication_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authentication type. Valid values: <code class="docutils literal notranslate"><span class="pre">API_KEY</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_COGNITO_USER_POOLS</span></code>, <code class="docutils literal notranslate"><span class="pre">OPENID_CONNECT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">openid_connect_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument containing OpenID Connect configuration. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of milliseconds a token is valid after being authenticated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iatTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of milliseconds a token is valid after being issued to a user.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_pool_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Amazon Cognito User Pool configuration. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appIdClientRegex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A regular expression for validating the incoming Amazon Cognito User Pool app client ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">awsRegion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The AWS region in which the user pool was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user pool ID.</p></li>
</ul>
</li>
</ul>
<p>The <strong>log_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogsRoleArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name of the service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldLogLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Field logging level. Valid values: <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">ERROR</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
</ul>
<p>The <strong>openid_connect_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of milliseconds a token is valid after being authenticated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iatTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of milliseconds a token is valid after being issued to a user.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.</p></li>
</ul>
<p>The <strong>user_pool_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appIdClientRegex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A regular expression for validating the incoming Amazon Cognito User Pool app client ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">awsRegion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The AWS region in which the user pool was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn’t match the Amazon Cognito User Pool configuration. Valid: <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code> and <code class="docutils literal notranslate"><span class="pre">DENY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user pool ID.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.additional_authentication_providers">
<code class="sig-name descname">additional_authentication_providers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.additional_authentication_providers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more additional authentication providers for the GraphqlApi. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authentication_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The authentication type. Valid values: <code class="docutils literal notranslate"><span class="pre">API_KEY</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_COGNITO_USER_POOLS</span></code>, <code class="docutils literal notranslate"><span class="pre">OPENID_CONNECT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">openid_connect_config</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument containing OpenID Connect configuration. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of milliseconds a token is valid after being authenticated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iatTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of milliseconds a token is valid after being issued to a user.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_pool_config</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The Amazon Cognito User Pool configuration. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appIdClientRegex</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A regular expression for validating the incoming Amazon Cognito User Pool app client ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">awsRegion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The AWS region in which the user pool was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The user pool ID.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.authentication_type">
<code class="sig-name descname">authentication_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.authentication_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication type. Valid values: <code class="docutils literal notranslate"><span class="pre">API_KEY</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_COGNITO_USER_POOLS</span></code>, <code class="docutils literal notranslate"><span class="pre">OPENID_CONNECT</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.log_config">
<code class="sig-name descname">log_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.log_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument containing logging configuration. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogsRoleArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon Resource Name of the service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldLogLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Field logging level. Valid values: <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">ERROR</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-supplied name for the GraphqlApi.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.openid_connect_config">
<code class="sig-name descname">openid_connect_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.openid_connect_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument containing OpenID Connect configuration. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of milliseconds a token is valid after being authenticated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iatTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of milliseconds a token is valid after being issued to a user.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.schema">
<code class="sig-name descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.uris">
<code class="sig-name descname">uris</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.uris" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of URIs associated with the API. e.g. <code class="docutils literal notranslate"><span class="pre">uris[&quot;GRAPHQL&quot;]</span> <span class="pre">=</span> <span class="pre">https://ID.appsync-api.REGION.amazonaws.com/graphql</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.user_pool_config">
<code class="sig-name descname">user_pool_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.user_pool_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Cognito User Pool configuration. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appIdClientRegex</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A regular expression for validating the incoming Amazon Cognito User Pool app client ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">awsRegion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The AWS region in which the user pool was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn’t match the Amazon Cognito User Pool configuration. Valid: <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code> and <code class="docutils literal notranslate"><span class="pre">DENY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The user pool ID.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.GraphQLApi.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_authentication_providers=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">authentication_type=None</em>, <em class="sig-param">log_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">openid_connect_config=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">uris=None</em>, <em class="sig-param">user_pool_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GraphQLApi resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_authentication_providers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more additional authentication providers for the GraphqlApi. Defined below.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN</p></li>
<li><p><strong>authentication_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication type. Valid values: <code class="docutils literal notranslate"><span class="pre">API_KEY</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_COGNITO_USER_POOLS</span></code>, <code class="docutils literal notranslate"><span class="pre">OPENID_CONNECT</span></code></p></li>
<li><p><strong>log_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing logging configuration. Defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-supplied name for the GraphqlApi.</p></li>
<li><p><strong>openid_connect_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing OpenID Connect configuration. Defined below.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The schema definition, in GraphQL schema language format. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>uris</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of URIs associated with the API. e.g. <code class="docutils literal notranslate"><span class="pre">uris[&quot;GRAPHQL&quot;]</span> <span class="pre">=</span> <span class="pre">https://ID.appsync-api.REGION.amazonaws.com/graphql</span></code></p></li>
<li><p><strong>user_pool_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The Amazon Cognito User Pool configuration. Defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>additional_authentication_providers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authentication_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authentication type. Valid values: <code class="docutils literal notranslate"><span class="pre">API_KEY</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_COGNITO_USER_POOLS</span></code>, <code class="docutils literal notranslate"><span class="pre">OPENID_CONNECT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">openid_connect_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument containing OpenID Connect configuration. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">authTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of milliseconds a token is valid after being authenticated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iatTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of milliseconds a token is valid after being issued to a user.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_pool_config</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The Amazon Cognito User Pool configuration. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">appIdClientRegex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A regular expression for validating the incoming Amazon Cognito User Pool app client ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">awsRegion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The AWS region in which the user pool was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user pool ID.</p></li>
</ul>
</li>
</ul>
<p>The <strong>log_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogsRoleArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name of the service role that AWS AppSync will assume to publish to Amazon CloudWatch logs in your account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fieldLogLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Field logging level. Valid values: <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">ERROR</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
</ul>
<p>The <strong>openid_connect_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of milliseconds a token is valid after being authenticated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Client identifier of the Relying party at the OpenID identity provider. This identifier is typically obtained when the Relying party is registered with the OpenID identity provider. You can specify a regular expression so the AWS AppSync can validate against multiple client identifiers at a time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iatTtl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of milliseconds a token is valid after being issued to a user.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Issuer for the OpenID Connect configuration. The issuer returned by discovery MUST exactly match the value of iss in the ID Token.</p></li>
</ul>
<p>The <strong>user_pool_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appIdClientRegex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A regular expression for validating the incoming Amazon Cognito User Pool app client ID.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">awsRegion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The AWS region in which the user pool was created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action that you want your GraphQL API to take when a request that uses Amazon Cognito User Pool authentication doesn’t match the Amazon Cognito User Pool configuration. Valid: <code class="docutils literal notranslate"><span class="pre">ALLOW</span></code> and <code class="docutils literal notranslate"><span class="pre">DENY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user pool ID.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.GraphQLApi.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.GraphQLApi.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.Resolver">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.appsync.</code><code class="sig-name descname">Resolver</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">data_source=None</em>, <em class="sig-param">field=None</em>, <em class="sig-param">kind=None</em>, <em class="sig-param">pipeline_config=None</em>, <em class="sig-param">request_template=None</em>, <em class="sig-param">response_template=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.Resolver" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AppSync Resolver.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appsync_resolver.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appsync_resolver.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API ID for the GraphQL API.</p></li>
<li><p><strong>data_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DataSource name.</p></li>
<li><p><strong>field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The field name from the schema defined in the GraphQL API.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resolver type. Valid values are <code class="docutils literal notranslate"><span class="pre">UNIT</span></code> and <code class="docutils literal notranslate"><span class="pre">PIPELINE</span></code>.</p></li>
<li><p><strong>pipeline_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The PipelineConfig. A <code class="docutils literal notranslate"><span class="pre">pipeline_config</span></code> block is documented below.</p></li>
<li><p><strong>request_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The request mapping template for UNIT resolver or ‘before mapping template’ for PIPELINE resolver.</p></li>
<li><p><strong>response_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The response mapping template for UNIT resolver or ‘after mapping template’ for PIPELINE resolver.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type name from the schema defined in the GraphQL API.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>pipeline_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">functions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.api_id">
<code class="sig-name descname">api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API ID for the GraphQL API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.data_source">
<code class="sig-name descname">data_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.data_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The DataSource name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.field">
<code class="sig-name descname">field</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.field" title="Permalink to this definition">¶</a></dt>
<dd><p>The field name from the schema defined in the GraphQL API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.kind">
<code class="sig-name descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The resolver type. Valid values are <code class="docutils literal notranslate"><span class="pre">UNIT</span></code> and <code class="docutils literal notranslate"><span class="pre">PIPELINE</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.pipeline_config">
<code class="sig-name descname">pipeline_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.pipeline_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The PipelineConfig. A <code class="docutils literal notranslate"><span class="pre">pipeline_config</span></code> block is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">functions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.request_template">
<code class="sig-name descname">request_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.request_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The request mapping template for UNIT resolver or ‘before mapping template’ for PIPELINE resolver.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.response_template">
<code class="sig-name descname">response_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.response_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The response mapping template for UNIT resolver or ‘after mapping template’ for PIPELINE resolver.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type name from the schema defined in the GraphQL API.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.Resolver.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">data_source=None</em>, <em class="sig-param">field=None</em>, <em class="sig-param">kind=None</em>, <em class="sig-param">pipeline_config=None</em>, <em class="sig-param">request_template=None</em>, <em class="sig-param">response_template=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.Resolver.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Resolver resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API ID for the GraphQL API.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN</p></li>
<li><p><strong>data_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DataSource name.</p></li>
<li><p><strong>field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The field name from the schema defined in the GraphQL API.</p></li>
<li><p><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resolver type. Valid values are <code class="docutils literal notranslate"><span class="pre">UNIT</span></code> and <code class="docutils literal notranslate"><span class="pre">PIPELINE</span></code>.</p></li>
<li><p><strong>pipeline_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The PipelineConfig. A <code class="docutils literal notranslate"><span class="pre">pipeline_config</span></code> block is documented below.</p></li>
<li><p><strong>request_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The request mapping template for UNIT resolver or ‘before mapping template’ for PIPELINE resolver.</p></li>
<li><p><strong>response_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The response mapping template for UNIT resolver or ‘after mapping template’ for PIPELINE resolver.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type name from the schema defined in the GraphQL API.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>pipeline_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">functions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.Resolver.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.Resolver.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.Resolver.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.Resolver.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
