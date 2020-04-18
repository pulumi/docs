---
title: Module apigatewayv2
title_tag: Module apigatewayv2 | Package pulumi_aws | Python SDK
linktitle: apigatewayv2
notitle: true
---

<div class="section" id="apigatewayv2">
<h1>apigatewayv2<a class="headerlink" href="#apigatewayv2" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.apigatewayv2"></span><dl class="class">
<dt id="pulumi_aws.apigatewayv2.Api">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">Api</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_key_selection_expression=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protocol_type=None</em>, <em class="sig-param">route_selection_expression=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Amazon API Gateway Version 2 API.</p>
<blockquote>
<div><p><strong>Note:</strong> Amazon API Gateway Version 2 resources are used for creating and deploying WebSocket and HTTP APIs. To create and deploy REST APIs, use Amazon API Gateway Version 1.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions">API key selection expression</a>.
Valid values: <code class="docutils literal notranslate"><span class="pre">$context.authorizer.usageIdentifierKey</span></code>, <code class="docutils literal notranslate"><span class="pre">$request.header.x-api-key</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">$request.header.x-api-key</span></code>.
Applicable for WebSocket APIs.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the API.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API.</p></li>
<li><p><strong>protocol_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API protocol. Valid values: <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">WEBSOCKET</span></code>.</p></li>
<li><p><strong>route_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-selection-expressions">route selection expression</a> for the API.
Defaults to <code class="docutils literal notranslate"><span class="pre">$request.method</span> <span class="pre">$request.path</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the API.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A version identifier for the API.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Api.api_endpoint">
<code class="sig-name descname">api_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.api_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the API, of the form <code class="docutils literal notranslate"><span class="pre">{api-id}.execute-api.{region}.amazonaws.com</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Api.api_key_selection_expression">
<code class="sig-name descname">api_key_selection_expression</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.api_key_selection_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>An <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions">API key selection expression</a>.
Valid values: <code class="docutils literal notranslate"><span class="pre">$context.authorizer.usageIdentifierKey</span></code>, <code class="docutils literal notranslate"><span class="pre">$request.header.x-api-key</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">$request.header.x-api-key</span></code>.
Applicable for WebSocket APIs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Api.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Api.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Api.execution_arn">
<code class="sig-name descname">execution_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.execution_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN prefix to be used in an <cite>``lambda.Permission`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">source_arn</span></code> attribute
or in an <cite>``iam.Policy`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_policy.html">https://www.terraform.io/docs/providers/aws/r/iam_policy.html</a>&gt;`_ to authorize access to the <cite>``&#64;connections`</cite> API &lt;<a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html">https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html</a>&gt;`_.
See the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-control-access-iam.html">Amazon API Gateway Developer Guide</a> for details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Api.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Api.protocol_type">
<code class="sig-name descname">protocol_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.protocol_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The API protocol. Valid values: <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">WEBSOCKET</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Api.route_selection_expression">
<code class="sig-name descname">route_selection_expression</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.route_selection_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-selection-expressions">route selection expression</a> for the API.
Defaults to <code class="docutils literal notranslate"><span class="pre">$request.method</span> <span class="pre">$request.path</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Api.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Api.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.version" title="Permalink to this definition">¶</a></dt>
<dd><p>A version identifier for the API.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigatewayv2.Api.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_endpoint=None</em>, <em class="sig-param">api_key_selection_expression=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">execution_arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protocol_type=None</em>, <em class="sig-param">route_selection_expression=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Api resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the API, of the form <code class="docutils literal notranslate"><span class="pre">{api-id}.execute-api.{region}.amazonaws.com</span></code>.</p></li>
<li><p><strong>api_key_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>An <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions">API key selection expression</a>.
Valid values: <code class="docutils literal notranslate"><span class="pre">$context.authorizer.usageIdentifierKey</span></code>, <code class="docutils literal notranslate"><span class="pre">$request.header.x-api-key</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">$request.header.x-api-key</span></code>.
Applicable for WebSocket APIs.</p>
</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the API.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the API.</p></li>
<li><p><strong>execution_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ARN prefix to be used in an <cite>``lambda.Permission`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">source_arn</span></code> attribute
or in an <cite>``iam.Policy`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_policy.html">https://www.terraform.io/docs/providers/aws/r/iam_policy.html</a>&gt;`_ to authorize access to the <cite>``&#64;connections`</cite> API &lt;<a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html">https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html</a>&gt;`_.
See the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-control-access-iam.html">Amazon API Gateway Developer Guide</a> for details.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API.</p></li>
<li><p><strong>protocol_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API protocol. Valid values: <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">WEBSOCKET</span></code>.</p></li>
<li><p><strong>route_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-selection-expressions">route selection expression</a> for the API.
Defaults to <code class="docutils literal notranslate"><span class="pre">$request.method</span> <span class="pre">$request.path</span></code>.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the API.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A version identifier for the API.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigatewayv2.Api.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Api.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Authorizer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">Authorizer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">authorizer_credentials_arn=None</em>, <em class="sig-param">authorizer_type=None</em>, <em class="sig-param">authorizer_uri=None</em>, <em class="sig-param">identity_sources=None</em>, <em class="sig-param">jwt_configuration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Amazon API Gateway Version 2 authorizer.
More information can be found in the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html">Amazon API Gateway Developer Guide</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>authorizer_credentials_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The required credentials as an IAM role for API Gateway to invoke the authorizer.
Supported only for <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers.</p></li>
<li><p><strong>authorizer_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorizer type. Valid values: <code class="docutils literal notranslate"><span class="pre">JWT</span></code>, <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.
For WebSocket APIs, specify <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> for a Lambda function using incoming request parameters.
For HTTP APIs, specify <code class="docutils literal notranslate"><span class="pre">JWT</span></code> to use JSON Web Tokens.</p></li>
<li><p><strong>authorizer_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorizer’s Uniform Resource Identifier (URI).
For <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers this must be a well-formed Lambda function URI, such as the <code class="docutils literal notranslate"><span class="pre">invoke_arn</span></code> attribute of the <cite>``lambda.Function`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_function.html">https://www.terraform.io/docs/providers/aws/r/lambda_function.html</a>&gt;`_ resource.
Supported only for <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers.</p></li>
<li><p><strong>identity_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The identity sources for which authorization is requested.
For <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers the value is a list of one or more mapping expressions of the specified request parameters.
For <code class="docutils literal notranslate"><span class="pre">JWT</span></code> authorizers the single entry specifies where to extract the JSON Web Token (JWT) from inbound requests.</p></li>
<li><p><strong>jwt_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration of a JWT authorizer. Required for the <code class="docutils literal notranslate"><span class="pre">JWT</span></code> authorizer type.
Supported only for HTTP APIs.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the authorizer.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>jwt_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audiences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of the intended recipients of the JWT. A valid JWT must provide an aud that matches at least one entry in this list.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The base domain of the identity provider that issues JSON Web Tokens, such as the <code class="docutils literal notranslate"><span class="pre">endpoint</span></code> attribute of the <cite>``cognito.UserPool`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/cognito_user_pool.html">https://www.terraform.io/docs/providers/aws/r/cognito_user_pool.html</a>&gt;`_ resource.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Authorizer.api_id">
<code class="sig-name descname">api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Authorizer.authorizer_credentials_arn">
<code class="sig-name descname">authorizer_credentials_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.authorizer_credentials_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The required credentials as an IAM role for API Gateway to invoke the authorizer.
Supported only for <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Authorizer.authorizer_type">
<code class="sig-name descname">authorizer_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.authorizer_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorizer type. Valid values: <code class="docutils literal notranslate"><span class="pre">JWT</span></code>, <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.
For WebSocket APIs, specify <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> for a Lambda function using incoming request parameters.
For HTTP APIs, specify <code class="docutils literal notranslate"><span class="pre">JWT</span></code> to use JSON Web Tokens.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Authorizer.authorizer_uri">
<code class="sig-name descname">authorizer_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.authorizer_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorizer’s Uniform Resource Identifier (URI).
For <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers this must be a well-formed Lambda function URI, such as the <code class="docutils literal notranslate"><span class="pre">invoke_arn</span></code> attribute of the <cite>``lambda.Function`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_function.html">https://www.terraform.io/docs/providers/aws/r/lambda_function.html</a>&gt;`_ resource.
Supported only for <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Authorizer.identity_sources">
<code class="sig-name descname">identity_sources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.identity_sources" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity sources for which authorization is requested.
For <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers the value is a list of one or more mapping expressions of the specified request parameters.
For <code class="docutils literal notranslate"><span class="pre">JWT</span></code> authorizers the single entry specifies where to extract the JSON Web Token (JWT) from inbound requests.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Authorizer.jwt_configuration">
<code class="sig-name descname">jwt_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.jwt_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration of a JWT authorizer. Required for the <code class="docutils literal notranslate"><span class="pre">JWT</span></code> authorizer type.
Supported only for HTTP APIs.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audiences</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of the intended recipients of the JWT. A valid JWT must provide an aud that matches at least one entry in this list.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The base domain of the identity provider that issues JSON Web Tokens, such as the <code class="docutils literal notranslate"><span class="pre">endpoint</span></code> attribute of the <cite>``cognito.UserPool`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/cognito_user_pool.html">https://www.terraform.io/docs/providers/aws/r/cognito_user_pool.html</a>&gt;`_ resource.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Authorizer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the authorizer.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigatewayv2.Authorizer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">authorizer_credentials_arn=None</em>, <em class="sig-param">authorizer_type=None</em>, <em class="sig-param">authorizer_uri=None</em>, <em class="sig-param">identity_sources=None</em>, <em class="sig-param">jwt_configuration=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Authorizer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>authorizer_credentials_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The required credentials as an IAM role for API Gateway to invoke the authorizer.
Supported only for <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers.</p></li>
<li><p><strong>authorizer_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorizer type. Valid values: <code class="docutils literal notranslate"><span class="pre">JWT</span></code>, <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.
For WebSocket APIs, specify <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> for a Lambda function using incoming request parameters.
For HTTP APIs, specify <code class="docutils literal notranslate"><span class="pre">JWT</span></code> to use JSON Web Tokens.</p></li>
<li><p><strong>authorizer_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorizer’s Uniform Resource Identifier (URI).
For <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers this must be a well-formed Lambda function URI, such as the <code class="docutils literal notranslate"><span class="pre">invoke_arn</span></code> attribute of the <cite>``lambda.Function`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_function.html">https://www.terraform.io/docs/providers/aws/r/lambda_function.html</a>&gt;`_ resource.
Supported only for <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers.</p></li>
<li><p><strong>identity_sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The identity sources for which authorization is requested.
For <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers the value is a list of one or more mapping expressions of the specified request parameters.
For <code class="docutils literal notranslate"><span class="pre">JWT</span></code> authorizers the single entry specifies where to extract the JSON Web Token (JWT) from inbound requests.</p></li>
<li><p><strong>jwt_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The configuration of a JWT authorizer. Required for the <code class="docutils literal notranslate"><span class="pre">JWT</span></code> authorizer type.
Supported only for HTTP APIs.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the authorizer.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>jwt_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audiences</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of the intended recipients of the JWT. A valid JWT must provide an aud that matches at least one entry in this list.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The base domain of the identity provider that issues JSON Web Tokens, such as the <code class="docutils literal notranslate"><span class="pre">endpoint</span></code> attribute of the <cite>``cognito.UserPool`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/cognito_user_pool.html">https://www.terraform.io/docs/providers/aws/r/cognito_user_pool.html</a>&gt;`_ resource.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigatewayv2.Authorizer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Authorizer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Integration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">Integration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">connection_id=None</em>, <em class="sig-param">connection_type=None</em>, <em class="sig-param">content_handling_strategy=None</em>, <em class="sig-param">credentials_arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">integration_method=None</em>, <em class="sig-param">integration_type=None</em>, <em class="sig-param">integration_uri=None</em>, <em class="sig-param">passthrough_behavior=None</em>, <em class="sig-param">payload_format_version=None</em>, <em class="sig-param">request_templates=None</em>, <em class="sig-param">template_selection_expression=None</em>, <em class="sig-param">timeout_milliseconds=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Amazon API Gateway Version 2 integration.
More information can be found in the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html">Amazon API Gateway Developer Guide</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC link for a private integration. Supported only for HTTP APIs.</p></li>
<li><p><strong>connection_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the network connection to the integration endpoint. Valid values: <code class="docutils literal notranslate"><span class="pre">INTERNET</span></code>, <code class="docutils literal notranslate"><span class="pre">VPC_LINK</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">INTERNET</span></code>.</p></li>
<li><p><strong>content_handling_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How to handle response payload content type conversions. Valid values: <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_BINARY</span></code>, <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_TEXT</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><strong>credentials_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The credentials required for the integration, if any.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the integration.</p></li>
<li><p><strong>integration_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration’s HTTP method. Must be specified if <code class="docutils literal notranslate"><span class="pre">integration_type</span></code> is not <code class="docutils literal notranslate"><span class="pre">MOCK</span></code>.</p></li>
<li><p><strong>integration_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration type of an integration.
Valid values: <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code>, <code class="docutils literal notranslate"><span class="pre">MOCK</span></code>.</p></li>
<li><p><strong>integration_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the Lambda function for a Lambda proxy integration, when <code class="docutils literal notranslate"><span class="pre">integration_type</span></code> is <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>.
For an <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service.</p></li>
<li><p><strong>passthrough_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the <code class="docutils literal notranslate"><span class="pre">request_templates</span></code> attribute.
Valid values: <code class="docutils literal notranslate"><span class="pre">WHEN_NO_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">WHEN_NO_TEMPLATES</span></code>, <code class="docutils literal notranslate"><span class="pre">NEVER</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">WHEN_NO_MATCH</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><strong>payload_format_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.proxy-format">format of the payload</a> sent to an integration. Valid values: <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">2.0</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">1.0</span></code>.</p></li>
<li><p><strong>request_templates</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. Supported only for WebSocket APIs.</p></li>
<li><p><strong>template_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions">template selection expression</a> for the integration.</p></li>
<li><p><strong>timeout_milliseconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.api_id">
<code class="sig-name descname">api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.connection_id">
<code class="sig-name descname">connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC link for a private integration. Supported only for HTTP APIs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.connection_type">
<code class="sig-name descname">connection_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.connection_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the network connection to the integration endpoint. Valid values: <code class="docutils literal notranslate"><span class="pre">INTERNET</span></code>, <code class="docutils literal notranslate"><span class="pre">VPC_LINK</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">INTERNET</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.content_handling_strategy">
<code class="sig-name descname">content_handling_strategy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.content_handling_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>How to handle response payload content type conversions. Valid values: <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_BINARY</span></code>, <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_TEXT</span></code>. Supported only for WebSocket APIs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.credentials_arn">
<code class="sig-name descname">credentials_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.credentials_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The credentials required for the integration, if any.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the integration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.integration_method">
<code class="sig-name descname">integration_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.integration_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration’s HTTP method. Must be specified if <code class="docutils literal notranslate"><span class="pre">integration_type</span></code> is not <code class="docutils literal notranslate"><span class="pre">MOCK</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.integration_response_selection_expression">
<code class="sig-name descname">integration_response_selection_expression</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.integration_response_selection_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions">integration response selection expression</a> for the integration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.integration_type">
<code class="sig-name descname">integration_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.integration_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration type of an integration.
Valid values: <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code>, <code class="docutils literal notranslate"><span class="pre">MOCK</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.integration_uri">
<code class="sig-name descname">integration_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.integration_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the Lambda function for a Lambda proxy integration, when <code class="docutils literal notranslate"><span class="pre">integration_type</span></code> is <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>.
For an <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.passthrough_behavior">
<code class="sig-name descname">passthrough_behavior</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.passthrough_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>The pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the <code class="docutils literal notranslate"><span class="pre">request_templates</span></code> attribute.
Valid values: <code class="docutils literal notranslate"><span class="pre">WHEN_NO_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">WHEN_NO_TEMPLATES</span></code>, <code class="docutils literal notranslate"><span class="pre">NEVER</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">WHEN_NO_MATCH</span></code>. Supported only for WebSocket APIs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.payload_format_version">
<code class="sig-name descname">payload_format_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.payload_format_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.proxy-format">format of the payload</a> sent to an integration. Valid values: <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">2.0</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">1.0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.request_templates">
<code class="sig-name descname">request_templates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.request_templates" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. Supported only for WebSocket APIs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.template_selection_expression">
<code class="sig-name descname">template_selection_expression</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.template_selection_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions">template selection expression</a> for the integration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.timeout_milliseconds">
<code class="sig-name descname">timeout_milliseconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.timeout_milliseconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigatewayv2.Integration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">connection_id=None</em>, <em class="sig-param">connection_type=None</em>, <em class="sig-param">content_handling_strategy=None</em>, <em class="sig-param">credentials_arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">integration_method=None</em>, <em class="sig-param">integration_response_selection_expression=None</em>, <em class="sig-param">integration_type=None</em>, <em class="sig-param">integration_uri=None</em>, <em class="sig-param">passthrough_behavior=None</em>, <em class="sig-param">payload_format_version=None</em>, <em class="sig-param">request_templates=None</em>, <em class="sig-param">template_selection_expression=None</em>, <em class="sig-param">timeout_milliseconds=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Integration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC link for a private integration. Supported only for HTTP APIs.</p></li>
<li><p><strong>connection_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the network connection to the integration endpoint. Valid values: <code class="docutils literal notranslate"><span class="pre">INTERNET</span></code>, <code class="docutils literal notranslate"><span class="pre">VPC_LINK</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">INTERNET</span></code>.</p></li>
<li><p><strong>content_handling_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How to handle response payload content type conversions. Valid values: <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_BINARY</span></code>, <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_TEXT</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><strong>credentials_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The credentials required for the integration, if any.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the integration.</p></li>
<li><p><strong>integration_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration’s HTTP method. Must be specified if <code class="docutils literal notranslate"><span class="pre">integration_type</span></code> is not <code class="docutils literal notranslate"><span class="pre">MOCK</span></code>.</p></li>
<li><p><strong>integration_response_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions">integration response selection expression</a> for the integration.</p>
</p></li>
<li><p><strong>integration_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration type of an integration.
Valid values: <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code>, <code class="docutils literal notranslate"><span class="pre">MOCK</span></code>.</p></li>
<li><p><strong>integration_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI of the Lambda function for a Lambda proxy integration, when <code class="docutils literal notranslate"><span class="pre">integration_type</span></code> is <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>.
For an <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service.</p></li>
<li><p><strong>passthrough_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the <code class="docutils literal notranslate"><span class="pre">request_templates</span></code> attribute.
Valid values: <code class="docutils literal notranslate"><span class="pre">WHEN_NO_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">WHEN_NO_TEMPLATES</span></code>, <code class="docutils literal notranslate"><span class="pre">NEVER</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">WHEN_NO_MATCH</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><strong>payload_format_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.proxy-format">format of the payload</a> sent to an integration. Valid values: <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">2.0</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">1.0</span></code>.</p>
</p></li>
<li><p><strong>request_templates</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. Supported only for WebSocket APIs.</p></li>
<li><p><strong>template_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions">template selection expression</a> for the integration.</p>
</p></li>
<li><p><strong>timeout_milliseconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigatewayv2.Integration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Integration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Model">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">Model</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">schema=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Amazon API Gateway Version 2 <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html#models-mappings-models">model</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content-type for the model, for example, <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the model.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the model. Must be alphanumeric.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The schema for the model. This should be a <a class="reference external" href="https://tools.ietf.org/html/draft-zyp-json-schema-04">JSON schema draft 4</a> model.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Model.api_id">
<code class="sig-name descname">api_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Model.content_type">
<code class="sig-name descname">content_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The content-type for the model, for example, <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Model.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the model.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Model.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the model. Must be alphanumeric.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.apigatewayv2.Model.schema">
<code class="sig-name descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The schema for the model. This should be a <a class="reference external" href="https://tools.ietf.org/html/draft-zyp-json-schema-04">JSON schema draft 4</a> model.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigatewayv2.Model.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">api_id=None</em>, <em class="sig-param">content_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">schema=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Model resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The content-type for the model, for example, <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the model.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the model. Must be alphanumeric.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The schema for the model. This should be a <a class="reference external" href="https://tools.ietf.org/html/draft-zyp-json-schema-04">JSON schema draft 4</a> model.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.apigatewayv2.Model.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Model.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
