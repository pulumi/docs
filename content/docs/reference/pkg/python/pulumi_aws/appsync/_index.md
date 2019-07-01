---
---

<div class="section" id="module-pulumi_aws.appsync">
<span id="appsync"></span><h1>appsync<a class="headerlink" href="#module-pulumi_aws.appsync" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.appsync.ApiKey">
<em class="property">class </em><code class="descclassname">pulumi_aws.appsync.</code><code class="descname">ApiKey</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_id=None</em>, <em>description=None</em>, <em>expires=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.ApiKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AppSync API Key.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated AppSync API</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API key description. Defaults to “Managed by Terraform”.</li>
<li><strong>expires</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – RFC3339 string representation of the expiry date. Rounded down to nearest hour. By default, it is 7 days from the date of creation.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.appsync.ApiKey.api_id">
<code class="descname">api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.ApiKey.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated AppSync API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.ApiKey.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.ApiKey.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The API key description. Defaults to “Managed by Terraform”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.ApiKey.expires">
<code class="descname">expires</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.ApiKey.expires" title="Permalink to this definition">¶</a></dt>
<dd><p>RFC3339 string representation of the expiry date. Rounded down to nearest hour. By default, it is 7 days from the date of creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.ApiKey.key">
<code class="descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.ApiKey.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The API key</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.ApiKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.ApiKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.ApiKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.ApiKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.DataSource">
<em class="property">class </em><code class="descclassname">pulumi_aws.appsync.</code><code class="descname">DataSource</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_id=None</em>, <em>description=None</em>, <em>dynamodb_config=None</em>, <em>elasticsearch_config=None</em>, <em>http_config=None</em>, <em>lambda_config=None</em>, <em>name=None</em>, <em>service_role_arn=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.DataSource" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AppSync DataSource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API ID for the GraphQL API for the DataSource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the DataSource.</li>
<li><strong>dynamodb_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – DynamoDB settings. See below</li>
<li><strong>elasticsearch_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Amazon Elasticsearch settings. See below</li>
<li><strong>http_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – HTTP settings. See below</li>
<li><strong>lambda_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – AWS Lambda settings. See below</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-supplied name for the DataSource.</li>
<li><strong>service_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM service role ARN for the data source.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the DataSource. Valid values: <code class="docutils literal notranslate"><span class="pre">AWS_LAMBDA</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_DYNAMODB</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_ELASTICSEARCH</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.api_id">
<code class="descname">api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API ID for the GraphQL API for the DataSource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the DataSource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.dynamodb_config">
<code class="descname">dynamodb_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.dynamodb_config" title="Permalink to this definition">¶</a></dt>
<dd><p>DynamoDB settings. See below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.elasticsearch_config">
<code class="descname">elasticsearch_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.elasticsearch_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Elasticsearch settings. See below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.http_config">
<code class="descname">http_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.http_config" title="Permalink to this definition">¶</a></dt>
<dd><p>HTTP settings. See below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.lambda_config">
<code class="descname">lambda_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.lambda_config" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS Lambda settings. See below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-supplied name for the DataSource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.service_role_arn">
<code class="descname">service_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.service_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM service role ARN for the data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.DataSource.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.DataSource.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the DataSource. Valid values: <code class="docutils literal notranslate"><span class="pre">AWS_LAMBDA</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_DYNAMODB</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_ELASTICSEARCH</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.DataSource.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.DataSource.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.DataSource.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.DataSource.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.Function">
<em class="property">class </em><code class="descclassname">pulumi_aws.appsync.</code><code class="descname">Function</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_id=None</em>, <em>data_source=None</em>, <em>description=None</em>, <em>function_version=None</em>, <em>name=None</em>, <em>request_mapping_template=None</em>, <em>response_mapping_template=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.Function" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AppSync Function.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated AppSync API.</li>
<li><strong>data_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function DataSource name.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function description.</li>
<li><strong>function_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the request mapping template. Currently the supported value is <code class="docutils literal notranslate"><span class="pre">2018-05-29</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function name. The function name does not have to be unique.</li>
<li><strong>request_mapping_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.</li>
<li><strong>response_mapping_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Function response mapping template.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.api_id">
<code class="descname">api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated AppSync API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the Function object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.data_source">
<code class="descname">data_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.data_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function DataSource name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.function_id">
<code class="descname">function_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.function_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique ID representing the Function object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.function_version">
<code class="descname">function_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.function_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the request mapping template. Currently the supported value is <code class="docutils literal notranslate"><span class="pre">2018-05-29</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function name. The function name does not have to be unique.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.request_mapping_template">
<code class="descname">request_mapping_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.request_mapping_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function request mapping template. Functions support only the 2018-05-29 version of the request mapping template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Function.response_mapping_template">
<code class="descname">response_mapping_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Function.response_mapping_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The Function response mapping template.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.Function.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.Function.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.Function.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.Function.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.GraphQLApi">
<em class="property">class </em><code class="descclassname">pulumi_aws.appsync.</code><code class="descname">GraphQLApi</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>authentication_type=None</em>, <em>log_config=None</em>, <em>name=None</em>, <em>openid_connect_config=None</em>, <em>schema=None</em>, <em>tags=None</em>, <em>user_pool_config=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AppSync GraphQL API.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>authentication_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication type. Valid values: <code class="docutils literal notranslate"><span class="pre">API_KEY</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_COGNITO_USER_POOLS</span></code>, <code class="docutils literal notranslate"><span class="pre">OPENID_CONNECT</span></code></li>
<li><strong>log_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing logging configuration. Defined below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-supplied name for the GraphqlApi.</li>
<li><strong>openid_connect_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing OpenID Connect configuration. Defined below.</li>
<li><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The schema definition, in GraphQL schema language format. Terraform cannot perform drift detection of this configuration.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>user_pool_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The Amazon Cognito User Pool configuration. Defined below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.authentication_type">
<code class="descname">authentication_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.authentication_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication type. Valid values: <code class="docutils literal notranslate"><span class="pre">API_KEY</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">AMAZON_COGNITO_USER_POOLS</span></code>, <code class="docutils literal notranslate"><span class="pre">OPENID_CONNECT</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.log_config">
<code class="descname">log_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.log_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument containing logging configuration. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-supplied name for the GraphqlApi.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.openid_connect_config">
<code class="descname">openid_connect_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.openid_connect_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument containing OpenID Connect configuration. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.schema">
<code class="descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The schema definition, in GraphQL schema language format. Terraform cannot perform drift detection of this configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.uris">
<code class="descname">uris</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.uris" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of URIs associated with the API. e.g. <code class="docutils literal notranslate"><span class="pre">uris[&quot;GRAPHQL&quot;]</span> <span class="pre">=</span> <span class="pre">https://ID.appsync-api.REGION.amazonaws.com/graphql</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.GraphQLApi.user_pool_config">
<code class="descname">user_pool_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.user_pool_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Cognito User Pool configuration. Defined below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.GraphQLApi.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.GraphQLApi.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.Resolver">
<em class="property">class </em><code class="descclassname">pulumi_aws.appsync.</code><code class="descname">Resolver</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>api_id=None</em>, <em>data_source=None</em>, <em>field=None</em>, <em>kind=None</em>, <em>pipeline_config=None</em>, <em>request_template=None</em>, <em>response_template=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.Resolver" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AppSync Resolver.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API ID for the GraphQL API.</li>
<li><strong>data_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DataSource name.</li>
<li><strong>field</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The field name from the schema defined in the GraphQL API.</li>
<li><strong>kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resolver type. Valid values are <code class="docutils literal notranslate"><span class="pre">UNIT</span></code> and <code class="docutils literal notranslate"><span class="pre">PIPELINE</span></code>.</li>
<li><strong>pipeline_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The PipelineConfig. A <code class="docutils literal notranslate"><span class="pre">pipeline_config</span></code> block is documented below.</li>
<li><strong>request_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The request mapping template for this resolver.</li>
<li><strong>response_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The response mapping template for this resolver.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type name from the schema defined in the GraphQL API.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.api_id">
<code class="descname">api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API ID for the GraphQL API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.data_source">
<code class="descname">data_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.data_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The DataSource name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.field">
<code class="descname">field</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.field" title="Permalink to this definition">¶</a></dt>
<dd><p>The field name from the schema defined in the GraphQL API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.kind">
<code class="descname">kind</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.kind" title="Permalink to this definition">¶</a></dt>
<dd><p>The resolver type. Valid values are <code class="docutils literal notranslate"><span class="pre">UNIT</span></code> and <code class="docutils literal notranslate"><span class="pre">PIPELINE</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.pipeline_config">
<code class="descname">pipeline_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.pipeline_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The PipelineConfig. A <code class="docutils literal notranslate"><span class="pre">pipeline_config</span></code> block is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.request_template">
<code class="descname">request_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.request_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The request mapping template for this resolver.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.response_template">
<code class="descname">response_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.response_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The response mapping template for this resolver.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appsync.Resolver.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.Resolver.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type name from the schema defined in the GraphQL API.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.Resolver.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.Resolver.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appsync.Resolver.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.Resolver.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
