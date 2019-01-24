<div class="section" id="module-pulumi_aws.appsync">
<span id="appsync"></span><h1>appsync<a class="headerlink" href="#module-pulumi_aws.appsync" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.appsync.ApiKey">
<em class="property">class </em><code class="descclassname">pulumi_aws.appsync.</code><code class="descname">ApiKey</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>api_id=None</em>, <em>description=None</em>, <em>expires=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.ApiKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AppSync API Key.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
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
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.ApiKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.ApiKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.appsync.DataSource">
<em class="property">class </em><code class="descclassname">pulumi_aws.appsync.</code><code class="descname">DataSource</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>api_id=None</em>, <em>description=None</em>, <em>dynamodb_config=None</em>, <em>elasticsearch_config=None</em>, <em>http_config=None</em>, <em>lambda_config=None</em>, <em>name=None</em>, <em>service_role_arn=None</em>, <em>type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.DataSource" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AppSync DataSource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API ID for the GraphQL API for the DataSource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the DataSource.</li>
<li><strong>dynamodb_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – DynamoDB settings. See below</li>
<li><strong>elasticsearch_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Amazon Elasticsearch settings. See below</li>
<li><strong>http_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – HTTP settings. See below</li>
<li><strong>lambda_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – AWS Lambda settings. See below</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-supplied name for the DataSource.</li>
<li><strong>service_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM service role ARN for the data source.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the DataSource. Valid values: <cite>AWS_LAMBDA</cite>, <cite>AMAZON_DYNAMODB</cite>, <cite>AMAZON_ELASTICSEARCH</cite>, <cite>HTTP</cite>, <cite>NONE</cite>.</li>
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
<dd><p>The type of the DataSource. Valid values: <cite>AWS_LAMBDA</cite>, <cite>AMAZON_DYNAMODB</cite>, <cite>AMAZON_ELASTICSEARCH</cite>, <cite>HTTP</cite>, <cite>NONE</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.DataSource.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.DataSource.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.DataSource.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.DataSource.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.appsync.GraphQLApi">
<em class="property">class </em><code class="descclassname">pulumi_aws.appsync.</code><code class="descname">GraphQLApi</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>authentication_type=None</em>, <em>log_config=None</em>, <em>name=None</em>, <em>openid_connect_config=None</em>, <em>user_pool_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AppSync GraphQL API.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>authentication_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication type. Valid values: <cite>API_KEY</cite>, <cite>AWS_IAM</cite>, <cite>AMAZON_COGNITO_USER_POOLS</cite>, <cite>OPENID_CONNECT</cite></li>
<li><strong>log_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing logging configuration. Defined below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-supplied name for the GraphqlApi.</li>
<li><strong>openid_connect_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing OpenID Connect configuration. Defined below.</li>
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
<dd><p>The authentication type. Valid values: <cite>API_KEY</cite>, <cite>AWS_IAM</cite>, <cite>AMAZON_COGNITO_USER_POOLS</cite>, <cite>OPENID_CONNECT</cite></p>
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
<dt id="pulumi_aws.appsync.GraphQLApi.uris">
<code class="descname">uris</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.uris" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of URIs associated with the API. e.g. <cite>uris[“GRAPHQL”] = https://ID.appsync-api.REGION.amazonaws.com/graphql</cite></p>
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
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appsync.GraphQLApi.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appsync.GraphQLApi.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
