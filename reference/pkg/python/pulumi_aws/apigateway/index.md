<div class="section" id="module-pulumi_aws.apigateway">
<span id="apigateway"></span><h1>apigateway<a class="headerlink" href="#module-pulumi_aws.apigateway" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.apigateway.Account">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">Account</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>cloudwatch_role_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a settings of an API Gateway Account. Settings is applied region-wide per <cite>provider</cite> block.</p>
<p>-&gt; <strong>Note:</strong> As there is no API method for deleting account settings or resetting it to defaults, destroying this resource will keep your account settings intact</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cloudwatch_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role for CloudWatch (to allow logging &amp; monitoring).
See more [in AWS Docs](<a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console">https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console</a>).
Logging &amp; monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Account.cloudwatch_role_arn">
<code class="descname">cloudwatch_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Account.cloudwatch_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM role for CloudWatch (to allow logging &amp; monitoring).
See more [in AWS Docs](<a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console">https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console</a>).
Logging &amp; monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Account.throttle_settings">
<code class="descname">throttle_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Account.throttle_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Account-Level throttle settings. See exported fields below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Account.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Account.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.ApiKey">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">ApiKey</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>enabled=None</em>, <em>name=None</em>, <em>stage_keys=None</em>, <em>value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway API Key.</p>
<p>&gt; <strong>Warning:</strong> Since the API Gateway usage plans feature was launched on August 11, 2016, usage plans are now <strong>required</strong> to associate an API key with an API stage.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API key description. Defaults to “Managed by Terraform”.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the API key can be used by callers. Defaults to <cite>true</cite>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API key</li>
<li><strong>stage_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of stage keys associated with the API key - see below</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the API key. If not specified, it will be automatically generated by AWS on creation.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.created_date">
<code class="descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the API key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The API key description. Defaults to “Managed by Terraform”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the API key can be used by callers. Defaults to <cite>true</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.last_updated_date">
<code class="descname">last_updated_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.last_updated_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The last update date of the API key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.stage_keys">
<code class="descname">stage_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.stage_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of stage keys associated with the API key - see below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the API key. If not specified, it will be automatically generated by AWS on creation.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.ApiKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.ApiKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Authorizer">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">Authorizer</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>authorizer_credentials=None</em>, <em>authorizer_result_ttl_in_seconds=None</em>, <em>authorizer_uri=None</em>, <em>identity_source=None</em>, <em>identity_validation_expression=None</em>, <em>name=None</em>, <em>provider_arns=None</em>, <em>rest_api=None</em>, <em>type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Authorizer.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>authorizer_credentials</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.</li>
<li><strong>authorizer_result_ttl_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The TTL of cached authorizer results in seconds.
Defaults to <cite>300</cite>.</li>
<li><strong>authorizer_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorizer’s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of <cite>arn:aws:apigateway:{region}:lambda:path/{service_api}</cite>,
e.g. <cite>arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations</cite></li>
<li><strong>identity_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source of the identity in an incoming request.
Defaults to <cite>method.request.header.Authorization</cite>. For <cite>REQUEST</cite> type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. <cite>“method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName”</cite></li>
<li><strong>identity_validation_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A validation expression for the incoming identity.
For <cite>TOKEN</cite> type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn’t match,
the client receives a 401 Unauthorized response.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the authorizer</li>
<li><strong>provider_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the Amazon Cognito user pool ARNs.
Each element is of this format: <cite>arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}</cite>.</li>
<li><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the authorizer. Possible values are <cite>TOKEN</cite> for a Lambda function using a single authorization token submitted in a custom header, <cite>REQUEST</cite> for a Lambda function using incoming request parameters, or <cite>COGNITO_USER_POOLS</cite> for using an Amazon Cognito user pool.
Defaults to <cite>TOKEN</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.authorizer_credentials">
<code class="descname">authorizer_credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.authorizer_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.authorizer_result_ttl_in_seconds">
<code class="descname">authorizer_result_ttl_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.authorizer_result_ttl_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL of cached authorizer results in seconds.
Defaults to <cite>300</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.authorizer_uri">
<code class="descname">authorizer_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.authorizer_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorizer’s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of <cite>arn:aws:apigateway:{region}:lambda:path/{service_api}</cite>,
e.g. <cite>arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.identity_source">
<code class="descname">identity_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.identity_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The source of the identity in an incoming request.
Defaults to <cite>method.request.header.Authorization</cite>. For <cite>REQUEST</cite> type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. <cite>“method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName”</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.identity_validation_expression">
<code class="descname">identity_validation_expression</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.identity_validation_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>A validation expression for the incoming identity.
For <cite>TOKEN</cite> type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn’t match,
the client receives a 401 Unauthorized response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the authorizer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.provider_arns">
<code class="descname">provider_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.provider_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Amazon Cognito user pool ARNs.
Each element is of this format: <cite>arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.rest_api">
<code class="descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the authorizer. Possible values are <cite>TOKEN</cite> for a Lambda function using a single authorization token submitted in a custom header, <cite>REQUEST</cite> for a Lambda function using incoming request parameters, or <cite>COGNITO_USER_POOLS</cite> for using an Amazon Cognito user pool.
Defaults to <cite>TOKEN</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Authorizer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Authorizer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.BasePathMapping">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">BasePathMapping</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>rest_api=None</em>, <em>base_path=None</em>, <em>domain_name=None</em>, <em>stage_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping" title="Permalink to this definition">¶</a></dt>
<dd><p>Connects a custom domain name registered via <cite>aws_api_gateway_domain_name</cite>
with a deployed API so that its methods can be called via the
custom domain name.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the API to connect.</li>
<li><strong>base_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.</li>
<li><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The already-registered domain name to connect the API to.</li>
<li><strong>stage_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.BasePathMapping.rest_api">
<code class="descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the API to connect.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.BasePathMapping.base_path">
<code class="descname">base_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping.base_path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.BasePathMapping.domain_name">
<code class="descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The already-registered domain name to connect the API to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.BasePathMapping.stage_name">
<code class="descname">stage_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping.stage_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.BasePathMapping.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.BasePathMapping.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.ClientCertificate">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">ClientCertificate</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Client Certificate.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the client certificate.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.ClientCertificate.created_date">
<code class="descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date when the client certificate was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ClientCertificate.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the client certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ClientCertificate.expiration_date">
<code class="descname">expiration_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.expiration_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date when the client certificate will expire.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ClientCertificate.pem_encoded_certificate">
<code class="descname">pem_encoded_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.pem_encoded_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The PEM-encoded public key of the client certificate.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.ClientCertificate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.ClientCertificate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Deployment">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">Deployment</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>rest_api=None</em>, <em>stage_description=None</em>, <em>stage_name=None</em>, <em>variables=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Deployment.</p>
<p>-&gt; <strong>Note:</strong> Depends on having <cite>aws_api_gateway_integration</cite> inside your rest api (which in turn depends on <cite>aws_api_gateway_method</cite>). To avoid race conditions
you might need to add an explicit <cite>depends_on = [“aws_api_gateway_integration.name”]</cite>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the deployment</li>
<li><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</li>
<li><strong>stage_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the stage</li>
<li><strong>stage_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stage. If the specified stage already exists, it will be updated to point to the new deployment. If the stage does not exist, a new one will be created and point to this deployment. Use <cite>“”</cite> to point at the default stage.</li>
<li><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map that defines variables for the stage</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.created_date">
<code class="descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the deployment</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the deployment</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.execution_arn">
<code class="descname">execution_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.execution_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The execution ARN to be used in [<cite>lambda_permission</cite>](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)’s</a> <cite>source_arn</cite>
when allowing API Gateway to invoke a Lambda function,
e.g. <cite>arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.invoke_url">
<code class="descname">invoke_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.invoke_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to invoke the API pointing to the stage,
e.g. <cite>https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.rest_api">
<code class="descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.stage_description">
<code class="descname">stage_description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.stage_description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the stage</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.stage_name">
<code class="descname">stage_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.stage_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the stage. If the specified stage already exists, it will be updated to point to the new deployment. If the stage does not exist, a new one will be created and point to this deployment. Use <cite>“”</cite> to point at the default stage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.variables">
<code class="descname">variables</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.variables" title="Permalink to this definition">¶</a></dt>
<dd><p>A map that defines variables for the stage</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Deployment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Deployment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.DocumentationPart">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">DocumentationPart</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>location=None</em>, <em>properties=None</em>, <em>rest_api_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationPart" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a settings of an API Gateway Documentation Part.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The location of the targeted API entity of the to-be-created documentation part. See below.</li>
<li><strong>properties</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., “{ “description”: “The API does …” }”. Only Swagger-compliant key-value pairs can be exported and, hence, published.</li>
<li><strong>rest_api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated Rest API</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.DocumentationPart.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationPart.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the targeted API entity of the to-be-created documentation part. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DocumentationPart.properties">
<code class="descname">properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationPart.properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., “{ “description”: “The API does …” }”. Only Swagger-compliant key-value pairs can be exported and, hence, published.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DocumentationPart.rest_api_id">
<code class="descname">rest_api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationPart.rest_api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated Rest API</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.DocumentationPart.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationPart.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.DocumentationPart.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationPart.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.DocumentationVersion">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">DocumentationVersion</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>rest_api_id=None</em>, <em>version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage an API Gateway Documentation Version.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the API documentation version.</li>
<li><strong>rest_api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated Rest API</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version identifier of the API documentation snapshot.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.DocumentationVersion.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationVersion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the API documentation version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DocumentationVersion.rest_api_id">
<code class="descname">rest_api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationVersion.rest_api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated Rest API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DocumentationVersion.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationVersion.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version identifier of the API documentation snapshot.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.DocumentationVersion.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationVersion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.DocumentationVersion.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationVersion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.DomainName">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">DomainName</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>certificate_arn=None</em>, <em>certificate_body=None</em>, <em>certificate_chain=None</em>, <em>certificate_name=None</em>, <em>certificate_private_key=None</em>, <em>domain_name=None</em>, <em>endpoint_configuration=None</em>, <em>regional_certificate_arn=None</em>, <em>regional_certificate_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DomainName" title="Permalink to this definition">¶</a></dt>
<dd><p>Registers a custom domain name for use with AWS API Gateway.</p>
<p>This resource just establishes ownership of and the TLS settings for
a particular domain name. An API can be attached to a particular path
under the registered domain name using
the <cite>aws_api_gateway_base_path_mapping</cite> resource.</p>
<p>API Gateway domains can be defined as either ‘edge-optimized’ or ‘regional’.  In an edge-optimized configuration,
API Gateway internally creates and manages a CloudFront distribution to route requests on the given hostname. In
addition to this resource it’s necessary to create a DNS record corresponding to the given domain name which is an alias
(either Route53 alias or traditional CNAME) to the Cloudfront domain name exported in the <cite>cloudfront_domain_name</cite>
attribute.</p>
<p>In a regional configuration, API Gateway does not create a CloudFront distribution to route requests to the API, though
a distribution can be created if needed. In either case, it is necessary to create a DNS record corresponding to the
given domain name which is an alias (either Route53 alias or traditional CNAME) to the regional domain name exported in
the <cite>regional_domain_name</cite> attribute.</p>
<p>&gt; <strong>Note:</strong> All arguments including the private key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">https://www.terraform.io/docs/state/sensitive-data.html</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with <cite>certificate_name</cite>, <cite>certificate_body</cite>, <cite>certificate_chain</cite>, <cite>certificate_private_key</cite>, <cite>regional_certificate_arn</cite>, and <cite>regional_certificate_name</cite>.</li>
<li><strong>certificate_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate issued for the domain name
being registered, in PEM format. Only valid for <cite>EDGE</cite> endpoint configuration type. Conflicts with <cite>certificate_arn</cite>, <cite>regional_certificate_arn</cite>, and
<cite>regional_certificate_name</cite>.</li>
<li><strong>certificate_chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for <cite>EDGE</cite> endpoint configuration type. Conflicts with <cite>certificate_arn</cite>,
<cite>regional_certificate_arn</cite>, and <cite>regional_certificate_name</cite>.</li>
<li><strong>certificate_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with <cite>certificate_arn</cite>, <cite>regional_certificate_arn</cite>, and
<cite>regional_certificate_name</cite>. Required if <cite>certificate_arn</cite> is not set.</li>
<li><strong>certificate_private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key associated with the
domain certificate given in <cite>certificate_body</cite>. Only valid for <cite>EDGE</cite> endpoint configuration type. Conflicts with <cite>certificate_arn</cite>, <cite>regional_certificate_arn</cite>, and <cite>regional_certificate_name</cite>.</li>
<li><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully-qualified domain name to register</li>
<li><strong>endpoint_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block defining API endpoint information including type. Defined below.</li>
<li><strong>regional_certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with <cite>certificate_arn</cite>, <cite>certificate_name</cite>, <cite>certificate_body</cite>, <cite>certificate_chain</cite>, and <cite>certificate_private_key</cite>.</li>
<li><strong>regional_certificate_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with <cite>certificate_arn</cite>, <cite>certificate_name</cite>, <cite>certificate_body</cite>, <cite>certificate_chain</cite>, and
<cite>certificate_private_key</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.certificate_arn">
<code class="descname">certificate_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with <cite>certificate_name</cite>, <cite>certificate_body</cite>, <cite>certificate_chain</cite>, <cite>certificate_private_key</cite>, <cite>regional_certificate_arn</cite>, and <cite>regional_certificate_name</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.certificate_body">
<code class="descname">certificate_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.certificate_body" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate issued for the domain name
being registered, in PEM format. Only valid for <cite>EDGE</cite> endpoint configuration type. Conflicts with <cite>certificate_arn</cite>, <cite>regional_certificate_arn</cite>, and
<cite>regional_certificate_name</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.certificate_chain">
<code class="descname">certificate_chain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.certificate_chain" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for <cite>EDGE</cite> endpoint configuration type. Conflicts with <cite>certificate_arn</cite>,
<cite>regional_certificate_arn</cite>, and <cite>regional_certificate_name</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.certificate_name">
<code class="descname">certificate_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.certificate_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with <cite>certificate_arn</cite>, <cite>regional_certificate_arn</cite>, and
<cite>regional_certificate_name</cite>. Required if <cite>certificate_arn</cite> is not set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.certificate_private_key">
<code class="descname">certificate_private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.certificate_private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key associated with the
domain certificate given in <cite>certificate_body</cite>. Only valid for <cite>EDGE</cite> endpoint configuration type. Conflicts with <cite>certificate_arn</cite>, <cite>regional_certificate_arn</cite>, and <cite>regional_certificate_name</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.certificate_upload_date">
<code class="descname">certificate_upload_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.certificate_upload_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The upload date associated with the domain certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.cloudfront_domain_name">
<code class="descname">cloudfront_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.cloudfront_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.cloudfront_zone_id">
<code class="descname">cloudfront_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.cloudfront_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>For convenience, the hosted zone ID (<cite>Z2FDTNDATAQYW2</cite>)
that can be used to create a Route53 alias record for the distribution.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.domain_name">
<code class="descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-qualified domain name to register</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.endpoint_configuration">
<code class="descname">endpoint_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.endpoint_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block defining API endpoint information including type. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.regional_certificate_arn">
<code class="descname">regional_certificate_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.regional_certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with <cite>certificate_arn</cite>, <cite>certificate_name</cite>, <cite>certificate_body</cite>, <cite>certificate_chain</cite>, and <cite>certificate_private_key</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.regional_certificate_name">
<code class="descname">regional_certificate_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.regional_certificate_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with <cite>certificate_arn</cite>, <cite>certificate_name</cite>, <cite>certificate_body</cite>, <cite>certificate_chain</cite>, and
<cite>certificate_private_key</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.regional_domain_name">
<code class="descname">regional_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.regional_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname for the custom domain’s regional endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.regional_zone_id">
<code class="descname">regional_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.regional_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.DomainName.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.DomainName.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.GetKeyResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">GetKeyResult</code><span class="sig-paren">(</span><em>name=None</em>, <em>value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.GetKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKey.</p>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetKeyResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetKeyResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the name of the API Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetKeyResult.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetKeyResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the value of the API Key.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.apigateway.GetResourceResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">GetResourceResult</code><span class="sig-paren">(</span><em>parent_id=None</em>, <em>path_part=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.GetResourceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getResource.</p>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetResourceResult.parent_id">
<code class="descname">parent_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetResourceResult.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the ID of the parent Resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetResourceResult.path_part">
<code class="descname">path_part</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetResourceResult.path_part" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the path relative to the parent Resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetResourceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetResourceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.apigateway.GetRestApiResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">GetRestApiResult</code><span class="sig-paren">(</span><em>root_resource_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.GetRestApiResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRestApi.</p>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetRestApiResult.root_resource_id">
<code class="descname">root_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetRestApiResult.root_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the ID of the API Gateway Resource on the found REST API where the route matches ‘/’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetRestApiResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetRestApiResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.apigateway.GetVpcLinkResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">GetVpcLinkResult</code><span class="sig-paren">(</span><em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.GetVpcLinkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpcLink.</p>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetVpcLinkResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetVpcLinkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the ID of the found API Gateway VPC Link.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.apigateway.Integration">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">Integration</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>cache_key_parameters=None</em>, <em>cache_namespace=None</em>, <em>connection_id=None</em>, <em>connection_type=None</em>, <em>content_handling=None</em>, <em>credentials=None</em>, <em>http_method=None</em>, <em>integration_http_method=None</em>, <em>passthrough_behavior=None</em>, <em>request_parameters=None</em>, <em>request_parameters_in_json=None</em>, <em>request_templates=None</em>, <em>resource_id=None</em>, <em>rest_api=None</em>, <em>timeout_milliseconds=None</em>, <em>type=None</em>, <em>uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an HTTP Method Integration for an API Gateway Integration.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cache_key_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of cache key parameters for the integration.</li>
<li><strong>cache_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration’s cache namespace.</li>
<li><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the VpcLink used for the integration. <strong>Required</strong> if <cite>connection_type</cite> is <cite>VPC_LINK</cite></li>
<li><strong>connection_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration input’s [connectionType](<a class="reference external" href="https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/#connectionType">https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/#connectionType</a>). Valid values are <cite>INTERNET</cite> (default for connections through the public routable internet), and <cite>VPC_LINK</cite> (for private connections between API Gateway and a network load balancer in a VPC).</li>
<li><strong>content_handling</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how to handle request payload content type conversions. Supported values are <cite>CONVERT_TO_BINARY</cite> and <cite>CONVERT_TO_TEXT</cite>. If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the passthroughBehaviors is configured to support payload pass-through.</li>
<li><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The credentials required for the integration. For <cite>AWS</cite> integrations, 2 options are available. To specify an IAM Role for Amazon API Gateway to assume, use the role’s ARN. To require that the caller’s identity be passed through from the request, specify the string <cite>arn:aws:iam::*:user/*</cite>.</li>
<li><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP method (<cite>GET</cite>, <cite>POST</cite>, <cite>PUT</cite>, <cite>DELETE</cite>, <cite>HEAD</cite>, <cite>OPTION</cite>, <cite>ANY</cite>)
when calling the associated resource.</li>
<li><strong>integration_http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration HTTP method
(<cite>GET</cite>, <cite>POST</cite>, <cite>PUT</cite>, <cite>DELETE</cite>, <cite>HEAD</cite>, <cite>OPTION</cite>) specifying how API Gateway will interact with the back end.
<strong>Required</strong> if <cite>type</cite> is <cite>AWS</cite>, <cite>AWS_PROXY</cite>, <cite>HTTP</cite> or <cite>HTTP_PROXY</cite>.
Not all methods are compatible with all <cite>AWS</cite> integrations.
e.g. Lambda function [can only be invoked](<a class="reference external" href="https://github.com/awslabs/aws-apigateway-importer/issues/9#issuecomment-129651005">https://github.com/awslabs/aws-apigateway-importer/issues/9#issuecomment-129651005</a>) via <cite>POST</cite>.</li>
<li><strong>passthrough_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration passthrough behavior (<cite>WHEN_NO_MATCH</cite>, <cite>WHEN_NO_TEMPLATES</cite>, <cite>NEVER</cite>).  <strong>Required</strong> if <cite>request_templates</cite> is used.</li>
<li><strong>request_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of request query string parameters and headers that should be passed to the backend responder.
For example: <cite>request_parameters = { “integration.request.header.X-Some-Other-Header” = “method.request.header.X-Some-Header” }</cite></li>
<li><strong>request_parameters_in_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <strong>Deprecated</strong>, use <cite>request_parameters</cite> instead.</li>
<li><strong>request_templates</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of the integration’s request templates.</li>
<li><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API resource ID.</li>
<li><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API.</li>
<li><strong>timeout_milliseconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration input’s [type](<a class="reference external" href="https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/">https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/</a>). Valid values are <cite>HTTP</cite> (for HTTP backends), <cite>MOCK</cite> (not calling any real backend), <cite>AWS</cite> (for AWS services), <cite>AWS_PROXY</cite> (for Lambda proxy integration) and <cite>HTTP_PROXY</cite> (for HTTP proxy integration). An <cite>HTTP</cite> or <cite>HTTP_PROXY</cite> integration with a <cite>connection_type</cite> of <cite>VPC_LINK</cite> is referred to as a private integration and uses a VpcLink to connect API Gateway to a network load balancer of a VPC.</li>
<li><strong>uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The input’s URI (HTTP, AWS). <strong>Required</strong> if <cite>type</cite> is <cite>HTTP</cite> or <cite>AWS</cite>.
For HTTP integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification . For AWS integrations, the URI should be of the form <cite>arn:aws:apigateway:{region}:{subdomain.service|service}:{path|action}/{service_api}</cite>. <cite>region</cite>, <cite>subdomain</cite> and <cite>service</cite> are used to determine the right endpoint.
e.g. <cite>arn:aws:apigateway:eu-west-1:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-1:012345678901:function:my-func/invocations</cite></li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.cache_key_parameters">
<code class="descname">cache_key_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.cache_key_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of cache key parameters for the integration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.cache_namespace">
<code class="descname">cache_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.cache_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration’s cache namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.connection_id">
<code class="descname">connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the VpcLink used for the integration. <strong>Required</strong> if <cite>connection_type</cite> is <cite>VPC_LINK</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.connection_type">
<code class="descname">connection_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.connection_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration input’s [connectionType](<a class="reference external" href="https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/#connectionType">https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/#connectionType</a>). Valid values are <cite>INTERNET</cite> (default for connections through the public routable internet), and <cite>VPC_LINK</cite> (for private connections between API Gateway and a network load balancer in a VPC).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.content_handling">
<code class="descname">content_handling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.content_handling" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how to handle request payload content type conversions. Supported values are <cite>CONVERT_TO_BINARY</cite> and <cite>CONVERT_TO_TEXT</cite>. If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the passthroughBehaviors is configured to support payload pass-through.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.credentials">
<code class="descname">credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>The credentials required for the integration. For <cite>AWS</cite> integrations, 2 options are available. To specify an IAM Role for Amazon API Gateway to assume, use the role’s ARN. To require that the caller’s identity be passed through from the request, specify the string <cite>arn:aws:iam::*:user/*</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.http_method">
<code class="descname">http_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.http_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP method (<cite>GET</cite>, <cite>POST</cite>, <cite>PUT</cite>, <cite>DELETE</cite>, <cite>HEAD</cite>, <cite>OPTION</cite>, <cite>ANY</cite>)
when calling the associated resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.integration_http_method">
<code class="descname">integration_http_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.integration_http_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration HTTP method
(<cite>GET</cite>, <cite>POST</cite>, <cite>PUT</cite>, <cite>DELETE</cite>, <cite>HEAD</cite>, <cite>OPTION</cite>) specifying how API Gateway will interact with the back end.
<strong>Required</strong> if <cite>type</cite> is <cite>AWS</cite>, <cite>AWS_PROXY</cite>, <cite>HTTP</cite> or <cite>HTTP_PROXY</cite>.
Not all methods are compatible with all <cite>AWS</cite> integrations.
e.g. Lambda function [can only be invoked](<a class="reference external" href="https://github.com/awslabs/aws-apigateway-importer/issues/9#issuecomment-129651005">https://github.com/awslabs/aws-apigateway-importer/issues/9#issuecomment-129651005</a>) via <cite>POST</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.passthrough_behavior">
<code class="descname">passthrough_behavior</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.passthrough_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration passthrough behavior (<cite>WHEN_NO_MATCH</cite>, <cite>WHEN_NO_TEMPLATES</cite>, <cite>NEVER</cite>).  <strong>Required</strong> if <cite>request_templates</cite> is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.request_parameters">
<code class="descname">request_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.request_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of request query string parameters and headers that should be passed to the backend responder.
For example: <cite>request_parameters = { “integration.request.header.X-Some-Other-Header” = “method.request.header.X-Some-Header” }</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.request_parameters_in_json">
<code class="descname">request_parameters_in_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.request_parameters_in_json" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>Deprecated</strong>, use <cite>request_parameters</cite> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.request_templates">
<code class="descname">request_templates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.request_templates" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of the integration’s request templates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API resource ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.rest_api">
<code class="descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.timeout_milliseconds">
<code class="descname">timeout_milliseconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.timeout_milliseconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration input’s [type](<a class="reference external" href="https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/">https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/</a>). Valid values are <cite>HTTP</cite> (for HTTP backends), <cite>MOCK</cite> (not calling any real backend), <cite>AWS</cite> (for AWS services), <cite>AWS_PROXY</cite> (for Lambda proxy integration) and <cite>HTTP_PROXY</cite> (for HTTP proxy integration). An <cite>HTTP</cite> or <cite>HTTP_PROXY</cite> integration with a <cite>connection_type</cite> of <cite>VPC_LINK</cite> is referred to as a private integration and uses a VpcLink to connect API Gateway to a network load balancer of a VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.uri">
<code class="descname">uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The input’s URI (HTTP, AWS). <strong>Required</strong> if <cite>type</cite> is <cite>HTTP</cite> or <cite>AWS</cite>.
For HTTP integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification . For AWS integrations, the URI should be of the form <cite>arn:aws:apigateway:{region}:{subdomain.service|service}:{path|action}/{service_api}</cite>. <cite>region</cite>, <cite>subdomain</cite> and <cite>service</cite> are used to determine the right endpoint.
e.g. <cite>arn:aws:apigateway:eu-west-1:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-1:012345678901:function:my-func/invocations</cite></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Integration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Integration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.IntegrationResponse">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">IntegrationResponse</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>content_handling=None</em>, <em>http_method=None</em>, <em>resource_id=None</em>, <em>response_parameters=None</em>, <em>response_parameters_in_json=None</em>, <em>response_templates=None</em>, <em>rest_api=None</em>, <em>selection_pattern=None</em>, <em>status_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an HTTP Method Integration Response for an API Gateway Resource.</p>
<p>-&gt; <strong>Note:</strong> Depends on having <cite>aws_api_gateway_integration</cite> inside your rest api. To ensure this
you might need to add an explicit <cite>depends_on</cite> for clean runs.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>content_handling</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how to handle request payload content type conversions. Supported values are <cite>CONVERT_TO_BINARY</cite> and <cite>CONVERT_TO_TEXT</cite>. If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.</li>
<li><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP method (<cite>GET</cite>, <cite>POST</cite>, <cite>PUT</cite>, <cite>DELETE</cite>, <cite>HEAD</cite>, <cite>OPTIONS</cite>, <cite>ANY</cite>)</li>
<li><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API resource ID</li>
<li><strong>response_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of response parameters that can be read from the backend response.
For example: <cite>response_parameters = { “method.response.header.X-Some-Header” = “integration.response.header.X-Some-Other-Header” }</cite>,</li>
<li><strong>response_parameters_in_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <strong>Deprecated</strong>, use <cite>response_parameters</cite> instead.</li>
<li><strong>response_templates</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map specifying the templates used to transform the integration response body</li>
<li><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</li>
<li><strong>selection_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the regular expression pattern used to choose
an integration response based on the response from the backend. Setting this to <cite>-</cite> makes the integration the default one.
If the backend is an <cite>AWS</cite> Lambda function, the AWS Lambda function error header is matched.
For all other <cite>HTTP</cite> and <cite>AWS</cite> backends, the HTTP status code is matched.</li>
<li><strong>status_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP status code</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.content_handling">
<code class="descname">content_handling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.content_handling" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how to handle request payload content type conversions. Supported values are <cite>CONVERT_TO_BINARY</cite> and <cite>CONVERT_TO_TEXT</cite>. If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.http_method">
<code class="descname">http_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.http_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP method (<cite>GET</cite>, <cite>POST</cite>, <cite>PUT</cite>, <cite>DELETE</cite>, <cite>HEAD</cite>, <cite>OPTIONS</cite>, <cite>ANY</cite>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API resource ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.response_parameters">
<code class="descname">response_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.response_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of response parameters that can be read from the backend response.
For example: <cite>response_parameters = { “method.response.header.X-Some-Header” = “integration.response.header.X-Some-Other-Header” }</cite>,</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.response_parameters_in_json">
<code class="descname">response_parameters_in_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.response_parameters_in_json" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>Deprecated</strong>, use <cite>response_parameters</cite> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.response_templates">
<code class="descname">response_templates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.response_templates" title="Permalink to this definition">¶</a></dt>
<dd><p>A map specifying the templates used to transform the integration response body</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.rest_api">
<code class="descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.selection_pattern">
<code class="descname">selection_pattern</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.selection_pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the regular expression pattern used to choose
an integration response based on the response from the backend. Setting this to <cite>-</cite> makes the integration the default one.
If the backend is an <cite>AWS</cite> Lambda function, the AWS Lambda function error header is matched.
For all other <cite>HTTP</cite> and <cite>AWS</cite> backends, the HTTP status code is matched.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.status_code">
<code class="descname">status_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.status_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP status code</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.IntegrationResponse.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.IntegrationResponse.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Method">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">Method</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>api_key_required=None</em>, <em>authorization=None</em>, <em>authorization_scopes=None</em>, <em>authorizer_id=None</em>, <em>http_method=None</em>, <em>request_models=None</em>, <em>request_parameters=None</em>, <em>request_parameters_in_json=None</em>, <em>request_validator_id=None</em>, <em>resource_id=None</em>, <em>rest_api=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Method" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a HTTP Method for an API Gateway Resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_key_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify if the method requires an API key</li>
<li><strong>authorization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of authorization used for the method (<cite>NONE</cite>, <cite>CUSTOM</cite>, <cite>AWS_IAM</cite>, <cite>COGNITO_USER_POOLS</cite>)</li>
<li><strong>authorization_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The authorization scopes used when the authorization is <cite>COGNITO_USER_POOLS</cite></li>
<li><strong>authorizer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorizer id to be used when the authorization is <cite>CUSTOM</cite> or <cite>COGNITO_USER_POOLS</cite></li>
<li><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP Method (<cite>GET</cite>, <cite>POST</cite>, <cite>PUT</cite>, <cite>DELETE</cite>, <cite>HEAD</cite>, <cite>OPTIONS</cite>, <cite>ANY</cite>)</li>
<li><strong>request_models</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of the API models used for the request’s content type
where key is the content type (e.g. <cite>application/json</cite>)
and value is either <cite>Error</cite>, <cite>Empty</cite> (built-in models) or <cite>aws_api_gateway_model</cite>’s <cite>name</cite>.</li>
<li><strong>request_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of request query string parameters and headers that should be passed to the integration.
For example:
<code class="docutils literal notranslate"><span class="pre">`hcl</span>
<span class="pre">request_parameters</span> <span class="pre">=</span> <span class="pre">{</span>
<span class="pre">&quot;method.request.header.X-Some-Header&quot;</span>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; <span class="pre">=</span> <span class="pre">true</span>
<span class="pre">&quot;method.request.querystring.some-query-param&quot;</span> <span class="pre">=</span> <span class="pre">true</span>
<span class="pre">}</span>
<span class="pre">`</span></code>
would define that the header <cite>X-Some-Header</cite> and the query string <cite>some-query-param</cite> must be provided on the request, or</li>
<li><strong>request_parameters_in_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <strong>Deprecated</strong>, use <cite>request_parameters</cite> instead.</li>
<li><strong>request_validator_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a <cite>aws_api_gateway_request_validator</cite></li>
<li><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API resource ID</li>
<li><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.api_key_required">
<code class="descname">api_key_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.api_key_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify if the method requires an API key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.authorization">
<code class="descname">authorization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.authorization" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of authorization used for the method (<cite>NONE</cite>, <cite>CUSTOM</cite>, <cite>AWS_IAM</cite>, <cite>COGNITO_USER_POOLS</cite>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.authorization_scopes">
<code class="descname">authorization_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.authorization_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorization scopes used when the authorization is <cite>COGNITO_USER_POOLS</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.authorizer_id">
<code class="descname">authorizer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.authorizer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorizer id to be used when the authorization is <cite>CUSTOM</cite> or <cite>COGNITO_USER_POOLS</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.http_method">
<code class="descname">http_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.http_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP Method (<cite>GET</cite>, <cite>POST</cite>, <cite>PUT</cite>, <cite>DELETE</cite>, <cite>HEAD</cite>, <cite>OPTIONS</cite>, <cite>ANY</cite>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.request_models">
<code class="descname">request_models</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.request_models" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of the API models used for the request’s content type
where key is the content type (e.g. <cite>application/json</cite>)
and value is either <cite>Error</cite>, <cite>Empty</cite> (built-in models) or <cite>aws_api_gateway_model</cite>’s <cite>name</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.request_parameters">
<code class="descname">request_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.request_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of request query string parameters and headers that should be passed to the integration.
For example:
<code class="docutils literal notranslate"><span class="pre">`hcl</span>
<span class="pre">request_parameters</span> <span class="pre">=</span> <span class="pre">{</span>
<span class="pre">&quot;method.request.header.X-Some-Header&quot;</span>&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; <span class="pre">=</span> <span class="pre">true</span>
<span class="pre">&quot;method.request.querystring.some-query-param&quot;</span> <span class="pre">=</span> <span class="pre">true</span>
<span class="pre">}</span>
<span class="pre">`</span></code>
would define that the header <cite>X-Some-Header</cite> and the query string <cite>some-query-param</cite> must be provided on the request, or</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.request_parameters_in_json">
<code class="descname">request_parameters_in_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.request_parameters_in_json" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>Deprecated</strong>, use <cite>request_parameters</cite> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.request_validator_id">
<code class="descname">request_validator_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.request_validator_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a <cite>aws_api_gateway_request_validator</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API resource ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.rest_api">
<code class="descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Method.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Method.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Method.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Method.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.MethodResponse">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">MethodResponse</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>http_method=None</em>, <em>resource_id=None</em>, <em>response_models=None</em>, <em>response_parameters=None</em>, <em>response_parameters_in_json=None</em>, <em>rest_api=None</em>, <em>status_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an HTTP Method Response for an API Gateway Resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP Method (<cite>GET</cite>, <cite>POST</cite>, <cite>PUT</cite>, <cite>DELETE</cite>, <cite>HEAD</cite>, <cite>OPTIONS</cite>, <cite>ANY</cite>)</li>
<li><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API resource ID</li>
<li><strong>response_models</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of the API models used for the response’s content type</li>
<li><strong>response_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of response parameters that can be sent to the caller.
For example: <cite>response_parameters = { “method.response.header.X-Some-Header” = true }</cite>
would define that the header <cite>X-Some-Header</cite> can be provided on the response.</li>
<li><strong>response_parameters_in_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <strong>Deprecated</strong>, use <cite>response_parameters</cite> instead.</li>
<li><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</li>
<li><strong>status_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP status code</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodResponse.http_method">
<code class="descname">http_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.http_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP Method (<cite>GET</cite>, <cite>POST</cite>, <cite>PUT</cite>, <cite>DELETE</cite>, <cite>HEAD</cite>, <cite>OPTIONS</cite>, <cite>ANY</cite>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodResponse.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API resource ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodResponse.response_models">
<code class="descname">response_models</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.response_models" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of the API models used for the response’s content type</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodResponse.response_parameters">
<code class="descname">response_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.response_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of response parameters that can be sent to the caller.
For example: <cite>response_parameters = { “method.response.header.X-Some-Header” = true }</cite>
would define that the header <cite>X-Some-Header</cite> can be provided on the response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodResponse.response_parameters_in_json">
<code class="descname">response_parameters_in_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.response_parameters_in_json" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>Deprecated</strong>, use <cite>response_parameters</cite> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodResponse.rest_api">
<code class="descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodResponse.status_code">
<code class="descname">status_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.status_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP status code</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.MethodResponse.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.MethodResponse.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.MethodSettings">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">MethodSettings</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>method_path=None</em>, <em>rest_api=None</em>, <em>settings=None</em>, <em>stage_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Method Settings, e.g. logging or monitoring.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>method_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Method path defined as <cite>{resource_path}/{http_method}</cite> for an individual method override, or <cite>*/*</cite> for overriding all methods in the stage.</li>
<li><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the REST API</li>
<li><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings block, see below.</li>
<li><strong>stage_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stage</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodSettings.method_path">
<code class="descname">method_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings.method_path" title="Permalink to this definition">¶</a></dt>
<dd><p>Method path defined as <cite>{resource_path}/{http_method}</cite> for an individual method override, or <cite>*/*</cite> for overriding all methods in the stage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodSettings.rest_api">
<code class="descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodSettings.settings">
<code class="descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The settings block, see below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodSettings.stage_name">
<code class="descname">stage_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings.stage_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the stage</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.MethodSettings.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.MethodSettings.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Model">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">Model</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>content_type=None</em>, <em>description=None</em>, <em>name=None</em>, <em>rest_api=None</em>, <em>schema=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Model" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Model for a API Gateway.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content type of the model</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the model</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the model</li>
<li><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</li>
<li><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The schema of the model in a JSON form</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Model.content_type">
<code class="descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Model.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The content type of the model</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Model.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Model.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the model</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Model.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Model.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the model</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Model.rest_api">
<code class="descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Model.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Model.schema">
<code class="descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Model.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The schema of the model in a JSON form</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Model.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Model.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Model.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Model.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.RequestValidator">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">RequestValidator</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>name=None</em>, <em>rest_api=None</em>, <em>validate_request_body=None</em>, <em>validate_request_parameters=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Gateway Request Validator.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the request validator</li>
<li><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated Rest API</li>
<li><strong>validate_request_body</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether to validate request body. Defaults to <cite>false</cite>.</li>
<li><strong>validate_request_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether to validate request parameters. Defaults to <cite>false</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.RequestValidator.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the request validator</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RequestValidator.rest_api">
<code class="descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated Rest API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RequestValidator.validate_request_body">
<code class="descname">validate_request_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator.validate_request_body" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether to validate request body. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RequestValidator.validate_request_parameters">
<code class="descname">validate_request_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator.validate_request_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether to validate request parameters. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.RequestValidator.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.RequestValidator.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Resource">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">Resource</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>parent_id=None</em>, <em>path_part=None</em>, <em>rest_api=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Resource" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the parent API resource</li>
<li><strong>path_part</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The last path segment of this API resource.</li>
<li><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Resource.parent_id">
<code class="descname">parent_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Resource.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the parent API resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Resource.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Resource.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The complete path for this API resource, including all parent paths.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Resource.path_part">
<code class="descname">path_part</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Resource.path_part" title="Permalink to this definition">¶</a></dt>
<dd><p>The last path segment of this API resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Resource.rest_api">
<code class="descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Resource.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Resource.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Resource.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Resource.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Resource.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Response">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">Response</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>response_parameters=None</em>, <em>response_templates=None</em>, <em>response_type=None</em>, <em>rest_api_id=None</em>, <em>status_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Response" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Gateway Response for a REST API Gateway.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>response_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map specifying the templates used to transform the response body.</li>
<li><strong>response_templates</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map specifying the parameters (paths, query strings and headers) of the Gateway Response.</li>
<li><strong>response_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The response type of the associated GatewayResponse.</li>
<li><strong>rest_api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The string identifier of the associated REST API.</li>
<li><strong>status_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP status code of the Gateway Response.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Response.response_parameters">
<code class="descname">response_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Response.response_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map specifying the templates used to transform the response body.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Response.response_templates">
<code class="descname">response_templates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Response.response_templates" title="Permalink to this definition">¶</a></dt>
<dd><p>A map specifying the parameters (paths, query strings and headers) of the Gateway Response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Response.response_type">
<code class="descname">response_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Response.response_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The response type of the associated GatewayResponse.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Response.rest_api_id">
<code class="descname">rest_api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Response.rest_api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The string identifier of the associated REST API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Response.status_code">
<code class="descname">status_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Response.status_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP status code of the Gateway Response.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Response.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Response.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Response.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Response.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.RestApi">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">RestApi</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>api_key_source=None</em>, <em>binary_media_types=None</em>, <em>body=None</em>, <em>description=None</em>, <em>endpoint_configuration=None</em>, <em>minimum_compression_size=None</em>, <em>name=None</em>, <em>policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.RestApi" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway REST API.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_key_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source of the API key for requests. Valid values are HEADER (default) and AUTHORIZER.</li>
<li><strong>binary_media_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.</li>
<li><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the REST API</li>
<li><strong>endpoint_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument defining API endpoint configuration including endpoint type. Defined below.</li>
<li><strong>minimum_compression_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the REST API</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON formatted policy document that controls access to the API Gateway. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html</a>)</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.api_key_source">
<code class="descname">api_key_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.api_key_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The source of the API key for requests. Valid values are HEADER (default) and AUTHORIZER.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.binary_media_types">
<code class="descname">binary_media_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.binary_media_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.body">
<code class="descname">body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.body" title="Permalink to this definition">¶</a></dt>
<dd><p>An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.created_date">
<code class="descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.endpoint_configuration">
<code class="descname">endpoint_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.endpoint_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument defining API endpoint configuration including endpoint type. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.execution_arn">
<code class="descname">execution_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.execution_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The execution ARN part to be used in [<cite>lambda_permission</cite>](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)’s</a> <cite>source_arn</cite>
when allowing API Gateway to invoke a Lambda function,
e.g. <cite>arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j</cite>, which can be concatenated with allowed stage, method and resource path.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.minimum_compression_size">
<code class="descname">minimum_compression_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.minimum_compression_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON formatted policy document that controls access to the API Gateway. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html</a>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.root_resource_id">
<code class="descname">root_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.root_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource ID of the REST API’s root</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.RestApi.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.RestApi.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Stage">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">Stage</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>access_log_settings=None</em>, <em>cache_cluster_enabled=None</em>, <em>cache_cluster_size=None</em>, <em>client_certificate_id=None</em>, <em>deployment=None</em>, <em>description=None</em>, <em>documentation_version=None</em>, <em>rest_api=None</em>, <em>stage_name=None</em>, <em>tags=None</em>, <em>variables=None</em>, <em>xray_tracing_enabled=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Stage" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Stage.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>access_log_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enables access logs for the API stage. Detailed below.</li>
<li><strong>cache_cluster_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether a cache cluster is enabled for the stage</li>
<li><strong>cache_cluster_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The size of the cache cluster for the stage, if enabled.
Allowed values include <cite>0.5</cite>, <cite>1.6</cite>, <cite>6.1</cite>, <cite>13.5</cite>, <cite>28.4</cite>, <cite>58.2</cite>, <cite>118</cite> and <cite>237</cite>.</li>
<li><strong>client_certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of a client certificate for the stage.</li>
<li><strong>deployment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the deployment that the stage points to</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the stage</li>
<li><strong>documentation_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the associated API documentation</li>
<li><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</li>
<li><strong>stage_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stage</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map that defines the stage variables</li>
<li><strong>xray_tracing_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether active tracing with X-ray is enabled. Defaults to <cite>false</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.access_log_settings">
<code class="descname">access_log_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.access_log_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables access logs for the API stage. Detailed below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.cache_cluster_enabled">
<code class="descname">cache_cluster_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.cache_cluster_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether a cache cluster is enabled for the stage</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.cache_cluster_size">
<code class="descname">cache_cluster_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.cache_cluster_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the cache cluster for the stage, if enabled.
Allowed values include <cite>0.5</cite>, <cite>1.6</cite>, <cite>6.1</cite>, <cite>13.5</cite>, <cite>28.4</cite>, <cite>58.2</cite>, <cite>118</cite> and <cite>237</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.client_certificate_id">
<code class="descname">client_certificate_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.client_certificate_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of a client certificate for the stage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.deployment">
<code class="descname">deployment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the deployment that the stage points to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the stage</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.documentation_version">
<code class="descname">documentation_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.documentation_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the associated API documentation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.execution_arn">
<code class="descname">execution_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.execution_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The execution ARN to be used in [<cite>lambda_permission</cite>](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)'s">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html)’s</a> <cite>source_arn</cite>
when allowing API Gateway to invoke a Lambda function,
e.g. <cite>arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.invoke_url">
<code class="descname">invoke_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.invoke_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to invoke the API pointing to the stage,
e.g. <cite>https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.rest_api">
<code class="descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.stage_name">
<code class="descname">stage_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.stage_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the stage</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.variables">
<code class="descname">variables</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.variables" title="Permalink to this definition">¶</a></dt>
<dd><p>A map that defines the stage variables</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.xray_tracing_enabled">
<code class="descname">xray_tracing_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.xray_tracing_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether active tracing with X-ray is enabled. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Stage.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Stage.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Stage.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Stage.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.UsagePlan">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">UsagePlan</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>api_stages=None</em>, <em>description=None</em>, <em>name=None</em>, <em>product_code=None</em>, <em>quota_settings=None</em>, <em>throttle_settings=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Usage Plan.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>api_stages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The associated API stages of the usage plan.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of a usage plan.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the usage plan.</li>
<li><strong>product_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.</li>
<li><strong>quota_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The quota settings of the usage plan.</li>
<li><strong>throttle_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The throttling limits of the usage plan.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlan.api_stages">
<code class="descname">api_stages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.api_stages" title="Permalink to this definition">¶</a></dt>
<dd><p>The associated API stages of the usage plan.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlan.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of a usage plan.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlan.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the usage plan.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlan.product_code">
<code class="descname">product_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.product_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlan.quota_settings">
<code class="descname">quota_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.quota_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The quota settings of the usage plan.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlan.throttle_settings">
<code class="descname">throttle_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.throttle_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The throttling limits of the usage plan.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.UsagePlan.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.UsagePlan.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.UsagePlanKey">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">UsagePlanKey</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>key_id=None</em>, <em>key_type=None</em>, <em>usage_plan_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Usage Plan Key.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the API key resource.</li>
<li><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the API key resource. Currently, the valid key type is API_KEY.</li>
<li><strong>usage_plan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of the usage plan resource representing to associate the key to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlanKey.key_id">
<code class="descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the API key resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlanKey.key_type">
<code class="descname">key_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the API key resource. Currently, the valid key type is API_KEY.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlanKey.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a usage plan key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlanKey.usage_plan_id">
<code class="descname">usage_plan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.usage_plan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of the usage plan resource representing to associate the key to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlanKey.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of a usage plan key.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.UsagePlanKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.UsagePlanKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.VpcLink">
<em class="property">class </em><code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">VpcLink</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>name=None</em>, <em>target_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.VpcLink" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway VPC Link.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the VPC link.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name used to label and identify the VPC link.</li>
<li><strong>target_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.VpcLink.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.VpcLink.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the VPC link.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.VpcLink.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.VpcLink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name used to label and identify the VPC link.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.VpcLink.target_arn">
<code class="descname">target_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.VpcLink.target_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.VpcLink.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.VpcLink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.VpcLink.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.VpcLink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_aws.apigateway.get_key">
<code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">get_key</code><span class="sig-paren">(</span><em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.get_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the name and value of a pre-existing API Key, for
example to supply credentials for a dependency microservice.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.apigateway.get_resource">
<code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">get_resource</code><span class="sig-paren">(</span><em>path=None</em>, <em>rest_api_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.get_resource" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the id of a Resource in API Gateway. 
To fetch the Resource, you must provide the REST API id as well as the full path.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.apigateway.get_rest_api">
<code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">get_rest_api</code><span class="sig-paren">(</span><em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.get_rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the id and root_resource_id of a REST API in
API Gateway. To fetch the REST API you must provide a name to match against. 
As there is no unique name constraint on REST APIs this data source will 
error if there is more than one match.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.apigateway.get_vpc_link">
<code class="descclassname">pulumi_aws.apigateway.</code><code class="descname">get_vpc_link</code><span class="sig-paren">(</span><em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.get_vpc_link" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the id of a VPC Link in
API Gateway. To fetch the VPC Link you must provide a name to match against. 
As there is no unique name constraint on API Gateway VPC Links this data source will 
error if there is more than one match.</p>
</dd></dl>

</div>
