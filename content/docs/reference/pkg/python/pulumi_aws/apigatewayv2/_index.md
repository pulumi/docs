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

</div>
