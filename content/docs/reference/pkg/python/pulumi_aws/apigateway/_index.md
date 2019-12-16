---
title: Module apigateway
title_tag: Module apigateway | Package pulumi_aws | Python SDK
linktitle: apigateway
notitle: true
---

<div class="section" id="apigateway">
<h1>apigateway<a class="headerlink" href="#apigateway" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.apigateway"></span><dl class="class">
<dt id="pulumi_aws.apigateway.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloudwatch_role_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a settings of an API Gateway Account. Settings is applied region-wide per <code class="docutils literal notranslate"><span class="pre">provider</span></code> block.</p>
<blockquote>
<div><p><strong>Note:</strong> As there is no API method for deleting account settings or resetting it to defaults, destroying this resource will keep your account settings intact</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloudwatch_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role for CloudWatch (to allow logging &amp; monitoring).
See more <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console">in AWS Docs</a>.
Logging &amp; monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_account.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_account.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Account.cloudwatch_role_arn">
<code class="sig-name descname">cloudwatch_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Account.cloudwatch_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM role for CloudWatch (to allow logging &amp; monitoring).
See more <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console">in AWS Docs</a>.
Logging &amp; monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Account.throttle_settings">
<code class="sig-name descname">throttle_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Account.throttle_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Account-Level throttle settings. See exported fields below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">burstLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The absolute maximum number of times API Gateway allows the API to be called per second (RPS).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rateLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of times API Gateway allows the API to be called per second on average (RPS).</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloudwatch_role_arn=None</em>, <em class="sig-param">throttle_settings=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloudwatch_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ARN of an IAM role for CloudWatch (to allow logging &amp; monitoring).
See more <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-stage-settings.html#how-to-stage-settings-console">in AWS Docs</a>.
Logging &amp; monitoring can be enabled/disabled and otherwise tuned on the API Gateway Stage level.</p>
</p></li>
<li><p><strong>throttle_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Account-Level throttle settings. See exported fields below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>throttle_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">burstLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The absolute maximum number of times API Gateway allows the API to be called per second (RPS).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rateLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of times API Gateway allows the API to be called per second on average (RPS).</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_account.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_account.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.ApiKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">ApiKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway API Key.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Since the API Gateway usage plans feature was launched on August 11, 2016, usage plans are now <strong>required</strong> to associate an API key with an API stage.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API key description. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the API key can be used by callers. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API key</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the API key. If not specified, it will be automatically generated by AWS on creation.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_api_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_api_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.created_date">
<code class="sig-name descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the API key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The API key description. Defaults to “Managed by Pulumi”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the API key can be used by callers. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.last_updated_date">
<code class="sig-name descname">last_updated_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.last_updated_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The last update date of the API key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ApiKey.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the API key. If not specified, it will be automatically generated by AWS on creation.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.ApiKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">created_date=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">last_updated_date=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApiKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN)</p></li>
<li><p><strong>created_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creation date of the API key</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API key description. Defaults to “Managed by Pulumi”.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the API key can be used by callers. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>last_updated_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The last update date of the API key</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API key</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the API key. If not specified, it will be automatically generated by AWS on creation.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_api_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_api_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.ApiKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.ApiKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.ApiKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Authorizer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">Authorizer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">authorizer_credentials=None</em>, <em class="sig-param">authorizer_result_ttl_in_seconds=None</em>, <em class="sig-param">authorizer_uri=None</em>, <em class="sig-param">identity_source=None</em>, <em class="sig-param">identity_validation_expression=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">provider_arns=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Authorizer.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorizer_credentials</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.</p></li>
<li><p><strong>authorizer_result_ttl_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TTL of cached authorizer results in seconds.
Defaults to <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p></li>
<li><p><strong>authorizer_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorizer’s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of <code class="docutils literal notranslate"><span class="pre">arn:aws:apigateway:{region}:lambda:path/{service_api}</span></code>,
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations</span></code></p></li>
<li><p><strong>identity_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source of the identity in an incoming request.
Defaults to <code class="docutils literal notranslate"><span class="pre">method.request.header.Authorization</span></code>. For <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. <code class="docutils literal notranslate"><span class="pre">&quot;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&quot;</span></code></p></li>
<li><p><strong>identity_validation_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A validation expression for the incoming identity.
For <code class="docutils literal notranslate"><span class="pre">TOKEN</span></code> type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn’t match,
the client receives a 401 Unauthorized response.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the authorizer</p></li>
<li><p><strong>provider_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the Amazon Cognito user pool ARNs.
Each element is of this format: <code class="docutils literal notranslate"><span class="pre">arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}</span></code>.</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the authorizer. Possible values are <code class="docutils literal notranslate"><span class="pre">TOKEN</span></code> for a Lambda function using a single authorization token submitted in a custom header, <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> for a Lambda function using incoming request parameters, or <code class="docutils literal notranslate"><span class="pre">COGNITO_USER_POOLS</span></code> for using an Amazon Cognito user pool.
Defaults to <code class="docutils literal notranslate"><span class="pre">TOKEN</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_authorizer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_authorizer.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.authorizer_credentials">
<code class="sig-name descname">authorizer_credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.authorizer_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.authorizer_result_ttl_in_seconds">
<code class="sig-name descname">authorizer_result_ttl_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.authorizer_result_ttl_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL of cached authorizer results in seconds.
Defaults to <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.authorizer_uri">
<code class="sig-name descname">authorizer_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.authorizer_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorizer’s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of <code class="docutils literal notranslate"><span class="pre">arn:aws:apigateway:{region}:lambda:path/{service_api}</span></code>,
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.identity_source">
<code class="sig-name descname">identity_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.identity_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The source of the identity in an incoming request.
Defaults to <code class="docutils literal notranslate"><span class="pre">method.request.header.Authorization</span></code>. For <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. <code class="docutils literal notranslate"><span class="pre">&quot;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&quot;</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.identity_validation_expression">
<code class="sig-name descname">identity_validation_expression</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.identity_validation_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>A validation expression for the incoming identity.
For <code class="docutils literal notranslate"><span class="pre">TOKEN</span></code> type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn’t match,
the client receives a 401 Unauthorized response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the authorizer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.provider_arns">
<code class="sig-name descname">provider_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.provider_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Amazon Cognito user pool ARNs.
Each element is of this format: <code class="docutils literal notranslate"><span class="pre">arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.rest_api">
<code class="sig-name descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Authorizer.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the authorizer. Possible values are <code class="docutils literal notranslate"><span class="pre">TOKEN</span></code> for a Lambda function using a single authorization token submitted in a custom header, <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> for a Lambda function using incoming request parameters, or <code class="docutils literal notranslate"><span class="pre">COGNITO_USER_POOLS</span></code> for using an Amazon Cognito user pool.
Defaults to <code class="docutils literal notranslate"><span class="pre">TOKEN</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Authorizer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">authorizer_credentials=None</em>, <em class="sig-param">authorizer_result_ttl_in_seconds=None</em>, <em class="sig-param">authorizer_uri=None</em>, <em class="sig-param">identity_source=None</em>, <em class="sig-param">identity_validation_expression=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">provider_arns=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Authorizer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorizer_credentials</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The credentials required for the authorizer.
To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.</p></li>
<li><p><strong>authorizer_result_ttl_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TTL of cached authorizer results in seconds.
Defaults to <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p></li>
<li><p><strong>authorizer_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorizer’s Uniform Resource Identifier (URI).
This must be a well-formed Lambda function URI in the form of <code class="docutils literal notranslate"><span class="pre">arn:aws:apigateway:{region}:lambda:path/{service_api}</span></code>,
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations</span></code></p></li>
<li><p><strong>identity_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source of the identity in an incoming request.
Defaults to <code class="docutils literal notranslate"><span class="pre">method.request.header.Authorization</span></code>. For <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. <code class="docutils literal notranslate"><span class="pre">&quot;method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName&quot;</span></code></p></li>
<li><p><strong>identity_validation_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A validation expression for the incoming identity.
For <code class="docutils literal notranslate"><span class="pre">TOKEN</span></code> type, this value should be a regular expression. The incoming token from the client is matched
against this expression, and will proceed if the token matches. If the token doesn’t match,
the client receives a 401 Unauthorized response.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the authorizer</p></li>
<li><p><strong>provider_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the Amazon Cognito user pool ARNs.
Each element is of this format: <code class="docutils literal notranslate"><span class="pre">arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}</span></code>.</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the authorizer. Possible values are <code class="docutils literal notranslate"><span class="pre">TOKEN</span></code> for a Lambda function using a single authorization token submitted in a custom header, <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> for a Lambda function using incoming request parameters, or <code class="docutils literal notranslate"><span class="pre">COGNITO_USER_POOLS</span></code> for using an Amazon Cognito user pool.
Defaults to <code class="docutils literal notranslate"><span class="pre">TOKEN</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_authorizer.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_authorizer.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Authorizer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Authorizer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Authorizer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.AwaitableGetKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">AwaitableGetKeyResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.AwaitableGetKeyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.apigateway.AwaitableGetResourceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">AwaitableGetResourceResult</code><span class="sig-paren">(</span><em class="sig-param">parent_id=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">path_part=None</em>, <em class="sig-param">rest_api_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.AwaitableGetResourceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.apigateway.AwaitableGetRestApiResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">AwaitableGetRestApiResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">root_resource_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.AwaitableGetRestApiResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.apigateway.AwaitableGetVpcLinkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">AwaitableGetVpcLinkResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.AwaitableGetVpcLinkResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.apigateway.BasePathMapping">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">BasePathMapping</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">base_path=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">stage_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping" title="Permalink to this definition">¶</a></dt>
<dd><p>Connects a custom domain name registered via <code class="docutils literal notranslate"><span class="pre">apigateway.DomainName</span></code>
with a deployed API so that its methods can be called via the
custom domain name.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the API to connect.</p></li>
<li><p><strong>base_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The already-registered domain name to connect the API to.</p></li>
<li><p><strong>stage_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_base_path_mapping.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_base_path_mapping.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.BasePathMapping.rest_api">
<code class="sig-name descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the API to connect.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.BasePathMapping.base_path">
<code class="sig-name descname">base_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping.base_path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.BasePathMapping.domain_name">
<code class="sig-name descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The already-registered domain name to connect the API to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.BasePathMapping.stage_name">
<code class="sig-name descname">stage_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping.stage_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.BasePathMapping.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">base_path=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">stage_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BasePathMapping resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the API to connect.</p></li>
<li><p><strong>base_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path segment that must be prepended to the path when accessing the API via this mapping. If omitted, the API is exposed at the root of the given domain.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The already-registered domain name to connect the API to.</p></li>
<li><p><strong>stage_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a specific deployment stage to expose at the given path. If omitted, callers may select any stage by including its name as a path element after the base path.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_base_path_mapping.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_base_path_mapping.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.BasePathMapping.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.BasePathMapping.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.BasePathMapping.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.ClientCertificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">ClientCertificate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Client Certificate.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the client certificate.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_client_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_client_certificate.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.ClientCertificate.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ClientCertificate.created_date">
<code class="sig-name descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date when the client certificate was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ClientCertificate.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the client certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ClientCertificate.expiration_date">
<code class="sig-name descname">expiration_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.expiration_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date when the client certificate will expire.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ClientCertificate.pem_encoded_certificate">
<code class="sig-name descname">pem_encoded_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.pem_encoded_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The PEM-encoded public key of the client certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.ClientCertificate.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.ClientCertificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">created_date=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expiration_date=None</em>, <em class="sig-param">pem_encoded_certificate=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ClientCertificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN)</p></li>
<li><p><strong>created_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date when the client certificate was created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the client certificate.</p></li>
<li><p><strong>expiration_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date when the client certificate will expire.</p></li>
<li><p><strong>pem_encoded_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The PEM-encoded public key of the client certificate.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_client_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_client_certificate.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.ClientCertificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.ClientCertificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.ClientCertificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Deployment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">Deployment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">stage_description=None</em>, <em class="sig-param">stage_name=None</em>, <em class="sig-param">variables=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Deployment.</p>
<blockquote>
<div><p><strong>Note:</strong> Depends on having <code class="docutils literal notranslate"><span class="pre">apigateway.Integration</span></code> inside your rest api (which in turn depends on <code class="docutils literal notranslate"><span class="pre">apigateway.Method</span></code>). To avoid race conditions
you might need to add an explicit <code class="docutils literal notranslate"><span class="pre">depends_on</span> <span class="pre">=</span> <span class="pre">[&quot;aws_api_gateway_integration.name&quot;]</span></code>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the deployment</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
<li><p><strong>stage_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the stage</p></li>
<li><p><strong>stage_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stage. If the specified stage already exists, it will be updated to point to the new deployment. If the stage does not exist, a new one will be created and point to this deployment.</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map that defines variables for the stage</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_deployment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_deployment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.created_date">
<code class="sig-name descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the deployment</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the deployment</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.execution_arn">
<code class="sig-name descname">execution_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.execution_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The execution ARN to be used in <cite>``lambda_permission`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">source_arn</span></code>
when allowing API Gateway to invoke a Lambda function,
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.invoke_url">
<code class="sig-name descname">invoke_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.invoke_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to invoke the API pointing to the stage,
e.g. <code class="docutils literal notranslate"><span class="pre">https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.rest_api">
<code class="sig-name descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.stage_description">
<code class="sig-name descname">stage_description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.stage_description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the stage</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.stage_name">
<code class="sig-name descname">stage_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.stage_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the stage. If the specified stage already exists, it will be updated to point to the new deployment. If the stage does not exist, a new one will be created and point to this deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Deployment.variables">
<code class="sig-name descname">variables</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.variables" title="Permalink to this definition">¶</a></dt>
<dd><p>A map that defines variables for the stage</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Deployment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">created_date=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">execution_arn=None</em>, <em class="sig-param">invoke_url=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">stage_description=None</em>, <em class="sig-param">stage_name=None</em>, <em class="sig-param">variables=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Deployment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creation date of the deployment</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the deployment</p></li>
<li><p><strong>execution_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The execution ARN to be used in <cite>``lambda_permission`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">source_arn</span></code>
when allowing API Gateway to invoke a Lambda function,
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod</span></code></p></li>
<li><p><strong>invoke_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to invoke the API pointing to the stage,
e.g. <code class="docutils literal notranslate"><span class="pre">https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod</span></code></p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
<li><p><strong>stage_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the stage</p></li>
<li><p><strong>stage_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stage. If the specified stage already exists, it will be updated to point to the new deployment. If the stage does not exist, a new one will be created and point to this deployment.</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map that defines variables for the stage</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_deployment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_deployment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Deployment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Deployment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Deployment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.DocumentationPart">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">DocumentationPart</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">properties=None</em>, <em class="sig-param">rest_api_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationPart" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a settings of an API Gateway Documentation Part.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The location of the targeted API entity of the to-be-created documentation part. See below.</p></li>
<li><p><strong>properties</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., “{ “description”: “The API does …” }”. Only Swagger-compliant key-value pairs can be exported and, hence, published.</p></li>
<li><p><strong>rest_api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated Rest API</p></li>
</ul>
</dd>
</dl>
<p>The <strong>location</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP verb of a method. The default value is <code class="docutils literal notranslate"><span class="pre">*</span></code> for any method.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the targeted API entity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL path of the target. The default value is <code class="docutils literal notranslate"><span class="pre">/</span></code> for the root resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP status code of a response. The default value is <code class="docutils literal notranslate"><span class="pre">*</span></code> for any status code.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of API entity to which the documentation content applies. e.g. <code class="docutils literal notranslate"><span class="pre">API</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">REQUEST_BODY</span></code></p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_documentation_part.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_documentation_part.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.DocumentationPart.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationPart.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the targeted API entity of the to-be-created documentation part. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The HTTP verb of a method. The default value is <code class="docutils literal notranslate"><span class="pre">*</span></code> for any method.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the targeted API entity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL path of the target. The default value is <code class="docutils literal notranslate"><span class="pre">/</span></code> for the root resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The HTTP status code of a response. The default value is <code class="docutils literal notranslate"><span class="pre">*</span></code> for any status code.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of API entity to which the documentation content applies. e.g. <code class="docutils literal notranslate"><span class="pre">API</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">REQUEST_BODY</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DocumentationPart.properties">
<code class="sig-name descname">properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationPart.properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., “{ “description”: “The API does …” }”. Only Swagger-compliant key-value pairs can be exported and, hence, published.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DocumentationPart.rest_api_id">
<code class="sig-name descname">rest_api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationPart.rest_api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated Rest API</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.DocumentationPart.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">properties=None</em>, <em class="sig-param">rest_api_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationPart.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DocumentationPart resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The location of the targeted API entity of the to-be-created documentation part. See below.</p></li>
<li><p><strong>properties</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., “{ “description”: “The API does …” }”. Only Swagger-compliant key-value pairs can be exported and, hence, published.</p></li>
<li><p><strong>rest_api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated Rest API</p></li>
</ul>
</dd>
</dl>
<p>The <strong>location</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP verb of a method. The default value is <code class="docutils literal notranslate"><span class="pre">*</span></code> for any method.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the targeted API entity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL path of the target. The default value is <code class="docutils literal notranslate"><span class="pre">/</span></code> for the root resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status_code</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTP status code of a response. The default value is <code class="docutils literal notranslate"><span class="pre">*</span></code> for any status code.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of API entity to which the documentation content applies. e.g. <code class="docutils literal notranslate"><span class="pre">API</span></code>, <code class="docutils literal notranslate"><span class="pre">METHOD</span></code> or <code class="docutils literal notranslate"><span class="pre">REQUEST_BODY</span></code></p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_documentation_part.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_documentation_part.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.DocumentationPart.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationPart.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.DocumentationPart.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationPart.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.DocumentationVersion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">DocumentationVersion</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">rest_api_id=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage an API Gateway Documentation Version.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the API documentation version.</p></li>
<li><p><strong>rest_api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated Rest API</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version identifier of the API documentation snapshot.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_documentation_version.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_documentation_version.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.DocumentationVersion.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationVersion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the API documentation version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DocumentationVersion.rest_api_id">
<code class="sig-name descname">rest_api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationVersion.rest_api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated Rest API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DocumentationVersion.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationVersion.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version identifier of the API documentation snapshot.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.DocumentationVersion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">rest_api_id=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationVersion.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DocumentationVersion resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the API documentation version.</p></li>
<li><p><strong>rest_api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated Rest API</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version identifier of the API documentation snapshot.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_documentation_version.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_documentation_version.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.DocumentationVersion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationVersion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.DocumentationVersion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DocumentationVersion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.DomainName">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">DomainName</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">certificate_arn=None</em>, <em class="sig-param">certificate_body=None</em>, <em class="sig-param">certificate_chain=None</em>, <em class="sig-param">certificate_name=None</em>, <em class="sig-param">certificate_private_key=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">endpoint_configuration=None</em>, <em class="sig-param">regional_certificate_arn=None</em>, <em class="sig-param">regional_certificate_name=None</em>, <em class="sig-param">security_policy=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DomainName" title="Permalink to this definition">¶</a></dt>
<dd><p>Registers a custom domain name for use with AWS API Gateway. Additional information about this functionality
can be found in the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html">API Gateway Developer Guide</a>.</p>
<p>This resource just establishes ownership of and the TLS settings for
a particular domain name. An API can be attached to a particular path
under the registered domain name using
the <code class="docutils literal notranslate"><span class="pre">apigateway.BasePathMapping</span></code> resource.</p>
<p>API Gateway domains can be defined as either ‘edge-optimized’ or ‘regional’.  In an edge-optimized configuration,
API Gateway internally creates and manages a CloudFront distribution to route requests on the given hostname. In
addition to this resource it’s necessary to create a DNS record corresponding to the given domain name which is an alias
(either Route53 alias or traditional CNAME) to the Cloudfront domain name exported in the <code class="docutils literal notranslate"><span class="pre">cloudfront_domain_name</span></code>
attribute.</p>
<p>In a regional configuration, API Gateway does not create a CloudFront distribution to route requests to the API, though
a distribution can be created if needed. In either case, it is necessary to create a DNS record corresponding to the
given domain name which is an alias (either Route53 alias or traditional CNAME) to the regional domain name exported in
the <code class="docutils literal notranslate"><span class="pre">regional_domain_name</span></code> attribute.</p>
<blockquote>
<div><p><strong>Note:</strong> API Gateway requires the use of AWS Certificate Manager (ACM) certificates instead of Identity and Access Management (IAM) certificates in regions that support ACM. Regions that support ACM can be found in the <a class="reference external" href="https://docs.aws.amazon.com/general/latest/gr/rande.html#acm_region">Regions and Endpoints Documentation</a>. To import an existing private key and certificate into ACM or request an ACM certificate, see the <cite>``acm.Certificate`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/acm_certificate.html">https://www.terraform.io/docs/providers/aws/r/acm_certificate.html</a>&gt;`_.</p>
<p><strong>Note:</strong> The <code class="docutils literal notranslate"><span class="pre">apigateway.DomainName</span></code> resource expects dependency on the <code class="docutils literal notranslate"><span class="pre">acm.CertificateValidation</span></code> as 
only verified certificates can be used. This can be made either explicitly by adding the 
<code class="docutils literal notranslate"><span class="pre">depends_on</span> <span class="pre">=</span> <span class="pre">[aws_acm_certificate_validation.cert]</span></code> attribute. Or implicitly by referring certificate ARN 
from the validation resource where it will be available after the resource creation: 
<code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span> <span class="pre">=</span> <span class="pre">aws_acm_certificate_validation.cert.certificate_arn</span></code>.</p>
<p><strong>Note:</strong> All arguments including the private key will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_name</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_body</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_chain</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_private_key</span></code>, <code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and <code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>.</p></li>
<li><p><strong>certificate_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate issued for the domain name
being registered, in PEM format. Only valid for <code class="docutils literal notranslate"><span class="pre">EDGE</span></code> endpoint configuration type. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and
<code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>.</p></li>
<li><p><strong>certificate_chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for <code class="docutils literal notranslate"><span class="pre">EDGE</span></code> endpoint configuration type. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>,
<code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and <code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>.</p></li>
<li><p><strong>certificate_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and
<code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>. Required if <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code> is not set.</p></li>
<li><p><strong>certificate_private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key associated with the
domain certificate given in <code class="docutils literal notranslate"><span class="pre">certificate_body</span></code>. Only valid for <code class="docutils literal notranslate"><span class="pre">EDGE</span></code> endpoint configuration type. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and <code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully-qualified domain name to register</p></li>
<li><p><strong>endpoint_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block defining API endpoint information including type. Defined below.</p></li>
<li><p><strong>regional_certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_name</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_body</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_chain</span></code>, and <code class="docutils literal notranslate"><span class="pre">certificate_private_key</span></code>.</p></li>
<li><p><strong>regional_certificate_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_name</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_body</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_chain</span></code>, and
<code class="docutils literal notranslate"><span class="pre">certificate_private_key</span></code>.</p></li>
<li><p><strong>security_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Transport Layer Security (TLS) version + cipher suite for this DomainName. The valid values are <code class="docutils literal notranslate"><span class="pre">TLS_1_0</span></code> and <code class="docutils literal notranslate"><span class="pre">TLS_1_2</span></code>. Must be configured to perform drift detection.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>endpoint_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">types</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of endpoint types. This resource currently only supports managing a single value. Valid values: <code class="docutils literal notranslate"><span class="pre">EDGE</span></code> or <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>. If unspecified, defaults to <code class="docutils literal notranslate"><span class="pre">EDGE</span></code>. Must be declared as <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code> in non-Commercial partitions. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html">documentation</a> for more information on the difference between edge-optimized and regional APIs.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_domain_name.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_domain_name.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.certificate_arn">
<code class="sig-name descname">certificate_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_name</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_body</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_chain</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_private_key</span></code>, <code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and <code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.certificate_body">
<code class="sig-name descname">certificate_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.certificate_body" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate issued for the domain name
being registered, in PEM format. Only valid for <code class="docutils literal notranslate"><span class="pre">EDGE</span></code> endpoint configuration type. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and
<code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.certificate_chain">
<code class="sig-name descname">certificate_chain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.certificate_chain" title="Permalink to this definition">¶</a></dt>
<dd><p>The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for <code class="docutils literal notranslate"><span class="pre">EDGE</span></code> endpoint configuration type. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>,
<code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and <code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.certificate_name">
<code class="sig-name descname">certificate_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.certificate_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and
<code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>. Required if <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code> is not set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.certificate_private_key">
<code class="sig-name descname">certificate_private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.certificate_private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key associated with the
domain certificate given in <code class="docutils literal notranslate"><span class="pre">certificate_body</span></code>. Only valid for <code class="docutils literal notranslate"><span class="pre">EDGE</span></code> endpoint configuration type. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and <code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.certificate_upload_date">
<code class="sig-name descname">certificate_upload_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.certificate_upload_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The upload date associated with the domain certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.cloudfront_domain_name">
<code class="sig-name descname">cloudfront_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.cloudfront_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.cloudfront_zone_id">
<code class="sig-name descname">cloudfront_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.cloudfront_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>For convenience, the hosted zone ID (<code class="docutils literal notranslate"><span class="pre">Z2FDTNDATAQYW2</span></code>)
that can be used to create a Route53 alias record for the distribution.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.domain_name">
<code class="sig-name descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-qualified domain name to register</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.endpoint_configuration">
<code class="sig-name descname">endpoint_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.endpoint_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block defining API endpoint information including type. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">types</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A list of endpoint types. This resource currently only supports managing a single value. Valid values: <code class="docutils literal notranslate"><span class="pre">EDGE</span></code> or <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>. If unspecified, defaults to <code class="docutils literal notranslate"><span class="pre">EDGE</span></code>. Must be declared as <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code> in non-Commercial partitions. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html">documentation</a> for more information on the difference between edge-optimized and regional APIs.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.regional_certificate_arn">
<code class="sig-name descname">regional_certificate_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.regional_certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_name</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_body</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_chain</span></code>, and <code class="docutils literal notranslate"><span class="pre">certificate_private_key</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.regional_certificate_name">
<code class="sig-name descname">regional_certificate_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.regional_certificate_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_name</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_body</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_chain</span></code>, and
<code class="docutils literal notranslate"><span class="pre">certificate_private_key</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.regional_domain_name">
<code class="sig-name descname">regional_domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.regional_domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname for the custom domain’s regional endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.regional_zone_id">
<code class="sig-name descname">regional_zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.regional_zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.security_policy">
<code class="sig-name descname">security_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.security_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The Transport Layer Security (TLS) version + cipher suite for this DomainName. The valid values are <code class="docutils literal notranslate"><span class="pre">TLS_1_0</span></code> and <code class="docutils literal notranslate"><span class="pre">TLS_1_2</span></code>. Must be configured to perform drift detection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.DomainName.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.DomainName.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">certificate_arn=None</em>, <em class="sig-param">certificate_body=None</em>, <em class="sig-param">certificate_chain=None</em>, <em class="sig-param">certificate_name=None</em>, <em class="sig-param">certificate_private_key=None</em>, <em class="sig-param">certificate_upload_date=None</em>, <em class="sig-param">cloudfront_domain_name=None</em>, <em class="sig-param">cloudfront_zone_id=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">endpoint_configuration=None</em>, <em class="sig-param">regional_certificate_arn=None</em>, <em class="sig-param">regional_certificate_name=None</em>, <em class="sig-param">regional_domain_name=None</em>, <em class="sig-param">regional_zone_id=None</em>, <em class="sig-param">security_policy=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DomainName resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN)</p></li>
<li><p><strong>certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when an edge-optimized domain name is desired. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_name</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_body</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_chain</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_private_key</span></code>, <code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and <code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>.</p></li>
<li><p><strong>certificate_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate issued for the domain name
being registered, in PEM format. Only valid for <code class="docutils literal notranslate"><span class="pre">EDGE</span></code> endpoint configuration type. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and
<code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>.</p></li>
<li><p><strong>certificate_chain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The certificate for the CA that issued the
certificate, along with any intermediate CA certificates required to
create an unbroken chain to a certificate trusted by the intended API clients. Only valid for <code class="docutils literal notranslate"><span class="pre">EDGE</span></code> endpoint configuration type. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>,
<code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and <code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>.</p></li>
<li><p><strong>certificate_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name to use when registering this
certificate as an IAM server certificate. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and
<code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>. Required if <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code> is not set.</p></li>
<li><p><strong>certificate_private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key associated with the
domain certificate given in <code class="docutils literal notranslate"><span class="pre">certificate_body</span></code>. Only valid for <code class="docutils literal notranslate"><span class="pre">EDGE</span></code> endpoint configuration type. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">regional_certificate_arn</span></code>, and <code class="docutils literal notranslate"><span class="pre">regional_certificate_name</span></code>.</p></li>
<li><p><strong>certificate_upload_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The upload date associated with the domain certificate.</p></li>
<li><p><strong>cloudfront_domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname created by Cloudfront to represent
the distribution that implements this domain name mapping.</p></li>
<li><p><strong>cloudfront_zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For convenience, the hosted zone ID (<code class="docutils literal notranslate"><span class="pre">Z2FDTNDATAQYW2</span></code>)
that can be used to create a Route53 alias record for the distribution.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully-qualified domain name to register</p></li>
<li><p><strong>endpoint_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block defining API endpoint information including type. Defined below.</p></li>
<li><p><strong>regional_certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for an AWS-managed certificate. AWS Certificate Manager is the only supported source. Used when a regional domain name is desired. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_name</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_body</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_chain</span></code>, and <code class="docutils literal notranslate"><span class="pre">certificate_private_key</span></code>.</p></li>
<li><p><strong>regional_certificate_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user-friendly name of the certificate that will be used by regional endpoint for this domain name. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_name</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_body</span></code>, <code class="docutils literal notranslate"><span class="pre">certificate_chain</span></code>, and
<code class="docutils literal notranslate"><span class="pre">certificate_private_key</span></code>.</p></li>
<li><p><strong>regional_domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hostname for the custom domain’s regional endpoint.</p></li>
<li><p><strong>regional_zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The hosted zone ID that can be used to create a Route53 alias record for the regional endpoint.</p></li>
<li><p><strong>security_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Transport Layer Security (TLS) version + cipher suite for this DomainName. The valid values are <code class="docutils literal notranslate"><span class="pre">TLS_1_0</span></code> and <code class="docutils literal notranslate"><span class="pre">TLS_1_2</span></code>. Must be configured to perform drift detection.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>endpoint_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">types</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of endpoint types. This resource currently only supports managing a single value. Valid values: <code class="docutils literal notranslate"><span class="pre">EDGE</span></code> or <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>. If unspecified, defaults to <code class="docutils literal notranslate"><span class="pre">EDGE</span></code>. Must be declared as <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code> in non-Commercial partitions. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html">documentation</a> for more information on the difference between edge-optimized and regional APIs.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_domain_name.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_domain_name.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.DomainName.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.DomainName.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.DomainName.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.GetKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">GetKeyResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.GetKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKey.</p>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetKeyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the ID of the API Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetKeyResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetKeyResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the name of the API Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetKeyResult.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetKeyResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the value of the API Key.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.apigateway.GetResourceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">GetResourceResult</code><span class="sig-paren">(</span><em class="sig-param">parent_id=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">path_part=None</em>, <em class="sig-param">rest_api_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.GetResourceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getResource.</p>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetResourceResult.parent_id">
<code class="sig-name descname">parent_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetResourceResult.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the ID of the parent Resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetResourceResult.path_part">
<code class="sig-name descname">path_part</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetResourceResult.path_part" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the path relative to the parent Resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetResourceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetResourceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.apigateway.GetRestApiResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">GetRestApiResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">root_resource_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.GetRestApiResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRestApi.</p>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetRestApiResult.root_resource_id">
<code class="sig-name descname">root_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetRestApiResult.root_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the ID of the API Gateway Resource on the found REST API where the route matches ‘/’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetRestApiResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetRestApiResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.apigateway.GetVpcLinkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">GetVpcLinkResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.GetVpcLinkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpcLink.</p>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.GetVpcLinkResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.GetVpcLinkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the ID of the found API Gateway VPC Link.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.apigateway.Integration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">Integration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cache_key_parameters=None</em>, <em class="sig-param">cache_namespace=None</em>, <em class="sig-param">connection_id=None</em>, <em class="sig-param">connection_type=None</em>, <em class="sig-param">content_handling=None</em>, <em class="sig-param">credentials=None</em>, <em class="sig-param">http_method=None</em>, <em class="sig-param">integration_http_method=None</em>, <em class="sig-param">passthrough_behavior=None</em>, <em class="sig-param">request_parameters=None</em>, <em class="sig-param">request_templates=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">timeout_milliseconds=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">uri=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an HTTP Method Integration for an API Gateway Integration.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cache_key_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of cache key parameters for the integration.</p></li>
<li><p><strong>cache_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration’s cache namespace.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the VpcLink used for the integration. <strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">connection_type</span></code> is <code class="docutils literal notranslate"><span class="pre">VPC_LINK</span></code></p></li>
<li><p><strong>connection_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration input’s <a class="reference external" href="https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/#connectionType">connectionType</a>. Valid values are <code class="docutils literal notranslate"><span class="pre">INTERNET</span></code> (default for connections through the public routable internet), and <code class="docutils literal notranslate"><span class="pre">VPC_LINK</span></code> (for private connections between API Gateway and a network load balancer in a VPC).</p></li>
<li><p><strong>content_handling</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how to handle request payload content type conversions. Supported values are <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_BINARY</span></code> and <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_TEXT</span></code>. If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the passthroughBehaviors is configured to support payload pass-through.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The credentials required for the integration. For <code class="docutils literal notranslate"><span class="pre">AWS</span></code> integrations, 2 options are available. To specify an IAM Role for Amazon API Gateway to assume, use the role’s ARN. To require that the caller’s identity be passed through from the request, specify the string <code class="docutils literal notranslate"><span class="pre">arn:aws:iam::\*:user/\*</span></code>.</p></li>
<li><p><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP method (<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTION</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>)
when calling the associated resource.</p></li>
<li><p><strong>integration_http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration HTTP method
(<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONs</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>) specifying how API Gateway will interact with the back end.
<strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code>.
Not all methods are compatible with all <code class="docutils literal notranslate"><span class="pre">AWS</span></code> integrations.
e.g. Lambda function <a class="reference external" href="https://github.com/awslabs/aws-apigateway-importer/issues/9#issuecomment-129651005">can only be invoked</a> via <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p></li>
<li><p><strong>passthrough_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration passthrough behavior (<code class="docutils literal notranslate"><span class="pre">WHEN_NO_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">WHEN_NO_TEMPLATES</span></code>, <code class="docutils literal notranslate"><span class="pre">NEVER</span></code>).  <strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">request_templates</span></code> is used.</p></li>
<li><p><strong>request_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of request query string parameters and headers that should be passed to the backend responder.
For example: <code class="docutils literal notranslate"><span class="pre">request_parameters</span> <span class="pre">=</span> <span class="pre">{</span> <span class="pre">&quot;integration.request.header.X-Some-Other-Header&quot;</span> <span class="pre">=</span> <span class="pre">&quot;method.request.header.X-Some-Header&quot;</span> <span class="pre">}</span></code></p></li>
<li><p><strong>request_templates</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of the integration’s request templates.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API resource ID.</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API.</p></li>
<li><p><strong>timeout_milliseconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration input’s <a class="reference external" href="https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/">type</a>. Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> (for HTTP backends), <code class="docutils literal notranslate"><span class="pre">MOCK</span></code> (not calling any real backend), <code class="docutils literal notranslate"><span class="pre">AWS</span></code> (for AWS services), <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code> (for Lambda proxy integration) and <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code> (for HTTP proxy integration). An <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code> integration with a <code class="docutils literal notranslate"><span class="pre">connection_type</span></code> of <code class="docutils literal notranslate"><span class="pre">VPC_LINK</span></code> is referred to as a private integration and uses a VpcLink to connect API Gateway to a network load balancer of a VPC.</p></li>
<li><p><strong>uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The input’s URI. <strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code>.
For HTTP integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification . For AWS integrations, the URI should be of the form <code class="docutils literal notranslate"><span class="pre">arn:aws:apigateway:{region}:{subdomain.service|service}:{path|action}/{service_api}</span></code>. <code class="docutils literal notranslate"><span class="pre">region</span></code>, <code class="docutils literal notranslate"><span class="pre">subdomain</span></code> and <code class="docutils literal notranslate"><span class="pre">service</span></code> are used to determine the right endpoint.
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:apigateway:eu-west-1:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-1:012345678901:function:my-func/invocations</span></code></p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_integration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_integration.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.cache_key_parameters">
<code class="sig-name descname">cache_key_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.cache_key_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of cache key parameters for the integration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.cache_namespace">
<code class="sig-name descname">cache_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.cache_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration’s cache namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.connection_id">
<code class="sig-name descname">connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the VpcLink used for the integration. <strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">connection_type</span></code> is <code class="docutils literal notranslate"><span class="pre">VPC_LINK</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.connection_type">
<code class="sig-name descname">connection_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.connection_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration input’s <a class="reference external" href="https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/#connectionType">connectionType</a>. Valid values are <code class="docutils literal notranslate"><span class="pre">INTERNET</span></code> (default for connections through the public routable internet), and <code class="docutils literal notranslate"><span class="pre">VPC_LINK</span></code> (for private connections between API Gateway and a network load balancer in a VPC).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.content_handling">
<code class="sig-name descname">content_handling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.content_handling" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how to handle request payload content type conversions. Supported values are <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_BINARY</span></code> and <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_TEXT</span></code>. If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the passthroughBehaviors is configured to support payload pass-through.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.credentials">
<code class="sig-name descname">credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>The credentials required for the integration. For <code class="docutils literal notranslate"><span class="pre">AWS</span></code> integrations, 2 options are available. To specify an IAM Role for Amazon API Gateway to assume, use the role’s ARN. To require that the caller’s identity be passed through from the request, specify the string <code class="docutils literal notranslate"><span class="pre">arn:aws:iam::\*:user/\*</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.http_method">
<code class="sig-name descname">http_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.http_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP method (<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTION</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>)
when calling the associated resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.integration_http_method">
<code class="sig-name descname">integration_http_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.integration_http_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration HTTP method
(<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONs</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>) specifying how API Gateway will interact with the back end.
<strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code>.
Not all methods are compatible with all <code class="docutils literal notranslate"><span class="pre">AWS</span></code> integrations.
e.g. Lambda function <a class="reference external" href="https://github.com/awslabs/aws-apigateway-importer/issues/9#issuecomment-129651005">can only be invoked</a> via <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.passthrough_behavior">
<code class="sig-name descname">passthrough_behavior</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.passthrough_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration passthrough behavior (<code class="docutils literal notranslate"><span class="pre">WHEN_NO_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">WHEN_NO_TEMPLATES</span></code>, <code class="docutils literal notranslate"><span class="pre">NEVER</span></code>).  <strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">request_templates</span></code> is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.request_parameters">
<code class="sig-name descname">request_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.request_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of request query string parameters and headers that should be passed to the backend responder.
For example: <code class="docutils literal notranslate"><span class="pre">request_parameters</span> <span class="pre">=</span> <span class="pre">{</span> <span class="pre">&quot;integration.request.header.X-Some-Other-Header&quot;</span> <span class="pre">=</span> <span class="pre">&quot;method.request.header.X-Some-Header&quot;</span> <span class="pre">}</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.request_templates">
<code class="sig-name descname">request_templates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.request_templates" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of the integration’s request templates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.resource_id">
<code class="sig-name descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API resource ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.rest_api">
<code class="sig-name descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.timeout_milliseconds">
<code class="sig-name descname">timeout_milliseconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.timeout_milliseconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration input’s <a class="reference external" href="https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/">type</a>. Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> (for HTTP backends), <code class="docutils literal notranslate"><span class="pre">MOCK</span></code> (not calling any real backend), <code class="docutils literal notranslate"><span class="pre">AWS</span></code> (for AWS services), <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code> (for Lambda proxy integration) and <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code> (for HTTP proxy integration). An <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code> integration with a <code class="docutils literal notranslate"><span class="pre">connection_type</span></code> of <code class="docutils literal notranslate"><span class="pre">VPC_LINK</span></code> is referred to as a private integration and uses a VpcLink to connect API Gateway to a network load balancer of a VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Integration.uri">
<code class="sig-name descname">uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Integration.uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The input’s URI. <strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code>.
For HTTP integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification . For AWS integrations, the URI should be of the form <code class="docutils literal notranslate"><span class="pre">arn:aws:apigateway:{region}:{subdomain.service|service}:{path|action}/{service_api}</span></code>. <code class="docutils literal notranslate"><span class="pre">region</span></code>, <code class="docutils literal notranslate"><span class="pre">subdomain</span></code> and <code class="docutils literal notranslate"><span class="pre">service</span></code> are used to determine the right endpoint.
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:apigateway:eu-west-1:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-1:012345678901:function:my-func/invocations</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Integration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cache_key_parameters=None</em>, <em class="sig-param">cache_namespace=None</em>, <em class="sig-param">connection_id=None</em>, <em class="sig-param">connection_type=None</em>, <em class="sig-param">content_handling=None</em>, <em class="sig-param">credentials=None</em>, <em class="sig-param">http_method=None</em>, <em class="sig-param">integration_http_method=None</em>, <em class="sig-param">passthrough_behavior=None</em>, <em class="sig-param">request_parameters=None</em>, <em class="sig-param">request_templates=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">timeout_milliseconds=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">uri=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Integration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Integration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cache_key_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of cache key parameters for the integration.</p></li>
<li><p><strong>cache_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration’s cache namespace.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the VpcLink used for the integration. <strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">connection_type</span></code> is <code class="docutils literal notranslate"><span class="pre">VPC_LINK</span></code></p></li>
<li><p><strong>connection_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The integration input’s <a class="reference external" href="https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/#connectionType">connectionType</a>. Valid values are <code class="docutils literal notranslate"><span class="pre">INTERNET</span></code> (default for connections through the public routable internet), and <code class="docutils literal notranslate"><span class="pre">VPC_LINK</span></code> (for private connections between API Gateway and a network load balancer in a VPC).</p>
</p></li>
<li><p><strong>content_handling</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how to handle request payload content type conversions. Supported values are <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_BINARY</span></code> and <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_TEXT</span></code>. If this property is not defined, the request payload will be passed through from the method request to integration request without modification, provided that the passthroughBehaviors is configured to support payload pass-through.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The credentials required for the integration. For <code class="docutils literal notranslate"><span class="pre">AWS</span></code> integrations, 2 options are available. To specify an IAM Role for Amazon API Gateway to assume, use the role’s ARN. To require that the caller’s identity be passed through from the request, specify the string <code class="docutils literal notranslate"><span class="pre">arn:aws:iam::\*:user/\*</span></code>.</p></li>
<li><p><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP method (<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTION</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>)
when calling the associated resource.</p></li>
<li><p><strong>integration_http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The integration HTTP method
(<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONs</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>) specifying how API Gateway will interact with the back end.
<strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code>.
Not all methods are compatible with all <code class="docutils literal notranslate"><span class="pre">AWS</span></code> integrations.
e.g. Lambda function <a class="reference external" href="https://github.com/awslabs/aws-apigateway-importer/issues/9#issuecomment-129651005">can only be invoked</a> via <code class="docutils literal notranslate"><span class="pre">POST</span></code>.</p>
</p></li>
<li><p><strong>passthrough_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration passthrough behavior (<code class="docutils literal notranslate"><span class="pre">WHEN_NO_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">WHEN_NO_TEMPLATES</span></code>, <code class="docutils literal notranslate"><span class="pre">NEVER</span></code>).  <strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">request_templates</span></code> is used.</p></li>
<li><p><strong>request_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of request query string parameters and headers that should be passed to the backend responder.
For example: <code class="docutils literal notranslate"><span class="pre">request_parameters</span> <span class="pre">=</span> <span class="pre">{</span> <span class="pre">&quot;integration.request.header.X-Some-Other-Header&quot;</span> <span class="pre">=</span> <span class="pre">&quot;method.request.header.X-Some-Header&quot;</span> <span class="pre">}</span></code></p></li>
<li><p><strong>request_templates</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of the integration’s request templates.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API resource ID.</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API.</p></li>
<li><p><strong>timeout_milliseconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The integration input’s <a class="reference external" href="https://docs.aws.amazon.com/apigateway/api-reference/resource/integration/">type</a>. Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> (for HTTP backends), <code class="docutils literal notranslate"><span class="pre">MOCK</span></code> (not calling any real backend), <code class="docutils literal notranslate"><span class="pre">AWS</span></code> (for AWS services), <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code> (for Lambda proxy integration) and <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code> (for HTTP proxy integration). An <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code> integration with a <code class="docutils literal notranslate"><span class="pre">connection_type</span></code> of <code class="docutils literal notranslate"><span class="pre">VPC_LINK</span></code> is referred to as a private integration and uses a VpcLink to connect API Gateway to a network load balancer of a VPC.</p>
</p></li>
<li><p><strong>uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The input’s URI. <strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code>.
For HTTP integrations, the URI must be a fully formed, encoded HTTP(S) URL according to the RFC-3986 specification . For AWS integrations, the URI should be of the form <code class="docutils literal notranslate"><span class="pre">arn:aws:apigateway:{region}:{subdomain.service|service}:{path|action}/{service_api}</span></code>. <code class="docutils literal notranslate"><span class="pre">region</span></code>, <code class="docutils literal notranslate"><span class="pre">subdomain</span></code> and <code class="docutils literal notranslate"><span class="pre">service</span></code> are used to determine the right endpoint.
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:apigateway:eu-west-1:lambda:path/2015-03-31/functions/arn:aws:lambda:eu-west-1:012345678901:function:my-func/invocations</span></code></p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_integration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_integration.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Integration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Integration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.IntegrationResponse">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">IntegrationResponse</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content_handling=None</em>, <em class="sig-param">http_method=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">response_parameters=None</em>, <em class="sig-param">response_templates=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">selection_pattern=None</em>, <em class="sig-param">status_code=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an HTTP Method Integration Response for an API Gateway Resource.</p>
<blockquote>
<div><p><strong>Note:</strong> Depends on having <code class="docutils literal notranslate"><span class="pre">apigateway.Integration</span></code> inside your rest api. To ensure this
you might need to add an explicit <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> for clean runs.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_handling</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how to handle request payload content type conversions. Supported values are <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_BINARY</span></code> and <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_TEXT</span></code>. If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.</p></li>
<li><p><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP method (<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>)</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API resource ID</p></li>
<li><p><strong>response_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of response parameters that can be read from the backend response.
For example: <code class="docutils literal notranslate"><span class="pre">response_parameters</span> <span class="pre">=</span> <span class="pre">{</span> <span class="pre">&quot;method.response.header.X-Some-Header&quot;</span> <span class="pre">=</span> <span class="pre">&quot;integration.response.header.X-Some-Other-Header&quot;</span> <span class="pre">}</span></code></p></li>
<li><p><strong>response_templates</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map specifying the templates used to transform the integration response body</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
<li><p><strong>selection_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the regular expression pattern used to choose
an integration response based on the response from the backend. Setting this to <code class="docutils literal notranslate"><span class="pre">-</span></code> makes the integration the default one.
If the backend is an <code class="docutils literal notranslate"><span class="pre">AWS</span></code> Lambda function, the AWS Lambda function error header is matched.
For all other <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> and <code class="docutils literal notranslate"><span class="pre">AWS</span></code> backends, the HTTP status code is matched.</p></li>
<li><p><strong>status_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP status code</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_integration_response.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_integration_response.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.content_handling">
<code class="sig-name descname">content_handling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.content_handling" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how to handle request payload content type conversions. Supported values are <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_BINARY</span></code> and <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_TEXT</span></code>. If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.http_method">
<code class="sig-name descname">http_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.http_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP method (<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.resource_id">
<code class="sig-name descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API resource ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.response_parameters">
<code class="sig-name descname">response_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.response_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of response parameters that can be read from the backend response.
For example: <code class="docutils literal notranslate"><span class="pre">response_parameters</span> <span class="pre">=</span> <span class="pre">{</span> <span class="pre">&quot;method.response.header.X-Some-Header&quot;</span> <span class="pre">=</span> <span class="pre">&quot;integration.response.header.X-Some-Other-Header&quot;</span> <span class="pre">}</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.response_templates">
<code class="sig-name descname">response_templates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.response_templates" title="Permalink to this definition">¶</a></dt>
<dd><p>A map specifying the templates used to transform the integration response body</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.rest_api">
<code class="sig-name descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.selection_pattern">
<code class="sig-name descname">selection_pattern</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.selection_pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the regular expression pattern used to choose
an integration response based on the response from the backend. Setting this to <code class="docutils literal notranslate"><span class="pre">-</span></code> makes the integration the default one.
If the backend is an <code class="docutils literal notranslate"><span class="pre">AWS</span></code> Lambda function, the AWS Lambda function error header is matched.
For all other <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> and <code class="docutils literal notranslate"><span class="pre">AWS</span></code> backends, the HTTP status code is matched.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.IntegrationResponse.status_code">
<code class="sig-name descname">status_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.status_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP status code</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.IntegrationResponse.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content_handling=None</em>, <em class="sig-param">http_method=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">response_parameters=None</em>, <em class="sig-param">response_templates=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">selection_pattern=None</em>, <em class="sig-param">status_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IntegrationResponse resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_handling</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how to handle request payload content type conversions. Supported values are <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_BINARY</span></code> and <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_TEXT</span></code>. If this property is not defined, the response payload will be passed through from the integration response to the method response without modification.</p></li>
<li><p><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP method (<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>)</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API resource ID</p></li>
<li><p><strong>response_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of response parameters that can be read from the backend response.
For example: <code class="docutils literal notranslate"><span class="pre">response_parameters</span> <span class="pre">=</span> <span class="pre">{</span> <span class="pre">&quot;method.response.header.X-Some-Header&quot;</span> <span class="pre">=</span> <span class="pre">&quot;integration.response.header.X-Some-Other-Header&quot;</span> <span class="pre">}</span></code></p></li>
<li><p><strong>response_templates</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map specifying the templates used to transform the integration response body</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
<li><p><strong>selection_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the regular expression pattern used to choose
an integration response based on the response from the backend. Setting this to <code class="docutils literal notranslate"><span class="pre">-</span></code> makes the integration the default one.
If the backend is an <code class="docutils literal notranslate"><span class="pre">AWS</span></code> Lambda function, the AWS Lambda function error header is matched.
For all other <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> and <code class="docutils literal notranslate"><span class="pre">AWS</span></code> backends, the HTTP status code is matched.</p></li>
<li><p><strong>status_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP status code</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_integration_response.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_integration_response.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.IntegrationResponse.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.IntegrationResponse.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.IntegrationResponse.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Method">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">Method</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_key_required=None</em>, <em class="sig-param">authorization=None</em>, <em class="sig-param">authorization_scopes=None</em>, <em class="sig-param">authorizer_id=None</em>, <em class="sig-param">http_method=None</em>, <em class="sig-param">request_models=None</em>, <em class="sig-param">request_parameters=None</em>, <em class="sig-param">request_validator_id=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Method" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a HTTP Method for an API Gateway Resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify if the method requires an API key</p></li>
<li><p><strong>authorization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of authorization used for the method (<code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">COGNITO_USER_POOLS</span></code>)</p></li>
<li><p><strong>authorization_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The authorization scopes used when the authorization is <code class="docutils literal notranslate"><span class="pre">COGNITO_USER_POOLS</span></code></p></li>
<li><p><strong>authorizer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorizer id to be used when the authorization is <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code> or <code class="docutils literal notranslate"><span class="pre">COGNITO_USER_POOLS</span></code></p></li>
<li><p><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP Method (<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>)</p></li>
<li><p><strong>request_models</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of the API models used for the request’s content type
where key is the content type (e.g. <code class="docutils literal notranslate"><span class="pre">application/json</span></code>)
and value is either <code class="docutils literal notranslate"><span class="pre">Error</span></code>, <code class="docutils literal notranslate"><span class="pre">Empty</span></code> (built-in models) or <code class="docutils literal notranslate"><span class="pre">apigateway.Model</span></code>’s <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>request_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of request parameters (from the path, query string and headers) that should be passed to the integration. The boolean value indicates whether the parameter is required (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or optional (<code class="docutils literal notranslate"><span class="pre">false</span></code>).
For example: <code class="docutils literal notranslate"><span class="pre">request_parameters</span> <span class="pre">=</span> <span class="pre">{&quot;method.request.header.X-Some-Header&quot;</span> <span class="pre">=</span> <span class="pre">true</span> <span class="pre">&quot;method.request.querystring.some-query-param&quot;</span> <span class="pre">=</span> <span class="pre">true}</span></code> would define that the header <code class="docutils literal notranslate"><span class="pre">X-Some-Header</span></code> and the query string <code class="docutils literal notranslate"><span class="pre">some-query-param</span></code> must be provided in the request.</p></li>
<li><p><strong>request_validator_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a <code class="docutils literal notranslate"><span class="pre">apigateway.RequestValidator</span></code></p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API resource ID</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.api_key_required">
<code class="sig-name descname">api_key_required</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.api_key_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify if the method requires an API key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.authorization">
<code class="sig-name descname">authorization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.authorization" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of authorization used for the method (<code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">COGNITO_USER_POOLS</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.authorization_scopes">
<code class="sig-name descname">authorization_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.authorization_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorization scopes used when the authorization is <code class="docutils literal notranslate"><span class="pre">COGNITO_USER_POOLS</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.authorizer_id">
<code class="sig-name descname">authorizer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.authorizer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorizer id to be used when the authorization is <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code> or <code class="docutils literal notranslate"><span class="pre">COGNITO_USER_POOLS</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.http_method">
<code class="sig-name descname">http_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.http_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP Method (<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.request_models">
<code class="sig-name descname">request_models</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.request_models" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of the API models used for the request’s content type
where key is the content type (e.g. <code class="docutils literal notranslate"><span class="pre">application/json</span></code>)
and value is either <code class="docutils literal notranslate"><span class="pre">Error</span></code>, <code class="docutils literal notranslate"><span class="pre">Empty</span></code> (built-in models) or <code class="docutils literal notranslate"><span class="pre">apigateway.Model</span></code>’s <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.request_parameters">
<code class="sig-name descname">request_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.request_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of request parameters (from the path, query string and headers) that should be passed to the integration. The boolean value indicates whether the parameter is required (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or optional (<code class="docutils literal notranslate"><span class="pre">false</span></code>).
For example: <code class="docutils literal notranslate"><span class="pre">request_parameters</span> <span class="pre">=</span> <span class="pre">{&quot;method.request.header.X-Some-Header&quot;</span> <span class="pre">=</span> <span class="pre">true</span> <span class="pre">&quot;method.request.querystring.some-query-param&quot;</span> <span class="pre">=</span> <span class="pre">true}</span></code> would define that the header <code class="docutils literal notranslate"><span class="pre">X-Some-Header</span></code> and the query string <code class="docutils literal notranslate"><span class="pre">some-query-param</span></code> must be provided in the request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.request_validator_id">
<code class="sig-name descname">request_validator_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.request_validator_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a <code class="docutils literal notranslate"><span class="pre">apigateway.RequestValidator</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.resource_id">
<code class="sig-name descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API resource ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Method.rest_api">
<code class="sig-name descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Method.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Method.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_key_required=None</em>, <em class="sig-param">authorization=None</em>, <em class="sig-param">authorization_scopes=None</em>, <em class="sig-param">authorizer_id=None</em>, <em class="sig-param">http_method=None</em>, <em class="sig-param">request_models=None</em>, <em class="sig-param">request_parameters=None</em>, <em class="sig-param">request_validator_id=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">rest_api=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Method.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Method resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify if the method requires an API key</p></li>
<li><p><strong>authorization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of authorization used for the method (<code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">COGNITO_USER_POOLS</span></code>)</p></li>
<li><p><strong>authorization_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The authorization scopes used when the authorization is <code class="docutils literal notranslate"><span class="pre">COGNITO_USER_POOLS</span></code></p></li>
<li><p><strong>authorizer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorizer id to be used when the authorization is <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code> or <code class="docutils literal notranslate"><span class="pre">COGNITO_USER_POOLS</span></code></p></li>
<li><p><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP Method (<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>)</p></li>
<li><p><strong>request_models</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of the API models used for the request’s content type
where key is the content type (e.g. <code class="docutils literal notranslate"><span class="pre">application/json</span></code>)
and value is either <code class="docutils literal notranslate"><span class="pre">Error</span></code>, <code class="docutils literal notranslate"><span class="pre">Empty</span></code> (built-in models) or <code class="docutils literal notranslate"><span class="pre">apigateway.Model</span></code>’s <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>request_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of request parameters (from the path, query string and headers) that should be passed to the integration. The boolean value indicates whether the parameter is required (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or optional (<code class="docutils literal notranslate"><span class="pre">false</span></code>).
For example: <code class="docutils literal notranslate"><span class="pre">request_parameters</span> <span class="pre">=</span> <span class="pre">{&quot;method.request.header.X-Some-Header&quot;</span> <span class="pre">=</span> <span class="pre">true</span> <span class="pre">&quot;method.request.querystring.some-query-param&quot;</span> <span class="pre">=</span> <span class="pre">true}</span></code> would define that the header <code class="docutils literal notranslate"><span class="pre">X-Some-Header</span></code> and the query string <code class="docutils literal notranslate"><span class="pre">some-query-param</span></code> must be provided in the request.</p></li>
<li><p><strong>request_validator_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a <code class="docutils literal notranslate"><span class="pre">apigateway.RequestValidator</span></code></p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API resource ID</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Method.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Method.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Method.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Method.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.MethodResponse">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">MethodResponse</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">http_method=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">response_models=None</em>, <em class="sig-param">response_parameters=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">status_code=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an HTTP Method Response for an API Gateway Resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP Method (<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>)</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API resource ID</p></li>
<li><p><strong>response_models</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of the API models used for the response’s content type</p></li>
<li><p><strong>response_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of response parameters that can be sent to the caller.
For example: <code class="docutils literal notranslate"><span class="pre">response_parameters</span> <span class="pre">=</span> <span class="pre">{</span> <span class="pre">&quot;method.response.header.X-Some-Header&quot;</span> <span class="pre">=</span> <span class="pre">true</span> <span class="pre">}</span></code>
would define that the header <code class="docutils literal notranslate"><span class="pre">X-Some-Header</span></code> can be provided on the response.</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
<li><p><strong>status_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP status code</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method_response.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method_response.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodResponse.http_method">
<code class="sig-name descname">http_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.http_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP Method (<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodResponse.resource_id">
<code class="sig-name descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API resource ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodResponse.response_models">
<code class="sig-name descname">response_models</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.response_models" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of the API models used for the response’s content type</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodResponse.response_parameters">
<code class="sig-name descname">response_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.response_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of response parameters that can be sent to the caller.
For example: <code class="docutils literal notranslate"><span class="pre">response_parameters</span> <span class="pre">=</span> <span class="pre">{</span> <span class="pre">&quot;method.response.header.X-Some-Header&quot;</span> <span class="pre">=</span> <span class="pre">true</span> <span class="pre">}</span></code>
would define that the header <code class="docutils literal notranslate"><span class="pre">X-Some-Header</span></code> can be provided on the response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodResponse.rest_api">
<code class="sig-name descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodResponse.status_code">
<code class="sig-name descname">status_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.status_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP status code</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.MethodResponse.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">http_method=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">response_models=None</em>, <em class="sig-param">response_parameters=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">status_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MethodResponse resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>http_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP Method (<code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code>, <code class="docutils literal notranslate"><span class="pre">PUT</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">ANY</span></code>)</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API resource ID</p></li>
<li><p><strong>response_models</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of the API models used for the response’s content type</p></li>
<li><p><strong>response_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of response parameters that can be sent to the caller.
For example: <code class="docutils literal notranslate"><span class="pre">response_parameters</span> <span class="pre">=</span> <span class="pre">{</span> <span class="pre">&quot;method.response.header.X-Some-Header&quot;</span> <span class="pre">=</span> <span class="pre">true</span> <span class="pre">}</span></code>
would define that the header <code class="docutils literal notranslate"><span class="pre">X-Some-Header</span></code> can be provided on the response.</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
<li><p><strong>status_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP status code</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method_response.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method_response.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.MethodResponse.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.MethodResponse.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.MethodResponse.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.MethodSettings">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">MethodSettings</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">method_path=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">stage_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Method Settings, e.g. logging or monitoring.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>method_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Method path defined as <code class="docutils literal notranslate"><span class="pre">{resource_path}/{http_method}</span></code> for an individual method override, or <code class="docutils literal notranslate"><span class="pre">*/*</span></code> for overriding all methods in the stage.</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the REST API</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings block, see below.</p></li>
<li><p><strong>stage_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stage</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheDataEncrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether the cached responses are encrypted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheTtlInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL, the longer the response will be cached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cachingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether responses should be cached and returned for requests. A cache cluster must be enabled on the stage for responses to be cached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataTraceEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether data trace logging is enabled for this method, which effects the log entries pushed to Amazon CloudWatch Logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the logging level for this method, which effects the log entries pushed to Amazon CloudWatch Logs. The available levels are <code class="docutils literal notranslate"><span class="pre">OFF</span></code>, <code class="docutils literal notranslate"><span class="pre">ERROR</span></code>, and <code class="docutils literal notranslate"><span class="pre">INFO</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Amazon CloudWatch metrics are enabled for this method.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireAuthorizationForCacheControl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether authorization is required for a cache invalidation request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingBurstLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the throttling burst limit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingRateLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the throttling rate limit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthorizedCacheControlHeaderStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how to handle unauthorized requests for cache invalidation. The available values are <code class="docutils literal notranslate"><span class="pre">FAIL_WITH_403</span></code>, <code class="docutils literal notranslate"><span class="pre">SUCCEED_WITH_RESPONSE_HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">SUCCEED_WITHOUT_RESPONSE_HEADER</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method_settings.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method_settings.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodSettings.method_path">
<code class="sig-name descname">method_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings.method_path" title="Permalink to this definition">¶</a></dt>
<dd><p>Method path defined as <code class="docutils literal notranslate"><span class="pre">{resource_path}/{http_method}</span></code> for an individual method override, or <code class="docutils literal notranslate"><span class="pre">*/*</span></code> for overriding all methods in the stage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodSettings.rest_api">
<code class="sig-name descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodSettings.settings">
<code class="sig-name descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The settings block, see below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheDataEncrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether the cached responses are encrypted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheTtlInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL, the longer the response will be cached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cachingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether responses should be cached and returned for requests. A cache cluster must be enabled on the stage for responses to be cached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataTraceEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether data trace logging is enabled for this method, which effects the log entries pushed to Amazon CloudWatch Logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the logging level for this method, which effects the log entries pushed to Amazon CloudWatch Logs. The available levels are <code class="docutils literal notranslate"><span class="pre">OFF</span></code>, <code class="docutils literal notranslate"><span class="pre">ERROR</span></code>, and <code class="docutils literal notranslate"><span class="pre">INFO</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether Amazon CloudWatch metrics are enabled for this method.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireAuthorizationForCacheControl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether authorization is required for a cache invalidation request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingBurstLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the throttling burst limit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingRateLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the throttling rate limit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthorizedCacheControlHeaderStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies how to handle unauthorized requests for cache invalidation. The available values are <code class="docutils literal notranslate"><span class="pre">FAIL_WITH_403</span></code>, <code class="docutils literal notranslate"><span class="pre">SUCCEED_WITH_RESPONSE_HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">SUCCEED_WITHOUT_RESPONSE_HEADER</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.MethodSettings.stage_name">
<code class="sig-name descname">stage_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings.stage_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the stage</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.MethodSettings.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">method_path=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">stage_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MethodSettings resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>method_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Method path defined as <code class="docutils literal notranslate"><span class="pre">{resource_path}/{http_method}</span></code> for an individual method override, or <code class="docutils literal notranslate"><span class="pre">*/*</span></code> for overriding all methods in the stage.</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the REST API</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The settings block, see below.</p></li>
<li><p><strong>stage_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stage</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheDataEncrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether the cached responses are encrypted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheTtlInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the time to live (TTL), in seconds, for cached responses. The higher the TTL, the longer the response will be cached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cachingEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether responses should be cached and returned for requests. A cache cluster must be enabled on the stage for responses to be cached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dataTraceEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether data trace logging is enabled for this method, which effects the log entries pushed to Amazon CloudWatch Logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the logging level for this method, which effects the log entries pushed to Amazon CloudWatch Logs. The available levels are <code class="docutils literal notranslate"><span class="pre">OFF</span></code>, <code class="docutils literal notranslate"><span class="pre">ERROR</span></code>, and <code class="docutils literal notranslate"><span class="pre">INFO</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Amazon CloudWatch metrics are enabled for this method.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireAuthorizationForCacheControl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether authorization is required for a cache invalidation request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingBurstLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the throttling burst limit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingRateLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the throttling rate limit.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unauthorizedCacheControlHeaderStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how to handle unauthorized requests for cache invalidation. The available values are <code class="docutils literal notranslate"><span class="pre">FAIL_WITH_403</span></code>, <code class="docutils literal notranslate"><span class="pre">SUCCEED_WITH_RESPONSE_HEADER</span></code>, <code class="docutils literal notranslate"><span class="pre">SUCCEED_WITHOUT_RESPONSE_HEADER</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method_settings.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method_settings.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.MethodSettings.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.MethodSettings.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.MethodSettings.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Model">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">Model</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Model" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Model for a API Gateway.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content type of the model</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the model</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the model</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The schema of the model in a JSON form</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_model.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_model.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Model.content_type">
<code class="sig-name descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Model.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The content type of the model</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Model.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Model.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the model</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Model.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Model.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the model</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Model.rest_api">
<code class="sig-name descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Model.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Model.schema">
<code class="sig-name descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Model.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The schema of the model in a JSON form</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Model.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">schema=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Model.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Model resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content type of the model</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the model</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the model</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The schema of the model in a JSON form</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_model.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_model.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Model.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Model.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Model.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Model.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.RequestValidator">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">RequestValidator</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">validate_request_body=None</em>, <em class="sig-param">validate_request_parameters=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an API Gateway Request Validator.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the request validator</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated Rest API</p></li>
<li><p><strong>validate_request_body</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether to validate request body. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>validate_request_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether to validate request parameters. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_request_validator.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_request_validator.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.RequestValidator.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the request validator</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RequestValidator.rest_api">
<code class="sig-name descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated Rest API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RequestValidator.validate_request_body">
<code class="sig-name descname">validate_request_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator.validate_request_body" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether to validate request body. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RequestValidator.validate_request_parameters">
<code class="sig-name descname">validate_request_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator.validate_request_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether to validate request parameters. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.RequestValidator.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">validate_request_body=None</em>, <em class="sig-param">validate_request_parameters=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RequestValidator resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the request validator</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated Rest API</p></li>
<li><p><strong>validate_request_body</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether to validate request body. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>validate_request_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether to validate request parameters. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_request_validator.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_request_validator.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.RequestValidator.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.RequestValidator.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.RequestValidator.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Resource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">Resource</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">parent_id=None</em>, <em class="sig-param">path_part=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Resource" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the parent API resource</p></li>
<li><p><strong>path_part</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The last path segment of this API resource.</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_resource.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_resource.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Resource.parent_id">
<code class="sig-name descname">parent_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Resource.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the parent API resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Resource.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Resource.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The complete path for this API resource, including all parent paths.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Resource.path_part">
<code class="sig-name descname">path_part</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Resource.path_part" title="Permalink to this definition">¶</a></dt>
<dd><p>The last path segment of this API resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Resource.rest_api">
<code class="sig-name descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Resource.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Resource.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">parent_id=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">path_part=None</em>, <em class="sig-param">rest_api=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Resource.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Resource resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the parent API resource</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The complete path for this API resource, including all parent paths.</p></li>
<li><p><strong>path_part</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The last path segment of this API resource.</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_resource.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_resource.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Resource.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Resource.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Resource.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Resource.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Response">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">Response</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">response_parameters=None</em>, <em class="sig-param">response_templates=None</em>, <em class="sig-param">response_type=None</em>, <em class="sig-param">rest_api_id=None</em>, <em class="sig-param">status_code=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Response" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Gateway Response for a REST API Gateway.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>response_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map specifying the parameters (paths, query strings and headers) of the Gateway Response.</p></li>
<li><p><strong>response_templates</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map specifying the templates used to transform the response body.</p></li>
<li><p><strong>response_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The response type of the associated GatewayResponse.</p></li>
<li><p><strong>rest_api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The string identifier of the associated REST API.</p></li>
<li><p><strong>status_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP status code of the Gateway Response.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_gateway_response.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_gateway_response.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Response.response_parameters">
<code class="sig-name descname">response_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Response.response_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map specifying the parameters (paths, query strings and headers) of the Gateway Response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Response.response_templates">
<code class="sig-name descname">response_templates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Response.response_templates" title="Permalink to this definition">¶</a></dt>
<dd><p>A map specifying the templates used to transform the response body.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Response.response_type">
<code class="sig-name descname">response_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Response.response_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The response type of the associated GatewayResponse.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Response.rest_api_id">
<code class="sig-name descname">rest_api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Response.rest_api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The string identifier of the associated REST API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Response.status_code">
<code class="sig-name descname">status_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Response.status_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP status code of the Gateway Response.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Response.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">response_parameters=None</em>, <em class="sig-param">response_templates=None</em>, <em class="sig-param">response_type=None</em>, <em class="sig-param">rest_api_id=None</em>, <em class="sig-param">status_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Response.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Response resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>response_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map specifying the parameters (paths, query strings and headers) of the Gateway Response.</p></li>
<li><p><strong>response_templates</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map specifying the templates used to transform the response body.</p></li>
<li><p><strong>response_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The response type of the associated GatewayResponse.</p></li>
<li><p><strong>rest_api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The string identifier of the associated REST API.</p></li>
<li><p><strong>status_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HTTP status code of the Gateway Response.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_gateway_response.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_gateway_response.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Response.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Response.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Response.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Response.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.RestApi">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">RestApi</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_key_source=None</em>, <em class="sig-param">binary_media_types=None</em>, <em class="sig-param">body=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">endpoint_configuration=None</em>, <em class="sig-param">minimum_compression_size=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.RestApi" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway REST API.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source of the API key for requests. Valid values are HEADER (default) and AUTHORIZER.</p></li>
<li><p><strong>binary_media_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the REST API</p></li>
<li><p><strong>endpoint_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument defining API endpoint configuration including endpoint type. Defined below.</p></li>
<li><p><strong>minimum_compression_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the REST API</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>endpoint_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">types</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of endpoint types. This resource currently only supports managing a single value. Valid values: <code class="docutils literal notranslate"><span class="pre">EDGE</span></code>, <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>. If unspecified, defaults to <code class="docutils literal notranslate"><span class="pre">EDGE</span></code>. Must be declared as <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code> in non-Commercial partitions. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html">documentation</a> for more information on the difference between edge-optimized and regional APIs.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_rest_api.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_rest_api.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.api_key_source">
<code class="sig-name descname">api_key_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.api_key_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The source of the API key for requests. Valid values are HEADER (default) and AUTHORIZER.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.binary_media_types">
<code class="sig-name descname">binary_media_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.binary_media_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.body">
<code class="sig-name descname">body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.body" title="Permalink to this definition">¶</a></dt>
<dd><p>An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.created_date">
<code class="sig-name descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The creation date of the REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.endpoint_configuration">
<code class="sig-name descname">endpoint_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.endpoint_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument defining API endpoint configuration including endpoint type. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">types</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A list of endpoint types. This resource currently only supports managing a single value. Valid values: <code class="docutils literal notranslate"><span class="pre">EDGE</span></code>, <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>. If unspecified, defaults to <code class="docutils literal notranslate"><span class="pre">EDGE</span></code>. Must be declared as <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code> in non-Commercial partitions. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html">documentation</a> for more information on the difference between edge-optimized and regional APIs.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.execution_arn">
<code class="sig-name descname">execution_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.execution_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The execution ARN part to be used in <cite>``lambda_permission`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">source_arn</span></code>
when allowing API Gateway to invoke a Lambda function,
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j</span></code>, which can be concatenated with allowed stage, method and resource path.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.minimum_compression_size">
<code class="sig-name descname">minimum_compression_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.minimum_compression_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.root_resource_id">
<code class="sig-name descname">root_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.root_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource ID of the REST API’s root</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.RestApi.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.RestApi.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_key_source=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">binary_media_types=None</em>, <em class="sig-param">body=None</em>, <em class="sig-param">created_date=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">endpoint_configuration=None</em>, <em class="sig-param">execution_arn=None</em>, <em class="sig-param">minimum_compression_size=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">root_resource_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RestApi resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source of the API key for requests. Valid values are HEADER (default) and AUTHORIZER.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN)</p></li>
<li><p><strong>binary_media_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An OpenAPI specification that defines the set of routes and integrations to create as part of the REST API.</p></li>
<li><p><strong>created_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The creation date of the REST API</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the REST API</p></li>
<li><p><strong>endpoint_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument defining API endpoint configuration including endpoint type. Defined below.</p></li>
<li><p><strong>execution_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The execution ARN part to be used in <cite>``lambda_permission`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">source_arn</span></code>
when allowing API Gateway to invoke a Lambda function,
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j</span></code>, which can be concatenated with allowed stage, method and resource path.</p></li>
<li><p><strong>minimum_compression_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum response size to compress for the REST API. Integer between -1 and 10485760 (10MB). Setting a value greater than -1 will enable compression, -1 disables compression (default).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the REST API</p></li>
<li><p><strong>root_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource ID of the REST API’s root</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<p>The <strong>endpoint_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">types</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of endpoint types. This resource currently only supports managing a single value. Valid values: <code class="docutils literal notranslate"><span class="pre">EDGE</span></code>, <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code> or <code class="docutils literal notranslate"><span class="pre">PRIVATE</span></code>. If unspecified, defaults to <code class="docutils literal notranslate"><span class="pre">EDGE</span></code>. Must be declared as <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code> in non-Commercial partitions. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/create-regional-api.html">documentation</a> for more information on the difference between edge-optimized and regional APIs.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_rest_api.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_rest_api.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.RestApi.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.RestApi.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.RestApi.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Stage">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">Stage</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_log_settings=None</em>, <em class="sig-param">cache_cluster_enabled=None</em>, <em class="sig-param">cache_cluster_size=None</em>, <em class="sig-param">client_certificate_id=None</em>, <em class="sig-param">deployment=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">documentation_version=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">stage_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">variables=None</em>, <em class="sig-param">xray_tracing_enabled=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Stage" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Stage.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_log_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enables access logs for the API stage. Detailed below.</p></li>
<li><p><strong>cache_cluster_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether a cache cluster is enabled for the stage</p></li>
<li><p><strong>cache_cluster_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The size of the cache cluster for the stage, if enabled.
Allowed values include <code class="docutils literal notranslate"><span class="pre">0.5</span></code>, <code class="docutils literal notranslate"><span class="pre">1.6</span></code>, <code class="docutils literal notranslate"><span class="pre">6.1</span></code>, <code class="docutils literal notranslate"><span class="pre">13.5</span></code>, <code class="docutils literal notranslate"><span class="pre">28.4</span></code>, <code class="docutils literal notranslate"><span class="pre">58.2</span></code>, <code class="docutils literal notranslate"><span class="pre">118</span></code> and <code class="docutils literal notranslate"><span class="pre">237</span></code>.</p></li>
<li><p><strong>client_certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of a client certificate for the stage.</p></li>
<li><p><strong>deployment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the deployment that the stage points to</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the stage</p></li>
<li><p><strong>documentation_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the associated API documentation</p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
<li><p><strong>stage_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stage</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map that defines the stage variables</p></li>
<li><p><strong>xray_tracing_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether active tracing with X-ray is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>access_log_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">destinationArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the log group to send the logs to. Automatically removes trailing <code class="docutils literal notranslate"><span class="pre">:*</span></code> if present.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The formatting and values recorded in the logs. 
For more information on configuring the log format rules visit the AWS <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html">documentation</a></p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_stage.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_stage.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.access_log_settings">
<code class="sig-name descname">access_log_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.access_log_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables access logs for the API stage. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">destinationArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ARN of the log group to send the logs to. Automatically removes trailing <code class="docutils literal notranslate"><span class="pre">:*</span></code> if present.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The formatting and values recorded in the logs. 
For more information on configuring the log format rules visit the AWS <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html">documentation</a></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.cache_cluster_enabled">
<code class="sig-name descname">cache_cluster_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.cache_cluster_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether a cache cluster is enabled for the stage</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.cache_cluster_size">
<code class="sig-name descname">cache_cluster_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.cache_cluster_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the cache cluster for the stage, if enabled.
Allowed values include <code class="docutils literal notranslate"><span class="pre">0.5</span></code>, <code class="docutils literal notranslate"><span class="pre">1.6</span></code>, <code class="docutils literal notranslate"><span class="pre">6.1</span></code>, <code class="docutils literal notranslate"><span class="pre">13.5</span></code>, <code class="docutils literal notranslate"><span class="pre">28.4</span></code>, <code class="docutils literal notranslate"><span class="pre">58.2</span></code>, <code class="docutils literal notranslate"><span class="pre">118</span></code> and <code class="docutils literal notranslate"><span class="pre">237</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.client_certificate_id">
<code class="sig-name descname">client_certificate_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.client_certificate_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of a client certificate for the stage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.deployment">
<code class="sig-name descname">deployment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the deployment that the stage points to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the stage</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.documentation_version">
<code class="sig-name descname">documentation_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.documentation_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the associated API documentation</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.execution_arn">
<code class="sig-name descname">execution_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.execution_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The execution ARN to be used in <cite>``lambda_permission`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">source_arn</span></code>
when allowing API Gateway to invoke a Lambda function,
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.invoke_url">
<code class="sig-name descname">invoke_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.invoke_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to invoke the API pointing to the stage,
e.g. <code class="docutils literal notranslate"><span class="pre">https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.rest_api">
<code class="sig-name descname">rest_api</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the associated REST API</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.stage_name">
<code class="sig-name descname">stage_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.stage_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the stage</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.variables">
<code class="sig-name descname">variables</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.variables" title="Permalink to this definition">¶</a></dt>
<dd><p>A map that defines the stage variables</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.Stage.xray_tracing_enabled">
<code class="sig-name descname">xray_tracing_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.Stage.xray_tracing_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether active tracing with X-ray is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Stage.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_log_settings=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">cache_cluster_enabled=None</em>, <em class="sig-param">cache_cluster_size=None</em>, <em class="sig-param">client_certificate_id=None</em>, <em class="sig-param">deployment=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">documentation_version=None</em>, <em class="sig-param">execution_arn=None</em>, <em class="sig-param">invoke_url=None</em>, <em class="sig-param">rest_api=None</em>, <em class="sig-param">stage_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">variables=None</em>, <em class="sig-param">xray_tracing_enabled=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Stage.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Stage resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_log_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enables access logs for the API stage. Detailed below.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN)</p></li>
<li><p><strong>cache_cluster_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether a cache cluster is enabled for the stage</p></li>
<li><p><strong>cache_cluster_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The size of the cache cluster for the stage, if enabled.
Allowed values include <code class="docutils literal notranslate"><span class="pre">0.5</span></code>, <code class="docutils literal notranslate"><span class="pre">1.6</span></code>, <code class="docutils literal notranslate"><span class="pre">6.1</span></code>, <code class="docutils literal notranslate"><span class="pre">13.5</span></code>, <code class="docutils literal notranslate"><span class="pre">28.4</span></code>, <code class="docutils literal notranslate"><span class="pre">58.2</span></code>, <code class="docutils literal notranslate"><span class="pre">118</span></code> and <code class="docutils literal notranslate"><span class="pre">237</span></code>.</p></li>
<li><p><strong>client_certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of a client certificate for the stage.</p></li>
<li><p><strong>deployment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the deployment that the stage points to</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the stage</p></li>
<li><p><strong>documentation_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of the associated API documentation</p></li>
<li><p><strong>execution_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The execution ARN to be used in <cite>``lambda_permission`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">source_arn</span></code>
when allowing API Gateway to invoke a Lambda function,
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:execute-api:eu-west-2:123456789012:z4675bid1j/prod</span></code></p></li>
<li><p><strong>invoke_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to invoke the API pointing to the stage,
e.g. <code class="docutils literal notranslate"><span class="pre">https://z4675bid1j.execute-api.eu-west-2.amazonaws.com/prod</span></code></p></li>
<li><p><strong>rest_api</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the associated REST API</p></li>
<li><p><strong>stage_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stage</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map that defines the stage variables</p></li>
<li><p><strong>xray_tracing_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether active tracing with X-ray is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>access_log_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">destinationArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the log group to send the logs to. Automatically removes trailing <code class="docutils literal notranslate"><span class="pre">:*</span></code> if present.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The formatting and values recorded in the logs. 
For more information on configuring the log format rules visit the AWS <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html">documentation</a></p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_stage.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_stage.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.Stage.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Stage.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.Stage.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.Stage.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.UsagePlan">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">UsagePlan</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_stages=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">product_code=None</em>, <em class="sig-param">quota_settings=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">throttle_settings=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Usage Plan.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_stages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The associated API stages of the usage plan.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of a usage plan.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the usage plan.</p></li>
<li><p><strong>product_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.</p></li>
<li><p><strong>quota_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The quota settings of the usage plan.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>throttle_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The throttling limits of the usage plan.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>api_stages</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apiId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - API Id of the associated API stage in a usage plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - API stage name of the associated API stage in a usage plan.</p></li>
</ul>
<p>The <strong>quota_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">limit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of requests that can be made in a given time period.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of requests subtracted from the given limit in the initial time period.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time period in which the limit applies. Valid values are “DAY”, “WEEK” or “MONTH”.</p></li>
</ul>
<p>The <strong>throttle_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">burstLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rateLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The API request steady-state rate limit.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_usage_plan.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_usage_plan.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlan.api_stages">
<code class="sig-name descname">api_stages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.api_stages" title="Permalink to this definition">¶</a></dt>
<dd><p>The associated API stages of the usage plan.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apiId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - API Id of the associated API stage in a usage plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - API stage name of the associated API stage in a usage plan.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlan.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlan.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of a usage plan.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlan.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the usage plan.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlan.product_code">
<code class="sig-name descname">product_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.product_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlan.quota_settings">
<code class="sig-name descname">quota_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.quota_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The quota settings of the usage plan.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">limit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of requests that can be made in a given time period.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offset</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of requests subtracted from the given limit in the initial time period.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The time period in which the limit applies. Valid values are “DAY”, “WEEK” or “MONTH”.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlan.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlan.throttle_settings">
<code class="sig-name descname">throttle_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.throttle_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The throttling limits of the usage plan.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">burstLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rateLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The API request steady-state rate limit.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.UsagePlan.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_stages=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">product_code=None</em>, <em class="sig-param">quota_settings=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">throttle_settings=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UsagePlan resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_stages</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The associated API stages of the usage plan.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN)</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of a usage plan.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the usage plan.</p></li>
<li><p><strong>product_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.</p></li>
<li><p><strong>quota_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The quota settings of the usage plan.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>throttle_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The throttling limits of the usage plan.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>api_stages</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apiId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - API Id of the associated API stage in a usage plan.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - API stage name of the associated API stage in a usage plan.</p></li>
</ul>
<p>The <strong>quota_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">limit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of requests that can be made in a given time period.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offset</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of requests subtracted from the given limit in the initial time period.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time period in which the limit applies. Valid values are “DAY”, “WEEK” or “MONTH”.</p></li>
</ul>
<p>The <strong>throttle_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">burstLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rateLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The API request steady-state rate limit.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_usage_plan.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_usage_plan.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.UsagePlan.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.UsagePlan.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlan.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.UsagePlanKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">UsagePlanKey</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">key_type=None</em>, <em class="sig-param">usage_plan_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway Usage Plan Key.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the API key resource.</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the API key resource. Currently, the valid key type is API_KEY.</p></li>
<li><p><strong>usage_plan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of the usage plan resource representing to associate the key to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_usage_plan_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_usage_plan_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlanKey.key_id">
<code class="sig-name descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the API key resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlanKey.key_type">
<code class="sig-name descname">key_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the API key resource. Currently, the valid key type is API_KEY.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlanKey.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a usage plan key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlanKey.usage_plan_id">
<code class="sig-name descname">usage_plan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.usage_plan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of the usage plan resource representing to associate the key to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.UsagePlanKey.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of a usage plan key.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.UsagePlanKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key_id=None</em>, <em class="sig-param">key_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">usage_plan_id=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UsagePlanKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the API key resource.</p></li>
<li><p><strong>key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the API key resource. Currently, the valid key type is API_KEY.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a usage plan key.</p></li>
<li><p><strong>usage_plan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of the usage plan resource representing to associate the key to.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of a usage plan key.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_usage_plan_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_usage_plan_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.UsagePlanKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.UsagePlanKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.UsagePlanKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.VpcLink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">VpcLink</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.VpcLink" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an API Gateway VPC Link.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the VPC link.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name used to label and identify the VPC link.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>target_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_vpc_link.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_vpc_link.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.apigateway.VpcLink.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.VpcLink.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the VPC link.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.VpcLink.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.VpcLink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name used to label and identify the VPC link.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.VpcLink.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.VpcLink.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigateway.VpcLink.target_arn">
<code class="sig-name descname">target_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigateway.VpcLink.target_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.VpcLink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.VpcLink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VpcLink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the VPC link.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name used to label and identify the VPC link.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
<li><p><strong>target_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_vpc_link.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_vpc_link.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigateway.VpcLink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.VpcLink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.VpcLink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.VpcLink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigateway.get_key">
<code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">get_key</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.get_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the name and value of a pre-existing API Key, for
example to supply credentials for a dependency microservice.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>id</strong> (<em>str</em>) – The ID of the API Key to look up.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/api_gateway_api_key.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/api_gateway_api_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.apigateway.get_resource">
<code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">get_resource</code><span class="sig-paren">(</span><em class="sig-param">path=None</em>, <em class="sig-param">rest_api_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.get_resource" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the id of a Resource in API Gateway. 
To fetch the Resource, you must provide the REST API id as well as the full path.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>path</strong> (<em>str</em>) – The full path of the resource.  If no path is found, an error will be returned.</p></li>
<li><p><strong>rest_api_id</strong> (<em>str</em>) – The REST API id that owns the resource. If no REST API is found, an error will be returned.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/api_gateway_resource.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/api_gateway_resource.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.apigateway.get_rest_api">
<code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">get_rest_api</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.get_rest_api" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the id and root_resource_id of a REST API in
API Gateway. To fetch the REST API you must provide a name to match against. 
As there is no unique name constraint on REST APIs this data source will 
error if there is more than one match.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the REST API to look up. If no REST API is found with this name, an error will be returned. 
If multiple REST APIs are found with this name, an error will be returned.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/api_gateway_rest_api.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/api_gateway_rest_api.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.apigateway.get_vpc_link">
<code class="sig-prename descclassname">pulumi_aws.apigateway.</code><code class="sig-name descname">get_vpc_link</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigateway.get_vpc_link" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the id of a VPC Link in
API Gateway. To fetch the VPC Link you must provide a name to match against. 
As there is no unique name constraint on API Gateway VPC Links this data source will 
error if there is more than one match.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the API Gateway VPC Link to look up. If no API Gateway VPC Link is found with this name, an error will be returned. 
If multiple API Gateway VPC Links are found with this name, an error will be returned.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/api_gateway_vpc_link.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/api_gateway_vpc_link.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
