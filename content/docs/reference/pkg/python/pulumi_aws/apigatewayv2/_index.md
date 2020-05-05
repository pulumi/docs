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
<span class="target" id="module-pulumi_aws.apigatewayv2"></span><dl class="py class">
<dt id="pulumi_aws.apigatewayv2.Api">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">Api</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cors_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>cors_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The cross-origin resource sharing (CORS) <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html">configuration</a>. Applicable for HTTP APIs.</p></li>
<li><p><strong>credentials_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Part of <em>quick create</em>. Specifies any credentials required for the integration. Applicable for HTTP APIs.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the API.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API.</p></li>
<li><p><strong>protocol_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API protocol. Valid values: <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">WEBSOCKET</span></code>.</p></li>
<li><p><strong>route_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Part of <em>quick create</em>. Specifies any <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-routes.html">route key</a>. Applicable for HTTP APIs.</p></li>
<li><p><strong>route_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-selection-expressions">route selection expression</a> for the API.
Defaults to <code class="docutils literal notranslate"><span class="pre">$request.method</span> <span class="pre">$request.path</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the API.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Part of <em>quick create</em>. Quick create produces an API with an integration, a default catch-all route, and a default stage which is configured to automatically deploy changes.
For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN.
The type of the integration will be <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code> or <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>, respectively. Applicable for HTTP APIs.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A version identifier for the API.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cors_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether credentials are included in the CORS request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of allowed HTTP headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of allowed HTTP methods.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of allowed origins.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exposeHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of exposed HTTP headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of seconds that the browser should cache preflight request results.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Api.api_endpoint">
<code class="sig-name descname">api_endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.api_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the API, of the form <code class="docutils literal notranslate"><span class="pre">{api-id}.execute-api.{region}.amazonaws.com</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Api.api_key_selection_expression">
<code class="sig-name descname">api_key_selection_expression</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.api_key_selection_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>An <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions">API key selection expression</a>.
Valid values: <code class="docutils literal notranslate"><span class="pre">$context.authorizer.usageIdentifierKey</span></code>, <code class="docutils literal notranslate"><span class="pre">$request.header.x-api-key</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">$request.header.x-api-key</span></code>.
Applicable for WebSocket APIs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Api.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the API.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Api.cors_configuration">
<code class="sig-name descname">cors_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.cors_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The cross-origin resource sharing (CORS) <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html">configuration</a>. Applicable for HTTP APIs.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether credentials are included in the CORS request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of allowed HTTP headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of allowed HTTP methods.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of allowed origins.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exposeHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The set of exposed HTTP headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAge</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of seconds that the browser should cache preflight request results.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Api.credentials_arn">
<code class="sig-name descname">credentials_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.credentials_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Part of <em>quick create</em>. Specifies any credentials required for the integration. Applicable for HTTP APIs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Api.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the API.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Api.execution_arn">
<code class="sig-name descname">execution_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.execution_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN prefix to be used in an <cite>``lambda.Permission`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">source_arn</span></code> attribute
or in an <cite>``iam.Policy`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_policy.html">https://www.terraform.io/docs/providers/aws/r/iam_policy.html</a>&gt;`_ to authorize access to the <cite>``&#64;connections`</cite> API &lt;<a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html">https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html</a>&gt;`_.
See the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-control-access-iam.html">Amazon API Gateway Developer Guide</a> for details.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Api.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the API.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Api.protocol_type">
<code class="sig-name descname">protocol_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.protocol_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The API protocol. Valid values: <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">WEBSOCKET</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Api.route_key">
<code class="sig-name descname">route_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.route_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Part of <em>quick create</em>. Specifies any <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-routes.html">route key</a>. Applicable for HTTP APIs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Api.route_selection_expression">
<code class="sig-name descname">route_selection_expression</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.route_selection_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-selection-expressions">route selection expression</a> for the API.
Defaults to <code class="docutils literal notranslate"><span class="pre">$request.method</span> <span class="pre">$request.path</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Api.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the API.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Api.target">
<code class="sig-name descname">target</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.target" title="Permalink to this definition">¶</a></dt>
<dd><p>Part of <em>quick create</em>. Quick create produces an API with an integration, a default catch-all route, and a default stage which is configured to automatically deploy changes.
For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN.
The type of the integration will be <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code> or <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>, respectively. Applicable for HTTP APIs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Api.version">
<code class="sig-name descname">version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.version" title="Permalink to this definition">¶</a></dt>
<dd><p>A version identifier for the API.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.Api.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cors_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">execution_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>cors_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>The cross-origin resource sharing (CORS) <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html">configuration</a>. Applicable for HTTP APIs.</p>
</p></li>
<li><p><strong>credentials_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Part of <em>quick create</em>. Specifies any credentials required for the integration. Applicable for HTTP APIs.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the API.</p></li>
<li><p><strong>execution_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ARN prefix to be used in an <cite>``lambda.Permission`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">source_arn</span></code> attribute
or in an <cite>``iam.Policy`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_policy.html">https://www.terraform.io/docs/providers/aws/r/iam_policy.html</a>&gt;`_ to authorize access to the <cite>``&#64;connections`</cite> API &lt;<a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html">https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html</a>&gt;`_.
See the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-control-access-iam.html">Amazon API Gateway Developer Guide</a> for details.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the API.</p></li>
<li><p><strong>protocol_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API protocol. Valid values: <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">WEBSOCKET</span></code>.</p></li>
<li><p><strong>route_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Part of <em>quick create</em>. Specifies any <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-routes.html">route key</a>. Applicable for HTTP APIs.</p>
</p></li>
<li><p><strong>route_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-selection-expressions">route selection expression</a> for the API.
Defaults to <code class="docutils literal notranslate"><span class="pre">$request.method</span> <span class="pre">$request.path</span></code>.</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the API.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Part of <em>quick create</em>. Quick create produces an API with an integration, a default catch-all route, and a default stage which is configured to automatically deploy changes.
For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN.
The type of the integration will be <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code> or <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>, respectively. Applicable for HTTP APIs.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A version identifier for the API.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cors_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowCredentials</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether credentials are included in the CORS request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of allowed HTTP headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowMethods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of allowed HTTP methods.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">allowOrigins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of allowed origins.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exposeHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The set of exposed HTTP headers.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxAge</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of seconds that the browser should cache preflight request results.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.Api.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Api.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Api.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.ApiMapping">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">ApiMapping</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_mapping_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.ApiMapping" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Amazon API Gateway Version 2 API mapping.
More information can be found in the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html">Amazon API Gateway Developer Guide</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>api_mapping_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html">API mapping key</a>.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name. Use the <cite>``apigatewayv2.DomainName`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_domain_name.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_domain_name.html</a>&gt;`_ resource to configure a domain name.</p></li>
<li><p><strong>stage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API stage. Use the <cite>``apigatewayv2.Stage`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_stage.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_stage.html</a>&gt;`_ resource to configure an API stage.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.ApiMapping.api_id">
<code class="sig-name descname">api_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.ApiMapping.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.ApiMapping.api_mapping_key">
<code class="sig-name descname">api_mapping_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.ApiMapping.api_mapping_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html">API mapping key</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.ApiMapping.domain_name">
<code class="sig-name descname">domain_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.ApiMapping.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain name. Use the <cite>``apigatewayv2.DomainName`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_domain_name.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_domain_name.html</a>&gt;`_ resource to configure a domain name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.ApiMapping.stage">
<code class="sig-name descname">stage</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.ApiMapping.stage" title="Permalink to this definition">¶</a></dt>
<dd><p>The API stage. Use the <cite>``apigatewayv2.Stage`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_stage.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_stage.html</a>&gt;`_ resource to configure an API stage.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.ApiMapping.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_mapping_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stage</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.ApiMapping.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApiMapping resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>api_mapping_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-mapping-template-reference.html">API mapping key</a>.</p>
</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name. Use the <cite>``apigatewayv2.DomainName`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_domain_name.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_domain_name.html</a>&gt;`_ resource to configure a domain name.</p></li>
<li><p><strong>stage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API stage. Use the <cite>``apigatewayv2.Stage`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_stage.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_stage.html</a>&gt;`_ resource to configure an API stage.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.ApiMapping.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.ApiMapping.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.ApiMapping.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.ApiMapping.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Authorizer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">Authorizer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorizer_credentials_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorizer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorizer_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwt_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer" title="Permalink to this definition">¶</a></dt>
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
<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Authorizer.api_id">
<code class="sig-name descname">api_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Authorizer.authorizer_credentials_arn">
<code class="sig-name descname">authorizer_credentials_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.authorizer_credentials_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The required credentials as an IAM role for API Gateway to invoke the authorizer.
Supported only for <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Authorizer.authorizer_type">
<code class="sig-name descname">authorizer_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.authorizer_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorizer type. Valid values: <code class="docutils literal notranslate"><span class="pre">JWT</span></code>, <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code>.
For WebSocket APIs, specify <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> for a Lambda function using incoming request parameters.
For HTTP APIs, specify <code class="docutils literal notranslate"><span class="pre">JWT</span></code> to use JSON Web Tokens.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Authorizer.authorizer_uri">
<code class="sig-name descname">authorizer_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.authorizer_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorizer’s Uniform Resource Identifier (URI).
For <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers this must be a well-formed Lambda function URI, such as the <code class="docutils literal notranslate"><span class="pre">invoke_arn</span></code> attribute of the <cite>``lambda.Function`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_function.html">https://www.terraform.io/docs/providers/aws/r/lambda_function.html</a>&gt;`_ resource.
Supported only for <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Authorizer.identity_sources">
<code class="sig-name descname">identity_sources</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.identity_sources" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity sources for which authorization is requested.
For <code class="docutils literal notranslate"><span class="pre">REQUEST</span></code> authorizers the value is a list of one or more mapping expressions of the specified request parameters.
For <code class="docutils literal notranslate"><span class="pre">JWT</span></code> authorizers the single entry specifies where to extract the JSON Web Token (JWT) from inbound requests.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Authorizer.jwt_configuration">
<code class="sig-name descname">jwt_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.jwt_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration of a JWT authorizer. Required for the <code class="docutils literal notranslate"><span class="pre">JWT</span></code> authorizer type.
Supported only for HTTP APIs.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audiences</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of the intended recipients of the JWT. A valid JWT must provide an aud that matches at least one entry in this list.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The base domain of the identity provider that issues JSON Web Tokens, such as the <code class="docutils literal notranslate"><span class="pre">endpoint</span></code> attribute of the <cite>``cognito.UserPool`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/cognito_user_pool.html">https://www.terraform.io/docs/providers/aws/r/cognito_user_pool.html</a>&gt;`_ resource.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Authorizer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the authorizer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.Authorizer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorizer_credentials_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorizer_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorizer_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jwt_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.Authorizer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Authorizer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Authorizer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Deployment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">Deployment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Deployment" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Amazon API Gateway Version 2 deployment.
More information can be found in the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html">Amazon API Gateway Developer Guide</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> Creating a deployment for an API requires at least one <code class="docutils literal notranslate"><span class="pre">apigatewayv2.Route</span></code> resource associated with that API.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the deployment resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Deployment.api_id">
<code class="sig-name descname">api_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Deployment.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Deployment.auto_deployed">
<code class="sig-name descname">auto_deployed</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Deployment.auto_deployed" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the deployment was automatically released.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Deployment.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Deployment.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the deployment resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.Deployment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_deployed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Deployment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Deployment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>auto_deployed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the deployment was automatically released.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the deployment resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.Deployment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Deployment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Deployment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Deployment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.DomainName">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">DomainName</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.DomainName" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Amazon API Gateway Version 2 domain name.
More information can be found in the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html">Amazon API Gateway Developer Guide</a>.</p>
<blockquote>
<div><p><strong>Note:</strong> This resource establishes ownership of and the TLS settings for
a particular domain name. An API stage can be associated with the domain name using the <code class="docutils literal notranslate"><span class="pre">apigatewayv2.ApiMapping</span></code> resource.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name.</p></li>
<li><p><strong>domain_name_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The domain name configuration.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the domain name.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>domain_name_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an AWS-managed certificate that will be used by the endpoint for the domain name. AWS Certificate Manager is the only supported source.
Use the <cite>``acm.Certificate`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/acm_certificate.html">https://www.terraform.io/docs/providers/aws/r/acm_certificate.html</a>&gt;`_ resource to configure an ACM certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The endpoint type. Valid values: <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hosted_zone_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon Route 53 Hosted Zone ID of the endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Transport Layer Security (TLS) version of the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html">security policy</a> for the domain name. Valid values: <code class="docutils literal notranslate"><span class="pre">TLS_1_2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetDomainName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The target domain name.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.DomainName.api_mapping_selection_expression">
<code class="sig-name descname">api_mapping_selection_expression</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.DomainName.api_mapping_selection_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-mapping-selection-expressions">API mapping selection expression</a> for the domain name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.DomainName.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.DomainName.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the domain name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.DomainName.domain_name">
<code class="sig-name descname">domain_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.DomainName.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.DomainName.domain_name_configuration">
<code class="sig-name descname">domain_name_configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.DomainName.domain_name_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain name configuration.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of an AWS-managed certificate that will be used by the endpoint for the domain name. AWS Certificate Manager is the only supported source.
Use the <cite>``acm.Certificate`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/acm_certificate.html">https://www.terraform.io/docs/providers/aws/r/acm_certificate.html</a>&gt;`_ resource to configure an ACM certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The endpoint type. Valid values: <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hosted_zone_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon Route 53 Hosted Zone ID of the endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Transport Layer Security (TLS) version of the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html">security policy</a> for the domain name. Valid values: <code class="docutils literal notranslate"><span class="pre">TLS_1_2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetDomainName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The target domain name.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.DomainName.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.DomainName.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the domain name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.DomainName.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_mapping_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.DomainName.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DomainName resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_mapping_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-mapping-selection-expressions">API mapping selection expression</a> for the domain name.</p>
</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the domain name.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain name.</p></li>
<li><p><strong>domain_name_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The domain name configuration.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the domain name.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>domain_name_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificate_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of an AWS-managed certificate that will be used by the endpoint for the domain name. AWS Certificate Manager is the only supported source.
Use the <cite>``acm.Certificate`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/acm_certificate.html">https://www.terraform.io/docs/providers/aws/r/acm_certificate.html</a>&gt;`_ resource to configure an ACM certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endpoint_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The endpoint type. Valid values: <code class="docutils literal notranslate"><span class="pre">REGIONAL</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hosted_zone_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon Route 53 Hosted Zone ID of the endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Transport Layer Security (TLS) version of the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html">security policy</a> for the domain name. Valid values: <code class="docutils literal notranslate"><span class="pre">TLS_1_2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetDomainName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The target domain name.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.DomainName.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.DomainName.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.DomainName.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.DomainName.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Integration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">Integration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_handling_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">passthrough_behavior</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">payload_format_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_templates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_milliseconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration" title="Permalink to this definition">¶</a></dt>
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
<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.api_id">
<code class="sig-name descname">api_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.connection_id">
<code class="sig-name descname">connection_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC link for a private integration. Supported only for HTTP APIs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.connection_type">
<code class="sig-name descname">connection_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.connection_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the network connection to the integration endpoint. Valid values: <code class="docutils literal notranslate"><span class="pre">INTERNET</span></code>, <code class="docutils literal notranslate"><span class="pre">VPC_LINK</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">INTERNET</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.content_handling_strategy">
<code class="sig-name descname">content_handling_strategy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.content_handling_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>How to handle response payload content type conversions. Valid values: <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_BINARY</span></code>, <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_TEXT</span></code>. Supported only for WebSocket APIs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.credentials_arn">
<code class="sig-name descname">credentials_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.credentials_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The credentials required for the integration, if any.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the integration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.integration_method">
<code class="sig-name descname">integration_method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.integration_method" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration’s HTTP method. Must be specified if <code class="docutils literal notranslate"><span class="pre">integration_type</span></code> is not <code class="docutils literal notranslate"><span class="pre">MOCK</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.integration_response_selection_expression">
<code class="sig-name descname">integration_response_selection_expression</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.integration_response_selection_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions">integration response selection expression</a> for the integration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.integration_type">
<code class="sig-name descname">integration_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.integration_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration type of an integration.
Valid values: <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP</span></code>, <code class="docutils literal notranslate"><span class="pre">HTTP_PROXY</span></code>, <code class="docutils literal notranslate"><span class="pre">MOCK</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.integration_uri">
<code class="sig-name descname">integration_uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.integration_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI of the Lambda function for a Lambda proxy integration, when <code class="docutils literal notranslate"><span class="pre">integration_type</span></code> is <code class="docutils literal notranslate"><span class="pre">AWS_PROXY</span></code>.
For an <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.passthrough_behavior">
<code class="sig-name descname">passthrough_behavior</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.passthrough_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>The pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the <code class="docutils literal notranslate"><span class="pre">request_templates</span></code> attribute.
Valid values: <code class="docutils literal notranslate"><span class="pre">WHEN_NO_MATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">WHEN_NO_TEMPLATES</span></code>, <code class="docutils literal notranslate"><span class="pre">NEVER</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">WHEN_NO_MATCH</span></code>. Supported only for WebSocket APIs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.payload_format_version">
<code class="sig-name descname">payload_format_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.payload_format_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.proxy-format">format of the payload</a> sent to an integration. Valid values: <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">2.0</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">1.0</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.request_templates">
<code class="sig-name descname">request_templates</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.request_templates" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. Supported only for WebSocket APIs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.template_selection_expression">
<code class="sig-name descname">template_selection_expression</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.template_selection_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions">template selection expression</a> for the integration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Integration.timeout_milliseconds">
<code class="sig-name descname">timeout_milliseconds</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.timeout_milliseconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.Integration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_handling_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_response_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">passthrough_behavior</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">payload_format_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_templates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_milliseconds</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.Integration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Integration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.IntegrationResponse">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">IntegrationResponse</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_handling_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_response_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_templates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.IntegrationResponse" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Amazon API Gateway Version 2 integration response.
More information can be found in the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html">Amazon API Gateway Developer Guide</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>content_handling_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How to handle response payload content type conversions. Valid values: <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_BINARY</span></code>, <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_TEXT</span></code>.</p></li>
<li><p><strong>integration_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the <cite>``apigatewayv2.Integration`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration.html</a>&gt;`_.</p></li>
<li><p><strong>integration_response_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration response key.</p></li>
<li><p><strong>response_templates</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client.</p></li>
<li><p><strong>template_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions">template selection expression</a> for the integration response.</p>
</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.IntegrationResponse.api_id">
<code class="sig-name descname">api_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.IntegrationResponse.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.IntegrationResponse.content_handling_strategy">
<code class="sig-name descname">content_handling_strategy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.IntegrationResponse.content_handling_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>How to handle response payload content type conversions. Valid values: <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_BINARY</span></code>, <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_TEXT</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.IntegrationResponse.integration_id">
<code class="sig-name descname">integration_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.IntegrationResponse.integration_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the <cite>``apigatewayv2.Integration`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration.html</a>&gt;`_.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.IntegrationResponse.integration_response_key">
<code class="sig-name descname">integration_response_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.IntegrationResponse.integration_response_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The integration response key.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.IntegrationResponse.response_templates">
<code class="sig-name descname">response_templates</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.IntegrationResponse.response_templates" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.IntegrationResponse.template_selection_expression">
<code class="sig-name descname">template_selection_expression</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.IntegrationResponse.template_selection_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions">template selection expression</a> for the integration response.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.IntegrationResponse.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_handling_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_response_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_templates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.IntegrationResponse.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IntegrationResponse resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>content_handling_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How to handle response payload content type conversions. Valid values: <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_BINARY</span></code>, <code class="docutils literal notranslate"><span class="pre">CONVERT_TO_TEXT</span></code>.</p></li>
<li><p><strong>integration_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the <cite>``apigatewayv2.Integration`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration.html</a>&gt;`_.</p></li>
<li><p><strong>integration_response_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The integration response key.</p></li>
<li><p><strong>response_templates</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client.</p></li>
<li><p><strong>template_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions">template selection expression</a> for the integration response.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.IntegrationResponse.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.IntegrationResponse.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.IntegrationResponse.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.IntegrationResponse.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Model">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">Model</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model" title="Permalink to this definition">¶</a></dt>
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
<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Model.api_id">
<code class="sig-name descname">api_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Model.content_type">
<code class="sig-name descname">content_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The content-type for the model, for example, <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Model.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the model.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Model.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the model. Must be alphanumeric.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Model.schema">
<code class="sig-name descname">schema</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The schema for the model. This should be a <a class="reference external" href="https://tools.ietf.org/html/draft-zyp-json-schema-04">JSON schema draft 4</a> model.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.Model.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.Model.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Model.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Model.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Route">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">Route</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key_required</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorizer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">model_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operation_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_models</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_response_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Amazon API Gateway Version 2 route.
More information can be found in the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html">Amazon API Gateway Developer Guide</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>api_key_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether an API key is required for the route. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>authorization_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The authorization scopes supported by this route. The scopes are used with a JWT authorizer to authorize the method invocation.</p></li>
<li><p><strong>authorization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorization type for the route.
For WebSocket APIs, valid values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> for open access, <code class="docutils literal notranslate"><span class="pre">AWS_IAM</span></code> for using AWS IAM permissions, and <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code> for using a Lambda authorizer.
For HTTP APIs, valid values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> for open access, or <code class="docutils literal notranslate"><span class="pre">JWT</span></code> for using JSON Web Tokens.
Defaults to <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
<li><p><strong>authorizer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the <cite>``apigatewayv2.Authorizer`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer.html</a>&gt;`_ resource to be associated with this route, if the authorizationType is <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code>.</p></li>
<li><p><strong>model_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions">model selection expression</a> for the route.</p></li>
<li><p><strong>operation_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operation name for the route.</p></li>
<li><p><strong>request_models</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The request models for the route.</p></li>
<li><p><strong>route_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The route key for the route.</p></li>
<li><p><strong>route_response_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-response-selection-expressions">route response selection expression</a> for the route.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target for the route.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Route.api_id">
<code class="sig-name descname">api_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Route.api_key_required">
<code class="sig-name descname">api_key_required</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route.api_key_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether an API key is required for the route. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Route.authorization_scopes">
<code class="sig-name descname">authorization_scopes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route.authorization_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorization scopes supported by this route. The scopes are used with a JWT authorizer to authorize the method invocation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Route.authorization_type">
<code class="sig-name descname">authorization_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route.authorization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorization type for the route.
For WebSocket APIs, valid values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> for open access, <code class="docutils literal notranslate"><span class="pre">AWS_IAM</span></code> for using AWS IAM permissions, and <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code> for using a Lambda authorizer.
For HTTP APIs, valid values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> for open access, or <code class="docutils literal notranslate"><span class="pre">JWT</span></code> for using JSON Web Tokens.
Defaults to <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Route.authorizer_id">
<code class="sig-name descname">authorizer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route.authorizer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the <cite>``apigatewayv2.Authorizer`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer.html</a>&gt;`_ resource to be associated with this route, if the authorizationType is <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Route.model_selection_expression">
<code class="sig-name descname">model_selection_expression</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route.model_selection_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions">model selection expression</a> for the route.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Route.operation_name">
<code class="sig-name descname">operation_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route.operation_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The operation name for the route.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Route.request_models">
<code class="sig-name descname">request_models</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route.request_models" title="Permalink to this definition">¶</a></dt>
<dd><p>The request models for the route.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Route.route_key">
<code class="sig-name descname">route_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route.route_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The route key for the route.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Route.route_response_selection_expression">
<code class="sig-name descname">route_response_selection_expression</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route.route_response_selection_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-response-selection-expressions">route response selection expression</a> for the route.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Route.target">
<code class="sig-name descname">target</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route.target" title="Permalink to this definition">¶</a></dt>
<dd><p>The target for the route.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.Route.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key_required</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorizer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">model_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operation_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_models</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_response_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Route resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>api_key_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether an API key is required for the route. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>authorization_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The authorization scopes supported by this route. The scopes are used with a JWT authorizer to authorize the method invocation.</p></li>
<li><p><strong>authorization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorization type for the route.
For WebSocket APIs, valid values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> for open access, <code class="docutils literal notranslate"><span class="pre">AWS_IAM</span></code> for using AWS IAM permissions, and <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code> for using a Lambda authorizer.
For HTTP APIs, valid values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code> for open access, or <code class="docutils literal notranslate"><span class="pre">JWT</span></code> for using JSON Web Tokens.
Defaults to <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.</p></li>
<li><p><strong>authorizer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the <cite>``apigatewayv2.Authorizer`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_authorizer.html</a>&gt;`_ resource to be associated with this route, if the authorizationType is <code class="docutils literal notranslate"><span class="pre">CUSTOM</span></code>.</p></li>
<li><p><strong>model_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions">model selection expression</a> for the route.</p>
</p></li>
<li><p><strong>operation_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operation name for the route.</p></li>
<li><p><strong>request_models</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The request models for the route.</p></li>
<li><p><strong>route_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The route key for the route.</p></li>
<li><p><strong>route_response_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-route-response-selection-expressions">route response selection expression</a> for the route.</p>
</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target for the route.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.Route.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Route.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Route.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.RouteResponse">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">RouteResponse</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">model_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_models</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_response_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.RouteResponse" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Amazon API Gateway Version 2 route response.
More information can be found in the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html">Amazon API Gateway Developer Guide</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>model_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions">model selection expression</a> for the route response.</p>
</p></li>
<li><p><strong>response_models</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The response models for the route response.</p></li>
<li><p><strong>route_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the <cite>``apigatewayv2.Route`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route.html</a>&gt;`_.</p></li>
<li><p><strong>route_response_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The route response key.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.RouteResponse.api_id">
<code class="sig-name descname">api_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.RouteResponse.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.RouteResponse.model_selection_expression">
<code class="sig-name descname">model_selection_expression</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.RouteResponse.model_selection_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions">model selection expression</a> for the route response.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.RouteResponse.response_models">
<code class="sig-name descname">response_models</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.RouteResponse.response_models" title="Permalink to this definition">¶</a></dt>
<dd><p>The response models for the route response.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.RouteResponse.route_id">
<code class="sig-name descname">route_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.RouteResponse.route_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the <cite>``apigatewayv2.Route`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route.html</a>&gt;`_.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.RouteResponse.route_response_key">
<code class="sig-name descname">route_response_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.RouteResponse.route_response_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The route response key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.RouteResponse.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">model_selection_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">response_models</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_response_key</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.RouteResponse.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RouteResponse resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>model_selection_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions">model selection expression</a> for the route response.</p>
</p></li>
<li><p><strong>response_models</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The response models for the route response.</p></li>
<li><p><strong>route_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the <cite>``apigatewayv2.Route`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route.html">https://www.terraform.io/docs/providers/aws/r/apigatewayv2_route.html</a>&gt;`_.</p></li>
<li><p><strong>route_response_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The route response key.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.RouteResponse.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.RouteResponse.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.RouteResponse.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.RouteResponse.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Stage">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">Stage</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_log_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_deploy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_certificate_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_route_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stage_variables</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Amazon API Gateway Version 2 stage.
More information can be found in the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html">Amazon API Gateway Developer Guide</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_log_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings for logging access in this stage.
Use the <cite>``apigateway.Account`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/api_gateway_account.html">https://www.terraform.io/docs/providers/aws/r/api_gateway_account.html</a>&gt;`_ resource to configure <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#set-up-access-logging-permissions">permissions for CloudWatch Logging</a>.</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>auto_deploy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether updates to an API automatically trigger a new deployment. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>client_certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of a client certificate for the stage. Use the <cite>``apigateway.ClientCertificate`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/api_gateway_client_certificate.html">https://www.terraform.io/docs/providers/aws/r/api_gateway_client_certificate.html</a>&gt;`_ resource to configure a client certificate.
Supported only for WebSocket APIs.</p></li>
<li><p><strong>default_route_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default route settings for the stage.</p></li>
<li><p><strong>deployment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deployment identifier of the stage. Use the <code class="docutils literal notranslate"><span class="pre">apigatewayv2.Deployment</span></code> resource to configure a deployment.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the stage.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stage.</p></li>
<li><p><strong>route_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Route settings for the stage.</p></li>
<li><p><strong>stage_variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map that defines the stage variables for the stage.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the stage.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>access_log_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">destination_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the CloudWatch Logs log group to receive access logs. Any trailing <code class="docutils literal notranslate"><span class="pre">:*</span></code> is trimmed from the ARN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A single line <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#apigateway-cloudwatch-log-formats">format</a> of the access logs of data, as specified by <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-logging.html">selected $context variables</a>.</p></li>
</ul>
<p>The <strong>default_route_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataTraceEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether data trace logging is enabled for the default route. Affects the log entries pushed to Amazon CloudWatch Logs.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">detailedMetricsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether detailed metrics are enabled for the default route. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The logging level for the default route. Affects the log entries pushed to Amazon CloudWatch Logs.
Valid values: <code class="docutils literal notranslate"><span class="pre">ERROR</span></code>, <code class="docutils literal notranslate"><span class="pre">INFO</span></code>, <code class="docutils literal notranslate"><span class="pre">OFF</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">OFF</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingBurstLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The throttling burst limit for the default route.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingRateLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The throttling rate limit for the default route.</p></li>
</ul>
<p>The <strong>route_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataTraceEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether data trace logging is enabled for the route. Affects the log entries pushed to Amazon CloudWatch Logs.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">detailedMetricsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether detailed metrics are enabled for the route. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The logging level for the route. Affects the log entries pushed to Amazon CloudWatch Logs.
Valid values: <code class="docutils literal notranslate"><span class="pre">ERROR</span></code>, <code class="docutils literal notranslate"><span class="pre">INFO</span></code>, <code class="docutils literal notranslate"><span class="pre">OFF</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">OFF</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">route_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Route key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingBurstLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The throttling burst limit for the route.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingRateLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The throttling rate limit for the route.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Stage.access_log_settings">
<code class="sig-name descname">access_log_settings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.access_log_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings for logging access in this stage.
Use the <cite>``apigateway.Account`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/api_gateway_account.html">https://www.terraform.io/docs/providers/aws/r/api_gateway_account.html</a>&gt;`_ resource to configure <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#set-up-access-logging-permissions">permissions for CloudWatch Logging</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">destination_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the CloudWatch Logs log group to receive access logs. Any trailing <code class="docutils literal notranslate"><span class="pre">:*</span></code> is trimmed from the ARN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A single line <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#apigateway-cloudwatch-log-formats">format</a> of the access logs of data, as specified by <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-logging.html">selected $context variables</a>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Stage.api_id">
<code class="sig-name descname">api_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.api_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The API identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Stage.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the stage.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Stage.auto_deploy">
<code class="sig-name descname">auto_deploy</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.auto_deploy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether updates to an API automatically trigger a new deployment. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Stage.client_certificate_id">
<code class="sig-name descname">client_certificate_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.client_certificate_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of a client certificate for the stage. Use the <cite>``apigateway.ClientCertificate`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/api_gateway_client_certificate.html">https://www.terraform.io/docs/providers/aws/r/api_gateway_client_certificate.html</a>&gt;`_ resource to configure a client certificate.
Supported only for WebSocket APIs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Stage.default_route_settings">
<code class="sig-name descname">default_route_settings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.default_route_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The default route settings for the stage.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataTraceEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether data trace logging is enabled for the default route. Affects the log entries pushed to Amazon CloudWatch Logs.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">detailedMetricsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether detailed metrics are enabled for the default route. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The logging level for the default route. Affects the log entries pushed to Amazon CloudWatch Logs.
Valid values: <code class="docutils literal notranslate"><span class="pre">ERROR</span></code>, <code class="docutils literal notranslate"><span class="pre">INFO</span></code>, <code class="docutils literal notranslate"><span class="pre">OFF</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">OFF</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingBurstLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The throttling burst limit for the default route.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingRateLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The throttling rate limit for the default route.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Stage.deployment_id">
<code class="sig-name descname">deployment_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.deployment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The deployment identifier of the stage. Use the <code class="docutils literal notranslate"><span class="pre">apigatewayv2.Deployment</span></code> resource to configure a deployment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Stage.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the stage.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Stage.execution_arn">
<code class="sig-name descname">execution_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.execution_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN prefix to be used in an <cite>``lambda.Permission`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">source_arn</span></code> attribute
or in an <cite>``iam.Policy`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_policy.html">https://www.terraform.io/docs/providers/aws/r/iam_policy.html</a>&gt;`_ to authorize access to the <cite>``&#64;connections`</cite> API &lt;<a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html">https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html</a>&gt;`_.
See the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-control-access-iam.html">Amazon API Gateway Developer Guide</a> for details.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Stage.invoke_url">
<code class="sig-name descname">invoke_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.invoke_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to invoke the API pointing to the stage,
e.g. <code class="docutils literal notranslate"><span class="pre">wss://z4675bid1j.execute-api.eu-west-2.amazonaws.com/example-stage</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Stage.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the stage.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Stage.route_settings">
<code class="sig-name descname">route_settings</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.route_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Route settings for the stage.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataTraceEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether data trace logging is enabled for the route. Affects the log entries pushed to Amazon CloudWatch Logs.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">detailedMetricsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether detailed metrics are enabled for the route. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The logging level for the route. Affects the log entries pushed to Amazon CloudWatch Logs.
Valid values: <code class="docutils literal notranslate"><span class="pre">ERROR</span></code>, <code class="docutils literal notranslate"><span class="pre">INFO</span></code>, <code class="docutils literal notranslate"><span class="pre">OFF</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">OFF</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">route_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Route key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingBurstLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The throttling burst limit for the route.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingRateLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The throttling rate limit for the route.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Stage.stage_variables">
<code class="sig-name descname">stage_variables</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.stage_variables" title="Permalink to this definition">¶</a></dt>
<dd><p>A map that defines the stage variables for the stage.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.Stage.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the stage.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.Stage.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_log_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_deploy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_certificate_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_route_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">execution_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invoke_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stage_variables</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Stage resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_log_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Settings for logging access in this stage.
Use the <cite>``apigateway.Account`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/api_gateway_account.html">https://www.terraform.io/docs/providers/aws/r/api_gateway_account.html</a>&gt;`_ resource to configure <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#set-up-access-logging-permissions">permissions for CloudWatch Logging</a>.</p>
</p></li>
<li><p><strong>api_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API identifier.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the stage.</p></li>
<li><p><strong>auto_deploy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether updates to an API automatically trigger a new deployment. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>client_certificate_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of a client certificate for the stage. Use the <cite>``apigateway.ClientCertificate`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/api_gateway_client_certificate.html">https://www.terraform.io/docs/providers/aws/r/api_gateway_client_certificate.html</a>&gt;`_ resource to configure a client certificate.
Supported only for WebSocket APIs.</p></li>
<li><p><strong>default_route_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The default route settings for the stage.</p></li>
<li><p><strong>deployment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deployment identifier of the stage. Use the <code class="docutils literal notranslate"><span class="pre">apigatewayv2.Deployment</span></code> resource to configure a deployment.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the stage.</p></li>
<li><p><strong>execution_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ARN prefix to be used in an <cite>``lambda.Permission`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/lambda_permission.html">https://www.terraform.io/docs/providers/aws/r/lambda_permission.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">source_arn</span></code> attribute
or in an <cite>``iam.Policy`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/iam_policy.html">https://www.terraform.io/docs/providers/aws/r/iam_policy.html</a>&gt;`_ to authorize access to the <cite>``&#64;connections`</cite> API &lt;<a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html">https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html</a>&gt;`_.
See the <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-control-access-iam.html">Amazon API Gateway Developer Guide</a> for details.</p>
</p></li>
<li><p><strong>invoke_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to invoke the API pointing to the stage,
e.g. <code class="docutils literal notranslate"><span class="pre">wss://z4675bid1j.execute-api.eu-west-2.amazonaws.com/example-stage</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the stage.</p></li>
<li><p><strong>route_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Route settings for the stage.</p></li>
<li><p><strong>stage_variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map that defines the stage variables for the stage.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the stage.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>access_log_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">destination_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the CloudWatch Logs log group to receive access logs. Any trailing <code class="docutils literal notranslate"><span class="pre">:*</span></code> is trimmed from the ARN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A single line <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#apigateway-cloudwatch-log-formats">format</a> of the access logs of data, as specified by <a class="reference external" href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-logging.html">selected $context variables</a>.</p></li>
</ul>
<p>The <strong>default_route_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataTraceEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether data trace logging is enabled for the default route. Affects the log entries pushed to Amazon CloudWatch Logs.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">detailedMetricsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether detailed metrics are enabled for the default route. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The logging level for the default route. Affects the log entries pushed to Amazon CloudWatch Logs.
Valid values: <code class="docutils literal notranslate"><span class="pre">ERROR</span></code>, <code class="docutils literal notranslate"><span class="pre">INFO</span></code>, <code class="docutils literal notranslate"><span class="pre">OFF</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">OFF</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingBurstLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The throttling burst limit for the default route.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingRateLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The throttling rate limit for the default route.</p></li>
</ul>
<p>The <strong>route_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataTraceEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether data trace logging is enabled for the route. Affects the log entries pushed to Amazon CloudWatch Logs.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">detailedMetricsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether detailed metrics are enabled for the route. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loggingLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The logging level for the route. Affects the log entries pushed to Amazon CloudWatch Logs.
Valid values: <code class="docutils literal notranslate"><span class="pre">ERROR</span></code>, <code class="docutils literal notranslate"><span class="pre">INFO</span></code>, <code class="docutils literal notranslate"><span class="pre">OFF</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">OFF</span></code>. Supported only for WebSocket APIs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">route_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Route key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingBurstLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The throttling burst limit for the route.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">throttlingRateLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The throttling rate limit for the route.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.Stage.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.Stage.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.Stage.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.VpcLink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.apigatewayv2.</code><code class="sig-name descname">VpcLink</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.VpcLink" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Amazon API Gateway Version 2 VPC Link.</p>
<blockquote>
<div><p><strong>Note:</strong> Amazon API Gateway Version 2 VPC Links enable private integrations that connect HTTP APIs to private resources in a VPC.
To enable private integration for REST APIs, use the Amazon API Gateway Version 1 VPC Link <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/api_gateway_vpc_link.html">resource</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the VPC Link.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Security group IDs for the VPC Link.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Subnet IDs for the VPC Link.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the VPC Link.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.VpcLink.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.VpcLink.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC Link ARN.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.VpcLink.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.VpcLink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the VPC Link.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.VpcLink.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.VpcLink.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Security group IDs for the VPC Link.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.VpcLink.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.VpcLink.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnet IDs for the VPC Link.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.apigatewayv2.VpcLink.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.apigatewayv2.VpcLink.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the VPC Link.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.VpcLink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.VpcLink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VpcLink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC Link ARN.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the VPC Link.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Security group IDs for the VPC Link.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Subnet IDs for the VPC Link.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the VPC Link.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.apigatewayv2.VpcLink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.VpcLink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.apigatewayv2.VpcLink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.apigatewayv2.VpcLink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
